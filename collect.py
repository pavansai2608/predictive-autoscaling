"""Prometheus -> data/traffic.parquet.

Idempotent by construction: every run re-queries an overlapping 6h window and
merges on timestamp, so running it hourly — or twice by accident — converges on
the same history instead of duplicating rows or leaving gaps.
"""

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
from prometheus_api_client import PrometheusConnect

PROM_URL = "http://localhost:9090"  # local end of `make forward-prom`
OUT = Path("data/traffic.parquet")

# Only /work. The other endpoints are SELF-TRAFFIC: measured on this cluster,
# /healthz probes ran at 0.667 req/s and /metrics scrapes at 0.133 req/s with
# 2 pods — and both scale with replica count. Leaving them in creates a
# feedback loop where adding pods raises the measured rate, which forecasts a
# higher rate, which adds pods. src/live.py MUST use this identical query.
QUERY = 'sum(rate(http_requests_total{handler="/work"}[1m]))'

# Anything before this instant was recorded through a BROKEN load path and must
# never reach the model. Until 2026-08-19 the load generator ran on the Mac
# behind `kubectl port-forward`, which pins every request to a single pod, so
# the recorded rate was one pod's ceiling rather than real demand — and while
# the forward was down, macOS AirPlay answered on port 5000 with instant 403s,
# recording an hour of silence as if traffic had stopped.
#
# A cutoff is needed rather than just deleting the parquet: every run re-reads
# a 6h window, so deleted rows come straight back out of Prometheus. Once the
# bad period is more than LOOKBACK old this line stops doing anything, and it
# is then safe to remove.
EARLIEST = pd.Timestamp("2026-08-19T11:53:00Z")

# 6h of overlap gives every run a wide re-read, so a crash or a dead
# port-forward costs nothing as long as the next run lands within the window.
LOOKBACK = timedelta(hours=6)
STEP_SECONDS = 15  # matches the scrape interval; finer would only interpolate
STEP = f"{STEP_SECONDS}s"


def _grid_aligned_now() -> datetime:
    """Now, snapped DOWN to an absolute 15s boundary since the epoch.

    Prometheus aligns query_range output to the start_time it is given, not to
    any absolute clock. Pass a raw now() and each run gets its own grid offset
    by however many seconds elapsed since the last one — so the same instant
    comes back as :29 on one run and :30 on the next, drop_duplicates matches
    nothing, and every row is re-appended as new. (Observed: two runs a minute
    apart produced 327 then +331 rows.)

    Snapping to a fixed grid makes repeated runs return byte-identical
    timestamps, which is what makes the merge in main() actually idempotent.
    """
    epoch = datetime.now(timezone.utc).timestamp()
    return datetime.fromtimestamp(epoch - (epoch % STEP_SECONDS), tz=timezone.utc)


def fetch() -> pd.DataFrame:
    prom = PrometheusConnect(url=PROM_URL, disable_ssl=True)
    end = _grid_aligned_now()
    result = prom.custom_query_range(
        QUERY, start_time=end - LOOKBACK, end_time=end, step=STEP
    )
    if not result:
        return pd.DataFrame(columns=["ts", "y"])

    # sum() collapses everything to one series, so result[0] is the whole answer.
    df = pd.DataFrame(result[0]["values"], columns=["ts", "y"])
    # Stored as UTC datetimes, not raw epochs, because the model's features are
    # minute-of-day and day-of-week — cheap now, painful to retrofit later.
    df["ts"] = pd.to_datetime(df["ts"], unit="s", utc=True)
    df["y"] = pd.to_numeric(df["y"], errors="coerce")
    return df[df["ts"] >= EARLIEST].dropna()


def main() -> None:
    frames = []
    before = 0
    if OUT.exists():
        old = pd.read_parquet(OUT)
        before = len(old)
        frames.append(old)

    fresh = fetch()
    if not fresh.empty:
        frames.append(fresh)

    if not frames:
        sys.exit("no data and no existing file — is `make forward-prom` running?")

    # keep="last": a re-query of the same instant wins, so a row captured from a
    # half-filled rate() window gets corrected rather than frozen into history.
    df = (
        pd.concat(frames, ignore_index=True)
        .drop_duplicates(subset="ts", keep="last")
        .sort_values("ts")
        .reset_index(drop=True)
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUT, index=False)
    print(f"{len(df)} rows (+{len(df) - before} new)")
    print(f"{df.ts.min()} -> {df.ts.max()}")


if __name__ == "__main__":
    main()
