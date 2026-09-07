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
