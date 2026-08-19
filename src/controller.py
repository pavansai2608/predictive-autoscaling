"""The predictive autoscaler. This is the file that makes the project a system.

    CAPACITY_PER_POD=120 python src/controller.py

Every 30 seconds: read live traffic -> forecast H steps ahead -> convert to a
pod count -> apply it to the deployment. Then log what it did and why.

The safety rules below are not decoration. A model can be wrong, and the
difference between a demo and something worth showing an engineer is whether
you planned for that. AWS runs predictive scaling ALONGSIDE reactive policies
rather than replacing them, for exactly this reason - when this controller
declines to act, the reactive HPA is the net underneath.

Ctrl+C to stop. Stopping the controller does not revert anything; pods stay
where they are until the HPA or you move them.
"""

from __future__ import annotations

import csv
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
from kubernetes import client, config as kube_config

sys.path.insert(0, str(Path(__file__).resolve().parent))

import config as C
import live

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs/decisions.csv"

# --- knobs -------------------------------------------------------------------
DEPLOYMENT = os.getenv("DEPLOYMENT", "traffic-app")
NAMESPACE = os.getenv("NAMESPACE", "default")
INTERVAL_S = int(os.getenv("INTERVAL_S", "30"))

# Requests/second one pod serves comfortably. MEASURED 2026-08-19 with
# `make capacity` against a single replica (HPA deleted), stepping the arrival
# rate 4 -> 28 req/s:
#
#     offered   served   p95     cpu
#        12      12.0     95ms   0.35
#        16      16.0     95ms   0.40   <- pinned at the 400m limit
#        20      20.1     95ms   0.40   <- last flat step
#        24      24.1    381ms   0.40   <- knee: 4x latency, no more throughput
#
# So 20, not the 120 this used to default to. A wrong value here makes every
# decision wrong in the same direction and is invisible in the forecast
# metrics — the forecast stays correct while the pod count silently does not.
# Re-measure if WORK_MS or the CPU limit in k8s/deployment.yaml changes.
CAPACITY_PER_POD = float(os.getenv("CAPACITY_PER_POD", "20"))

HEADROOM = float(os.getenv("HEADROOM", "1.1"))
MIN_PODS = int(os.getenv("MIN_PODS", "2"))
MAX_PODS = int(os.getenv("MAX_PODS", "20"))

# Scale-down is capped at one pod per cycle; scale-up is uncapped. Deliberately
# asymmetric, and for the same reason the model targets q=0.90: being late to
# add capacity costs users, being slow to remove it costs pennies.
MAX_SCALE_DOWN_PER_CYCLE = 1


def load_bundle():
    path = ROOT / C.MODEL_FILE
    if not path.exists():
        sys.exit(f"ERROR: {path} not found. Run: python src/train_final.py")
    return joblib.load(path)


def k8s_api():
    # Loaded from ~/.kube/config because this runs on the laptop, not inside a
    # pod. In-cluster it would be load_incluster_config() plus a ServiceAccount.
    kube_config.load_kube_config()
    return client.AppsV1Api()


def current_replicas(api) -> int:
    return int(api.read_namespaced_deployment_scale(DEPLOYMENT, NAMESPACE).spec.replicas or 0)


def set_replicas(api, n: int):
    api.patch_namespaced_deployment_scale(
        DEPLOYMENT, NAMESPACE, {"spec": {"replicas": int(n)}}
    )


def log_row(**kw):
    LOG.parent.mkdir(exist_ok=True)
    new = not LOG.exists()
    with open(LOG, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "ts", "current_rate", "predicted", "pods_now", "pods_target",
            "action", "reason"])
        if new:
            w.writeheader()
        w.writerow(kw)


def main():
    bundle = load_bundle()
    model, feats, horizon = bundle["model"], bundle["features"], bundle["horizon"]
    api = k8s_api()

    print(f"predictive autoscaler running\n"
          f"  deployment      : {DEPLOYMENT} (ns {NAMESPACE})\n"
          f"  horizon         : {horizon} steps = {horizon * C.STEP_SECONDS}s ahead\n"
          f"  capacity/pod    : {CAPACITY_PER_POD:g} req/s   headroom {HEADROOM:g}\n"
          f"  bounds          : {MIN_PODS}-{MAX_PODS} pods\n"
          f"  logging to      : {LOG}\n")

    recent_max = 0.0

    while True:
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        pods_now = -1
        try:
            pods_now = current_replicas(api)
            df = live.fetch_recent()
            row, now_rate = live.latest_feature_row(df, horizon)

            # ---- refuse to act on bad input --------------------------------
            if row is None or df.empty:
                raise ValueError("no data from Prometheus")

            X = row.reindex(columns=feats)
            pred = float(model.predict(X)[0])

            recent_max = max(recent_max * 0.99, float(df["y"].tail(240).max()))

            if not np.isfinite(pred) or pred < 0:
                reason = f"prediction not usable ({pred})"
                print(f"  {stamp}  HOLD  {reason}")
                log_row(ts=stamp, current_rate=round(now_rate, 3), predicted=pred,
                        pods_now=pods_now, pods_target=pods_now,
                        action="hold", reason=reason)
                time.sleep(INTERVAL_S)
                continue

            if recent_max > 0 and pred > 10 * recent_max:
                # An absurd forecast is more likely a broken feature row than a
                # real 10x event. Hand control back to the HPA rather than
                # launching twenty pods on a bad number.
                reason = f"prediction {pred:.1f} > 10x recent max {recent_max:.1f}"
                print(f"  {stamp}  HOLD  {reason}")
                log_row(ts=stamp, current_rate=round(now_rate, 3), predicted=round(pred, 3),
                        pods_now=pods_now, pods_target=pods_now,
                        action="hold", reason=reason)
                time.sleep(INTERVAL_S)
                continue

            # ---- forecast -> pods ------------------------------------------
            want = int(np.clip(math.ceil(pred * HEADROOM / CAPACITY_PER_POD),
                               MIN_PODS, MAX_PODS))

            if want < pods_now - MAX_SCALE_DOWN_PER_CYCLE:
                # Damping. Without it a noisy forecast makes pods flap up and
                # down every cycle, which looks broken and thrashes the app.
                want = pods_now - MAX_SCALE_DOWN_PER_CYCLE
                note = "damped"
            else:
                note = "ok"

            if want == pods_now:
                action, reason = "none", note
            else:
                set_replicas(api, want)
                action = "scale_up" if want > pods_now else "scale_down"
                reason = note

            print(f"  {stamp}  now={now_rate:7.2f}  pred={pred:7.2f}  "
                  f"pods {pods_now}->{want}  {action}")
            log_row(ts=stamp, current_rate=round(now_rate, 3), predicted=round(pred, 3),
                    pods_now=pods_now, pods_target=want, action=action, reason=reason)

        except Exception as e:
            reason = f"{type(e).__name__}: {e}"
            print(f"  {stamp}  HOLD  {reason}")
            log_row(ts=stamp, current_rate="", predicted="", pods_now=pods_now,
                    pods_target=pods_now, action="hold", reason=reason)

        time.sleep(INTERVAL_S)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nstopped. Pods left as-is; re-enable the HPA if you want "
              "reactive scaling back.")
