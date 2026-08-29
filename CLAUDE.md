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
k6 POD in-cluster (k8s/load/k6.yaml)  ->  Service traffic-app:80  ->  pod:8000
   NOT via `kubectl port-forward`: that resolves the Service to ONE pod and pins
   every request to it (measured 6.94 req/s on one pod, 0.00 on three others).
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

  TWO BUGS OF EXACTLY THIS KIND SHIPPED AND WERE CAUGHT BY RUNNING THE SYSTEM, NOT BY
  READING IT. Both produced plausible forecasts (~45% too high) and raised nothing:
    1. `live.py` fed raw Prometheus output to `build_table` without the 15s grid
       reindex `load_series` applies, so every positional lag pointed at the wrong
       instant. Fixed by extracting `features.to_grid()` and calling it from both.
    2. Clock features were anchored to the input frame's first row — fixed in
       training, sliding at inference — so `f_pos_in_cycle` was frozen at a constant
       when serving. Fixed by anchoring to the Unix epoch.
  The backtest cannot catch this class of bug: it only ever exercises the training
  path. `predictor.py` against live Prometheus is the check that can.
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

Both MEASURED on 2026-08-22. Re-measure if `WORK_MS`, `STARTUP_DELAY_S` or the CPU
limit in `k8s/deployment.yaml` changes.

- `C.HORIZON_STEPS = 4` (60s). Pod created -> Ready timed over three deletions: 19s,
  19s, 18s. Plus the 30s controller interval, rounded up: `ceil(48.7/15) = 4`.
- `CAPACITY_PER_POD = 20` req/s (`src/controller.py`, overridable by env). `make
  capacity` steps the arrival rate against a single replica: p95 is flat at 95ms
  through 20 req/s and jumps to 381ms at 24, with CPU pinned at the 400m limit
  throughout. The old default of 120 would have provisioned 6x too few pods for
  every forecast, and no forecast metric would have shown it.

## Commands

ONE port-forward is the prerequisite for everything live. collect.py, live.py,
predictor.py, analyze.py, export_replay.py and dashboard.py all hardcode
`localhost:9090`:

```bash
make forward-prom      # monitoring-kube-prometheus-prometheus 9090:9090
```

There is deliberately no `forward-app`. `kubectl port-forward svc/...` pins every
request to a single pod, so laptop-side load can never demonstrate a benefit from
scaling; k6 runs in-cluster and reaches the Service directly. Nothing on the Mac
needs the app's port. `make run` (local dev, no cluster) uses 8000 rather than 5000
because macOS Control Center holds 5000 for AirPlay.

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

Load — ALL of it runs in-cluster, never from the laptop (see the architecture note):

```bash
make load-start          # daily.js as a Deployment — the training signal
make load-stop           # scale it to 0; REQUIRED before any benchmark run
make capacity            # one pod's req/s; needs 1 replica and no HPA first
make bench RUN=A1r SCRIPT=ramp.js    # one 20-min benchmark run
```

`make load-start` rebuilds the ConfigMap from `load/` and does a rollout restart —
editing a script without that leaves the old version running, silently.

Forecasting pipeline (repo root, venv active):

```bash
python collect.py                      # Prometheus -> data/traffic.parquet (idempotent, 6h overlap)
python src/backtest.py                 # rolling-origin backtest -> outputs/results.csv + forecast.png
python src/backtest.py --horizon 8     # try a different horizon without editing config
python src/train_final.py              # retrain on ALL data -> models/forecaster.joblib
python src/predictor.py                # dry run: prints forecasts, touches nothing
CAPACITY_PER_POD=20 python src/controller.py    # the real thing: scales the deployment
python analyze.py                      # score the A/B -> results-r.md, comparison-r.png
python analyze.py --suffix s           # same, for the step scenario
```

`controller.py` also reads `DEPLOYMENT`, `NAMESPACE`, `INTERVAL_S`, `HEADROOM`, `MIN_PODS`,
`MAX_PODS` from the env, and appends every decision to `logs/decisions.csv`.

There is no test suite and no linter configured. The backtest **is** the correctness check for
the forecasting side: read `outputs/results.csv` top-down, lowest **cost** wins. If a baseline
beats the GBM, that is a real finding to report, not a bug to hide.

## Results — MEASURED, 2026-08-24

Backtest, 4 folds, 12,277 rows: `gbm_q0.90` cost 4,295 vs naive 12,094 — **64.5% lower**.
The mean-targeting GBM has half the MAE (2.24 vs 4.77) and costs 31% MORE, which is the
clearest evidence in the project that the metric choice matters more than the model.

