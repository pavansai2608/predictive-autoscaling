"""Read the most recent traffic from Prometheus and shape it exactly like
training data.

The subtle thing this file exists to prevent is TRAIN/SERVE SKEW: the model was
trained on rows whose features included lags reaching back one "week"
(STEPS_PER_WEEK). If inference only fetched the last hour, those columns would
be empty at predict time but populated at train time, and the model would be
quietly asked a different question than the one it learned. So the fetch window
is deliberately sized to cover the longest lag the feature builder uses.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pandas as pd
from prometheus_api_client import PrometheusConnect

import config as C
import features as F

PROM_URL = "http://localhost:9090"

# Byte-for-byte the query collect.py records, so the model sees at serve time
# the identical signal it trained on. Narrowed to /work because health probes
# and metric scrapes scale with replica count — see the note in collect.py.
# If one of these two queries ever changes, the other must change with it.
QUERY = 'sum(rate(http_requests_total{handler="/work"}[1m]))'

# Longest lag + rolling window + a margin for missed scrapes.
FETCH_STEPS = C.STEPS_PER_WEEK + C.STEPS_PER_CYCLE + 60


def fetch_recent(url: str = PROM_URL) -> pd.DataFrame:
    """Return [ts, y] covering enough history to build every feature."""
    prom = PrometheusConnect(url=url, disable_ssl=True)
    end = datetime.now(timezone.utc)
    start = end - timedelta(seconds=FETCH_STEPS * C.STEP_SECONDS)

    result = prom.custom_query_range(
        QUERY, start_time=start, end_time=end, step=f"{C.STEP_SECONDS}s"
    )
    if not result:
        return pd.DataFrame(columns=["ts", "y"])

    df = pd.DataFrame(result[0]["values"], columns=["ts", "y"])
    df["ts"] = pd.to_datetime(df["ts"], unit="s", utc=True)
    df["y"] = pd.to_numeric(df["y"], errors="coerce")
    return df.dropna().reset_index(drop=True)


def latest_feature_row(df: pd.DataFrame, horizon: int):
    """Build features and return the single most recent row.

    That row has no `target` - the future has not happened yet - which is
    exactly the difference between training (rows with answers) and inference
    (one row without one).
    """
    if df.empty:
        return None, float("nan")

    table = F.build_table(df, horizon=horizon)
    row = table.iloc[[-1]]
    current_rate = float(df["y"].iloc[-1])
    return row, current_rate
