"""Pull the benchmark runs out of Prometheus into a single JSON file.

    python export_replay.py            # ramp runs   -> bench/replay.json
    python export_replay.py --runs A1,A2,A3,B1,B2,B3,C1,C2,C3 \
        --out replay-step.json --scenario "instant 4x step at minute 5, held 4 min"

Prometheus keeps 15 days. After that these windows are gone for good, and with
them any chance of rebuilding the comparison. This script freezes them into the
repo so the visualisation keeps working long after the cluster is switched off.

Every series here was recorded during a real run. Nothing is generated.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent
PROM = "http://localhost:9090"
STEP = 20  # seconds — matches what analyze.py uses, so the numbers agree


def series(query: str, start: int, end: int) -> dict[int, float]:
    """One Prometheus series over a window, keyed by seconds since run start."""
    r = requests.get(f"{PROM}/api/v1/query_range", params={
        "query": query, "start": start, "end": end, "step": STEP}, timeout=30)
    res = r.json().get("data", {}).get("result", [])
    if not res:
        return {}
    return {int(t) - start: float(v) for t, v in res[0]["values"]}


# Run-name prefix -> which arm it is. The prefix is the only label a run
# carries: `make bench RUN=C1` writes bench/C1.json and nothing else records
# that C meant MODE=hpa-floor. Keep this table in step with the dashboard's.
ARM_OF_PREFIX = {"A": "baseline", "B": "predictive", "C": "floor"}


def decisions(start: int, end: int) -> list[dict]:
    """What the controller predicted during this window, from its own log.

    Only the B and C runs have these — the baseline has no forecaster running.
    This is the series that makes the point: it is the model's forecast,
    timestamped, next to what actually happened.
    """
    path = ROOT / "logs/decisions.csv"
    if not path.exists():
        return []
    out = []
    with open(path) as fh:
        for row in csv.DictReader(fh):
            try:
                ts = int(datetime.fromisoformat(row["ts"]).timestamp())
            except (ValueError, KeyError):
                continue
            if not (start <= ts <= end):
                continue
            try:
                out.append({
                    "t": ts - start,
                    "now": float(row["current_rate"]),
                    "pred": float(row["predicted"]),
                    "pods_now": int(row["pods_now"]),
                    "pods_target": int(row["pods_target"]),
                    "action": row["action"],
                })
            except (ValueError, TypeError):
                continue  # 'hold' rows have empty numeric fields
    return out


def export_run(name: str) -> dict | None:
    s, e = ROOT / f"bench/{name}.start", ROOT / f"bench/{name}.end"
    j = ROOT / f"bench/{name}.json"
    if not (s.exists() and e.exists() and j.exists()):
        print(f"  {name}: missing files, skipped")
        return None

    start, end = int(s.read_text()), int(e.read_text())
    rate = series('sum(rate(http_requests_total{handler="/work"}[1m]))', start, end)
    pods = series('kube_deployment_status_replicas_available'
                  '{deployment="traffic-app"}', start, end)
    # p99 from the APP's own histogram, so it is a value over time rather than
    # the single whole-run figure k6 reports at the end.
    p99 = series('histogram_quantile(0.99, sum by (le) (rate('
                 'http_request_duration_seconds_bucket{handler="/work"}[1m])))',
                 start, end)

    summary = json.loads(j.read_text())["metrics"]
    d = summary["http_req_duration"]["values"]

    grid = sorted(set(rate) | set(pods) | set(p99))
    if not grid:
        print(f"  {name}: no data in Prometheus (expired?), skipped")
        return None

    return {
        "name": name,
        "arm": ARM_OF_PREFIX.get(name[0], "baseline"),
        "t": grid,
        "rate": [round(rate.get(t, float("nan")), 2) if t in rate else None for t in grid],
        "pods": [int(pods[t]) if t in pods else None for t in grid],
        # milliseconds, so the page never has to do unit maths
        "p99": [round(p99[t] * 1000) if t in p99 and p99[t] == p99[t] else None
                for t in grid],
        "decisions": decisions(start, end),
        "summary": {
            "p50": round(d["p(50)"]), "p95": round(d["p(95)"]),
            "p99": round(d["p(99)"]), "max": round(d["max"]),
            "reqs": int(summary["http_reqs"]["values"]["count"]),
            "pod_seconds": round(sum(v for v in pods.values()) * STEP),
        },
        "started_utc": datetime.fromtimestamp(start, timezone.utc).isoformat(timespec="seconds"),
    }


def main(runs: list[str], out_name: str, scenario: str):
    data = [r for r in (export_run(n) for n in runs) if r]
    if not data:
        raise SystemExit("nothing exported — is `make forward-prom` running?")

    out = ROOT / "bench" / out_name
    out.write_text(json.dumps({
        "step_seconds": STEP,
        "scenario": scenario,
        "runs": data,
    }, indent=1))
    for r in data:
        print(f"  {r['name']:<5} {len(r['t']):>3} samples  "
              f"p99 {r['summary']['p99']:>4}ms  "
              f"{r['summary']['pod_seconds']:>5} pod-s  "
              f"{len(r['decisions']):>3} decisions")
    print(f"\n  wrote {out.relative_to(ROOT)} ({out.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Freeze benchmark runs into JSON.")
    ap.add_argument("--runs", default="A1r,A2r,A3r,B1r,B2r,B3r")
    ap.add_argument("--out", default="replay.json")
    ap.add_argument("--scenario",
                    default="ramp 20 -> 80 req/s over 6 min, hold 4 min, ramp down",
                    help="one line describing the load profile, shown in the UI")
    a = ap.parse_args()
    main(a.runs.split(","), a.out, a.scenario)