A/B benchmark, identical traffic, 3 runs per arm:

| scenario | p99 baseline | p99 predictive | pod-seconds | verdict |
|----------|--------------|----------------|-------------|---------|
| ramp (20->80 req/s over 6 min) | 479 ms | **183 ms** | 3,053 -> 3,907 | **62% lower, +28% compute** |
| step (instant 4x)              | 467 ms | 522 ms (1 run) | — | no advantage |

The step result is the honest half: with no precursor there is nothing to forecast, both
arms are blind for 30-60s, and pods take 19s regardless. The controller still provisioned
CORRECTLY there (5 pods vs the HPA's 3) — arriving late with the right answer is the
point being made.

Both arms must provision to the SAME steady-state pod count or the benchmark compares
generosity, not timing. That is why `k8s/deployment.yaml` sets `requests == limits ==
400m` and `k8s/hpa.yaml` targets 90%: at 60% of a 200m request the HPA held ~7 pods where
the controller held 3, and any latency win would have been explained by the extra capacity.

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

## Repo layout — state as of 2026-08-24

```
app/main.py            FastAPI app under test — deliberately CPU-bound and slow to start
Dockerfile             python:3.11-slim image `traffic-app:v1`
Makefile               every command above; ports defined once at the top
requirements.txt       HOST pipeline deps (pinned) — separate from app/requirements.txt
collect.py             Prometheus -> data/traffic.parquet
analyze.py             scores the A/B -> results-*.md + outputs/comparison-*.png

k8s/deployment.yaml    requests == limits == 400m (see Results for why)
k8s/service.yaml       ClusterIP; the only way load reaches pods
k8s/servicemonitor.yaml
k8s/hpa.yaml           THE BASELINE ARM, at 90% — a manifest so it is reproducible
k8s/load/k6.yaml               daily.js as a Deployment; scale 0/1 to stop/start
k8s/load/k6-capacity.yaml      one-off Job, Step 25
k8s/load/k6-benchmark.yaml     one Job per benchmark run
                       k8s/load/ is a SUBDIRECTORY on purpose: `kubectl apply -f k8s/`
                       is not recursive, so `make deploy` cannot start a load test.

load/daily.js          60-min diurnal cycles — the training signal
load/ramp.js           BENCHMARK: 20->80 req/s over 6 min. The predictable event.
load/benchmark.js      BENCHMARK: instant 4x step. The unpredictable one.
load/capacity.js       stepped arrival rate to find one pod's knee

src/config.py          every constant
src/features.py        to_grid() + build_table() — SHARED by training and inference
src/models.py          baseline ladder + LightGBM/sklearn GBM + replicas_needed()
src/evaluate.py        rolling-origin folds, cost metric, under/over split
src/backtest.py        the evaluation run
src/train_final.py     retrain on everything -> models/forecaster.joblib
src/live.py            Prometheus -> one inference-shaped feature row (+ freshness guard)
src/predictor.py       dry-run forecaster — the ONLY check for train/serve skew
src/controller.py      the predictive autoscaler

data/traffic.parquet   12,281 rows, 51h, 100% coverage. NOT gitignored: Prometheus
                       keeps 15 days, so this is the one unreproducible artefact.
bench/*.json           six benchmark runs + their start/end epochs
bench/discarded/       runs thrown out, with README.md saying why
```

Nothing outstanding. A screen recording was considered and deliberately skipped — the
chart carries the same evidence.

**Every number in this file has been measured on this machine.** Do not add one that
has not. If you change `WORK_MS`, `STARTUP_DELAY_S`, the CPU limit, or `PEAK_RPS`, the
horizon and capacity figures are void until re-measured.

### Operational traps, all of them hit at least once

- **`kubectl port-forward svc/X` pins to ONE pod.** It also dies when that pod dies.
- **macOS Control Center holds port 5000** (AirPlay). When a forward drops, k6 gets
  instant 403s instead of connection errors — it looks healthy while delivering nothing.
- **kube-proxy balances per TCP connection**, so k6 needs `noConnectionReuse: true` or
  one VU's keep-alive socket pins all traffic to one pod.
- **Closing the laptop lid sleeps the Mac even on AC** ("Clamshell Sleep"). It freezes
  the cluster mid-run; `caffeinate` does not prevent it.
- **Readiness probes must detect DEAD, not BUSY.** At the default 1s timeout a saturated
  pod fails its probe, leaves the Service, dumps its load on the survivors, and the
  deployment cascades to zero available replicas.
- **A benchmark run with `dropped_iterations > 0` is invalid** — k6 quietly reduced the
  offered load exactly when the app was struggling.

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
