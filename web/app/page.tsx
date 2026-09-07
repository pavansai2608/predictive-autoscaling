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
