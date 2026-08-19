"""Run the whole evaluation.

    python src/backtest.py
    python src/backtest.py --horizon 8        # override the horizon in steps

Reads data/traffic.parquet, builds features, walks forward through time
scoring every model against the baselines, writes outputs/results.csv and
outputs/forecast.png.

Read the table from the top: lowest COST wins. If a baseline wins, that is a
real finding and you report it - a project that honestly says "seasonal naive
was hard to beat, and here is why" is worth more than one that hides it.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

import config as C
import evaluate as ev
import features as F
import models as M

ROOT = Path(__file__).resolve().parent.parent
C_ACTUAL = "#52514e"
C_MODEL = "#2a78d6"
C_BASE = "#eb6834"


def main(horizon: int) -> pd.DataFrame:
    print(f"\nbackend: {M.BACKEND}   horizon: {horizon} steps "
          f"({horizon * C.STEP_SECONDS}s ahead)\n")

    # ---- 1. data ------------------------------------------------------------
    path = ROOT / C.DATA_FILE
    if not path.exists():
        sys.exit(f"ERROR: {path} not found. Run collect.py first.")

    raw = F.load_series(str(path))
    span_h = (raw["ts"].max() - raw["ts"].min()).total_seconds() / 3600
    print(f"[1/4] {len(raw):,} rows  |  {span_h:.1f} hours  "
          f"|  {raw['ts'].min():%Y-%m-%d %H:%M} -> {raw['ts'].max():%H:%M} UTC")
    print(f"      traffic: min {raw['y'].min():.2f}  mean {raw['y'].mean():.2f}  "
          f"max {raw['y'].max():.2f} req/s")

    if span_h < 3:
        print("\n  ! Only a few hours of data. The backtest will run, but the "
              "\n    seasonal features have little to learn from. Collect more "
              "\n    and re-run for numbers you would put on a resume.\n")

    # ---- 2. features --------------------------------------------------------
    table = F.usable(F.build_table(raw, horizon=horizon))
    cols = F.feature_columns(table)
    print(f"[2/4] {len(cols)} features, {len(table):,} usable rows")
    if len(table) < 300:
        sys.exit("ERROR: not enough usable rows to evaluate. Collect more data.")

    # ---- 3. walk forward ----------------------------------------------------
    folds = ev.rolling_origin_folds(len(table), gap=horizon)
    if not folds:
        sys.exit("ERROR: dataset too short to build even one fold.")
    print(f"[3/4] rolling-origin backtest, {len(folds)} fold(s)")

    rows: list[dict] = []
    last_preds: dict[str, np.ndarray] = {}
    last_test: pd.DataFrame | None = None
    importance: pd.DataFrame | None = None

    for i, (train_end, test_start, test_end) in enumerate(folds, 1):
        train = table.iloc[:train_end]
        test = table.iloc[test_start:test_end]
        print(f"      fold {i}: train {len(train):>6,} rows | test {len(test):>5,} rows")

        for model in M.ladder():
            if isinstance(model, M.GBM):
                model.fit(train, train["target"], cols)
                if i == len(folds) and model.quantile is None:
                    imp = model.importance()
                    importance = imp if not imp.empty else importance

            pred = np.clip(model.predict(test), 0, None)
            s = ev.score(test["target"].to_numpy(), pred)
            s.update(model=model.name, fold=i)
            rows.append(s)

            if i == len(folds):
                last_preds[model.name] = pred

        if i == len(folds):
            last_test = test

    # ---- 4. report ----------------------------------------------------------
    print("\n[4/4] results — averaged across folds, ranked by COST\n")
    table_out = ev.summarise(rows)

    disp = table_out.copy()
    if "seasonal_naive" in disp.index:
        base = disp.loc["seasonal_naive", "cost"]
        disp["vs_baseline_%"] = (1 - disp["cost"] / base) * 100

    with pd.option_context("display.width", 200, "display.max_columns", 20):
        print(disp.round(2).to_string())

    print(f"\n  cost = {C.COST_UNDER:g} x under-provisioning + {C.COST_OVER:g} x over-provisioning"
          "\n  under / over = summed shortfall and surplus across the test window"
          "\n  vs_baseline_% = cost reduction against seasonal naive (higher is better)")

    (ROOT / "outputs").mkdir(exist_ok=True)
    table_out.to_csv(ROOT / C.RESULTS_FILE)
    pd.DataFrame(rows).to_csv(ROOT / "outputs/results_by_fold.csv", index=False)

    if importance is not None and not importance.empty:
        print("\n  top features:")
        for _, r in importance.head(8).iterrows():
            print(f"    {r['feature']:<22} {r['gain']:>14,.0f}")
        importance.to_csv(ROOT / "outputs/feature_importance.csv", index=False)

    if last_test is not None and last_preds:
        _plot(last_test, last_preds, horizon)

    print(f"\n  wrote results and chart to {ROOT / 'outputs'}\n")
    return table_out


def _plot(test: pd.DataFrame, preds: dict, horizon: int):
    t = test["ts"]
    fig, ax = plt.subplots(figsize=(13, 5))
    ax.plot(t, test["target"], color=C_ACTUAL, lw=1.5, label="actual", zorder=3)

    for name, style in [("seasonal_naive", dict(color=C_BASE, lw=1.3, alpha=0.9)),
                        (f"gbm_q{C.QUANTILE:g}", dict(color=C_MODEL, lw=1.8))]:
        if name in preds:
            ax.plot(t, preds[name], label=name, zorder=2, **style)

    ax.set_title(f"{horizon * C.STEP_SECONDS}s-ahead forecast — final backtest fold",
                 fontsize=12)
    ax.set_ylabel("requests / second")
    ax.grid(alpha=0.25, lw=0.6)
    ax.legend(frameon=False, ncols=3)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(ROOT / C.PLOT_FILE, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Backtest the traffic forecaster.")
    ap.add_argument("--horizon", type=int, default=C.HORIZON_STEPS,
                    help=f"steps ahead to predict (default {C.HORIZON_STEPS}"
                         f" = {C.HORIZON_STEPS * C.STEP_SECONDS}s)")
    main(ap.parse_args().horizon)
