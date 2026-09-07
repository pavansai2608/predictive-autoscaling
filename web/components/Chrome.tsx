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
