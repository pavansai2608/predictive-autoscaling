# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Predictive Autoscaling for Kubernetes

## The problem

Kubernetes' built-in autoscaler (HPA) is **reactive**: it adds pods only *after* load rises.
Pods take minutes to become ready, so during every traffic ramp users sit on an under-scaled
app and see slow responses.

## The idea

Forecast the request rate a few minutes ahead and scale the deployment **before** the traffic
arrives — then prove the benefit with an A/B benchmark against stock HPA under identical load.

## Architecture — a closed loop

```
load/daily.js (k6)  ->  localhost:5000  --port-forward-->  Service traffic-app:80 -> pod:8000
                                                                    |
  app/main.py exposes /metrics (http_requests_total)  <--------------+
                                                                    |
  k8s/servicemonitor.yaml  ->  Prometheus scrapes every 15s  <-------+
                                                                    |
  collect.py  (localhost:9090 -> data/traffic.parquet)  <------------+
                                                                    |
  src/features.py -> src/models.py -> src/backtest.py (rank by cost) |
                  -> src/train_final.py -> models/forecaster.joblib  |
                                                                    |
  src/live.py (Prometheus -> one feature row)                        |
    -> src/predictor.py  (prints a forecast, changes nothing)        |
    -> src/controller.py (forecast -> replica count -> k8s scale API)|
                                                                    |
  more pods -> lower latency -> more traffic served -> more history -+
```

Two things make this a system rather than a notebook, and both are worth protecting when
editing:

- **`src/features.py:build_table` is the single feature definition, used by BOTH training and
  inference.** `train_final.py` calls it over the whole parquet; `live.py:latest_feature_row`
  calls it over a Prometheus window sized (`FETCH_STEPS`) to cover the longest lag. If those
  two ever build features differently, the model is silently asked a different question at
  serve time than it learned. Any new feature must be computable from the live window too.
- **`models/forecaster.joblib` is a bundle, not a bare model**: `{model, features, horizon,
  quantile, backend, trained_rows}`. `predictor.py` and `controller.py` both
  `row.reindex(columns=bundle["features"])` before predicting — column *order* skew is a silent,
  catastrophic failure mode, so never predict on a raw feature frame.

`src/config.py` is the single source of truth for every constant (step size, cycle shape,
horizon, cost ratio, file paths). Change a number there, not in four files.

Scripts in `src/` do `sys.path.insert(0, <src dir>)` and import each other flat (`import
config as C`), while resolving data/model paths against the **repo root**. So run them as
`python src/backtest.py` from the repo root — not `python -m src.backtest`, and not from
inside `src/`.

## Two numbers that must be MEASURED, never guessed

- `C.HORIZON_STEPS` (src/config.py) — measured pod start-up time + the 30s controller
  interval, in 15s steps. Currently `6` (90s), matching the app's `STARTUP_DELAY_S=15` plus
  scheduling; re-measure and update if the deployment changes.
- `CAPACITY_PER_POD` (env var read by `src/controller.py`, default 120 req/s) — measure by
  scaling to 1 replica and raising k6 load until p95 degrades. A wrong value makes every
  decision wrong in the same direction and is invisible in the forecast metrics.

## Commands

Two port-forwards are the prerequisite for everything live — collect.py, live.py, predictor.py
and the k6 scripts all hardcode `localhost:9090` (Prometheus) and `localhost:5000` (app):

```bash
make forward-app       # svc/traffic-app 5000:80
make forward-prom      # monitoring-kube-prometheus-prometheus 9090:9090
```

Cluster loop (kind cluster is named `autoscale`; `imagePullPolicy: Never` means the image must
be side-loaded, there is no registry):

```bash
make build && make load && make deploy   # after ANY app/ change — all three
make pods                                # watch the 0/1 -> 1/1 readiness gap
kubectl rollout restart deploy/traffic-app
```

Local app without the cluster (1s warm-up instead of 15s, auto-reload):

```bash
make run
```

Load:

```bash
k6 run load/steady.js    # 2-minute smoke, 5 VUs
k6 run load/daily.js     # 60-min diurnal cycles, every 7th light — the training signal
```

Forecasting pipeline (repo root, venv active):

```bash
python collect.py                      # Prometheus -> data/traffic.parquet (idempotent, 6h overlap)
python src/backtest.py                 # rolling-origin backtest -> outputs/results.csv + forecast.png
python src/backtest.py --horizon 8     # try a different horizon without editing config
python src/train_final.py              # retrain on ALL data -> models/forecaster.joblib
python src/predictor.py                # dry run: prints forecasts, touches nothing
CAPACITY_PER_POD=120 python src/controller.py   # the real thing: scales the deployment
```

`controller.py` also reads `DEPLOYMENT`, `NAMESPACE`, `INTERVAL_S`, `HEADROOM`, `MIN_PODS`,
`MAX_PODS` from the env, and appends every decision to `logs/decisions.csv`.

There is no test suite and no linter configured. The backtest **is** the correctness check for
the forecasting side: read `outputs/results.csv` top-down, lowest **cost** wins. If a baseline
beats the GBM, that is a real finding to report, not a bug to hide.

## Success criteria

A/B benchmark, same k6 scenario both sides, **3 runs each**:

| Arm         | What it does                          |
|-------------|---------------------------------------|
| Predictive  | controller.py scales from the forecast |
| Baseline    | stock HPA, untouched                   |

