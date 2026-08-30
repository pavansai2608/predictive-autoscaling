"""The UI. Two pages: replay a recorded benchmark, or watch the model live.

    pip install -r requirements.txt
    streamlit run dashboard.py

REPLAY reads bench/replay.json — the six benchmark runs frozen out of Prometheus
by export_replay.py. It needs no cluster and works forever, which matters because
Prometheus keeps only 15 days.

LIVE reads Prometheus and the trained model directly. It needs `make forward-prom`
running, and it is the view that would have caught the two train/serve bugs
months earlier: it shows the forecast beside what actually happened next.

Nothing here computes a new result. The numbers are the ones the benchmark and
the backtest already produced — this file only draws them.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

BASE = "#c2591f"      # baseline / HPA — same hue as outputs/comparison-r.png
PRED = "#2a78d6"      # predictive
RUN_SECONDS = 1200    # every benchmark run is 20 minutes

st.set_page_config(page_title="Predictive Autoscaling", page_icon="📈", layout="wide")


# ---------------------------------------------------------------- data
@st.cache_data
def load_replay() -> dict | None:
    p = ROOT / "bench/replay.json"
    return json.loads(p.read_text()) if p.exists() else None


def series(run: dict, key: str) -> pd.DataFrame:
    return pd.DataFrame({"t": run["t"], key: run[key]}).dropna()


def value_at(run: dict, key: str, t: int):
    """Last known value at or before t — the reading a dashboard would show."""
    v = None
    for tt, x in zip(run["t"], run[key]):
        if tt > t:
            break
        if x is not None:
            v = x
    return v


def decision_at(run: dict, t: int):
    d = None
    for x in run["decisions"]:
        if x["t"] > t:
            break
        d = x
    return d


# ---------------------------------------------------------------- replay page
def page_replay():
    data = load_replay()
    if not data:
        st.error("bench/replay.json not found. Run `python export_replay.py` first "
                 "(it needs `make forward-prom` running).")
        return

    runs = {r["name"]: r for r in data["runs"]}
    pairs = [("A1r", "B1r"), ("A2r", "B2r"), ("A3r", "B3r")]

    st.title("Watch the pods arrive early")
    st.caption("The same traffic, sent twice. Left: Kubernetes' built-in autoscaler, "
               "which reacts to CPU. Right: a forecast that scales ahead of the load. "
               "Every number was recorded during a real 20-minute run.")

    c1, c2 = st.columns([1, 3])
    with c1:
        which = st.selectbox("Which run", [1, 2, 3], format_func=lambda i: f"Run {i}")
    a, b = (runs.get(n) for n in pairs[which - 1])
    if not (a and b):
        st.error("That run is missing from replay.json.")
        return

    with c2:
        t = st.slider("Minute of the run", 0, RUN_SECONDS, 0, step=20,
                      format="%d s", label_visibility="visible")

    # Play steps the slider forward by re-running the script. Streamlit has no
    # animation loop, so this is the honest way to do it — and the slider stays
    # draggable, which matters more than smoothness for reading the numbers.
    if st.button("▶ Play from here", disabled=t >= RUN_SECONDS):
        for nxt in range(t, RUN_SECONDS + 1, 20):
            st.session_state["t"] = nxt
            time.sleep(0.05)
        st.rerun()

    phase = ("Steady traffic. Both sit at the 2-pod minimum." if t < 240 else
             "**The ramp.** Traffic climbs 20 → 80 req/s. Watch the right side add pods "
             "while it is still rising." if t < 600 else
             "**The plateau.** Traffic is at its peak. The baseline finally reaches 3 pods — "
             "but its response times already climbed." if t < 840 else
             "Winding down. Both release pods.")
    st.info(f"**Minute {t // 60}:{t % 60:02d}** — {phase}")

    left, right = st.columns(2)
    for col, run, name, colour in ((left, a, "Baseline — Kubernetes HPA", BASE),
                                   (right, b, "Predictive — forecast", PRED)):
        with col:
            st.subheader(name)
            rate = value_at(run, "rate", t) or 0
            pods = value_at(run, "pods", t) or 0
            p99 = value_at(run, "p99", t)
            m1, m2, m3 = st.columns(3)
            m1.metric("Traffic in", f"{rate:.0f}/s")
            m2.metric("Pods running", pods)
            m3.metric("Slowest 1%", f"{p99} ms" if p99 else "–")
            # One block per pod: the clearest possible "did capacity arrive yet".
            st.markdown(
                "".join(f"<span style='display:inline-block;width:26px;height:34px;"
                        f"margin:0 4px 4px 0;border-radius:3px;background:{colour}'></span>"
                        for _ in range(int(pods))) or "<i>no pods</i>",
                unsafe_allow_html=True)

            d = decision_at(run, t)
            if d:
                st.caption(f"Model: traffic now **{d['now']:.0f}/s**, expects "
                           f"**{d['pred']:.0f}/s** in 60 s → wants **{d['pods_target']} pods**"
                           + ("  ·  **adding a pod now**" if d["action"] == "scale_up" else ""))
            elif run["arm"] == "baseline":
                st.caption("No forecast — this version only reacts to what already happened.")

    # ---- charts, drawn only up to the playhead so the run unfolds -----------
    st.divider()
    frames = []
    for run, label in ((a, "Baseline"), (b, "Predictive")):
        for key in ("p99", "pods", "rate"):
            df = series(run, key)
            df = df[df.t <= t].rename(columns={key: "value"})
            df["metric"], df["arm"] = key, label
            frames.append(df)
    long = pd.concat(frames, ignore_index=True)
    scale = alt.Scale(domain=["Baseline", "Predictive"], range=[BASE, PRED])

    titles = {"p99": "Response time of the slowest 1% (ms)",
              "pods": "Pods running",
              "rate": "Requests arriving per second"}
    for key in ("p99", "pods", "rate"):
        sub = long[long.metric == key]
        if sub.empty:
            continue
        chart = (alt.Chart(sub)
                 .mark_line(interpolate="step-after" if key == "pods" else "linear",
                            strokeWidth=2)
                 .encode(
                     x=alt.X("t:Q", title="seconds into run",
                             scale=alt.Scale(domain=[0, RUN_SECONDS])),
                     y=alt.Y("value:Q", title=None),
                     color=alt.Color("arm:N", scale=scale, title=None),
                     tooltip=["arm", "t", "value"])
                 .properties(height=170, title=titles[key]))
        st.altair_chart(chart, use_container_width=True)

    # ---- verdict ------------------------------------------------------------
    st.divider()
    st.subheader("What this run measured")
    sa, sb = a["summary"], b["summary"]
    st.dataframe(pd.DataFrame([
        {"Version": "Baseline (HPA)", "Slowest 1%": f"{sa['p99']} ms",
         "Typical": f"{sa['p50']} ms", "Computing used": f"{sa['pod_seconds']:,} pod-s"},
        {"Version": "Predictive", "Slowest 1%": f"{sb['p99']} ms",
         "Typical": f"{sb['p50']} ms", "Computing used": f"{sb['pod_seconds']:,} pod-s"},
    ]), hide_index=True, use_container_width=True)

    lat = (1 - sb["p99"] / sa["p99"]) * 100
    cost = (sb["pod_seconds"] / sa["pod_seconds"] - 1) * 100
    st.markdown(
        f"The slowest 1% of responses were **{lat:.0f}% faster** with the forecast "
        f"({sa['p99']} ms → {sb['p99']} ms), using **{cost:+.0f}% computing**. "
        "Both numbers matter — being faster by running unlimited servers is not an improvement.")
    st.caption("Averaged over three runs per version: 479 ms vs 183 ms. On a spike that "
               "arrives instantly with no warning, the forecast shows no advantage — there "
               "is nothing to predict from.")


# ---------------------------------------------------------------- live page
@st.cache_resource
def load_model():
    import joblib
    p = ROOT / "models/forecaster.joblib"
    return joblib.load(p) if p.exists() else None


@st.cache_data(ttl=30)
def prometheus_reachable() -> bool:
    """Cheap probe, so the page can explain itself instead of throwing.

    On Streamlit Cloud this is always False: Prometheus runs on the laptop that
    ran the experiment. Saying so plainly is better than showing a visitor a
    connection error they cannot act on.
    """
    try:
        import requests
        return requests.get("http://localhost:9090/-/healthy", timeout=2).status_code == 200
    except Exception:
        return False


def page_live():
    st.title("Live forecast")

    if not prometheus_reachable():
        st.info(
            "**This page only works on the machine running the cluster.**\n\n"
            "It reads Prometheus at `localhost:9090` and asks the trained model what "
            "traffic is coming in the next 60 seconds. Prometheus is not reachable from "
            "here, so there is nothing live to read.\n\n"
            "Everything the project measured is on the **Benchmark replay** page, which "
            "needs nothing running.")
        with st.expander("What this page shows when it is running"):
            st.markdown(
                "- current request rate, straight from Prometheus\n"
                "- what the model expects 60 seconds ahead, and the difference\n"
                "- the pod count that implies, at the measured 20 req/s per pod\n"
                "- the last 30 minutes charted, with the forecast as a dashed line\n"
                "- a **hold** notice when recent history has gaps — the model declining "
                "to answer rather than guessing\n\n"
                "To run it yourself: `make forward-prom`, `make load-start`, then `make ui`.")
        return

    st.caption("Reads Prometheus and the trained model right now.")

    bundle = load_model()
    if not bundle:
        st.error("models/forecaster.joblib not found. Run `python src/train_final.py`.")
        return

    try:
        import numpy as np
        import live
    except Exception as e:
        st.error(f"Could not import the live path: {type(e).__name__}: {e}")
        return

    auto = st.toggle("Refresh every 15 seconds", value=False)

    try:
        df = live.fetch_recent()
        row, now_rate = live.latest_feature_row(df, bundle["horizon"])
    except Exception as e:
        st.error(f"Could not reach Prometheus at localhost:9090 — is `make forward-prom` "
                 f"running?\n\n`{type(e).__name__}: {e}`")
        return

    if row is None:
        # Not a crash: live.py refuses to answer when the recent window has holes,
        # and showing that refusal is more useful than hiding it.
        st.warning("**Holding.** The last 30 minutes of history has gaps, so the model "
                   "declines to predict. The controller would leave the replica count "
                   "alone and let the HPA cover. Common cause: the laptop slept, or "
                   "traffic has been stopped.")
        st.caption(f"Prometheus returned {len(df)} samples.")
        return

    X = row.reindex(columns=bundle["features"])
    pred = float(np.clip(bundle["model"].predict(X)[0], 0, None))
    ahead = bundle["horizon"] * 15
    capacity, headroom = 20.0, 1.1
    want = max(2, min(20, int(-(-pred * headroom // capacity))))

    c1, c2, c3 = st.columns(3)
    c1.metric("Traffic now", f"{now_rate:.1f}/s")
    c2.metric(f"Expected in {ahead}s", f"{pred:.1f}/s", f"{pred - now_rate:+.1f}")
    c3.metric("Pods this needs", want)

    hist = df.tail(120).copy()
    hist["when"] = "actual"
    chart = (alt.Chart(hist).mark_line(color=PRED, strokeWidth=2)
             .encode(x=alt.X("ts:T", title=None), y=alt.Y("y:Q", title="requests / second"),
                     tooltip=["ts:T", "y:Q"])
             .properties(height=220, title="Last 30 minutes"))
    rule = alt.Chart(pd.DataFrame({"y": [pred]})).mark_rule(
        color=BASE, strokeDash=[4, 4], strokeWidth=2).encode(y="y:Q")
    st.altair_chart(chart + rule, use_container_width=True)
    st.caption(f"Dashed line is the forecast for {ahead} seconds from now. "
               "If it simply tracks the current value, the model is behaving like the "
               "naive baseline and something upstream is wrong.")

    log = ROOT / "logs/decisions.csv"
    if log.exists():
        st.subheader("Recent controller decisions")
        d = pd.read_csv(log).tail(12).iloc[::-1]
        st.dataframe(d, hide_index=True, use_container_width=True)

    if auto:
        time.sleep(15)
        st.rerun()


# ---------------------------------------------------------------- shell
page = st.sidebar.radio("View", ["Benchmark replay", "Live forecast"])
st.sidebar.divider()
st.sidebar.markdown(
    "**Predictive autoscaling**\n\n"
    "Forecast the request rate 60 s ahead and add pods before the traffic arrives.\n\n"
    "- pod start-up: **19 s** (measured)\n"
    "- one pod handles: **20 req/s** (measured)\n"
    "- backtest: **64.5%** below the naive baseline\n"
    "- benchmark: **p99 62% lower**, +28% compute")

page_replay() if page == "Benchmark replay" else page_live()
