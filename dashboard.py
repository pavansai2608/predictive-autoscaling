"""The UI. Two pages: replay a recorded benchmark, or watch the model live.

    pip install -r requirements.txt
    streamlit run dashboard.py

REPLAY reads bench/replay.json (the ramp) and bench/replay-step.json (the instant
spike) — benchmark runs frozen out of Prometheus by export_replay.py. It needs no
cluster and works forever, which matters because Prometheus keeps only 15 days.
A scenario whose file is absent is simply not offered.

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

# Amber = reactive, cyan = predictive, everywhere. Matches
# chartCategoricalColors in .streamlit/config.toml so Altair, the metric rails
# and the pod blocks all agree without any of them being told twice.
BASE  = "#f0873f"     # baseline / HPA
PRED  = "#3fa9f5"     # predictive owns the replica count
FLOOR = "#4ad991"     # predictive raises the HPA's floor — the composition
DIM   = "#8b95a6"
RUN_SECONDS = 1200    # every benchmark run is 20 minutes

# A run's name prefix is the ONLY record of which arm it was: `make bench RUN=C1`
# writes bench/C1.json and nothing in it says MODE=hpa-floor. This table is the
# decoder, and it has a twin in export_replay.ARM_OF_PREFIX — change both.
ARMS = {
    "A": ("Baseline", BASE, "reacts to cpu"),
    "B": ("Predictive", PRED, "owns the replica count"),
    "C": ("Predictive + floor", FLOOR, "raises the hpa's minimum"),
}

# Phase boundaries are read off the k6 stage lists in load/ramp.js and
# load/benchmark.js — not eyeballed from the charts. If a stage duration
# changes there, these are wrong and the narration lies about the run.
SCENARIOS = {
    "Gradual ramp": {
        "file": "replay.json",
        "title": "Watch the pods arrive early",
        "sub": "The same traffic, sent twice. Kubernetes' built-in autoscaler reacts to "
               "CPU that has already risen. The forecast scales ahead of it. Every figure "
               "below was recorded during a real run.",
        "phases": [
            (240, "Steady traffic. Every arm sits at the 2-pod minimum."),
            (600, "**The ramp.** Traffic climbs 20 → 80 req/s over six minutes. Watch the "
                  "forecasting arms add pods while it is still rising."),
            (840, "**The plateau.** Traffic is at its peak. The baseline finally reaches "
                  "3 pods — but its response times already climbed."),
            (RUN_SECONDS + 1, "Winding down. Every arm releases pods."),
        ],
    },
    "Instant spike": {
        "file": "replay-step.json",
        "title": "The spike nothing could see coming",
        "sub": "A 4x step in one second, with no precursor in the traffic. There is nothing "
               "here for a forecaster to predict — so this page is the honest half of the "
               "project. It shows where forecasting alone LOSES, and what fixed it.",
        "phases": [
            (300, "Steady at 20 req/s. Nothing in this traffic hints at what is coming."),
            (540, "**The step.** 20 → 80 req/s instantly. No arm had warning; what "
                  "separates them now is only how fast capacity arrives."),
            (RUN_SECONDS + 1, "**Recovery.** Traffic is back to 20/s. This is where the "
                  "forecast-only arm lost: it withdrew pods while the spike was still "
                  "running. The floor arm cannot — lowering a floor only permits the HPA "
                  "to shrink, and the HPA declines while CPU is high."),
        ],
    },
}

st.set_page_config(page_title="Predictive Autoscaling", page_icon="📈",
                   layout="wide", initial_sidebar_state="expanded")


def inject_style():
    """Fonts and the handful of things the theme config cannot reach.

    Kept deliberately small. Streamlit's own theme system handles colour, radius
    and font family; this covers the type scale, the eyebrow labels, the metric
    rails and the pod gauge — none of which have config equivalents.
    """
    st.html("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap">
<style>
  /* ---- the ground ---------------------------------------------------
     Same #0f1319, but built up in layers instead of left flat:

       1. a cyan bloom top-left and an amber bloom top-right — the two arms,
          bleeding in from the edges rather than sitting anywhere specific
       2. graph paper: a 120px major grid over a 24px minor grid, both at
          very low alpha. This is an instrument for reading measurements, so
          the surface it sits on is ruled like one.
       3. a floor vignette so the page has a bottom rather than fading out

     background-attachment:fixed keeps the grid still while content scrolls,
     which reads as a panel you are looking THROUGH rather than a texture
     glued to the content.
  ------------------------------------------------------------------- */
  .stApp{
    background-color:#0f1319;
    background-image:
      radial-gradient(1100px 620px at 8% -8%,  rgba(63,169,245,.15), transparent 58%),
      radial-gradient(900px  520px at 96% -4%, rgba(240,135,63,.10), transparent 60%),
      radial-gradient(1200px 700px at 50% 118%, rgba(6,9,14,.85),    transparent 62%),
      linear-gradient(rgba(150,180,220,.030) 1px, transparent 1px),
      linear-gradient(90deg, rgba(150,180,220,.030) 1px, transparent 1px),
      linear-gradient(rgba(150,180,220,.013) 1px, transparent 1px),
      linear-gradient(90deg, rgba(150,180,220,.013) 1px, transparent 1px);
    background-size:
      auto, auto, auto,
      120px 120px, 120px 120px,
      24px 24px, 24px 24px;
    background-attachment:fixed;
  }

  /* Panels float over the grid instead of hiding it. The inset highlight is
     a single hairline of light on the top edge — the thing that separates a
     surface from a coloured rectangle. */
  [data-testid="stMetric"], .stDataFrame, [data-testid="stAlert"]{
    background:rgba(19,26,36,.74) !important;
    backdrop-filter:blur(3px);
    box-shadow:inset 0 1px 0 rgba(255,255,255,.045);
  }

  section[data-testid="stSidebar"]{
    background-image:linear-gradient(180deg, rgba(63,169,245,.055), transparent 240px);
    border-right:1px solid #1b2431;
  }

  /* ---- type scale -------------------------------------------------- */
  .stApp h1{
    font-weight:700; font-size:2.45rem; line-height:1.05;
    letter-spacing:-.025em; margin-bottom:.35rem;
  }
  .stApp h2{font-weight:600; font-size:1.35rem; letter-spacing:-.012em}
  .stApp h3{font-weight:600; font-size:1.05rem; letter-spacing:-.008em}

  /* Every figure in the app is monospace so columns of digits line up and
     a number changing does not reflow the text beside it. */
  [data-testid="stMetricValue"], .stDataFrame, code, .mono{
    font-family:"JetBrains Mono", ui-monospace, monospace !important;
    font-variant-numeric:tabular-nums;
  }

  /* ---- eyebrow: a small uppercase label above a section ------------- */
  .eyebrow{
    font-family:"JetBrains Mono", monospace; font-size:.66rem;
    letter-spacing:.19em; text-transform:uppercase; color:#7d8798;
    display:block; margin:0 0 .3rem;
  }

  /* ---- masthead ----------------------------------------------------- */
  .masthead{
    padding:.2rem 0 1.2rem; margin-bottom:1.4rem; position:relative;
  }
  /* A rule that fades out reads as a horizon; a flat 1px border reads as a
     table cell. Cyan at the left because that is the arm the page argues for. */
  .masthead::after{
    content:""; position:absolute; left:0; right:0; bottom:0; height:1px;
    background:linear-gradient(90deg, #3fa9f5 0%, #26303f 22%, transparent 78%);
  }
  .masthead .sub{color:#9aa5b5; font-size:1.02rem; max-width:64ch; margin:.15rem 0 0}
  .headline{
    display:flex; gap:2.2rem; flex-wrap:wrap; margin-top:1.1rem;
  }
  .headline .fig{border-left:2px solid #26303f; padding-left:.85rem}
  .headline .fig b{
    font-family:"JetBrains Mono", monospace; font-size:1.5rem; font-weight:600;
    display:block; line-height:1.15; font-variant-numeric:tabular-nums;
  }
  .headline .fig span{font-size:.72rem; color:#7d8798; letter-spacing:.03em}
  .fig.amber b{color:#f0873f} .fig.amber{border-left-color:#f0873f}
  .fig.cyan  b{color:#3fa9f5} .fig.cyan{border-left-color:#3fa9f5}

  /* ---- arm panels: a coloured rail is the fastest possible label ----- */
  .armhead{
    display:flex; align-items:baseline; gap:.6rem; padding:.55rem 0 .55rem .8rem;
    border-left:3px solid var(--rail); margin-bottom:.7rem;
  }
  .armhead b{font-size:1.02rem; font-weight:600; color:var(--rail)}
  .armhead span{font-family:"JetBrains Mono",monospace; font-size:.66rem;
                letter-spacing:.13em; text-transform:uppercase; color:#7d8798}

  /* ---- pod gauge: filled slots against a fixed frame ---------------- */
  .pods{display:flex; gap:4px; align-items:flex-end; height:46px; margin:.1rem 0 .2rem}
  .pods i{
    width:22px; border-radius:2px; display:block;
    border:1px solid #26303f; background:transparent; height:46px;
  }
  .pods i.on{border-color:transparent}
  /* Lit slots glow slightly in their own colour, so a pod appearing registers
     out of the corner of the eye while you are reading the chart below. */
  .pods i.on{box-shadow:0 0 10px -1px currentColor}
  /* Unfilled slots stay visible so "3 of a possible 8" is legible at a
     glance — a bare count of blocks hides how much headroom is left. */

  /* ---- metrics ------------------------------------------------------ */
  [data-testid="stMetric"]{
    background:#141b25; border:1px solid #222c3a; border-radius:4px;
    padding:.6rem .8rem;
  }
  [data-testid="stMetricLabel"] p{
    font-size:.68rem !important; letter-spacing:.13em; text-transform:uppercase;
    color:#7d8798 !important;
  }

  /* ---- chrome ------------------------------------------------------- */
  [data-testid="stSidebarNav"], footer, #MainMenu{visibility:hidden}
  .stSlider [data-baseweb="slider"]{padding-top:.2rem}
  hr{border-color:#222c3a !important; margin:1.1rem 0 !important}
</style>""")


