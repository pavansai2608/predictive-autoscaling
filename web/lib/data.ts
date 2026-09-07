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
