"""Turn the raw [ts, y] series into a table of question -> answer rows.

The single rule that governs this whole file:

    To predict what happens at t+H, you may only use what was knowable at t.

Break it and your scores become fiction - the model quietly peeks at the
future, every metric looks brilliant, and none of it survives contact with a
live system. This is the first thing an interviewer checks, so it is worth
being able to point at exactly where it is enforced (see build_table below).

Two kinds of feature are legitimate:

  * LAGS AND ROLLING STATS of y, taken at t or earlier. pandas' .rolling()
    includes the current row, which is fine: t is "now", you are allowed to
    know it.

  * CLOCK FEATURES OF t+H. This looks like cheating and is not - you always
    know what time it will be in ninety seconds. Clocks are not a secret.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

import config as C

# Lags in 15-second steps. The interesting ones:
#   4   = 1 minute ago
#   240 = same point one cycle ("yesterday") ago
#   1680= same point one week ago
LAGS = [1, 2, 3, 4, 6, 8, 12, 20, 40, 80, 120, C.STEPS_PER_CYCLE, C.STEPS_PER_WEEK]
ROLL_WINDOWS = [4, 12, 40, 120, C.STEPS_PER_CYCLE]


def to_grid(df: pd.DataFrame) -> pd.DataFrame:
    """Put a [ts, y] frame onto a fixed STEP_SECONDS grid.

    CALLED BY BOTH PATHS - load_series() below for training, and
    live.latest_feature_row() for inference. That shared call is the whole
    point: Prometheus can miss a scrape (a restart, a sleeping laptop), which
    leaves holes, and every lag in build_table() is positional. Reindexing
    makes "lag 240" mean a true one cycle back rather than "240 rows back,
    whenever those happened to be".

    Skipping this on the serve side is not a small inaccuracy - it silently
    asks the model a different question than it was trained on. Observed on
    2026-08-22: the live window held 120 rows spanning 7.8 hours (1872 rows if
    gapless, 13 gaps, the largest 79 minutes), and the controller forecast
    ~52 req/s while traffic was steady at ~36.
    """
    d = df[["ts", "y"]].copy()
    d["ts"] = pd.to_datetime(d["ts"], utc=True)
    d = d.dropna(subset=["ts"]).drop_duplicates(subset="ts").sort_values("ts")

    grid = pd.date_range(d["ts"].min(), d["ts"].max(),
                         freq=f"{C.STEP_SECONDS}s", tz="UTC")
    d = d.set_index("ts").reindex(grid)
    d.index.name = "ts"

    # Short gaps get bridged; long outages stay NaN and are dropped later.
    # Inventing hours of traffic that never happened would teach the model a
    # pattern that does not exist.
    d["y"] = d["y"].interpolate(limit=8).astype(float)

    return d.reset_index()


def load_series(path: str = C.DATA_FILE) -> pd.DataFrame:
    """Read the parquet the collector writes, on the same grid inference uses."""
    df = pd.read_parquet(path)

    if "ts" not in df.columns or "y" not in df.columns:
        raise ValueError(f"expected columns [ts, y], found {list(df.columns)}")

    return to_grid(df)


def build_table(df: pd.DataFrame, horizon: int = C.HORIZON_STEPS) -> pd.DataFrame:
    """Add the clue columns and the answer column."""
    d = df.sort_values("ts").reset_index(drop=True).copy()
    y = d["y"]

    # ---- THE ANSWER ---------------------------------------------------------
    # Shift the y column UP by `horizon` rows: each row's target is the value
    # that really occurred `horizon` steps later. The past grades itself.
    d["target"] = y.shift(-horizon)

    # ---- lags ---------------------------------------------------------------
    for lag in LAGS:
        d[f"lag_{lag}"] = y.shift(lag)

    # ---- rolling statistics -------------------------------------------------
    for w in ROLL_WINDOWS:
        r = y.rolling(w, min_periods=max(2, w // 4))
        d[f"roll_mean_{w}"] = r.mean()
        d[f"roll_std_{w}"] = r.std()
        d[f"roll_max_{w}"] = r.max()

    # ---- shape of the recent past ------------------------------------------
    # A rising ramp is exactly where reactive scaling fails, so give the model
    # a direct view of "is this climbing, and how fast".
    d["diff_1"] = y.diff(1)
    d["diff_4"] = y.diff(4)
    d["slope_12"] = (y - y.shift(12)) / 12.0
    d["accel"] = d["diff_1"] - d["diff_1"].shift(1)
    d["ratio_short_long"] = d["roll_mean_4"] / d["roll_mean_120"].replace(0, np.nan)

    # ---- comparison with the previous cycle --------------------------------
    prev = y.shift(C.STEPS_PER_CYCLE)
    d["vs_prev_cycle"] = d["roll_mean_12"] / prev.replace(0, np.nan)

    # ---- clock features of the moment being predicted -----------------------
    # Position within the k6 cycle, anchored to the UNIX EPOCH rather than to
    # this frame's first row.
    #
    # Anchoring to d["ts"].iloc[0] looks equivalent and is not. Training passes
    # the whole parquet, so row 0 is a fixed instant. Inference passes a window
    # that slides with the wall clock, so row 0 moves - and the LAST row, the
    # only one being predicted, always lands the same distance from it.
    # Measured on 2026-08-24: f_pos_in_cycle read 142.0 on three consecutive
    # live fetches, i.e. the model's "where are we in the day" input was a
    # constant at serve time while it varied across the whole range in
    # training. Same column name, different question.
    #
    # An epoch anchor is identical in both paths by construction. It is offset
    # from k6's true cycle start by a constant, which does not matter: a
    # constant phase shift is something the model learns once.
    # Subtracting a fixed epoch and asking for total_seconds() is deliberate:
    # .astype("int64") returns the underlying integer in whatever unit the dtype
    # happens to use - pandas 3 builds these ranges as datetime64[us], so a
    # nanosecond assumption silently floors every row in an hour to the same
    # value. total_seconds() is unit-agnostic.
    future_ts = d["ts"] + pd.Timedelta(seconds=horizon * C.STEP_SECONDS)
    epoch = pd.Timestamp("1970-01-01", tz="UTC")
    elapsed = (future_ts - epoch).dt.total_seconds() // C.STEP_SECONDS

    pos = elapsed % C.STEPS_PER_CYCLE                 # where in the "day"
    cycle_no = (elapsed // C.STEPS_PER_CYCLE).astype(int)

    d["f_pos_in_cycle"] = pos
    # sin/cos so the model knows the end of a cycle sits next to the start,
    # instead of treating step 239 and step 0 as far apart.
    d["f_cycle_sin"] = np.sin(2 * np.pi * pos / C.STEPS_PER_CYCLE)
    d["f_cycle_cos"] = np.cos(2 * np.pi * pos / C.STEPS_PER_CYCLE)
    d["f_cycle_no"] = cycle_no % C.WEEKEND_EVERY
    d["f_is_weekend"] = (cycle_no % C.WEEKEND_EVERY == C.WEEKEND_EVERY - 1).astype(int)

    return d


def feature_columns(table: pd.DataFrame) -> list[str]:
    """Everything except the timestamp, the raw value, and the answer."""
    drop = {"ts", "y", "target"}
    return [c for c in table.columns if c not in drop]


def usable(table: pd.DataFrame) -> pd.DataFrame:
    """Drop rows that cannot be scored or have no recent history.

    Deliberately NOT dropping rows whose long lags are missing: with only a
    few hours collected, lag_1680 is empty everywhere, and requiring it would
    throw away the entire dataset. Both model backends treat NaN as "unknown"
    and route around it, so an absent long lag costs accuracy, not the run.
    """
    need = ["target", "lag_1", "roll_mean_12"]
    return table.dropna(subset=need).reset_index(drop=True)