def pod_gauge(n: int, colour: str, slots: int = 8) -> str:
    """n filled slots out of `slots`, so headroom is visible, not implied."""
    n = int(n or 0)
    return ('<div class="pods">'
            # color as well as background: the CSS glow uses currentColor, so
            # each lit slot haloes in its own arm colour rather than in ink.
            + "".join(f'<i class="on" style="background:{colour};color:{colour}"></i>'
                      for _ in range(min(n, slots)))
            + "".join('<i></i>' for _ in range(max(0, slots - n)))
            + "</div>")


# ---------------------------------------------------------------- data
@st.cache_data
def load_replay(filename: str) -> dict | None:
    p = ROOT / "bench" / filename
    return json.loads(p.read_text()) if p.exists() else None


def group_runs(data: dict) -> dict[str, dict[str, dict]]:
    """{run number: {arm prefix: run}} — runs pair up by the digit in their name.

    A1/B1/C1 are the same traffic sent three times, so they belong side by side;
    A1 vs B2 would compare two different 20-minute windows.
    """
    out: dict[str, dict[str, dict]] = {}
    for r in data["runs"]:
        out.setdefault(r["name"][1], {})[r["name"][0]] = r
    return dict(sorted(out.items()))


def arm_means(data: dict) -> dict[str, dict[str, float]]:
    """Mean p99 and pod-seconds per arm — the same mean analyze.py prints.

    Averaged here rather than hardcoded so the headline follows the data when a
    scenario is switched. Three stale numbers in the masthead would be worse
    than none, and this file used to carry exactly that.
    """
    acc: dict[str, list[dict]] = {}
    for r in data["runs"]:
        acc.setdefault(r["name"][0], []).append(r["summary"])
    return {p: {k: sum(s[k] for s in v) / len(v) for k in ("p99", "pod_seconds")}
            for p, v in acc.items()}


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
    available = [n for n, s in SCENARIOS.items()
                 if (ROOT / "bench" / s["file"]).exists()]
    if not available:
        st.error("No replay file found in bench/. Run `make replay-data` first "
                 "(it needs `make forward-prom` running).")
        return

    top = st.columns([2, 1, 3])
    with top[0]:
        scen_name = st.radio("Scenario", available, horizontal=True)
    scen = SCENARIOS[scen_name]
    data = load_replay(scen["file"])
    grouped = group_runs(data)
    means = arm_means(data)

    # ---- masthead: every figure below is a mean over that arm's runs --------
    figs = "".join(
        f'<div class="fig" style="border-left-color:{ARMS[p][1]}">'
        f'<b style="color:{ARMS[p][1]}">{means[p]["p99"]:.0f} ms</b>'
        f'<span>{ARMS[p][0].upper()} &mdash; SLOWEST 1%</span></div>'
        for p in ARMS if p in means)
    # The winner is whichever non-baseline arm has the lowest p99 — picked from
    # the data, not asserted. On the step scenario that is the floor arm; on the
    # ramp there is only one candidate.
    rivals = [p for p in means if p != "A"]
    if rivals and "A" in means:
        best = min(rivals, key=lambda p: means[p]["p99"])
        lat = (1 - means[best]["p99"] / means["A"]["p99"]) * 100
        cost = (means[best]["pod_seconds"] / means["A"]["pod_seconds"] - 1) * 100
        figs += (f'<div class="fig"><b>{lat:.0f}%</b><span>FASTER &mdash; BEST ARM</span></div>'
                 f'<div class="fig"><b>{cost:+.0f}%</b><span>COMPUTE</span></div>')

    st.html(f"""
<div class="masthead">
  <span class="eyebrow">Recorded benchmark &middot; 20 minutes &middot;
    {len(grouped)} runs per arm &middot; {data["scenario"]}</span>
  <h1>{scen["title"]}</h1>
  <p class="sub">{scen["sub"]}</p>
  <div class="headline">{figs}</div>
</div>""")

    with top[1]:
        which = st.selectbox("Which run", list(grouped),
                             format_func=lambda i: f"Run {i}")
    arms = grouped[which]

    # No key= on the slider: with a key, Streamlit restores the widget from its
    # own stored state and ignores `value` on every rerun, so Play could never
    # move it. Keyless + explicit value means the playhead is ours to set.
    with top[2]:
        t = st.slider("Minute of the run", 0, RUN_SECONDS,
                      value=st.session_state.get("t", 0), step=20, format="%d s")
    st.session_state["t"] = t

    # Streamlit has no animation loop, so playing means: draw one frame, sleep,
    # advance, rerun. The advance happens at the BOTTOM of this function, after
    # the charts exist — stepping here would redraw the old frame first.
    playing = st.toggle("▶ Play", value=False, disabled=t >= RUN_SECONDS)

    phase = next(text for until, text in scen["phases"] if t < until)
    st.info(f"**Minute {t // 60}:{t % 60:02d}** — {phase}")

    present = [p for p in ARMS if p in arms]
    for col, prefix in zip(st.columns(len(present)), present):
        run = arms[prefix]
        name, colour, kind = ARMS[prefix]
        with col:
            st.html(f'<div class="armhead" style="--rail:{colour}">'
                    f'<b>{name}</b><span>{kind}</span></div>')
            rate = value_at(run, "rate", t) or 0
            pods = value_at(run, "pods", t) or 0
            p99 = value_at(run, "p99", t)
            st.html(pod_gauge(pods, colour))
            m1, m2, m3 = st.columns(3)
            m1.metric("Traffic in", f"{rate:.0f}/s")
            m2.metric("Pods", pods)
            m3.metric("Slowest 1%", f"{p99} ms" if p99 else "–")

            d = decision_at(run, t)
            if d:
                # The two forecasting arms act through different levers, and the
                # caption has to say which — "adding a pod" would be a lie in
                # floor mode, where the controller only ever moves minReplicas
                # and the HPA decides whether a pod actually appears.
                act = {"scale_up": "  ·  **adding a pod now**",
                       "floor_up": "  ·  **raising the hpa's floor now**",
                       }.get(d["action"], "")
                st.caption(f"Model: traffic now **{d['now']:.0f}/s**, expects "
                           f"**{d['pred']:.0f}/s** in 60 s → wants **{d['pods_target']} pods**"
                           + act)
            elif run["arm"] == "baseline":
                st.caption("No forecast — this version only reacts to what already happened.")

    # ---- charts, drawn only up to the playhead so the run unfolds -----------
    st.divider()
    frames = []
    for prefix in present:
        for key in ("p99", "pods", "rate"):
            df = series(arms[prefix], key)
            df = df[df.t <= t].rename(columns={key: "value"})
            df["metric"], df["arm"] = key, ARMS[prefix][0]
            frames.append(df)
    long = pd.concat(frames, ignore_index=True)
    # The scale is passed explicitly rather than left to Altair's default order:
    # an arm must keep its colour when a scenario has two arms instead of three,
    # or the reader relearns the legend every time they switch pages.
    scale = alt.Scale(domain=[ARMS[p][0] for p in present],
                      range=[ARMS[p][1] for p in present])

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
    st.dataframe(pd.DataFrame([
        {"Version": ARMS[p][0],
         "Slowest 1%": f"{arms[p]['summary']['p99']} ms",
         "Typical": f"{arms[p]['summary']['p50']} ms",
         "Computing used": f"{arms[p]['summary']['pod_seconds']:,} pod-s"}
        for p in present]), hide_index=True, use_container_width=True)

    # Pod-seconds sits in the same sentence as latency, never in a footnote: a
    # latency win bought with unlimited compute is not a win, and hiding the
    # cost side is the easiest way to make a benchmark dishonest.
    sa = arms["A"]["summary"] if "A" in arms else None
    if sa:
        for p in present:
            if p == "A":
                continue
            s = arms[p]["summary"]
            lat = (1 - s["p99"] / sa["p99"]) * 100
            cost = (s["pod_seconds"] / sa["pod_seconds"] - 1) * 100
            st.markdown(
                f"**{ARMS[p][0]}** — the slowest 1% of responses were "
                f"**{lat:.0f}% faster** than the baseline "
                f"({sa['p99']} ms → {s['p99']} ms), using **{cost:+.0f}% computing**.")

    st.caption(
        "Figures above are this single run; the masthead averages all "
        f"{len(grouped)} runs per arm. A negative 'faster' is a real result, "
        "reported rather than dropped.")

    # One frame per rerun, advanced only once the whole page above has drawn.
    # The sleep is what makes it watchable rather than a flicker; the slider
    # stays draggable throughout, which matters more than smoothness because
    # the point is reading the numbers at a chosen instant.
    if playing and t < RUN_SECONDS:
        time.sleep(0.4)
        st.session_state["t"] = min(RUN_SECONDS, t + 20)
        st.rerun()


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
inject_style()

