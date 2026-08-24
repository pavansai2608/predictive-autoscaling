"""Score the A/B benchmark.

    python analyze.py            # the ramp scenario (the headline result)
    python analyze.py --suffix s # the step scenario

Reads the k6 summaries in bench/, replays each run's window against Prometheus
for the replica count, and writes results.md plus outputs/comparison.png.

Two numbers, always together. A latency win bought with far more compute is not
a win, and a benchmark that reports only p99 is not an honest one — so
pod-seconds sits in the same table, not in a footnote.

Pod-seconds is not captured live: Prometheus already records the replica count
and keeps 15 days, so each run's start/end epoch (written by `make bench`) is
enough to reconstruct it afterwards.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import requests

ROOT = Path(__file__).resolve().parent
PROM = "http://localhost:9090"
STEP = 20  # seconds between samples when replaying a window

C_A = "#eb6834"   # baseline / HPA
C_B = "#2a78d6"   # predictive


def prom_range(query: str, start: int, end: int, step: int = STEP):
    """One Prometheus series over a run window, as (elapsed_seconds, value)."""
    r = requests.get(f"{PROM}/api/v1/query_range", params={
        "query": query, "start": start, "end": end, "step": step}, timeout=30)
    res = r.json().get("data", {}).get("result", [])
    if not res:
        return np.array([]), np.array([])
    v = res[0]["values"]
    t = np.array([int(x[0]) - start for x in v], dtype=float)
    y = np.array([float(x[1]) for x in v], dtype=float)
    return t, y


def load_run(name: str) -> dict | None:
    """k6 summary + the replica trace Prometheus recorded during that window."""
    j = ROOT / "bench" / f"{name}.json"
    s, e = ROOT / "bench" / f"{name}.start", ROOT / "bench" / f"{name}.end"
    if not (j.exists() and s.exists() and e.exists()):
        return None

    m = json.loads(j.read_text())["metrics"]
    d = m["http_req_duration"]["values"]
    start, end = int(s.read_text()), int(e.read_text())

    tp, pods = prom_range(
        'kube_deployment_status_replicas_available{deployment="traffic-app"}',
        start, end)
    # Latency over time comes from the APP's histogram, not from k6: k6 only
    # emits aggregates at the end of a run, and the shape over time is the
    # whole point of the chart.
    tl, p99 = prom_range(
        'histogram_quantile(0.99, sum by (le) '
        '(rate(http_request_duration_seconds_bucket{handler="/work"}[1m])))',
        start, end)

    return {
        "name": name,
        "p50": d["p(50)"], "p95": d["p(95)"], "p99": d["p(99)"], "max": d["max"],
        "reqs": int(m["http_reqs"]["values"]["count"]),
        "failed": m["http_req_failed"]["values"]["rate"] * 100,
        # A run that dropped iterations offered LESS load than intended, at
        # exactly the moment the app was struggling — it is not comparable.
        "dropped": int(m.get("dropped_iterations", {}).get("values", {}).get("count", 0)),
        "pod_seconds": float(np.nansum(pods) * STEP) if pods.size else float("nan"),
        "t_pods": tp, "pods": pods,
        "t_lat": tl, "p99_series": p99,
    }


def mean_series(runs: list[dict], tkey: str, ykey: str):
    """Average the runs onto a common elapsed-time axis.

    Runs differ by a few seconds in length, so they are interpolated onto one
    grid rather than averaged index-by-index — otherwise a run that started
    two samples late would shift the whole curve.
    """
    runs = [r for r in runs if r[tkey].size]
    if not runs:
        return np.array([]), np.array([])
    grid = np.arange(0, min(r[tkey].max() for r in runs) + 1, STEP)
    stack = [np.interp(grid, r[tkey], r[ykey]) for r in runs]
    return grid, np.nanmean(stack, axis=0)


def main(suffix: str, event: tuple[int, int]):
    arms = {
        "Baseline (HPA)": [load_run(f"A{i}{suffix}") for i in (1, 2, 3)],
        "Predictive": [load_run(f"B{i}{suffix}") for i in (1, 2, 3)],
    }
    arms = {k: [r for r in v if r] for k, v in arms.items()}
    for k, v in arms.items():
        if not v:
            raise SystemExit(f"no runs found for {k} with suffix '{suffix}'")

    # ---- table --------------------------------------------------------------
    lines = ["| arm | runs | p50 | p95 | **p99** | max | pod-seconds | failed |",
             "|---|---|---|---|---|---|---|---|"]
    summary = {}
    for arm, runs in arms.items():
        f = lambda k: np.mean([r[k] for r in runs])
        summary[arm] = {"p99": f("p99"), "pods": f("pod_seconds")}
        lines.append(
            f"| {arm} | {len(runs)} | {f('p50'):.0f} ms | {f('p95'):.0f} ms | "
            f"**{f('p99'):.0f} ms** | {f('max'):.0f} ms | {f('pod_seconds'):.0f} | "
            f"{f('failed'):.2f}% |")

    a, b = summary["Baseline (HPA)"], summary["Predictive"]
    lat = (1 - b["p99"] / a["p99"]) * 100
    cost = (b["pods"] / a["pods"] - 1) * 100
    head = (f"p99 latency: baseline {a['p99']:.0f} ms -> predictive {b['p99']:.0f} ms "
            f"({lat:.0f}% lower). Pod-seconds: {a['pods']:.0f} -> {b['pods']:.0f} "
            f"({cost:+.0f}%).")

    per_run = ["", "Individual runs:", "",
               "| run | p99 | pod-seconds | dropped |", "|---|---|---|---|"]
    for runs in arms.values():
        for r in runs:
            flag = "" if r["dropped"] == 0 else "  ⚠ INVALID"
            per_run.append(f"| {r['name']} | {r['p99']:.0f} ms | "
                           f"{r['pod_seconds']:.0f} | {r['dropped']}{flag} |")

    out = ROOT / f"results{'-' + suffix if suffix else ''}.md"
    out.write_text("# A/B benchmark\n\n" + head + "\n\n" + "\n".join(lines + per_run) + "\n")
    print("\n  " + head + "\n")
    print("\n".join(lines))

    # ---- chart --------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), sharex=True,
                                   gridspec_kw={"height_ratios": [2, 1]})
    for (arm, runs), c in zip(arms.items(), (C_A, C_B)):
        t, y = mean_series(runs, "t_lat", "p99_series")
        if t.size:
            ax1.plot(t / 60, y * 1000, color=c, lw=1.8, label=arm)
        t, y = mean_series(runs, "t_pods", "pods")
        if t.size:
            ax2.step(t / 60, y, color=c, lw=1.6, where="post", label=arm)

    for ax in (ax1, ax2):
        # Dashed lines bracket the event, so "did capacity arrive before the
        # traffic did" is answerable by eye rather than from the table.
        for x in event:
            ax.axvline(x, ls="--", lw=0.9, color="#898781")
        ax.grid(alpha=0.25, lw=0.6)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)

    ax1.set_ylabel("p99 latency (ms)")
    ax1.set_title(f"Predictive vs reactive autoscaling — mean of "
                  f"{min(len(v) for v in arms.values())} runs per arm", fontsize=12)
    ax1.legend(frameon=False, ncols=2)
    ax2.set_ylabel("pods ready")
    ax2.set_xlabel("minutes into run")
    fig.tight_layout()
    (ROOT / "outputs").mkdir(exist_ok=True)
    png = ROOT / f"outputs/comparison{'-' + suffix if suffix else ''}.png"
    fig.savefig(png, dpi=150)
    plt.close(fig)
    print(f"\n  wrote {out.name} and {png.relative_to(ROOT)}\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Score the A/B benchmark.")
    ap.add_argument("--suffix", default="r",
                    help="run-name suffix: 'r' = ramp (default), 's'/'' = step")
    ap.add_argument("--event", default="4,14",
                    help="minutes bracketing the load event, for the chart")
    a = ap.parse_args()
    main(a.suffix, tuple(int(x) for x in a.event.split(",")))
