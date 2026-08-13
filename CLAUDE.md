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
k6 (scripted fake traffic)
  -> FastAPI app on a local kind cluster
  -> Prometheus scrapes request rate every 15s
  -> collect.py appends history to data/traffic.parquet
  -> LightGBM quantile model (q=0.90) forecasts load N minutes ahead
     (N = MEASURED pod start-up time, not a guessed number)
  -> controller.py sets deployment replicas via the kubernetes Python client
  -> (loop closes: more traffic -> more history -> better forecast)
```

## Success criteria

A/B benchmark, same k6 scenario both sides, **3 runs each**:

| Arm         | What it does                          |
|-------------|---------------------------------------|
| Predictive  | controller.py scales from the forecast |
| Baseline    | stock HPA, untouched                   |

Report **p99 latency** *and* **pod-seconds**.

## Decisions already made (don't relitigate these)

- **Quantile q=0.90, not the mean.** The cost of being wrong is asymmetric: under-predicting
  load costs user-visible latency, over-predicting costs a little compute. A model trained on
  symmetric error would optimise for the wrong thing.
- **Horizon N = measured pod start-up time.** Forecasting further ahead than pods take to boot
  throws away accuracy for no benefit; forecasting less far ahead doesn't buy enough lead time
  to be useful. So N gets measured, not assumed.
- **Report pod-seconds alongside p99.** A latency win bought with far more compute is not a
  win, and a benchmark that hides the cost side isn't honest.

## Environment

- MacBook, Apple Silicon, 16GB RAM. Docker Desktop capped at **8GB** — the cluster, the app,
  Prometheus and k6 all share it, so keep resource requests small.
- Installed and ready: `kind`, `kubectl`, `helm`, `k6`.
- Python venv at `.venv/` in this repo — **Python 3.14.2, currently containing only pip.**
  Worth checking when we first install: 3.14 is new enough that LightGBM / pyarrow wheels may
  not all be available yet.

## Repo layout

Everything that exists today:

```
README.md      one line
.venv/         Python 3.14.2, only pip installed
CLAUDE.md      this file
```

Planned — **none of this exists yet**, it lands one step at a time:

```
src/           forecasting pipeline: features.py, evaluate.py, models.py
app/           the FastAPI app under test
k8s/           manifests: deployment, service, HPA
data/          traffic.parquet (scraped history)
collect.py     Prometheus -> parquet
controller.py  forecast -> replica count
bench/         k6 scripts + results
```

**On `src/`:** the plan is to adapt an existing forecasting pipeline (`features.py`,
`evaluate.py`, `models.py`) that was built for a public dataset — **adapt it, not rewrite it**.
As of 2026-08-13 that code is *not in this repo and not on this machine*. It has to be located
and copied in before that step can start. Nothing in this file describes what it does, because
it hasn't been read.

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
