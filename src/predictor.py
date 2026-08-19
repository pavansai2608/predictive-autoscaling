"""Watch the live traffic and print a forecast. Changes nothing.

    python src/predictor.py

Run this BEFORE the controller. It exercises the whole inference path -
Prometheus -> features -> model -> a number - while being completely harmless,
so you can sanity-check the predictions against reality with your own eyes
before letting them move pods around.

What to look for while a k6 ramp climbs: the predicted value should lead the
current one, not echo it. If prediction simply mirrors "now", the model is
behaving like the naive baseline and something upstream is wrong.

Ctrl+C to stop.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

import joblib
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

import config as C
import live

ROOT = Path(__file__).resolve().parent.parent
INTERVAL_S = 30


def load_bundle():
    path = ROOT / C.MODEL_FILE
    if not path.exists():
        sys.exit(f"ERROR: {path} not found. Run: python src/train_final.py")
    b = joblib.load(path)
    print(f"loaded model: backend={b['backend']}  horizon={b['horizon']} steps "
          f"({b['horizon'] * C.STEP_SECONDS}s)  q={b['quantile']}  "
          f"trained on {b['trained_rows']:,} rows\n")
    return b


def main():
    bundle = load_bundle()
    model, feats, horizon = bundle["model"], bundle["features"], bundle["horizon"]
    ahead_s = horizon * C.STEP_SECONDS

    while True:
        try:
            df = live.fetch_recent()
            row, now_rate = live.latest_feature_row(df, horizon)

            if row is None:
                print("  no data from Prometheus (is `make forward-prom` running?)")
            else:
                # Reindex to the training feature order. Columns arriving in a
                # different order is a silent, catastrophic failure mode - the
                # model would read lag_1 as roll_std_240 and never complain.
                X = row.reindex(columns=feats)
                pred = float(np.clip(model.predict(X)[0], 0, None))
                arrow = "UP  " if pred > now_rate * 1.1 else (
                        "DOWN" if pred < now_rate * 0.9 else "flat")
                print(f"  {row['ts'].iloc[0]:%H:%M:%S}  now={now_rate:7.2f} req/s   "
                      f"predicted(+{ahead_s}s)={pred:7.2f}   {arrow}")

        except Exception as e:
            print(f"  [skip] {type(e).__name__}: {e}")

        time.sleep(INTERVAL_S)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nstopped.")
