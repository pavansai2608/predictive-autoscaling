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
