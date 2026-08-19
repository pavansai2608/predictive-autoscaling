"""One place for every number the pipeline depends on.

Everything downstream reads from here, so changing the traffic pattern or the
horizon is a single edit rather than a hunt through four files.
"""

# --- shape of the data -------------------------------------------------------
STEP_SECONDS = 15          # Prometheus scrape interval => one row every 15s
CYCLE_MINUTES = 60         # one k6 "day" (from load/daily.js CYCLE_MIN)
WEEKEND_EVERY = 7          # every 7th cycle is the light "weekend"

STEPS_PER_CYCLE = CYCLE_MINUTES * 60 // STEP_SECONDS       # 240
STEPS_PER_WEEK = STEPS_PER_CYCLE * WEEKEND_EVERY           # 1680

# --- the forecast horizon ----------------------------------------------------
# HOW FAR AHEAD TO PREDICT, in 15s steps.
#
# Set this from your MEASURED pod start-up time (Step 20), not a guess:
#     horizon_seconds = average_pod_ready_time + 30s controller interval
#     HORIZON_STEPS   = ceil(horizon_seconds / 15)
#
# Examples:  45s ready -> 75s  -> 5 steps
#            60s ready -> 90s  -> 6 steps
#            90s ready -> 120s -> 8 steps
#
# Forecasting further ahead than you can act on is wasted accuracy; forecasting
# less means capacity still arrives late. That is why this number is measured.
HORIZON_STEPS = 6

# --- the cost of being wrong -------------------------------------------------
# Under-provisioning means users hit a slow app. Over-provisioning means a
# slightly larger bill. These are NOT equally bad, so the scoreboard prices
# them differently. This ratio is a business assumption you should be able to
# defend out loud - and note that it is exactly a quantile loss at
# q = 10/(10+1) = 0.909, which is why the headline model targets q=0.90.
COST_UNDER = 10.0
COST_OVER = 1.0
QUANTILE = 0.90

# --- backtest ----------------------------------------------------------------
N_FOLDS = 4
TEST_STEPS = STEPS_PER_CYCLE * 2     # each fold tests on ~2 cycles of data

# --- paths -------------------------------------------------------------------
DATA_FILE = "data/traffic.parquet"
MODEL_FILE = "models/forecaster.joblib"
RESULTS_FILE = "outputs/results.csv"
PLOT_FILE = "outputs/forecast.png"
