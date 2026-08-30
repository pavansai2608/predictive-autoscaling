# A/B benchmark

p99 latency: baseline 467 ms -> predictive 655 ms (-40% lower). Pod-seconds: 2993 -> 3080 (+3%).

| arm | runs | p50 | p95 | **p99** | max | pod-seconds | failed |
|---|---|---|---|---|---|---|---|
| Baseline (HPA) | 3 | 50 ms | 281 ms | **467 ms** | 867 ms | 2993 | 0.00% |
| Predictive | 3 | 40 ms | 338 ms | **655 ms** | 1231 ms | 3080 | 0.00% |

Individual runs:

| run | p99 | pod-seconds | dropped |
|---|---|---|---|
| A1 | 493 ms | 3080 | 0 |
| A2 | 540 ms | 2940 | 0 |
| A3 | 369 ms | 2960 | 0 |
| B1 | 522 ms | 3060 | 0 |
| B2 | 565 ms | 3120 | 0 |
| B3 | 879 ms | 3060 | 0 |
