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
