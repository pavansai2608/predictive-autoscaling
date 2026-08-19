"""Train the chosen model on ALL data and save it for the controller.

    python src/train_final.py

The backtest answers "does this work?" using held-out time. Once that question
is settled there is no reason to keep throwing away the most recent data - the
model that goes live is retrained on everything, which is also the freshest
picture of how the service currently behaves.

Saves the fitted model, the exact feature list, and the horizon together in one
file. Keeping them together matters: a model fed columns in a different order,
or asked for a horizon it was not trained on, fails silently rather than
loudly.
"""

from __future__ import annotations

import sys
from pathlib import Path

import joblib

sys.path.insert(0, str(Path(__file__).resolve().parent))

import config as C
import features as F
import models as M

ROOT = Path(__file__).resolve().parent.parent


def main(horizon: int = C.HORIZON_STEPS):
    raw = F.load_series(str(ROOT / C.DATA_FILE))
    table = F.usable(F.build_table(raw, horizon=horizon))
    cols = F.feature_columns(table)

    print(f"training on {len(table):,} rows, {len(cols)} features "
          f"(backend: {M.BACKEND}, horizon {horizon} steps)")

    model = M.GBM(quantile=C.QUANTILE).fit(table, table["target"], cols)

    (ROOT / "models").mkdir(exist_ok=True)
    out = ROOT / C.MODEL_FILE
    joblib.dump({"model": model,
                 "features": cols,
                 "horizon": horizon,
                 "quantile": C.QUANTILE,
                 "backend": M.BACKEND,
                 "trained_rows": len(table)}, out)

    print(f"saved -> {out}")


if __name__ == "__main__":
    main()