page = st.sidebar.radio("View", ["Benchmark replay", "Live forecast"])
st.sidebar.divider()
st.sidebar.html("""
<span class="eyebrow">Measured on this cluster</span>

<div style="font-family:'JetBrains Mono',monospace;font-size:.78rem;line-height:2;
            font-variant-numeric:tabular-nums">
<span style="color:#7d8798">pod start-up</span>
<b style="float:right">19 s</b><br>
<span style="color:#7d8798">one pod serves</span>
<b style="float:right">20 req/s</b><br>
<span style="color:#7d8798">forecast horizon</span>
<b style="float:right">60 s</b><br>
<span style="color:#7d8798">history collected</span>
<b style="float:right">51 h</b><br>
<span style="color:#7d8798">vs naive baseline</span>
<b style="float:right;color:#3fa9f5">-64.5%</b>
</div>

<span class="eyebrow" style="margin-top:1.2rem">The claim</span>

<div style="font-size:.82rem;color:#9aa5b5;line-height:1.55">
Forecast the request rate 60&nbsp;s ahead and add pods <i>before</i> the traffic arrives.
On a gradual ramp that cuts the slowest 1% of responses by
<b style="color:#3fa9f5">62%</b> for <b>28%</b> more compute.<br><br>
On an instant spike the forecast alone is <b>worse</b> than the HPA &mdash; it withdraws
capacity while the spike is still running. Letting it raise the HPA's <i>floor</i> instead
of owning the replica count fixes that: <b style="color:#4ad991">49%</b> better than the
HPA alone, for 43% more compute.
</div>
""")

page_replay() if page == "Benchmark replay" else page_live()
