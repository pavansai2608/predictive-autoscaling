"""The models, weakest first.

Starting with baselines is not a formality - a baseline is what makes a result
mean something. "MAE of 14" is unreadable. "34% below the naive forecast any
engineer would write in one line" is a claim.

The ladder:

  1. Naive          - next value equals the current one. The zero-effort answer.
  2. SeasonalNaive  - next value equals the same point one cycle ago.
                      Surprisingly hard to beat on rhythmic traffic, and plenty
                      of published forecasting results quietly lose to it.
  3. MovingAverage  - mean of the recent window. Smooths noise, lags ramps.
  4. GBM            - gradient boosting on the engineered features.
  5. GBM (quantile) - the same model aimed at a HIGH percentile instead of the
                      middle, and the one that matters here:

     Forecasting the average expected load leaves you short roughly half the
     time. For a service at peak, "short half the time" is an outage half the
     time. Targeting the 90th percentile deliberately over-provisions a little,
     trading a small amount of money for a large amount of safety - and it
     puts that asymmetry inside the loss function rather than patching it
     afterwards with a fudge factor.

BACKEND NOTE: LightGBM is used when available; scikit-learn's
HistGradientBoostingRegressor is the fallback. They are the same algorithm
family, both support a quantile objective, and both treat NaN as "unknown"
rather than crashing - which matters because the long seasonal lags are empty
until a week of data exists. The fallback also means a Python version without
a LightGBM wheel yet does not block the project.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

import config as C

try:
    import lightgbm as lgb
    BACKEND = "lightgbm"
except Exception:                                  # pragma: no cover
    lgb = None
    from sklearn.ensemble import HistGradientBoostingRegressor
    BACKEND = "sklearn"


# ----------------------------------------------------------------------------
# baselines
# ----------------------------------------------------------------------------
class Naive:
    name = "naive"

    def fit(self, *a, **k):
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return X["lag_1"].to_numpy(dtype=float)


class SeasonalNaive:
    name = "seasonal_naive"

    def fit(self, *a, **k):
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        col = f"lag_{C.STEPS_PER_CYCLE}"
        p = X[col].to_numpy(dtype=float)
        # Before one full cycle of history exists this lag is empty; fall back
        # to the last value so the baseline is still scoreable rather than NaN.
        return np.where(np.isnan(p), X["lag_1"].to_numpy(dtype=float), p)


class MovingAverage:
    def __init__(self, window: int = 12):
        self.window = window
        self.name = f"moving_avg_{window}"

    def fit(self, *a, **k):
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return X[f"roll_mean_{self.window}"].to_numpy(dtype=float)


# ----------------------------------------------------------------------------
# gradient boosting
# ----------------------------------------------------------------------------
class GBM:
    """One model over the whole series, with an optional quantile objective."""

    def __init__(self, quantile: float | None = None, name: str | None = None,
                 rounds: int = 400, lr: float = 0.05):
        self.quantile = quantile
        self.rounds = rounds
        self.lr = lr
        self.name = name or (f"gbm_q{quantile:g}" if quantile else "gbm")
        self.model = None
        self.features: list[str] = []

    def fit(self, X: pd.DataFrame, y, features: list[str]):
        self.features = features
        Xf = X[features]

        if BACKEND == "lightgbm":
            params = dict(
                objective="quantile" if self.quantile else "regression_l1",
                metric="quantile" if self.quantile else "l1",
                learning_rate=self.lr,
                num_leaves=31,
                min_data_in_leaf=30,
                feature_fraction=0.85,
                bagging_fraction=0.85,
                bagging_freq=1,
                lambda_l2=1.0,
                verbosity=-1,
                num_threads=0,
            )
            if self.quantile:
                params["alpha"] = self.quantile
            ds = lgb.Dataset(Xf, label=y, free_raw_data=False)
            self.model = lgb.train(params, ds, num_boost_round=self.rounds)
        else:
            kwargs = dict(
                max_iter=self.rounds,
                learning_rate=self.lr,
                max_leaf_nodes=31,
                min_samples_leaf=30,
                l2_regularization=1.0,
                early_stopping=False,
            )
            if self.quantile:
                kwargs.update(loss="quantile", quantile=self.quantile)
            else:
                kwargs.update(loss="absolute_error")
            self.model = HistGradientBoostingRegressor(**kwargs).fit(Xf, y)

        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        if self.model is None:
            raise RuntimeError("call fit() first")
        return np.asarray(self.model.predict(X[self.features]), dtype=float)

    def importance(self, top: int = 15) -> pd.DataFrame:
        if BACKEND != "lightgbm" or self.model is None:
            return pd.DataFrame(columns=["feature", "gain"])
        return (pd.DataFrame({"feature": self.model.feature_name(),
                              "gain": self.model.feature_importance("gain")})
                .sort_values("gain", ascending=False)
                .head(top).reset_index(drop=True))


def ladder() -> list:
    """The models to compare, in increasing order of effort."""
    return [Naive(), SeasonalNaive(), MovingAverage(12), GBM(), GBM(quantile=C.QUANTILE)]


# ----------------------------------------------------------------------------
# forecast -> decision
# ----------------------------------------------------------------------------
def replicas_needed(predicted_rate, capacity_per_pod: float, min_pods: int = 2,
                    max_pods: int = 20, headroom: float = 1.1) -> np.ndarray:
    """Turn a predicted request rate into a pod count.

    This tiny function is the bridge from forecasting to control. A dashboard
    stops at `predicted_rate`; this project continues to a number that
    Kubernetes will actually act on.

    Keep `headroom` small and explicit. If you find yourself raising it to stop
    outages, the honest fix is a higher quantile in the model, not a bigger
    fudge factor here.
    """
    pods = np.ceil(np.asarray(predicted_rate, dtype=float) * headroom / capacity_per_pod)
    return np.clip(pods, min_pods, max_pods).astype(int)
