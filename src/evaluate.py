"""The scoreboard. Written before the models, on purpose.

If you build a model first and design the metric afterwards, you will - without
meaning to - pick the metric that flatters what you already built. Fixing the
rules while there is no result to protect is what makes every later number
trustworthy.

Two things here that most portfolio projects lack:

  1. ROLLING-ORIGIN BACKTESTING. Not one split - several, walking forward
     through time. One split can get lucky; several tell you whether the model
     works in general or worked once.

  2. A COST METRIC. MAE says how wrong the forecast was. It does not say
     whether the mistakes hurt. Being short of capacity causes an outage;
     having spare capacity costs a little money. Scoring those separately is
     the whole reason this project has a point.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

import config as C


def rolling_origin_folds(n_rows: int, n_folds: int = C.N_FOLDS,
                         test_steps: int = C.TEST_STEPS,
                         gap: int = C.HORIZON_STEPS) -> list[tuple[int, int, int]]:
    """Produce (train_end, test_start, test_end) row indices, walking forward.

        fold 1: train [=====]      test [--]
        fold 2: train [=======]    test [--]
        fold 3: train [=========]  test [--]

    Training always ends before testing begins, and there is no shuffling
    anywhere - shuffling would let the model learn from its own future.

    `gap` leaves a deliberate hole equal to the horizon: at prediction time you
    genuinely would not yet know the outcome of the most recent H steps.

    Folds are trimmed automatically if the dataset is short, so a first run on
    a few hours of data still produces an honest (if smaller) evaluation
    instead of crashing.
    """
    folds: list[tuple[int, int, int]] = []
    min_train = max(2 * C.STEPS_PER_CYCLE, 200)

    for k in range(n_folds, 0, -1):
        test_end = n_rows - (k - 1) * test_steps
        test_start = test_end - test_steps
        train_end = test_start - gap
        if train_end < min_train or test_start >= test_end:
            continue
        folds.append((train_end, test_start, min(test_end, n_rows)))

    if not folds and n_rows > min_train + 60:
        # Not enough for the full scheme - fall back to one small holdout so
        # the pipeline is still runnable on a first, thin dataset.
        test_start = int(n_rows * 0.8)
        folds = [(test_start - gap, test_start, n_rows)]

    return folds


# ----------------------------------------------------------------------------
# metrics
# ----------------------------------------------------------------------------
def mae(y, p) -> float:
    return float(np.mean(np.abs(y - p)))


def rmse(y, p) -> float:
    return float(np.sqrt(np.mean((y - p) ** 2)))


def smape(y, p) -> float:
    """Symmetric percentage error.

    Plain MAPE explodes when the true value approaches zero, and traffic does
    hit near-zero in the quiet part of every cycle. sMAPE degrades gracefully
    instead of producing infinities.
    """
    denom = (np.abs(y) + np.abs(p)) / 2.0
    m = denom > 1e-9
    return float(np.mean(np.abs(y[m] - p[m]) / denom[m]) * 100) if m.any() else float("nan")


def under_over(y, p) -> tuple[float, float]:
    """Split the error by direction.

      under = predicted too little -> not enough pods -> users suffer
      over  = predicted too much   -> idle pods       -> money wasted

    A model with excellent MAE that achieves it by systematically
    under-predicting is worse than useless in production, and only this split
    reveals that.
    """
    err = y - p
    return float(np.sum(np.clip(err, 0, None))), float(np.sum(np.clip(-err, 0, None)))


def cost(y, p, c_under: float = C.COST_UNDER, c_over: float = C.COST_OVER) -> float:
    u, o = under_over(y, p)
    return c_under * u + c_over * o


def score(y, p) -> dict:
    y = np.asarray(y, dtype=float)
    p = np.asarray(p, dtype=float)
    u, o = under_over(y, p)
    return {
        "mae": mae(y, p),
        "rmse": rmse(y, p),
        "smape": smape(y, p),
        "under": u,
        "over": o,
        "cost": C.COST_UNDER * u + C.COST_OVER * o,
        "n": int(len(y)),
    }


def summarise(rows: list[dict]) -> pd.DataFrame:
    """Average each model across folds and rank by COST, not MAE.

    Ranking by cost on purpose: cost is the thing the project claims to
    improve, so it is the thing the table should sort by. Watching a model win
    on cost while losing on MAE is the single most instructive moment in this
    whole pipeline.
    """
    df = pd.DataFrame(rows)
    agg = (df.groupby("model")
             .agg(mae=("mae", "mean"), mae_sd=("mae", "std"),
                  rmse=("rmse", "mean"), smape=("smape", "mean"),
                  under=("under", "mean"), over=("over", "mean"),
                  cost=("cost", "mean"), folds=("mae", "count"))
             .sort_values("cost"))
    return agg
