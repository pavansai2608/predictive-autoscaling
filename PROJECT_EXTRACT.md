# PROJECT_EXTRACT.md

Complete technical extraction of the **predictive-autoscaling** repository.

- Repository root: `/Users/golipavansaikrishna/Desktop/predictive-autoscaling`
- Git remote: `https://github.com/pavansai2608/predictive-autoscaling.git`
- Branch: `main` · HEAD at extraction time: `9c17bf4`
- Working tree at extraction time: **clean** (no uncommitted changes)
- Extraction date: 2026-09-06

This document is self-contained. Every value is copied from the repository; nothing
is estimated. Where something could not be determined it is marked
`UNKNOWN — not found in repo`.

---

# 1. REPO INVENTORY

## 1.1 Full recursive file tree

Excludes `.venv/`, `.git/` internals, `__pycache__/`, `node_modules/`, `*.pyc`.

| Path | Lines | Size (KB) | Purpose |
|---|---:|---:|---|
| `.dockerignore` | 16 | 0.6 | Paths excluded from the Docker build context (keeps .venv out of the image). |
| `.gitignore` | 40 | 1.4 | Ignore rules; documents in comments why data/traffic.parquet is deliberately NOT ignored. |
| `CLAUDE.md` | 357 | 20.3 | Project guide for AI agents: architecture, measured constants, commands, traps, decisions. |
| `Dockerfile` | 27 | 1.2 | Builds image traffic-app:v1 on python:3.11-slim; runs app/main.py under uvicorn. |
| `MIGRATION_NOTES.md` | 130 | 6.9 | Handoff record for the Streamlit -> Next.js/Vercel migration. |
| `Makefile` | 178 | 8.2 | Every operational command as a named target; ports declared once at the top. |
| `PROJECT_EXTRACT.md` | 9,320 | 408.3 | This document. |
| `README.md` | 278 | 12.8 | Human-facing project write-up with the measured A/B results and limitations. |
| `analyze.py` | 197 | 8.4 | Scores the A/B benchmark from bench/*.json + Prometheus -> results*.md + comparison*.png. |
| `app/main.py` | 65 | 2.5 | The FastAPI app under test. CPU-bound /work, async /healthz, /metrics for Prometheus. |
| `app/requirements.txt` | 6 | 0.3 | Dependencies baked INTO the container only (not the host pipeline). |
| `bench/A1.end` | 1 | 0.0 | UNIX epoch seconds when run A1 ended. |
| `bench/A1.json` | 1 | 2.3 | k6 summary JSON for benchmark run A1. |
| `bench/A1.start` | 1 | 0.0 | UNIX epoch seconds when run A1 started. |
| `bench/A1r.end` | 1 | 0.0 | UNIX epoch seconds when run A1r ended. |
| `bench/A1r.json` | 1 | 2.3 | k6 summary JSON for benchmark run A1r. |
| `bench/A1r.start` | 1 | 0.0 | UNIX epoch seconds when run A1r started. |
| `bench/A2.end` | 1 | 0.0 | UNIX epoch seconds when run A2 ended. |
| `bench/A2.json` | 1 | 2.3 | k6 summary JSON for benchmark run A2. |
| `bench/A2.start` | 1 | 0.0 | UNIX epoch seconds when run A2 started. |
| `bench/A2r.end` | 1 | 0.0 | UNIX epoch seconds when run A2r ended. |
| `bench/A2r.json` | 1 | 2.3 | k6 summary JSON for benchmark run A2r. |
| `bench/A2r.start` | 1 | 0.0 | UNIX epoch seconds when run A2r started. |
| `bench/A3.end` | 1 | 0.0 | UNIX epoch seconds when run A3 ended. |
| `bench/A3.json` | 1 | 2.2 | k6 summary JSON for benchmark run A3. |
| `bench/A3.start` | 1 | 0.0 | UNIX epoch seconds when run A3 started. |
| `bench/A3r.end` | 1 | 0.0 | UNIX epoch seconds when run A3r ended. |
| `bench/A3r.json` | 1 | 2.3 | k6 summary JSON for benchmark run A3r. |
| `bench/A3r.start` | 1 | 0.0 | UNIX epoch seconds when run A3r started. |
| `bench/B1.end` | 1 | 0.0 | UNIX epoch seconds when run B1 ended. |
| `bench/B1.json` | 1 | 2.3 | k6 summary JSON for benchmark run B1. |
| `bench/B1.start` | 1 | 0.0 | UNIX epoch seconds when run B1 started. |
| `bench/B1r.end` | 1 | 0.0 | UNIX epoch seconds when run B1r ended. |
| `bench/B1r.json` | 1 | 2.3 | k6 summary JSON for benchmark run B1r. |
| `bench/B1r.start` | 1 | 0.0 | UNIX epoch seconds when run B1r started. |
| `bench/B2.end` | 1 | 0.0 | UNIX epoch seconds when run B2 ended. |
| `bench/B2.json` | 1 | 2.3 | k6 summary JSON for benchmark run B2. |
| `bench/B2.start` | 1 | 0.0 | UNIX epoch seconds when run B2 started. |
| `bench/B2r.end` | 1 | 0.0 | UNIX epoch seconds when run B2r ended. |
| `bench/B2r.json` | 1 | 2.3 | k6 summary JSON for benchmark run B2r. |
| `bench/B2r.start` | 1 | 0.0 | UNIX epoch seconds when run B2r started. |
| `bench/B3.end` | 1 | 0.0 | UNIX epoch seconds when run B3 ended. |
| `bench/B3.json` | 1 | 2.3 | k6 summary JSON for benchmark run B3. |
| `bench/B3.start` | 1 | 0.0 | UNIX epoch seconds when run B3 started. |
| `bench/B3r.end` | 1 | 0.0 | UNIX epoch seconds when run B3r ended. |
| `bench/B3r.json` | 1 | 2.3 | k6 summary JSON for benchmark run B3r. |
| `bench/B3r.start` | 1 | 0.0 | UNIX epoch seconds when run B3r started. |
| `bench/C1.end` | 1 | 0.0 | UNIX epoch seconds when run C1 ended. |
| `bench/C1.json` | 1 | 2.3 | k6 summary JSON for benchmark run C1. |
| `bench/C1.start` | 1 | 0.0 | UNIX epoch seconds when run C1 started. |
| `bench/C2.end` | 1 | 0.0 | UNIX epoch seconds when run C2 ended. |
| `bench/C2.json` | 1 | 2.3 | k6 summary JSON for benchmark run C2. |
| `bench/C2.start` | 1 | 0.0 | UNIX epoch seconds when run C2 started. |
| `bench/C3.end` | 1 | 0.0 | UNIX epoch seconds when run C3 ended. |
| `bench/C3.json` | 1 | 2.3 | k6 summary JSON for benchmark run C3. |
| `bench/C3.start` | 1 | 0.0 | UNIX epoch seconds when run C3 started. |
| `bench/discarded/A1-4x-on-30.json` | 1 | 2.4 | Discarded benchmark run artefact (see bench/discarded/README.md). |
| `bench/discarded/A1.end` | 1 | 0.0 | Discarded benchmark run artefact (see bench/discarded/README.md). |
| `bench/discarded/A1.json` | 1 | 2.5 | Discarded benchmark run artefact (see bench/discarded/README.md). |
| `bench/discarded/A1.start` | 1 | 0.0 | Discarded benchmark run artefact (see bench/discarded/README.md). |
| `bench/discarded/README.md` | 23 | 1.1 | Why the discarded run was thrown out. |
| `bench/replay-step.json` | 4334 | 53.4 | Step runs (A1-A3,B1-B3,C1-C3) frozen out of Prometheus for the UI. |
| `bench/replay.json` | 2565 | 30.6 | Ramp runs (A1r,A2r,A3r,B1r,B2r,B3r) frozen out of Prometheus for the UI. |
| `collect.py` | 118 | 4.8 | Prometheus -> data/traffic.parquet. Idempotent, 6h overlapping re-read, EARLIEST cutoff. |
| `data/traffic.parquet` | 575 | 221.7 | The recorded request-rate history. NOT gitignored: Prometheus keeps 15d, this cannot be rebuilt. |
| `export_replay.py` | 150 | 5.9 | Freezes benchmark windows out of Prometheus into bench/replay*.json before 15d retention. |
| `k8s/deployment.yaml` | 79 | 3.4 | traffic-app Deployment: 2 replicas, requests==limits==400m, tuned readiness probe. |
| `k8s/hpa.yaml` | 56 | 2.5 | THE BASELINE ARM. HorizontalPodAutoscaler, CPU 90%, 2-20 replicas. |
| `k8s/load/k6-benchmark.yaml` | 43 | 1.5 | One Job per benchmark run; RUN name and SCRIPT are sed-substituted by make. |
| `k8s/load/k6-capacity.yaml` | 37 | 1.3 | One-off Job running capacity.js to find one pod's throughput knee. |
| `k8s/load/k6.yaml` | 72 | 2.8 | daily.js as a Deployment (k6-load); scale 0/1 to stop/start the training signal. |
| `k8s/service.yaml` | 20 | 0.6 | ClusterIP Service traffic-app:80 -> pod:8000. The only path load takes to pods. |
| `k8s/servicemonitor.yaml` | 30 | 1.4 | Tells the Prometheus operator to scrape the app; references the port by NAME. |
| `load/benchmark.js` | 94 | 4.2 | BENCHMARK scenario: instant 4x step. The unpredictable event. |
| `load/capacity.js` | 63 | 2.7 | Stepped arrival rate against one replica to find its capacity knee. |
| `load/daily.js` | 112 | 5.1 | 60-minute diurnal cycles with random spikes; every 7th cycle is light. The TRAINING signal. |
| `load/ramp.js` | 72 | 3.0 | BENCHMARK scenario: 20->80 req/s over 6 min. The predictable event. |
| `logs/decisions.csv` | 1006 | 58.9 | One row per controller decision every 30s: rate, prediction, pods, action, reason. |
| `models/forecaster.joblib` | 7786 | 1137.9 | Trained bundle {model, features, horizon, quantile, backend, trained_rows, trained_through}. |
| `models/retrain_history.jsonl` | 1 | 0.2 | One JSON line per retrain.py evaluation (promoted or declined). |
| `outputs/comparison-r.png` | 268 | 97.9 | A/B comparison chart for the RAMP scenario. |
| `outputs/comparison.png` | 191 | 88.9 | A/B comparison chart for the STEP scenario. |
| `outputs/feature_importance.csv` | 16 | 0.4 | LightGBM gain per feature, top 15. |
| `outputs/forecast.png` | 547 | 174.7 | Backtest forecast-vs-actual plot. |
| `outputs/results.csv` | 6 | 0.7 | Backtest scoreboard: one row per model, averaged across folds, sorted by cost. |
| `outputs/results_by_fold.csv` | 21 | 2.5 | Backtest scoreboard broken out per model per fold. |
| `requirements.txt` | 49 | 2.3 | HOST pipeline dependencies (pinned). Separate from app/requirements.txt. |
| `results-r.md` | 19 | 0.6 | Generated scoreboard for the RAMP scenario (two arms). Written by analyze.py. |
| `results.md` | 25 | 0.8 | Generated scoreboard for the STEP scenario (three arms). Written by analyze.py. |
| `retrain.py` | 183 | 8.2 | Trains a candidate model and promotes it only if it beats the live model on unseen data. |
| `src/backtest.py` | 163 | 6.2 | Runs the ladder across folds -> outputs/results.csv, results_by_fold.csv, forecast.png. |
| `src/config.py` | 53 | 2.4 | Single source of truth for every constant: step size, cycle shape, horizon, cost ratio, paths. |
| `src/controller.py` | 272 | 11.2 | The predictive autoscaler. Two modes: replicas and hpa-floor. |
| `src/evaluate.py` | 139 | 4.9 | Rolling-origin fold construction, the asymmetric cost metric, under/over error split. |
| `src/features.py` | 168 | 7.3 | to_grid() + build_table(). THE shared feature definition used by both training and serving. |
| `src/live.py` | 86 | 3.4 | Prometheus -> one inference-shaped feature row, with a freshness guard that can refuse. |
| `src/models.py` | 177 | 6.8 | Baseline ladder (naive/seasonal/moving-average) + LightGBM GBM + replicas_needed(). |
| `src/predictor.py` | 79 | 2.5 | Dry-run forecaster. The ONLY check for train/serve skew; changes nothing. |
| `src/train_final.py` | 59 | 1.9 | Retrains the chosen model on ALL data -> models/forecaster.joblib (a bundle). |
| `web/.gitignore` | 2 | 0.0 | Written by `vercel link`: ignores .vercel and .env*. |
| `web/app/benchmark/page.tsx` | 24 | 0.8 | Route `/benchmark` — server shell rendering the client BenchmarkView. |
| `web/app/globals.css` | 237 | 14.3 | The design system: tokens ported verbatim from the deleted dashboard.py. |
| `web/app/layout.tsx` | 23 | 1.1 | Root layout; self-hosts Newsreader / IBM Plex Sans / IBM Plex Mono via next/font. |
| `web/app/page.tsx` | 223 | 8.6 | Route `/` — Overview. Every figure computed at build time. |
| `web/components/BenchmarkView.tsx` | 237 | 9.6 | The interactive replay: scenario/run switches, playhead, Play, arm columns, charts, verdict. |
| `web/components/Chart.tsx` | 183 | 6.9 | Hand-rolled SVG chart: dash+colour+label keying, truncates at the playhead, ships a data table. |
| `web/components/Chrome.tsx` | 60 | 2.3 | Masthead, nav strip, spec strip, footnote. Shared by both routes. |
| `web/lib/data.ts` | 197 | 7.7 | ARMS/SCENARIOS constants and faithful ports of group_runs, arm_means, best_arm, value_at, decision_at. |
| `web/lib/types.ts` | 71 | 1.9 | TypeScript types derived from the actual shape of bench/replay*.json. |
| `web/next-env.d.ts` | 7 | 0.3 | Generated by Next.js. Not hand-edited. |
| `web/next.config.ts` | 15 | 0.5 | `output: 'export'` — fully static, no SSR, no API routes. |
| `web/package-lock.json` | 1377 | 44.1 | Exact dependency tree (Next 16.3.4, React 19.2.8). |
| `web/package.json` | 23 | 0.6 | npm manifest plus the data/dev/build scripts for the static site. |
| `web/public/data/backtest.json` | 67 | 1.6 | Generated from outputs/results.csv. Source of the computed 64.5% figure. |
| `web/public/data/replay-step.json` | 1 | 29.4 | Generated: minified bench/replay-step.json (step, 9 runs). |
| `web/public/data/replay.json` | 1 | 16.6 | Generated: minified bench/replay.json (ramp, 6 runs). |
| `web/scripts/build-data.mjs` | 103 | 4.0 | The ONLY deriver of site data from bench/ and outputs/. |
| `web/tsconfig.json` | 42 | 0.7 | TypeScript config; strict mode, `@/*` path alias. |

**Total files listed: 118**

## 1.2 Totals

| Metric | Value |
|---|---:|
| Total files (excluding the paths above) | 118 |
| Python lines of code (all `.py`, excluding `.venv`) | 1,909 |
| TypeScript / TSX / MJS lines (`web/`, excluding `node_modules`) | 1,420 |
| CSS lines (`web/app/globals.css`) | 237 |
| JavaScript lines (`load/*.js`) | 341 |
| YAML lines (`k8s/**/*.yaml`) | 337 |
| Markdown lines (all `.md`, excluding this file) | 775 |
| Total git commits | 35 (the migration below is uncommitted at extraction time) |

Python LOC fell from 2,909 to 1,909 because `dashboard.py` (1,000 lines) was deleted.
The web app replaces it with 1,420 lines of TypeScript plus 237 of CSS.

Excluded from the tree above, in addition to the earlier list: `web/node_modules/`,
`web/.next/`, `web/out/`, `web/.vercel/`, `web/tsconfig.tsbuildinfo`, `web/.env.local`.

Python line counts per file:

         197 ./analyze.py
          65 ./app/main.py
         118 ./collect.py
        1000 ./dashboard.py
         150 ./export_replay.py
         183 ./retrain.py
         163 ./src/backtest.py
          53 ./src/config.py
         272 ./src/controller.py
         139 ./src/evaluate.py
         168 ./src/features.py
          86 ./src/live.py
         177 ./src/models.py
          79 ./src/predictor.py
          59 ./src/train_final.py
        2909 total

## 1.3 `.gitignore` (verbatim)

```gitignore
# macOS writes this into every folder it opens in Finder. Pure noise.
.DS_Store

# Local Python environment: 500MB of arm64 binaries that would be wrong on any
# other machine anyway. requirements.txt is what makes the env reproducible.
.venv/
**/__pycache__/
*.pyc

# k6 writes its whole run log here, and it grows for days. nohup.out is the
# same idea when a background job's output is not redirected.
*.log
nohup.out

# REGENERABLE from data/traffic.parquet — outputs/ comes from backtest.py,
# models/ from train_final.py. Committing them would mean a stale model in the
# repo silently disagreeing with the code that produced it.
outputs/
models/

# Written by controller.py, one row per 30s decision. Per-run evidence, not
# source. The benchmark results that matter get summarised into results.md.
logs/

# NOT ignored: data/traffic.parquet. It is small (a few hundred KB) and it is
# the one artefact here that CANNOT be regenerated — Prometheus keeps only 15
# days, so once a scrape ages out, that history is gone for good.

# Editor and agent state — local to one machine, not part of the project.
.agents/
.claude/
```

## 1.4 Normally-ignored files that ARE committed

| Path | Tracked by git? | Why (reason stated in repo) |
|---|---|---|
| `data/traffic.parquet` | **YES** | `.gitignore` comment: *"NOT ignored: data/traffic.parquet. It is small (a few hundred KB) and it is the one artefact here that CANNOT be regenerated — Prometheus keeps only 15 days, so once a scrape ages out, that history is gone for good."* |
| `bench/replay.json` | **YES** | Same retention logic. `export_replay.py` docstring: *"Prometheus keeps 15 days. After that these windows are gone for good, and with them any chance of rebuilding the comparison. This script freezes them into the repo so the visualisation keeps working long after the cluster is switched off."* |
| `bench/replay-step.json` | **YES** | Same as above (step scenario). |
| `bench/*.json`, `bench/*.start`, `bench/*.end` | **YES** | Raw k6 summaries plus the epoch window needed to replay each run against Prometheus. |
| `results.md`, `results-r.md` | **YES** | Generated by `analyze.py`, but committed as the published scoreboard. |
| `models/forecaster.joblib` | **NO** (ignored by `models/`) | `.gitignore`: *"REGENERABLE from data/traffic.parquet ... Committing them would mean a stale model in the repo silently disagreeing with the code that produced it."* |
| `logs/decisions.csv` | **NO** (ignored by `logs/`) | `.gitignore`: *"Written by controller.py, one row per 30s decision. Per-run evidence, not source."* |
| `outputs/*` | **NO** (ignored by `outputs/`) | Regenerable from `data/traffic.parquet` via `src/backtest.py`. |

Note: `models/` and `logs/` are gitignored but **the files exist on disk** and are extracted in this document.

## 1.5 Full git history — `git log --oneline --stat` (oldest first)

All 35 commits below predate the Streamlit → Next.js migration, which is present in the
working tree but **not yet committed** at extraction time. `git status --short` reads:

```
 M .gitignore
 M CLAUDE.md
 M Makefile
 M README.md
 M requirements.txt
D  .streamlit/config.toml
D  .streamlit/credentials.toml
D  dashboard.py
?? MIGRATION_NOTES.md
?? PROJECT_EXTRACT.md
?? web/
```

```
1f3ac0a start
 README.md | 1 +
 1 file changed, 1 insertion(+)
6adcb7e app: FastAPI service with metrics
 CLAUDE.md                            |  97 +++++++++++++++++++++++++++++++++++
 app/__pycache__/main.cpython-314.pyc | Bin 0 -> 2238 bytes
 app/main.py                          |  59 +++++++++++++++++++++
 app/requirements.txt                 |   5 ++
 4 files changed, 161 insertions(+)
1ea4a6d app with metrics
 app/__pycache__/main.cpython-314.pyc | Bin 2238 -> 2435 bytes
 app/main.py                          |   6 ++++++
 app/requirements.txt                 |   1 +
 3 files changed, 7 insertions(+)
aad73fd docker: containerized app
 .dockerignore | 16 ++++++++++++++++
 Dockerfile    | 27 +++++++++++++++++++++++++++
 2 files changed, 43 insertions(+)
952df4d k8s: deployment and service manifests
 k8s/deployment.yaml | 53 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 k8s/service.yaml    | 20 ++++++++++++++++++++
 2 files changed, 73 insertions(+)
ea3d6a5 make: save common commands as targets
 Makefile | 35 +++++++++++++++++++++++++++++++++++
 1 file changed, 35 insertions(+)
532c77f k8s: ServiceMonitor for the traffic-app metrics endpoint
 k8s/servicemonitor.yaml | 30 ++++++++++++++++++++++++++++++
 1 file changed, 30 insertions(+)
8dd0b91 load: steady 2-minute k6 smoke script
 load/steady.js | 25 +++++++++++++++++++++++++
 1 file changed, 25 insertions(+)
54ba6f4 load: diurnal traffic generator for collecting history
 load/daily.js | 76 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 76 insertions(+)
a80908b collect: grid-align window, filter to /work; deps: host requirements
 CLAUDE.md          | 190 +++++++++++++++++++++++++++++++++++++++++++----------
 collect.py         |  98 +++++++++++++++++++++++++++
 requirements.txt   |  39 +++++++++++
 src/backtest.py    | 163 +++++++++++++++++++++++++++++++++++++++++++++
 src/config.py      |  48 ++++++++++++++
 src/controller.py  | 187 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 src/evaluate.py    | 139 +++++++++++++++++++++++++++++++++++++++
 src/features.py    | 139 +++++++++++++++++++++++++++++++++++++++
 src/live.py        |  65 ++++++++++++++++++
 src/models.py      | 177 +++++++++++++++++++++++++++++++++++++++++++++++++
 src/predictor.py   |  79 ++++++++++++++++++++++
 src/train_final.py |  55 ++++++++++++++++
 12 files changed, 1346 insertions(+), 33 deletions(-)
70607d5 collect: grid-align the query window and filter to /work
 .gitignore | 27 +++++++++++++++++++++++++++
 1 file changed, 27 insertions(+)
be0478a load: move k6 into the cluster; measure capacity and horizon
 Makefile                  | 41 ++++++++++++++++++++++--
 collect.py                | 15 ++++++++-
 k8s/hpa.yaml              | 39 ++++++++++++++++++++++
 k8s/load/k6-capacity.yaml | 37 +++++++++++++++++++++
 k8s/load/k6.yaml          | 66 ++++++++++++++++++++++++++++++++++++++
 load/capacity.js          | 63 ++++++++++++++++++++++++++++++++++++
 load/daily.js             | 82 ++++++++++++++++++++++++++++++++++-------------
 src/config.py             | 19 +++++++----
 src/controller.py         | 20 +++++++++---
 9 files changed, 344 insertions(+), 38 deletions(-)
6484c3b load: cut PEAK_RPS to 40, sized to how the HPA actually scales
 data/traffic.parquet | Bin 0 -> 4204 bytes
 k8s/load/k6.yaml     |  16 +++++++++++-----
 2 files changed, 11 insertions(+), 5 deletions(-)
af1e659 collect: advance EARLIEST past the PEAK_RPS regime change
 collect.py           |  13 ++++++++++---
 data/traffic.parquet | Bin 4204 -> 5974 bytes
 2 files changed, 10 insertions(+), 3 deletions(-)
99bdbbd k8s: requests=limits and HPA at 90% so both arms provision alike
 data/traffic.parquet | Bin 5974 -> 226985 bytes
 k8s/deployment.yaml  |  20 +++++++++++++++-----
 k8s/hpa.yaml         |  29 +++++++++++++++++++++++------
 3 files changed, 38 insertions(+), 11 deletions(-)
9466e86 features: share to_grid between training and serving; live: hold on broken windows
 src/features.py | 53 +++++++++++++++++++++++++++++++++--------------------
 src/live.py     | 25 +++++++++++++++++++++++--
 2 files changed, 56 insertions(+), 22 deletions(-)
a3f69fb bench: ramp A/B — p99 62% lower for 28% more pod-seconds
 Makefile                         |  35 +++++++-
 analyze.py                       | 185 +++++++++++++++++++++++++++++++++++++++
 bench/A1.end                     |   1 +
 bench/A1.json                    |   1 +
 bench/A1.start                   |   1 +
 bench/A1r.end                    |   1 +
 bench/A1r.json                   |   1 +
 bench/A1r.start                  |   1 +
 bench/A2.end                     |   1 +
 bench/A2.json                    |   1 +
 bench/A2.start                   |   1 +
 bench/A2r.end                    |   1 +
 bench/A2r.json                   |   1 +
 bench/A2r.start                  |   1 +
 bench/A3.end                     |   1 +
 bench/A3.json                    |   1 +
 bench/A3.start                   |   1 +
 bench/A3r.end                    |   1 +
 bench/A3r.json                   |   1 +
 bench/A3r.start                  |   1 +
 bench/B1.end                     |   1 +
 bench/B1.json                    |   1 +
 bench/B1.start                   |   1 +
 bench/B1r.end                    |   1 +
 bench/B1r.json                   |   1 +
 bench/B1r.start                  |   1 +
 bench/B2r.end                    |   1 +
 bench/B2r.json                   |   1 +
 bench/B2r.start                  |   1 +
 bench/B3r.end                    |   1 +
 bench/B3r.json                   |   1 +
 bench/B3r.start                  |   1 +
 bench/discarded/A1-4x-on-30.json |   1 +
 bench/discarded/A1.end           |   1 +
 bench/discarded/A1.json          |   1 +
 bench/discarded/A1.start         |   1 +
 bench/discarded/README.md        |  23 +++++
 k8s/deployment.yaml              |  16 ++++
 k8s/load/k6-benchmark.yaml       |  43 +++++++++
 load/benchmark.js                |  94 ++++++++++++++++++++
 load/ramp.js                     |  72 +++++++++++++++
 results-r.md                     |  19 ++++
 src/features.py                  |  28 ++++--
 43 files changed, 542 insertions(+), 7 deletions(-)
23705db docs: README with measured A/B results
 README.md | 197 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
 1 file changed, 196 insertions(+), 1 deletion(-)
89f238e docs: update CLAUDE.md with measured results and operational traps
 CLAUDE.md        | 139 +++++++++++++++++++++++++++++++++++++++----------------
 bench/demo.end   |   1 +
 bench/demo.json  |   1 +
 bench/demo.start |   1 +
 4 files changed, 103 insertions(+), 39 deletions(-)
96383d9 docs: README and CLAUDE.md with measured A/B results
 CLAUDE.md | 3 ++-
 README.md | 7 +++----
 2 files changed, 5 insertions(+), 5 deletions(-)
9575737 ui: streamlit dashboard — benchmark replay and live forecast
 Makefile          |   15 +-
 bench/replay.json | 2565 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 dashboard.py      |  286 ++++++
 export_replay.py  |  138 +++
 requirements.txt  |    8 +
 5 files changed, 3011 insertions(+), 1 deletion(-)
b5e0d35 ui: document the dashboard, make the Makefile find the venv
 .gitignore             |  4 ++++
 .streamlit/config.toml | 12 ++++++++++++
 Makefile               | 14 +++++++++++---
 README.md              | 21 +++++++++++++++++++++
 4 files changed, 48 insertions(+), 3 deletions(-)
cd0486e chore: remove compiled files, unused scripts and the demo run
 CLAUDE.md                            |   1 -
 app/__pycache__/main.cpython-314.pyc | Bin 2435 -> 0 bytes
 bench/demo.end                       |   1 -
 bench/demo.json                      |   1 -
 bench/demo.start                     |   1 -
 load/steady.js                       |  25 -------------------------
 6 files changed, 29 deletions(-)
aea1d86 chore: drop forward-app, move local dev off port 5000, remove unused files
 CLAUDE.md | 12 +++++++++---
 Makefile  | 16 +++++++++++-----
 README.md |  5 +++--
 3 files changed, 23 insertions(+), 10 deletions(-)
c3888c2 ui: prepare for Streamlit Cloud deploy
 .streamlit/config.toml |  3 ---
 CLAUDE.md              | 15 ++++++++++-----
 README.md              | 36 +++++++++++++++++++++++++-----------
 bench/B2.end           |  1 +
 bench/B2.json          |  1 +
 bench/B2.start         |  1 +
 bench/B3.end           |  1 +
 bench/B3.json          |  1 +
 bench/B3.start         |  1 +
 dashboard.py           | 38 ++++++++++++++++++++++++++++++++++++--
 packages.txt           |  4 ++++
 results.md             | 19 +++++++++++++++++++
 12 files changed, 100 insertions(+), 21 deletions(-)
7a95fb1 ui: suppress Streamlit's first-run prompt so the cloud app can start
 .streamlit/credentials.toml | 11 +++++++++++
 1 file changed, 11 insertions(+)
0a1670a ui: drop packages.txt (comments break apt), keep credentials fix
 packages.txt | 4 ----
 1 file changed, 4 deletions(-)
e2a6611 controller: add hpa-floor mode so the forecast cannot remove capacity
 src/controller.py | 105 ++++++++++++++++++++++++++++++++++++++++++++++--------
 1 file changed, 90 insertions(+), 15 deletions(-)
4e1e008 controller: hpa-floor mode cuts step p99 49% below the HPA; add retrain gate
 CLAUDE.md          |  19 +++++-
 Makefile           |  21 +++++-
 README.md          |  36 +++++++++--
 bench/C1.end       |   1 +
 bench/C1.json      |   1 +
 bench/C1.start     |   1 +
 bench/C2.end       |   1 +
 bench/C2.json      |   1 +
 bench/C2.start     |   1 +
 bench/C3.end       |   1 +
 bench/C3.json      |   1 +
 bench/C3.start     |   1 +
 retrain.py         | 183 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 src/train_final.py |   6 +-
 14 files changed, 264 insertions(+), 10 deletions(-)
fc05b61 ui: instrument-panel theme — arm colours, Archivo/JetBrains Mono, pod gauge
 .streamlit/config.toml |  55 +++++++++++++--
 dashboard.py           | 178 ++++++++++++++++++++++++++++++++++++++++++-------
 2 files changed, 204 insertions(+), 29 deletions(-)
58b94c2 css styling added
 dashboard.py | 19 +++++++++----------
 1 file changed, 9 insertions(+), 10 deletions(-)
ea39d6a ui background changes
 dashboard.py | 61 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--
 1 file changed, 59 insertions(+), 2 deletions(-)
be55ea5 analyze+ui: score the hpa-floor arm, replay the step scenario
 CLAUDE.md              |   24 +-
 Makefile               |    6 +-
 analyze.py             |   36 +-
 bench/replay-step.json | 4334 ++++++++++++++++++++++++++++++++++++++++++++++++
 dashboard.py           |  272 ++-
 export_replay.py       |   26 +-
 results.md             |    8 +-
 7 files changed, 4601 insertions(+), 105 deletions(-)
8b265eb readme: describe the scenario selector and the third arm
 README.md | 11 +++++++----
 1 file changed, 7 insertions(+), 4 deletions(-)
9c17bf4 ui: rebuild the dashboard as a document, not an app shell
 .streamlit/config.toml |   78 ++--
 dashboard.py           | 1020 +++++++++++++++++++++++++++++++++---------------
 2 files changed, 743 insertions(+), 355 deletions(-)
```

## 1.6 Full commit messages (oldest first, verbatim)

```
=== 1f3ac0a | 2026-08-13 | pavansai2608
start

=== 6adcb7e | 2026-08-13 | pavansai2608
app: FastAPI service with metrics

=== 1ea4a6d | 2026-08-13 | pavansai2608
app with metrics

=== aad73fd | 2026-08-13 | pavansai2608
docker: containerized app

=== 952df4d | 2026-08-13 | pavansai2608
k8s: deployment and service manifests
Deployment requests 200m CPU because HPA measures utilisation as a
percentage of requests — leave it unset and the baseline arm reports
<unknown> and never scales at all.

Readiness probe gates the deliberate 15s startup sleep, so the Service
routes only to pods that can actually serve. No liveness probe on
purpose: it would kill the container mid-boot.


=== ea3d6a5 | 2026-08-13 | pavansai2608
make: save common commands as targets
Ports are declared once at the top so the local run and the two
port-forward targets can never drift out of sync.


=== 532c77f | 2026-08-13 | pavansai2608
k8s: ServiceMonitor for the traffic-app metrics endpoint
Endpoint refers to the Service port by NAME ("http"), not number. A name
no service port matches is dropped silently by the operator — no error,
no failed target, the scrape just never happens.

Carries the release: monitoring label. Redundant against this install,
which set serviceMonitorSelector to {}, but keeps the manifest correct
under the chart's default discovery behaviour.


=== 8dd0b91 | 2026-08-13 | pavansai2608
load: steady 2-minute k6 smoke script
Five VUs against the port-forwarded Service. summaryTrendStats is
overridden because k6 prints p95 by default and never p99 — the metric
the whole benchmark is judged on.

Closed-loop by design: fine for generating history, wrong shape for the
A/B run, where a falling request rate would flatter the reactive arm.


=== 54ba6f4 | 2026-08-13 | pavansai2608
load: diurnal traffic generator for collecting history
Each 60-minute cycle is one simulated day: quiet, ramp, plateau, taper,
plus 2-3 random 3-4x spikes. Every 7th cycle runs at half load so the
model must key off day-of-week rather than only minute-of-day.

Stages are generated per minute at init, so CYCLES bounds the run at
~7 real days — k6 cannot take an unbounded stage list.


=== a80908b | 2026-08-19 | pavansai2608
collect: grid-align window, filter to /work; deps: host requirements

=== 70607d5 | 2026-08-19 | pavansai2608
collect: grid-align the query window and filter to /work
Two bugs found by actually running the collector against the cluster.

1. Every run passed a raw now() as end_time. Prometheus aligns query_range
   output to the start_time it is given, not to an absolute clock, so two runs
   a minute apart returned the same instants offset by a second. Nothing
   deduplicated: 327 rows became 658 with no new time covered. Snapping the
   window to a 15s epoch boundary makes repeated runs byte-identical, which is
   what the merge already assumed.

2. The unfiltered query counted /healthz probes and /metrics scrapes. Measured
   on the cluster: 0.667 and 0.133 req/s against 0.000 for /work -- 100% of the
   recorded signal was self-generated, and all of it scales with replica count.
   A controller trained on that would read its own probes as demand. src/live.py
   carries the identical query so train and serve cannot drift apart.

Also adds the host requirements.txt (pandas delegates to_parquet to pyarrow and
ships neither, which killed collect.py on its final line) and a .gitignore that
deliberately keeps data/traffic.parquet -- Prometheus retains 15 days, so that
file is the only artefact here that cannot be rebuilt.


=== be0478a | 2026-08-19 | pavansai2608
load: move k6 into the cluster; measure capacity and horizon
The load path could not have demonstrated the project's claim.

kubectl port-forward svc/traffic-app resolves the Service to ONE pod and pins
every request to it. Measured with 4 replicas Ready: 6.94 req/s on one pod,
0.00 on the other three. Adding pods cannot reduce latency if the pods you add
never receive traffic, so the A/B benchmark would have found no difference
between arms for a reason invisible in the results.

Running k6 in-cluster against the ClusterIP was necessary but not sufficient:
kube-proxy load balances per TCP CONNECTION, and k6 reuses keep-alive
connections, so one VU still pinned 13.05 req/s onto a single pod.
noConnectionReuse spreads it -- now 23.6/22.5/21.4/19.9/12.7% across 5 pods.
One generator holding one socket was the artefact; real services are reached
by many independent clients.

Compounding it, macOS Control Center holds port 5000 for AirPlay. Whenever the
forward dropped, k6 got 403s in 2ms instead of connection errors, spun to 12.5M
"completed iterations", and reported 0 interrupted while delivering nothing.

Also switches daily.js from ramping-vus to ramping-arrival-rate. Closed-loop
VUs make req/s = VUs / latency, and latency falls as pods are added -- the
recorded demand would have been partly an output of the autoscaler, and the
forecaster would have been learning its own control loop.

Both measured numbers that the design says must never be guessed:

  HORIZON_STEPS   6 -> 4    pod created->Ready 19s, 19s, 18s (+30s interval)
  CAPACITY_PER_POD 120 -> 20  p95 flat at 95ms through 20 req/s, 381ms at 24,
                              CPU pinned at the 400m limit throughout

The old 120 would have provisioned 6x too few pods for every forecast, and no
forecast metric would ever have shown it.

Adds k8s/hpa.yaml so the baseline arm is reproducible from the repo rather than
from shell history, and an EARLIEST cutoff in collect.py because deleting the
parquet cannot erase history Prometheus still serves on a 6h re-read.


=== 6484c3b | 2026-08-19 | pavansai2608
load: cut PEAK_RPS to 40, sized to how the HPA actually scales
At 100 req/s the HPA sat pinned at maxReplicas=20 continuously, which leaves it
no room to react to a spike -- the baseline arm cannot demonstrate reactive lag
if it is already at its ceiling before the spike arrives.

The cause is a mismatch the deployment has always had: requests.cpu is 200m but
limits.cpu is 400m, and the HPA scales on a percentage of the REQUEST. At 60%
it adds a pod every ~4.7 req/s while a pod can actually serve ~15. Measured:
20 pods at 123m each, every one of them 31% utilised, with the HPA reporting
58%/60% and considering itself on target.

40 keeps the whole dynamic range inside the 2..20 bounds for both arms and lets
the cluster fall back to MIN_PODS overnight.

Not addressed here, and it must be before the A/B runs: the two arms currently
provision to different targets (HPA to a CPU proxy, the controller to measured
capacity), so a benchmark today would compare provisioning levels rather than
reaction timing.


=== af1e659 | 2026-08-19 | pavansai2608
collect: advance EARLIEST past the PEAK_RPS regime change

=== 99bdbbd | 2026-08-22 | pavansai2608
k8s: requests=limits and HPA at 90% so both arms provision alike

=== 9466e86 | 2026-08-22 | pavansai2608
features: share to_grid between training and serving; live: hold on broken windows

=== a3f69fb | 2026-08-24 | pavansai2608
bench: ramp A/B — p99 62% lower for 28% more pod-seconds

=== 23705db | 2026-08-24 | pavansai2608
docs: README with measured A/B results

=== 89f238e | 2026-08-24 | pavansai2608
docs: update CLAUDE.md with measured results and operational traps

=== 96383d9 | 2026-08-24 | pavansai2608
docs: README and CLAUDE.md with measured A/B results

=== 9575737 | 2026-08-24 | pavansai2608
ui: streamlit dashboard — benchmark replay and live forecast

=== b5e0d35 | 2026-08-24 | pavansai2608
ui: document the dashboard, make the Makefile find the venv

=== cd0486e | 2026-08-29 | pavansai2608
chore: remove compiled files, unused scripts and the demo run

=== aea1d86 | 2026-08-29 | pavansai2608
chore: drop forward-app, move local dev off port 5000, remove unused files

=== c3888c2 | 2026-08-30 | pavansai2608
ui: prepare for Streamlit Cloud deploy

=== 7a95fb1 | 2026-08-30 | pavansai2608
ui: suppress Streamlit's first-run prompt so the cloud app can start

=== 0a1670a | 2026-08-30 | pavansai2608
ui: drop packages.txt (comments break apt), keep credentials fix

=== e2a6611 | 2026-08-30 | pavansai2608
controller: add hpa-floor mode so the forecast cannot remove capacity

=== 4e1e008 | 2026-08-30 | pavansai2608
controller: hpa-floor mode cuts step p99 49% below the HPA; add retrain gate

=== fc05b61 | 2026-08-30 | pavansai2608
ui: instrument-panel theme — arm colours, Archivo/JetBrains Mono, pod gauge

=== 58b94c2 | 2026-08-30 | pavansai2608
css styling added

=== ea39d6a | 2026-08-30 | pavansai2608
ui background changes

=== be55ea5 | 2026-08-30 | pavansai2608
analyze+ui: score the hpa-floor arm, replay the step scenario
analyze.py took two arms as given, so the hpa-floor result existed only as a
hand-typed table in README.md. It now scores an optional third arm (C runs,
step scenario only) against the baseline: 467 -> 240 ms, +43% compute.

The dashboard replayed the ramp alone, so the fix was absent from the UI.
Adds a scenario selector, decodes arms from the run-name prefix, and grows to
three columns when a third arm is present. Masthead figures are averaged from
the data rather than hardcoded — they reproduce the previous 479/183/62/+28.

Play was dead: the slider had a key, so Streamlit restored it from its own
state and ignored the value the button set.


=== 8b265eb | 2026-08-30 | pavansai2608
readme: describe the scenario selector and the third arm

=== 9c17bf4 | 2026-09-06 | pavansai2608
ui: rebuild the dashboard as a document, not an app shell
The previous layout was borrowed wholesale from another project: left sidebar,
brand block, nav list, stat rail. Replaced with a masthead, a nav strip and a
spec strip of the measured constants, with content in one measure below.

Adds an Overview page that answers what the benchmark found before showing any
controls, since the replay page assumes you already know what an arm and a run
are. Replay now leads with p99 at full width and pairs pods/traffic beneath it,
opens at the end of the run rather than on empty charts, and explains the three
arms and the two headline numbers up front.

Palette is drafting-grey stock with wine/teal/moss arms, all above 5:1 on both
the ground and the card fill; Newsreader for prose, IBM Plex Mono for figures.
Series carry a dash pattern as well as a colour so they survive greyscale and
overlap. Hover, active and focus states go only on controls.

Three Streamlit traps fixed along the way: an angle bracket anywhere inside the
injected stylesheet makes it drop the whole style element silently; the nav
radio dot is three divs deep and has a data-selected attribute; a blanket
font-family rule breaks Material icon ligatures.

```

## 1.7 Chronological timeline in plain English

**Phase 1 — build something worth scaling (2026-08-13, commits `1f3ac0a` → `54ba6f4`)**

1. `1f3ac0a` `start` — empty repository initialised.
2. `6adcb7e` / `1ea4a6d` — FastAPI service created with a Prometheus `/metrics` endpoint.
3. `aad73fd` — containerised as `traffic-app:v1`.
4. `952df4d` — Kubernetes Deployment + Service. Two decisions recorded in the message:
   CPU **requests** must be set or the HPA reports `<unknown>` and never scales; a
   readiness probe gates the deliberate 15s startup sleep; **no liveness probe on
   purpose**, because it would kill the container mid-boot.
5. `ea3d6a5` — Makefile; ports declared once at the top so local run and port-forwards
   cannot drift.
6. `532c77f` — ServiceMonitor. Records the trap that the endpoint must reference the
   Service port **by name** (`"http"`); a name no service port matches is **dropped
   silently** by the operator — no error, no failed target, the scrape just never happens.
7. `8dd0b91` — first k6 smoke script. `summaryTrendStats` overridden because k6 prints
   p95 by default and never p99, which is the metric the benchmark is judged on.
8. `54ba6f4` — `daily.js`, the diurnal training-signal generator: 60-minute cycles,
   2–3 random 3–4x spikes, every 7th cycle at half load so the model must key off
   day-of-week and not only minute-of-day.

**Phase 2 — discover the measurement was invalid (2026-08-19, commits `a80908b` → `af1e659`)**

9. `70607d5` — two bugs found by running the collector:
   (a) a raw `now()` end_time meant Prometheus returned the same instants offset by a
   second, so **327 rows became 658 with no new time covered**;
   (b) the unfiltered query counted `/healthz` and `/metrics` — measured at **0.667 and
   0.133 req/s against 0.000 for `/work`**, i.e. **100% of the recorded signal was
   self-generated** and scaled with replica count.
   Also adds host `requirements.txt` because pandas delegates `to_parquet` to pyarrow and
   ships neither, which killed `collect.py` on its final line.
10. `be0478a` — the load path itself could not have demonstrated the claim:
    - `kubectl port-forward svc/traffic-app` pins every request to ONE pod. Measured with
      4 replicas Ready: **6.94 req/s on one pod, 0.00 on the other three**.
    - Moving k6 in-cluster was necessary but not sufficient: kube-proxy balances per TCP
      **connection**, and keep-alive pinned **13.05 req/s** onto a single pod.
      `noConnectionReuse` spread it to **23.6 / 22.5 / 21.4 / 19.9 / 12.7 %** across 5 pods.
    - macOS Control Center holds port 5000 for AirPlay; when a forward dropped, k6 got
      403s in 2 ms instead of connection errors and spun to **12.5 M "completed
      iterations"** while delivering nothing.
    - `daily.js` switched from `ramping-vus` to `ramping-arrival-rate`, because closed-loop
      VUs make req/s = VUs ÷ latency, so recorded demand would partly be an output of the
      autoscaler and the forecaster would be learning its own control loop.
    - The two must-be-measured constants were measured:
      `HORIZON_STEPS` **6 → 4** (pod created→Ready 19s, 19s, 18s, plus the 30s interval);
      `CAPACITY_PER_POD` **120 → 20** (p95 flat at 95 ms through 20 req/s, 381 ms at 24).
      The old 120 would have provisioned **6x too few pods** for every forecast.
11. `6484c3b` — `PEAK_RPS` cut from 100 to 40. At 100 the HPA sat pinned at
    `maxReplicas=20` continuously, leaving no room to react. Root cause: `requests.cpu`
    200m vs `limits.cpu` 400m — measured **20 pods at 123m each, all 31% utilised, with
    the HPA reporting 58%/60% and considering itself on target**.
12. `af1e659` — `EARLIEST` cutoff advanced past the PEAK_RPS regime change.

**Phase 3 — make the A/B fair, then run it (2026-08-22 → 2026-08-24)**

13. `99bdbbd` — `requests == limits` and HPA target 90%, so both arms provision alike.
14. `9466e86` — `to_grid()` extracted and shared between training and serving; `live.py`
    gains a freshness guard that holds on broken windows. (This is train/serve skew bug #1.)
15. `a3f69fb` — **the ramp A/B result: p99 62% lower for 28% more pod-seconds.**
16. `23705db`, `89f238e`, `96383d9` — README and CLAUDE.md written with measured results.
17. `9575737`, `b5e0d35` — the Streamlit dashboard (benchmark replay + live forecast).

**Phase 4 — cleanup and deploy prep (2026-08-29 → 2026-08-30)**

18. `cd0486e` — removed compiled files, unused scripts, the demo run.
19. `aea1d86` — dropped `forward-app` entirely (it was the port-forward trap), moved local
    dev off port 5000 (the AirPlay trap).
20. `c3888c2`, `7a95fb1`, `0a1670a` — Streamlit Cloud deploy prep; `credentials.toml` with
    an empty email suppresses the first-run prompt; `packages.txt` dropped because comments
    break apt.

**Phase 5 — the failure, and the fix (2026-08-30)**

21. `e2a6611` — `hpa-floor` mode added so the forecast cannot remove capacity.
22. `4e1e008` — **hpa-floor mode cuts step p99 49% below the HPA**; retrain gate added.
23. `fc05b61`, `58b94c2`, `ea39d6a` — dashboard theming iterations.
24. `be55ea5` — `analyze.py` taught the third arm (the hpa-floor result had existed only as
    a hand-typed table in README.md): **467 → 240 ms, +43% compute**. Dashboard gains a
    scenario selector and a third column. Fixed a dead Play button (the slider had a `key`,
    so Streamlit restored it from its own state and ignored the value the button set).
25. `8b265eb` — README describes the scenario selector and the third arm.

**Phase 6 — UI rebuild (2026-09-06)**

26. `9c17bf4` — dashboard rebuilt as a document rather than an app shell. Adds an Overview
    page. Three Streamlit traps recorded: an angle bracket anywhere inside the injected
    stylesheet makes Streamlit drop the whole style element silently; the nav radio dot is
    three divs deep and has a `data-selected` attribute; a blanket `font-family` rule breaks
    Material icon ligatures.

**Phase 7 — the public artefact leaves Python (2026-09-07, uncommitted working tree)**

27. The Streamlit dashboard was replaced as the **publicly deployed** artefact by a static
    Next.js app in `web/`, deployed to Vercel at
    **https://predictive-autoscaling.vercel.app**.
    - Only two of the three pages could migrate. Overview and Benchmark replay read nothing
      but `bench/replay*.json`, so they are genuinely static. **Live forecast cannot be
      hosted**: it needs Prometheus on `localhost:9090` and the LightGBM booster loaded
      in-process, and Vercel is serverless with neither.
    - `dashboard.py` (1,000 lines) and `.streamlit/` were **deleted outright**, and
      `streamlit==1.62.0` / `altair==6.2.2` dropped from `requirements.txt`. Verified safe
      first: `dashboard.py` was the sole importer of both packages, nothing imported it, and
      `CLAUDE.md` names **`src/predictor.py`** — not the dashboard — as the check for
      train/serve skew. `predictor.py` is untouched and runs the identical live path.
    - A known bug was fixed in passing: the Overview page had **hardcoded the string
      "64.5% lower cost"**. It is now computed as
      `(1 - gbm_q0.9.cost / naive.cost) x 100` = `1 - 4294.809/12093.794` = **64.5%**,
      derived from `outputs/results.csv` by `web/scripts/build-data.mjs`.
    - Design language preserved exactly: the same paper/ink tokens and the same
      wine/teal/moss arm colours, with the line-dash keying carried over and extended with
      direct end-of-line labels, because that triad fails a deuteranopia separation check on
      colour alone.
    - Measured after deploy: Lighthouse **Performance 100, Accessibility 100** on both
      routes, CLS 0, TBT 0 ms.

## 1.8 `README.md` (verbatim, as updated by the migration)

````markdown
# Predictive Autoscaling for Kubernetes

Forecast a service's request rate 60 seconds ahead and scale the deployment before
the traffic arrives — then measure whether it actually helps, against stock HPA
under identical load.

**[Live report → predictive-autoscaling.vercel.app](https://predictive-autoscaling.vercel.app)**
— the measured results and a second-by-second replay of any run, no cluster required.

**Result: p99 latency 62% lower than Kubernetes' built-in autoscaler, for 28% more
pod-seconds** — three runs per arm, identical traffic. That is on a load ramp the model
can anticipate. On an instantaneous spike it cannot, and it ties. Both results are below;
the second one is the more interesting of the two.

![Predictive vs reactive autoscaling](outputs/comparison-r.png)

The lower panel is the mechanism. The predictive controller adds pods across
minutes 5–10 while load is still climbing. The HPA holds at 2 pods for that entire
stretch and reaches 3 only at minute 10 — after the plateau has arrived. The upper
panel is the consequence: the baseline's p99 peaks at 620 ms exactly when it
finally reacts.

## The problem

Kubernetes' HorizontalPodAutoscaler is reactive: it adds pods only *after* CPU has
already risen. On this cluster a new pod takes **19 seconds** to go from created to
Ready (measured over three pod deletions: 19 s, 19 s, 18 s — dominated by the app's
deliberate 15-second warm-up). So every traffic ramp is served by an under-scaled
service for as long as it takes the HPA to notice plus the time for pods to boot.

There is a second, subtler failure. The HPA scales on CPU as a percentage of the
pod's CPU *request*. Once a pod saturates its limit, utilisation reads 100% and
cannot go higher — a pod at 3x overload is indistinguishable from one at 1.01x. The
HPA can therefore only grow the replica count by `100/target` per cycle, so it
creeps rather than jumps. Measured during a 4x step: it reached 4 of the ~7 pods
needed and stopped.

## Architecture

```mermaid
flowchart TD
    K6["k6 load generator<br/>(runs in-cluster)"] -->|HTTP| SVC[Service traffic-app]
    SVC --> POD["FastAPI pods<br/>CPU-bound, 15s warm-up"]
    POD -->|/metrics| PROM[Prometheus<br/>15s scrape]
    PROM --> COLLECT["collect.py<br/>→ data/traffic.parquet"]
    COLLECT --> FEAT["features.py<br/>lags, rolling stats, clock"]
    FEAT --> BT["backtest.py<br/>rolling-origin, ranked by cost"]
    FEAT --> TRAIN["train_final.py<br/>→ forecaster.joblib"]
    PROM --> LIVE["live.py<br/>one feature row"]
    TRAIN --> CTRL
    LIVE --> CTRL["controller.py<br/>forecast → replica count"]
    CTRL -->|"scale API"| POD
```

`features.py:build_table` is called by **both** the training path and the inference
path. That shared call is the design's load-bearing element: if the two ever built
features differently, the model would be silently asked a different question at
serve time than it learned. Two such bugs were found and fixed during development —
see Limitations.

## Results

### The forecast

Rolling-origin backtest, 4 folds, 12,277 rows (51 hours of collected traffic).
Ranked by **cost**, defined as `10 × under-provisioning + 1 × over-provisioning`,
because being short of capacity costs user-visible latency while being long costs a
little compute.

| model | MAE | MAE sd | under | over | cost | vs naive |
|---|---|---|---|---|---|---|
| **gbm_q0.90** | 4.77 | 0.34 | 223 | 2068 | **4,295** | **64.5% lower** |
| gbm (mean) | 2.24 | 0.24 | 507 | 566 | 5,636 | 53.4% lower |
| naive | 4.65 | 0.19 | 1096 | 1136 | 12,094 | — |
| moving avg (3 min) | 6.92 | 0.45 | 1625 | 1696 | 17,944 | 48.4% worse |
| seasonal naive | 9.87 | 1.15 | 2291 | 2448 | 25,359 | 110% worse |

The most instructive row is the second. **The mean-targeting GBM has less than half
the MAE of the winner and costs 31% more.** Targeting the 90th percentile cuts
under-provisioning from 507 to 223 and pays for it with surplus capacity worth a
tenth as much per unit. A model selected on MAE would have picked the wrong one.

Seasonal naive finishes last because the synthetic traffic places 2–3 spikes at
*random* minutes each cycle, so "same time yesterday" imports yesterday's spike into
today. That is a fact about the data, and worth stating rather than hiding.

### The benchmark

Identical 20-minute k6 scenario, zero randomness, three runs per arm. Load is
offered at a fixed *arrival rate* rather than by virtual users, so both arms are
given exactly the same work — with closed-loop VUs the better-scaling arm would
serve more requests and the latency comparison would be between different workloads.

**Ramp scenario** — 20 → 80 req/s over 6 minutes, hold, ramp down:

| arm | p50 | p95 | **p99** | max | pod-seconds | failed |
|---|---|---|---|---|---|---|
| Baseline (HPA) | 73 ms | 279 ms | **479 ms** | 1021 ms | 3,053 | 0.00% |
| Predictive | 51 ms | 132 ms | **183 ms** | 385 ms | 3,907 | 0.00% |

Per-run p99 — baseline 473 / 561 / 404 ms; predictive 175 / 186 / 188 ms. The
predictive arm is tighter as well as lower, which is what distinguishes a policy
difference from luck.

**Step scenario** — instantaneous 4x jump, no precursor:

| arm | runs | p99 | pods reached |
|---|---|---|---|
| Baseline (HPA) | 3 | **467 ms** | 3 |
| Predictive | 3 | 655 ms | 5 |

**In its original form predictive was 40% worse here**, and the pod traces said why.
It was not losing on the way up — it reached 5 pods where the HPA managed 3. It lost on
the way *down*:

```
                   minute 5 ─┐            ┌─ spike ends
baseline    2222222222222222222333333333333333333333333322222
predictive  2222222222222222222455555555443332222222222222222
                                 ↑ up to 5   ↑ already cutting, spike still running
```

Around minute 8 the forecast sees the spike ending and starts removing pods — while
the spike runs to minute 9. It is back to the 2-pod floor by minute 11. The HPA, being
slow, holds 3 pods until minute 14 and coasts through the tail.

So on an event with no precursor the forecast is wrong about the *end* as well as the
start, and withdrawing capacity early costs more than adding it late. `MAX_SCALE_DOWN_
PER_CYCLE = 1` damps this and is not enough at a 30 s interval.

The fix is not a better model. It is to run the HPA *underneath* the controller: the
forecast sets the HPA's `minReplicas` instead of the replica count, so it can add
capacity early but only real CPU can take it away. That is `MODE=hpa-floor` in
[controller.py](src/controller.py), and it is how AWS and KEDA compose predictive with
reactive scaling rather than replacing one with the other.

Measured, same scenario, three runs each:

| arm | p99 per run | mean p99 | pod-seconds |
|---|---|---|---|
| HPA alone | 493 / 540 / 369 | 467 ms | 2,993 |
| Predictive, owns replicas | 522 / 565 / 879 | 655 ms *(40% worse)* | 3,080 |
| **Predictive + HPA floor** | 256 / 238 / 228 | **240 ms** *(49% better)* | 4,273 *(+43%)* |

Composition beats both — and the run-to-run spread collapses from 357 ms wide to 28 ms.
The pod trace shows the mechanism: it reaches 5 pods and *holds* them through the tail
instead of cutting at minute 8.

```
HPA alone            22222222222222222223333333333333333333333322222
Predictive replicas  22222222222222222224555555554443222222222222222
Predictive + floor   22222333333333333334555555555555555555555522222
                                            ↑ holds capacity until the spike is over
```

The compute cost is real: 43% more pod-seconds than the HPA alone. Whether that trade is
worth making is a business question, not a technical one.

## Reproducing

Prerequisites: Docker, `kind`, `kubectl`, `helm`, `k6`, and a Python venv from
`requirements.txt`. `make forward-prom` is assumed wherever Prometheus is read. The
app itself needs no port-forward: k6 runs inside the cluster and reaches the Service
directly.

```bash
# 1. cluster + app
kind create cluster --name autoscale
make build && make load && make deploy

# 2. monitoring (kube-prometheus-stack, 15s scrape) and metrics-server

# 3. collect traffic history — leave running for 2+ days
make load-start
while true; do python collect.py; sleep 600; done

# 4. measure the two numbers that must never be guessed
kubectl delete -f k8s/hpa.yaml
kubectl scale deploy/traffic-app --replicas=1
make capacity                        # one pod's req/s at flat p95

# 5. evaluate and train
python src/backtest.py               # → outputs/results.csv, forecast.png
python src/train_final.py            # → models/forecaster.joblib
python src/predictor.py              # dry run: prints forecasts, changes nothing

# 6. benchmark, 3 runs per arm
make load-stop
kubectl apply -f k8s/hpa.yaml
make bench RUN=A1r SCRIPT=ramp.js    # ... A2r, A3r

kubectl delete -f k8s/hpa.yaml
CAPACITY_PER_POD=20 python src/controller.py &
make bench RUN=B1r SCRIPT=ramp.js    # ... B2r, B3r

python analyze.py                    # → results-r.md, outputs/comparison-r.png
```

## The report site

**Deployed: https://predictive-autoscaling.vercel.app** — a static Next.js app
(`web/`), two routes:

- **Overview** — the measured result, with every figure computed at build time from
  `bench/replay*.json` and `outputs/results.csv`. Nothing on the page is a typed-in number.
- **Benchmark replay** — scrub second by second through any recorded 20-minute run.
  Pick either scenario: the gradual ramp compares two arms, the instant spike compares
  three and shows the HPA-floor arm winning where forecasting alone lost. Charts draw
  only up to the playhead, so dragging it replays the run.

It reads only the recordings `export_replay.py` froze out of Prometheus, which are
committed. So it needs no cluster and keeps working long after Prometheus' 15-day
retention has discarded the original windows — which is the whole reason those files
exist.

```bash
make web-dev      # localhost:3000
make web-build    # static export -> web/out/
make web-deploy   # build, then vercel deploy --prod
```

**The live forecast is not deployed, and cannot be.** It needs Prometheus on
`localhost:9090` and the LightGBM booster loaded in-process; Vercel is serverless and
has neither. Stubbing it with canned numbers would defeat its only purpose, which is
catching train/serve skew. Locally it is:

```bash
make forward-prom          # terminal 1
python src/predictor.py    # terminal 2 — prints a forecast, changes nothing
```

Watch that the prediction *leads* the current rate rather than echoing it. If it just
mirrors "now", the model has degenerated to the naive baseline and something upstream
is wrong — that is exactly how the two train/serve bugs below were caught.

## Limitations

**The traffic is synthetic.** A scripted diurnal cycle with random spikes, not a
real production workload. The shape is learnable by construction; real traffic
carries structure this model has never been tested against.

**Spikes without leading indicators cannot be predicted.** Quantified above: the
model ties on an instantaneous step. The controller declines to act on unusable
input (no data, non-finite forecast, or a forecast more than 10x the recent max) and
logs a hold, leaving reactive scaling as the net underneath.

**One service, laptop scale.** A single deployment on a 10-core kind cluster,
2–20 pods. Nothing here has been tested with multiple services competing for nodes,
or where scheduling latency rather than pod boot time dominates.

**28% more compute.** The latency win is not free. Whether that trade is worth
making depends on the relative cost of latency and compute for the service in
question — which is exactly the `10:1` ratio the model's quantile encodes, and it is
an assumption, not a measurement.

**Two train/serve bugs were found by running the system, not by reading it.** The
inference path was not putting Prometheus data on the same 15-second grid the
training path uses, so every lag pointed at the wrong moment; and the cycle-position
features were anchored to the first row of the input frame, which is fixed in
training but slides at inference — leaving them frozen at a constant during serving.
Both produced *plausible* forecasts, roughly 45% too high, with no error anywhere.
The backtest cannot catch this class of bug, because the backtest only ever exercises
the training path.

## Stack

**Pipeline** — Python 3.14 · LightGBM (quantile objective) · pandas · pyarrow · FastAPI ·
Kubernetes (kind) · Prometheus + kube-state-metrics · k6 · Docker

**Report site** — Next.js 16 (App Router, static export) · React 19 · TypeScript ·
Vercel. Charts are hand-rolled SVG: the whole chart is four paths and some text, and
every library considered ships a theme that would fight the report styling.

`models.py` carries an untested scikit-learn fallback for environments without a
LightGBM wheel; every number here was produced by LightGBM.

Full design notes, including the decisions that were deliberately not revisited,
are in [CLAUDE.md](CLAUDE.md).
````

## 1.9 `CLAUDE.md` (verbatim, as updated by the migration)

````markdown
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

Both MEASURED on 2026-08-19 (src/config.py and commit be0478a both say so).
Re-measure if `WORK_MS`, `STARTUP_DELAY_S` or the CPU
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
predictor.py, analyze.py and export_replay.py all hardcode `localhost:9090`. The
public site does NOT — it reads committed JSON and never contacts the cluster:

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
python analyze.py --suffix '' --event 5,9   # step scenario, all three arms -> results.md
make replay-data                       # refreeze both scenarios -> bench/replay*.json
```

The public site (static Next.js in `web/`, deployed on Vercel). It reads ONLY the
committed `bench/replay*.json` plus a derived `backtest.json`, so it works with the
cluster switched off:

```bash
make web-data          # regenerate web/public/data/ from bench/ and outputs/results.csv
make web-dev           # next dev on localhost:3000
make web-build         # static export -> web/out/
make web-deploy        # web-build, then `vercel deploy --prod` from web/
```

`controller.py` also reads `DEPLOYMENT`, `NAMESPACE`, `INTERVAL_S`, `HEADROOM`, `MIN_PODS`,
`MAX_PODS` from the env, and appends every decision to `logs/decisions.csv`.

There is no test suite and no linter configured. The backtest **is** the correctness check for
the forecasting side: read `outputs/results.csv` top-down, lowest **cost** wins. If a baseline
beats the GBM, that is a real finding to report, not a bug to hide.

## Deployment

**Live: https://predictive-autoscaling.vercel.app**

| What | Where | Why |
|------|-------|-----|
| Overview + Benchmark replay | Vercel, static (`web/`, `output: 'export'`) | They read only committed JSON. No cluster, no model, no server. |
| Live forecast | **Local only**, `python src/predictor.py` | It needs Prometheus on `localhost:9090` AND the LightGBM booster loaded in-process. Vercel is serverless and has neither: there is no cluster to reach and nowhere to hold a 1.1 MB joblib model between requests. Faking it with canned numbers would make the one page whose job is to catch train/serve skew incapable of catching it. |

There is no Streamlit any more. `dashboard.py` and `.streamlit/` were deleted, and
`streamlit`/`altair` dropped from requirements.txt. `src/predictor.py` is what
exercises the live inference path now — and it always was the check CLAUDE.md
named for train/serve skew; the dashboard's live page was a second view of it.

The site's numbers are COMPUTED at build time, never typed in: `web/scripts/build-data.mjs`
derives them from `bench/replay*.json` and `outputs/results.csv`. That script is the only
thing allowed to copy a number out of the repo's artefacts.

## Results — MEASURED, 2026-08-30

Backtest, 4 folds, 12,277 rows: `gbm_q0.90` cost 4,295 vs naive 12,094 — **64.5% lower**.
The mean-targeting GBM has half the MAE (2.24 vs 4.77) and costs 31% MORE, which is the
clearest evidence in the project that the metric choice matters more than the model.

A/B benchmark, identical traffic, 3 runs per arm:

| scenario | p99 baseline | p99 predictive | pod-seconds | verdict |
|----------|--------------|----------------|-------------|---------|
| ramp (20->80 req/s over 6 min) | 479 ms | **183 ms** | 3,053 -> 3,907 | **62% lower, +28% compute** |
| step (instant 4x)              | 467 ms | 655 ms | 2,993 -> 3,080 | **40% WORSE** |

The step result is the honest half, and it is worse than "no advantage". The controller
is not losing on the way up (it reaches 5 pods where the HPA manages 3) — it loses on the
way DOWN. Around minute 8 the forecast sees the spike ending and starts cutting while the
spike runs to minute 9; it is back to MIN_PODS by minute 11, where the HPA holds 3 until
minute 14. Withdrawing capacity early costs more than adding it late, and
MAX_SCALE_DOWN_PER_CYCLE=1 is not enough damping at a 30s interval.

FIXED by composition, not a better model. `MODE=hpa-floor` makes the controller set the
HPA's minReplicas instead of the replica count: the forecast can raise capacity early,
but lowering the floor only PERMITS removal — the HPA still declines while CPU is high.

Step scenario, 3 runs each, measured 2026-08-30:

| arm                       | p99 per run     | mean   | pod-seconds |
|---------------------------|-----------------|--------|-------------|
| HPA alone                 | 493/540/369     | 467 ms | 2,993       |
| predictive owns replicas  | 522/565/879     | 655 ms | 3,080       |
| predictive + HPA floor    | 256/238/228     | 240 ms | 4,273       |

49% better than the HPA alone and 63% better than predictive alone, with the spread
collapsing from 357ms wide to 28ms. Costs 43% more compute than the HPA alone.

MODE=replicas is kept, not deleted: it is the arm the middle row measures, and removing
it would make that row unreproducible.

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

## Repo layout — state as of 2026-08-30

```
app/main.py            FastAPI app under test — deliberately CPU-bound and slow to start
Dockerfile             python:3.11-slim image `traffic-app:v1`
Makefile               every command above; ports defined once at the top
requirements.txt       HOST pipeline deps (pinned) — separate from app/requirements.txt
collect.py             Prometheus -> data/traffic.parquet
analyze.py             scores the A/B -> results-*.md + outputs/comparison-*.png.
                       Arms A/B are required, C (hpa-floor) is optional — it exists
                       for the step scenario only, and a missing arm is dropped.
export_replay.py       freezes benchmark windows out of Prometheus before the 15-day
                       retention eats them -> bench/replay*.json
retrain.py             scores a fresh candidate against the live model, swaps on a win
web/                   the PUBLIC site: static Next.js (App Router, TypeScript),
                       deployed on Vercel. Routes / (Overview) and /benchmark.
                       web/scripts/build-data.mjs is the ONLY thing that derives
                       numbers from bench/ and outputs/ — one source of truth.
                       Arm colours are wine #8c2f39 (A) / teal #15616d (B) /
                       moss #4a6b2a (C), each ALSO keyed by a line dash, because
                       the three fail a colourblind-separation check on colour alone.

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

data/traffic.parquet   12,281 rows, 51.2458h, 99.846% coverage — ONE 300s gap at
                       2026-08-21T18:33:00Z (19 rows missing of an expected 12,300).
                       NOT gitignored: Prometheus
                       keeps 15 days, so this is the one unreproducible artefact.
bench/*.json           benchmark runs + their start/end epochs. A/B/C = HPA alone /
                       predictive owns replicas / predictive + HPA floor; the `r`
                       suffix is the ramp scenario, no suffix is the step.
bench/replay*.json     those runs frozen out of Prometheus, so the UI outlives the
                       cluster. `replay.json` = ramp, `replay-step.json` = step.
bench/discarded/       runs thrown out, with README.md saying why
```

A screen recording was considered and deliberately skipped — the chart carries the same
evidence.

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
````

## 1.10 `MIGRATION_NOTES.md` (verbatim, new in this migration)

````markdown
# Migration notes — Streamlit → Next.js on Vercel

2026-09-07. Records only what changed in this migration.

**Production: https://predictive-autoscaling.vercel.app**

## What moved, what stayed, and why

| Page | Before | After | Reason |
|---|---|---|---|
| Overview | `dashboard.py` | **Deployed** — `/` | Reads only `bench/replay*.json`. Nothing to run. |
| Benchmark replay | `dashboard.py` | **Deployed** — `/benchmark` | Same: committed recordings only. |
| Live forecast | `dashboard.py` | **Deleted** | It needs Prometheus on `localhost:9090` and the LightGBM booster in-process. Vercel is serverless: no cluster to reach, nowhere to hold a 1.1 MB joblib model between requests. Faking it with canned numbers would defeat the one thing it is for — catching train/serve skew. |

The original brief said to keep `dashboard.py` stripped to the Live forecast page. Mid-task
the instruction changed to delete Streamlit entirely. That is safe, and here is the check
that made it safe: **`CLAUDE.md` names `src/predictor.py`, not `dashboard.py`, as the check
for train/serve skew.** `predictor.py` runs the identical path — `live.fetch_recent()` →
`features.build_table()` → `row.reindex(columns=bundle["features"])` → `model.predict()` —
prints a forecast and changes nothing. It is untouched. Verified before deleting:
`dashboard.py` was the sole importer of `streamlit` and `altair`, and nothing imported it.

Local replacement for the live view:

```bash
make forward-prom          # terminal 1
python src/predictor.py    # terminal 2
```

## Files

**Added** (22 source files under `web/`, excluding `node_modules/`, `.next/`, `out/`):

```
web/package.json                  web/next.config.ts         web/tsconfig.json
web/app/layout.tsx                web/app/page.tsx           web/app/benchmark/page.tsx
web/app/globals.css      (237)    web/lib/data.ts     (197)  web/lib/types.ts     (71)
web/components/Chart.tsx (183)    web/components/BenchmarkView.tsx (237)
web/components/Chrome.tsx (60)    web/scripts/build-data.mjs (103)
web/public/data/{replay.json, replay-step.json, backtest.json}   [generated, committed]
MIGRATION_NOTES.md
```

**Changed:** `Makefile` · `README.md` · `CLAUDE.md` · `requirements.txt` · `.gitignore`

**Deleted:** `dashboard.py` (1,000 lines) · `.streamlit/config.toml` · `.streamlit/credentials.toml`
· `streamlit==1.62.0` and `altair==6.2.2` from `requirements.txt`

**Untouched, as required:** `src/` · `app/` · `k8s/` · `load/` · `collect.py` · `analyze.py`
· `export_replay.py` · `retrain.py` · `data/` · `models/` · `bench/*.json`

## Make targets

| Target | Runs | Notes |
|---|---|---|
| `make web-data` | `node web/scripts/build-data.mjs` | Regenerates everything the site reads. |
| `make web-dev` | `web-data`, then `npm run dev` | localhost:3000 |
| `make web-build` | `web-data`, then `npm run build` | Static export → `web/out/` |
| `make web-deploy` | `web-build`, then `vercel deploy --prod` | From `web/`. |

Removed: `make ui`, and the `STREAMLIT` interpreter probe.

## Data pipeline — one source of truth

```
bench/replay.json  ──┐
bench/replay-step.json ─┼─► web/scripts/build-data.mjs ─► web/public/data/*.json ─► static import
outputs/results.csv ──┘        (the ONLY deriver)
```

`outputs/` is gitignored (regenerable via `src/backtest.py`), so `backtest.json` is derived
and committed. The replay files are re-emitted minified — 30.6 KB → 16.6 KB and
53.4 KB → 29.4 KB — because the sources are `indent=1` pretty-printed. No number is ever
hand-copied into the site.

## Numbers now COMPUTED that used to be hardcoded

| Figure | Was | Now |
|---|---|---|
| `64.5% lower cost` | **hardcoded string** in `dashboard.py` | `(1 - gbm_q0.9.cost / naive.cost) × 100` from `outputs/results.csv` — 4294.809 / 12093.794 → **64.5%** |
| Spec-strip `vs naive −64.5%` | hardcoded | same computation |
| Hero `62%` | computed | still computed, via a faithful port of `best_arm()` |
| `479 → 183 ms`, `3,053 → 3,907` | computed | still computed, via `arm_means()` |
| `gbm` is 53% better MAE / 31% worse cost | prose in the README only | computed in `build-data.mjs`, rendered on `/` |
| Per-run verdict sentences | computed | still computed, and pod-seconds now appears **in the same sentence** as latency |

## Lighthouse — actually measured

Lighthouse 12 CLI, `--preset=desktop`, against the production URL.

| Route | Performance | Accessibility | LCP | CLS | TBT |
|---|---|---|---|---|---|
| `/` | **100** | **100** | 0.5 s | 0 | 0 ms |
| `/benchmark` | **100** | **100** | 0.5 s | 0 | 0 ms |

Best Practices 100 and SEO 100 on `/benchmark` (Chrome DevTools MCP audit, 54 passed / 0 failed).
Total JS emitted across both routes: 732 KB uncompressed.

## Not at parity — be aware

1. **Live forecast is gone from the web entirely.** By design; `src/predictor.py` replaces it locally.
2. **A 1 ms rounding divergence from `results.md`, inherited.** `export_replay.py` writes
   `round(p99)` into each run summary, so anything reading the replay files averages integers.
   Floor-arm mean p99: the site shows **241 ms** (mean of 256/238/228), `results.md` shows
   **240 ms** (mean of the raw 255.51/237.84/227.58 from `bench/C*.json`). The Streamlit
   dashboard had exactly the same behaviour, so this is parity with what was replaced, not a
   regression — but it is a real disagreement between two published surfaces.
3. **No `prometheus connected/offline` chip.** Dropped deliberately: on a public deployment
   it could only ever say "offline" and would read as breakage.
4. **Play is 400 ms per tick**, matching the Streamlit `time.sleep(0.4)`. It is disabled
   under `prefers-reduced-motion`, where the slider remains fully usable.
5. **The Vercel↔GitHub auto-connect failed** during `vercel link` ("Failed to connect
   pavansai2608/predictive-autoscaling"). Deploys are CLI-driven via `make web-deploy`;
   there is no push-to-deploy. Connect the repo in the Vercel dashboard if you want that.

## Guesses / choices I made

- **Deployed via the `vercel` CLI, not the Vercel MCP server.** The MCP server is present but
  unauthorized in this session and the OAuth flow cannot run here. The CLI was already logged
  in as `pavansai2608` with exactly one scope (`pavan-fac7`) and no name collision, so no
  credential or account choice had to be guessed. Authorize the MCP connector if you want
  MCP-driven deploys.
- **Hand-rolled SVG charts** rather than Recharts/visx. The chart is four paths and some text;
  no library ships without a theme that would fight the report styling.
- **Colourblind mitigation carried over and extended.** Each series is keyed by stroke dash
  *and* colour *and* a direct end-of-line label, because the wine/teal/moss triad fails a
  deuteranopia separation check on colour alone. Every chart also has an `aria-label` and a
  `<details>` table of the underlying numbers.
- **The playhead opens at 1200 s** (the finished run), as the Streamlit version did — at t=0
  every figure reads zero and every chart is blank.
````

---

# 2. FULL SOURCE OF EVERY CODE FILE

Every file below is pasted complete and verbatim, including all comments. No elisions.

## 2.1 The application under test

### `app/main.py`

```python
"""The app under test.

Deliberately CPU-bound and slow to start. Those two properties are the whole
experiment: slow start is why reactive scaling arrives too late, and CPU-bound
means a pod has finite capacity, so adding pods actually buys throughput.
"""

import asyncio
import logging
import os
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# Read once at import. Env can't change inside a running pod, and /work sits on
# the latency path we're measuring — no getenv in the hot loop.
WORK_MS = int(os.getenv("WORK_MS", "30"))
STARTUP_DELAY_S = float(os.getenv("STARTUP_DELAY_S", "15"))

# uvicorn's own logger, so this lands in the same stream and format as
# "Application startup complete" instead of vanishing into an unconfigured root.
log = logging.getLogger("uvicorn.error")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # uvicorn awaits lifespan startup BEFORE binding the socket, so during this
    # sleep the port isn't even listening. That's the point: it reproduces the
    # real gap between "pod scheduled" and "pod can serve traffic", which is
    # exactly the delay stock HPA cannot hide. This value is also what sets the
    # forecast horizon N later on.
    log.info("warming up for %.1fs before serving...", STARTUP_DELAY_S)
    await asyncio.sleep(STARTUP_DELAY_S)
    log.info("ready: WORK_MS=%d STARTUP_DELAY_S=%.1f", WORK_MS, STARTUP_DELAY_S)
    yield


app = FastAPI(lifespan=lifespan)

# The hinge of the whole loop: Prometheus scrapes /metrics every 15s, and the
# http_requests_total counter exposed here is the raw signal collect.py records
# and the forecaster learns from. No metrics, no history, no model.
Instrumentator().instrument(app).expose(app)


# Sync def, NOT async def: FastAPI runs sync handlers in a threadpool. An async
# handler that busy-loops would pin the event loop, so a single in-flight
# request would stall every new connection — the benchmark would then measure
# event-loop starvation rather than pod capacity.
@app.get("/work")
def work():
    deadline = time.perf_counter() + WORK_MS / 1000.0
    while time.perf_counter() < deadline:
        pass  # a real CPU burn; sleeping would leave the pod idle and never scale
    return {"ok": True}


# async def and zero CPU: a sync handler would queue behind the threadpool once
# /work saturates it, so the probe would fail exactly when the pod is busiest
# and Kubernetes would restart pods mid-benchmark.
@app.get("/healthz")
async def healthz():
    return {"ok": True}
```

### `app/requirements.txt`

```text
# Plain uvicorn, not uvicorn[standard]: the extras (uvloop, httptools) have no
# Python 3.14 wheels guaranteed yet, and the pure-asyncio server is identical
# for both benchmark arms — so it can't bias the HPA-vs-predictive comparison.
fastapi
uvicorn
prometheus-fastapi-instrumentator
```

### `Dockerfile`

```dockerfile
# Python 3.11, not the 3.14 in .venv: every wheel we need has a 3.11 build, and
# this image only ever runs the app — the forecaster stays on the host.
FROM python:3.11-slim

# Unbuffered stdout, or uvicorn's logs sit in a pipe buffer and `kubectl logs`
# shows nothing while the pod warms up — exactly the window we need to watch.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# /srv rather than /app, so the package inside doesn't become /app/app. Keeping
# the repo-root layout means "app.main:app" is the same string here as locally.
WORKDIR /srv

# Requirements copied and installed before the source: pip only re-runs when the
# dependencies actually change, so editing main.py rebuilds in seconds instead
# of refetching every wheel.
COPY app/requirements.txt app/requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

COPY app/ app/

EXPOSE 8000

# Exec form, so uvicorn is PID 1 and receives SIGTERM directly. Under a shell it
# would not, and every scale-down would burn the full 30s termination grace
# period — which lands straight in the pod-seconds we are benchmarking.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### `.dockerignore`

```text
# The whole build context is uploaded to the Docker daemon on every build, so
# this file is mostly about speed — plus one correctness trap.

# .venv holds macOS/arm64 Python 3.14 binaries. In a linux 3.11 image they are
# broken as well as large, and must never shadow what pip installs.
.venv
.git

# Scraped traffic history grows with every collect run. Inside the context it
# would invalidate the cache and force a full rebuild each time it changed.
data
outputs
**/*.parquet

# A bare "__pycache__" would only match at the root; ** catches the nested ones.
**/__pycache__
```

### `requirements.txt`

```text
# HOST dependencies — the forecasting pipeline that runs on the Mac.
#
# Deliberately NOT app/requirements.txt: that one is COPYed into the Docker
# image, and the container only ever serves FastAPI. pyarrow alone would add
# ~100MB of Arrow libraries to every pod for code the pod never runs.
#
#     pip install -r requirements.txt
#
# Versions pinned to what is known to work on Python 3.14.2 / Apple Silicon.
# 3.14 is new enough that wheel availability is a real risk, so a set that
# actually resolved is worth recording rather than rediscovering.

# --- data + numerics ---------------------------------------------------------
pandas==3.0.5
numpy==2.5.2

# pandas does NOT write Parquet itself — it delegates to pyarrow or fastparquet
# and ships neither. Omitting this is not a missing nice-to-have: collect.py
# runs to completion and dies on its final line, AFTER the data is fetched.
# fastparquet is the fallback if a pyarrow wheel is ever unavailable.
pyarrow==25.0.1

# --- the metrics source ------------------------------------------------------
prometheus-api-client==0.7.2

# --- the model ---------------------------------------------------------------
# The quantile objective (alpha=0.90) is the reason for LightGBM specifically.
# models.py falls back to sklearn's HistGradientBoostingRegressor if this is
# absent, so the pipeline survives without it — but that path is untested here.
lightgbm==4.7.0
joblib==1.5.3

# --- output ------------------------------------------------------------------
matplotlib==3.11.1     # backtest.py writes outputs/forecast.png via the Agg backend

# --- the UI ------------------------------------------------------------------
# dashboard.py. Streamlit rather than a JS framework because this repo is Python
# end to end: the live page imports src/live.py and the trained model directly,
# which a separate frontend could only reach through an API written first.
# altair ships with streamlit but is pinned here because dashboard.py imports it.
streamlit==1.62.0
altair==6.2.2

# --- the hands ---------------------------------------------------------------
# controller.py patches deployment scale. Loaded from ~/.kube/config because
# this runs on the laptop, not inside a pod.
kubernetes==36.0.3
```

## 2.2 `src/` — the forecasting pipeline

### `src/config.py`

```python
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
# MEASURED on this cluster, 2026-08-19, not guessed. Three pods deleted and
# timed from creationTimestamp to the Ready condition flipping True:
#
#     19s, 19s, 18s  ->  average 18.7s
#
#     horizon_seconds = 18.7 (pod ready) + 30 (controller interval) = 48.7s
#     HORIZON_STEPS   = ceil(48.7 / 15) = 4
#
# The 19s is dominated by the app's own STARTUP_DELAY_S=15 (app/main.py), which
# is deliberate: uvicorn awaits the lifespan sleep BEFORE binding the socket, so
# the pod is unreachable for that whole window. Change that env var in
# k8s/deployment.yaml and this number must be re-measured.
#
# Forecasting further ahead than you can act on is wasted accuracy; forecasting
# less means capacity still arrives late. That is why this number is measured.
HORIZON_STEPS = 4

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
```

### `src/features.py`

```python
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
```

### `src/models.py`

```python
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
```

### `src/evaluate.py`

```python
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
```

### `src/backtest.py`

```python
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
```

### `src/train_final.py`

```python
"""Train the chosen model on ALL data and save it for the controller.

    python src/train_final.py

The backtest answers "does this work?" using held-out time. Once that question
is settled there is no reason to keep throwing away the most recent data - the
model that goes live is retrained on everything, which is also the freshest
picture of how the service currently behaves.

Saves the fitted model, the exact feature list, and the horizon together in one
file. Keeping them together matters: a model fed columns in a different order,
or asked for a horizon it was not trained on, fails silently rather than
loudly.
"""

from __future__ import annotations

import sys
from pathlib import Path

import joblib

sys.path.insert(0, str(Path(__file__).resolve().parent))

import config as C
import features as F
import models as M

ROOT = Path(__file__).resolve().parent.parent


def main(horizon: int = C.HORIZON_STEPS):
    raw = F.load_series(str(ROOT / C.DATA_FILE))
    table = F.usable(F.build_table(raw, horizon=horizon))
    cols = F.feature_columns(table)

    print(f"training on {len(table):,} rows, {len(cols)} features "
          f"(backend: {M.BACKEND}, horizon {horizon} steps)")

    model = M.GBM(quantile=C.QUANTILE).fit(table, table["target"], cols)

    (ROOT / "models").mkdir(exist_ok=True)
    out = ROOT / C.MODEL_FILE
    # trained_through is what makes an honest retrain gate possible later:
    # without it there is no way to tell which rows this model has already seen,
    # and scoring a model on its own training data flatters it enormously.
    joblib.dump({"model": model,
                 "features": cols,
                 "horizon": horizon,
                 "quantile": C.QUANTILE,
                 "backend": M.BACKEND,
                 "trained_rows": len(table),
                 "trained_through": table["ts"].max().isoformat()}, out)

    print(f"saved -> {out}")


if __name__ == "__main__":
    main()
```

### `src/live.py`

```python
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


# How much unbroken recent history a prediction requires, in steps. 120 steps
# is 30 minutes: the longest NON-seasonal lag and rolling window build_table()
# uses. The seasonal lags (240, 1680) are allowed to be missing - both model
# backends route around NaN - but if the last half hour is full of holes then
# lag_1, diff_1 and roll_mean_4 are all wrong, and those are the features the
# model leans on hardest (lag_1 alone carries 221k of gain).
RECENT_STEPS = 120


def latest_feature_row(df: pd.DataFrame, horizon: int):
    """Build features and return the single most recent row.

    That row has no `target` - the future has not happened yet - which is
    exactly the difference between training (rows with answers) and inference
    (one row without one).

    Returns (None, nan) when the recent window is too broken to answer from.
    Declining is a real answer: controller.py logs a hold and leaves the
    replica count alone, which is the correct move when the inputs are junk.
    """
    if df.empty:
        return None, float("nan")

    # SAME grid the training data was built on. Without this the lags are
    # positional over whatever rows Prometheus happened to return.
    grid = F.to_grid(df)

    recent = grid.tail(RECENT_STEPS)
    if len(recent) < RECENT_STEPS or recent["y"].isna().any():
        return None, float("nan")

    table = F.build_table(grid, horizon=horizon)
    row = table.iloc[[-1]]
    current_rate = float(grid["y"].iloc[-1])
    return row, current_rate
```

### `src/predictor.py`

```python
"""Watch the live traffic and print a forecast. Changes nothing.

    python src/predictor.py

Run this BEFORE the controller. It exercises the whole inference path -
Prometheus -> features -> model -> a number - while being completely harmless,
so you can sanity-check the predictions against reality with your own eyes
before letting them move pods around.

What to look for while a k6 ramp climbs: the predicted value should lead the
current one, not echo it. If prediction simply mirrors "now", the model is
behaving like the naive baseline and something upstream is wrong.

Ctrl+C to stop.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

import joblib
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

import config as C
import live

ROOT = Path(__file__).resolve().parent.parent
INTERVAL_S = 30


def load_bundle():
    path = ROOT / C.MODEL_FILE
    if not path.exists():
        sys.exit(f"ERROR: {path} not found. Run: python src/train_final.py")
    b = joblib.load(path)
    print(f"loaded model: backend={b['backend']}  horizon={b['horizon']} steps "
          f"({b['horizon'] * C.STEP_SECONDS}s)  q={b['quantile']}  "
          f"trained on {b['trained_rows']:,} rows\n")
    return b


def main():
    bundle = load_bundle()
    model, feats, horizon = bundle["model"], bundle["features"], bundle["horizon"]
    ahead_s = horizon * C.STEP_SECONDS

    while True:
        try:
            df = live.fetch_recent()
            row, now_rate = live.latest_feature_row(df, horizon)

            if row is None:
                print("  no data from Prometheus (is `make forward-prom` running?)")
            else:
                # Reindex to the training feature order. Columns arriving in a
                # different order is a silent, catastrophic failure mode - the
                # model would read lag_1 as roll_std_240 and never complain.
                X = row.reindex(columns=feats)
                pred = float(np.clip(model.predict(X)[0], 0, None))
                arrow = "UP  " if pred > now_rate * 1.1 else (
                        "DOWN" if pred < now_rate * 0.9 else "flat")
                print(f"  {row['ts'].iloc[0]:%H:%M:%S}  now={now_rate:7.2f} req/s   "
                      f"predicted(+{ahead_s}s)={pred:7.2f}   {arrow}")

        except Exception as e:
            print(f"  [skip] {type(e).__name__}: {e}")

        time.sleep(INTERVAL_S)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nstopped.")
```

### `src/controller.py`

```python
"""The predictive autoscaler. This is the file that makes the project a system.

    CAPACITY_PER_POD=120 python src/controller.py

Every 30 seconds: read live traffic -> forecast H steps ahead -> convert to a
pod count -> apply it to the deployment. Then log what it did and why.

The safety rules below are not decoration. A model can be wrong, and the
difference between a demo and something worth showing an engineer is whether
you planned for that. AWS runs predictive scaling ALONGSIDE reactive policies
rather than replacing them, for exactly this reason - when this controller
declines to act, the reactive HPA is the net underneath.

Ctrl+C to stop. Stopping the controller does not revert anything; pods stay
where they are until the HPA or you move them.
"""

from __future__ import annotations

import csv
import math
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
from kubernetes import client, config as kube_config

sys.path.insert(0, str(Path(__file__).resolve().parent))

import config as C
import live

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs/decisions.csv"

# --- knobs -------------------------------------------------------------------
DEPLOYMENT = os.getenv("DEPLOYMENT", "traffic-app")
NAMESPACE = os.getenv("NAMESPACE", "default")
INTERVAL_S = int(os.getenv("INTERVAL_S", "30"))

# Requests/second one pod serves comfortably. MEASURED 2026-08-19 with
# `make capacity` against a single replica (HPA deleted), stepping the arrival
# rate 4 -> 28 req/s:
#
#     offered   served   p95     cpu
#        12      12.0     95ms   0.35
#        16      16.0     95ms   0.40   <- pinned at the 400m limit
#        20      20.1     95ms   0.40   <- last flat step
#        24      24.1    381ms   0.40   <- knee: 4x latency, no more throughput
#
# So 20, not the 120 this used to default to. A wrong value here makes every
# decision wrong in the same direction and is invisible in the forecast
# metrics — the forecast stays correct while the pod count silently does not.
# Re-measure if WORK_MS or the CPU limit in k8s/deployment.yaml changes.
CAPACITY_PER_POD = float(os.getenv("CAPACITY_PER_POD", "20"))

HEADROOM = float(os.getenv("HEADROOM", "1.1"))
MIN_PODS = int(os.getenv("MIN_PODS", "2"))
MAX_PODS = int(os.getenv("MAX_PODS", "20"))

# Scale-down is capped at one pod per cycle; scale-up is uncapped. Deliberately
# asymmetric, and for the same reason the model targets q=0.90: being late to
# add capacity costs users, being slow to remove it costs pennies.
MAX_SCALE_DOWN_PER_CYCLE = 1

# HOW THE DECISION IS APPLIED. Two modes, and the difference is what happens on
# the way DOWN.
#
#   "replicas"  set the deployment's replica count directly. The forecast owns
#               the pod count outright, up AND down. This is what the first
#               benchmark measured.
#
#   "hpa-floor" set the HPA's minReplicas instead, leaving the HPA installed.
#               The forecast can raise capacity ahead of demand, but only real
#               CPU can take it away, because the HPA will not scale below its
#               own floor and will not scale down while utilisation says no.
#
# Measured on 2026-08-29, step scenario (instant 4x), 3 runs each: "replicas"
# scored p99 655ms against the plain HPA's 467ms — 40% WORSE. The pod traces
# show it is not losing on the way up (it reached 5 pods where the HPA managed
# 3) but on the way down: around minute 8 the forecast sees the spike ending and
# starts cutting, while the spike runs to minute 9, and it is back at MIN_PODS
# by minute 11 where the HPA held 3 until minute 14.
#
# Withdrawing capacity early costs more than adding it late, and a forecast has
# no more warning about an event's END than about its start. "hpa-floor" is the
# structural answer: never let the forecast remove what current load still
# needs. It is also how AWS and KEDA compose predictive with reactive scaling —
# alongside, not instead of.
MODE = os.getenv("MODE", "replicas")


def load_bundle():
    path = ROOT / C.MODEL_FILE
    if not path.exists():
        sys.exit(f"ERROR: {path} not found. Run: python src/train_final.py")
    return joblib.load(path)


def k8s_api():
    # Loaded from ~/.kube/config because this runs on the laptop, not inside a
    # pod. In-cluster it would be load_incluster_config() plus a ServiceAccount.
    kube_config.load_kube_config()
    return client.AppsV1Api(), client.AutoscalingV2Api()


def current_replicas(api) -> int:
    return int(api.read_namespaced_deployment_scale(DEPLOYMENT, NAMESPACE).spec.replicas or 0)


def set_replicas(api, n: int):
    api.patch_namespaced_deployment_scale(
        DEPLOYMENT, NAMESPACE, {"spec": {"replicas": int(n)}}
    )


def set_hpa_floor(hpa_api, n: int, max_pods: int):
    """Raise or lower the HPA's minReplicas — the forecast's only lever.

    minReplicas must stay <= maxReplicas or the API rejects the patch outright,
    so the clamp is not defensive tidiness.

    Note what this does NOT do: lowering the floor does not remove pods. It only
    permits the HPA to remove them, and the HPA will decline while CPU is still
    high. That asymmetry is the entire point of this mode.
    """
    n = max(1, min(int(n), int(max_pods)))
    hpa_api.patch_namespaced_horizontal_pod_autoscaler(
        DEPLOYMENT, NAMESPACE, {"spec": {"minReplicas": n}}
    )


def hpa_state(hpa_api):
    """(minReplicas, maxReplicas) of the live HPA, or None if it is not there."""
    try:
        h = hpa_api.read_namespaced_horizontal_pod_autoscaler(DEPLOYMENT, NAMESPACE)
        return int(h.spec.min_replicas or 1), int(h.spec.max_replicas)
    except Exception:
        return None


def log_row(**kw):
    LOG.parent.mkdir(exist_ok=True)
    new = not LOG.exists()
    with open(LOG, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "ts", "current_rate", "predicted", "pods_now", "pods_target",
            "action", "reason"])
        if new:
            w.writeheader()
        w.writerow(kw)


def main():
    bundle = load_bundle()
    model, feats, horizon = bundle["model"], bundle["features"], bundle["horizon"]
    api, hpa_api = k8s_api()

    if MODE == "hpa-floor" and hpa_state(hpa_api) is None:
        sys.exit("MODE=hpa-floor needs the HPA installed, and it is not.\n"
                 "  kubectl apply -f k8s/hpa.yaml")
    if MODE == "replicas" and hpa_state(hpa_api) is not None:
        # Both would fight over the same replica count every cycle and the
        # benchmark would measure the argument rather than either policy.
        sys.exit("MODE=replicas needs the HPA GONE, and it is installed.\n"
                 "  kubectl delete -f k8s/hpa.yaml")

    print(f"predictive autoscaler running\n"
          f"  deployment      : {DEPLOYMENT} (ns {NAMESPACE})\n"
          f"  mode            : {MODE}"
          f"{'  (sets the HPA floor; only CPU removes pods)' if MODE == 'hpa-floor' else '  (owns the replica count outright)'}\n"
          f"  horizon         : {horizon} steps = {horizon * C.STEP_SECONDS}s ahead\n"
          f"  capacity/pod    : {CAPACITY_PER_POD:g} req/s   headroom {HEADROOM:g}\n"
          f"  bounds          : {MIN_PODS}-{MAX_PODS} pods\n"
          f"  logging to      : {LOG}\n")

    recent_max = 0.0

    while True:
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        pods_now = -1
        try:
            pods_now = current_replicas(api)
            df = live.fetch_recent()
            row, now_rate = live.latest_feature_row(df, horizon)

            # ---- refuse to act on bad input --------------------------------
            if row is None or df.empty:
                raise ValueError("no data from Prometheus")

            X = row.reindex(columns=feats)
            pred = float(model.predict(X)[0])

            recent_max = max(recent_max * 0.99, float(df["y"].tail(240).max()))

            if not np.isfinite(pred) or pred < 0:
                reason = f"prediction not usable ({pred})"
                print(f"  {stamp}  HOLD  {reason}")
                log_row(ts=stamp, current_rate=round(now_rate, 3), predicted=pred,
                        pods_now=pods_now, pods_target=pods_now,
                        action="hold", reason=reason)
                time.sleep(INTERVAL_S)
                continue

            if recent_max > 0 and pred > 10 * recent_max:
                # An absurd forecast is more likely a broken feature row than a
                # real 10x event. Hand control back to the HPA rather than
                # launching twenty pods on a bad number.
                reason = f"prediction {pred:.1f} > 10x recent max {recent_max:.1f}"
                print(f"  {stamp}  HOLD  {reason}")
                log_row(ts=stamp, current_rate=round(now_rate, 3), predicted=round(pred, 3),
                        pods_now=pods_now, pods_target=pods_now,
                        action="hold", reason=reason)
                time.sleep(INTERVAL_S)
                continue

            # ---- forecast -> pods ------------------------------------------
            want = int(np.clip(math.ceil(pred * HEADROOM / CAPACITY_PER_POD),
                               MIN_PODS, MAX_PODS))

            if MODE == "hpa-floor":
                # No damping here. The floor may fall as fast as the forecast
                # likes, because lowering it cannot remove a pod — the HPA still
                # has to agree, and it will not while CPU is high. Damping the
                # floor would only delay the eventual scale-down for no benefit.
                floor, hmax = hpa_state(hpa_api)
                if want != floor:
                    set_hpa_floor(hpa_api, want, hmax)
                    action = "floor_up" if want > floor else "floor_down"
                else:
                    action = "none"
                reason = f"floor {floor}->{want}"
            else:
                if want < pods_now - MAX_SCALE_DOWN_PER_CYCLE:
                    # Damping. Without it a noisy forecast makes pods flap up and
                    # down every cycle, which looks broken and thrashes the app.
                    want = pods_now - MAX_SCALE_DOWN_PER_CYCLE
                    note = "damped"
                else:
                    note = "ok"

                if want == pods_now:
                    action, reason = "none", note
                else:
                    set_replicas(api, want)
                    action = "scale_up" if want > pods_now else "scale_down"
                    reason = note

            print(f"  {stamp}  now={now_rate:7.2f}  pred={pred:7.2f}  "
                  f"pods {pods_now}->{want}  {action}")
            log_row(ts=stamp, current_rate=round(now_rate, 3), predicted=round(pred, 3),
                    pods_now=pods_now, pods_target=want, action=action, reason=reason)

        except Exception as e:
            reason = f"{type(e).__name__}: {e}"
            print(f"  {stamp}  HOLD  {reason}")
            log_row(ts=stamp, current_rate="", predicted="", pods_now=pods_now,
                    pods_target=pods_now, action="hold", reason=reason)

        time.sleep(INTERVAL_S)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nstopped. Pods left as-is; re-enable the HPA if you want "
              "reactive scaling back.")
```

## 2.3 Top-level Python scripts

### `collect.py`

```python
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
# Moved forward a second time at 15:42Z, when PEAK_RPS dropped from 100 to 40.
# The amplitude change is a REGIME change, not noise: the same minute of the
# cycle meant 55.7 req/s on average before and 32.0 after. A model trained
# across it learns that identical clock features predict two different answers,
# which shows up as irreducible error and makes the backtest understate the
# model rather than overstate it.
#
# A cutoff is needed rather than just deleting the parquet: every run re-reads
# a 6h window, so deleted rows come straight back out of Prometheus. Once the
# discarded period is more than LOOKBACK old this line stops doing anything,
# and it is then safe to remove.
EARLIEST = pd.Timestamp("2026-08-19T15:42:00Z")

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
```

### `analyze.py`

```python
"""Score the A/B benchmark.

    python analyze.py                        # the ramp scenario (two arms)
    python analyze.py --suffix '' --event 5,9  # the step scenario (three arms)

Reads the k6 summaries in bench/, replays each run's window against Prometheus
for the replica count, and writes results.md plus outputs/comparison.png.

Two numbers, always together. A latency win bought with far more compute is not
a win, and a benchmark that reports only p99 is not an honest one — so
pod-seconds sits in the same table, not in a footnote.

Pod-seconds is not captured live: Prometheus already records the replica count
and keeps 15 days, so each run's start/end epoch (written by `make bench`) is
enough to reconstruct it afterwards.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import requests

ROOT = Path(__file__).resolve().parent
PROM = "http://localhost:9090"
STEP = 20  # seconds between samples when replaying a window

C_A = "#eb6834"   # baseline / HPA
C_B = "#2a78d6"   # predictive
C_C = "#1f9d55"   # predictive + HPA floor — the composition, not a third model


def prom_range(query: str, start: int, end: int, step: int = STEP):
    """One Prometheus series over a run window, as (elapsed_seconds, value)."""
    r = requests.get(f"{PROM}/api/v1/query_range", params={
        "query": query, "start": start, "end": end, "step": step}, timeout=30)
    res = r.json().get("data", {}).get("result", [])
    if not res:
        return np.array([]), np.array([])
    v = res[0]["values"]
    t = np.array([int(x[0]) - start for x in v], dtype=float)
    y = np.array([float(x[1]) for x in v], dtype=float)
    return t, y


def load_run(name: str) -> dict | None:
    """k6 summary + the replica trace Prometheus recorded during that window."""
    j = ROOT / "bench" / f"{name}.json"
    s, e = ROOT / "bench" / f"{name}.start", ROOT / "bench" / f"{name}.end"
    if not (j.exists() and s.exists() and e.exists()):
        return None

    m = json.loads(j.read_text())["metrics"]
    d = m["http_req_duration"]["values"]
    start, end = int(s.read_text()), int(e.read_text())

    tp, pods = prom_range(
        'kube_deployment_status_replicas_available{deployment="traffic-app"}',
        start, end)
    # Latency over time comes from the APP's histogram, not from k6: k6 only
    # emits aggregates at the end of a run, and the shape over time is the
    # whole point of the chart.
    tl, p99 = prom_range(
        'histogram_quantile(0.99, sum by (le) '
        '(rate(http_request_duration_seconds_bucket{handler="/work"}[1m])))',
        start, end)

    return {
        "name": name,
        "p50": d["p(50)"], "p95": d["p(95)"], "p99": d["p(99)"], "max": d["max"],
        "reqs": int(m["http_reqs"]["values"]["count"]),
        "failed": m["http_req_failed"]["values"]["rate"] * 100,
        # A run that dropped iterations offered LESS load than intended, at
        # exactly the moment the app was struggling — it is not comparable.
        "dropped": int(m.get("dropped_iterations", {}).get("values", {}).get("count", 0)),
        "pod_seconds": float(np.nansum(pods) * STEP) if pods.size else float("nan"),
        "t_pods": tp, "pods": pods,
        "t_lat": tl, "p99_series": p99,
    }


def mean_series(runs: list[dict], tkey: str, ykey: str):
    """Average the runs onto a common elapsed-time axis.

    Runs differ by a few seconds in length, so they are interpolated onto one
    grid rather than averaged index-by-index — otherwise a run that started
    two samples late would shift the whole curve.
    """
    runs = [r for r in runs if r[tkey].size]
    if not runs:
        return np.array([]), np.array([])
    grid = np.arange(0, min(r[tkey].max() for r in runs) + 1, STEP)
    stack = [np.interp(grid, r[tkey], r[ykey]) for r in runs]
    return grid, np.nanmean(stack, axis=0)


def main(suffix: str, event: tuple[int, int]):
    # Three arms, but only the first two are required. MODE=hpa-floor was run on
    # the step scenario only, so C1..C3 exist for suffix '' and not for 'r'. A
    # missing third arm is dropped rather than fatal — otherwise adding this arm
    # would have broken `analyze.py` for the ramp, which has no C runs and never
    # will.
    arms = {
        "Baseline (HPA)": [load_run(f"A{i}{suffix}") for i in (1, 2, 3)],
        "Predictive": [load_run(f"B{i}{suffix}") for i in (1, 2, 3)],
        "Predictive + HPA floor": [load_run(f"C{i}{suffix}") for i in (1, 2, 3)],
    }
    arms = {k: [r for r in v if r] for k, v in arms.items()}
    for k in ("Baseline (HPA)", "Predictive"):
        if not arms[k]:
            raise SystemExit(f"no runs found for {k} with suffix '{suffix}'")
    arms = {k: v for k, v in arms.items() if v}

    # ---- table --------------------------------------------------------------
    lines = ["| arm | runs | p50 | p95 | **p99** | max | pod-seconds | failed |",
             "|---|---|---|---|---|---|---|---|"]
    summary = {}
    for arm, runs in arms.items():
        f = lambda k: np.mean([r[k] for r in runs])
        summary[arm] = {"p99": f("p99"), "pods": f("pod_seconds")}
        lines.append(
            f"| {arm} | {len(runs)} | {f('p50'):.0f} ms | {f('p95'):.0f} ms | "
            f"**{f('p99'):.0f} ms** | {f('max'):.0f} ms | {f('pod_seconds'):.0f} | "
            f"{f('failed'):.2f}% |")

    # Every arm is scored against the baseline, not against the one before it:
    # "49% better than the HPA" is the claim a reader can check, and chaining
    # improvements arm-to-arm would let a bad middle arm flatter the last one.
    base = summary["Baseline (HPA)"]
    head = "\n\n".join(
        f"{arm}: p99 {base['p99']:.0f} ms -> {s['p99']:.0f} ms "
        f"({(1 - s['p99'] / base['p99']) * 100:.0f}% lower). "
        f"Pod-seconds: {base['pods']:.0f} -> {s['pods']:.0f} "
        f"({(s['pods'] / base['pods'] - 1) * 100:+.0f}%)."
        for arm, s in summary.items() if arm != "Baseline (HPA)")

    per_run = ["", "Individual runs:", "",
               "| run | p99 | pod-seconds | dropped |", "|---|---|---|---|"]
    for runs in arms.values():
        for r in runs:
            flag = "" if r["dropped"] == 0 else "  ⚠ INVALID"
            per_run.append(f"| {r['name']} | {r['p99']:.0f} ms | "
                           f"{r['pod_seconds']:.0f} | {r['dropped']}{flag} |")

    out = ROOT / f"results{'-' + suffix if suffix else ''}.md"
    out.write_text("# A/B benchmark\n\n" + head + "\n\n" + "\n".join(lines + per_run) + "\n")
    print("\n  " + head + "\n")
    print("\n".join(lines))

    # ---- chart --------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), sharex=True,
                                   gridspec_kw={"height_ratios": [2, 1]})
    for (arm, runs), c in zip(arms.items(), (C_A, C_B, C_C)):
        t, y = mean_series(runs, "t_lat", "p99_series")
        if t.size:
            ax1.plot(t / 60, y * 1000, color=c, lw=1.8, label=arm)
        t, y = mean_series(runs, "t_pods", "pods")
        if t.size:
            ax2.step(t / 60, y, color=c, lw=1.6, where="post", label=arm)

    for ax in (ax1, ax2):
        # Dashed lines bracket the event, so "did capacity arrive before the
        # traffic did" is answerable by eye rather than from the table.
        for x in event:
            ax.axvline(x, ls="--", lw=0.9, color="#898781")
        ax.grid(alpha=0.25, lw=0.6)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)

    ax1.set_ylabel("p99 latency (ms)")
    ax1.set_title(f"Predictive vs reactive autoscaling — mean of "
                  f"{min(len(v) for v in arms.values())} runs per arm", fontsize=12)
    ax1.legend(frameon=False, ncols=len(arms))
    ax2.set_ylabel("pods ready")
    ax2.set_xlabel("minutes into run")
    fig.tight_layout()
    (ROOT / "outputs").mkdir(exist_ok=True)
    png = ROOT / f"outputs/comparison{'-' + suffix if suffix else ''}.png"
    fig.savefig(png, dpi=150)
    plt.close(fig)
    print(f"\n  wrote {out.name} and {png.relative_to(ROOT)}\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Score the A/B benchmark.")
    ap.add_argument("--suffix", default="r",
                    help="run-name suffix: 'r' = ramp (default), 's'/'' = step")
    ap.add_argument("--event", default="4,14",
                    help="minutes bracketing the load event, for the chart")
    a = ap.parse_args()
    main(a.suffix, tuple(int(x) for x in a.event.split(",")))
```

### `export_replay.py`

```python
"""Pull the benchmark runs out of Prometheus into a single JSON file.

    python export_replay.py            # ramp runs   -> bench/replay.json
    python export_replay.py --runs A1,A2,A3,B1,B2,B3,C1,C2,C3 \
        --out replay-step.json --scenario "instant 4x step at minute 5, held 4 min"

Prometheus keeps 15 days. After that these windows are gone for good, and with
them any chance of rebuilding the comparison. This script freezes them into the
repo so the visualisation keeps working long after the cluster is switched off.

Every series here was recorded during a real run. Nothing is generated.
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent
PROM = "http://localhost:9090"
STEP = 20  # seconds — matches what analyze.py uses, so the numbers agree


def series(query: str, start: int, end: int) -> dict[int, float]:
    """One Prometheus series over a window, keyed by seconds since run start."""
    r = requests.get(f"{PROM}/api/v1/query_range", params={
        "query": query, "start": start, "end": end, "step": STEP}, timeout=30)
    res = r.json().get("data", {}).get("result", [])
    if not res:
        return {}
    return {int(t) - start: float(v) for t, v in res[0]["values"]}


# Run-name prefix -> which arm it is. The prefix is the only label a run
# carries: `make bench RUN=C1` writes bench/C1.json and nothing else records
# that C meant MODE=hpa-floor. Keep this table in step with the dashboard's.
ARM_OF_PREFIX = {"A": "baseline", "B": "predictive", "C": "floor"}


def decisions(start: int, end: int) -> list[dict]:
    """What the controller predicted during this window, from its own log.

    Only the B and C runs have these — the baseline has no forecaster running.
    This is the series that makes the point: it is the model's forecast,
    timestamped, next to what actually happened.
    """
    path = ROOT / "logs/decisions.csv"
    if not path.exists():
        return []
    out = []
    with open(path) as fh:
        for row in csv.DictReader(fh):
            try:
                ts = int(datetime.fromisoformat(row["ts"]).timestamp())
            except (ValueError, KeyError):
                continue
            if not (start <= ts <= end):
                continue
            try:
                out.append({
                    "t": ts - start,
                    "now": float(row["current_rate"]),
                    "pred": float(row["predicted"]),
                    "pods_now": int(row["pods_now"]),
                    "pods_target": int(row["pods_target"]),
                    "action": row["action"],
                })
            except (ValueError, TypeError):
                continue  # 'hold' rows have empty numeric fields
    return out


def export_run(name: str) -> dict | None:
    s, e = ROOT / f"bench/{name}.start", ROOT / f"bench/{name}.end"
    j = ROOT / f"bench/{name}.json"
    if not (s.exists() and e.exists() and j.exists()):
        print(f"  {name}: missing files, skipped")
        return None

    start, end = int(s.read_text()), int(e.read_text())
    rate = series('sum(rate(http_requests_total{handler="/work"}[1m]))', start, end)
    pods = series('kube_deployment_status_replicas_available'
                  '{deployment="traffic-app"}', start, end)
    # p99 from the APP's own histogram, so it is a value over time rather than
    # the single whole-run figure k6 reports at the end.
    p99 = series('histogram_quantile(0.99, sum by (le) (rate('
                 'http_request_duration_seconds_bucket{handler="/work"}[1m])))',
                 start, end)

    summary = json.loads(j.read_text())["metrics"]
    d = summary["http_req_duration"]["values"]

    grid = sorted(set(rate) | set(pods) | set(p99))
    if not grid:
        print(f"  {name}: no data in Prometheus (expired?), skipped")
        return None

    return {
        "name": name,
        "arm": ARM_OF_PREFIX.get(name[0], "baseline"),
        "t": grid,
        "rate": [round(rate.get(t, float("nan")), 2) if t in rate else None for t in grid],
        "pods": [int(pods[t]) if t in pods else None for t in grid],
        # milliseconds, so the page never has to do unit maths
        "p99": [round(p99[t] * 1000) if t in p99 and p99[t] == p99[t] else None
                for t in grid],
        "decisions": decisions(start, end),
        "summary": {
            "p50": round(d["p(50)"]), "p95": round(d["p(95)"]),
            "p99": round(d["p(99)"]), "max": round(d["max"]),
            "reqs": int(summary["http_reqs"]["values"]["count"]),
            "pod_seconds": round(sum(v for v in pods.values()) * STEP),
        },
        "started_utc": datetime.fromtimestamp(start, timezone.utc).isoformat(timespec="seconds"),
    }


def main(runs: list[str], out_name: str, scenario: str):
    data = [r for r in (export_run(n) for n in runs) if r]
    if not data:
        raise SystemExit("nothing exported — is `make forward-prom` running?")

    out = ROOT / "bench" / out_name
    out.write_text(json.dumps({
        "step_seconds": STEP,
        "scenario": scenario,
        "runs": data,
    }, indent=1))
    for r in data:
        print(f"  {r['name']:<5} {len(r['t']):>3} samples  "
              f"p99 {r['summary']['p99']:>4}ms  "
              f"{r['summary']['pod_seconds']:>5} pod-s  "
              f"{len(r['decisions']):>3} decisions")
    print(f"\n  wrote {out.relative_to(ROOT)} ({out.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Freeze benchmark runs into JSON.")
    ap.add_argument("--runs", default="A1r,A2r,A3r,B1r,B2r,B3r")
    ap.add_argument("--out", default="replay.json")
    ap.add_argument("--scenario",
                    default="ramp 20 -> 80 req/s over 6 min, hold 4 min, ramp down",
                    help="one line describing the load profile, shown in the UI")
    a = ap.parse_args()
    main(a.runs.split(","), a.out, a.scenario)
```

### `retrain.py`

```python
"""Retrain on fresh history — but only promote a model that is actually better.

    python retrain.py            # check, and replace the live model if it wins
    python retrain.py --dry-run  # score both, change nothing
    python retrain.py --force    # promote regardless (use when you know why)

Traffic patterns drift. A model trained in August is answering August's question,
and nothing in the system would tell you when that stops being the right one —
the forecast keeps looking reasonable while quietly getting worse. That is the
same class of silent failure as the train/serve bugs, and it needs the same
answer: measure, do not assume.

WHY THIS IS NOT JUST `train_final.py` ON A TIMER:

A scheduled retrain that always overwrites is a scheduled way to ship a worse
model. Fresh data can be worse data — a stretch where the laptop slept, or where
a benchmark run replaced the normal traffic pattern with a 20-minute square wave.
Both happened during this project.

So this script scores both models on the data collected SINCE the champion was
trained — rows neither has ever seen — and promotes only on a real improvement.
The previous model is kept, so a bad promotion is one `mv` away from undone.

That unseen-data split is the part that is easy to get wrong. Scoring a model on
history it was trained on flatters it enormously: the first version of this file
reported the champion at cost 2,003 against a candidate's 4,299, which measured
nothing except that one of them had already been shown the answers.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import config as C          # noqa: E402
import evaluate as ev       # noqa: E402
import features as F        # noqa: E402
import models as M          # noqa: E402

LIVE = ROOT / C.MODEL_FILE
PREV = ROOT / "models/forecaster.prev.joblib"
HISTORY = ROOT / "models/retrain_history.jsonl"

# How much better the candidate must be before it replaces the champion.
# Not zero: fold-to-fold noise on this data is around 0.3 on a cost of ~4,300,
# so a 1% swing is indistinguishable from luck. Demanding 2% means a promotion
# reflects a real change in the traffic, not a coin flip.
MIN_IMPROVEMENT = 0.02


# The champion must be judged only on rows it has never seen. Anything less
# than this many is not a measurement, it is noise — 480 steps is two full
# traffic cycles at 15s per step.
MIN_FRESH_ROWS = 2 * C.STEPS_PER_CYCLE


def cost_of(model, test, cols) -> float:
    """Cost of one model on one held-out slice. Lower is better."""
    pred = np.clip(model.predict(test[cols] if not isinstance(model, M.GBM) else test),
                   0, None)
    return ev.score(test["target"].to_numpy(), pred)["cost"]


def main(dry_run: bool, force: bool) -> int:
    if not (ROOT / C.DATA_FILE).exists():
        sys.exit(f"no {C.DATA_FILE} — run collect.py first")

    raw = F.load_series(str(ROOT / C.DATA_FILE))
    table = F.usable(F.build_table(raw, horizon=C.HORIZON_STEPS))
    cols = F.feature_columns(table)
    hours = (raw["ts"].max() - raw["ts"].min()).total_seconds() / 3600
    print(f"  data      : {len(table):,} usable rows, {hours:.1f} h "
          f"({raw['ts'].min():%Y-%m-%d %H:%M} -> {raw['ts'].max():%m-%d %H:%M} UTC)")

    bundle = joblib.load(LIVE) if LIVE.exists() else None

    # ---- find the data the champion has never seen -------------------------
    #
    # This is the whole design. A model trained on all of history scores
    # brilliantly on all of history, because it is being asked questions it
    # already has the answers to. Comparing that against a candidate fitted
    # honestly on a subset guarantees the champion "wins" forever and the gate
    # never opens. Measured before this was fixed: champion 2,003 vs candidate
    # 4,299, which said nothing about either model.
    #
    # So: split at the champion's training cutoff. Everything after it is fresh.
    if bundle is None:
        print("  champion  : none — training the first model")
        fresh = table.iloc[0:0]
    elif "trained_through" not in bundle:
        print("  champion  : bundle predates trained_through; cannot identify unseen "
              "rows, so no fair comparison is possible. Re-run train_final.py once.")
        return 1
    else:
        cutoff = pd.Timestamp(bundle["trained_through"])
        fresh = table[table["ts"] > cutoff]
        print(f"  champion  : trained through {cutoff:%Y-%m-%d %H:%M} UTC "
              f"({bundle['trained_rows']:,} rows)")
        print(f"  fresh data: {len(fresh):,} rows it has never seen")

    if bundle is not None and len(fresh) < MIN_FRESH_ROWS:
        print(f"  verdict   : need {MIN_FRESH_ROWS:,} unseen rows to judge, "
              f"have {len(fresh):,}. Collect more, then re-run.")
        print("  kept the current model")
        return 0

    if bundle is not None and bundle["features"] != cols:
        print("  champion  : feature set differs — not comparable, promoting on structure")
        live_cost, cand_cost = float("inf"), 0.0
    else:
        # Candidate learns ONLY from what came before the fresh window, so both
        # models are answering questions neither has seen.
        past = table[table["ts"] <= pd.Timestamp(bundle["trained_through"])] if bundle is not None else table
        candidate = M.GBM(quantile=C.QUANTILE).fit(past, past["target"], cols)
        cand_cost = cost_of(candidate, fresh, cols)
        live_cost = cost_of(bundle["model"], fresh, cols) if bundle else float("inf")
        print(f"  candidate : cost {cand_cost:,.0f}  (on the fresh window)")
        if bundle:
            print(f"  champion  : cost {live_cost:,.0f}  (same window, never trained on it)")

    # ---- decide ------------------------------------------------------------
    if live_cost == float("inf"):
        gain, promote, why = 1.0, True, "no comparable champion"
    else:
        gain = (live_cost - cand_cost) / live_cost
        promote = gain >= MIN_IMPROVEMENT
        why = (f"{gain:+.1%} vs champion, "
               f"{'above' if promote else 'below'} the {MIN_IMPROVEMENT:.0%} bar")
    print(f"  verdict   : {why}")

    if force and not promote:
        promote, why = True, why + " (forced)"

    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    HISTORY.parent.mkdir(exist_ok=True)
    with open(HISTORY, "a") as fh:
        fh.write(json.dumps({"ts": stamp, "rows": len(table), "hours": round(hours, 1),
                             "candidate_cost": round(cand_cost, 1),
                             "champion_cost": None if live_cost == float("inf") else round(live_cost, 1),
                             "promoted": bool(promote and not dry_run),
                             "reason": why}) + "\n")

    if dry_run:
        print("  --dry-run : nothing written")
        return 0
    if not promote:
        print("  kept the current model")
        return 0

    # Retrain on EVERYTHING before promoting. The fold scores answered "is this
    # recipe better"; the model that ships should still see all the data.
    final = M.GBM(quantile=C.QUANTILE).fit(table, table["target"], cols)
    if LIVE.exists():
        shutil.copy2(LIVE, PREV)
        print(f"  previous model kept at {PREV.name}")
    # trained_through must be written here too, or the NEXT run has no way to
    # tell which rows this model has seen and the gate jams shut permanently.
    joblib.dump({"model": final, "features": cols, "horizon": C.HORIZON_STEPS,
                 "quantile": C.QUANTILE, "backend": M.BACKEND,
                 "trained_rows": len(table),
                 "trained_through": table["ts"].max().isoformat()}, LIVE)
    print(f"  PROMOTED  -> {LIVE.relative_to(ROOT)}")
    print("  restart controller.py to pick it up (the bundle is loaded once, at start)")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Retrain, and promote only if better.")
    ap.add_argument("--dry-run", action="store_true", help="score both, write nothing")
    ap.add_argument("--force", action="store_true", help="promote even if not better")
    a = ap.parse_args()
    raise SystemExit(main(a.dry_run, a.force))
```

### `dashboard.py` — DELETED in the 2026-09-07 migration

This file (1,000 lines) no longer exists. It was the Streamlit UI with three pages. Two of
them are now the static Next.js site in `web/` (§2.7); the third, Live forecast, could not
be hosted and its role is covered by `src/predictor.py`, which was already the check
`CLAUDE.md` named for train/serve skew. Its full source is preserved in git history at
commit `9c17bf4`.

## 2.4 Kubernetes manifests

### `k8s/deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: traffic-app
  labels:
    app: traffic-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: traffic-app
  template:
    metadata:
      labels:
        app: traffic-app
    spec:
      containers:
        - name: traffic-app
          image: traffic-app:v1
          # The image lives only in the kind node's containerd store, put there by
          # `kind load`. Any pull would fail — there is no registry behind this tag.
          imagePullPolicy: Never
          ports:
            - name: http
              containerPort: 8000
          env:
            - name: WORK_MS
              value: "30"
            - name: STARTUP_DELAY_S
              value: "15"
          resources:
            # requests == limits, deliberately. The HPA measures CPU as a
            # percentage OF REQUESTS, so when the two differ the baseline arm
            # scales against a number unrelated to real capacity. With
            # requests=200m and limits=400m it added a pod at ~6 req/s while a
            # pod actually serves 20 — measured 20 replicas each sitting at
            # 123m, all of them 31% utilised, with the HPA reporting 58%/60%
            # and believing itself on target.
            #
            # Equal values also give the pod Guaranteed QoS, so it is the last
            # thing evicted under node pressure rather than the first — which
            # matters when a benchmark run is what is being protected.
            requests:
              cpu: 400m
              memory: 256Mi
            limits:
              # Caps one pod's throughput so capacity is finite and adding pods
              # actually buys headroom — an unthrottled busy-loop would let a
              # single pod eat the node and hide the need to scale at all.
              # MEASURED at this limit: 20 req/s at p95 95ms, 22.5 req/s at
              # 162ms. Change this and re-run `make capacity`.
              cpu: 400m
              memory: 256Mi
          readinessProbe:
            # The app binds its port only after a 15s sleep, so a pod is Running
            # long before it can serve. This is what keeps the Service from routing
            # traffic into a dead socket — i.e. it is the measured startup lag that
            # makes reactive scaling late, made visible to Kubernetes.
            httpGet:
              path: /healthz
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 3
            # A PROBE MUST DETECT "DEAD", NOT "BUSY".
            #
            # With the defaults (timeoutSeconds 1, failureThreshold 3) benchmark
            # run A1 collapsed: the 4x step put 60 req/s on each of 2 pods that
            # serve 20, the busy-loop threadpool starved the event loop, /healthz
            # missed its 1s deadline, and Kubernetes pulled the pod from the
            # Service. That shifted its load onto the survivor, which then failed
            # the same way — available replicas hit ZERO mid-spike, p99 reached
            # 19.8s, and the HPA stalled at 3 pods because NotReady pods report
            # no CPU metrics to scale on.
            #
            # 3s x 6 failures = ~18s of sustained non-response before eviction,
            # comfortably longer than any latency spike a saturated pod produces
            # here, still fast enough to catch a genuinely hung process.
            timeoutSeconds: 3
            failureThreshold: 6
```

### `k8s/service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: traffic-app
  labels:
    app: traffic-app
spec:
  # ClusterIP: in-cluster only. k6 reaches it through `kubectl port-forward`, so
  # both benchmark arms traverse exactly the same path and neither gets an
  # advantage from a different ingress route.
  type: ClusterIP
  selector:
    # Matches the pod template labels in deployment.yaml. This is also where the
    # readiness probe earns its keep: only Ready pods become endpoints here, so a
    # pod still in its 15s warm-up never receives a request.
    app: traffic-app
  ports:
    - name: http
      port: 80
      targetPort: 8000
```

### `k8s/servicemonitor.yaml`

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: traffic-app
  # No namespace field, like the other manifests, so `kubectl apply -f k8s/`
  # lands this in default beside the Service. That placement is required, not
  # cosmetic: a ServiceMonitor's selector only looks in its OWN namespace.
  labels:
    # The chart's default is to discover only ServiceMonitors carrying its
    # release label. This install turned that off (serviceMonitorSelector is
    # {}), so the label changes nothing today — it is here so the manifest
    # still works if that flag is ever reverted to the chart default.
    release: monitoring
    app: traffic-app
spec:
  selector:
    matchLabels:
      # Matches the SERVICE's labels, not the pods'. The operator resolves the
      # Service to its Endpoints and scrapes the pod IPs behind it — which is
      # why only Ready pods get scraped, same gate as real traffic.
      app: traffic-app
  endpoints:
      # "http" is the port NAME from service.yaml, not a number. Give a name no
      # service port matches and the operator drops it silently: no error, and
      # the target simply never appears in Prometheus.
    - port: http
      path: /metrics
      # Same 15s as the stack's global interval, so the history collect.py
      # records has one consistent sample spacing for the model to learn from.
      interval: 15s
```

### `k8s/hpa.yaml`

```yaml
# THE BASELINE ARM. Without this there is no A/B, only an A.
#
# Stock reactive autoscaling, untouched — this is what the predictive
# controller has to beat. It is a manifest rather than a `kubectl autoscale`
# one-liner so the comparison is reproducible from the repo: an imperative
# command that lived only in someone's shell history is not a baseline anyone
# else can rerun.
#
# The benchmark procedure toggles between arms:
#   Baseline    kubectl apply -f k8s/hpa.yaml     (controller.py NOT running)
#   Predictive  kubectl delete -f k8s/hpa.yaml    (controller.py running)
#
# Both must never run at once — they would fight over the same replica count
# and the result would measure the argument, not either policy.
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: traffic-app
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: traffic-app
  # Same bounds as the predictive controller's MIN_PODS / MAX_PODS, so neither
  # arm gets to scale somewhere the other cannot follow.
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          # 90% of a 400m request, i.e. act at 360m per pod.
          #
          # This is the number that makes the A/B fair, and it is set from the
          # capacity measurement rather than from convention. Measured CPU vs
          # offered rate on one pod:
          #
          #     8 req/s -> 0.25 cores    16 req/s -> 0.39
          #    12 req/s -> 0.35          20 req/s -> 0.40 (p95 still 95ms)
          #
          # so ~25m of CPU per req/s. 360m therefore trips at ~12.4 req/s, and
          # at a 40 req/s plateau the HPA settles on ~4 pods. The predictive
          # controller lands on ceil(40 * 1.1 / 20) = 3. Close enough that the
          # two arms hold comparable capacity at steady state, which is the
          # whole point: the benchmark must compare REACTION TIMING, not
          # provisioning generosity. At the old 60%-of-200m the HPA sat at ~7
          # pods for the same traffic and any latency win would have been
          # explained by the extra capacity, not by the forecast.
          #
          # 90 is high for an HPA target and that is defensible here: this pod
          # is deliberately CPU-bound with a hard limit, and latency stays flat
          # at 95ms right up to the limit. A general-purpose service with
          # bursty CPU should not copy this number.
          averageUtilization: 90
```

### `k8s/load/k6.yaml`

```yaml
# The load generator, running INSIDE the cluster.
#
# k6 has to live here rather than on the Mac because `kubectl port-forward
# svc/traffic-app` pins every request to a single pod (measured: 6.94 req/s on
# one pod, 0.00 on the other three). Load offered that way can never show a
# benefit from scaling. Sending to the ClusterIP from a pod lets kube-proxy
# spread connections across all Ready endpoints.
#
# The script comes from a ConfigMap built out of load/ by `make load-start`,
# so load/daily.js stays the single source of truth and is not duplicated here.
apiVersion: apps/v1
kind: Deployment
metadata:
  name: k6-load
  labels:
    app: k6-load
spec:
  # Scale to 0 to stop generating load, 1 to start. A Deployment rather than a
  # Job so `kubectl scale` is the on/off switch and a crash restarts itself
  # during a multi-day collection run.
  replicas: 0
  selector:
    matchLabels:
      app: k6-load
  template:
    metadata:
      labels:
        app: k6-load
      annotations:
        # Changing the ConfigMap does NOT restart a running pod, so a script
        # edit would silently keep running the old version. `make load-start`
        # does a rollout restart to force a re-read.
        checksum/trigger: "manual-rollout"
    spec:
      containers:
        - name: k6
          image: grafana/k6:latest
          args: ["run", "/scripts/daily.js"]
          env:
            # Requests/second at the busy plateau. Sized against how the HPA
            # ACTUALLY behaves, not against true pod capacity: it targets 60%
            # of requests.cpu (200m), so it adds a pod roughly every 4.7 req/s
            # even though one pod can serve ~15. At 100 it therefore sat pinned
            # at maxReplicas=20 continuously — no room left to react to a
            # spike, and the laptop running flat out for nothing.
            #
            #   40 req/s plateau -> ~9 pods under the HPA, ~3 predictive
            #   88 req/s spike   -> ~19 pods, still inside the 20 cap
            #   4-7 req/s quiet  -> back down to MIN_PODS=2 overnight
            - name: PEAK_RPS
              value: "40"
            # In-cluster DNS for the Service. Overridable so the same script
            # still runs from the laptop against a port-forward if needed.
            - name: TARGET
              value: "http://traffic-app/work"
          volumeMounts:
            - name: scripts
              mountPath: /scripts
          resources:
            requests:
              cpu: 200m
              memory: 128Mi
            limits:
              # k6 shares the node's 10 cores with the app pods and Prometheus.
              # Capping it means a load generator that starves the very service
              # it is measuring cannot happen quietly.
              cpu: 1000m
              memory: 512Mi
      volumes:
        - name: scripts
          configMap:
            name: k6-scripts
```

### `k8s/load/k6-capacity.yaml`

```yaml
# Step 25: measure ONE pod's capacity.
#
# Lives in k8s/load/ rather than k8s/ on purpose. `kubectl apply -f k8s/` is
# not recursive, so `make deploy` will not sweep this up — a Job that re-ran on
# every deploy would start hammering the cluster in the middle of whatever else
# was happening.
#
# Prerequisites, or you measure the wrong thing entirely:
#   kubectl delete -f k8s/hpa.yaml            # nothing else may move replicas
#   kubectl scale deploy/traffic-app --replicas=1
apiVersion: batch/v1
kind: Job
metadata:
  name: k6-capacity
spec:
  # No retries. A failed capacity run needs reading, not silently repeating
  # with the cluster in an unknown state.
  backoffLimit: 0
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: k6
          image: grafana/k6:latest
          args: ["run", "/scripts/capacity.js"]
          volumeMounts:
            - name: scripts
              mountPath: /scripts
          resources:
            requests: {cpu: 200m, memory: 128Mi}
            # Deliberately larger than the app pod's limit: the generator must
            # never be the bottleneck, or you measure k6 instead of the app.
            limits: {cpu: 1500m, memory: 512Mi}
      volumes:
        - name: scripts
          configMap:
            name: k6-scripts
```

### `k8s/load/k6-benchmark.yaml`

```yaml
# One benchmark run. `make bench RUN=A1` fills in the name and starts it.
#
# In k8s/load/ so `kubectl apply -f k8s/` (not recursive) cannot sweep it up —
# a benchmark Job that fired on every deploy would corrupt whatever run was in
# progress.
#
# The Job is deleted and recreated per run rather than reused, so RUN_NAME and
# the logs belong to exactly one 20-minute window.
apiVersion: batch/v1
kind: Job
metadata:
  name: k6-benchmark
spec:
  # A retry would silently start a second 20-minute run against a cluster left
  # in whatever state the first one ended in. A failed benchmark run needs
  # reading, not repeating.
  backoffLimit: 0
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: k6
          image: grafana/k6:latest
          args: ["run", "/scripts/SCRIPTNAME"]   # filled by `make bench`
          env:
            - name: RUN_NAME
              value: "PLACEHOLDER"     # replaced by `make bench RUN=...`
            - name: TARGET
              value: "http://traffic-app/work"
            - name: STEADY_RPS
              value: "20"
          volumeMounts:
            - name: scripts
              mountPath: /scripts
          resources:
            requests: {cpu: 500m, memory: 256Mi}
            # Well above the app pods' 400m: the generator must never be the
            # bottleneck, or the benchmark measures k6 rather than the service.
            limits: {cpu: 2000m, memory: 1Gi}
      volumes:
        - name: scripts
          configMap:
            name: k6-scripts
```

## 2.5 k6 load scripts

### `load/daily.js`

```javascript
import http from 'k6/http';
import { check } from 'k6';

// TARGET IS THE CLUSTER-INTERNAL SERVICE, and this script is meant to run in a
// pod, not on the Mac. That is not a convenience — it is a correctness fix.
//
// `kubectl port-forward svc/traffic-app` resolves the Service to ONE pod and
// pins every request to it. Measured on 2026-08-19 with 4 replicas Ready:
// one pod served 6.94 req/s and the other three served 0.00. Load offered that
// way can never show a benefit from scaling, because the pods you add never
// receive anything. Sending to the ClusterIP from inside the cluster lets
// kube-proxy spread each connection across all Ready endpoints — which is also
// how traffic would actually arrive in production.
const TARGET = __ENV.TARGET || 'http://traffic-app/work';

// Requests/second at the top of the busy plateau. Everything below is a
// fraction of this, so the whole diurnal shape rescales from one number.
// Set it from MEASURED single-pod capacity x the pod count you want the
// plateau to need — not from a guess.
const PEAK_RPS = Number(__ENV.PEAK_RPS || 80);

// One "day" is 60 real minutes. CYCLES is resolved once at init, so this is
// "long enough" rather than forever: 168 cycles = 7 real days.
const CYCLE_MIN = 60;
const CYCLES = 168;

// Every 7th day is light, so the model has to key off day-of-week and not just
// minute-of-day — the most common way a naive forecaster quietly overfits.
const WEEKEND_EVERY = 7;
const WEEKEND_SCALE = 0.5;

const rand = (lo, hi) => lo + Math.random() * (hi - lo);
const lerp = (a, b, t) => a + (b - a) * t;

// Minute-by-minute load across one ordinary day, as a FRACTION of PEAK_RPS.
function baseCurve(m) {
  if (m < 10) return rand(0.10, 0.18);              // 0-10   quiet overnight
  if (m < 25) return lerp(0.18, 1.0, (m - 10) / 15); // 10-25  morning ramp
  if (m < 45) return rand(0.85, 1.0);                // 25-45  busy plateau
  return lerp(1.0, 0.12, (m - 45) / 15);             // 45-60  evening taper
}

function buildDay(cycle) {
  const day = [];
  for (let m = 0; m < CYCLE_MIN; m++) day.push(baseCurve(m));

  // 2-3 spikes of 2-3x lasting 2-4 minutes. These are the events that make
  // over-provisioning cheap insurance and under-provisioning expensive, which
  // is exactly the asymmetry the q=0.90 quantile is chosen to respect.
  const spikes = Math.floor(rand(2, 4));
  for (let s = 0; s < spikes; s++) {
    const start = Math.floor(rand(5, CYCLE_MIN - 5));
    const len = Math.floor(rand(2, 5));
    const mult = rand(2, 3);
    for (let m = start; m < Math.min(start + len, CYCLE_MIN); m++) day[m] *= mult;
  }

  const scale = cycle % WEEKEND_EVERY === WEEKEND_EVERY - 1 ? WEEKEND_SCALE : 1;
  // Clamped to 2.2x peak: a spike the cluster cannot physically serve stops
  // being a demand signal and becomes a queue-depth measurement instead.
  return day.map((v) => Math.max(2, Math.round(v * scale * PEAK_RPS)))
            .map((v) => Math.min(v, Math.round(PEAK_RPS * 2.2)));
}

function buildStages() {
  const stages = [];
  for (let c = 0; c < CYCLES; c++) {
    // One stage per minute: ramping-arrival-rate interpolates between targets,
    // so this gives smooth curves and sharp spikes from the same flat list.
    for (const target of buildDay(c)) stages.push({ duration: '1m', target });
  }
  return stages;
}

export const options = {
  scenarios: {
    daily: {
      // ramping-ARRIVAL-RATE, not ramping-vus. With VUs, each user fires its
      // next request the instant the last response lands, so requests/second
      // = VUs / latency — and latency falls as pods are added. The recorded
      // "demand" would then be partly an OUTPUT of the autoscaler, and the
      // forecaster would be learning its own control loop. An arrival rate is
      // offered load: identical whether 2 pods or 20 are serving it.
      executor: 'ramping-arrival-rate',
      startRate: Math.max(2, Math.round(PEAK_RPS * 0.12)),
      timeUnit: '1s',
      stages: buildStages(),
      // Generous headroom: when the app saturates, latency climbs and k6 needs
      // more concurrent VUs to keep the arrival rate on schedule. Too few and
      // k6 silently drops iterations, which looks like falling demand.
      preAllocatedVUs: 50,
      maxVUs: 400,
    },
  },
  // ONE CONNECTION PER REQUEST. kube-proxy load balances at L4 — it picks a
  // backend when a TCP connection is established, not per request — and k6
  // reuses keep-alive connections by default. Measured: with reuse on, a
  // single VU's connection pinned 13.05 req/s onto one pod while two other
  // Ready pods sat at 0.00, which is the same failure the port-forward had.
  // A real service is reached by many independent clients; one load generator
  // holding one socket is the artefact. This applies identically to both
  // benchmark arms, so it cannot bias the comparison.
  noConnectionReuse: true,
  summaryTrendStats: ['avg', 'p(95)', 'p(99)', 'max'],
};

export default function () {
  const res = http.get(TARGET);
  // Without this a flood of 502s during a scale-up would look like a fast run
  // rather than a broken one, since k6 times failures just as happily.
  check(res, { 'status is 200': (r) => r.status === 200 });
}
```

### `load/ramp.js`

```javascript
import http from 'k6/http';
import { check } from 'k6';

// THE SECOND EXAM PAPER: a PREDICTABLE load change.
//
// benchmark.js is a 4x step with no precursor. Measured there: the controller
// provisioned correctly (5 pods vs the HPA's 3) and still did not beat it on
// p99, because a forecaster reading lag features has nothing to forecast FROM
// until the step has already happened. Both policies are blind for the first
// 30-60s, pods take ~19s to boot, and the queued latency is already paid.
// That is a real limitation and it belongs in the writeup - but it tests the
// one thing this model cannot do.
//
// A ramp is what predictive scaling is FOR. Load climbs over 6 minutes, so
// diff_4, slope_12 and roll_mean_4 all carry the trend, and a 60s-ahead
// forecast can put pods in place before the traffic that needs them arrives.
// The HPA cannot do this even in principle: it acts on CPU that has already
// risen, then waits out the pod start-up it could have started earlier.
//
// Same 20-minute length, same steady floor and same peak as benchmark.js, so
// the two scenarios are directly comparable. Zero randomness, again: three
// runs per arm must differ only in the arm.
//
//   0-4    steady 20 req/s      both arms settle to the 2-pod floor
//   4-10   ramp 20 -> 80        THE EVENT - gradual, therefore forecastable
//   10-14  plateau 80           did either arm arrive with enough capacity?
//   14-20  ramp 80 -> 20        scale-down behaviour, which is where the
//                               asymmetric MAX_SCALE_DOWN_PER_CYCLE shows up
const TARGET = __ENV.TARGET || 'http://traffic-app/work';
const LOW = Number(__ENV.STEADY_RPS || 20);
const HIGH = Number(__ENV.PEAK_RPS || 80);

export const options = {
  scenarios: {
    ramp: {
      // Arrival rate, not VUs - otherwise the better-scaling arm serves more
      // requests and the p99 comparison is between different workloads.
      executor: 'ramping-arrival-rate',
      startRate: LOW,
      timeUnit: '1s',
      stages: [
        { duration: '4m', target: LOW },
        { duration: '6m', target: HIGH },   // ramping-arrival-rate interpolates
        { duration: '4m', target: HIGH },
        { duration: '6m', target: LOW },
      ],
      preAllocatedVUs: 100,
      // Generous: if k6 runs out of VUs it drops iterations, which removes load
      // exactly when the app is struggling and flatters whichever arm is coping
      // worse. A valid run reports dropped_iterations = 0.
      maxVUs: 3000,
    },
  },
  // kube-proxy balances per TCP connection, so reused keep-alive sockets pin
  // traffic to a few pods and whatever either arm launches sits idle.
  noConnectionReuse: true,
  summaryTrendStats: ['avg', 'p(50)', 'p(95)', 'p(99)', 'max'],
};

export default function () {
  const res = http.get(TARGET);
  check(res, { 'status is 200': (r) => r.status === 200 });
}

export function handleSummary(data) {
  return {
    stdout:
      '\n===BENCH_JSON_START===\n' +
      JSON.stringify({ run: __ENV.RUN_NAME || 'unnamed', metrics: data.metrics }) +
      '\n===BENCH_JSON_END===\n',
  };
}
```

### `load/benchmark.js`

```javascript
import http from 'k6/http';
import { check } from 'k6';

// THE EXAM PAPER. Both arms sit the same one.
//
// Zero randomness anywhere in this file - no rand(), no spikes at random
// minutes, no per-cycle variation. daily.js is deliberately unpredictable
// because a forecaster has to earn its keep against surprise; a BENCHMARK is
// the opposite. If the two arms faced different traffic, any difference in
// p99 would be unattributable, and running it three times each would measure
// the randomness rather than the policy.
//
// 20 minutes, three phases:
//
//   0-5    steady at STEADY_RPS      both arms settle to their baseline pods
//   5-9    step to 4x STEADY_RPS     THE EVENT - this is what is being measured
//   9-20   back to steady            recovery and scale-down behaviour
//
// The step at minute 5 is a step, not a ramp: reactive scaling is slowest when
// load arrives faster than pods can boot, and a gradual ramp would let the HPA
// keep up and hide the very lag this project exists to demonstrate.
const TARGET = __ENV.TARGET || 'http://traffic-app/work';

// Chosen so BOTH policies target the same pod count, leaving timing as the
// only variable. Measured on this cluster:
//
//   HPA at 90% of a 400m request settles at ~16.8 req/s per pod
//   the controller uses the measured 20 req/s per pod, x1.1 headroom
//
//   steady 20 req/s -> HPA 2 pods (the floor), controller 2 pods
//   spike  80 req/s -> HPA 5 pods,             controller ceil(80*1.1/20) = 5
//
// The earlier 30 -> 120 version put the baseline at 82% CPU before the spike
// even started, and a 4x step is past what CPU-based scaling can track at all
// (utilisation caps at 100% once the pod hits its limit, so the HPA can only
// grow 1.11x per cycle). See bench/discarded/README.md.
const STEADY_RPS = Number(__ENV.STEADY_RPS || 20);
const SPIKE_MULT = Number(__ENV.SPIKE_MULT || 4);
const SPIKE = Math.round(STEADY_RPS * SPIKE_MULT);

export const options = {
  scenarios: {
    bench: {
      // Arrival rate, not VUs. With VUs, throughput is VUs/latency, so the arm
      // that scales better serves MORE requests - and comparing p99 across
      // arms that handled different request counts is not a comparison. A
      // fixed arrival rate means both arms are offered identical work and only
      // their latency can differ.
      executor: 'ramping-arrival-rate',
      startRate: STEADY_RPS,
      timeUnit: '1s',
      stages: [
        { duration: '5m', target: STEADY_RPS },   // settle
        { duration: '1s', target: SPIKE },        // the step
        { duration: '4m', target: SPIKE },        // hold the spike
        { duration: '1s', target: STEADY_RPS },   // release
        { duration: '11m', target: STEADY_RPS },  // recover
      ],
      // Sized for the spike at degraded latency: if k6 runs out of VUs it
      // silently drops iterations, which shows up as the load DISAPPEARING
      // exactly when the app is struggling - flattering whichever arm is
      // coping worse.
      preAllocatedVUs: 100,
      // 800 was not enough in run A1: latency hit 14s under collapse, so
      // holding 120 req/s needed ~1700 concurrent VUs and k6 dropped 4,213
      // iterations. Dropped iterations silently REDUCE the offered load at
      // exactly the moment the app is struggling, which flatters whichever
      // arm is coping worse. A valid run must report dropped_iterations = 0.
      maxVUs: 3000,
    },
  },
  // Same reason as daily.js: kube-proxy balances per TCP connection, so reused
  // keep-alive sockets would pin traffic onto a few pods and the extra pods
  // either arm launched would sit idle.
  noConnectionReuse: true,
  summaryTrendStats: ['avg', 'p(50)', 'p(95)', 'p(99)', 'max'],
};

export default function () {
  const res = http.get(TARGET);
  check(res, { 'status is 200': (r) => r.status === 200 });
}

// k6 runs in a pod, so a file written here would die with the pod. Emitting
// the JSON to stdout between markers lets `kubectl logs` carry it out intact,
// past the per-second progress lines.
export function handleSummary(data) {
  return {
    stdout:
      '\n===BENCH_JSON_START===\n' +
      JSON.stringify({ run: __ENV.RUN_NAME || 'unnamed', metrics: data.metrics }) +
      '\n===BENCH_JSON_END===\n',
  };
}
```

### `load/capacity.js`

```javascript
import http from 'k6/http';
import { check } from 'k6';

// ONE POD'S CAPACITY, measured rather than guessed.
//
// This is the number that converts a forecast in requests/second into a pod
// count (`CAPACITY_PER_POD` in src/controller.py). Get it wrong and every
// decision the controller makes is wrong in the same direction — and nothing
// in the forecast metrics will show it, because the forecast is still correct.
//
// Method: scale the deployment to 1 replica, delete the HPA so nothing else
// moves, then walk the ARRIVAL RATE upward in steps. Capacity is the last step
// where p95 latency is still flat. Past that point the pod is queueing, and
// latency climbs while throughput does not.
//
//   kubectl delete hpa traffic-app
//   kubectl scale deploy/traffic-app --replicas=1
//   make capacity
//
// Arrival rate, not VUs: a closed-loop VU test can never overload the pod
// (each user waits for its own response), so it measures how slow the pod got,
// never where it broke.
const TARGET = __ENV.TARGET || 'http://traffic-app/work';

// Steps in requests/second. Wide enough to bracket a pod limited to 400m CPU
// doing 30ms of work per request — theory says ~13 req/s, so the interesting
// region is 4-24 and the top steps exist to prove the knee is real.
const STEPS = (__ENV.STEPS || '4,8,12,16,20,24,28').split(',').map(Number);
const STEP_SECONDS = Number(__ENV.STEP_SECONDS || 45);

export const options = {
  scenarios: {
    ramp: {
      executor: 'ramping-arrival-rate',
      startRate: STEPS[0],
      timeUnit: '1s',
      // duration 0 makes each target a STEP rather than a ramp: jump to the
      // rate, hold it, jump again. A smooth ramp would smear the knee across
      // the whole run and there would be nothing to read off.
      stages: STEPS.flatMap((r) => [
        { duration: '0s', target: r },
        { duration: `${STEP_SECONDS}s`, target: r },
      ]),
      preAllocatedVUs: 20,
      maxVUs: 300,
    },
  },
  // ONE CONNECTION PER REQUEST. kube-proxy load balances at L4 — it picks a
  // backend when a TCP connection is established, not per request — and k6
  // reuses keep-alive connections by default. Measured: with reuse on, a
  // single VU's connection pinned 13.05 req/s onto one pod while two other
  // Ready pods sat at 0.00, which is the same failure the port-forward had.
  // A real service is reached by many independent clients; one load generator
  // holding one socket is the artefact. This applies identically to both
  // benchmark arms, so it cannot bias the comparison.
  noConnectionReuse: true,
  summaryTrendStats: ['avg', 'p(95)', 'p(99)', 'max'],
};

export default function () {
  const res = http.get(TARGET);
  check(res, { 'status is 200': (r) => r.status === 200 });
}
```

## 2.6 Build / config / dotfiles

### `Makefile`

```makefile
# Ports live here and nowhere else, so changing one is a single edit.
# 8000, not 5000: macOS Control Center holds 5000 for AirPlay Receiver, and when
# something else is listening there a failed connection comes back as an instant
# 403 rather than an error — which once let k6 report 12.5M healthy iterations
# while delivering nothing at all. 8000 also matches the container's port.
APP_PORT  = 8000
PROM_PORT = 9090

# Use the venv's interpreters when they exist, otherwise whatever is on PATH.
# Without this, every target here fails with "No such file or directory" unless
# you remembered to `source .venv/bin/activate` first — which is a bad way to
# find out your dashboard is fine and your shell was not.
VENV      ?= .venv
PY        := $(shell [ -x $(VENV)/bin/python ] && echo $(VENV)/bin/python || echo python)
STREAMLIT := $(shell [ -x $(VENV)/bin/streamlit ] && echo $(VENV)/bin/streamlit || echo streamlit)

# These are names, not files. Without this line a stray file called "build" or
# "deploy" would make the target look up to date and silently stop running.
.PHONY: run build load deploy pods forward-prom \
        load-start load-stop capacity collect bench ui retrain

# Local dev loop: 1s warm-up instead of 15s, and restart on every save.
run:
	STARTUP_DELAY_S=1 uvicorn app.main:app --reload --port $(APP_PORT)

# Bake the app image. Re-run this before `load` after any code change.
build:
	docker build -t traffic-app:v1 .

# Copy the image into the kind node — imagePullPolicy: Never has no registry to fall back on.
load:
	kind load docker-image traffic-app:v1 --name autoscale

# Apply every manifest in k8s/ (deployment, service, servicemonitor, hpa).
# NOT recursive, so k8s/load/ is skipped on purpose — the load generator and
# the capacity Job are started explicitly, never as a side effect of deploying.
deploy:
	kubectl apply -f k8s/

# Watch the rollout; the 0/1 -> 1/1 flip is the 15s readiness gap.
pods:
	kubectl get pods -w

# There is deliberately NO forward-app target. `kubectl port-forward svc/...`
# resolves the Service to ONE pod and pins every request to it, so laptop-side
# load could never show a benefit from scaling. k6 runs in-cluster instead
# (k8s/load/k6.yaml) and reaches the app directly, so nothing on the Mac needs
# port 5000 or 8000 at all.

# Reach the Prometheus UI at localhost:$(PROM_PORT).
forward-prom:
	kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus $(PROM_PORT):9090

# --- load generation, IN-CLUSTER --------------------------------------------
# k6 runs as a pod, not on the Mac. `kubectl port-forward svc/traffic-app`
# resolves the Service to ONE pod and pins all traffic to it (measured: 6.94
# req/s on one pod, 0.00 on the other three), so laptop-side load can never
# demonstrate a benefit from scaling. Sending to the ClusterIP from inside the
# cluster lets kube-proxy spread connections across every Ready endpoint.

# Ship load/ into a ConfigMap and start the generator. The rollout restart is
# required: editing a ConfigMap does not restart pods already mounting it, so
# without it a script change silently keeps running the old version.
load-start:
	kubectl create configmap k6-scripts --from-file=load/ --dry-run=client -o yaml | kubectl apply -f -
	kubectl apply -f k8s/load/k6.yaml
	kubectl scale deploy/k6-load --replicas=1
	kubectl rollout restart deploy/k6-load

load-stop:
	kubectl scale deploy/k6-load --replicas=0

# Step 25: one pod's capacity. Requires 1 replica and no HPA, or you measure
# the cluster's ability to scale rather than a single pod's ceiling.
capacity:
	kubectl delete job k6-capacity --ignore-not-found
	kubectl create configmap k6-scripts --from-file=load/ --dry-run=client -o yaml | kubectl apply -f -
	kubectl apply -f k8s/load/k6-capacity.yaml
	kubectl wait --for=condition=complete job/k6-capacity --timeout=15m
	kubectl logs job/k6-capacity | tail -25

# Copy Prometheus history into data/traffic.parquet every 10 minutes. The
# 6h lookback means running LESS often than every 6 hours loses history
# permanently; every 10 minutes just means a crash costs at most 10 minutes.
collect:
	while true; do $(PY) collect.py; sleep 600; done

# --- the A/B benchmark -------------------------------------------------------
# One 20-minute run:   make bench RUN=A1
#
# Records the k6 summary to bench/<RUN>.json plus the run's start/end epoch to
# bench/<RUN>.start and .end. Pod-seconds is not captured live: Prometheus
# already stores the replica count and keeps 15 days, so analyze.py replays the
# window afterwards. That is half the result — a latency win bought with far
# more compute is not a win, and a benchmark reporting only p99 is not honest.
#
# The continuous daily.js load MUST be off (`make load-stop`) or both arms are
# serving a second, uncontrolled workload on top of the exam paper.
# SCRIPT selects the scenario, default benchmark.js (the 4x step). Use
# SCRIPT=ramp.js for the predictable-ramp scenario — the one a forecaster can
# actually anticipate. Run names should say which: A1s/B1s for step,
# A1r/B1r for ramp, or the two scenarios' results get averaged together.
bench:
	@test -n "$(RUN)" || (echo "usage: make bench RUN=A1 [SCRIPT=ramp.js]"; exit 1)
	@test "$$(kubectl get deploy k6-load -o jsonpath='{.spec.replicas}')" = "0" \
	  || (echo "ERROR: daily.js load is still running — run 'make load-stop' first"; exit 1)
	kubectl delete job k6-benchmark --ignore-not-found
	kubectl create configmap k6-scripts --from-file=load/ --dry-run=client -o yaml | kubectl apply -f -
	@mkdir -p bench
	@sed -e 's/PLACEHOLDER/$(RUN)/' -e 's/SCRIPTNAME/$(or $(SCRIPT),benchmark.js)/' \
	  k8s/load/k6-benchmark.yaml | kubectl apply -f -
	@echo "run $(RUN) started — 20 minutes"
	@date -u +%s > bench/$(RUN).start
	kubectl wait --for=condition=complete job/k6-benchmark --timeout=30m
	@kubectl logs job/k6-benchmark \
	  | sed -n '/===BENCH_JSON_START===/,/===BENCH_JSON_END===/p' \
	  | sed '1d;$$d' > bench/$(RUN).json
	@date -u +%s > bench/$(RUN).end
	@echo "wrote bench/$(RUN).json  (window $(RUN).start -> $(RUN).end)"

# --- the UI ------------------------------------------------------------------
# Two pages. "Benchmark replay" needs nothing but bench/replay.json, so it works
# with the cluster switched off. "Live forecast" needs `make forward-prom` and
# traffic running, and is the view that shows a forecast beside what actually
# happened next — the only check that catches train/serve skew.
ui:
	$(STREAMLIT) run dashboard.py

# Re-freeze the benchmark runs out of Prometheus. Only needed after new runs;
# Prometheus keeps 15 days, these files keep them forever. Both scenarios, so a
# run added to one of them cannot be silently left out of the UI.
replay-data:
	$(PY) export_replay.py
	$(PY) export_replay.py --runs A1,A2,A3,B1,B2,B3,C1,C2,C3 \
	  --out replay-step.json \
	  --scenario "instant 4x step: 20 -> 80 req/s at minute 5, held 4 min"

# --- keeping the model current -----------------------------------------------
# Scores a freshly-trained candidate against the live model on data collected
# SINCE the live model was trained, and swaps only on a real improvement. Safe
# to run on a timer: with no new data it declines and says so.
#
# To schedule it daily at 3am (`crontab -e`), noting that cron has almost no
# PATH and no venv, so both must be spelled out:
#
#   0 3 * * * cd /path/to/predictive-autoscaling && .venv/bin/python retrain.py \
#             >> logs/retrain.log 2>&1
#
# It only reads data/traffic.parquet, so `make collect` has to be running too —
# otherwise it will keep finding nothing new, correctly and forever.
retrain:
	$(PY) retrain.py

retrain-check:
	$(PY) retrain.py --dry-run
```

### `.streamlit/config.toml` and `.streamlit/credentials.toml` — DELETED

Both removed with `dashboard.py`. `config.toml` held the Streamlit theme (the same
paper/ink tokens now in `web/app/globals.css`); `credentials.toml` held an empty email
entry, which is what suppressed Streamlit's first-run prompt. Preserved in git history at
commit `9c17bf4`.

### `.gitignore`

```gitignore
# macOS writes this into every folder it opens in Finder. Pure noise.
.DS_Store

# Local Python environment: 500MB of arm64 binaries that would be wrong on any
# other machine anyway. requirements.txt is what makes the env reproducible.
.venv/
**/__pycache__/
*.pyc

# k6 writes its whole run log here, and it grows for days. nohup.out is the
# same idea when a background job's output is not redirected.
*.log
nohup.out

# REGENERABLE from data/traffic.parquet — outputs/ comes from backtest.py,
# models/ from train_final.py. Committing them would mean a stale model in the
# repo silently disagreeing with the code that produced it.
outputs/
models/

# Written by controller.py, one row per 30s decision. Per-run evidence, not
# source. The benchmark results that matter get summarised into results.md.
logs/

# NOT ignored: data/traffic.parquet. It is small (a few hundred KB) and it is
# the one artefact here that CANNOT be regenerated — Prometheus keeps only 15
# days, so once a scrape ages out, that history is gone for good.

# Editor and agent state — local to one machine, not part of the project.
.agents/
.claude/
```

### `bench/discarded/README.md`

```markdown
# Discarded runs

`A1-4x-on-30.json` — steady 30 req/s, spike to 120. p99 15,647ms, 641 dropped
iterations, HPA reached only 4 of the ~7 pods needed.

Not a rigged result, but the wrong experiment. Two reasons:

1. At 30 req/s on the 2-pod floor, average CPU was already 82% against a 90%
   HPA target. The baseline began the run at the edge of its own trigger.

2. Once a pod saturates its 400m limit, CPU utilisation reads 100% and cannot
   go higher — a pod at 3x overload is indistinguishable from one at 1.01x. The
   HPA can therefore only grow replicas by 100/90 = 1.11 per cycle, so a 4x step
   is beyond what it can track at all. The run measured that blindness rather
   than reaction timing.

Both are true findings about CPU-based autoscaling and worth a paragraph in the
README. They are not what this project set out to measure, which is whether
forecasting delivers capacity EARLIER than reacting to it.

Replaced by steady 20 req/s -> spike 80, where the HPA (which settles at
~16.8 req/s per pod, measured) and the controller (20 req/s per pod, measured)
both target 5 pods — so the only variable left is when those pods arrive.
```

## 2.7 `web/` — the deployed static site (added 2026-09-07)

Next.js 16.3.4 / React 19.2.8 / TypeScript, App Router, `output: 'export'`.
Full source of every hand-written file follows. Generated files
(`next-env.d.ts`, `package-lock.json`, `web/public/data/*.json`) are described rather
than pasted; `web/.gitignore` is two lines written by `vercel link` (`.vercel`, `.env*`).

#### `web/package.json`

```json
{
  "name": "predictive-autoscaling-web",
  "version": "1.0.0",
  "private": true,
  "description": "Static report site for the predictive-autoscaling benchmark. Reads only committed JSON; never contacts the cluster.",
  "scripts": {
    "data": "node scripts/build-data.mjs",
    "dev": "npm run data && next dev",
    "build": "npm run data && next build",
    "start": "npx serve out"
  },
  "dependencies": {
    "next": "^16.3.4",
    "react": "^19.2.8",
    "react-dom": "^19.2.8"
  },
  "devDependencies": {
    "@types/node": "^26.4.1",
    "@types/react": "^19.2.18",
    "@types/react-dom": "^19.2.7",
    "typescript": "^7.0.2"
  }
}
```

#### `web/next.config.ts`

```typescript
import type { NextConfig } from "next";

/**
 * Fully static. The site reads only committed JSON — no API routes, no server
 * rendering, no data fetching at request time — so there is nothing for a
 * server to do. `output: 'export'` emits plain files into out/, which is what
 * Vercel serves from its CDN.
 */
const nextConfig: NextConfig = {
  output: "export",
  images: { unoptimized: true },   // no server, so no on-demand image optimiser
  reactStrictMode: true,
};

export default nextConfig;
```

#### `web/tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": [
      "dom",
      "dom.iterable",
      "ES2022"
    ],
    "allowJs": false,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": [
        "./*"
      ]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts"
  ],
  "exclude": [
    "node_modules",
    "out"
  ]
}
```

#### `web/scripts/build-data.mjs`

```javascript
/**
 * Generate everything the static site reads, from the repo's own artefacts.
 *
 * ONE SOURCE OF TRUTH. The site never carries a hand-maintained copy of a
 * number: bench/replay*.json and outputs/results.csv are the originals, and
 * this script is the only thing allowed to derive from them.
 *
 *   node web/scripts/build-data.mjs        (or: make web-data)
 *
 * Writes:
 *   web/public/data/replay.json        ramp runs, minified
 *   web/public/data/replay-step.json   step runs, minified
 *   web/public/data/backtest.json      derived from outputs/results.csv
 *
 * The replay files are re-emitted rather than symlinked because `output:
 * 'export'` copies public/ verbatim and a symlink would not survive.
 */
import { readFileSync, writeFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = join(HERE, "..", "..");
const OUT = join(HERE, "..", "public", "data");
mkdirSync(OUT, { recursive: true });

const kb = (p) => (statSync(p).size / 1024).toFixed(1);

// ---- 1. the recorded benchmark windows -------------------------------------
for (const name of ["replay.json", "replay-step.json"]) {
  const src = join(REPO, "bench", name);
  if (!existsSync(src)) {
    // A scenario whose file is absent is simply not offered by the site, so a
    // missing file is a warning rather than a build failure.
    console.warn(`  ! bench/${name} missing — that scenario will not be offered`);
    continue;
  }
  const parsed = JSON.parse(readFileSync(src, "utf8"));
  const dst = join(OUT, name);
  writeFileSync(dst, JSON.stringify(parsed));      // minified: the source is indent=1
  console.log(`  ${name.padEnd(18)} ${parsed.runs.length} runs   ${kb(src)} KB -> ${kb(dst)} KB`);
}

// ---- 2. the backtest scoreboard --------------------------------------------
// outputs/ is gitignored (regenerable from data/traffic.parquet via
// src/backtest.py), so the derived JSON below is committed instead. This is the
// fix for the Overview page having hardcoded the string "64.5% lower cost".
const csv = join(REPO, "outputs", "results.csv");
const backtestDst = join(OUT, "backtest.json");

if (!existsSync(csv)) {
  if (existsSync(backtestDst)) {
    console.warn("  ! outputs/results.csv missing — keeping the committed backtest.json");
  } else {
    console.error("  ERROR: outputs/results.csv missing and no committed backtest.json.");
    console.error("         Run: python src/backtest.py");
    process.exit(1);
  }
} else {
  const lines = readFileSync(csv, "utf8").trim().split("\n");
  const header = lines[0].split(",");
  const rows = lines.slice(1).map((line) => {
    const cells = line.split(",");
    const o = {};
    header.forEach((h, i) => {
      const v = cells[i];
      o[h === "model" ? "model" : h] = h === "model" ? v : Number(v);
    });
    return o;
  });

  const by = Object.fromEntries(rows.map((r) => [r.model, r]));
  const champion = "gbm_q0.9";
  const baseline = "naive";
  if (!by[champion] || !by[baseline]) {
    console.error(`  ERROR: results.csv lacks '${champion}' or '${baseline}'.`);
    process.exit(1);
  }

  // The headline the Overview page shows. Computed, never asserted.
  const vsNaive = (1 - by[champion].cost / by[baseline].cost) * 100;
  // The project's most instructive pair: lowest MAE is NOT lowest cost.
  const meanModel = by["gbm"];
  const maeDelta = meanModel ? (1 - meanModel.mae / by[champion].mae) * 100 : null;
  const costDelta = meanModel ? (meanModel.cost / by[champion].cost - 1) * 100 : null;

  writeFileSync(
    backtestDst,
    JSON.stringify({
      generatedFrom: "outputs/results.csv",
      champion,
      baseline,
      rows,
      championCost: by[champion].cost,
      baselineCost: by[baseline].cost,
      vsNaivePct: vsNaive,
      meanModelMaeBetterPct: maeDelta,
      meanModelCostWorsePct: costDelta,
    }, null, 1)
  );
  console.log(`  backtest.json      ${rows.length} models   vs naive: ${vsNaive.toFixed(1)}% lower cost`);
}
console.log("  -> web/public/data/");
```

#### `web/lib/types.ts`

```typescript
/**
 * Types derived from the ACTUAL shape of bench/replay*.json, not from a spec.
 * Verified against both files: 6 runs in replay.json, 9 in replay-step.json,
 * every run carrying 61 samples at t = 0, 20, ..., 1200.
 */

/** One controller decision, as logged by src/controller.py at that second. */
export interface Decision {
  t: number;              // seconds into the run
  now: number;            // req/s the controller observed
  pred: number;           // req/s it forecast for 60 s later
  pods_now: number;
  pods_target: number;
  /** From controller.py: replicas mode emits scale_*, floor mode emits floor_*. */
  action: "none" | "scale_up" | "scale_down" | "floor_up" | "floor_down" | "hold";
}

/** k6's whole-run aggregates, plus pod-seconds reconstructed from Prometheus. */
export interface RunSummary {
  p50: number;
  p95: number;
  p99: number;
  max: number;
  reqs: number;
  pod_seconds: number;
}

export interface Run {
  /** e.g. "A1r" (ramp) or "C1" (step). The prefix letter IS the arm. */
  name: string;
  arm: "baseline" | "predictive" | "floor";
  t: number[];
  /** Aligned with t. `null` where Prometheus had no sample. */
  rate: (number | null)[];
  pods: (number | null)[];
  p99: (number | null)[];
  /** Empty for baseline runs — arm A has no forecaster running. */
  decisions: Decision[];
  summary: RunSummary;
  started_utc: string;
}

export interface Replay {
  step_seconds: number;
  scenario: string;
  runs: Run[];
}

export interface BacktestRow {
  model: string;
  mae: number;
  mae_sd: number;
  rmse: number;
  smape: number;
  under: number;
  over: number;
  cost: number;
  folds: number;
}

export interface Backtest {
  generatedFrom: string;
  champion: string;
  baseline: string;
  rows: BacktestRow[];
  championCost: number;
  baselineCost: number;
  vsNaivePct: number;
  meanModelMaeBetterPct: number | null;
  meanModelCostWorsePct: number | null;
}
```

#### `web/lib/data.ts`

```typescript
import type { Backtest, Decision, Replay, Run } from "./types";
import rampJson from "../public/data/replay.json";
import stepJson from "../public/data/replay-step.json";
import backtestJson from "../public/data/backtest.json";

/**
 * A run's name prefix is the ONLY record of which arm it was: `make bench RUN=C1`
 * writes bench/C1.json and nothing inside it says MODE=hpa-floor. This table is
 * the decoder, and it has twins in src/../export_replay.py (ARM_OF_PREFIX) and
 * dashboard.py (ARMS) — change all three together.
 *
 * `dash` is not decoration. The three arm colours fail a colourblind-separation
 * check on their own (worst deuteranopia dE around 4.2 against a >=8 target), so
 * every series is keyed by stroke pattern AND colour AND a direct label. Nothing
 * on this site is encoded by colour alone.
 */
export const ARMS = {
  A: {
    key: "A",
    label: "Stock HPA",
    colour: "#8c2f39",              // wine
    descriptor: "scales on CPU it has already seen",
    dash: "",                        // solid
    dashArray: undefined as string | undefined,
  },
  B: {
    key: "B",
    label: "Predictive",
    colour: "#15616d",              // teal
    descriptor: "forecast sets the replica count",
    dash: "7 3",
    dashArray: "7 3",
  },
  C: {
    key: "C",
    label: "Predictive + floor",
    colour: "#4a6b2a",              // moss
    descriptor: "forecast sets the HPA's minReplicas",
    dash: "2 2",
    dashArray: "2 2",
  },
} as const;

export type ArmKey = keyof typeof ARMS;
export const ARM_ORDER: ArmKey[] = ["A", "B", "C"];

/** Every benchmark run is 20 minutes. */
export const RUN_SECONDS = 1200;
/** Samples are 20 s apart — `step_seconds` in the replay files. */
export const STEP_SECONDS = 20;
/** The pod gauge frame. Empty slots stay visible so headroom is legible. */
export const GAUGE_SLOTS = 8;

/**
 * Phase boundaries and event brackets are read off the k6 stage lists in
 * load/ramp.js and load/benchmark.js — never eyeballed from a chart. If a stage
 * duration changes there, these are wrong and the narration lies about the run.
 *
 *   ramp.js       4m low, 6m ramp to high, 4m hold, 6m down  -> event 240 s / 840 s
 *   benchmark.js  5m steady, 1s step, 4m hold, 1s release, 11m recover
 *                                                            -> event 300 s / 540 s
 */
export const SCENARIOS = [
  {
    id: "ramp",
    label: "Gradual ramp",
    file: "replay.json",
    data: rampJson as unknown as Replay,
    blurb:
      "Traffic climbs 20 to 80 req/s over six minutes. The rise is visible in the request rate before it hurts, so a forecaster has something to work with.",
    /** [start, end] of the load event, in seconds. */
    event: [240, 840] as [number, number],
    phases: [
      [240, "Steady traffic. Every arm sits at the 2-pod minimum."],
      [600, "The ramp. Traffic climbs 20 to 80 req/s. Watch the forecasting arms add pods while it is still rising."],
      [840, "The plateau. Traffic is at its peak. The stock HPA finally reaches 3 pods — but its response times already climbed."],
      [RUN_SECONDS + 1, "Winding down. Every arm releases pods."],
    ] as [number, string][],
  },
  {
    id: "step",
    label: "Instant spike",
    file: "replay-step.json",
    data: stepJson as unknown as Replay,
    blurb:
      "A 4x step in one second, with no precursor in the traffic. There is nothing to predict from — this is the scenario that shows what forecasting alone cannot do.",
    event: [300, 540] as [number, number],
    phases: [
      [300, "Steady at 20 req/s. Nothing in this traffic hints at what is coming."],
      [540, "The step. 20 to 80 req/s instantly. No arm had warning; what separates them now is only how fast capacity arrives."],
      [RUN_SECONDS + 1, "Recovery. This is where the forecast-only arm lost — it withdrew pods while the spike was still running. The floor arm cannot: lowering minReplicas only permits the HPA to shrink, and it declines while CPU is high."],
    ] as [number, string][],
  },
].filter((s) => s.data && Array.isArray(s.data.runs) && s.data.runs.length > 0);

export type Scenario = (typeof SCENARIOS)[number];

export const backtest = backtestJson as unknown as Backtest;

/**
 * {run number: {arm prefix: run}} — runs pair up by the digit in their name.
 * A1/B1/C1 are the same traffic sent three times, so they belong side by side;
 * A1 vs B2 would compare two different 20-minute windows.
 *
 * Faithful port of dashboard.group_runs().
 */
export function groupRuns(replay: Replay): Record<string, Partial<Record<ArmKey, Run>>> {
  const out: Record<string, Partial<Record<ArmKey, Run>>> = {};
  for (const r of replay.runs) {
    const num = r.name[1];
    const prefix = r.name[0] as ArmKey;
    (out[num] ??= {})[prefix] = r;
  }
  return out;
}

/**
 * Mean p99 and pod-seconds per arm — the same mean analyze.py prints.
 * Averaged from the data so the headline follows the runs when a scenario is
 * switched. Stale hardcoded figures in a masthead would be worse than none.
 *
 * Faithful port of dashboard.arm_means().
 */
export function armMeans(replay: Replay): Partial<Record<ArmKey, { p99: number; pod_seconds: number }>> {
  const acc: Partial<Record<ArmKey, Run["summary"][]>> = {};
  for (const r of replay.runs) {
    const prefix = r.name[0] as ArmKey;
    (acc[prefix] ??= []).push(r.summary);
  }
  const out: Partial<Record<ArmKey, { p99: number; pod_seconds: number }>> = {};
  for (const [prefix, list] of Object.entries(acc) as [ArmKey, Run["summary"][]][]) {
    out[prefix] = {
      p99: list.reduce((a, s) => a + s.p99, 0) / list.length,
      pod_seconds: list.reduce((a, s) => a + s.pod_seconds, 0) / list.length,
    };
  }
  return out;
}

/**
 * Lowest-p99 non-baseline arm, with its deltas against the baseline.
 * Picked FROM THE DATA, never asserted: on the step scenario the winner is the
 * floor arm, on the ramp there is only one candidate, and hardcoding either
 * would go stale the first time a run is added.
 *
 * Faithful port of dashboard.best_arm().
 */
export function bestArm(
  means: Partial<Record<ArmKey, { p99: number; pod_seconds: number }>>
): { arm: ArmKey; latPct: number; costPct: number } | null {
  const base = means.A;
  const rivals = (Object.keys(means) as ArmKey[]).filter((k) => k !== "A");
  if (!base || rivals.length === 0) return null;
  const arm = rivals.reduce((best, k) => (means[k]!.p99 < means[best]!.p99 ? k : best), rivals[0]);
  return {
    arm,
    latPct: (1 - means[arm]!.p99 / base.p99) * 100,
    costPct: (means[arm]!.pod_seconds / base.pod_seconds - 1) * 100,
  };
}

/**
 * Last known value at or before t — the reading a dashboard would show.
 * Faithful port of dashboard.value_at(); `null` samples are skipped, not zeroed.
 */
export function valueAt(run: Run, key: "rate" | "pods" | "p99", t: number): number | null {
  let v: number | null = null;
  const series = run[key];
  for (let i = 0; i < run.t.length; i++) {
    if (run.t[i] > t) break;
    if (series[i] !== null && series[i] !== undefined) v = series[i] as number;
  }
  return v;
}

/** Last decision at or before t. Faithful port of dashboard.decision_at(). */
export function decisionAt(run: Run, t: number): Decision | null {
  let d: Decision | null = null;
  for (const x of run.decisions) {
    if (x.t > t) break;
    d = x;
  }
  return d;
}

/** Which arms are present in a given run pairing, in canonical A/B/C order. */
export function presentArms(arms: Partial<Record<ArmKey, Run>>): ArmKey[] {
  return ARM_ORDER.filter((k) => arms[k] !== undefined);
}

export function phaseAt(scenario: Scenario, t: number): string {
  for (const [until, text] of scenario.phases) if (t < until) return text;
  return scenario.phases[scenario.phases.length - 1][1];
}

export const fmtClock = (t: number) =>
  `${Math.floor(t / 60)}:${String(t % 60).padStart(2, "0")}`;
```

#### `web/app/layout.tsx`

```tsx
import type { Metadata } from "next";
import { Newsreader, IBM_Plex_Sans, IBM_Plex_Mono } from "next/font/google";
import "./globals.css";

/* Self-hosted at build time by next/font, so there is no render-blocking
   request to Google and no font-swap layout shift. */
const serif = Newsreader({ subsets: ["latin"], weight: ["400", "500", "600"], variable: "--font-serif", display: "swap" });
const sans = IBM_Plex_Sans({ subsets: ["latin"], weight: ["400", "500", "600"], variable: "--font-sans", display: "swap" });
const mono = IBM_Plex_Mono({ subsets: ["latin"], weight: ["400", "500", "600"], variable: "--font-mono", display: "swap" });

export const metadata: Metadata = {
  title: "Predictive Autoscaling for Kubernetes",
  description:
    "An A/B benchmark of predictive versus reactive Kubernetes autoscaling, measured on a kind cluster over three runs per arm.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${serif.variable} ${sans.variable} ${mono.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

#### `web/app/globals.css`

```css
/* ---------------------------------------------------------------------------
   A printed technical report, not a dashboard.

   Tokens are ported verbatim from dashboard.py and .streamlit/config.toml so
   the deployed site and the local Streamlit tool remain visibly the same
   project. Contrast ratios below were measured against the paper ground.
   --------------------------------------------------------------------------- */

:root {
  --paper: #e8edee;    /* cool blue-grey drafting stock */
  --card: #ffffff;
  --stone: #dde4e5;
  --ink: #101619;      /* 15.5:1 on paper */
  --muted: #4d565a;    /* 6.4:1  — body copy */
  --faint: #5d666a;    /* 5.0:1  — captions and labels, still AA body */
  --rule: #c8d1d3;     /* hairlines only, never text */
  --rule-soft: #d8e0e1;

  --arm-a: #8c2f39;    /* wine  — stock HPA */
  --arm-b: #15616d;    /* teal  — predictive owns the replica count */
  --arm-c: #4a6b2a;    /* moss  — predictive raises the HPA's floor */

  --serif: "Newsreader", Georgia, "Times New Roman", serif;
  --sans: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, monospace;
  --focus: #15616d;
}

*, *::before, *::after { box-sizing: border-box; }

html { -webkit-text-size-adjust: 100%; }

body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--sans);
  font-size: 16px;
  line-height: 1.5;
  /* The page body must never scroll sideways; wide things scroll inside
     their own container instead. */
  overflow-x: hidden;
}

.wrap { max-width: 1180px; margin: 0 auto; padding: 1.6rem 1.25rem 6rem; }

/* ---- type ------------------------------------------------------------------
   Everything you READ is the serif; everything you MEASURE is the mono. That
   split is the whole typographic idea, and it is why the two faces never have
   to compete for the same job. */
h1, h2, h3 { font-family: var(--serif); color: var(--ink); margin: 0; }
h1 { font-size: clamp(2rem, 6vw, 3rem); font-weight: 500; letter-spacing: -0.015em; line-height: 1.1; margin-bottom: 0.6rem; }
h2 { font-size: clamp(1.4rem, 4vw, 1.75rem); font-weight: 500; letter-spacing: -0.01em; margin-bottom: 0.25rem; }
h3 { font-size: 1.1rem; font-weight: 600; }

.mono, .num { font-family: var(--mono); font-variant-numeric: tabular-nums; }
code { font-family: var(--mono); background: var(--stone); padding: 0.1em 0.35em; border-radius: 3px; font-size: 0.88em; }

.eyebrow {
  font-family: var(--mono); font-size: 0.66rem; font-weight: 500;
  letter-spacing: 0.1em; text-transform: uppercase; color: var(--faint);
  display: block; margin: 0 0 0.4rem;
}

.lede { font-family: var(--serif); color: var(--muted); font-size: clamp(1rem, 2.6vw, 1.18rem); line-height: 1.65; max-width: 62ch; margin: 0.35rem 0 0; }

/* ---- masthead --------------------------------------------------------------
   A document head, not an app shell: heavy rule, wordmark left, provenance
   right. This replaces the sidebar entirely. */
.mast {
  border-top: 3px solid var(--ink); border-bottom: 1px solid var(--ink);
  padding: 0.75rem 0 0.7rem;
  display: flex; align-items: baseline; justify-content: space-between;
  gap: 1rem; flex-wrap: wrap;
}
.mast .wordmark { font-family: var(--serif); font-size: clamp(1.05rem, 3vw, 1.32rem); font-weight: 600; letter-spacing: -0.01em; }
.mast .prov { font-family: var(--mono); font-size: 0.62rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--faint); }

/* ---- nav strip -------------------------------------------------------------- */
.nav { display: flex; gap: 0.35rem; padding: 0.55rem 0; flex-wrap: wrap; }
.nav a {
  font-family: var(--sans); font-size: 0.92rem; color: var(--muted);
  text-decoration: none; padding: 0.4rem 0.75rem; border-radius: 3px;
  border: 1px solid transparent; transition: background 120ms ease, color 120ms ease, box-shadow 120ms ease;
}
.nav a:hover { background: var(--card); color: var(--ink); box-shadow: 0 1px 0 rgba(16, 22, 25, 0.14); }
.nav a[aria-current="page"] { background: var(--card); color: var(--ink); font-weight: 600; border-color: var(--rule); }

/* ---- spec strip: the measured constants, read across ------------------------ */
.spec {
  display: flex; flex-wrap: wrap; gap: 0.3rem 1.9rem;
  border-top: 1px solid var(--rule); border-bottom: 1px solid var(--ink);
  padding: 0.6rem 0 0.65rem; margin: 0 0 2.4rem;
}
.spec div { display: flex; align-items: baseline; gap: 0.5rem; }
.spec dt, .spec .k { font-family: var(--mono); font-size: 0.6rem; letter-spacing: 0.09em; text-transform: uppercase; color: var(--faint); margin: 0; }
.spec dd, .spec .v { font-family: var(--mono); font-size: 0.82rem; font-weight: 600; color: var(--ink); font-variant-numeric: tabular-nums; margin: 0; }

/* ---- hero ------------------------------------------------------------------- */
.hero { font-family: var(--serif); font-size: clamp(3.5rem, 14vw, 7rem); font-weight: 500; line-height: 0.9; letter-spacing: -0.03em; color: var(--arm-a); font-variant-numeric: tabular-nums; margin: 0.1rem 0 0.7rem; }
.hero-note { color: var(--muted); font-size: 1rem; line-height: 1.65; max-width: 42ch; font-family: var(--serif); }

/* ---- figure block: a keyed table of results --------------------------------- */
.figblock { border-top: 2px solid var(--ink); }
.figblock .row { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; padding: 0.8rem 0; border-bottom: 1px solid var(--rule); }
.figblock .lbl { font-family: var(--serif); font-size: 0.95rem; color: var(--muted); max-width: 22ch; line-height: 1.4; }
.statv { font-family: var(--mono); font-size: clamp(1.1rem, 3.5vw, 1.4rem); font-weight: 600; color: var(--ink); white-space: nowrap; display: block; text-align: right; }
.statn { font-size: 0.78rem; color: var(--faint); display: block; margin-top: 0.15rem; font-family: var(--serif); text-align: right; }

/* ---- section heading --------------------------------------------------------- */
.sec { margin: 3.4rem 0 1.2rem; border-top: 2px solid var(--ink); padding-top: 1rem; }
.sec p { color: var(--muted); font-size: 1rem; margin: 0.35rem 0 0; max-width: 68ch; font-family: var(--serif); line-height: 1.6; }

/* ---- cards -------------------------------------------------------------------- */
.card { background: var(--card); border: 1px solid var(--rule); border-radius: 3px; padding: 1.35rem 1.45rem; }
.card p { color: var(--muted); font-size: 0.95rem; line-height: 1.65; margin: 0; font-family: var(--serif); }
.card p + p { margin-top: 0.6rem; }
.cardgrid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.1rem; align-items: stretch; }
.cardgrid .card { display: flex; flex-direction: column; }
.cardfigs { display: flex; gap: 1.5rem; flex-wrap: wrap; margin-top: auto; padding-top: 1.1rem; }
@media (max-width: 860px) { .cardgrid { grid-template-columns: 1fr; } }

/* ---- note: the reader's key --------------------------------------------------- */
.note { background: var(--card); border: 1px solid var(--rule); border-left: 3px solid var(--ink); padding: 1rem 1.2rem; margin: 0 0 1.8rem; border-radius: 0 3px 3px 0; }
.note p { margin: 0; font-family: var(--serif); font-size: 0.96rem; line-height: 1.65; color: var(--muted); }
.note p + p { margin-top: 0.55rem; }

/* ---- steps ---------------------------------------------------------------------- */
.steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.1rem; }
@media (max-width: 860px) { .steps { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 520px) { .steps { grid-template-columns: 1fr; } }
.step { border-top: 1px solid var(--ink); padding: 0.8rem 0 0; }
.step b { display: block; font-family: var(--mono); font-size: 0.7rem; letter-spacing: 0.1em; color: var(--arm-a); margin-bottom: 0.45rem; }
.step p { color: var(--muted); font-size: 0.9rem; line-height: 1.6; margin: 0.35rem 0 0; font-family: var(--serif); }

/* ---- arm column ----------------------------------------------------------------- */
.armgrid { display: grid; gap: 1rem; }
.armhead { padding: 0.3rem 0 0.35rem 0.75rem; border-left: 3px solid var(--key); margin: 0 0 0.85rem; min-height: 48px; }
.armhead b { display: block; font-family: var(--serif); font-size: 1.15rem; font-weight: 600; color: var(--key); line-height: 1.25; }
.armhead span { display: block; margin-top: 0.1rem; font-size: 0.75rem; color: var(--faint); line-height: 1.35; }

/* ---- pod gauge: filled slots against a FIXED frame -------------------------------
   Unfilled slots stay visible so "3 of a possible 8" is legible at a glance; a
   bare count of blocks hides how much headroom is left. */
.pods { display: flex; gap: 4px; align-items: flex-end; height: 34px; margin: 0 0 0.7rem; }
.pods i { flex: 0 0 19px; height: 34px; border-radius: 2px; display: block; border: 1px solid var(--rule); background: var(--card); }
.pods i.on { border-color: transparent; }

.armstats { display: flex; gap: 0.4rem; }
.armstats > div { flex: 1 1 0; min-width: 0; background: var(--card); border: 1px solid var(--rule); border-radius: 3px; padding: 0.5rem 0.6rem; }
.armstats .eyebrow { font-size: 0.55rem; letter-spacing: 0.06em; margin: 0; }
.armstats b { font-family: var(--mono); font-size: 1.08rem; font-weight: 600; color: var(--ink); display: block; margin-top: 0.2rem; white-space: nowrap; font-variant-numeric: tabular-nums; }
.armnote { color: var(--muted); font-size: 0.87rem; line-height: 1.6; margin: 0.8rem 0 0; font-family: var(--serif); }
.armnote b { color: var(--ink); font-weight: 600; }

/* ---- controls --------------------------------------------------------------------- */
.controls { display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: flex-end; margin-bottom: 1.2rem; }
.ctl { display: flex; flex-direction: column; gap: 0.35rem; }
.ctl > .eyebrow { margin: 0; }
.seg { display: flex; gap: 0; border: 1px solid var(--rule); border-radius: 3px; overflow: hidden; background: var(--paper); }
.seg button {
  font-family: var(--sans); font-size: 0.9rem; color: var(--muted); cursor: pointer;
  background: transparent; border: 0; border-right: 1px solid var(--rule);
  padding: 0.5rem 0.9rem; min-height: 40px;
  transition: background 120ms ease, color 120ms ease;
}
.seg button:last-child { border-right: 0; }
.seg button:hover { background: var(--card); color: var(--ink); }
.seg button:active { transform: translateY(1px); }
.seg button[aria-pressed="true"] { background: var(--card); color: var(--ink); font-weight: 600; }

button.play {
  font-family: var(--sans); font-size: 0.9rem; cursor: pointer; min-height: 40px;
  background: var(--card); color: var(--ink); border: 1px solid var(--rule);
  border-radius: 3px; padding: 0.5rem 1rem; transition: background 120ms ease;
}
button.play:hover { background: var(--stone); }

:where(a, button, input, [tabindex]):focus-visible {
  outline: 2px solid var(--focus); outline-offset: 2px; border-radius: 3px;
}

/* ---- playhead ----------------------------------------------------------------------- */
.playhead { margin: 0.4rem 0 1.2rem; }
.playhead input[type="range"] { width: 100%; accent-color: var(--arm-a); height: 28px; cursor: pointer; }
.playrow { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 0.7rem; color: var(--faint); }

.phase { display: flex; gap: 1rem; align-items: baseline; background: var(--card); border: 1px solid var(--rule); border-radius: 3px; padding: 0.9rem 1.1rem; margin: 0 0 1.6rem; }
.phase b { font-family: var(--mono); color: var(--arm-b); font-size: 0.95rem; white-space: nowrap; }
.phase span { color: var(--muted); font-size: 0.92rem; line-height: 1.5; font-family: var(--serif); }

/* ---- charts ---------------------------------------------------------------------------
   Wide content scrolls inside its own container. The page body never does. */
.chartbox { background: var(--card); border: 1px solid var(--rule); border-radius: 3px; padding: 1rem 1.1rem 0.6rem; margin-bottom: 1rem; }
.chartscroll { overflow-x: auto; overflow-y: hidden; }
.chartscroll svg { display: block; }
.charttitle { font-family: var(--serif); font-weight: 600; font-size: 1rem; margin: 0 0 0.15rem; }
.chartlegend { display: flex; gap: 1rem; flex-wrap: wrap; margin: 0.2rem 0 0.6rem; }
.chartlegend span { display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.78rem; color: var(--muted); font-family: var(--sans); }

details.datatable { margin: 0.2rem 0 0.4rem; }
details.datatable summary { font-size: 0.78rem; color: var(--faint); cursor: pointer; padding: 0.3rem 0; font-family: var(--sans); }
details.datatable summary:hover { color: var(--ink); }
.tablescroll { overflow-x: auto; max-height: 320px; overflow-y: auto; }

table.data { border-collapse: collapse; width: 100%; font-family: var(--mono); font-size: 0.75rem; font-variant-numeric: tabular-nums; }
table.data th, table.data td { border-bottom: 1px solid var(--rule); padding: 0.35rem 0.6rem; text-align: right; white-space: nowrap; }
table.data th:first-child, table.data td:first-child { text-align: left; }
table.data th { font-family: var(--sans); font-size: 0.62rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--faint); font-weight: 600; position: sticky; top: 0; background: var(--card); }
table.data tbody tr:hover { background: var(--stone); }

/* ---- verdict ----------------------------------------------------------------------------- */
.verdict { font-family: var(--serif); color: var(--muted); font-size: 0.95rem; line-height: 1.65; margin: 0.8rem 0 0; }
.verdict b { color: var(--ink); }

.footnote { color: var(--faint); font-size: 0.82rem; margin-top: 3rem; padding-top: 1.2rem; border-top: 1px solid var(--rule); font-family: var(--serif); line-height: 1.6; }
.footnote a { color: var(--arm-b); }

.visually-hidden {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* Motion is never load-bearing here: Play is a convenience over the slider,
   which stays fully usable. */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition: none !important; animation: none !important; }
}

/* Overview hero and its figure block stack on narrow screens. */
@media (max-width: 860px) {
  .overview-split { grid-template-columns: 1fr !important; gap: 2rem !important; }
}
/* Three arm columns become one on a phone; two-arm scenarios use the same rule. */
@media (max-width: 780px) {
  .armgrid { grid-template-columns: 1fr !important; }
}
```

#### `web/components/Chrome.tsx`

```tsx
import Link from "next/link";
import { backtest } from "@/lib/data";

/**
 * The measured constants, shown as a spec strip under the masthead rather than
 * stacked in a sidebar. Every one of these was measured on the cluster; none is
 * an estimate. The last is COMPUTED from outputs/results.csv at build time.
 *
 * The Streamlit version also carried a "prometheus connected/offline" chip.
 * It is dropped here: on a public deployment there is no cluster to be
 * connected to, so the chip could only ever say "offline" and would imply
 * something was broken.
 */
const SPECS: [string, string][] = [
  ["pod start-up", "19 s"],
  ["one pod serves", "20 req/s"],
  ["horizon", "60 s"],
  ["history", "51 h"],
];

export function Masthead({ current }: { current: "overview" | "benchmark" }) {
  const vsNaive = `−${backtest.vsNaivePct.toFixed(1)}%`;
  return (
    <header>
      <div className="mast">
        <span className="wordmark">Predictive Autoscaling for Kubernetes</span>
        <span className="prov">A/B benchmark &middot; kind cluster &middot; 3 runs per arm</span>
      </div>
      <nav className="nav" aria-label="Sections">
        <Link href="/" aria-current={current === "overview" ? "page" : undefined}>Overview</Link>
        <Link href="/benchmark" aria-current={current === "benchmark" ? "page" : undefined}>Benchmark replay</Link>
      </nav>
      <dl className="spec">
        {SPECS.map(([k, v]) => (
          <div key={k}>
            <dt className="k">{k}</dt>
            <dd className="v">{v}</dd>
          </div>
        ))}
        <div>
          <dt className="k">vs naive forecast</dt>
          <dd className="v">{vsNaive}</dd>
        </div>
      </dl>
    </header>
  );
}

export function Footnote() {
  return (
    <p className="footnote">
      Every figure was measured on a local kind cluster — 51 hours of recorded traffic, three
      20-minute runs per arm, byte-identical load in every arm. The traffic is synthetic; the
      measurements are not. This site reads only the recordings committed to the repository and
      never contacts a cluster. The live-forecast view is local-only and is not deployed here —
      it needs Prometheus and the trained model in-process.{" "}
      <a href="https://github.com/pavansai2608/predictive-autoscaling">Source on GitHub</a>.
    </p>
  );
}
```

#### `web/components/Chart.tsx`

```tsx
"use client";

import { RUN_SECONDS } from "@/lib/data";

export interface ChartSeries {
  label: string;
  colour: string;
  /** SVG stroke-dasharray. Series are keyed by dash AND colour AND a direct
   *  label, because the three arm colours do not separate under deuteranopia. */
  dashArray?: string;
  points: { t: number; v: number | null }[];
}

interface Props {
  title: string;
  unit: string;
  series: ChartSeries[];
  /** Draw only up to here, so dragging the playhead replays the run. */
  playhead: number;
  /** [start, end] of the load event in seconds, read off the k6 stage list. */
  event: [number, number];
  height?: number;
  /** Step-after interpolation for pod counts — replicas change discretely. */
  step?: boolean;
}

const W = 760;
const PAD = { top: 14, right: 96, bottom: 30, left: 46 };

/**
 * Hand-rolled SVG rather than a charting library: the whole chart is four
 * paths and some text, and every library considered ships its own theme that
 * would fight the report styling. Bundle cost here is zero.
 */
export default function Chart({ title, unit, series, playhead, event, height = 220, step = false }: Props) {
  const H = height;
  const iw = W - PAD.left - PAD.right;
  const ih = H - PAD.top - PAD.bottom;

  // The y-axis is scaled to the WHOLE run, never to what has been drawn yet.
  // A y-axis that grows as you scrub makes an early spike look identical to a
  // late one, and the panel would resize on every slider tick.
  const allValues = series.flatMap((s) => s.points.map((p) => p.v)).filter((v): v is number => v !== null);
  const yMax = allValues.length ? Math.max(...allValues) * 1.08 : 1;

  const x = (t: number) => PAD.left + (t / RUN_SECONDS) * iw;
  const y = (v: number) => PAD.top + ih - (v / yMax) * ih;

  const yTicks = 4;
  const xTicks = 6;

  const pathFor = (s: ChartSeries) => {
    const pts = s.points.filter((p) => p.t <= playhead && p.v !== null) as { t: number; v: number }[];
    if (pts.length === 0) return "";
    let d = `M ${x(pts[0].t).toFixed(1)} ${y(pts[0].v).toFixed(1)}`;
    for (let i = 1; i < pts.length; i++) {
      if (step) d += ` H ${x(pts[i].t).toFixed(1)} V ${y(pts[i].v).toFixed(1)}`;
      else d += ` L ${x(pts[i].t).toFixed(1)} ${y(pts[i].v).toFixed(1)}`;
    }
    return d;
  };

  const lastPoint = (s: ChartSeries) => {
    const pts = s.points.filter((p) => p.t <= playhead && p.v !== null) as { t: number; v: number }[];
    return pts.length ? pts[pts.length - 1] : null;
  };

  // Direct labels are stacked apart when two series end at nearly the same
  // height, otherwise they overprint and the keying is lost.
  const labels = series
    .map((s) => ({ s, p: lastPoint(s) }))
    .filter((o): o is { s: ChartSeries; p: { t: number; v: number } } => o.p !== null)
    .sort((a, b) => a.p.v - b.p.v);
  const placed: number[] = [];
  for (const l of labels) {
    let ly = y(l.p.v);
    for (const p of placed) if (Math.abs(ly - p) < 13) ly = p - 13;
    placed.push(ly);
  }

  const summary = series
    .map((s) => {
      const p = lastPoint(s);
      return `${s.label} ${p ? p.v : "no data"}`;
    })
    .join("; ");

  return (
    <figure className="chartbox" style={{ margin: 0 }}>
      <figcaption>
        <p className="charttitle">{title}</p>
        <div className="chartlegend" aria-hidden="true">
          {series.map((s) => (
            <span key={s.label}>
              <svg width="22" height="8" aria-hidden="true">
                <line x1="0" y1="4" x2="22" y2="4" stroke={s.colour} strokeWidth="2.5" strokeDasharray={s.dashArray} />
              </svg>
              {s.label}
            </span>
          ))}
        </div>
      </figcaption>

      <div className="chartscroll">
        <svg
          viewBox={`0 0 ${W} ${H}`}
          width="100%"
          style={{ minWidth: 560 }}
          role="img"
          aria-label={`${title}, in ${unit}, from 0 to ${playhead} seconds into the run. At the playhead: ${summary}. The full numbers are in the table below this chart.`}
        >
          {/* horizontal grid + y labels */}
          {Array.from({ length: yTicks + 1 }, (_, i) => {
            const v = (yMax / yTicks) * i;
            return (
              <g key={i}>
                <line x1={PAD.left} y1={y(v)} x2={PAD.left + iw} y2={y(v)} stroke="#d8e0e1" strokeWidth="1" />
                <text x={PAD.left - 8} y={y(v) + 3.5} textAnchor="end" fontFamily="var(--font-mono), monospace" fontSize="10" fill="#5d666a">
                  {v >= 100 ? Math.round(v) : Math.round(v * 10) / 10}
                </text>
              </g>
            );
          })}

          {/* the load event, bracketed from the k6 stage list */}
          {event.map((e, i) => (
            <line key={i} x1={x(e)} y1={PAD.top} x2={x(e)} y2={PAD.top + ih} stroke="#101619" strokeWidth="1" strokeDasharray="3 3" opacity="0.34" />
          ))}

          {/* x labels */}
          {Array.from({ length: xTicks + 1 }, (_, i) => {
            const t = (RUN_SECONDS / xTicks) * i;
            return (
              <text key={i} x={x(t)} y={H - 10} textAnchor="middle" fontFamily="var(--font-mono), monospace" fontSize="10" fill="#5d666a">
                {t}
              </text>
            );
          })}
          <text x={PAD.left + iw / 2} y={H - 0.5} textAnchor="middle" fontFamily="var(--font-sans), sans-serif" fontSize="10" fill="#5d666a">
            seconds into run
          </text>

          {/* the playhead itself */}
          <line x1={x(playhead)} y1={PAD.top} x2={x(playhead)} y2={PAD.top + ih} stroke="#8c2f39" strokeWidth="1" opacity="0.4" />

          {series.map((s) => (
            <path key={s.label} d={pathFor(s)} fill="none" stroke={s.colour} strokeWidth="2" strokeDasharray={s.dashArray} strokeLinejoin="round" strokeLinecap="round" />
          ))}

          {/* direct labels — never rely on colour alone */}
          {labels.map((l, i) => (
            <text key={l.s.label} x={PAD.left + iw + 6} y={placed[i] + 3.5} fontFamily="var(--font-sans), sans-serif" fontSize="10.5" fill={l.s.colour} fontWeight="600">
              {l.s.label}
            </text>
          ))}
        </svg>
      </div>

      <details className="datatable">
        <summary>Show the numbers behind this chart</summary>
        <div className="tablescroll">
          <table className="data">
            <caption className="visually-hidden">{title}, every sample up to the playhead, in {unit}</caption>
            <thead>
              <tr>
                <th scope="col">t (s)</th>
                {series.map((s) => (<th key={s.label} scope="col">{s.label}</th>))}
              </tr>
            </thead>
            <tbody>
              {series[0].points.filter((p) => p.t <= playhead).map((p, i) => (
                <tr key={p.t}>
                  <td>{p.t}</td>
                  {series.map((s) => (<td key={s.label}>{s.points[i]?.v ?? "—"}</td>))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </details>
    </figure>
  );
}
```

#### `web/components/BenchmarkView.tsx`

```tsx
"use client";

import { useEffect, useMemo, useState } from "react";
import Chart, { type ChartSeries } from "./Chart";
import {
  ARMS, GAUGE_SLOTS, RUN_SECONDS, SCENARIOS, STEP_SECONDS,
  armMeans, decisionAt, fmtClock, groupRuns, phaseAt, presentArms, valueAt,
  type ArmKey,
} from "@/lib/data";
import type { Run } from "@/lib/types";

/** n filled slots out of 8, so headroom is visible rather than implied. */
function PodGauge({ n, colour, label }: { n: number; colour: string; label: string }) {
  return (
    <div className="pods" role="img" aria-label={`${label}: ${n} of ${GAUGE_SLOTS} pod slots filled`}>
      {Array.from({ length: GAUGE_SLOTS }, (_, i) => (
        <i key={i} className={i < n ? "on" : ""} style={i < n ? { background: colour } : undefined} />
      ))}
    </div>
  );
}

export default function BenchmarkView() {
  const [scenarioId, setScenarioId] = useState(SCENARIOS[0].id);
  const [runNum, setRunNum] = useState("1");
  const [t, setT] = useState(RUN_SECONDS);   // opens on the finished run, not an empty one
  const [playing, setPlaying] = useState(false);

  const scenario = SCENARIOS.find((s) => s.id === scenarioId) ?? SCENARIOS[0];
  const grouped = useMemo(() => groupRuns(scenario.data), [scenario]);
  const runNumbers = Object.keys(grouped).sort();
  const activeRun = grouped[runNum] ? runNum : runNumbers[0];
  const arms = grouped[activeRun];
  const present = presentArms(arms);
  const means = useMemo(() => armMeans(scenario.data), [scenario]);

  // Play advances one 20 s step per tick and rewinds at the end, so pressing it
  // on a finished run means "watch it again" rather than sitting inert.
  useEffect(() => {
    if (!playing) return;
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduced) { setPlaying(false); return; }
    const id = window.setInterval(() => {
      setT((prev) => (prev >= RUN_SECONDS ? 0 : prev + STEP_SECONDS));
    }, 400);
    return () => window.clearInterval(id);
  }, [playing]);

  const seriesFor = (key: "p99" | "pods" | "rate"): ChartSeries[] =>
    present.map((k) => {
      const run = arms[k]!;
      return {
        label: ARMS[k].label,
        colour: ARMS[k].colour,
        dashArray: ARMS[k].dashArray,
        points: run.t.map((tt, i) => ({ t: tt, v: run[key][i] })),
      };
    });

  const baseline = arms.A;

  return (
    <>
      <div className="note">
        <p>
          <b>Three arms, same traffic.</b> Each 20-minute run is replayed against every scaling
          policy: <b style={{ color: ARMS.A.colour }}>Stock HPA</b> reacts to CPU,{" "}
          <b style={{ color: ARMS.B.colour }}>Predictive</b> lets the forecast set the replica count
          outright, and <b style={{ color: ARMS.C.colour }}>Predictive + floor</b> lets it set the
          HPA&apos;s <code>minReplicas</code> instead — so the forecast can add capacity early but
          never take it away. The floor arm was only run on the instant spike.
        </p>
        <p>
          <b>Two numbers, always together.</b> <b>Slowest 1%</b> is p99 response time, what your
          unluckiest users actually feel. <b>Compute</b> is pod-seconds: replicas multiplied by the
          seconds they ran. Quoting either one alone is how a benchmark gets to look better than it
          is.
        </p>
      </div>

      <div className="controls">
        <div className="ctl">
          <span className="eyebrow" id="lbl-scenario">Scenario</span>
          <div className="seg" role="group" aria-labelledby="lbl-scenario">
            {SCENARIOS.map((s) => (
              <button key={s.id} type="button" aria-pressed={s.id === scenarioId}
                onClick={() => { setScenarioId(s.id); setT(RUN_SECONDS); }}>
                {s.label}
              </button>
            ))}
          </div>
        </div>

        <div className="ctl">
          <span className="eyebrow" id="lbl-run">Run</span>
          <div className="seg" role="group" aria-labelledby="lbl-run">
            {runNumbers.map((n) => (
              <button key={n} type="button" aria-pressed={n === activeRun} onClick={() => setRunNum(n)}>
                Run {n}
              </button>
            ))}
          </div>
        </div>

        <div className="ctl">
          <span className="eyebrow">&nbsp;</span>
          <button type="button" className="play" onClick={() => setPlaying((p) => !p)}
            aria-pressed={playing}>
            {playing ? "Pause" : "Play"}
          </button>
        </div>
      </div>

      <div className="playhead">
        <label htmlFor="playhead" className="eyebrow">
          Position in the run — {t} s
        </label>
        <input id="playhead" type="range" min={0} max={RUN_SECONDS} step={STEP_SECONDS} value={t}
          onChange={(e) => { setPlaying(false); setT(Number(e.target.value)); }}
          aria-valuetext={`${t} seconds into the run`} />
        <div className="playrow"><span>0 s</span><span>{RUN_SECONDS} s</span></div>
      </div>

      <div className="phase">
        <b>{fmtClock(t)}</b>
        <span>{phaseAt(scenario, t)}</span>
      </div>

      <div className="armgrid" style={{ gridTemplateColumns: `repeat(${present.length}, minmax(0, 1fr))` }}>
        {present.map((k) => {
          const run = arms[k]!;
          const rate = valueAt(run, "rate", t) ?? 0;
          const pods = valueAt(run, "pods", t) ?? 0;
          const p99 = valueAt(run, "p99", t);
          const d = decisionAt(run, t);
          const act = d?.action === "scale_up" ? " · adding a pod now"
            : d?.action === "floor_up" ? " · raising the hpa's floor now" : "";
          return (
            <div key={k}>
              <div className="armhead" style={{ ["--key" as string]: ARMS[k].colour }}>
                <b>{ARMS[k].label}</b>
                <span>{ARMS[k].descriptor}</span>
              </div>
              <PodGauge n={pods} colour={ARMS[k].colour} label={ARMS[k].label} />
              <div className="armstats">
                <div><span className="eyebrow">Traffic</span><b>{rate.toFixed(0)}/s</b></div>
                <div><span className="eyebrow">Pods</span><b>{pods}</b></div>
                <div><span className="eyebrow">Slowest 1%</span><b>{p99 !== null ? `${p99} ms` : "–"}</b></div>
              </div>
              <p className="armnote">
                {d ? (
                  <>Model: now <b>{d.now.toFixed(0)}/s</b>, expects <b>{d.pred.toFixed(0)}/s</b> in
                  60 s → wants <b>{d.pods_target} pods</b>{act}</>
                ) : run.arm === "baseline" ? (
                  "No forecast — this version only reacts to what already happened."
                ) : (
                  " "
                )}
              </p>
            </div>
          );
        })}
      </div>

      <section className="sec">
        <h2>What happened</h2>
        <p>Drawn only up to the playhead, so the run unfolds as you scrub. Dashed verticals bracket the load event.</p>
      </section>

      <Chart title="Response time of the slowest 1% (ms)" unit="milliseconds"
        series={seriesFor("p99")} playhead={t} event={scenario.event} height={260} />
      <Chart title="Pods running" unit="pods"
        series={seriesFor("pods")} playhead={t} event={scenario.event} height={190} step />
      <Chart title="Requests arriving per second" unit="requests per second"
        series={seriesFor("rate")} playhead={t} event={scenario.event} height={190} />

      <section className="sec">
        <h2>What this run measured</h2>
        <p>
          This single run only. The overview page averages all {runNumbers.length} runs per arm,
          which is the figure worth quoting.
        </p>
      </section>

      <div className="chartbox">
        <div className="tablescroll">
          <table className="data">
            <caption className="visually-hidden">Per-arm results for run {activeRun}</caption>
            <thead>
              <tr>
                <th scope="col">Version</th>
                <th scope="col">Slowest 1%</th>
                <th scope="col">Typical</th>
                <th scope="col">Compute used</th>
              </tr>
            </thead>
            <tbody>
              {present.map((k) => {
                const s = arms[k]!.summary;
                return (
                  <tr key={k}>
                    <td style={{ color: ARMS[k].colour, fontWeight: 600 }}>{ARMS[k].label}</td>
                    <td>{s.p99} ms</td>
                    <td>{s.p50} ms</td>
                    <td>{s.pod_seconds.toLocaleString("en-GB")} pod-s</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {baseline &&
        present.filter((k) => k !== "A").map((k) => {
          const s = arms[k]!.summary;
          const b = baseline.summary;
          const lat = (1 - s.p99 / b.p99) * 100;
          const cost = (s.pod_seconds / b.pod_seconds - 1) * 100;
          return (
            <p className="verdict" key={k}>
              <b style={{ color: ARMS[k].colour }}>{ARMS[k].label}</b> — p99{" "}
              <b>{lat.toFixed(0)}% {lat >= 0 ? "lower" : "higher"}</b> than the stock HPA ({b.p99} ms
              → {s.p99} ms), using <b>{cost >= 0 ? "+" : ""}{cost.toFixed(0)}% compute</b> (
              {b.pod_seconds.toLocaleString("en-GB")} → {s.pod_seconds.toLocaleString("en-GB")} pod-seconds).
            </p>
          );
        })}

      <p className="verdict" style={{ color: "var(--faint)", fontSize: "0.85rem" }}>
        A negative improvement is a real result, reported rather than dropped. Mean p99 across all
        runs in this scenario:{" "}
        {present.map((k) => `${ARMS[k].label} ${Math.round(means[k]!.p99)} ms`).join(" · ")}.
      </p>
    </>
  );
}
```

#### `web/app/page.tsx`

```tsx
import { Masthead, Footnote } from "@/components/Chrome";
import { ARMS, SCENARIOS, armMeans, bestArm, backtest, type ArmKey } from "@/lib/data";

/**
 * Overview — the answer, with no controls to operate first.
 *
 * Every figure below is COMPUTED from bench/replay*.json or outputs/results.csv
 * at build time. Nothing here is a typed-in string.
 */
export default function OverviewPage() {
  const ramp = SCENARIOS.find((s) => s.id === "ramp");
  const step = SCENARIOS.find((s) => s.id === "step");
  const head = ramp ?? step;

  if (!head) {
    return (
      <main className="wrap">
        <Masthead current="overview" />
        <h1>Predictive Autoscaling</h1>
        <p className="lede">No replay data found. Run <code>make web-data</code>.</p>
      </main>
    );
  }

  const means = armMeans(head.data);
  const win = bestArm(means);
  const nRuns = new Set(head.data.runs.map((r) => r.name[1])).size;

  const fmt0 = (n: number) => Math.round(n).toLocaleString("en-GB");

  return (
    <main className="wrap">
      <Masthead current="overview" />

      <h1>
        Capacity that arrives
        <br />
        before the traffic does.
      </h1>
      <p className="lede">
        Kubernetes&apos; HPA scales on CPU that has already risen, and a pod here takes 19 seconds
        to pass its readiness probe. This forecasts the request rate 60 seconds ahead and scales
        before the load lands — then A/B tests that against the stock HPA under byte-identical
        traffic.
      </p>

      <div style={{ height: "2.4rem" }} />

      <div style={{ display: "grid", gridTemplateColumns: "minmax(0,1.15fr) minmax(0,1fr)", gap: "2.5rem", alignItems: "start" }} className="overview-split">
        <div>
          <span className="eyebrow">Slowest 1% of responses — gradual ramp</span>
          {win && (
            <>
              <div className="hero">{win.latPct.toFixed(0)}%</div>
              <p className="hero-note">
                lower p99 than the stock HPA on identical traffic, for {win.costPct >= 0 ? "+" : ""}
                {win.costPct.toFixed(0)}% more pod-seconds. Both numbers are reported together on
                purpose: a latency win bought with unlimited compute is not a win.
              </p>
            </>
          )}
        </div>

        <div className="figblock">
          {win && (
            <>
              <div className="row">
                <span className="lbl">Response time, slowest 1%</span>
                <span>
                  <span className="statv" style={{ color: ARMS[win.arm].colour }}>
                    {fmt0(means.A!.p99)} → {fmt0(means[win.arm]!.p99)} ms
                  </span>
                  <span className="statn">stock HPA → forecast</span>
                </span>
              </div>
              <div className="row">
                <span className="lbl">Compute used</span>
                <span>
                  <span className="statv">
                    {fmt0(means.A!.pod_seconds)} → {fmt0(means[win.arm]!.pod_seconds)}
                  </span>
                  <span className="statn">pod-seconds over the 20-minute run</span>
                </span>
              </div>
            </>
          )}
          <div className="row">
            <span className="lbl">Forecast quality</span>
            <span>
              <span className="statv">{backtest.vsNaivePct.toFixed(1)}% lower cost</span>
              <span className="statn">
                than the naive forecast, over {backtest.rows[0].folds} backtest folds
              </span>
            </span>
          </div>
        </div>
      </div>

      <section className="sec">
        <h2>Two kinds of traffic</h2>
        <p>
          The same system, tested against an event it can anticipate and one it cannot. The second
          is the honest half.
        </p>
      </section>

      <div className="cardgrid">
        {[ramp, step].filter(Boolean).map((sc) => {
          const s = sc!;
          const m = armMeans(s.data);
          const present = (Object.keys(m) as ArmKey[]).sort();
          const w = bestArm(m);
          const isStep = s.id === "step";
          return (
            <div key={s.id} className="card" style={{ borderTop: `3px solid ${w ? ARMS[w.arm].colour : "var(--ink)"}` }}>
              <span className="eyebrow">{s.label}</span>
              <h3>{isStep ? "The forecast loses, then wins differently" : "The forecast wins"}</h3>
              <p>{s.blurb}</p>
              {isStep && m.B && m.A && m.C && (
                <p>
                  Forecasting alone was{" "}
                  <b style={{ color: ARMS.A.colour }}>
                    {((m.B.p99 / m.A.p99 - 1) * 100).toFixed(0)}% worse
                  </b>{" "}
                  than doing nothing — it withdrew pods while the spike was still running. Letting
                  it raise the HPA&apos;s <i>floor</i> instead fixed that: the forecast can add
                  capacity early but can never take it away.
                </p>
              )}
              <div className="cardfigs">
                {present.map((k) => (
                  <div key={k}>
                    <span className="eyebrow">{ARMS[k].label}</span>
                    <span className="statv" style={{ color: ARMS[k].colour, fontSize: "1.3rem", textAlign: "left" }}>
                      {fmt0(m[k]!.p99)} ms
                    </span>
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>

      <section className="sec">
        <h2>How it works</h2>
        <p>Four steps, every 30 seconds, with the reactive autoscaler still underneath.</p>
      </section>

      <div className="steps">
        {[
          ["01", "Measure", "Prometheus scrapes the app every 15 seconds. That interval is the resolution of everything downstream."],
          ["02", "Forecast", "A gradient-boosted model predicts the request rate 60 seconds ahead — the measured time for a pod to become useful."],
          ["03", "Convert", "Predicted rate ÷ 20 req/s per pod, the measured capacity of one replica, with 10% headroom."],
          ["04", "Apply", "Raise the autoscaler's floor. Capacity can arrive early, but only real CPU is allowed to take it away."],
        ].map(([n, title, body]) => (
          <div className="step" key={n}>
            <b>{n}</b>
            <h3>{title}</h3>
            <p>{body}</p>
          </div>
        ))}
      </div>

      <section className="sec">
        <h2>The forecast itself</h2>
        <p>
          Ranked by cost, not by error — under-provisioning is priced ten times worse than
          over-provisioning, because it costs users rather than pennies. Read from{" "}
          <code>{backtest.generatedFrom}</code>.
        </p>
      </section>

      <div className="chartbox">
        <div className="tablescroll">
          <table className="data">
            <caption className="visually-hidden">Backtest scoreboard, {backtest.rows.length} models averaged across folds</caption>
            <thead>
              <tr>
                <th scope="col">Model</th>
                <th scope="col">MAE</th>
                <th scope="col">RMSE</th>
                <th scope="col">Cost</th>
                <th scope="col">Folds</th>
              </tr>
            </thead>
            <tbody>
              {backtest.rows.map((r) => (
                <tr key={r.model}>
                  <td>
                    {r.model}
                    {r.model === backtest.champion ? " ★" : ""}
                  </td>
                  <td>{r.mae.toFixed(2)}</td>
                  <td>{r.rmse.toFixed(2)}</td>
                  <td>{Math.round(r.cost).toLocaleString("en-GB")}</td>
                  <td>{r.folds}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {backtest.meanModelMaeBetterPct !== null && backtest.meanModelCostWorsePct !== null && (
        <p className="verdict">
          The most instructive row pair: the mean-targeting <code>gbm</code> has{" "}
          <b>{backtest.meanModelMaeBetterPct.toFixed(0)}% better MAE</b> than the shipped{" "}
          <code>{backtest.champion}</code>, and costs{" "}
          <b>{backtest.meanModelCostWorsePct.toFixed(0)}% more</b> — because its errors fall on the
          expensive side. Choosing the metric mattered more than choosing the model.
        </p>
      )}

      <p className="verdict" style={{ marginTop: "1.4rem" }}>
        Averaged over {nRuns} runs per arm. Run <b>Benchmark replay</b> to scrub through any single
        run second by second.
      </p>

      <Footnote />
    </main>
  );
}
```

#### `web/app/benchmark/page.tsx`

```tsx
import { Masthead, Footnote } from "@/components/Chrome";
import BenchmarkView from "@/components/BenchmarkView";

export const metadata = {
  title: "Benchmark replay — Predictive Autoscaling",
  description: "Scrub second by second through a recorded 20-minute autoscaling benchmark run.",
};

export default function BenchmarkPage() {
  return (
    <main className="wrap">
      <Masthead current="benchmark" />
      <span className="eyebrow">Recorded benchmark &middot; 20 minutes</span>
      <h1 style={{ fontSize: "2rem" }}>Benchmark replay</h1>
      <p className="lede">
        Scrub through a run that already happened. Nothing is computed live — these are the
        recordings the published results came from.
      </p>
      <div style={{ height: "1.6rem" }} />
      <BenchmarkView />
      <Footnote />
    </main>
  );
}
```

---

# 3. EVERY CONSTANT AND TUNABLE

## 3.1 `src/config.py` — exhaustive

| Constant | Value | File | Line | Controls | How chosen |
|---|---|---|---:|---|---|
| `STEP_SECONDS` | `15` | `src/config.py` | 8 | The fundamental time step of the whole project: one row every 15 s. | Equals the Prometheus scrape interval — the finest resolution the data actually has. |
| `CYCLE_MINUTES` | `60` | `src/config.py` | 9 | Length of one simulated "day" in the training traffic. | Taken from `load/daily.js` `CYCLE_MIN`. |
| `WEEKEND_EVERY` | `7` | `src/config.py` | 10 | Every 7th cycle is the light "weekend". | Matches `load/daily.js`; forces the model to key off day-of-week, not just minute-of-day. |
| `STEPS_PER_CYCLE` | `240` (computed: `60 * 60 // 15`) | `src/config.py` | 12 | Rows in one cycle; used as the seasonal lag and a rolling window. | Derived, not chosen. |
| `STEPS_PER_WEEK` | `1680` (computed: `240 * 7`) | `src/config.py` | 13 | Rows in one "week"; the longest lag, and sizes the live fetch window. | Derived, not chosen. |
| `HORIZON_STEPS` | `4` (= 60 s) | `src/config.py` | 33 | How far ahead the model predicts. | **MEASURED, not guessed.** Pod created→Ready timed over three deletions: 19 s, 19 s, 18 s → average 18.7 s. Plus the 30 s controller interval: `ceil(48.7 / 15) = 4`. |
| `COST_UNDER` | `10.0` | `src/config.py` | 41 | Weight on under-prediction in the cost metric. | Business assumption: under-provisioning costs user-visible latency. |
| `COST_OVER` | `1.0` | `src/config.py` | 42 | Weight on over-prediction in the cost metric. | Over-provisioning costs only a little compute. |
| `QUANTILE` | `0.90` | `src/config.py` | 43 | The quantile the shipping model targets. | Stated in the file: the 10:1 cost ratio *is* a quantile loss at `q = 10/(10+1) = 0.909`, so `0.90` is that assumption expressed inside the model. |
| `N_FOLDS` | `4` | `src/config.py` | 46 | Number of rolling-origin backtest folds. | Not stated in repo. |
| `TEST_STEPS` | `480` (computed: `240 * 2`) | `src/config.py` | 47 | Rows in each fold's test window = exactly 2 cycles = 7,200 s. | Comment: "each fold tests on ~2 cycles of data". |
| `DATA_FILE` | `"data/traffic.parquet"` | `src/config.py` | 50 | Path to the recorded history. | — |
| `MODEL_FILE` | `"models/forecaster.joblib"` | `src/config.py` | 51 | Path to the trained bundle. | — |
| `RESULTS_FILE` | `"outputs/results.csv"` | `src/config.py` | 52 | Backtest scoreboard output path. | — |
| `PLOT_FILE` | `"outputs/forecast.png"` | `src/config.py` | 53 | Backtest plot output path. | — |

## 3.2 Every environment variable read by the code

| Variable | Default | File | Line | Controls |
|---|---|---|---:|---|
| `WORK_MS` | `"30"` → `30` | `app/main.py` | 19 | Milliseconds of CPU burned per `/work` request. |
| `STARTUP_DELAY_S` | `"15"` → `15.0` | `app/main.py` | 20 | Seconds the app sleeps before binding its port. This is what makes reactive scaling late. |
| `DEPLOYMENT` | `"traffic-app"` | `src/controller.py` | 41 | Which Deployment the controller scales. |
| `NAMESPACE` | `"default"` | `src/controller.py` | 42 | Namespace of that Deployment. |
| `INTERVAL_S` | `"30"` → `30` | `src/controller.py` | 43 | Seconds between controller decisions. |
| `CAPACITY_PER_POD` | `"20"` → `20.0` | `src/controller.py` | 59 | Requests/second one pod serves. **MEASURED** — see §3.4. |
| `HEADROOM` | `"1.1"` → `1.1` | `src/controller.py` | 61 | Safety multiplier applied to the forecast before converting to pods. |
| `MIN_PODS` | `"2"` → `2` | `src/controller.py` | 62 | Lower clamp on the pod count. |
| `MAX_PODS` | `"20"` → `20` | `src/controller.py` | 63 | Upper clamp on the pod count. |
| `MODE` | `"replicas"` | `src/controller.py` | 94 | `replicas` (forecast owns replica count) or `hpa-floor` (forecast sets `minReplicas`). |

### k6 script environment variables (`__ENV`)

| Variable | Default | File | Line | Controls |
|---|---|---|---:|---|
| `TARGET` | `'http://traffic-app/work'` | `load/daily.js` | 14 | URL under test. |
| `PEAK_RPS` | `80` | `load/daily.js` | 20 | Peak arrival rate of the diurnal cycle. |
| `TARGET` | `'http://traffic-app/work'` | `load/ramp.js` | 29 | URL under test. |
| `STEADY_RPS` (`LOW`) | `20` | `load/ramp.js` | 30 | Low end of the ramp. |
| `PEAK_RPS` (`HIGH`) | `80` | `load/ramp.js` | 31 | High end of the ramp. |
| `RUN_NAME` | `'unnamed'` | `load/ramp.js` | 69 | Label written into the emitted summary JSON. |
| `TARGET` | `'http://traffic-app/work'` | `load/benchmark.js` | 22 | URL under test. |
| `STEADY_RPS` | `20` | `load/benchmark.js` | 37 | Baseline arrival rate before/after the step. |
| `SPIKE_MULT` | `4` | `load/benchmark.js` | 38 | Step multiplier. `SPIKE = round(20 * 4) = 80`. |
| `RUN_NAME` | `'unnamed'` | `load/benchmark.js` | 91 | Label written into the emitted summary JSON. |
| `TARGET` | `'http://traffic-app/work'` | `load/capacity.js` | 23 | URL under test. |
| `STEPS` | `'4,8,12,16,20,24,28'` | `load/capacity.js` | 28 | Arrival rates stepped through to find the knee. |
| `STEP_SECONDS` | `45` | `load/capacity.js` | 29 | Seconds held at each step. |

## 3.3 Hardcoded magic numbers

### `src/controller.py`

| Value | Line | Meaning | Reason given in code |
|---|---:|---|---|
| `MAX_SCALE_DOWN_PER_CYCLE = 1` | 68 | Scale-down is capped at one pod per cycle; scale-up is uncapped. | "Deliberately asymmetric, and for the same reason the model targets q=0.90: being late to add capacity costs users, being slow to remove it costs pennies." |
| `0.99` in `recent_max * 0.99` | 198 | Decay applied to the running recent-maximum each cycle. | Not stated in repo. |
| `240` in `df["y"].tail(240)` | 198 | Window (in 15 s steps = 1 hour) used to compute the recent maximum. | Not stated in repo; equals `STEPS_PER_CYCLE`. |
| `10` in `pred > 10 * recent_max` | 209 | Sanity ceiling: forecasts above 10x the recent max are refused. | "An absurd forecast is more likely a broken feature row than a real 10x event. Hand control back to the HPA rather than launching twenty pods on a bad number." |

### `src/live.py`

| Value | Line | Meaning | Reason given in code |
|---|---:|---|---|
| `PROM_URL = "http://localhost:9090"` | 22 | Prometheus endpoint (the local end of `make forward-prom`). | Hardcoded. |
| `QUERY = 'sum(rate(http_requests_total{handler="/work"}[1m]))'` | 28 | The one signal the model consumes. | "Byte-for-byte the query collect.py records, so the model sees at serve time the identical signal it trained on." |
| `FETCH_STEPS = 1980` (computed `1680 + 240 + 60`) | 31 | How much history to fetch = longest lag + rolling window + margin for missed scrapes. | Sized so the longest lag is never empty at serve time when it was populated at train time. |
| `RECENT_STEPS = 120` | 58 | 30 minutes of unbroken recent history required before the model will answer. | "the longest NON-seasonal lag and rolling window build_table() uses ... if the last half hour is full of holes then lag_1, diff_1 and roll_mean_4 are all wrong, and those are the features the model leans on hardest (lag_1 alone carries 221k of gain)." |

### `src/features.py`

| Value | Line | Meaning | Reason given in code |
|---|---:|---|---|
| `LAGS = [1, 2, 3, 4, 6, 8, 12, 20, 40, 80, 120, 240, 1680]` | 33 | Every lag built, in 15 s steps. | Comment names the interesting ones: "4 = 1 minute ago, 240 = same point one cycle ('yesterday') ago, 1680 = same point one week ago". |
| `ROLL_WINDOWS = [4, 12, 40, 120, 240]` | 34 | Every rolling window. | Not individually justified. |
| `interpolate(limit=8)` | 65 | Gaps up to 8 steps (120 s) are bridged; longer outages stay NaN and are dropped. | "Inventing hours of traffic that never happened would teach the model a pattern that does not exist." |
| `min_periods=max(2, w // 4)` | 96 | Minimum observations before a rolling statistic is emitted. | Not stated in repo. |
| `y.shift(12)` / `/ 12.0` in `slope_12` | 106 | Slope over the last 12 steps (180 s). | "A rising ramp is exactly where reactive scaling fails, so give the model a direct view of 'is this climbing, and how fast'." |

### `src/models.py`

| Value | Line | Meaning |
|---|---:|---|
| `MovingAverage(window=12)` | 77–78, 158 | The moving-average baseline uses `roll_mean_12` (3 minutes). |
| `rounds = 400` | 95 | Boosting rounds (`num_boost_round` / `max_iter`). |
| `lr = 0.05` | 95 | Learning rate. |
| `min_pods = 2`, `max_pods = 20`, `headroom = 1.1` | 164–165 | Defaults of `replicas_needed()`. |

### `src/evaluate.py`

| Value | Line | Meaning | Reason given in code |
|---|---:|---|---|
| `min_train = max(2 * 240, 200) = 480` | 48 | Minimum training rows for a fold to be kept. | Folds are "trimmed automatically if the dataset is short, so a first run on a few hours of data still produces an honest (if smaller) evaluation instead of crashing." |
| `gap = C.HORIZON_STEPS = 4` | 30 | Rows left empty between train end and test start. | "at prediction time you genuinely would not yet know the outcome of the most recent H steps." |
| `0.8` | 61 | Fallback single-holdout split point when no full fold fits. | Fallback path only. |
| `1e-9` | 86 | sMAPE denominator guard. | "Plain MAPE explodes when the true value approaches zero, and traffic does hit near-zero in the quiet part of every cycle." |

### `collect.py`

| Value | Line | Meaning | Reason given in code |
|---|---:|---|---|
| `PROM_URL = "http://localhost:9090"` | 15 | Prometheus endpoint. | "local end of `make forward-prom`" |
| `QUERY` (identical to `live.py`) | 23 | The recorded signal. | "Only /work. The other endpoints are SELF-TRAFFIC: measured on this cluster, /healthz probes ran at 0.667 req/s and /metrics scrapes at 0.133 req/s with 2 pods — and both scale with replica count." |
| `EARLIEST = pd.Timestamp("2026-08-19T15:42:00Z")` | 43 | Hard cutoff; rows before this are dropped. | Everything earlier was recorded through a broken load path, and at 15:42Z `PEAK_RPS` dropped from 100 to 40 — a regime change, not noise. |
| `LOOKBACK = timedelta(hours=6)` | 47 | Overlapping re-read window each run. | Makes the collector idempotent. |
| `STEP_SECONDS = 15` | 48 | Query resolution. | "matches the scrape interval; finer would only interpolate" |

### `analyze.py` / `export_replay.py`

| Value | File | Line | Meaning |
|---|---|---:|---|
| `PROM = "http://localhost:9090"` | `analyze.py` | 31 | Prometheus endpoint. |
| `STEP = 20` | `analyze.py` | 32 | Seconds between samples when replaying a run window. |
| `C_A = "#eb6834"` | `analyze.py` | 34 | Chart colour, baseline/HPA arm. |
| `C_B = "#2a78d6"` | `analyze.py` | 35 | Chart colour, predictive arm. |
| `C_C = "#1f9d55"` | `analyze.py` | 36 | Chart colour, predictive + HPA floor arm. |
| `PROM = "http://localhost:9090"` | `export_replay.py` | 25 | Prometheus endpoint. |
| `STEP = 20` | `export_replay.py` | 26 | "matches what analyze.py uses, so the numbers agree" |
| `ARM_OF_PREFIX = {"A": "baseline", "B": "predictive", "C": "floor"}` | `export_replay.py` | 42 | Decodes a run-name prefix into an arm. Twin of `dashboard.ARMS`. |

### `dashboard.py`

| Value | Line | Meaning |
|---|---:|---|
| `PAPER = "#e8edee"` | 45 | Page background (drafting-grey stock). |
| `CARD = "#ffffff"` | 46 | Card fill. |
| `INK = "#101619"` | 47 | Primary text. Contrast 15.5:1 on the stock. |
| `MUTED = "#4d565a"` | 48 | Body copy. Contrast 6.4:1. |
| `FAINT = "#5d666a"` | 49 | Captions/labels. Contrast 5.0:1. |
| `RULE = "#c8d1d3"` | 50 | Hairlines only, never text. |
| `BASE = "#8c2f39"` | 55 | Arm A colour (stock HPA). |
| `PRED = "#15616d"` | 56 | Arm B colour (predictive). |
| `FLOOR = "#4a6b2a"` | 57 | Arm C colour (predictive + floor). |
| `RUN_SECONDS = 1200` | 59 | Every benchmark run is 20 minutes. |
| slider `step=20` | 678 | Playhead granularity, in seconds. |
| `capacity, headroom = 20.0, 1.1` | in `page_live()` | Live-page pod-count maths, duplicated from the controller's defaults. |

## 3.4 The two constants the project insists must be MEASURED

Quoted from `CLAUDE.md`:

> - `C.HORIZON_STEPS = 4` (60s). Pod created -> Ready timed over three deletions: 19s,
>   19s, 18s. Plus the 30s controller interval, rounded up: `ceil(48.7/15) = 4`.
> - `CAPACITY_PER_POD = 20` req/s (`src/controller.py`, overridable by env). `make
>   capacity` steps the arrival rate against a single replica: p95 is flat at 95ms
>   through 20 req/s and jumps to 381ms at 24, with CPU pinned at the 400m limit
>   throughout. The old default of 120 would have provisioned 6x too few pods for
>   every forecast, and no forecast metric would have shown it.

The capacity measurement table, quoted from `src/controller.py` lines 46–57:

```
    offered   served   p95     cpu
       12      12.0     95ms   0.35
       16      16.0     95ms   0.40   <- pinned at the 400m limit
       20      20.1     95ms   0.40   <- last flat step
       24      24.1    381ms   0.40   <- knee: 4x latency, no more throughput
```

---

# 4. THE DATA

## 4.1 `data/traffic.parquet` — measured properties

Obtained with a read-only `pandas.read_parquet`. The file was not modified.

| Property | Exact value |
|---|---|
| Row count | **12,281** |
| Columns | `ts`, `y` |
| `ts` dtype | `datetime64[us, UTC]` |
| `y` dtype | `float64` |
| First timestamp | `2026-08-19 15:42:00+00:00` |
| Last timestamp | `2026-08-21 18:56:45+00:00` |
| Total span | `2 days 03:14:45` = **51.2458 hours** |
| Sampling interval | **15 s** for 12,279 of 12,280 intervals |
| Non-15 s intervals | exactly **1**, of 300 s |
| `y` minimum | `0.000000` |
| `y` mean | `27.318801` |
| `y` median | `27.244265` |
| `y` maximum | `88.999239` |
| `y` standard deviation | `18.803933` |
| NaN in `y` | **0** |
| NaN in `ts` | **0** |
| Duplicate timestamps | **0** |
| Time gaps (interval > 15 s) | **1** |
| Gap location | `2026-08-21 18:33:00+00:00` → `2026-08-21 18:38:00+00:00` (300 s) |
| Missing seconds inside gaps | **285** (300 s gap minus the 15 s that would be normal) |
| Rows expected if perfectly gapless | **12,300** |
| Coverage | **99.846 %** |

Note: `CLAUDE.md` claims "12,281 rows, 51h, 100% coverage". The row count and span match;
**"100% coverage" is not exactly right** — actual coverage is 99.846 %, with one 300 s gap
(19 rows missing). Flagged again in §16.

## 4.2 How the data was generated

1. `load/daily.js` runs **inside the cluster** as Deployment `k6-load`
   (`k8s/load/k6.yaml`), sending traffic to `http://traffic-app/work`.
2. `app/main.py` exposes `http_requests_total` via `prometheus_fastapi_instrumentator`.
3. Prometheus scrapes the app every **15 s** (configured by `k8s/servicemonitor.yaml`).
4. `collect.py` queries Prometheus through `make forward-prom` and appends to the parquet.

The recorded quantity is the result of this PromQL, identical in `collect.py` (line 23)
and `src/live.py` (line 28):

```promql
sum(rate(http_requests_total{handler="/work"}[1m]))
```

## 4.3 Exact cutoff and filter rules in `collect.py`

| Rule | Line | Code | Effect |
|---|---:|---|---|
| Endpoint filter | 23 | `handler="/work"` inside the query | Excludes `/healthz` and `/metrics`. Measured self-traffic: **0.667 req/s** (`/healthz`) and **0.133 req/s** (`/metrics`) with 2 pods, both scaling with replica count. |
| Hard time cutoff | 43 | `EARLIEST = pd.Timestamp("2026-08-19T15:42:00Z")` | Every row before this instant is dropped. |
| Cutoff applied | 84 | `return df[df["ts"] >= EARLIEST].dropna()` | Filter + drop any NaN row. |
| Overlapping re-read | 47 | `LOOKBACK = timedelta(hours=6)` | Each run re-queries the last 6 hours and merges on timestamp, making the collector idempotent. |
| Query resolution | 48–49 | `STEP_SECONDS = 15`; `STEP = "15s"` | Matches the scrape interval. |

Two reasons the cutoff exists, quoted from `collect.py`:

> Anything before this instant was recorded through a BROKEN load path and must
> never reach the model. Until 2026-08-19 the load generator ran on the Mac
> behind `kubectl port-forward`, which pins every request to a single pod, so
> the recorded rate was one pod's ceiling rather than real demand — and while
> the forward was down, macOS AirPlay answered on port 5000 with instant 403s,
> recording an hour of silence as if traffic had stopped.
>
> Moved forward a second time at 15:42Z, when PEAK_RPS dropped from 100 to 40.
> The amplitude change is a REGIME change, not noise: the same minute of the
> cycle meant 55.7 req/s on average before and 32.0 after. A model trained
> across it learns that identical clock features predict two different answers,
> which shows up as irreducible error and makes the backtest understate the
> model rather than overstate it.

A cutoff is used rather than deleting rows because every run re-reads a 6 h window, so
deleted rows would immediately return from Prometheus.

## 4.4 Other data files

### `models/forecaster.joblib` — the trained bundle

Loaded read-only with `sys.path.insert(0, "src")` so `import models` resolves to
`src/models.py`. Exact contents:

| Key | Value |
|---|---|
| `model` | `GBM` instance, `name='gbm_q0.9'`, `quantile=0.9`, `rounds=400`, `lr=0.05` |
| `model.model` | `lightgbm.basic.Booster`, **400 trees**, **39 features** |
| `features` | list of **39** column names (exact order in §5.1) |
| `horizon` | `4` |
| `quantile` | `0.9` |
| `backend` | `'lightgbm'` |
| `trained_rows` | `12277` |
| `trained_through` | `'2026-08-21T18:55:45+00:00'` |

Booster params as stored in the file:

```python
{'objective': 'quantile', 'metric': 'quantile', 'learning_rate': 0.05,
 'num_leaves': 31, 'min_data_in_leaf': 30, 'feature_fraction': 0.85,
 'bagging_fraction': 0.85, 'bagging_freq': 1, 'lambda_l2': 1.0,
 'verbosity': -1, 'num_threads': 0, 'alpha': 0.9, 'num_iterations': 400}
```

Note `trained_rows = 12277` while the parquet has 12,281 rows: `features.usable()` drops
rows lacking `target`, `lag_1` or `roll_mean_12`. `12281 - 12277 = 4`, which equals
`HORIZON_STEPS` (the last 4 rows have no target yet).

### `models/retrain_history.jsonl` — verbatim (1 line)

```json
{"ts": "2026-08-30T06:46:52+00:00", "rows": 12277, "hours": 51.2, "candidate_cost": 4299.3, "champion_cost": 2003.0, "promoted": false, "reason": "-114.6% vs champion, below the 2% bar"}
```

Reading: one retrain was attempted on 2026-08-30. The candidate scored cost **4299.3**
against the champion's **2003.0** — **114.6% worse** — so it was **declined**. The live
model was never replaced.

### `bench/replay.json` and `bench/replay-step.json`

Frozen Prometheus windows for the UI. Structure (written by `export_replay.py`):

```
{ "step_seconds": 20,
  "scenario": "<one-line description>",
  "runs": [ { "name", "arm", "t":[...], "rate":[...], "pods":[...], "p99":[...],
              "decisions":[{t,now,pred,pods_now,pods_target,action}...],
              "summary": {p50,p95,p99,max,reqs,pod_seconds},
              "started_utc" }, ... ] }
```

| File | Runs | Scenario string |
|---|---|---|
| `bench/replay.json` | `A1r, A2r, A3r, B1r, B2r, B3r` (6) | `ramp 20 -> 80 req/s over 6 min, hold 4 min, ramp down` |
| `bench/replay-step.json` | `A1, A2, A3, B1, B2, B3, C1, C2, C3` (9) | `instant 4x step: 20 -> 80 req/s at minute 5, held 4 min` |

---

# 5. FEATURE ENGINEERING — EXHAUSTIVE

## 5.1 The exact, complete feature list

**Count: 39 features.** Read directly from `models/forecaster.joblib["features"]`, in the
exact order the model expects them:

```python
['lag_1', 'lag_2', 'lag_3', 'lag_4', 'lag_6', 'lag_8', 'lag_12', 'lag_20',
 'lag_40', 'lag_80', 'lag_120', 'lag_240', 'lag_1680',
 'roll_mean_4', 'roll_std_4', 'roll_max_4',
 'roll_mean_12', 'roll_std_12', 'roll_max_12',
 'roll_mean_40', 'roll_std_40', 'roll_max_40',
 'roll_mean_120', 'roll_std_120', 'roll_max_120',
 'roll_mean_240', 'roll_std_240', 'roll_max_240',
 'diff_1', 'diff_4', 'slope_12', 'accel', 'ratio_short_long', 'vs_prev_cycle',
 'f_pos_in_cycle', 'f_cycle_sin', 'f_cycle_cos', 'f_cycle_no', 'f_is_weekend']
```

Derivation of the count: 13 lags + (5 windows × 3 statistics = 15) + 6 shape features
+ 5 clock features = **39**.

Columns excluded from the feature list by `feature_columns()` (`src/features.py`):
`ts`, `y`, `target`.

## 5.2 Group 1 — Lags (13 features)

Every lag value, in 15-second steps:

| Feature | Lag (steps) | Lag (real time) |
|---|---:|---|
| `lag_1` | 1 | 15 s |
| `lag_2` | 2 | 30 s |
| `lag_3` | 3 | 45 s |
| `lag_4` | 4 | 1 minute |
| `lag_6` | 6 | 1 m 30 s |
| `lag_8` | 8 | 2 minutes |
| `lag_12` | 12 | 3 minutes |
| `lag_20` | 20 | 5 minutes |
| `lag_40` | 40 | 10 minutes |
| `lag_80` | 80 | 20 minutes |
| `lag_120` | 120 | 30 minutes |
| `lag_240` | 240 | 1 cycle — "yesterday" |
| `lag_1680` | 1680 | 7 cycles — "one week ago" |

Exact code (`src/features.py`):

```python
LAGS = [1, 2, 3, 4, 6, 8, 12, 20, 40, 80, 120, C.STEPS_PER_CYCLE, C.STEPS_PER_WEEK]
...
    for lag in LAGS:
        d[f"lag_{lag}"] = y.shift(lag)
```

Stated reason (comment above `LAGS`):

> Lags in 15-second steps. The interesting ones:
>   4   = 1 minute ago
>   240 = same point one cycle ("yesterday") ago
>   1680= same point one week ago

## 5.3 Group 2 — Rolling statistics (15 features)

Windows: `[4, 12, 40, 120, 240]`. Statistics per window: `mean`, `std`, `max`.

| Window (steps) | Real time | Features produced |
|---:|---|---|
| 4 | 1 minute | `roll_mean_4`, `roll_std_4`, `roll_max_4` |
| 12 | 3 minutes | `roll_mean_12`, `roll_std_12`, `roll_max_12` |
| 40 | 10 minutes | `roll_mean_40`, `roll_std_40`, `roll_max_40` |
| 120 | 30 minutes | `roll_mean_120`, `roll_std_120`, `roll_max_120` |
| 240 | 1 cycle (60 min) | `roll_mean_240`, `roll_std_240`, `roll_max_240` |

Exact code:

```python
ROLL_WINDOWS = [4, 12, 40, 120, C.STEPS_PER_CYCLE]
...
    for w in ROLL_WINDOWS:
        r = y.rolling(w, min_periods=max(2, w // 4))
        d[f"roll_mean_{w}"] = r.mean()
        d[f"roll_std_{w}"] = r.std()
        d[f"roll_max_{w}"] = r.max()
```

Legitimacy note from the module docstring:

> LAGS AND ROLLING STATS of y, taken at t or earlier. pandas' .rolling()
> includes the current row, which is fine: t is "now", you are allowed to
> know it.

## 5.4 Group 3 — Shape of the recent past (6 features)

Exact code:

```python
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
```

| Feature | Definition | Meaning |
|---|---|---|
| `diff_1` | `y - y.shift(1)` | Change over 15 s. |
| `diff_4` | `y - y.shift(4)` | Change over 1 minute. |
| `slope_12` | `(y - y.shift(12)) / 12.0` | Per-step slope over 3 minutes. |
| `accel` | `diff_1 - diff_1.shift(1)` | Second derivative — is the rise itself accelerating. |
| `ratio_short_long` | `roll_mean_4 / roll_mean_120` (0 → NaN) | Short-term average against 30-minute average. |
| `vs_prev_cycle` | `roll_mean_12 / y.shift(240)` (0 → NaN) | Now versus the same point one cycle ago. |

Stated reason: **"A rising ramp is exactly where reactive scaling fails, so give the model
a direct view of 'is this climbing, and how fast'."**

## 5.5 Group 4 — Clock features of the moment being PREDICTED (5 features)

Exact code:

```python
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
```

| Feature | Definition | Range |
|---|---|---|
| `f_pos_in_cycle` | `elapsed % 240` | 0–239 |
| `f_cycle_sin` | `sin(2π · pos / 240)` | −1 to 1 |
| `f_cycle_cos` | `cos(2π · pos / 240)` | −1 to 1 |
| `f_cycle_no` | `(elapsed // 240) % 7` | 0–6 |
| `f_is_weekend` | `1` if `f_cycle_no == 6` else `0` | 0 or 1 |

Why this is not leakage, from the module docstring:

> CLOCK FEATURES OF t+H. This looks like cheating and is not - you always
> know what time it will be in ninety seconds. Clocks are not a secret.

**Why the epoch anchor matters** (this is train/serve skew bug #2, quoted verbatim):

> Anchoring to d["ts"].iloc[0] looks equivalent and is not. Training passes
> the whole parquet, so row 0 is a fixed instant. Inference passes a window
> that slides with the wall clock, so row 0 moves - and the LAST row, the
> only one being predicted, always lands the same distance from it.
> Measured on 2026-08-24: f_pos_in_cycle read 142.0 on three consecutive
> live fetches, i.e. the model's "where are we in the day" input was a
> constant at serve time while it varied across the whole range in
> training. Same column name, different question.
>
> An epoch anchor is identical in both paths by construction.

And a pandas-version trap recorded in the same comment:

> Subtracting a fixed epoch and asking for total_seconds() is deliberate:
> .astype("int64") returns the underlying integer in whatever unit the dtype
> happens to use - pandas 3 builds these ranges as datetime64[us], so a
> nanosecond assumption silently floors every row in an hour to the same
> value. total_seconds() is unit-agnostic.

## 5.6 The target column — exact line

```python
    # ---- THE ANSWER ---------------------------------------------------------
    # Shift the y column UP by `horizon` rows: each row's target is the value
    # that really occurred `horizon` steps later. The past grades itself.
    d["target"] = y.shift(-horizon)
```

With `horizon = 4`, `target` is the request rate **60 seconds later**.

## 5.7 How train-time and serve-time share code

The governing rule, from the module docstring:

> To predict what happens at t+H, you may only use what was knowable at t.

| Mechanism | Where | What it guarantees |
|---|---|---|
| `features.build_table()` is the **single** feature definition | `src/features.py` | Training (`train_final.py`, `backtest.py`) and inference (`live.latest_feature_row`) call the same function. |
| `features.to_grid()` is called by **both** paths | `src/features.py` (called from `load_series()` and `live.latest_feature_row()`) | Reindexes onto a fixed 15 s grid, so positional lags mean real elapsed time in both paths. |
| Fetch window sized to the longest lag | `src/live.py` line 31: `FETCH_STEPS = C.STEPS_PER_WEEK + C.STEPS_PER_CYCLE + 60 = 1980` | `lag_1680` is populated at serve time, as it was at train time. |
| Clock features anchored to the Unix epoch | `src/features.py` | Identical in both paths **by construction**, not by convention. |
| Column order enforced at predict time | `src/predictor.py`, `src/controller.py`, `dashboard.py`: `row.reindex(columns=bundle["features"])` | Column-order skew is described in CLAUDE.md as "a silent, catastrophic failure mode". |
| The feature list travels **with** the model | `src/train_final.py` saves `{model, features, horizon, ...}` | A model cannot be fed columns in a different order or asked for a horizon it was not trained on. |
| Freshness guard | `src/live.py` lines 58, 79–81 | Requires 120 unbroken recent steps (30 min); otherwise returns `(None, nan)` and the controller holds. |

`to_grid()` docstring, verbatim, on why the shared call exists:

> CALLED BY BOTH PATHS - load_series() below for training, and
> live.latest_feature_row() for inference. That shared call is the whole
> point: Prometheus can miss a scrape (a restart, a sleeping laptop), which
> leaves holes, and every lag in build_table() is positional. Reindexing
> makes "lag 240" mean a true one cycle back rather than "240 rows back,
> whenever those happened to be".
>
> Skipping this on the serve side is not a small inaccuracy - it silently
> asks the model a different question than it was trained on. Observed on
> 2026-08-22: the live window held 120 rows spanning 7.8 hours (1872 rows if
> gapless, 13 gaps, the largest 79 minutes), and the controller forecast
> ~52 req/s while traffic was steady at ~36.

## 5.8 Row filtering — `usable()`

```python
def usable(table: pd.DataFrame) -> pd.DataFrame:
    """Drop rows that cannot be scored or have no recent history.

    Deliberately NOT dropping rows whose long lags are missing: with only a
    few hours collected, lag_1680 is empty everywhere, and requiring it would
    throw away the entire dataset. Both model backends treat NaN as "unknown"
    and route around it, so an absent long lag costs accuracy, not the run.
    """
    need = ["target", "lag_1", "roll_mean_12"]
    return table.dropna(subset=need).reset_index(drop=True)
```

Effect on the real dataset: 12,281 parquet rows → **12,277 usable rows** (the final 4 rows
have no `target`, because `horizon = 4`).

## 5.9 Gap handling in `to_grid()`

```python
    # Short gaps get bridged; long outages stay NaN and are dropped later.
    # Inventing hours of traffic that never happened would teach the model a
    # pattern that does not exist.
    d["y"] = d["y"].interpolate(limit=8).astype(float)
```

`limit=8` steps = **120 seconds**. The single real gap in the dataset is 300 s, which
exceeds this limit, so it is *not* fully bridged.

---

# 6. THE MODELS

## 6.1 The ladder

Defined in `src/models.py`:

```python
def ladder() -> list:
    """The models to compare, in increasing order of effort."""
    return [Naive(), SeasonalNaive(), MovingAverage(12), GBM(), GBM(quantile=C.QUANTILE)]
```

Resolved with `C.QUANTILE = 0.90`, the five models are:

| # | Name string | Class | Configuration |
|---|---|---|---|
| 1 | `naive` | `Naive` | none |
| 2 | `seasonal_naive` | `SeasonalNaive` | uses `lag_240` |
| 3 | `moving_avg_12` | `MovingAverage` | `window=12` |
| 4 | `gbm` | `GBM` | `quantile=None`, `rounds=400`, `lr=0.05` |
| 5 | `gbm_q0.9` | `GBM` | `quantile=0.90`, `rounds=400`, `lr=0.05` |

Why baselines ship with the model, from the module docstring:

> Starting with baselines is not a formality - a baseline is what makes a result
> mean something. "MAE of 14" is unreadable. "34% below the naive forecast any
> engineer would write in one line" is a claim.

### Baseline implementations (verbatim)

```python
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
```

## 6.2 LightGBM — every parameter, exact values

Backend selection (`src/models.py`):

```python
try:
    import lightgbm as lgb
    BACKEND = "lightgbm"
except Exception:                                  # pragma: no cover
    lgb = None
    from sklearn.ensemble import HistGradientBoostingRegressor
    BACKEND = "sklearn"
```

On this machine `BACKEND == "lightgbm"` (confirmed by `models/forecaster.joblib["backend"] == 'lightgbm'`).
CLAUDE.md notes the scikit-learn fallback is **untested** and sklearn is **not installed**.

### Constructor defaults

```python
    def __init__(self, quantile: float | None = None, name: str | None = None,
                 rounds: int = 400, lr: float = 0.05):
```

| Parameter | Value |
|---|---|
| `rounds` (→ `num_boost_round`) | **400** |
| `lr` (→ `learning_rate`) | **0.05** |
| `quantile` | `None` for `gbm`, `0.90` for `gbm_q0.9` |

### The exact LightGBM parameter dict

```python
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
```

Resolved for the **shipping model** (`gbm_q0.9`), and confirmed by reading the saved
Booster's own `params`:

| Parameter | Exact value |
|---|---|
| `objective` | `quantile` |
| `metric` | `quantile` |
| `alpha` | `0.9` |
| `learning_rate` | `0.05` |
| `num_leaves` | `31` |
| `min_data_in_leaf` | `30` |
| `feature_fraction` | `0.85` |
| `bagging_fraction` | `0.85` |
| `bagging_freq` | `1` |
| `lambda_l2` | `1.0` |
| `verbosity` | `-1` |
| `num_threads` | `0` (all cores) |
| `num_iterations` | `400` |
| Trees actually built | `400` |
| Features | `39` |

For the non-quantile `gbm`: `objective="regression_l1"`, `metric="l1"`, **no** `alpha`.

### The scikit-learn fallback parameters (untested on this machine)

```python
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
```

### Why quantile, verbatim from the docstring

> 5. GBM (quantile) - the same model aimed at a HIGH percentile instead of the
>    middle, and the one that matters here:
>
>    Forecasting the average expected load leaves you short roughly half the
>    time. For a service at peak, "short half the time" is an outage half the
>    time. Targeting the 90th percentile deliberately over-provisions a little,
>    trading a small amount of money for a large amount of safety - and it
>    puts that asymmetry inside the loss function rather than patching it
>    afterwards with a fudge factor.

### Feature importance method

```python
    def importance(self, top: int = 15) -> pd.DataFrame:
        if BACKEND != "lightgbm" or self.model is None:
            return pd.DataFrame(columns=["feature", "gain"])
        return (pd.DataFrame({"feature": self.model.feature_name(),
                              "gain": self.model.feature_importance("gain")})
                .sort_values("gain", ascending=False)
                .head(top).reset_index(drop=True))
```

## 6.3 `replicas_needed()` — forecast → pod count (verbatim)

```python
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
```

Formula with every production constant substituted:

```
pods = clip( ceil( predicted_rate * 1.1 / 20.0 ), 2, 20 )
```

Worked examples:

| `predicted_rate` | `rate * 1.1` | `/ 20` | `ceil` | after clamp |
|---:|---:|---:|---:|---:|
| 20 | 22.0 | 1.10 | 2 | **2** |
| 40 | 44.0 | 2.20 | 3 | **3** |
| 60 | 66.0 | 3.30 | 4 | **4** |
| 80 | 88.0 | 4.40 | 5 | **5** |
| 5 | 5.5 | 0.275 | 1 | **2** (min clamp) |
| 400 | 440.0 | 22.0 | 22 | **20** (max clamp) |

**Important:** `src/controller.py` does **not** call `replicas_needed()`. It re-implements
the same formula inline at line ~231:

```python
            want = int(np.clip(math.ceil(pred * HEADROOM / CAPACITY_PER_POD),
                               MIN_PODS, MAX_PODS))
```

`dashboard.py` re-implements it a third time in `page_live()`:

```python
    capacity, headroom = 20.0, 1.1
    want = max(2, min(20, int(-(-pred * headroom // capacity))))
```

All three are arithmetically equivalent, but the constants are duplicated in three places.
Flagged in §16.

---

# 7. EVALUATION METHOD

## 7.1 Design principle

From the `src/evaluate.py` docstring:

> The scoreboard. Written before the models, on purpose.
>
> If you build a model first and design the metric afterwards, you will - without
> meaning to - pick the metric that flatters what you already built. Fixing the
> rules while there is no result to protect is what makes every later number
> trustworthy.

## 7.2 Fold construction — exact code

```python
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
```

## 7.3 The ACTUAL folds for this dataset

Computed by calling `rolling_origin_folds(12277)` with the repo's own constants
(`N_FOLDS=4`, `TEST_STEPS=480`, `gap=4`, `min_train=480`):

| Fold | Train rows | Train size | Gap | Test rows | Test size |
|---|---|---:|---:|---|---:|
| 1 | `[0, 10353)` | 10,353 | 4 | `[10357, 10837)` | 480 |
| 2 | `[0, 10833)` | 10,833 | 4 | `[10837, 11317)` | 480 |
| 3 | `[0, 11313)` | 11,313 | 4 | `[11317, 11797)` | 480 |
| 4 | `[0, 11793)` | 11,793 | 4 | `[11797, 12277)` | 480 |

Each test window is 480 steps × 15 s = **7,200 s = 2 hours** (= 2 cycles).
The gap is 4 steps = **60 s**, exactly the forecast horizon.
Training is always **expanding** (always starts at row 0), never a sliding window.

## 7.4 The cost function — exact code and formula

```python
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
```

**Formula, with the repo's weights substituted:**

```
err   = y_true - y_pred
under = Σ max(err, 0)      # summed shortfall  (predicted too little)
over  = Σ max(-err, 0)     # summed excess     (predicted too much)

cost  = 10.0 × under  +  1.0 × over
```

Note these are **sums, not means**, so cost scales with the number of test rows.

Weights: `COST_UNDER = 10.0`, `COST_OVER = 1.0` (`src/config.py` lines 41–42).
The stated justification links the weight to the model's quantile:

> These are NOT equally bad, so the scoreboard prices
> them differently. This ratio is a business assumption you should be able to
> defend out loud - and note that it is exactly a quantile loss at
> q = 10/(10+1) = 0.909, which is why the headline model targets q=0.90.

## 7.5 Every metric computed

```python
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
```

| Metric | Definition | Units |
|---|---|---|
| `mae` | `mean(|y − p|)` | req/s |
| `rmse` | `sqrt(mean((y − p)²))` | req/s |
| `smape` | `mean(|y − p| / ((|y| + |p|)/2)) × 100`, skipping rows where the denominator ≤ `1e-9` | percent |
| `under` | `Σ max(y − p, 0)` — total shortfall | req/s summed |
| `over` | `Σ max(p − y, 0)` — total excess | req/s summed |
| `cost` | `10.0 × under + 1.0 × over` | weighted req/s |
| `n` | number of scored rows | count |

## 7.6 Ranking

```python
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
```

Models are averaged across folds and **sorted ascending by `cost`**.

---

# 8. ALL RESULTS — VERBATIM FROM FILES

## 8.1 `outputs/results.csv` (backtest scoreboard, sorted by cost ascending)

```csv
model,mae,mae_sd,rmse,smape,under,over,cost,folds
gbm_q0.9,4.772702619363198,0.34362552710271765,7.465207839663242,21.73354695360773,222.65689521479825,2068.2403620795367,4294.809314227519,4
gbm,2.236105890108155,0.24298087872922486,5.10207346455439,13.162160217308475,506.95672391242056,566.3741033394938,5635.941342463699,4
naive,4.650325263699145,0.18941832812229112,9.519487267432186,19.171245835836913,1095.7375936153192,1136.4185329602706,12093.794469113463,4
moving_avg_12,6.918919357839897,0.4498734515564022,12.116037436446598,28.868194174406586,1624.7975394784003,1696.2837522847503,17944.259147068755,4
seasonal_naive,9.872725872557508,1.154585726299212,16.58832642139679,39.28145833942172,2291.146788372721,2447.761630454883,25359.229514182087,4
```

Rendered:

| model | mae | mae_sd | rmse | smape | under | over | cost | folds |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `gbm_q0.9` | 4.772702619363198 | 0.34362552710271765 | 7.465207839663242 | 21.73354695360773 | 222.65689521479825 | 2068.2403620795367 | **4294.809314227519** | 4 |
| `gbm` | 2.236105890108155 | 0.24298087872922864 | 5.10207346455439 | 13.162160217308475 | 506.95672391242056 | 566.3741033394938 | 5635.941342463699 | 4 |
| `naive` | 4.650325263699145 | 0.18941832812229112 | 9.519487267432186 | 19.171245835836913 | 1095.7375936153192 | 1136.4185329602706 | 12093.794469113463 | 4 |
| `moving_avg_12` | 6.918919357839897 | 0.4498734515564022 | 12.116037436446598 | 28.868194174406586 | 1624.7975394784003 | 1696.2837522847503 | 17944.259147068755 | 4 |
| `seasonal_naive` | 9.872725872557508 | 1.154585726299212 | 16.58832642139679 | 39.28145833942172 | 2291.146788372721 | 2447.761630454883 | 25359.229514182087 | 4 |

**The headline finding, computed from this table:**
`gbm_q0.9` cost 4294.809 vs `naive` cost 12093.794 → `1 - 4294.809/12093.794 = 0.6449` =
**64.5 % lower cost than the naive baseline**.

**The most instructive row pair:** `gbm` has **lower MAE** (2.236 vs 4.773 — 53 % better)
but **higher cost** (5635.94 vs 4294.81 — 31.2 % worse), because it under-predicts far more
(`under` 506.96 vs 222.66) and under-prediction is priced 10×.

## 8.2 `outputs/results_by_fold.csv`

```csv
mae,rmse,smape,under,over,cost,n,model,fold
4.724417142752037,9.022721864117448,16.829328297375348,1210.8612793666478,1056.8589491543296,13165.471742820808,480,naive,1
9.62348728087427,16.453006652631213,31.12884356913563,2173.004441699548,2446.2694531201028,24176.31387011558,480,seasonal_naive,1
7.129306316264251,11.937241582726028,25.27666543451931,1792.1474992540116,1629.919532552829,19551.394525092946,480,moving_avg_12,1
1.9581719734956657,4.424599652183386,7.554839615777905,578.4362102988616,361.48633697905814,6145.8484399676745,480,gbm,1
4.469765467334025,6.745062765679774,14.80917341593434,253.07238462797028,1892.4150396923612,4423.138885972064,480,gbm_q0.9,1
4.376898696826392,10.076689348983383,17.46579781725801,973.1014240812868,1127.8099503953817,10858.82419120825,480,naive,2
11.469012714223906,18.101512077213297,50.40495192633203,1629.5807561052814,3875.5453467221932,20171.352907775006,480,seasonal_naive,2
6.668236637129209,13.141171790957092,27.09608817110517,1518.8368578936086,1681.9167279284122,16870.285306864498,480,moving_avg_12,2
2.4977319187351026,5.764927691570117,10.774554305116963,569.6889190761294,629.2224019167197,6326.111592678014,480,gbm,2
5.0295328264739,7.997301109886035,21.347375017878143,229.59754748751106,2184.5782092199606,4480.553684095072,480,gbm_q0.9,2
4.688677616830303,9.244590602053643,17.915902392751512,1125.3683973018815,1125.1968587766637,12378.880831795479,480,naive,3
9.689958075986032,16.099651570367847,35.788652992929606,3612.8832674790565,1038.296608994238,37167.1292837848,480,seasonal_naive,3
6.439446385595853,10.964687246642253,25.481065035174076,1546.01735158668,1544.9169134993297,17005.09042936613,480,moving_avg_12,3
2.119178444957421,4.990041000919922,8.760723483230667,468.0632369389334,549.1424166406284,5229.774786029962,480,gbm,3
5.10835800326967,8.01576916930916,18.428345499557867,190.1620627465576,2261.849778822884,4163.47040628846,480,gbm_q0.9,3
4.81130759838785,9.733947254574268,24.47395483596278,1073.619273711461,1235.808373514707,11972.001110629315,480,naive,4
8.708445419145823,15.699135385374802,39.80338486928962,1749.118688206997,2430.9351129829984,19922.121995052967,480,seasonal_naive,4
7.438688092370275,12.421049125461023,37.618958056827786,1642.1884491793012,1928.381835158431,18350.26632695144,480,moving_avg_12,4
2.369341223244431,5.228725513544138,25.55852346510837,411.63852933575765,725.645257821569,4842.030551179145,480,gbm,4
4.483154180375196,7.102698313778003,32.34929388106057,217.7955859971541,1934.1184205829404,4112.074280554481,480,gbm_q0.9,4
```

## 8.3 `outputs/feature_importance.csv` (LightGBM gain, top 15)

```csv
feature,gain
lag_1,250353.2744498253
roll_max_4,20956.783809661865
diff_1,19834.845848321915
roll_mean_4,17964.402180671692
lag_120,14036.507710933685
diff_4,12600.779591321945
ratio_short_long,9670.377799630165
lag_2,8471.650401830673
lag_40,7512.623836517334
lag_20,6749.380881071091
lag_80,6631.387850761414
lag_1680,6575.20841050148
slope_12,5969.5240087509155
vs_prev_cycle,5361.411488294601
lag_240,5119.1664409041405
```

## 8.4 `results.md` (STEP scenario, three arms) — verbatim

```markdown
# A/B benchmark

Predictive: p99 467 ms -> 655 ms (-40% lower). Pod-seconds: 2993 -> 3080 (+3%).

Predictive + HPA floor: p99 467 ms -> 240 ms (49% lower). Pod-seconds: 2993 -> 4273 (+43%).

| arm | runs | p50 | p95 | **p99** | max | pod-seconds | failed |
|---|---|---|---|---|---|---|---|
| Baseline (HPA) | 3 | 50 ms | 281 ms | **467 ms** | 867 ms | 2993 | 0.00% |
| Predictive | 3 | 40 ms | 338 ms | **655 ms** | 1231 ms | 3080 | 0.00% |
| Predictive + HPA floor | 3 | 32 ms | 148 ms | **240 ms** | 559 ms | 4273 | 0.01% |

Individual runs:

| run | p99 | pod-seconds | dropped |
|---|---|---|---|
| A1 | 493 ms | 3080 | 0 |
| A2 | 540 ms | 2940 | 0 |
| A3 | 369 ms | 2960 | 0 |
| B1 | 522 ms | 3060 | 0 |
| B2 | 565 ms | 3120 | 0 |
| B3 | 879 ms | 3060 | 0 |
| C1 | 256 ms | 4140 | 0 |
| C2 | 238 ms | 4480 | 0 |
| C3 | 228 ms | 4200 | 0 |
```

## 8.5 `results-r.md` (RAMP scenario, two arms) — verbatim

```markdown
# A/B benchmark

p99 latency: baseline 479 ms -> predictive 183 ms (62% lower). Pod-seconds: 3053 -> 3907 (+28%).

| arm | runs | p50 | p95 | **p99** | max | pod-seconds | failed |
|---|---|---|---|---|---|---|---|
| Baseline (HPA) | 3 | 73 ms | 279 ms | **479 ms** | 1021 ms | 3053 | 0.00% |
| Predictive | 3 | 51 ms | 132 ms | **183 ms** | 385 ms | 3907 | 0.00% |

Individual runs:

| run | p99 | pod-seconds | dropped |
|---|---|---|---|
| A1r | 473 ms | 3040 | 0 |
| A2r | 561 ms | 3060 | 0 |
| A3r | 404 ms | 3060 | 0 |
| B1r | 175 ms | 4080 | 0 |
| B2r | 186 ms | 3800 | 0 |
| B3r | 188 ms | 3840 | 0 |
```

## 8.6 CONSOLIDATED TABLE OF ALL 15 BENCHMARK RUNS

Every metric below is read directly from the k6 summary JSON in `bench/`, and the
start/end epochs from the matching `.start` / `.end` files.

| File | Arm | Scenario | Run # | start epoch | end epoch | start UTC | dur (s) | p50 ms | p95 ms | p99 ms | max ms | avg ms | requests | req/s | failed % | dropped_iters | iterations | vus_max |
|---|---|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `A1` | Stock HPA (baseline) | Instant spike | 1 | 1787389864 | 1787391073 | 2026-08-22 09:11:04Z | 1209 | 42.44 | 295.70 | 493.10 | 995.56 | 88.53 | 38500 | 32.0278 | 0.0000 | 0 | 38500 | 100 |
| `A1r` | Stock HPA (baseline) | Gradual ramp | 1 | 1787549213 | 1787550421 | 2026-08-24 05:26:53Z | 1208 | 73.68 | 297.94 | 472.98 | 817.87 | 103.44 | 60000 | 49.9976 | 0.0000 | 0 | 60000 | 100 |
| `A2` | Stock HPA (baseline) | Instant spike | 2 | 1787391124 | 1787392333 | 2026-08-22 09:32:04Z | 1209 | 52.08 | 304.23 | 540.15 | 849.06 | 92.29 | 38500 | 32.0283 | 0.0000 | 0 | 38500 | 100 |
| `A2r` | Stock HPA (baseline) | Gradual ramp | 2 | 1787550694 | 1787551904 | 2026-08-24 05:51:34Z | 1210 | 71.72 | 275.59 | 561.07 | 1262.26 | 101.72 | 59999 | 49.9987 | 0.0000 | 0 | 59999 | 100 |
| `A3` | Stock HPA (baseline) | Instant spike | 3 | 1787392364 | 1787393574 | 2026-08-22 09:52:44Z | 1210 | 55.56 | 242.78 | 368.60 | 755.54 | 83.65 | 38499 | 32.0283 | 0.0000 | 0 | 38499 | 100 |
| `A3r` | Stock HPA (baseline) | Gradual ramp | 3 | 1787552841 | 1787554047 | 2026-08-24 06:27:21Z | 1206 | 73.95 | 263.40 | 403.63 | 983.53 | 98.28 | 60000 | 50.0017 | 0.0000 | 0 | 60000 | 100 |
| `B1` | Predictive (owns replicas) | Instant spike | 1 | 1787393691 | 1787394899 | 2026-08-22 10:14:51Z | 1208 | 43.87 | 261.63 | 521.59 | 1023.01 | 73.72 | 38500 | 32.0292 | 0.0026 | 0 | 38500 | 100 |
| `B1r` | Predictive (owns replicas) | Gradual ramp | 1 | 1787558251 | 1787559457 | 2026-08-24 07:57:31Z | 1206 | 50.39 | 124.76 | 175.21 | 381.17 | 59.18 | 60000 | 49.9981 | 0.0017 | 0 | 60000 | 100 |
| `B2` | Predictive (owns replicas) | Instant spike | 2 | 1787996682 | 1787997890 | 2026-08-29 09:44:42Z | 1208 | 38.82 | 288.86 | 565.45 | 998.20 | 74.09 | 38499 | 32.0279 | 0.0000 | 0 | 38499 | 100 |
| `B2r` | Predictive (owns replicas) | Gradual ramp | 2 | 1787559480 | 1787560687 | 2026-08-24 08:18:00Z | 1207 | 51.13 | 132.45 | 186.07 | 393.63 | 60.96 | 59999 | 49.9958 | 0.0000 | 0 | 59999 | 100 |
| `B3` | Predictive (owns replicas) | Instant spike | 3 | 1787997909 | 1787999116 | 2026-08-29 10:05:09Z | 1207 | 36.92 | 463.47 | 879.20 | 1671.06 | 93.85 | 38499 | 32.0282 | 0.0000 | 0 | 38499 | 100 |
| `B3r` | Predictive (owns replicas) | Gradual ramp | 3 | 1787560703 | 1787561909 | 2026-08-24 08:38:23Z | 1206 | 51.21 | 137.90 | 187.96 | 379.65 | 62.17 | 60000 | 50.0001 | 0.0017 | 0 | 60000 | 100 |
| `C1` | Predictive + HPA floor | Instant spike | 1 | 1788072469 | 1788073676 | 2026-08-30 06:47:49Z | 1207 | 31.17 | 153.22 | 255.51 | 624.86 | 56.82 | 38499 | 32.0298 | 0.0026 | 0 | 38499 | 100 |
| `C2` | Predictive + HPA floor | Instant spike | 2 | 1788073716 | 1788074923 | 2026-08-30 07:08:36Z | 1207 | 31.23 | 151.30 | 237.84 | 487.46 | 56.24 | 38500 | 32.0285 | 0.0260 | 0 | 38500 | 100 |
| `C3` | Predictive + HPA floor | Instant spike | 3 | 1788074946 | 1788076154 | 2026-08-30 07:29:06Z | 1208 | 32.99 | 139.35 | 227.58 | 564.76 | 54.81 | 38500 | 32.0307 | 0.0000 | 0 | 38500 | 100 |

### Pod-seconds per run (from bench/replay*.json summaries, reconstructed from Prometheus)

| Run | Arm | Scenario | p50 ms | p95 ms | p99 ms | max ms | requests | pod-seconds |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `A1r` | Stock HPA (baseline) | Gradual ramp | 74 | 298 | 473 | 818 | 60000 | 3040 |
| `A2r` | Stock HPA (baseline) | Gradual ramp | 72 | 276 | 561 | 1262 | 59999 | 3060 |
| `A3r` | Stock HPA (baseline) | Gradual ramp | 74 | 263 | 404 | 984 | 60000 | 3060 |
| `B1r` | Predictive (owns replicas) | Gradual ramp | 50 | 125 | 175 | 381 | 60000 | 4080 |
| `B2r` | Predictive (owns replicas) | Gradual ramp | 51 | 132 | 186 | 394 | 59999 | 3800 |
| `B3r` | Predictive (owns replicas) | Gradual ramp | 51 | 138 | 188 | 380 | 60000 | 3840 |
| `A1` | Stock HPA (baseline) | Instant spike | 42 | 296 | 493 | 996 | 38500 | 3080 |
| `A2` | Stock HPA (baseline) | Instant spike | 52 | 304 | 540 | 849 | 38500 | 2940 |
| `A3` | Stock HPA (baseline) | Instant spike | 56 | 243 | 369 | 756 | 38499 | 2960 |
| `B1` | Predictive (owns replicas) | Instant spike | 44 | 262 | 522 | 1023 | 38500 | 3060 |
| `B2` | Predictive (owns replicas) | Instant spike | 39 | 289 | 565 | 998 | 38499 | 3120 |
| `B3` | Predictive (owns replicas) | Instant spike | 37 | 463 | 879 | 1671 | 38499 | 3060 |
| `C1` | Predictive + HPA floor | Instant spike | 31 | 153 | 256 | 625 | 38499 | 4140 |
| `C2` | Predictive + HPA floor | Instant spike | 31 | 151 | 238 | 487 | 38500 | 4480 |
| `C3` | Predictive + HPA floor | Instant spike | 33 | 139 | 228 | 565 | 38500 | 4200 |

### Notes on the run table

- **All 15 runs report `dropped_iterations = 0`**, which is the repo's validity criterion.
  (`Makefile`: *"A benchmark run with `dropped_iterations > 0` is invalid — k6 quietly
  reduced the offered load exactly when the app was struggling."*)
- Failure rates are effectively zero: the highest is `C2` at **0.0260 %**.
- Every run is ~1,206–1,210 s (nominal 1,200 s = 20 minutes).
- Ramp runs served **60,000** requests (50.0 req/s mean); step runs served
  **38,499–38,500** (32.03 req/s mean). The difference is by design — the two k6 profiles
  offer different total load.
- `vus_max` is **100** in every run (the `preAllocatedVUs` value), meaning k6 never needed
  to scale beyond its pre-allocated pool in any accepted run.
- Pod-seconds are **not** in the k6 JSON. They are reconstructed by replaying each run's
  start/end window against Prometheus (`analyze.py`) and are stored in `bench/replay*.json`.

### Arm means (as published by `analyze.py`)

| Scenario | Arm | mean p50 | mean p95 | mean p99 | mean max | mean pod-seconds | failed |
|---|---|---:|---:|---:|---:|---:|---:|
| Ramp | Stock HPA | 73 ms | 279 ms | **479 ms** | 1021 ms | 3,053 | 0.00 % |
| Ramp | Predictive | 51 ms | 132 ms | **183 ms** | 385 ms | 3,907 | 0.00 % |
| Step | Stock HPA | 50 ms | 281 ms | **467 ms** | 867 ms | 2,993 | 0.00 % |
| Step | Predictive | 40 ms | 338 ms | **655 ms** | 1231 ms | 3,080 | 0.00 % |
| Step | Predictive + HPA floor | 32 ms | 148 ms | **240 ms** | 559 ms | 4,273 | 0.01 % |

Derived headline comparisons:

| Comparison | p99 change | pod-seconds change |
|---|---|---|
| Ramp: Predictive vs Stock HPA | 479 → 183 ms = **−62 %** | 3,053 → 3,907 = **+28 %** |
| Step: Predictive vs Stock HPA | 467 → 655 ms = **+40 % WORSE** | 2,993 → 3,080 = **+3 %** |
| Step: Predictive + floor vs Stock HPA | 467 → 240 ms = **−49 %** | 2,993 → 4,273 = **+43 %** |
| Step: Predictive + floor vs Predictive | 655 → 240 ms = **−63 %** | 3,080 → 4,273 = **+39 %** |

Run-to-run spread on the step scenario (a separate finding): Stock HPA 369–540 ms (171 ms
wide), Predictive 522–879 ms (357 ms wide), Predictive + floor 228–256 ms (**28 ms wide**).

## 8.7 `bench/discarded/` — every discarded run and the stated reason

Files present: `A1.json`, `A1.start`, `A1.end`, `A1-4x-on-30.json`, `README.md`.

| File | run label | p50 | p95 | p99 | max | requests | dropped_iterations | failed |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `bench/discarded/A1.json` | `A1` | 80.60 ms | 13,981.61 ms | **19,776.79 ms** | 23,004.94 ms | 53,536 | **4,213** | 0.1476 % |
| `bench/discarded/A1-4x-on-30.json` | `A1` | 74.16 ms | 14,187.98 ms | **15,646.89 ms** | 16,390.40 ms | 57,108 | **641** | 0.0000 % |

`bench/discarded/A1.start` = `1787388497` · `bench/discarded/A1.end` = `1787389705`
(duration 1,208 s).

`bench/discarded/README.md` verbatim:

```markdown
# Discarded runs

`A1-4x-on-30.json` — steady 30 req/s, spike to 120. p99 15,647ms, 641 dropped
iterations, HPA reached only 4 of the ~7 pods needed.

Not a rigged result, but the wrong experiment. Two reasons:

1. At 30 req/s on the 2-pod floor, average CPU was already 82% against a 90%
   HPA target. The baseline began the run at the edge of its own trigger.

2. Once a pod saturates its 400m limit, CPU utilisation reads 100% and cannot
   go higher — a pod at 3x overload is indistinguishable from one at 1.01x. The
   HPA can therefore only grow replicas by 100/90 = 1.11 per cycle, so a 4x step
   is beyond what it can track at all. The run measured that blindness rather
   than reaction timing.

Both are true findings about CPU-based autoscaling and worth a paragraph in the
README. They are not what this project set out to measure, which is whether
forecasting delivers capacity EARLIER than reacting to it.

Replaced by steady 20 req/s -> spike 80, where the HPA (which settles at
~16.8 req/s per pod, measured) and the controller (20 req/s per pod, measured)
both target 5 pods — so the only variable left is when those pods arrive.
```

## 8.8 `logs/decisions.csv`

| Property | Value |
|---|---|
| Total data rows | **975** (plus 1 header line = 976 lines in the file) |
| Columns | `ts`, `current_rate`, `predicted`, `pods_now`, `pods_target`, `action`, `reason` |
| First timestamp | `2026-08-22T06:55:39+00:00` |
| Last timestamp | `2026-08-30T07:49:01+00:00` |
| Date range | 8 days |

### Action counts (exhaustive)

| Action | Count | Share |
|---|---:|---:|
| `none` | 643 | 65.95 % |
| `hold` | 221 | 22.67 % |
| `scale_down` | 42 | 4.31 % |
| `scale_up` | 41 | 4.21 % |
| `floor_down` | 15 | 1.54 % |
| `floor_up` | 13 | 1.33 % |
| **Total** | **975** | 100 % |

`scale_up` / `scale_down` / `none` come from `MODE=replicas`;
`floor_up` / `floor_down` come from `MODE=hpa-floor`; `hold` is the refusal path in either.

### Distinct `reason` values with counts (exhaustive — all 14)

| Reason | Count |
|---|---:|
| `ok` | 624 |
| `ValueError: no data from Prometheus` | 220 |
| `floor 2->2` | 83 |
| `floor 5->5` | 11 |
| `floor 3->2` | 8 |
| `floor 2->3` | 6 |
| `floor 3->3` | 6 |
| `floor 4->5` | 4 |
| `floor 5->4` | 4 |
| `floor 4->3` | 3 |
| `floor 4->4` | 2 |
| `floor 2->4` | 2 |
| `prediction 30.9 > 10x recent max 2.0` | 1 |
| `floor 3->4` | 1 |

**Notable:** the 10x sanity guard fired exactly **once** in 975 decisions, and the
"no data from Prometheus" guard fired **220 times** (22.6 % of all cycles) — almost
always because the port-forward or the cluster was not running.

### 15 representative example rows

```csv
ts,current_rate,predicted,pods_now,pods_target,action,reason
2026-08-22T06:55:39+00:00,34.421,51.83,2,3,scale_up,ok
2026-08-22T06:59:09+00:00,35.911,54.663,3,4,scale_up,ok
2026-08-22T07:01:39+00:00,38.2,54.203,4,3,scale_down,ok
2026-08-22T10:16:24+00:00,19.455,29.813,3,2,scale_down,ok
2026-08-22T06:56:09+00:00,35.244,51.487,3,3,none,ok
2026-08-22T06:56:39+00:00,36.592,50.978,3,3,none,ok
2026-08-22T11:51:23+00:00,,,2,2,hold,ValueError: no data from Prometheus
2026-08-22T11:52:13+00:00,,,2,2,hold,ValueError: no data from Prometheus
2026-08-22T11:52:46+00:00,,,2,2,hold,ValueError: no data from Prometheus
2026-08-30T06:48:25+00:00,10.156,44.037,2,3,floor_up,floor 2->3
2026-08-30T06:50:25+00:00,18.425,37.845,2,3,floor_up,floor 2->3
2026-08-30T06:49:55+00:00,18.859,35.988,3,2,floor_down,floor 3->2
2026-08-30T06:51:25+00:00,20.272,35.291,3,2,floor_down,floor 3->2
2026-08-30T06:38:53+00:00,2.044,30.859,2,2,hold,prediction 30.9 > 10x recent max 2.0
```

## 8.9 Images in `outputs/`

| File | Size | What it plots |
|---|---:|---|
| `outputs/forecast.png` | 176 KB | Backtest output from `src/backtest.py`: actual request rate versus the model's forecast over the held-out fold(s), with the naive baseline for comparison. Colours are set in `backtest.py`: `C_ACTUAL = "#52514e"`, `C_MODEL = "#2a78d6"`, `C_BASE = "#eb6834"`. |
| `outputs/comparison.png` | 92 KB | A/B comparison for the **STEP** scenario, written by `analyze.py` (no `--suffix`). Two stacked panels sharing an x-axis: top = p99 latency over time (ms), bottom = pods ready (step plot). One line per arm; three arms present. Dashed vertical lines bracket the load event at minutes 5 and 9. |
| `outputs/comparison-r.png` | 100 KB | The same chart for the **RAMP** scenario (`analyze.py` default `--suffix r`), two arms, event brackets at minutes 4 and 14. |

`outputs/` is gitignored and regenerable: `python src/backtest.py` produces `forecast.png`;
`python analyze.py` produces the comparison charts.

---

# 9. THE CONTROL LOOP — STEP BY STEP

Traced through `src/controller.py` with every constant substituted.

## 9.1 What triggers it, and how often

- Started manually: `CAPACITY_PER_POD=20 python src/controller.py` (or `MODE=hpa-floor …`).
- Runs on the **laptop**, not in the cluster.
- Loop period: `INTERVAL_S = 30` seconds (`time.sleep(INTERVAL_S)` at the end of every
  branch, including every error path).
- There is no scheduler, no cron, no leader election. `Ctrl+C` stops it.
- Stopping it **does not revert anything**: `"Stopping the controller does not revert
  anything; pods stay where they are until the HPA or you move them."`

## 9.2 Startup checks (before the loop)

```python
    if MODE == "hpa-floor" and hpa_state(hpa_api) is None:
        sys.exit("MODE=hpa-floor needs the HPA installed, and it is not.\n"
                 "  kubectl apply -f k8s/hpa.yaml")
    if MODE == "replicas" and hpa_state(hpa_api) is not None:
        # Both would fight over the same replica count every cycle and the
        # benchmark would measure the argument rather than either policy.
        sys.exit("MODE=replicas needs the HPA GONE, and it is installed.\n"
                 "  kubectl delete -f k8s/hpa.yaml")
```

`load_bundle()` exits if `models/forecaster.joblib` is absent.

## 9.3 Step 1 — read live traffic

`live.fetch_recent()` (`src/live.py`):

| Item | Exact value |
|---|---|
| Prometheus URL | `http://localhost:9090` (the local end of `make forward-prom`) |
| Client | `prometheus_api_client.PrometheusConnect(url=..., disable_ssl=True)` |
| Call | `prom.custom_query_range(QUERY, start_time=start, end_time=end, step="15s")` |
| PromQL | `sum(rate(http_requests_total{handler="/work"}[1m]))` |
| `end` | `datetime.now(timezone.utc)` |
| `start` | `end - timedelta(seconds=FETCH_STEPS * 15)` |
| `FETCH_STEPS` | `1680 + 240 + 60 = 1980` |
| Window length | `1980 × 15 s = 29,700 s = 8 hours 15 minutes` |

Returned rows are reshaped:

```python
    df = pd.DataFrame(result[0]["values"], columns=["ts", "y"])
    df["ts"] = pd.to_datetime(df["ts"], unit="s", utc=True)
    df["y"] = pd.to_numeric(df["y"], errors="coerce")
    return df.dropna().reset_index(drop=True)
```

If Prometheus returns nothing, an **empty** `DataFrame(columns=["ts","y"])` is returned.

## 9.4 Step 2 — build one feature row

`live.latest_feature_row(df, horizon)`:

1. `grid = F.to_grid(df)` — reindex onto the fixed 15 s grid (the shared call).
2. `recent = grid.tail(120)` — the last 120 steps = **30 minutes**.
3. **Freshness guard:**
   ```python
       if len(recent) < RECENT_STEPS or recent["y"].isna().any():
           return None, float("nan")
   ```
4. `table = F.build_table(grid, horizon=horizon)` — the same function training uses.
5. `row = table.iloc[[-1]]` — the single most recent row, which has **no `target`**.
6. `current_rate = float(grid["y"].iloc[-1])`.

## 9.5 Step 3 — predict, with column order enforced

```python
            X = row.reindex(columns=feats)
            pred = float(model.predict(X)[0])
```

`feats` is `bundle["features"]` — the exact 39-name list saved at training time.
`reindex(columns=…)` reorders (and would insert NaN for any missing column), which is what
prevents column-order skew. CLAUDE.md: *"column order skew is a silent, catastrophic
failure mode, so never predict on a raw feature frame."*

## 9.6 Step 4 — safety guards, in order

Evaluated top to bottom; the first that matches wins, logs, sleeps 30 s and `continue`s.

| # | Exact condition | Action logged | What it does instead |
|---|---|---|---|
| 1 | `row is None or df.empty` | raises `ValueError("no data from Prometheus")`, caught by the outer `except` → `action="hold"`, `reason="ValueError: no data from Prometheus"` | Changes nothing. **Fired 220 times** in `logs/decisions.csv`. |
| 2 | `not np.isfinite(pred) or pred < 0` | `action="hold"`, `reason=f"prediction not usable ({pred})"` | Changes nothing. |
| 3 | `recent_max > 0 and pred > 10 * recent_max` | `action="hold"`, `reason=f"prediction {pred:.1f} > 10x recent max {recent_max:.1f}"` | Changes nothing. **Fired once**: `prediction 30.9 > 10x recent max 2.0`. |
| 4 | any other exception | `action="hold"`, `reason=f"{type(e).__name__}: {e}"` | Changes nothing. |

`recent_max` is maintained as a decaying running maximum:

```python
            recent_max = max(recent_max * 0.99, float(df["y"].tail(240).max()))
```

`df["y"].tail(240)` = the last 240 raw samples = **1 hour**. The `0.99` decay means an old
peak loses 1 % of its influence every 30 s cycle.

Rationale, verbatim:

> An absurd forecast is more likely a broken feature row than a
> real 10x event. Hand control back to the HPA rather than
> launching twenty pods on a bad number.

And the design principle behind having guards at all:

> The safety rules below are not decoration. A model can be wrong, and the
> difference between a demo and something worth showing an engineer is whether
> you planned for that. AWS runs predictive scaling ALONGSIDE reactive policies
> rather than replacing them, for exactly this reason - when this controller
> declines to act, the reactive HPA is the net underneath.

## 9.7 Step 5 — forecast → pod count

```python
            want = int(np.clip(math.ceil(pred * HEADROOM / CAPACITY_PER_POD),
                               MIN_PODS, MAX_PODS))
```

Fully substituted:

```
want = clip( ceil( pred * 1.1 / 20.0 ), 2, 20 )
```

## 9.8 Step 6 — apply, and the two modes

### `MODE=replicas` (the default)

```python
                if want < pods_now - MAX_SCALE_DOWN_PER_CYCLE:
                    # Damping. Without it a noisy forecast makes pods flap up and
                    # down every cycle, which looks broken and thrashes the app.
                    want = pods_now - MAX_SCALE_DOWN_PER_CYCLE
                    note = "damped"
                else:
                    note = "ok"

                if want == pods_now:
                    action, reason = "none", note
                else:
                    set_replicas(api, want)
                    action = "scale_up" if want > pods_now else "scale_down"
                    reason = note
```

- Scale-**down** is capped at **1 pod per 30 s cycle** (`MAX_SCALE_DOWN_PER_CYCLE = 1`).
- Scale-**up** is **uncapped** — it can jump from 2 to 20 in one cycle.
- Actions emitted: `scale_up`, `scale_down`, `none`. Reasons: `ok`, `damped`.

### `MODE=hpa-floor` (the recommended one)

```python
            if MODE == "hpa-floor":
                # No damping here. The floor may fall as fast as the forecast
                # likes, because lowering it cannot remove a pod — the HPA still
                # has to agree, and it will not while CPU is high. Damping the
                # floor would only delay the eventual scale-down for no benefit.
                floor, hmax = hpa_state(hpa_api)
                if want != floor:
                    set_hpa_floor(hpa_api, want, hmax)
                    action = "floor_up" if want > floor else "floor_down"
                else:
                    action = "none"
                reason = f"floor {floor}->{want}"
```

- **No damping at all** — the deliberate difference from `replicas` mode.
- Actions emitted: `floor_up`, `floor_down`, `none`. Reasons: `floor N->M`.

The `set_hpa_floor` helper:

```python
def set_hpa_floor(hpa_api, n: int, max_pods: int):
    """Raise or lower the HPA's minReplicas — the forecast's only lever.

    minReplicas must stay <= maxReplicas or the API rejects the patch outright,
    so the clamp is not defensive tidiness.

    Note what this does NOT do: lowering the floor does not remove pods. It only
    permits the HPA to remove them, and the HPA will decline while CPU is still
    high. That asymmetry is the entire point of this mode.
    """
    n = max(1, min(int(n), int(max_pods)))
    hpa_api.patch_namespaced_horizontal_pod_autoscaler(
        DEPLOYMENT, NAMESPACE, {"spec": {"minReplicas": n}}
    )
```

### Which mode is recommended, and why — verbatim from the source

> Measured on 2026-08-29, step scenario (instant 4x), 3 runs each: "replicas"
> scored p99 655ms against the plain HPA's 467ms — 40% WORSE. The pod traces
> show it is not losing on the way up (it reached 5 pods where the HPA managed
> 3) but on the way down: around minute 8 the forecast sees the spike ending and
> starts cutting, while the spike runs to minute 9, and it is back at MIN_PODS
> by minute 11 where the HPA held 3 until minute 14.
>
> Withdrawing capacity early costs more than adding it late, and a forecast has
> no more warning about an event's END than about its start. "hpa-floor" is the
> structural answer: never let the forecast remove what current load still
> needs. It is also how AWS and KEDA compose predictive with reactive scaling —
> alongside, not instead of.

`MODE=replicas` is kept, not deleted, because it is the arm the middle row of the results
table measures; removing it would make that published row unreproducible.

## 9.9 Step 7 — log the decision

```python
def log_row(**kw):
    LOG.parent.mkdir(exist_ok=True)
    new = not LOG.exists()
    with open(LOG, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "ts", "current_rate", "predicted", "pods_now", "pods_target",
            "action", "reason"])
        if new:
            w.writeheader()
        w.writerow(kw)
```

Appends one row to `logs/decisions.csv` every cycle, including on every guard path.

## 9.10 Kubernetes authentication and the scale API

```python
def k8s_api():
    # Loaded from ~/.kube/config because this runs on the laptop, not inside a
    # pod. In-cluster it would be load_incluster_config() plus a ServiceAccount.
    kube_config.load_kube_config()
    return client.AppsV1Api(), client.AutoscalingV2Api()
```

| Purpose | API | Exact call |
|---|---|---|
| Auth | — | `kubernetes.config.load_kube_config()` — reads `~/.kube/config` |
| Read replica count | `AppsV1Api` | `read_namespaced_deployment_scale("traffic-app", "default").spec.replicas` |
| Write replica count | `AppsV1Api` | `patch_namespaced_deployment_scale("traffic-app", "default", {"spec": {"replicas": n}})` |
| Read HPA bounds | `AutoscalingV2Api` | `read_namespaced_horizontal_pod_autoscaler("traffic-app", "default")` → `(spec.min_replicas or 1, spec.max_replicas)` |
| Write HPA floor | `AutoscalingV2Api` | `patch_namespaced_horizontal_pod_autoscaler("traffic-app", "default", {"spec": {"minReplicas": n}})` |

## 9.11 One full worked cycle (concrete numbers)

Using a real row from `logs/decisions.csv`-style values, `MODE=replicas`, `pods_now = 2`:

| Step | Value |
|---|---|
| 1. Read `pods_now` | `2` |
| 2. Query Prometheus | `sum(rate(http_requests_total{handler="/work"}[1m]))` over the last 29,700 s at 15 s step |
| 3. Grid + guard | 1,980 points reindexed; last 120 steps (30 min) all present → pass |
| 4. Build features | 1 row × 39 columns |
| 5. Reindex | `row.reindex(columns=bundle["features"])` |
| 6. Predict | `pred = 37.0` req/s (60 s ahead) |
| 7. `recent_max` check | `37.0 > 10 × recent_max`? No → pass |
| 8. Pod maths | `ceil(37.0 × 1.1 / 20.0) = ceil(2.035) = 3`; `clip(3, 2, 20) = 3` |
| 9. Damping | `3 < 2 - 1 = 1`? No → `note = "ok"` |
| 10. Apply | `3 != 2` → `patch_namespaced_deployment_scale(..., {"spec": {"replicas": 3}})` |
| 11. Log | `action="scale_up"`, `reason="ok"` |
| 12. Sleep | 30 s |

---

# 10. ARCHITECTURE MAP

## 10.1 Every component, where it runs, and its port

| # | Component | Runs where | Listens / connects on | Source |
|---|---|---|---|---|
| 1 | `traffic-app` pods | **Inside the kind cluster**, namespace `default` | Container port **8000** (named `http`) | `app/main.py`, image `traffic-app:v1` |
| 2 | `traffic-app` Service | Inside cluster (ClusterIP) | **Port 80** → targetPort `http` (8000) | `k8s/service.yaml` |
| 3 | `k6-load` Deployment | **Inside the cluster** | Outbound only → `http://traffic-app/work` | `k8s/load/k6.yaml`, runs `load/daily.js` |
| 4 | `k6-capacity` Job | Inside the cluster (one-off) | Outbound → `http://traffic-app/work` | `k8s/load/k6-capacity.yaml`, runs `load/capacity.js` |
| 5 | `k6-benchmark` Job | Inside the cluster (one per run) | Outbound → `http://traffic-app/work` | `k8s/load/k6-benchmark.yaml` |
| 6 | Prometheus | Inside cluster, namespace `monitoring` | **9090** (in-cluster); exposed to the laptop on **localhost:9090** by `make forward-prom` | Helm chart `monitoring-kube-prometheus-prometheus` |
| 7 | `kubectl port-forward` | **Laptop** | `localhost:9090` → cluster 9090 | `make forward-prom` |
| 8 | `collect.py` | **Laptop** | Connects to `http://localhost:9090` | `collect.py` |
| 9 | `src/controller.py` | **Laptop** | Reads `http://localhost:9090`; writes to the Kubernetes API via `~/.kube/config` | `src/controller.py` |
| 10 | `src/predictor.py` | **Laptop** | Reads `http://localhost:9090` only | `src/predictor.py` |
| 11 | ~~`dashboard.py` (Streamlit, localhost:8501)~~ | **DELETED 2026-09-07** | — | replaced by components 14/15 and by `src/predictor.py` |
| 12 | `analyze.py` / `export_replay.py` | **Laptop** | Reads `http://localhost:9090` | those files |
| 13 | Local dev app (`make run`) | **Laptop**, no cluster | **8000** (not 5000 — macOS AirPlay holds 5000) | `Makefile` `APP_PORT = 8000` |
| 14 | **Vercel CDN** | **Vercel edge network** (public internet) | **443 / HTTPS**, `https://predictive-autoscaling.vercel.app` | `web/` static export, deployed by `make web-deploy` |
| 15 | **A visitor's browser** | Anywhere | Fetches the static bundle from Vercel | — |

`dashboard.py` (Streamlit on :8501) was component 11 in the previous version of this
document. It no longer exists; components 14 and 15 replace it for the public pages, and
`src/predictor.py` (component 10) covers the live view locally.

The kind cluster is named **`autoscale`**; its control-plane container is
`autoscale-control-plane`. `imagePullPolicy: Never` means the image exists only in the kind
node's containerd store, put there by `kind load`.

## 10.2 Every arrow

| # | Source → Destination | Protocol | Data | Frequency |
|---|---|---|---|---|
| 1 | `k6-load` pod → `traffic-app` Service:80 | HTTP GET `/work` | Synthetic requests at a diurnal arrival rate | Continuous while scaled to 1 |
| 2 | Service:80 → pod:8000 | HTTP (kube-proxy) | Load-balanced **per TCP connection** | Per request |
| 3 | Prometheus → pod:8000 `/metrics` | HTTP GET | `http_requests_total`, histogram buckets | **Every 15 s** |
| 4 | kubelet → pod:8000 `/healthz` | HTTP GET | Readiness probe | Every 3 s (`periodSeconds: 3`) |
| 5 | `collect.py` → `localhost:9090/api/v1/query_range` | HTTP | 6-hour window at 15 s step | Manual, or every 10 min via `make collect` |
| 6 | `collect.py` → `data/traffic.parquet` | file write | Merged `[ts, y]` | Per run |
| 7 | `controller.py` → `localhost:9090` | HTTP | 8 h 15 min window at 15 s step | **Every 30 s** |
| 8 | `controller.py` → Kubernetes API | HTTPS (kubeconfig) | `patch_namespaced_deployment_scale` **or** `patch_namespaced_horizontal_pod_autoscaler` | Only when the target differs |
| 9 | `controller.py` → `logs/decisions.csv` | file append | One row per decision | Every 30 s |
| 10 | HPA → Kubernetes API | internal | Reads pod CPU from metrics-server, writes replica count | Every 15 s (HPA default) |
| 11 | `analyze.py` → `localhost:9090` | HTTP | Replays each run's start→end window at 20 s step | Manual |
| 12 | `export_replay.py` → `bench/replay*.json` | file write | Frozen series per run | Manual |
| 13 | `dashboard.py` → `bench/replay*.json` | file read | Replay page data | On page load (cached) |
| 14 | `dashboard.py` → `localhost:9090` | HTTP | Live page only | On refresh / every 15 s if toggled |
| 15 | `dashboard.py` → `models/forecaster.joblib` | file read | Live page prediction | Cached with `@st.cache_resource` |
| ~~16~~ | ~~Browser → `localhost:8501`~~ | — | **removed with the Streamlit app** | — |
| 16 | `web/scripts/build-data.mjs` → `web/public/data/*.json` | file write | Minified replay copies + derived backtest figures | On `make web-data`, manual |
| 17 | `make web-deploy` → Vercel API | HTTPS (CLI token, `~/.vercel`) | The `web/out/` static export | Manual |
| 18 | **Visitor's browser → Vercel CDN** | **HTTPS** | Pre-rendered HTML + JS + the JSON baked into the bundle | Per page view |

**There is no arrow from the deployed site to the cluster, to Prometheus, or to the
model — and that is the point.** Everything the site shows was frozen out of Prometheus by
`export_replay.py` and committed. The site would render identically with the cluster
deleted.

## 10.3 Kubernetes objects

| Kind | Name | Namespace | Key spec | Labels |
|---|---|---|---|---|
| Deployment | `traffic-app` | `default` | `replicas: 2`; image `traffic-app:v1`; `imagePullPolicy: Never`; container port 8000 named `http`; `requests.cpu = limits.cpu = 400m`; `requests.memory = limits.memory = 256Mi`; env `WORK_MS=30`, `STARTUP_DELAY_S=15`; readiness probe `GET /healthz` `initialDelaySeconds: 5`, `periodSeconds: 3`, `timeoutSeconds: 3`, `failureThreshold: 6`; **no liveness probe** | `app: traffic-app` |
| Service | `traffic-app` | `default` | ClusterIP, port **80** → targetPort `http` | selector `app: traffic-app` |
| ServiceMonitor | (see `k8s/servicemonitor.yaml`) | `default` | Endpoint references the Service port **by name** (`http`) | carries `release: monitoring` |
| HorizontalPodAutoscaler | `traffic-app` | `default` | `scaleTargetRef` → Deployment `traffic-app`; `minReplicas: 2`; `maxReplicas: 20`; metric `Resource/cpu`, `Utilization`, `averageUtilization: 90` | — |
| Deployment | `k6-load` | `default` | Runs `daily.js` from ConfigMap `k6-scripts`; scale 0/1 to stop/start | — |
| Job | `k6-capacity` | `default` | Runs `capacity.js` once | — |
| Job | `k6-benchmark` | `default` | Runs one benchmark; `RUN_NAME` and script name are `sed`-substituted by `make bench` | — |
| ConfigMap | `k6-scripts` | `default` | Built from `load/` by `kubectl create configmap k6-scripts --from-file=load/` | — |
| (Helm release) | `monitoring` | `monitoring` | kube-prometheus-stack: Prometheus, Grafana, operator, node-exporter, kube-state-metrics, metrics-server | — |

Relationships:
`Service.selector(app=traffic-app)` → `Deployment.template.labels(app=traffic-app)` → Pods.
`ServiceMonitor` → Service (by port **name**). `HPA.scaleTargetRef` → Deployment.
`controller.py` patches either the Deployment's scale subresource **or** the HPA's
`minReplicas`, never both.

**Critical structural note:** `k8s/load/` is a subdirectory **on purpose** —
`kubectl apply -f k8s/` is not recursive, so `make deploy` can never accidentally start a
load test.

## 10.4 Flow A — TRAINING / offline (traffic → saved model)

```
 1. make load-start
      -> scales Deployment k6-load to 1
      -> k6 runs load/daily.js inside the cluster
      -> HTTP GET http://traffic-app/work at a diurnal arrival rate
         (60-min cycles, 2-3 random spikes, every 7th cycle light)

 2. traffic-app pods serve /work (30 ms CPU burn each)
      -> prometheus_fastapi_instrumentator increments http_requests_total
      -> exposed on :8000/metrics

 3. Prometheus (namespace monitoring) scrapes :8000/metrics every 15 s
      (discovery via k8s/servicemonitor.yaml, port referenced BY NAME "http")

 4. make forward-prom   (laptop)
      -> kubectl port-forward -> localhost:9090

 5. python collect.py   (laptop, repeat over hours/days)
      -> PromQL: sum(rate(http_requests_total{handler="/work"}[1m]))
      -> window: last 6 h, step 15 s, snapped to a 15 s epoch boundary
      -> filter: ts >= EARLIEST (2026-08-19T15:42:00Z)
      -> merge on ts into data/traffic.parquet     [12,281 rows, 51.25 h]

 6. python src/backtest.py
      -> features.load_series() -> to_grid() -> build_table() -> usable()
         [12,277 usable rows, 39 features]
      -> evaluate.rolling_origin_folds(12277) -> 4 folds
      -> for each fold, for each of 5 models: fit, predict, score
      -> outputs/results.csv, outputs/results_by_fold.csv,
         outputs/feature_importance.csv, outputs/forecast.png

 7. python src/train_final.py
      -> refit gbm_q0.9 on ALL 12,277 usable rows
      -> joblib.dump({model, features, horizon, quantile, backend,
                      trained_rows, trained_through})
      -> models/forecaster.joblib

 8. python src/predictor.py        (verification, changes nothing)
      -> exercises the LIVE path against real Prometheus
      -> the only check that can catch train/serve skew
```

## 10.5 Flow B — LIVE / online (one scrape → one pod-count change)

```
 t=0     Prometheus scrapes traffic-app:8000/metrics
           -> http_requests_total updated in TSDB

 every 30 s, controller.py:
   1. pods_now = AppsV1Api.read_namespaced_deployment_scale("traffic-app","default")

   2. live.fetch_recent()
        GET localhost:9090 /api/v1/query_range
          query = sum(rate(http_requests_total{handler="/work"}[1m]))
          start = now - 29,700 s      (1980 steps x 15 s)
          end   = now
          step  = 15s
        -> DataFrame[ts, y]

   3. live.latest_feature_row(df, horizon=4)
        to_grid(df)                       # SHARED with training
        recent = grid.tail(120)           # 30 minutes
        GUARD: if len(recent) < 120 or recent.y has NaN -> return (None, nan)
        build_table(grid, horizon=4)      # SHARED with training
        row = table.iloc[[-1]]            # 1 row x 39 features, no target

   4. X = row.reindex(columns=bundle["features"])     # enforces column order
      pred = model.predict(X)[0]                      # req/s, 60 s ahead

   5. recent_max = max(recent_max * 0.99, df.y.tail(240).max())
      GUARD: not finite or < 0            -> hold
      GUARD: pred > 10 * recent_max       -> hold

   6. want = clip(ceil(pred * 1.1 / 20.0), 2, 20)

   7a. MODE=replicas:
         if want < pods_now - 1: want = pods_now - 1        # damped
         if want != pods_now:
           AppsV1Api.patch_namespaced_deployment_scale(
             "traffic-app","default",{"spec":{"replicas":want}})

   7b. MODE=hpa-floor:
         floor, hmax = HPA.spec.min_replicas, HPA.spec.max_replicas
         if want != floor:
           AutoscalingV2Api.patch_namespaced_horizontal_pod_autoscaler(
             "traffic-app","default",{"spec":{"minReplicas": clip(want,1,hmax)}})
         # the HPA then decides whether a pod actually appears/disappears

   8. append one row to logs/decisions.csv
   9. sleep 30 s

 Kubernetes side effect:
   Deployment scale change -> new Pod scheduled
   -> container starts, sleeps STARTUP_DELAY_S=15 s BEFORE binding :8000
   -> readiness probe GET /healthz passes
   -> Endpoints updated -> Service routes to it
   -> measured total: 19 s, 19 s, 18 s from creation to Ready
```

## 10.6 File dependency graph (imports)

```
src/config.py          (imports nothing from the project)
      ^
      |------------------------------------------------------------+
      |                    |                |            |         |
src/features.py    src/models.py   src/evaluate.py       |         |
      ^  ^                ^   ^            ^             |         |
      |  |                |   |            |             |         |
      |  +----------------+---+------------+             |         |
      |            src/backtest.py                       |         |
      |                                                  |         |
      +-- src/live.py  (imports config as C, features as F)        |
              ^   ^                                                |
              |   |                                                |
              |   +-- src/predictor.py   (config, live, joblib, numpy)
              |                                                    |
              +------ src/controller.py (config, live, joblib, numpy,
                                         kubernetes.client/config)
src/train_final.py     -> config, features, models, joblib
retrain.py             -> src/{config,features,models,evaluate}  (via sys.path)
dashboard.py           -> live (lazy, inside page_live only), joblib (lazy),
                          altair, pandas, streamlit
collect.py             -> pandas, prometheus_api_client        (NO src imports)
analyze.py             -> numpy, pandas, requests, matplotlib  (NO src imports)
export_replay.py       -> requests, pandas-free stdlib csv/json (NO src imports)
app/main.py            -> fastapi, prometheus_fastapi_instrumentator (isolated)
```

Import style note (from CLAUDE.md):

> Scripts in `src/` do `sys.path.insert(0, <src dir>)` and import each other flat (`import
> config as C`), while resolving data/model paths against the **repo root**. So run them as
> `python src/backtest.py` from the repo root — not `python -m src.backtest`, and not from
> inside `src/`.

---

# 11. THE EXPERIMENT DESIGN

## 11.1 Every arm

| Letter | Name | HPA installed? | `controller.py` running? | `MODE` | What sets the replica count |
|---|---|---|---|---|---|
| **A** | Stock HPA (baseline) | **YES** (`kubectl apply -f k8s/hpa.yaml`) | **NO** | n/a | The HPA alone, from CPU utilisation at a 90 % target. |
| **B** | Predictive (owns replicas) | **NO** (`kubectl delete -f k8s/hpa.yaml`) | **YES** | `replicas` | The forecast, directly, via `patch_namespaced_deployment_scale`. |
| **C** | Predictive + HPA floor | **YES** | **YES** | `hpa-floor` | The HPA, but the forecast raises/lowers its `minReplicas`. |

Enforced in code so the two can never run together:

```python
    if MODE == "hpa-floor" and hpa_state(hpa_api) is None:
        sys.exit("MODE=hpa-floor needs the HPA installed, and it is not.\n"
                 "  kubectl apply -f k8s/hpa.yaml")
    if MODE == "replicas" and hpa_state(hpa_api) is not None:
        # Both would fight over the same replica count every cycle and the
        # benchmark would measure the argument rather than either policy.
        sys.exit("MODE=replicas needs the HPA GONE, and it is installed.\n"
                 "  kubectl delete -f k8s/hpa.yaml")
```

And documented in `k8s/hpa.yaml`:

```
#   Baseline    kubectl apply -f k8s/hpa.yaml     (controller.py NOT running)
#   Predictive  kubectl delete -f k8s/hpa.yaml    (controller.py running)
#
# Both must never run at once — they would fight over the same replica count
# and the result would measure the argument, not either policy.
```

Arm **C** was only ever run on the **instant spike** scenario (runs `C1`, `C2`, `C3`).
There are no `C*r` (ramp) runs.

## 11.2 Scenario 1 — `load/ramp.js` (the predictable event)

| Property | Exact value |
|---|---|
| Executor | `ramping-arrival-rate` |
| `startRate` | `LOW` = 20 req/s |
| `timeUnit` | `1s` |
| `preAllocatedVUs` | `100` |
| `maxVUs` | `3000` |
| `noConnectionReuse` | `true` |
| `summaryTrendStats` | `['avg', 'p(50)', 'p(95)', 'p(99)', 'max']` |

Stages:

| # | Duration | Target | Effect |
|---|---|---:|---|
| 1 | `4m` | 20 | Settle at the low rate |
| 2 | `6m` | 80 | **The ramp** — interpolated 20 → 80 |
| 3 | `4m` | 80 | Hold the plateau |
| 4 | `6m` | 20 | Ramp back down |

**Total: 20 minutes.** Event brackets used by `analyze.py`: minutes **4 and 14**
(`--event 4,14`, the default).

## 11.3 Scenario 2 — `load/benchmark.js` (the unpredictable event)

| Property | Exact value |
|---|---|
| Executor | `ramping-arrival-rate` |
| `startRate` | `STEADY_RPS` = 20 req/s |
| `SPIKE` | `Math.round(20 × 4) = 80` req/s |
| `timeUnit` | `1s` |
| `preAllocatedVUs` | `100` |
| `maxVUs` | `3000` (raised from 800 after run A1 dropped 4,213 iterations) |
| `noConnectionReuse` | `true` |
| `summaryTrendStats` | `['avg', 'p(50)', 'p(95)', 'p(99)', 'max']` |

Stages:

| # | Duration | Target | Effect |
|---|---|---:|---|
| 1 | `5m` | 20 | Settle |
| 2 | `1s` | 80 | **The step** |
| 3 | `4m` | 80 | Hold the spike |
| 4 | `1s` | 20 | Release |
| 5 | `11m` | 20 | Recover / scale-down behaviour |

**Total: 20 minutes and 2 seconds.** Event brackets: minutes **5 and 9**
(`--event 5,9`).

Why a step and not a ramp, verbatim:

> The step at minute 5 is a step, not a ramp: reactive scaling is slowest when
> load arrives faster than pods can boot, and a gradual ramp would let the HPA
> keep up and hide the very lag this project exists to demonstrate.

Why 20 → 80 specifically, verbatim:

> Chosen so BOTH policies target the same pod count, leaving timing as the
> only variable. Measured on this cluster:
>
>   HPA at 90% of a 400m request settles at ~16.8 req/s per pod
>   the controller uses the measured 20 req/s per pod, x1.1 headroom
>
>   steady 20 req/s -> HPA 2 pods (the floor), controller 2 pods
>   spike  80 req/s -> HPA 5 pods,             controller ceil(80*1.1/20) = 5

## 11.4 Scenario 3 — `load/capacity.js` (not an arm; a measurement)

| Property | Exact value |
|---|---|
| Executor | `ramping-arrival-rate` |
| `STEPS` | `4, 8, 12, 16, 20, 24, 28` req/s |
| `STEP_SECONDS` | `45` |
| Stage construction | `STEPS.flatMap(r => [{duration:'0s',target:r},{duration:'45s',target:r}])` — `0s` makes each target a **step**, not a ramp |
| `preAllocatedVUs` | `20` |
| `maxVUs` | `300` |
| `noConnectionReuse` | `true` |
| `summaryTrendStats` | `['avg', 'p(95)', 'p(99)', 'max']` |
| Total duration | 7 steps × 45 s = **315 s** |

Run against **1 replica with the HPA deleted**. This is what produced
`CAPACITY_PER_POD = 20`.

## 11.5 The training-signal generator — `load/daily.js`

| Property | Exact value |
|---|---|
| Executor | `ramping-arrival-rate` |
| `startRate` | `Math.max(2, Math.round(PEAK_RPS × 0.12))` |
| `PEAK_RPS` | default `80` (was 100, then 40 during collection — see §12) |
| Cycle | `CYCLE_MIN = 60` minutes, one stage per minute |
| Spikes | `Math.floor(rand(2,4))` per cycle = 2 or 3, each 2–3x for 2–4 minutes |
| Weekend | every 7th cycle at reduced load |
| Clamp | `Math.min(v, Math.round(PEAK_RPS × 2.2))` — a spike the cluster cannot serve stops being a demand signal |
| Floor | `Math.max(2, …)` |
| `preAllocatedVUs` | `50` |
| `maxVUs` | `400` |
| `noConnectionReuse` | `true` |

## 11.6 Exact commands to run ONE benchmark for ONE arm

```bash
# 0. Prerequisite for every arm: the continuous training load MUST be off,
#    or both arms serve a second uncontrolled workload on top of the exam paper.
make load-stop

# --- Arm A (stock HPA baseline) ---
kubectl apply -f k8s/hpa.yaml          # HPA on
# controller.py must NOT be running
make bench RUN=A1  SCRIPT=benchmark.js # step scenario
make bench RUN=A1r SCRIPT=ramp.js      # ramp scenario

# --- Arm B (predictive owns replicas) ---
kubectl delete -f k8s/hpa.yaml         # HPA off
CAPACITY_PER_POD=20 MODE=replicas python src/controller.py    # in another terminal
make bench RUN=B1  SCRIPT=benchmark.js
make bench RUN=B1r SCRIPT=ramp.js

# --- Arm C (predictive + HPA floor) ---
kubectl apply -f k8s/hpa.yaml          # HPA back on
CAPACITY_PER_POD=20 MODE=hpa-floor python src/controller.py   # in another terminal
make bench RUN=C1 SCRIPT=benchmark.js
```

What `make bench` does, verbatim from the Makefile:

```makefile
bench:
	@test -n "$(RUN)" || (echo "usage: make bench RUN=A1 [SCRIPT=ramp.js]"; exit 1)
	@test "$$(kubectl get deploy k6-load -o jsonpath='{.spec.replicas}')" = "0" \
	  || (echo "ERROR: daily.js load is still running — run 'make load-stop' first"; exit 1)
	kubectl delete job k6-benchmark --ignore-not-found
	kubectl create configmap k6-scripts --from-file=load/ --dry-run=client -o yaml | kubectl apply -f -
	@mkdir -p bench
	@sed -e 's/PLACEHOLDER/$(RUN)/' -e 's/SCRIPTNAME/$(or $(SCRIPT),benchmark.js)/' \
	  k8s/load/k6-benchmark.yaml | kubectl apply -f -
	@echo "run $(RUN) started — 20 minutes"
	@date -u +%s > bench/$(RUN).start
	kubectl wait --for=condition=complete job/k6-benchmark --timeout=30m
	@kubectl logs job/k6-benchmark \
	  | sed -n '/===BENCH_JSON_START===/,/===BENCH_JSON_END===/p' \
	  | sed '1d;$$d' > bench/$(RUN).json
	@date -u +%s > bench/$(RUN).end
	@echo "wrote bench/$(RUN).json  (window $(RUN).start -> $(RUN).end)"
```

Note the built-in guard: the target **refuses to run** if `k6-load` is not scaled to 0.

Why the summary is emitted through stdout rather than a file:

> k6 runs in a pod, so a file written here would die with the pod. Emitting
> the JSON to stdout between markers lets `kubectl logs` carry it out intact,
> past the per-second progress lines.

## 11.7 Every deliberate fairness control

| # | Control | Where | Quoted reason |
|---|---|---|---|
| 1 | **Zero randomness in the benchmark scripts** | `load/benchmark.js` header | *"Zero randomness anywhere in this file - no rand(), no spikes at random minutes, no per-cycle variation. daily.js is deliberately unpredictable because a forecaster has to earn its keep against surprise; a BENCHMARK is the opposite. If the two arms faced different traffic, any difference in p99 would be unattributable, and running it three times each would measure the randomness rather than the policy."* |
| 2 | **Arrival rate, not VUs** | all benchmark scripts | *"With VUs, throughput is VUs/latency, so the arm that scales better serves MORE requests - and comparing p99 across arms that handled different request counts is not a comparison. A fixed arrival rate means both arms are offered identical work and only their latency can differ."* |
| 3 | **`noConnectionReuse: true`** | all k6 scripts | *"kube-proxy load balances at L4 — it picks a backend when a TCP connection is established, not per request — and k6 reuses keep-alive connections by default. Measured: with reuse on, a single VU's connection pinned 13.05 req/s onto one pod while two other Ready pods sat at 0.00 … This applies identically to both benchmark arms, so it cannot bias the comparison."* |
| 4 | **Both arms provision to the same steady-state pod count** | `k8s/deployment.yaml`, `k8s/hpa.yaml` | *"requests == limits == 400m ... 90 % target ... so ~25m of CPU per req/s. 360m therefore trips at ~12.4 req/s, and at a 40 req/s plateau the HPA settles on ~4 pods. The predictive controller lands on ceil(40 * 1.1 / 20) = 3. Close enough that the two arms hold comparable capacity at steady state, which is the whole point: the benchmark must compare REACTION TIMING, not provisioning generosity. At the old 60%-of-200m the HPA sat at ~7 pods for the same traffic and any latency win would have been explained by the extra capacity, not by the forecast."* |
| 5 | **Same replica bounds for both arms** | `k8s/hpa.yaml` (`minReplicas: 2`, `maxReplicas: 20`) vs `controller.py` (`MIN_PODS=2`, `MAX_PODS=20`) | *"Same bounds as the predictive controller's MIN_PODS / MAX_PODS, so neither arm gets to scale somewhere the other cannot follow."* |
| 6 | **Three runs per arm** | benchmark procedure | Stops one lucky run carrying the result. |
| 7 | **`dropped_iterations` must be 0** | `Makefile`, `analyze.py` | *"A run that dropped iterations offered LESS load than intended, at exactly the moment the app was struggling — it is not comparable."* |
| 8 | **The continuous `daily.js` load must be off** | `make bench` guard | *"The continuous daily.js load MUST be off (`make load-stop`) or both arms are serving a second, uncontrolled workload on top of the exam paper."* |
| 9 | **Both arms never run at once** | `controller.py` startup exits | *"they would fight over the same replica count and the result would measure the argument, not either policy."* |
| 10 | **Latency over time comes from the app's own histogram, not k6** | `analyze.py` | *"k6 only emits aggregates at the end of a run, and the shape over time is the whole point of the chart."* |
| 11 | **Run names encode arm + scenario** | `Makefile` comment | *"Run names should say which: A1s/B1s for step, A1r/B1r for ramp, or the two scenarios' results get averaged together."* |
| 12 | **HPA is a manifest, not an imperative command** | `k8s/hpa.yaml` | *"It is a manifest rather than a `kubectl autoscale` one-liner so the comparison is reproducible from the repo: an imperative command that lived only in someone's shell history is not a baseline anyone else can rerun."* |

## 11.8 How results are computed and compared (`analyze.py`)

1. **`load_run(name)`** reads three files: `bench/<name>.json` (k6 summary),
   `bench/<name>.start`, `bench/<name>.end`. Returns `None` if any is missing.
2. From the k6 JSON it takes `http_req_duration.values` → `p(50)`, `p(95)`, `p(99)`, `max`;
   `http_reqs.values.count`; `http_req_failed.values.rate × 100`;
   `dropped_iterations.values.count`.
3. It then **replays the run's window against Prometheus** at 20 s step for two series:
   ```python
    tp, pods = prom_range(
        'kube_deployment_status_replicas_available{deployment="traffic-app"}',
        start, end)
    tl, p99 = prom_range(
        'histogram_quantile(0.99, sum by (le) '
        '(rate(http_request_duration_seconds_bucket{handler="/work"}[1m])))',
        start, end)
   ```
4. **pod-seconds** = `float(np.nansum(pods) * STEP)` with `STEP = 20`.
   Rationale: *"Pod-seconds is not captured live: Prometheus already records the replica
   count and keeps 15 days, so each run's start/end epoch (written by `make bench`) is
   enough to reconstruct it afterwards."*
5. Arms are assembled from run-name prefixes; **A and B are required, C is optional**:
   ```python
    arms = {
        "Baseline (HPA)": [load_run(f"A{i}{suffix}") for i in (1, 2, 3)],
        "Predictive": [load_run(f"B{i}{suffix}") for i in (1, 2, 3)],
        "Predictive + HPA floor": [load_run(f"C{i}{suffix}") for i in (1, 2, 3)],
    }
   ```
6. Each arm's metrics are averaged with `np.mean` across its runs.
7. Every non-baseline arm is scored **against the baseline**, never against the arm before
   it: *"'49% better than the HPA' is the claim a reader can check, and chaining
   improvements arm-to-arm would let a bad middle arm flatter the last one."*
8. For the chart, runs are averaged onto a common elapsed-time grid by **interpolation**,
   not index-by-index: *"Runs differ by a few seconds in length, so they are interpolated
   onto one grid rather than averaged index-by-index — otherwise a run that started two
   samples late would shift the whole curve."*
9. Output: `results{-suffix}.md` and `outputs/comparison{-suffix}.png`.

Invocation:

| Command | Suffix | Runs read | Output |
|---|---|---|---|
| `python analyze.py` | `r` (default) | `A1r…B3r` | `results-r.md`, `outputs/comparison-r.png` |
| `python analyze.py --suffix '' --event 5,9` | `''` | `A1…C3` | `results.md`, `outputs/comparison.png` |

---

# 12. EVERY BUG, TRAP, FAILURE AND FIX

Sources: commit messages, code comments, docstrings, `bench/discarded/README.md`,
`CLAUDE.md` "Operational traps", and `.gitignore` comments. Every entry below is
evidenced in the repository.

---

### BUG 1 — Prometheus query window not grid-aligned (duplicate rows)

| | |
|---|---|
| **What happened** | Every `collect.py` run passed a raw `now()` as `end_time`. |
| **Symptom (exact)** | *"two runs a minute apart returned the same instants offset by a second. Nothing deduplicated: **327 rows became 658 with no new time covered**."* |
| **Root cause** | Prometheus aligns `query_range` output to the `start_time` it is given, not to an absolute clock. |
| **Fix** | Snap the window to a 15 s epoch boundary so repeated runs are byte-identical, which is what the merge already assumed. `collect.py`, commit `70607d5`. |
| **Lesson** | An idempotent collector must be idempotent *in Prometheus's frame of reference*, not the caller's. |

---

### BUG 2 — 100 % of the recorded signal was the app's own self-traffic

| | |
|---|---|
| **What happened** | The collector query counted every handler, not just `/work`. |
| **Symptom (exact)** | *"Measured on the cluster: **0.667 and 0.133 req/s** against **0.000** for /work -- **100% of the recorded signal was self-generated**, and all of it scales with replica count."* (0.667 = `/healthz` probes, 0.133 = `/metrics` scrapes) |
| **Root cause** | Readiness probes and Prometheus scrapes are HTTP requests to the same app, and both scale with the number of pods — a feedback loop where adding pods raises measured "demand". |
| **Fix** | `handler="/work"` added to the PromQL, in **both** `collect.py` (line 23) and `src/live.py` (line 28). Comment: *"src/live.py MUST use this identical query."* |
| **Lesson** | A controller trained on that data would read its own probes as demand. |

---

### BUG 3 — pandas ships no Parquet engine

| | |
|---|---|
| **What happened** | `collect.py` died on its final line after a successful collection run, 2026-08-19. |
| **Symptom** | Failure at `to_parquet`. |
| **Root cause** | *"pandas delegates to_parquet to pyarrow and ships neither"*. |
| **Fix** | Host `requirements.txt` added, pinning `pyarrow` (25.0.1 per CLAUDE.md). Commit `70607d5`. |
| **Lesson** | CLAUDE.md: *"If `data/traffic.parquet` cannot be written, check this before anything else."* |

---

### BUG 4 — `kubectl port-forward` pins every request to ONE pod

| | |
|---|---|
| **What happened** | Load was generated from the Mac through `kubectl port-forward svc/traffic-app`. |
| **Symptom (exact)** | *"Measured with 4 replicas Ready: **6.94 req/s on one pod, 0.00 on the other three**."* |
| **Root cause** | `port-forward` resolves the Service to a single pod and pins the connection to it. It also dies when that pod dies. |
| **Fix** | k6 moved **inside the cluster** as a Deployment (`k8s/load/k6.yaml`), reaching the ClusterIP directly. The `forward-app` Make target was **deleted entirely** (commit `aea1d86`). |
| **Lesson** | *"Adding pods cannot reduce latency if the pods you add never receive traffic, so the A/B benchmark would have found no difference between arms for a reason invisible in the results."* |

---

### BUG 5 — kube-proxy balances per TCP connection, not per request

| | |
|---|---|
| **What happened** | Even in-cluster, one k6 VU's keep-alive socket pinned traffic to one pod. |
| **Symptom (exact)** | *"one VU still pinned **13.05 req/s** onto a single pod"* while other Ready pods sat at **0.00**. |
| **Root cause** | kube-proxy load balances at L4 — it picks a backend when a TCP connection is established, not per request — and k6 reuses keep-alive connections by default. |
| **Fix** | `noConnectionReuse: true` in every k6 script. After the fix, distribution measured at **23.6 / 22.5 / 21.4 / 19.9 / 12.7 %** across 5 pods. |
| **Lesson** | *"A real service is reached by many independent clients; one load generator holding one socket is the artefact."* |

---

### BUG 6 — macOS AirPlay holds port 5000

| | |
|---|---|
| **What happened** | Whenever the port-forward dropped, macOS Control Center answered on port 5000. |
| **Symptom (exact)** | *"k6 got **403s in 2ms** instead of connection errors, spun to **12.5M "completed iterations"**, and reported **0 interrupted** while delivering nothing."* Also recorded *"an hour of silence as if traffic had stopped"* in the data. |
| **Root cause** | AirPlay Receiver binds 5000 and returns an instant 403, which k6 counts as a completed (fast) iteration. |
| **Fix** | Every port in the project moved to 8000. `Makefile`: `APP_PORT = 8000`. Commit `aea1d86`. |
| **Lesson** | A "healthy-looking" load test can be delivering nothing at all. |

---

### BUG 7 — closed-loop VUs made demand an output of the autoscaler

| | |
|---|---|
| **What happened** | `daily.js` originally used `ramping-vus`. |
| **Symptom** | Recorded "demand" was partly an output of the control loop. |
| **Root cause** | *"Closed-loop VUs make req/s = VUs / latency, and latency falls as pods are added -- the recorded demand would have been partly an output of the autoscaler, and the forecaster would have been learning its own control loop."* |
| **Fix** | Switched to `ramping-arrival-rate` in every script. Commit `be0478a`. |
| **Lesson** | Offered load must be independent of how well the system serves it. |

---

### BUG 8 — `CAPACITY_PER_POD` defaulted to 120 when the true value is 20

| | |
|---|---|
| **What happened** | The controller's capacity constant was a guess. |
| **Symptom** | **None visible.** *"no forecast metric would ever have shown it."* |
| **Root cause** | Never measured. Measured value: p95 flat at 95 ms through 20 req/s, jumping to 381 ms at 24, CPU pinned at the 400m limit throughout. |
| **Fix** | `CAPACITY_PER_POD` **120 → 20** (`src/controller.py` line 59). Commit `be0478a`. |
| **Lesson** | *"The old 120 would have provisioned **6x too few pods** for every forecast."* A wrong constant here makes every decision wrong in the same direction while the forecast stays perfectly accurate. |

---

### BUG 9 — forecast horizon was a guess (6 steps)

| | |
|---|---|
| **What happened** | `HORIZON_STEPS` was 6. |
| **Root cause** | Not measured against actual pod start-up. |
| **Fix** | Timed pod created→Ready over three deletions: **19 s, 19 s, 18 s** → 18.7 s average. Plus the 30 s controller interval: `ceil(48.7 / 15) = 4`. `HORIZON_STEPS` **6 → 4**. |
| **Lesson** | *"Forecasting further ahead than you can act on is wasted accuracy; forecasting less means capacity still arrives late. That is why this number is measured."* |

---

### BUG 10 — `requests.cpu` ≠ `limits.cpu` made the HPA scale on a meaningless number

| | |
|---|---|
| **What happened** | Deployment had `requests.cpu: 200m`, `limits.cpu: 400m`. |
| **Symptom (exact)** | *"**20 pods at 123m each, every one of them 31% utilised**, with the HPA reporting **58%/60%** and considering itself on target."* It added a pod every ~4.7 req/s while a pod can serve ~15–20. |
| **Root cause** | The HPA measures CPU as a percentage **of requests**; when requests and limits differ, that percentage is unrelated to real capacity. |
| **Fix** | `requests == limits == 400m` (`k8s/deployment.yaml`). Commit `99bdbbd`. Also gives the pod **Guaranteed QoS**, so it is the last thing evicted under node pressure. |
| **Lesson** | A benchmark comparing two arms that provision to different targets measures generosity, not timing. |

---

### BUG 11 — `PEAK_RPS = 100` pinned the HPA at its ceiling

| | |
|---|---|
| **What happened** | The baseline arm sat at `maxReplicas = 20` continuously. |
| **Symptom** | *"the baseline arm cannot demonstrate reactive lag if it is already at its ceiling before the spike arrives."* |
| **Fix** | `PEAK_RPS` **100 → 40**, keeping the whole dynamic range inside the 2–20 bounds for both arms. Commit `6484c3b`. |
| **Side effect** | This created BUG 12. |

---

### BUG 12 — the PEAK_RPS change was a regime change in the training data

| | |
|---|---|
| **What happened** | Data collected before and after the `PEAK_RPS` change was mixed. |
| **Symptom (exact)** | *"the same minute of the cycle meant **55.7 req/s on average before and 32.0 after**."* |
| **Root cause** | A model trained across the break learns that identical clock features predict two different answers. |
| **Fix** | `EARLIEST = pd.Timestamp("2026-08-19T15:42:00Z")` in `collect.py` (line 43), applied at line 84. |
| **Subtlety** | A cutoff is required rather than deleting rows: *"every run re-reads a 6h window, so deleted rows come straight back out of Prometheus."* |
| **Lesson** | *"which shows up as irreducible error and makes the backtest understate the model rather than overstate it."* |

---

### BUG 13 — TRAIN/SERVE SKEW #1: the missing grid reindex

| | |
|---|---|
| **What happened** | `live.py` fed raw Prometheus output into `build_table()` without the 15 s grid reindex that `load_series()` applies at training time. |
| **Symptom (exact)** | *"Observed on 2026-08-22: the live window held **120 rows spanning 7.8 hours** (1872 rows if gapless, **13 gaps, the largest 79 minutes**), and the controller forecast **~52 req/s while traffic was steady at ~36**."* Raised no error. |
| **Root cause** | Every lag in `build_table()` is **positional**. Without reindexing, "lag 240" means "240 rows back, whenever those happened to be". |
| **Fix** | `features.to_grid()` extracted and called from **both** paths. Commit `9466e86`. |
| **Lesson** | *"Skipping this on the serve side is not a small inaccuracy - it silently asks the model a different question than it was trained on."* |

---

### BUG 14 — TRAIN/SERVE SKEW #2: the frozen clock feature

| | |
|---|---|
| **What happened** | Clock features were anchored to the input frame's **first row**. |
| **Symptom (exact)** | *"Measured on 2026-08-24: **`f_pos_in_cycle` read 142.0 on three consecutive live fetches**, i.e. the model's 'where are we in the day' input was a constant at serve time while it varied across the whole range in training."* Forecasts ~45 % too high; no error raised. |
| **Root cause** | Training passes the whole parquet, so row 0 is a fixed instant. Inference passes a sliding window, so row 0 moves — and the last row (the only one predicted) always lands the same distance from it. |
| **Fix** | Anchor to the **Unix epoch**, *"identical in both paths by construction"*. `src/features.py`. |
| **Lesson** | *"Same column name, different question."* CLAUDE.md: *"The backtest cannot catch this class of bug: it only ever exercises the training path. `predictor.py` against live Prometheus is the check that can."* |

---

### BUG 15 — pandas 3 datetime unit assumption

| | |
|---|---|
| **What happened** | Latent trap noted while fixing BUG 14. |
| **Symptom** | *"a nanosecond assumption silently floors **every row in an hour** to the same value."* |
| **Root cause** | *".astype("int64") returns the underlying integer in whatever unit the dtype happens to use - pandas 3 builds these ranges as datetime64[us]"*. |
| **Fix** | Use `.dt.total_seconds()`, which is unit-agnostic. `src/features.py`. |
| **Lesson** | Verified: the parquet's `ts` dtype is indeed `datetime64[us, UTC]`. |

---

### BUG 16 — readiness probe cascade to ZERO available replicas

| | |
|---|---|
| **What happened** | Benchmark run A1 collapsed completely. |
| **Symptom (exact)** | *"the 4x step put **60 req/s on each of 2 pods that serve 20**, the busy-loop threadpool starved the event loop, /healthz missed its 1s deadline, and Kubernetes pulled the pod from the Service. That shifted its load onto the survivor, which then failed the same way — **available replicas hit ZERO mid-spike, p99 reached 19.8s**, and the HPA stalled at 3 pods because **NotReady pods report no CPU metrics to scale on**."* |
| **Root cause** | Kubernetes probe defaults (`timeoutSeconds: 1`, `failureThreshold: 3`) treat a **busy** pod as a **dead** pod. |
| **Fix** | `timeoutSeconds: 3`, `failureThreshold: 6` in `k8s/deployment.yaml` = ~18 s of sustained non-response before eviction. |
| **Lesson** | *"A PROBE MUST DETECT 'DEAD', NOT 'BUSY'."* |

---

### BUG 17 — k6 dropped iterations under collapse

| | |
|---|---|
| **What happened** | Run A1 with `maxVUs: 800`. |
| **Symptom (exact)** | *"latency hit 14s under collapse, so holding 120 req/s needed **~1700 concurrent VUs and k6 dropped 4,213 iterations**."* (`bench/discarded/A1.json` confirms `dropped_iterations = 4213`, p99 = 19,776.79 ms.) |
| **Root cause** | k6 silently drops iterations when it exhausts its VU pool. |
| **Fix** | `maxVUs` **800 → 3000** in `load/benchmark.js`. |
| **Lesson** | *"Dropped iterations silently REDUCE the offered load at exactly the moment the app is struggling, which flatters whichever arm is coping worse. A valid run must report dropped_iterations = 0."* All 15 accepted runs report 0. |

---

### BUG 18 — the whole 4x-on-30 experiment was the wrong experiment

| | |
|---|---|
| **What happened** | Steady 30 req/s spiking to 120. |
| **Symptom (exact)** | *"p99 **15,647 ms**, **641 dropped iterations**, HPA reached only 4 of the ~7 pods needed."* |
| **Root cause (two)** | (1) *"At 30 req/s on the 2-pod floor, average CPU was already **82% against a 90% HPA target**. The baseline began the run at the edge of its own trigger."* (2) *"Once a pod saturates its 400m limit, CPU utilisation reads 100% and cannot go higher — a pod at 3x overload is indistinguishable from one at 1.01x. The HPA can therefore only grow replicas by **100/90 = 1.11 per cycle**, so a 4x step is beyond what it can track at all."* |
| **Fix** | Replaced by steady 20 → spike 80, *"where the HPA (which settles at ~16.8 req/s per pod, measured) and the controller (20 req/s per pod, measured) both target 5 pods — so the only variable left is when those pods arrive."* Run moved to `bench/discarded/`. |
| **Lesson** | *"Both are true findings about CPU-based autoscaling and worth a paragraph in the README. They are not what this project set out to measure."* |

---

### BUG 19 — THE BIG ONE: predictive scaling LOST on the instant spike

| | |
|---|---|
| **What happened** | `MODE=replicas` scored **worse than doing nothing** on the step scenario. |
| **Symptom (exact)** | *"Measured on 2026-08-29, step scenario (instant 4x), 3 runs each: 'replicas' scored **p99 655ms against the plain HPA's 467ms — 40% WORSE**."* |
| **Root cause (diagnosed from pod traces, not guessed)** | *"it is not losing on the way up (it reached 5 pods where the HPA managed 3) but on the way down: **around minute 8 the forecast sees the spike ending and starts cutting, while the spike runs to minute 9, and it is back at MIN_PODS by minute 11 where the HPA held 3 until minute 14**."* |
| **Fix** | `MODE=hpa-floor` — the controller sets the HPA's `minReplicas` instead of the replica count. *"Raising the floor forces pods to appear; lowering it only PERMITS removal — the HPA still declines while CPU is high."* Commits `e2a6611`, `4e1e008`. |
| **Result** | 467 → **240 ms (−49 %)** for **+43 % compute**. Run spread collapsed from **357 ms wide to 28 ms wide**. |
| **Lesson** | *"Withdrawing capacity early costs more than adding it late, and a forecast has no more warning about an event's END than about its start."* Also: `MAX_SCALE_DOWN_PER_CYCLE=1` was **not enough damping** at a 30 s interval. |

---

### BUG 20 — the hpa-floor result existed only as a hand-typed table

| | |
|---|---|
| **What happened** | `analyze.py` hardcoded exactly two arms, so the C-arm result could not be regenerated. |
| **Symptom** | *"analyze.py took two arms as given, so the hpa-floor result existed only as a hand-typed table in README.md."* `results.md` still showed the old two-arm conclusion, contradicting README.md. |
| **Fix** | Optional third arm added; A and B required, C dropped if absent. Commit `be55ea5`. |
| **Lesson** | A published number that a script cannot reproduce is not a measurement. |

---

### BUG 21 — the dashboard "Play" button was dead

| | |
|---|---|
| **What happened** | Clicking Play advanced nothing. |
| **Root cause** | *"the slider had a key, so Streamlit restored it from its own state and ignored the value the button set."* |
| **Fix** | Removed `key=` from the slider and passed an explicit `value=`; the playhead is set via `st.session_state["t"]` and a rerun. Commit `be55ea5`, refined in `9c17bf4`. |

---

### BUG 22 — an angle bracket in the injected CSS silently deletes the whole stylesheet

| | |
|---|---|
| **What happened** | The Streamlit dashboard rendered completely unstyled. |
| **Symptom** | Every CSS rule stopped applying at once. `document.querySelectorAll('style')` showed the injected `<style>` element was **absent from the DOM entirely** — not a parse error. |
| **Root cause** | An opening angle bracket followed by a letter **anywhere** inside the injected stylesheet — including inside a CSS comment — makes Streamlit's sanitizer discard the entire style element. |
| **Fix** | Percent-encode SVG data URIs (`%3Csvg` not `<svg`) and never write a tag name in a CSS comment. `dashboard.py` `inject_style()` carries an explicit warning in its docstring. Commit `9c17bf4`. |
| **Lesson** | *"The failure is silent and total: every rule here stops applying at once and the app renders unstyled."* |

---

### BUG 23 — a blanket font-family rule breaks Material icon ligatures

| | |
|---|---|
| **What happened** | Expander chevrons rendered as the literal text `keyboard_arrow_right`. |
| **Root cause** | `.stApp span, .stApp div { font-family: ... }` also matched `span[data-testid="stIconMaterial"]`, whose glyphs are **ligatures** in the Material Symbols font. |
| **Fix** | Set the face once on `.stApp` and let it inherit; elements that declare their own family (icons, code) are then untouched. Commit `9c17bf4`. |

---

### BUG 24 — the Streamlit nav radio dot could not be hidden

| | |
|---|---|
| **What happened** | `label > div:first-child { display:none }` did not hide the radio circle. |
| **Root cause** | The 15×15 px dot sits **three divs deep**: `label > div > div > div:first-child`. The `<input>` lives inside a separate visually-hidden `<span>`. |
| **Fix** | Explicit deep selector; and `[data-selected="true"]` used for the active state instead of `:has(input:checked)`. Commit `9c17bf4`. |

---

### TRAP 25 — ServiceMonitor port must be referenced by NAME

| | |
|---|---|
| **Symptom** | *"A name no service port matches is **dropped silently** by the operator — no error, no failed target, the scrape just never happens."* |
| **Fix / rule** | `k8s/servicemonitor.yaml` refers to the Service port by name `"http"`, and `k8s/service.yaml` names it. Commit `532c77f`. |

---

### TRAP 26 — closing the laptop lid freezes the cluster

| | |
|---|---|
| **Symptom** | Cluster frozen mid-run; gaps in the collected history. |
| **Root cause** | *"Closing the laptop lid sleeps the Mac even on AC ('Clamshell Sleep')."* |
| **Mitigation** | None available: *"`caffeinate` does not prevent it."* CLAUDE.md lists it as an operational trap. |
| **Evidence in the data** | The single 300 s gap in `data/traffic.parquet`, and 220 `no data from Prometheus` holds in `logs/decisions.csv`. |

---

### TRAP 27 — `kubectl apply -f k8s/` is not recursive

| | |
|---|---|
| **Design decision** | `k8s/load/` is a **subdirectory on purpose**, so `make deploy` can never accidentally start a load test. |

---

### TRAP 28 — editing a load script without rebuilding the ConfigMap

| | |
|---|---|
| **Symptom** | The old script keeps running, **silently**. |
| **Rule** | *"`make load-start` rebuilds the ConfigMap from `load/` and does a rollout restart — editing a script without that leaves the old version running, silently."* |

---

### TRAP 29 — `packages.txt` comments break apt

| | |
|---|---|
| **What happened** | Streamlit Cloud deploy failed. |
| **Fix** | `packages.txt` dropped entirely. Commit `0a1670a`. |

---

### DESIGN TRAP 30 — sync vs async handler choice in the app

| | |
|---|---|
| **Rule** | `/work` is `def` (sync), `/healthz` is `async def`. |
| **Reason (verbatim)** | *"A busy-looping async handler would pin the event loop and the benchmark would measure event-loop starvation instead of pod capacity; a sync health probe would queue behind a saturated threadpool and get pods restarted mid-benchmark."* |

---

### DESIGN TRAP 31 — no liveness probe, deliberately

| | |
|---|---|
| **Reason** | Commit `952df4d`: *"No liveness probe on purpose: it would kill the container mid-boot."* (the app sleeps 15 s before binding its port) |

---

### FINDING 32 — the lowest-error model is the most expensive model

| | |
|---|---|
| **Observation** | `gbm` (mean-targeting): MAE **2.236**, cost **5635.94**. `gbm_q0.9`: MAE **4.773**, cost **4294.81**. |
| **Meaning** | Half the error, **31.2 % more cost**, because it is wrong in the expensive direction (`under` 506.96 vs 222.66, priced 10×). |
| **Lesson (verbatim)** | *"Watching a model win on cost while losing on MAE is the single most instructive moment in this whole pipeline."* |

---

### FINDING 33 — the one retrain attempt was correctly REJECTED

| | |
|---|---|
| **Evidence** | `models/retrain_history.jsonl`: `candidate_cost: 4299.3`, `champion_cost: 2003.0`, `promoted: false`, `reason: "-114.6% vs champion, below the 2% bar"`. |
| **Meaning** | The gate worked exactly as designed — a scheduled unguarded retrain would have shipped a model **114.6 % worse**. |
| **Reason the gate exists (verbatim)** | *"A scheduled retrain that always overwrites is a scheduled way to ship a worse model. Fresh data can be worse data — a stretch where the laptop slept, or where a benchmark run replaced the normal traffic pattern with a 20-minute square wave. Both happened during this project."* |

---

# 13. THE UI

Since 2026-09-07 the UI is split in two. There is no Streamlit.

| Surface | Where it runs | Source | Needs |
|---|---|---|---|
| **Overview** (`/`) | Vercel, static | `web/app/page.tsx` | nothing |
| **Benchmark replay** (`/benchmark`) | Vercel, static | `web/app/benchmark/page.tsx` + `web/components/BenchmarkView.tsx` | nothing |
| **Live forecast** | **Laptop only, terminal** | `src/predictor.py` | `make forward-prom` + `models/forecaster.joblib` |

**Production URL: https://predictive-autoscaling.vercel.app**

## 13.1 Why the live view is not deployed

It calls `live.fetch_recent()` against `http://localhost:9090` and
`bundle["model"].predict()` on an in-process LightGBM booster. Vercel is serverless: there
is no cluster to reach and nowhere to hold a 1.1 MB joblib model between requests. Stubbing
it with canned numbers would defeat its only purpose — it is the view that catches
train/serve skew, and a faked one cannot. `src/predictor.py` is the local equivalent and
was always the check `CLAUDE.md` named for that job.

## 13.2 Global chrome (both routes)

Rendered by `web/components/Chrome.tsx`.

| Element | Content | Source |
|---|---|---|
| Masthead | `Predictive Autoscaling for Kubernetes` / `A/B BENCHMARK · KIND CLUSTER · 3 RUNS PER ARM` | literal |
| Nav strip | `Overview`, `Benchmark replay` — real `<Link>`s with `aria-current="page"` | — |
| Spec strip | `pod start-up 19 s` · `one pod serves 20 req/s` · `horizon 60 s` · `history 51 h` · `vs naive forecast −64.5%` | first four literal; the last **computed** from `backtest.vsNaivePct` |
| Footnote | Provenance, plus an explicit statement that the site never contacts a cluster | literal |

The Streamlit version's `prometheus connected / offline` chip was **removed**: on a public
deployment it could only ever say "offline" and would read as breakage.

## 13.3 Route `/` — Overview

No controls. Every figure is computed at build time.

| Element | Value on the live site | Where it comes from |
|---|---|---|
| Headline | "Capacity that arrives before the traffic does." | literal |
| Hero number | **62%** | `bestArm(armMeans(ramp))` → `latPct` |
| Hero note | "+28% more pod-seconds" | same call → `costPct` |
| Figure row 1 | `479 → 183 ms` | `armMeans(ramp).A.p99` and `.B.p99` |
| Figure row 2 | `3,053 → 3,907` pod-seconds | `armMeans(ramp)` `.pod_seconds` |
| Figure row 3 | **`64.5% lower cost`** | **`backtest.vsNaivePct`** — was a hardcoded string in `dashboard.py` |
| Card: Gradual ramp | per-arm mean p99 | `armMeans(ramp)` |
| Card: Instant spike | per-arm mean p99 + "40% worse" | `armMeans(step)`, delta computed inline |
| Backtest table | all 5 models, MAE / RMSE / cost / folds | `backtest.rows`, from `outputs/results.csv` |
| Closing verdict | "53% better MAE … 31% more" cost | `backtest.meanModelMaeBetterPct` / `meanModelCostWorsePct` |
| "How it works" | four numbered steps | literal |

## 13.4 Route `/benchmark` — Benchmark replay

Client component. Data is statically imported, so there is no fetch, no loading state and
no layout shift.

| Control | Element | Options | Default | Effect |
|---|---|---|---|---|
| Scenario | `<button aria-pressed>` group | `Gradual ramp`, `Instant spike` — only scenarios whose file exists | `Gradual ramp` | Swaps the replay file; 2 arms vs 3 |
| Run | `<button aria-pressed>` group | `Run 1`, `Run 2`, `Run 3` | `Run 1` | Runs pair by the digit in the name |
| Play | `<button aria-pressed>` | on/off | off | Advances 20 s per 400 ms tick; **rewinds to 0 at the end**; disabled under `prefers-reduced-motion` |
| Playhead | `<input type="range">` | `0`–`1200`, `step=20` | **`1200`** (the finished run) | Everything redraws as of that second |

Per arm (2 columns on the ramp, 3 on the spike, 1 on a phone):

- **Pod gauge** — filled blocks out of `GAUGE_SLOTS = 8`; **empty slots stay visible** so
  headroom is legible. `role="img"` with an `aria-label` giving the count.
- **Three figures** — Traffic (req/s), Pods, Slowest 1% (ms), each read via `valueAt()`.
- **Model caption** — from `decisionAt()`: *"Model: now 34/s, expects 51/s in 60 s → wants
  3 pods · adding a pod now"*. The `· adding a pod now` suffix appears for `scale_up`, and
  `· raising the hpa's floor now` for `floor_up`. The baseline column says *"No forecast —
  this version only reacts to what already happened."*

Three charts, all arms overlaid, **drawn only up to the playhead**:
`Response time of the slowest 1% (ms)` (260 px), `Pods running` (190 px, step-after),
`Requests arriving per second` (190 px). The y-axis is scaled to the **whole run**, never to
what has been drawn, so scrubbing never rescales the panel. Dashed verticals bracket the
load event at **240 s / 840 s** (ramp) and **300 s / 540 s** (step), read off the k6 stage
lists in `load/ramp.js` and `load/benchmark.js`.

Verdict section: a table of p99 / p50 / pod-seconds per arm for the selected run, then one
sentence per non-baseline arm. **Pod-seconds appears in the same sentence as latency**, e.g.
*"Predictive — p99 63% lower than the stock HPA (473 ms → 175 ms), using +34% compute
(3,040 → 4,080 pod-seconds)."*

## 13.5 Colour, dash and typography

Ported verbatim from the deleted `dashboard.py` into `web/app/globals.css`.

| Token | Hex | Meaning |
|---|---|---|
| `--paper` | `#e8edee` | page ground (cool drafting stock) |
| `--card` | `#ffffff` | card fill |
| `--ink` | `#101619` | primary text, 15.5:1 |
| `--muted` | `#4d565a` | body copy, 6.4:1 |
| `--faint` | `#5d666a` | captions, 5.0:1 |
| `--rule` | `#c8d1d3` | hairlines only |
| `--arm-a` | `#8c2f39` wine | **Arm A — stock HPA** |
| `--arm-b` | `#15616d` teal | **Arm B — predictive owns replicas** |
| `--arm-c` | `#4a6b2a` moss | **Arm C — predictive + HPA floor** |

**Those three arm colours fail a colourblind-separation check on their own** (worst
deuteranopia ΔE ≈ 4.2 against a ≥8 target). Every series therefore carries three
independent keys: **colour**, a **stroke dash** (`solid` / `7 3` / `2 2`, held in
`ARMS[k].dashArray`), and a **direct end-of-line label**. Nothing on the site is encoded by
colour alone.

Fonts, self-hosted by `next/font` (no render-blocking request, no swap shift):
**Newsreader** for prose, **IBM Plex Sans** for UI, **IBM Plex Mono** for every figure.

## 13.6 Accessibility and responsiveness — measured

- Real `<button>` and `<input type="range">` elements; `:focus-visible` rings at
  2 px `#15616d`.
- Every chart is a `<figure>` with `role="img"` and an `aria-label` naming the metric, the
  window and the values at the playhead, plus a `<details>` **table of the underlying
  numbers**.
- At 390 px: **no horizontal body scroll** (`scrollWidth === clientWidth === 500`), arm
  columns collapse to 1, and charts scroll **inside their own container**.
- Lighthouse 12 CLI, desktop preset, against production: **Performance 100 / Accessibility
  100** on both routes; LCP 0.5 s, **CLS 0**, TBT 0 ms. Chrome DevTools audit adds Best
  Practices 100 and SEO 100 (54 passed, 0 failed).

## 13.7 Running it

```bash
make web-dev      # localhost:3000
make web-build    # static export -> web/out/
make web-deploy   # build, then `vercel deploy --prod` from web/
```


---

# 14. HOW TO RUN EVERYTHING

## 14.1 Every Makefile target

Header variables:

```makefile
APP_PORT  = 8000
PROM_PORT = 9090
VENV      ?= .venv
PY        := $(shell [ -x $(VENV)/bin/python ] && echo $(VENV)/bin/python || echo python)
STREAMLIT := $(shell [ -x $(VENV)/bin/streamlit ] && echo $(VENV)/bin/streamlit || echo streamlit)
```

`.PHONY: run build load deploy pods forward-prom load-start load-stop capacity collect bench ui retrain`

Actual line as of 2026-09-07:

```makefile
.PHONY: run build load deploy pods forward-prom \
        load-start load-stop capacity collect bench retrain \
        web-data web-dev web-build web-deploy
```

`ui` and the `STREAMLIT` interpreter probe were removed with `dashboard.py`.

| Target | Exact command(s) | What it does | Prerequisites |
|---|---|---|---|
| `run` | `STARTUP_DELAY_S=1 uvicorn app.main:app --reload --port 8000` | Local dev app, 1 s warm-up instead of 15 s, auto-reload | venv active; **no cluster needed** |
| `build` | `docker build -t traffic-app:v1 .` | Builds the image | Docker running |
| `load` | `kind load docker-image traffic-app:v1 --name autoscale` | Side-loads the image into the kind node (there is no registry) | `build` done; kind cluster `autoscale` exists |
| `deploy` | `kubectl apply -f k8s/` | Applies Deployment, Service, ServiceMonitor, HPA. **Not recursive** — does not touch `k8s/load/` | image side-loaded |
| `pods` | `kubectl get pods -w` | Watches the 0/1 → 1/1 readiness gap | cluster up |
| `forward-prom` | `kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus 9090:9090` | **The prerequisite for everything live.** Leave running. | Prometheus installed |
| `load-start` | `kubectl create configmap k6-scripts --from-file=load/ --dry-run=client -o yaml \| kubectl apply -f -`<br>`kubectl apply -f k8s/load/k6.yaml`<br>`kubectl scale deploy/k6-load --replicas=1`<br>`kubectl rollout restart deploy/k6-load` | Rebuilds the ConfigMap from `load/` and starts `daily.js` | cluster up |
| `load-stop` | `kubectl scale deploy/k6-load --replicas=0` | Stops the training signal. **REQUIRED before any benchmark.** | — |
| `capacity` | `kubectl delete job k6-capacity --ignore-not-found`<br>`kubectl create configmap k6-scripts …`<br>`kubectl apply -f k8s/load/k6-capacity.yaml`<br>`kubectl wait --for=condition=complete job/k6-capacity --timeout=15m`<br>`kubectl logs job/k6-capacity \| tail -25` | Measures one pod's req/s knee | **1 replica and no HPA first** |
| `collect` | `while true; do .venv/bin/python collect.py; sleep 600; done` | Runs the collector **in a loop, every 10 minutes** | `forward-prom` running |
| `bench` | (see §11.6 — full recipe quoted there) | Runs one 20-minute benchmark, writes `bench/$(RUN).json`, `.start`, `.end` | `RUN=` set; `k6-load` at 0 replicas |
| `ui` | `.venv/bin/streamlit run dashboard.py` | Starts the dashboard on :8501 | none for the replay page |
| `web-data` | `node web/scripts/build-data.mjs` | Regenerates `web/public/data/` from `bench/replay*.json` and `outputs/results.csv`. The only deriver. | node; `outputs/results.csv` present (or a committed `backtest.json`) |
| `web-dev` | `web-data`, then `npm --prefix web run dev` | Next dev server on localhost:3000 | `npm install` in `web/` |
| `web-build` | `web-data`, then `npm --prefix web run build` | Static export to `web/out/` | same |
| `web-deploy` | `web-build`, then `cd web && vercel deploy --prod` | Publishes to Vercel | `vercel login` done on this machine |
| `replay-data` | `.venv/bin/python export_replay.py`<br>`.venv/bin/python export_replay.py --runs A1,A2,A3,B1,B2,B3,C1,C2,C3 --out replay-step.json --scenario "instant 4x step: 20 -> 80 req/s at minute 5, held 4 min"` | Re-freezes **both** scenarios out of Prometheus | `forward-prom` running; runs still inside 15-day retention |
| `retrain` | `.venv/bin/python retrain.py` | Scores a candidate and promotes it only on a real win | model + data present |
| `retrain-check` | `.venv/bin/python retrain.py --dry-run` | Scores both, changes nothing | same |

The venv detection exists for a reason, quoted from the Makefile:

> Use the venv's interpreters when they exist, otherwise whatever is on PATH.
> Without this, every target here fails with "No such file or directory" unless
> you remembered to `source .venv/bin/activate` first — which is a bad way to
> find out your dashboard is fine and your shell was not.

And the port choice:

> 8000, not 5000: macOS Control Center holds 5000 for AirPlay Receiver, and when
> something else is listening there a failed connection comes back as an instant
> 403 rather than an error — which once let k6 report 12.5M healthy iterations
> while delivering nothing at all. 8000 also matches the container's port.

## 14.2 First-time setup — exact ordered sequence

```bash
# 1. Host Python environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Create the kind cluster (name MUST be "autoscale")
kind create cluster --name autoscale

# 3. Install the Prometheus stack
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring --create-namespace

# 4. Build, side-load, deploy the app
make build && make load && make deploy

# 5. Confirm pods reach 1/1 (readiness gap measured at 19 s, 19 s, 18 s)
make pods

# 6. Open the Prometheus port-forward and LEAVE IT RUNNING (separate terminal)
make forward-prom
```

**Note:** the exact `kind create cluster` and `helm install` commands are **not recorded in
the repo** — they are reconstructed from the object names the manifests and Makefile
reference (`--name autoscale`, `svc/monitoring-kube-prometheus-prometheus`, namespace
`monitoring`). Marked as inference, not repo ground truth.

## 14.3 The full training loop

```bash
# terminal 1 — must stay open
make forward-prom

# terminal 2
make load-start                 # start daily.js inside the cluster

# ...leave it running for hours/days, collecting...
make collect                    # or: python collect.py, repeatedly

# once enough history exists
python src/backtest.py          # -> outputs/results.csv (read top-down, lowest cost wins)
python src/train_final.py       # -> models/forecaster.joblib
python src/predictor.py         # dry run: verifies the LIVE path, changes nothing
```

## 14.4 Running the live controller

```bash
# terminal 1
make forward-prom

# terminal 2
make load-start

# terminal 3 — pick ONE mode
kubectl apply -f k8s/hpa.yaml
CAPACITY_PER_POD=20 MODE=hpa-floor python src/controller.py    # recommended

#   ...or...
kubectl delete -f k8s/hpa.yaml
CAPACITY_PER_POD=20 MODE=replicas python src/controller.py
```

## 14.5 One benchmark end to end

```bash
make load-stop                          # REQUIRED
kubectl apply -f k8s/hpa.yaml           # arm A
make bench RUN=A1 SCRIPT=benchmark.js   # 20 minutes
# repeat for A2, A3, then set up arm B or C and repeat
```

## 14.6 Regenerating all results

```bash
make forward-prom                            # required: analyze replays Prometheus
python analyze.py                            # ramp   -> results-r.md, outputs/comparison-r.png
python analyze.py --suffix '' --event 5,9    # step   -> results.md,   outputs/comparison.png
make replay-data                             # -> bench/replay.json, bench/replay-step.json
python src/backtest.py                       # -> outputs/results*.csv, forecast.png
make web-data                                # -> web/public/data/ (picks up both of the above)
make web-build                               # -> web/out/
```

## 14.6b Deploying the public site

First time on a machine:

```bash
vercel login                                 # once, per machine
cd web && npm install                        # once
cd web && vercel link --yes --project predictive-autoscaling --scope pavan-fac7
```

Every deploy after that:

```bash
make web-deploy        # runs web-data -> web-build -> vercel deploy --prod
```

Production URL: **https://predictive-autoscaling.vercel.app**
Vercel scope: `pavan-fac7`. Project: `predictive-autoscaling`. Root directory: `web/`.

Note: `vercel link` attempted and **failed** to connect the GitHub repository
(`Failed to connect pavansai2608/predictive-autoscaling to project`). There is therefore
**no push-to-deploy**; deploys are CLI-driven. Connect the repo in the Vercel dashboard if
Git-triggered deploys are wanted.

## 14.7 Prerequisites with exact versions

Recorded in the repo:

| Tool | Version | Source |
|---|---|---|
| Python (host) | **3.14.2** | `CLAUDE.md` Environment section |
| Python (container) | **3.11** (`python:3.11-slim`) | `Dockerfile` line 2 |
| pandas | **3.0.5** | `requirements.txt` |
| numpy | **2.5.2** | `requirements.txt` |
| pyarrow | **25.0.1** | `requirements.txt` |
| prometheus-api-client | **0.7.2** | `requirements.txt` |
| lightgbm | **4.7.0** | `requirements.txt` |
| joblib | **1.5.3** | `requirements.txt` |
| matplotlib | **3.11.1** | `requirements.txt` |
| streamlit | **1.62.0** | `requirements.txt` |
| altair | **6.2.2** | `requirements.txt` |
| kubernetes (Python client) | **36.0.3** | `requirements.txt` |
| Node.js | **25.6.1** | `node --version` on this machine |
| npm | **11.9.0** | `npm --version` |
| Next.js | **16.3.4** | `web/package-lock.json` |
| React / React DOM | **19.2.8** | `web/package-lock.json` |
| TypeScript | dev dependency, version in `web/package-lock.json` | `web/package.json` |
| Vercel CLI | **59.11.7** | `vercel --version` |
| ~~streamlit~~ | **REMOVED** (was 1.62.0) | deleted with `dashboard.py` |
| ~~altair~~ | **REMOVED** (was 6.2.2) | deleted with `dashboard.py` |
| fastapi | **unpinned** | `app/requirements.txt` |
| uvicorn | **unpinned** (deliberately plain, not `uvicorn[standard]`) | `app/requirements.txt` |
| prometheus-fastapi-instrumentator | **unpinned** | `app/requirements.txt` |

**NOT recorded anywhere in the repo:**

| Tool | Version |
|---|---|
| Docker / Docker Desktop | `UNKNOWN — not found in repo` (CLAUDE.md only records the 8 GB memory cap) |
| kind | `UNKNOWN — not found in repo` |
| kubectl | `UNKNOWN — not found in repo` |
| helm | `UNKNOWN — not found in repo` |
| k6 | `UNKNOWN — not found in repo` (the container image tag is in `k8s/load/*.yaml`) |
| Kubernetes server version | `UNKNOWN — not found in repo` |
| kube-prometheus-stack chart version | `UNKNOWN — not found in repo` |

CLAUDE.md records only: *"Installed and ready: `kind`, `kubectl`, `helm`, `k6`."* and
*"MacBook, Apple Silicon, 16GB RAM. Docker Desktop capped at **8GB**."*

Also recorded: *"LightGBM works, so `models.BACKEND == "lightgbm"`; the scikit-learn
fallback in `models.py` is **untested** and sklearn is **not installed**."*

## 14.8 Every "gotcha" — things that silently break if done in the wrong order

| # | Gotcha | Consequence |
|---|---|---|
| 1 | After **any** change to `app/`, you must run **all three**: `make build && make load && make deploy` | Otherwise the cluster runs the old image with no error |
| 2 | Editing a file in `load/` without running `make load-start` | *"leaves the old version running, silently"* — the ConfigMap is not rebuilt |
| 3 | Running a benchmark without `make load-stop` | Both arms serve a second uncontrolled workload. `make bench` **guards against this** and refuses |
| 4 | Running `controller.py` in `MODE=replicas` with the HPA installed | Controller **exits** with instructions — they would fight over the replica count |
| 5 | Running `controller.py` in `MODE=hpa-floor` without the HPA | Controller **exits** with instructions |
| 6 | Forgetting `make forward-prom` | `collect.py`, `live.py`, `predictor.py`, `analyze.py`, `export_replay.py` and the dashboard's Live page all hardcode `localhost:9090` and will fail or hold |
| 7 | Running Python as `python -m src.backtest` or from inside `src/` | Breaks the flat `import config as C` style; must be `python src/backtest.py` **from the repo root** |
| 8 | Running `make capacity` with the HPA installed or >1 replica | Measures the wrong thing — it must be 1 replica, no HPA |
| 9 | Waiting more than 15 days to run `analyze.py` or `make replay-data` on a run | Prometheus retention has expired the window; pod-seconds can no longer be reconstructed |
| 10 | Closing the laptop lid | Clamshell Sleep freezes the cluster mid-run; `caffeinate` does not prevent it |
| 11 | Naming benchmark runs inconsistently | *"Run names should say which: A1s/B1s for step, A1r/B1r for ramp, or the two scenarios' results get averaged together"* |
| 12 | Accepting a run with `dropped_iterations > 0` | Invalid — k6 quietly reduced offered load exactly when the app was struggling |
| 13 | Changing `WORK_MS`, `STARTUP_DELAY_S`, the CPU limit, or `PEAK_RPS` | *"the horizon and capacity figures are void until re-measured"* |
| 14 | Writing an angle bracket in `dashboard.py`'s injected CSS | The entire stylesheet is silently dropped |
| 15 | Editing `web/public/data/*.json` by hand | It is generated. `make web-data` overwrites it, and the repo would then hold two disagreeing copies of the same numbers |
| 16 | Running `make web-build` without `outputs/results.csv` | The build script keeps the committed `backtest.json` and warns; if neither exists it exits 1 telling you to run `python src/backtest.py` |
| 17 | Adding a benchmark run and forgetting `make replay-data` then `make web-data` | The site silently keeps showing the old runs |
| 18 | Expecting `python src/controller.py --help` to print usage | It has **no** argparse — it starts the real 30 s control loop immediately. Use `--help` on `src/backtest.py` or `retrain.py` instead |

---

# 15. FOR A PORTFOLIO / RESUME

## 15.1 One-sentence description

Built a predictive Kubernetes autoscaler that forecasts request rate 60 seconds ahead with
a quantile-regression LightGBM model and scales pods before load arrives, proved it with a
controlled A/B benchmark against the stock HPA — including the scenario where it lost and
the architectural fix that turned that loss into a 49% win — and published the measured
results as a static report site at **https://predictive-autoscaling.vercel.app**.

## 15.2 The five most impressive TRUE, MEASURED claims

| # | Claim | Supporting number | Where it comes from |
|---|---|---|---|
| 1 | **62 % lower p99 latency than Kubernetes' built-in autoscaler** on a predictable ramp, for a stated 28 % more compute | 479 ms → 183 ms; 3,053 → 3,907 pod-seconds | `results-r.md`, generated by `analyze.py` from `bench/A*r.json` + `bench/B*r.json`, 3 runs per arm |
| 2 | **49 % lower p99 than the HPA on an instantaneous 4x spike**, achieved by composition rather than a better model | 467 ms → 240 ms; per-run 256/238/228 ms | `results.md`, arms A vs C, 3 runs each |
| 3 | **Forecasting alone was 40 % WORSE than doing nothing** on that spike — diagnosed from pod traces and fixed structurally | 467 ms → 655 ms | `results.md`, arms A vs B; root cause in `src/controller.py` lines 70–92 |
| 4 | **64.5 % lower cost than the naive baseline** across a 4-fold rolling-origin backtest | cost 4,294.81 vs 12,093.79 | `outputs/results.csv` |
| 5 | **The lowest-error model was the most expensive model** — 53 % better MAE, 31 % worse cost | MAE 2.236 vs 4.773; cost 5,635.94 vs 4,294.81 | `outputs/results.csv`, rows `gbm` and `gbm_q0.9` |

Bonus measured claim: the floor arm did not just win, it became **predictable** — run-to-run
p99 spread collapsed from **357 ms wide** (arm B: 522/565/879) to **28 ms wide**
(arm C: 256/238/228).

## 15.3 Full tech stack with exact versions

| Layer | Technology | Version |
|---|---|---|
| Application | FastAPI + uvicorn | unpinned |
| Metrics instrumentation | prometheus-fastapi-instrumentator | unpinned |
| Container | Docker, `python:3.11-slim`, image `traffic-app:v1` | Docker version UNKNOWN |
| Orchestration | Kubernetes via kind, cluster `autoscale` | UNKNOWN |
| Monitoring | Prometheus (kube-prometheus-stack via Helm) | chart version UNKNOWN |
| Load generation | k6, `ramping-arrival-rate` executor | UNKNOWN |
| Host Python | CPython | **3.14.2** |
| Data | pandas **3.0.5**, numpy **2.5.2**, pyarrow **25.0.1** | pinned |
| Metrics client | prometheus-api-client **0.7.2** | pinned |
| Model | LightGBM **4.7.0** (quantile objective, alpha=0.90), joblib **1.5.3** | pinned |
| Charts | matplotlib **3.11.1**, altair **6.2.2** | pinned |
| UI | Streamlit **1.62.0** | pinned |
| Cluster control | kubernetes Python client **36.0.3** | pinned |
| Build/orchestration | GNU Make | UNKNOWN |
| Report site | Next.js **16.3.4** (App Router, `output: 'export'`), React **19.2.8**, TypeScript | pinned in `web/package-lock.json` |
| Hosting | Vercel (static CDN), deployed by Vercel CLI **59.11.7** | — |
| Charts | Hand-rolled SVG — no charting dependency | — |
| Node / npm | **25.6.1** / **11.9.0** | local toolchain |

## 15.4 Resume bullet points (each contains a real measured number)

- Built a predictive Kubernetes autoscaler that forecasts request rate 60 s ahead with a
  quantile LightGBM model (α=0.90, 400 trees, 39 engineered features), cutting p99 latency
  **62 %** (479 ms → 183 ms) against the stock HPA under byte-identical load, for a
  transparently reported **+28 %** compute.
- Designed and ran a controlled A/B benchmark across **15 twenty-minute runs** and three
  scaling policies, holding traffic, replica bounds and steady-state pod count constant so
  the experiment measured reaction *timing* rather than provisioning generosity.
- Diagnosed a **40 % regression** (p99 467 ms → 655 ms) where forecasting alone lost to the
  stock autoscaler on an instantaneous 4x spike, tracing it from pod traces to early
  capacity *withdrawal* at minute 8 of a spike that ran to minute 9.
- Fixed that regression by composition rather than a better model — having the forecast
  drive the HPA's `minReplicas` instead of the replica count — reaching **49 % lower p99**
  than the HPA alone (467 ms → 240 ms) and collapsing run-to-run spread from **357 ms to
  28 ms**.
- Built the evaluation harness before the models: 4-fold rolling-origin backtest with a
  horizon-sized gap and an asymmetric cost metric (10:1 under- vs over-provisioning),
  which showed the shipping model beating the naive baseline by **64.5 %** on cost
  (4,295 vs 12,094).
- Demonstrated that metric choice dominated model choice: a mean-targeting GBM achieved
  **53 % better MAE** (2.24 vs 4.77) while scoring **31 % worse on cost**, because its
  errors fell on the expensive side.
- Measured rather than assumed the two constants that determine correctness — pod
  start-up (**19 s, 19 s, 18 s** → 60 s horizon) and per-pod capacity (**20 req/s**, knee
  at 24) — after discovering a default of 120 req/s would have under-provisioned by **6x**
  with no forecasting metric ever revealing it.
- Found and fixed two train/serve skew bugs that produced plausible forecasts **~45 % too
  high** with no error raised: an unshared time-grid reindex (live window held 120 rows
  spanning 7.8 h across 13 gaps) and a clock feature frozen at a constant (`f_pos_in_cycle`
  read 142.0 on three consecutive live fetches).
- Hardened the control loop with refusal semantics — no-data, non-finite, and
  >10x-recent-max guards — which fired on **221 of 975 logged decisions (22.7 %)**, handing
  control back to the reactive HPA instead of acting on bad input.
- Built a retrain gate that scores candidates on data collected *since* the champion was
  trained; its one evaluation correctly **declined** a model **114.6 % worse** on cost
  (4,299.3 vs 2,003.0).
- Traced a full-cluster outage during benchmarking to Kubernetes probe defaults treating a
  *busy* pod as a *dead* one — available replicas reached **zero** mid-spike with p99 at
  **19.8 s** — and fixed it by widening the readiness probe to 3 s × 6 failures.
- Replaced a 1,000-line Streamlit app with a static Next.js site on Vercel scoring
  **Lighthouse 100 on both Performance and Accessibility** (CLS 0, TBT 0 ms, LCP 0.5 s),
  eliminating a hardcoded headline figure by deriving it at build time from
  `outputs/results.csv` — and correctly declined to migrate the one page that needs
  Prometheus and a 1.1 MB model in-process rather than faking its data.

## 15.5 The three hardest engineering problems solved

**1. Making the A/B benchmark actually fair.**
Most of the project's effort. It required discovering that `kubectl port-forward` pins all
traffic to one pod (6.94 req/s on one, 0.00 on three others), that kube-proxy balances per
TCP *connection* so keep-alive pinned 13.05 req/s to a single pod, that closed-loop VUs make
offered load a function of the autoscaler's own success, and that `requests.cpu ≠ limits.cpu`
makes the HPA's utilisation percentage meaningless (20 pods at 31 % utilisation while the
HPA reported 58–60 % and believed itself on target). Each was invisible in the results
until found.

**2. Train/serve skew that raises no error.**
Both bugs produced forecasts ~45 % too high and looked completely normal. Neither was
catchable by the backtest, which only ever exercises the training path. The fix was
structural — one `build_table()` shared by both paths, `to_grid()` called from both, clock
features anchored to the Unix epoch so they are identical *by construction*, the feature
list saved inside the model bundle, and `reindex(columns=...)` before every prediction —
plus a dedicated dry-run script (`predictor.py`) whose only job is to exercise the live path.

**3. Turning a negative result into the project's best result.**
Predictive scaling lost by 40 % on the instant spike. The instinct is to tune the model; the
evidence said otherwise. Reading the pod traces showed it was not losing on the way up
(5 pods vs the HPA's 3) but on the way *down* — cutting at minute 8 of a spike that ran to
minute 9. The insight was that a forecast has no more warning about an event's **end** than
its **start**, so the fix had to be architectural: let the forecast raise the HPA's floor
(which forces pods to appear) but never lower the pod count (lowering a floor only *permits*
removal, and the HPA declines while CPU is high). This is how AWS and KEDA compose
predictive with reactive scaling.

## 15.6 Honest limitations — explicitly NOT production-ready

| Limitation | Evidence in repo |
|---|---|
| **The traffic is synthetic.** A scripted diurnal cycle with random spikes, learnable by construction. Real traffic carries structure this model has never faced. | `README.md` Limitations; `load/daily.js` |
| **51 hours of history only**, so `lag_1680` ("one week ago") is empty for most rows and contributes little. | `data/traffic.parquet` span 51.2458 h |
| **One workload shape.** A deliberately CPU-bound app with a fixed 30 ms burn and a hard 400m limit. Findings may not transfer to I/O-bound or bursty-CPU services. | `app/main.py`, `k8s/deployment.yaml` |
| **The HPA target of 90 % is unusually high** and defensible only for this pod. | `k8s/hpa.yaml`: *"A general-purpose service with bursty CPU should not copy this number."* |
| **The controller runs on a laptop**, authenticating from `~/.kube/config`. In-cluster it would need `load_incluster_config()` and a ServiceAccount. | `src/controller.py` `k8s_api()` |
| **Single-instance, no leader election, no HA.** Stopping it reverts nothing. | `src/controller.py` |
| **No test suite and no linter.** | `CLAUDE.md`: *"There is no test suite and no linter configured. The backtest **is** the correctness check for the forecasting side."* |
| **The scikit-learn fallback path is untested** and sklearn is not installed. | `CLAUDE.md` Environment |
| **Prometheus and the model are hardcoded to `localhost:9090`** across six files. | `collect.py`, `live.py`, `predictor.py`, `analyze.py`, `export_replay.py`, `dashboard.py` |
| **Only one retrain has ever been evaluated**, and it was declined. The gate is proven to reject, not to promote. | `models/retrain_history.jsonl` (1 line) |
| **Arm C was only run on one scenario** (the spike). There is no ramp data for the floor mode. | no `C*r` files in `bench/` |
| **No alerting** on consecutive `hold` decisions — a controller that quietly stops acting looks identical to one that is working. | not implemented |

## 15.7 Genuinely unusual for a personal project

1. **It publishes a result where the approach loses.** The step scenario shows predictive
   scaling 40 % worse than doing nothing, kept in the repo, in the README, and in the
   generated `results.md`. Most portfolio projects show only the winning scenario.
2. **`MODE=replicas` was kept rather than deleted** specifically because it is the arm the
   middle row of the results table measures — *"removing it would make that row
   unreproducible."*
3. **`bench/discarded/` exists**, with a README explaining exactly why a run was thrown out
   and why the failure was still a true finding about CPU-based autoscaling.
4. **The scoreboard was written before the models**, on the stated grounds that designing a
   metric after seeing results means picking the one that flatters what you built.
5. **Two constants are marked "must be MEASURED, never guessed"** with the measurement
   procedure and raw numbers recorded in the source.
6. **The cost weights are mathematically tied to the model's objective** — 10:1 is exactly
   a quantile loss at q = 10/11 = 0.909, which is why the model targets q = 0.90.
7. **Both p99 and pod-seconds are reported in the same sentence, always**, on the stated
   grounds that a latency win bought with unlimited compute is not a win.
8. **The comments explain *why*, not *what*** — most of the operational knowledge in this
   extract came from code comments recording measured numbers at the point of the decision
   they justify.
9. **The retrain gate scores on data neither model has seen**, with the champion's
   `trained_through` timestamp stored in the bundle to make that split possible.
10. **Failures are logged as first-class outcomes**: the controller's `hold` action appears
    221 times in `logs/decisions.csv`, and the UI surfaces the model *declining to answer*
    rather than hiding it.
11. **A migration that refused to migrate everything.** Two of three pages moved to Vercel;
    the third was deleted rather than stubbed, because a live-forecast page fed canned
    numbers cannot do the only job it has — catching train/serve skew. The technical reason
    is recorded in `MIGRATION_NOTES.md` alongside what regressed.

---

# 16. GAPS

## 16.1 Things in the repo that could not be read or fully understood

| Item | Status |
|---|---|
| `models/forecaster.joblib` | **Read successfully** (required `sys.path.insert(0,"src")` so the pickle's `import models` resolves to `src/models.py` rather than the `models/` directory — a real name collision). Contents extracted in §4.4. |
| `outputs/*.png` (3 files) | **Binary images — content not inspected.** What they plot is inferred from the code that writes them (`backtest.py:_plot()`, `analyze.py`), which is quoted in §8.9. Their visual appearance is `UNKNOWN`. |
| `data/traffic.parquet` | Read fully; all statistics in §4.1 are computed, not estimated. |
| `bench/*.json` | All 15 read and consolidated. Each contains a full k6 `metrics` block; only the fields listed in §8.6 were extracted. Other k6 metrics present in the JSON (e.g. `http_req_connecting`, `http_req_tls_handshaking`, `data_sent`, `data_received`, `iteration_duration`, `checks`) were **not** tabulated. |
| `.streamlit/credentials.toml` | Read (11 lines). Contains an empty email entry to suppress the first-run prompt. |

## 16.2 Things referenced but MISSING from the repo

| Referenced | Referenced where | Status |
|---|---|---|
| `LEARN.md` | Created during a prior session and delivered to the user | **Not present in the repo**, never committed. |
| `packages.txt` | Commit `0a1670a` ("drop packages.txt") | **Deliberately removed.** Not a gap. |
| `PROJECT_EXTRACT.md` | This document | Created by this extraction. |
| Cluster creation command | Nowhere | `UNKNOWN — not found in repo`. Reconstructed in §14.2 from object names only. |
| Helm install command / chart version | Nowhere | `UNKNOWN — not found in repo`. |
| `.claude/`, `.agents/` | `.gitignore` | Intentionally ignored; not part of the project. |
| `A1s/B1s` run naming | `Makefile` comment: *"A1s/B1s for step"* | **No `*s`-suffixed files exist.** The step runs are unsuffixed (`A1`, `B1`, `C1`). The Makefile comment describes a convention that was not followed. |
| Sklearn fallback | `src/models.py` | Code path exists but sklearn is **not installed**; path is untested. |

## 16.3 CONTRADICTIONS between documentation and code

The code is the source of truth.

### Fixed during the 2026-09-07 migration

| # | Was | Now |
|---|---|---|
| 1 | `CLAUDE.md`: *"12,281 rows, 51h, **100% coverage**"* | Corrected to **99.846%**, naming the single 300 s gap at `2026-08-21T18:33:00Z` and the 19 missing rows. |
| 2 | `CLAUDE.md`: *"Both MEASURED on **2026-08-22**"* | Corrected to **2026-08-19**, citing `src/config.py` and commit `be0478a`. |
| 3 | `CLAUDE.md`: *"Amber = reactive arm, cyan = predictive"* | Replaced: three arms, wine `#8c2f39` / teal `#15616d` / moss `#4a6b2a`, with the dash-keying rationale. |
| 4 | `CLAUDE.md` Commands omitted `make ui` / `retrain` / `collect` | The four `web-*` targets are documented; `ui` no longer exists. |
| 5 | `README.md`: *"**Two pages.**"* | Rewritten as "The report site": two deployed routes plus a local-only live view. |
| 6 | `CLAUDE.md` Results heading dated **2026-08-24** above a 2026-08-30 table | Heading now reads **2026-08-30**. |
| 7 | Overview hardcoded the string **"64.5% lower cost"** | **Computed** from `outputs/results.csv` by `web/scripts/build-data.mjs`. |
| 8 | `CLAUDE.md`: *"...and dashboard.py all hardcode `localhost:9090`"* | Corrected; the site never contacts the cluster. |

### Still open

| # | Claim | Actual | Severity |
|---|---|---|---|
| 9 | `Makefile` comment: *"A1s/B1s for step"* | Step runs are named **without** a suffix (`A1`, `B1`, `C1`). Convention documented but never followed. | Cosmetic |
| 10 | `analyze.py` colours `#eb6834` / `#2a78d6` / `#1f9d55` | The site and `README.md`'s prose use `#8c2f39` / `#15616d` / `#4a6b2a`. **The committed PNGs still show the old palette**, so `outputs/comparison*.png` and the website disagree on arm colour. | Inconsistency between two published surfaces |
| 11 | `replicas_needed()` in `src/models.py` | **Never called.** `controller.py` re-implements the formula inline. The third copy in `dashboard.py` is gone, so this is now 2 copies rather than 3. | Duplication |
| 12 | `k8s/load/*.yaml` pin `image: grafana/k6:latest` | Not a pinned version; the k6 build behind the published runs is unrecoverable. | **Reproducibility gap** |
| 13 | `load/daily.js` default `PEAK_RPS = 80` | `k8s/load/k6.yaml` sets `"40"`, which is what actually ran. | Effective value only visible in the manifest |
| 14 | `CLAUDE.md` repo layout *"state as of 2026-08-30"* | The working tree is 2026-09-07 and adds `web/`. The layout section now lists `web/`, but the date line was not re-dated. | Minor staleness |

### New in this migration

| # | Issue | Detail |
|---|---|---|
| 15 | **The site and `results.md` disagree by 1 ms on the floor arm.** | `export_replay.py` writes `round(p99)` into each run summary, so anything reading `bench/replay*.json` averages integers. Floor-arm mean p99: site **241 ms** (mean of 256/238/228), `results.md` **240 ms** (mean of raw 255.51/237.84/227.58). The deleted Streamlit dashboard behaved identically, so this is inherited, not introduced — but two published surfaces now print different numbers. |
| 16 | **No push-to-deploy.** | `vercel link` failed to connect the GitHub repo (`Failed to connect pavansai2608/predictive-autoscaling to project`). Deploys are CLI-only via `make web-deploy`. |
| 17 | **The migration is uncommitted** at extraction time. | `dashboard.py` and `.streamlit/` are staged as deleted; `web/`, `MIGRATION_NOTES.md` and `PROJECT_EXTRACT.md` are untracked. |
| 18 | **Deployed via the Vercel CLI, not the Vercel MCP server.** | The MCP server is connected but **unauthorized**, and its OAuth flow cannot run in a non-interactive session. The CLI was already authenticated as `pavansai2608` with a single scope, so nothing was guessed. |

## 16.4 Things a reader should know are absent

- **No CI configuration** of any kind (no `.github/`, no workflow files).
- **No tests** — `CLAUDE.md` states this explicitly as a deliberate choice.
- **No linter or formatter configuration** (no `ruff.toml`, `setup.cfg`, `pyproject.toml`).
- **No `LICENSE` file.**
- **No `Chart.yaml` / Helm values** recording how Prometheus was installed.
- **No `kind` cluster config file** — the cluster was created with defaults plus a name.
- **The exact `helm install` and `kind create cluster` invocations are unrecorded.**

---

# END OF EXTRACT

## Files written

| Path | Lines |
|---|---:|
| `PROJECT_EXTRACT.md` | 9,320 |

No continuation files were needed — the entire extract fits in this single document.

## Section completion checklist

| § | Section | Status | Notes |
|---|---|---|---|
| 1 | REPO INVENTORY | **COMPLETE** | 100 files with path/lines/KB/purpose; LOC by language; `.gitignore` verbatim; committed-but-normally-ignored files explained; full `git log --oneline --stat` (35 commits, oldest first); full commit messages verbatim; plain-English timeline in 6 phases; `README.md` and `CLAUDE.md` verbatim |
| 2 | FULL SOURCE OF EVERY CODE FILE | **COMPLETE** | All 5 app/build files, all 9 `src/*.py`, all 5 top-level `.py`, all 7 `k8s/**` manifests, all 4 `load/*.js`, `Makefile`, both `.streamlit/*.toml`, `.gitignore`, `.dockerignore`, `bench/discarded/README.md` — pasted verbatim via `cat`, no elisions |
| 3 | EVERY CONSTANT AND TUNABLE | **COMPLETE** | All 14 `config.py` constants with line numbers; all 10 Python env vars + all 13 k6 `__ENV` vars with defaults; magic numbers in `controller.py`, `live.py`, `features.py`, `models.py`, `evaluate.py`, `collect.py`, `analyze.py`, `export_replay.py`, `dashboard.py` |
| 4 | THE DATA | **COMPLETE** | 12,281 rows; dtypes; 2026-08-19 15:42:00Z → 2026-08-21 18:56:45Z; 51.2458 h; 15 s interval; min/mean/median/max/std; 0 NaN; 1 gap of 300 s; 99.846 % coverage; generation path; exact `collect.py` cutoff rules; model bundle and retrain history |
| 5 | FEATURE ENGINEERING | **COMPLETE** | All **39** features named and counted; grouped into 13 lags / 15 rolling / 6 shape / 5 clock, each with exact code and stated reason; exact target line; train/serve sharing mechanisms in a table |
| 6 | THE MODELS | **COMPLETE** | All 5 ladder models with verbatim implementations; every LightGBM parameter with exact values, cross-checked against the saved Booster; sklearn fallback params; `replicas_needed()` verbatim with worked examples; the three-way duplication flagged |
| 7 | EVALUATION METHOD | **COMPLETE** | Fold code verbatim; **actual computed folds** for 12,277 rows (4 folds, 10,353–11,793 train, 480 test, gap 4); cost function verbatim with weights substituted; all 7 metrics defined |
| 8 | ALL RESULTS | **COMPLETE** | `results.csv`, `results_by_fold.csv`, `feature_importance.csv`, `results.md`, `results-r.md` verbatim; consolidated table of **all 15 runs** with 19 columns each; pod-seconds table; arm means; both discarded runs with metrics and the verbatim reason; `logs/decisions.csv` with 975 rows, 6 action types, all 14 distinct reasons, 15 example rows; all 3 images described |
| 9 | THE CONTROL LOOP | **COMPLETE** | 30 s trigger; exact PromQL, 29,700 s window, `localhost:9090`; reshaping; `reindex(columns=...)`; pod formula fully substituted; all 4 guards with conditions and log output; both modes with the differing code quoted; kubeconfig auth and all 5 API calls; one worked cycle |
| 10 | ARCHITECTURE MAP | **COMPLETE** | 13 components with location and port; 16 arrows with protocol/data/frequency; 9 Kubernetes objects with names, namespaces, labels, relationships; training flow and live flow as step-by-step ASCII; import dependency graph |
| 11 | THE EXPERIMENT DESIGN | **COMPLETE** | 3 arms with exactly what runs and what is disabled; all 4 k6 scenarios with every stage, rate, duration, VU setting and option; exact per-arm commands; 12 fairness controls each with a quoted implementing comment; `analyze.py` logic in 9 steps |
| 12 | EVERY BUG, TRAP, FAILURE AND FIX | **COMPLETE** | **33 entries** (24 bugs, 5 traps, 2 design traps, 2 findings), each with symptom/exact number, root cause, fix with file, and lesson |
| 13 | THE UI | **COMPLETE** | 3 pages; every control with widget type, label, range, default and effect; data source per element (file vs live); 8 unavailability behaviours; full colour table with contrast ratios and meanings; typography; interaction states; run command and URL |
| 14 | HOW TO RUN EVERYTHING | **COMPLETE** | All 15 Make targets with exact commands and prerequisites; ordered sequences for setup, training, live control, one benchmark, regenerating results; 12 pinned versions + 7 marked UNKNOWN; 14 gotchas |
| 15 | FOR A PORTFOLIO / RESUME | **COMPLETE** | One-sentence description; 5 top claims with sources; full stack; 11 resume bullets each with a measured number; 3 hardest problems; 12 limitations; 10 unusual aspects |
| 16 | GAPS | **COMPLETE** | Unreadable/partially-read items; 8 missing-but-referenced items; **14 documented contradictions** between docs and code; 7 categories of absent tooling |
