"""Retrain on fresh history — but only promote a model that is actually better.

    python retrain.py            # check, and replace the live model if it wins
    python retrain.py --dry-run  # score both, change nothing
    python retrain.py --force    # promote regardless (use when you know why)

Traffic patterns drift. A model trained in August is answering August's question,
and nothing in the system would tell you when that stops being the right one —
the forecast keeps looking reasonable while quietly getting worse. That is the
same class of silent failure as the train/serve bugs, and it needs the same
answer: measure, do not assume.

WHY THIS IS NOT JUST `train_final.py` ON A TIMER:

A scheduled retrain that always overwrites is a scheduled way to ship a worse
model. Fresh data can be worse data — a stretch where the laptop slept, or where
a benchmark run replaced the normal traffic pattern with a 20-minute square wave.
Both happened during this project.

So this script scores both models on the data collected SINCE the champion was
trained — rows neither has ever seen — and promotes only on a real improvement.
The previous model is kept, so a bad promotion is one `mv` away from undone.

That unseen-data split is the part that is easy to get wrong. Scoring a model on
history it was trained on flatters it enormously: the first version of this file
reported the champion at cost 2,003 against a candidate's 4,299, which measured
nothing except that one of them had already been shown the answers.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import config as C          # noqa: E402
import evaluate as ev       # noqa: E402
import features as F        # noqa: E402
import models as M          # noqa: E402

LIVE = ROOT / C.MODEL_FILE
PREV = ROOT / "models/forecaster.prev.joblib"
HISTORY = ROOT / "models/retrain_history.jsonl"

# How much better the candidate must be before it replaces the champion.
# Not zero: fold-to-fold noise on this data is around 0.3 on a cost of ~4,300,
# so a 1% swing is indistinguishable from luck. Demanding 2% means a promotion
# reflects a real change in the traffic, not a coin flip.
MIN_IMPROVEMENT = 0.02


# The champion must be judged only on rows it has never seen. Anything less
# than this many is not a measurement, it is noise — 480 steps is two full
# traffic cycles at 15s per step.
MIN_FRESH_ROWS = 2 * C.STEPS_PER_CYCLE


def cost_of(model, test, cols) -> float:
    """Cost of one model on one held-out slice. Lower is better."""
    pred = np.clip(model.predict(test[cols] if not isinstance(model, M.GBM) else test),
                   0, None)
    return ev.score(test["target"].to_numpy(), pred)["cost"]


def main(dry_run: bool, force: bool) -> int:
    if not (ROOT / C.DATA_FILE).exists():
        sys.exit(f"no {C.DATA_FILE} — run collect.py first")

    raw = F.load_series(str(ROOT / C.DATA_FILE))
    table = F.usable(F.build_table(raw, horizon=C.HORIZON_STEPS))
    cols = F.feature_columns(table)
    hours = (raw["ts"].max() - raw["ts"].min()).total_seconds() / 3600
    print(f"  data      : {len(table):,} usable rows, {hours:.1f} h "
          f"({raw['ts'].min():%Y-%m-%d %H:%M} -> {raw['ts'].max():%m-%d %H:%M} UTC)")

    bundle = joblib.load(LIVE) if LIVE.exists() else None

    # ---- find the data the champion has never seen -------------------------
    #
    # This is the whole design. A model trained on all of history scores
    # brilliantly on all of history, because it is being asked questions it
    # already has the answers to. Comparing that against a candidate fitted
    # honestly on a subset guarantees the champion "wins" forever and the gate
    # never opens. Measured before this was fixed: champion 2,003 vs candidate
    # 4,299, which said nothing about either model.
    #
    # So: split at the champion's training cutoff. Everything after it is fresh.
    if bundle is None:
        print("  champion  : none — training the first model")
        fresh = table.iloc[0:0]
    elif "trained_through" not in bundle:
        print("  champion  : bundle predates trained_through; cannot identify unseen "
              "rows, so no fair comparison is possible. Re-run train_final.py once.")
        return 1
    else:
        cutoff = pd.Timestamp(bundle["trained_through"])
        fresh = table[table["ts"] > cutoff]
        print(f"  champion  : trained through {cutoff:%Y-%m-%d %H:%M} UTC "
              f"({bundle['trained_rows']:,} rows)")
        print(f"  fresh data: {len(fresh):,} rows it has never seen")

    if bundle is not None and len(fresh) < MIN_FRESH_ROWS:
        print(f"  verdict   : need {MIN_FRESH_ROWS:,} unseen rows to judge, "
              f"have {len(fresh):,}. Collect more, then re-run.")
        print("  kept the current model")
        return 0

    if bundle is not None and bundle["features"] != cols:
        print("  champion  : feature set differs — not comparable, promoting on structure")
        live_cost, cand_cost = float("inf"), 0.0
    else:
        # Candidate learns ONLY from what came before the fresh window, so both
        # models are answering questions neither has seen.
        past = table[table["ts"] <= pd.Timestamp(bundle["trained_through"])] if bundle is not None else table
        candidate = M.GBM(quantile=C.QUANTILE).fit(past, past["target"], cols)
        cand_cost = cost_of(candidate, fresh, cols)
        live_cost = cost_of(bundle["model"], fresh, cols) if bundle else float("inf")
        print(f"  candidate : cost {cand_cost:,.0f}  (on the fresh window)")
        if bundle:
            print(f"  champion  : cost {live_cost:,.0f}  (same window, never trained on it)")

    # ---- decide ------------------------------------------------------------
    if live_cost == float("inf"):
        gain, promote, why = 1.0, True, "no comparable champion"
    else:
        gain = (live_cost - cand_cost) / live_cost
        promote = gain >= MIN_IMPROVEMENT
        why = (f"{gain:+.1%} vs champion, "
               f"{'above' if promote else 'below'} the {MIN_IMPROVEMENT:.0%} bar")
    print(f"  verdict   : {why}")

    if force and not promote:
        promote, why = True, why + " (forced)"

    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    HISTORY.parent.mkdir(exist_ok=True)
    with open(HISTORY, "a") as fh:
        fh.write(json.dumps({"ts": stamp, "rows": len(table), "hours": round(hours, 1),
                             "candidate_cost": round(cand_cost, 1),
                             "champion_cost": None if live_cost == float("inf") else round(live_cost, 1),
                             "promoted": bool(promote and not dry_run),
                             "reason": why}) + "\n")

    if dry_run:
        print("  --dry-run : nothing written")
        return 0
    if not promote:
        print("  kept the current model")
        return 0

    # Retrain on EVERYTHING before promoting. The fold scores answered "is this
    # recipe better"; the model that ships should still see all the data.
    final = M.GBM(quantile=C.QUANTILE).fit(table, table["target"], cols)
    if LIVE.exists():
        shutil.copy2(LIVE, PREV)
        print(f"  previous model kept at {PREV.name}")
    # trained_through must be written here too, or the NEXT run has no way to
    # tell which rows this model has seen and the gate jams shut permanently.
    joblib.dump({"model": final, "features": cols, "horizon": C.HORIZON_STEPS,
                 "quantile": C.QUANTILE, "backend": M.BACKEND,
                 "trained_rows": len(table),
                 "trained_through": table["ts"].max().isoformat()}, LIVE)
    print(f"  PROMOTED  -> {LIVE.relative_to(ROOT)}")
    print("  restart controller.py to pick it up (the bundle is loaded once, at start)")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Retrain, and promote only if better.")
    ap.add_argument("--dry-run", action="store_true", help="score both, write nothing")
    ap.add_argument("--force", action="store_true", help="promote even if not better")
    a = ap.parse_args()
    raise SystemExit(main(a.dry_run, a.force))