Report **p99 latency** *and* **pod-seconds**. (`summaryTrendStats` in both k6 scripts already
includes p99 — k6's default omits it.)

## Decisions already made (don't relitigate these)

- **Quantile q=0.90, not the mean.** The cost of being wrong is asymmetric: under-predicting
  load costs user-visible latency, over-predicting costs a little compute. A model trained on
  symmetric error would optimise for the wrong thing. The same asymmetry appears three times
  on purpose — `COST_UNDER=10 / COST_OVER=1` in the scoreboard, `alpha=0.90` in the model, and
  `MAX_SCALE_DOWN_PER_CYCLE=1` with uncapped scale-up in the controller.
- **Horizon N = measured pod start-up time.** Forecasting further ahead than pods take to boot
  throws away accuracy for no benefit; forecasting less far ahead doesn't buy enough lead time
  to be useful. So N gets measured, not assumed.
- **Report pod-seconds alongside p99.** A latency win bought with far more compute is not a
  win, and a benchmark that hides the cost side isn't honest.
- **Baselines ship with the model.** `models.ladder()` runs naive / seasonal-naive /
  moving-average alongside the GBMs, because "MAE of 14" is unreadable and "34% below the
  one-line forecast any engineer would write" is a claim.
- **The controller refuses to act on bad input** (no data, non-finite prediction, or a forecast
  >10x the recent max) and logs a `hold` instead. When it declines, reactive HPA is the net
  underneath — the same reason AWS runs predictive scaling *alongside* reactive policies.
- **`app/main.py:/work` is sync def, `/healthz` is async def.** A busy-looping async handler
  would pin the event loop and the benchmark would measure event-loop starvation instead of
  pod capacity; a sync health probe would queue behind a saturated threadpool and get pods
  restarted mid-benchmark.

## Environment

- MacBook, Apple Silicon, 16GB RAM. Docker Desktop capped at **8GB** — the cluster, the app,
  Prometheus and k6 all share it, so keep resource requests small.
- Installed and ready: `kind`, `kubectl`, `helm`, `k6`.
- Host venv at `.venv/`: **Python 3.14.2**, with lightgbm 4.7.0, pandas 3.0.5, numpy 2.5.2,
  joblib, kubernetes and prometheus-api-client installed. LightGBM works, so
  `models.BACKEND == "lightgbm"`; the scikit-learn fallback in `models.py` is untested and
  sklearn is **not** installed.
- **Host deps live in the root `requirements.txt`; `app/requirements.txt` is image-only.**
  Keep them apart — the second is COPYed into the container, which never touches Parquet or
  LightGBM.
- **A Parquet engine is a separate install.** pandas delegates `to_parquet` to pyarrow or
  fastparquet and ships neither; on 2026-08-19 `collect.py` died on its final line for exactly
  this reason (pyarrow 25.0.1 now installed). If `data/traffic.parquet` cannot be written,
  check this before anything else.
- The container is Python **3.11**, not 3.14, and only ever runs `app/` — the forecaster stays
  on the host. `.venv` is in `.dockerignore` for that reason.

## Repo layout — state as of 2026-08-18

Exists and works:

```
app/main.py            FastAPI app under test — deliberately CPU-bound and slow to start
Dockerfile             python:3.11-slim image `traffic-app:v1`
Makefile               every command above; ports defined once at the top
requirements.txt       HOST pipeline deps (pinned) — separate from app/requirements.txt
k8s/                   deployment.yaml, service.yaml, servicemonitor.yaml
load/                  steady.js (smoke), daily.js (diurnal training signal)
collect.py             Prometheus -> data/traffic.parquet
src/config.py          every constant
src/features.py        lags, rolling stats, clock features of t+H
src/models.py          baseline ladder + LightGBM/sklearn GBM + replicas_needed()
src/evaluate.py        rolling-origin folds, cost metric, under/over split
src/backtest.py        the evaluation run
src/train_final.py     retrain on everything -> models/forecaster.joblib
src/live.py            Prometheus -> one inference-shaped feature row
src/predictor.py       dry-run forecaster
src/controller.py      the predictive autoscaler
```

Does not exist yet — these are the remaining steps, one at a time:

```
k8s/hpa.yaml           the BASELINE arm. Without it there is no A/B, only an A.
bench/                 k6 scenario + results for the 3-runs-each benchmark
data/traffic.parquet   EMPTY. Nothing downstream of collect.py can run until
                       daily.js has been left running for several cycles.
models/, outputs/, logs/   created on first use by train_final / backtest / controller
```

**Do not claim a backtest number, a horizon, or a capacity figure that has not actually been
run on this machine.** `data/` is empty today, which means every number in this file marked
"measure this" is still unmeasured.

## How we work — follow these strictly

- **One small step at a time.** Do only what the current step asks.
- **Never create files or make changes beyond the current step.** No helpful extras, no
  scaffolding "while we're here."
- **The user runs all terminal commands.** Give the commands to run — never execute them.
- **When the user pastes an error, explain what it means before fixing it.** The point of this
  project is understanding, not a working repo.
- **Keep every file short and heavily commented with WHY, not what.** `# increment i` is
  noise; `# q=0.90 because under-scaling hurts users more than over-scaling costs money` is
  the comment worth writing.
- **Don't invent facts about code that hasn't been read.** If something isn't there, say so.
