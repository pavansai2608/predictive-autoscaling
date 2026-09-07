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
