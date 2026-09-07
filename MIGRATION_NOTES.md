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
