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
