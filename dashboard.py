"""The UI. Three views: what the project found, a recorded benchmark, the live model.

    pip install -r requirements.txt
    streamlit run dashboard.py        (or: make ui)

OVERVIEW answers "what did this measure?" with no controls at all. It exists
because the replay page cannot: that page needs you to already know what an arm
is, what a run is, and which scenario you care about before a single number
means anything. Leading with controls asks the reader to work before they are
told why.

REPLAY reads bench/replay.json (the ramp) and bench/replay-step.json (the instant
spike) — benchmark runs frozen out of Prometheus by export_replay.py. It needs no
cluster and works forever, which matters because Prometheus keeps only 15 days.
A scenario whose file is absent is simply not offered.

LIVE reads Prometheus and the trained model directly. It needs `make forward-prom`
running, and it is the view that would have caught the two train/serve bugs
months earlier: it shows the forecast beside what actually happened next.

Nothing here computes a new result. Means over runs are the same means analyze.py
prints; every other figure is read straight from the frozen recordings.
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

# --- design tokens -----------------------------------------------------------
# Drafting paper, not a dashboard shell. Two earlier attempts failed for the same
# reason from opposite directions: the first was near-black with a blue accent and
# Inter (the default dark-SaaS look), the second borrowed a sidebar-app layout
# wholesale. This one is laid out as a technical document — masthead across the
# top, a spec strip of measured constants, then content in one measure.
PAPER   = "#e8edee"   # cool blue-grey stock, the colour of drafting film
CARD    = "#ffffff"
INK     = "#101619"   # 15.5:1 on the stock
MUTED   = "#4d565a"   # 6.4:1  — body copy
FAINT   = "#5d666a"   # 5.0:1  — captions and labels, still AA body
RULE    = "#c8d1d3"   # hairlines only, never text

# The three arms, keyed the way a printed figure keys its series: dark enough to
# read as ink, far apart in hue, and all clearing 5:1 on both the stock and the
# card fill. Deliberately not the palette of any reference project.
BASE  = "#8c2f39"     # stock HPA — reactive
PRED  = "#15616d"     # predictive owns the replica count
FLOOR = "#4a6b2a"     # predictive raises the HPA's floor — the composition

RUN_SECONDS = 1200    # every benchmark run is 20 minutes

# The measured constants, shown as a spec strip under the masthead rather than
# stacked in a sidebar. Every one of these is in CLAUDE.md and was measured on
# the cluster; none is an estimate.
SPECS = [("pod start-up", "19 s"), ("one pod serves", "20 req/s"),
         ("horizon", "60 s"), ("history", "51 h"), ("vs naive", "-64.5%")]

# A run's name prefix is the ONLY record of which arm it was: `make bench RUN=C1`
# writes bench/C1.json and nothing in it says MODE=hpa-floor. This table is the
# decoder, and it has a twin in export_replay.ARM_OF_PREFIX — change both.
#
# Line dashes are carried alongside the colours so the three series stay
# separable in a greyscale print, for a red-green colourblind reader, and — the
# common case here — wherever two arms sit on top of each other.
ARMS = {
    "A": ("Stock HPA", BASE, "scales on CPU it has already seen", [1, 0]),
    "B": ("Predictive", PRED, "forecast sets the replica count", [7, 3]),
    "C": ("Predictive + floor", FLOOR, "forecast sets the HPA's minReplicas", [2, 2]),
}

# Phase boundaries are read off the k6 stage lists in load/ramp.js and
# load/benchmark.js — not eyeballed from the charts. If a stage duration
# changes there, these are wrong and the narration lies about the run.
SCENARIOS = {
    "Gradual ramp": {
        "file": "replay.json",
        "blurb": "Traffic climbs 20 to 80 req/s over six minutes. The rise is visible "
                 "in the request rate before it hurts, so a forecaster has something "
                 "to work with.",
        "phases": [
            (240, "Steady traffic. Every arm sits at the 2-pod minimum."),
            (600, "The ramp. Traffic climbs 20 to 80 req/s. Watch the forecasting arms "
                  "add pods while it is still rising."),
            (840, "The plateau. Traffic is at its peak. The stock HPA finally reaches "
                  "3 pods — but its response times already climbed."),
            (RUN_SECONDS + 1, "Winding down. Every arm releases pods."),
        ],
    },
    "Instant spike": {
        "file": "replay-step.json",
        "blurb": "A 4x step in one second, with no precursor in the traffic. There is "
                 "nothing to predict from — this is the scenario that shows what "
                 "forecasting alone cannot do.",
        "phases": [
            (300, "Steady at 20 req/s. Nothing in this traffic hints at what is coming."),
            (540, "The step. 20 to 80 req/s instantly. No arm had warning; what separates "
                  "them now is only how fast capacity arrives."),
            (RUN_SECONDS + 1, "Recovery. This is where the forecast-only arm lost — it "
                  "withdrew pods while the spike was still running. The floor arm cannot: "
                  "lowering minReplicas only permits the HPA to shrink, and it declines "
                  "while CPU is high."),
        ],
    },
}

st.set_page_config(page_title="Predictive Autoscaling", page_icon="📄",
                   layout="wide", initial_sidebar_state="collapsed")


# ---------------------------------------------------------------- style
def inject_style():
    """The design system, in one block so the tokens live in one place.

    NOTE FOR ANYONE EDITING THIS: an opening angle bracket followed by a letter
    anywhere below — in a url(), or even inside a comment — makes Streamlit
    discard the whole style element, and an unbalanced comment delimiter breaks
    every rule after it. Both failures are silent and total.
    """
    st.html("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
  :root{
    --paper:#e8edee; --card:#ffffff; --stone:#dde4e5;
    --ink:#101619; --muted:#4d565a; --faint:#5d666a;
    --rule:#c8d1d3; --rule-soft:#d8e0e1;
    --base:#8c2f39; --pred:#15616d; --floor:#4a6b2a;
    --serif:"Newsreader",Georgia,"Times New Roman",serif;
    --sans:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,monospace;
    --focus:#15616d;
  }

  /* Set the face ONCE and let it inherit. A blanket rule over span and div also
     hits the Material icon spans, whose glyphs are ligatures — overriding those
     renders expander chevrons as the literal word keyboard_arrow_right. */
  .stApp{ background:var(--paper); font-family:var(--sans); color:var(--ink); }
  .block-container{ padding-top:1.6rem; padding-bottom:6rem; max-width:1180px; }

  /* There is no sidebar in this layout. Navigation lives in the masthead, so
     the collapsed rail and its expand arrow would be a control leading nowhere. */
  section[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"],
  [data-testid="stSidebarNav"], footer, #MainMenu, [data-testid="stDecoration"],
  [data-testid="stToolbar"], [data-testid="stStatusWidget"],
  [data-testid="stElementToolbar"]{ display:none !important; }

  /* ---- type -----------------------------------------------------------
     Everything you READ is the serif; everything you MEASURE is the mono.
     That split is the whole typographic idea, and it is why the two faces
     never have to compete for the same job.                              */
  .stApp h1, .stApp h2, .stApp h3{ font-family:var(--serif); color:var(--ink); }
  .stApp h1{ font-size:3rem; font-weight:500; letter-spacing:-.015em;
             line-height:1.1; margin:0 0 .6rem; }
  .stApp h2{ font-size:1.75rem; font-weight:500; letter-spacing:-.01em;
             margin:0 0 .25rem; }
  .stApp h3{ font-size:1.1rem; font-weight:600; }

  [data-testid="stMetricValue"], .stDataFrame, code, .mono, .statv, .armstats b{
    font-family:var(--mono) !important; font-variant-numeric:tabular-nums;
  }
  code{ background:var(--stone); padding:.1em .35em; border-radius:3px;
        font-size:.88em; color:var(--ink); }

  .eyebrow{
    font-family:var(--mono); font-size:.66rem; font-weight:500;
    letter-spacing:.1em; text-transform:uppercase; color:var(--faint);
    display:block; margin:0 0 .4rem;
  }

  /* ---- masthead -------------------------------------------------------
     A document head, not an app shell: heavy rule, wordmark on the left,
     provenance on the right. This replaces the sidebar entirely.        */
  .mast{
    border-top:3px solid var(--ink); border-bottom:1px solid var(--ink);
    padding:.75rem 0 .7rem; margin:0 0 0;
    display:flex; align-items:baseline; justify-content:space-between;
    gap:1.5rem; flex-wrap:wrap;
  }
  .mast .wordmark{
    font-family:var(--serif); font-size:1.32rem; font-weight:600;
    letter-spacing:-.01em; color:var(--ink);
  }
  .mast .prov{
    font-family:var(--mono); font-size:.64rem; letter-spacing:.1em;
    text-transform:uppercase; color:var(--faint);
  }

  /* ---- spec strip: the measured constants, read across ---------------- */
  .spec{
    display:flex; flex-wrap:wrap; gap:.3rem 1.9rem;
    border-bottom:1px solid var(--ink); padding:.6rem 0 .65rem; margin:0 0 2.4rem;
  }
  .spec div{ display:flex; align-items:baseline; gap:.5rem; }
  .spec span{ font-family:var(--mono); font-size:.6rem; letter-spacing:.09em;
              text-transform:uppercase; color:var(--faint); }
  .spec b{ font-family:var(--mono); font-size:.82rem; font-weight:600;
           color:var(--ink); font-variant-numeric:tabular-nums; }
  .spec .live b{ color:var(--floor); }
  .spec .off b{ color:var(--faint); font-weight:400; }

  .pagehead{ margin:0 0 .4rem; }
  .lede{ font-family:var(--serif); color:var(--muted); font-size:1.18rem;
         line-height:1.65; max-width:62ch; margin:.35rem 0 0; }

  /* ---- the one big number --------------------------------------------
     Serif, not mono. At this size mono figures read as a terminal; a text
     serif at 7rem reads as the headline number of a printed report.     */
  .hero{ font-family:var(--serif); font-size:7rem; font-weight:500;
         line-height:.9; letter-spacing:-.03em; color:var(--base);
         font-variant-numeric:tabular-nums; margin:.1rem 0 .7rem; }
  .hero-note{ color:var(--muted); font-size:1rem; line-height:1.65; max-width:42ch;
              font-family:var(--serif); }

  /* ---- figure block: a keyed table of results, not a stat rail -------- */
  .figblock{ border-top:2px solid var(--ink); }
  .figblock .row{
    display:flex; align-items:baseline; justify-content:space-between; gap:1rem;
    padding:.8rem 0; border-bottom:1px solid var(--rule);
  }
  .figblock .lbl{ font-family:var(--serif); font-size:.95rem; color:var(--muted);
                  max-width:22ch; line-height:1.4; }
  .statv{ font-family:var(--mono); font-size:1.4rem; font-weight:600;
          color:var(--ink); white-space:nowrap; display:block; text-align:right; }
  .statn{ font-size:.78rem; color:var(--faint); display:block; margin-top:.15rem;
          font-family:var(--serif); text-align:right; }

  /* ---- section heading ------------------------------------------------ */
  .sec{ margin:3.4rem 0 1.2rem; border-top:2px solid var(--ink); padding-top:1rem; }
  .sec h2{ margin-bottom:.35rem; }
  .sec p{ color:var(--muted); font-size:1rem; margin:0; max-width:68ch;
          font-family:var(--serif); line-height:1.6; }

  /* ---- cards ----------------------------------------------------------- */
  .card{
    background:var(--card); border:1px solid var(--rule); border-radius:3px;
    padding:1.35rem 1.45rem;
  }
  .card h3{ margin:.15rem 0 .45rem; }
  .card p{ color:var(--muted); font-size:.95rem; line-height:1.65; margin:0;
           font-family:var(--serif); }
  .card p + p{ margin-top:.6rem; }
  .card.keyed{ border-top:3px solid var(--key); }
  .cardfigs{ display:flex; gap:1.5rem; flex-wrap:wrap; margin-top:auto;
             padding-top:1.1rem; }

  /* Side-by-side cards are laid out HERE, not with st.columns. Streamlit wraps
     each column cell in three nested divs that size to their own content, so a
     shorter card stopped well above its neighbour. A grid the page owns gets
     matched heights from stretch, and margin-top:auto on .cardfigs pins the
     figures to the bottom of each card regardless of body length. */
  .cardgrid{ display:grid; grid-template-columns:repeat(2,1fr); gap:1.1rem;
             align-items:stretch; }
  .cardgrid .card{ display:flex; flex-direction:column; }
  @media (max-width: 900px){ .cardgrid{ grid-template-columns:1fr; } }

  /* ---- a plain-language key, set apart like a footnote ---------------- */
  .note{
    background:var(--card); border:1px solid var(--rule); border-left:3px solid var(--ink);
    padding:1rem 1.2rem; margin:0 0 1.8rem; border-radius:0 3px 3px 0;
  }
  .note b{ color:var(--ink); }
  .note p{ margin:0; font-family:var(--serif); font-size:.96rem;
           line-height:1.65; color:var(--muted); }
  .note p + p{ margin-top:.55rem; }

  /* ---- arm header ------------------------------------------------------
     Name and descriptor stacked with a fixed height, so three columns line
     up even when one name wraps and the others do not. */
  .armhead{
    padding:.3rem 0 .35rem .75rem; border-left:3px solid var(--key);
    margin:0 0 .85rem; min-height:48px;
  }
  .armhead b{ display:block; font-family:var(--serif); font-size:1.15rem;
              font-weight:600; color:var(--key); line-height:1.25; }
  .armhead span{ display:block; margin-top:.1rem; font-size:.75rem;
                 color:var(--faint); line-height:1.35; }

  /* ---- pod gauge -------------------------------------------------------
     Unfilled slots stay visible so "3 of a possible 8" is legible at a
     glance — a bare count of blocks hides how much headroom is left. */
  .pods{ display:flex; gap:4px; align-items:flex-end; height:34px; margin:0 0 .7rem; }
  .pods i{ width:19px; height:34px; border-radius:2px; display:block;
           border:1px solid var(--rule); background:var(--card); }
  .pods i.on{ border-color:transparent; }

  /* ---- arm stat strip --------------------------------------------------- */
  .armstats{ display:flex; gap:.4rem; }
  .armstats > div{
    flex:1 1 0; min-width:0; background:var(--card);
    border:1px solid var(--rule); border-radius:3px; padding:.5rem .6rem;
  }
  .armstats .eyebrow{ font-size:.55rem; letter-spacing:.06em; margin:0; }
  .armstats b{ font-size:1.08rem; font-weight:600; color:var(--ink);
               display:block; margin-top:.2rem; white-space:nowrap; }
  .armnote{ color:var(--muted); font-size:.87rem; line-height:1.6; margin:.8rem 0 0;
            font-family:var(--serif); }
  .armnote b{ color:var(--ink); font-weight:600; }

  /* ---- numbered steps --------------------------------------------------- */
  .step{ border-top:1px solid var(--ink); padding:.8rem 0 0; height:100%; }
  .step b{ display:block; font-family:var(--mono); font-size:.7rem;
           letter-spacing:.1em; color:var(--base); margin-bottom:.45rem; }
  .step h3{ font-size:1.02rem; margin:0 0 .35rem; }
  .step p{ color:var(--muted); font-size:.9rem; line-height:1.6; margin:0;
           font-family:var(--serif); }

  /* ---- metrics ----------------------------------------------------------- */
  [data-testid="stMetric"]{
    background:var(--card); border:1px solid var(--rule);
    border-radius:3px; padding:.7rem .9rem;
  }
  [data-testid="stMetricLabel"] p{
    font-family:var(--mono); font-size:.62rem !important; letter-spacing:.08em;
    text-transform:uppercase; color:var(--faint) !important;
  }
  [data-testid="stMetricValue"]{ font-size:1.5rem !important; color:var(--ink); }

  /* =====================================================================
     INTERACTION
     Feedback goes ONLY on things that respond to a click or a drag. Cards,
     figures, notes and the spec strip are readable objects, not controls —
     giving them hover states would advertise affordances that do not exist
     and make the page feel arbitrary.
     ===================================================================== */

  /* Everything clickable gets the pointer and a visible keyboard focus ring. */
  [data-testid="stButtonGroup"] button, .stSlider [role="slider"],
  [data-testid="stExpander"] summary, .stCheckbox label, [data-baseweb="checkbox"]{
    cursor:pointer;
  }
  [data-testid="stButtonGroup"] button:focus-visible,
  [data-testid="stExpander"] summary:focus-visible,
  [data-baseweb="checkbox"]:focus-within{
    outline:2px solid var(--focus); outline-offset:2px; border-radius:3px;
  }

  /* Nav and scenario/run pickers: lift off the stock on hover, sit on white
     when chosen. The transition is short — 120ms reads as responsive, longer
     reads as laggy on a control you click repeatedly. */
  [data-testid="stButtonGroup"] button{
    background:transparent !important; border-radius:3px !important;
    transition:background .12s ease, color .12s ease, box-shadow .12s ease;
  }
  [data-testid="stButtonGroup"] button:hover{
    background:var(--card) !important; color:var(--ink) !important;
    box-shadow:0 1px 0 rgba(16,22,25,.14);
  }
  [data-testid="stButtonGroup"] button:active{ transform:translateY(1px); }

  /* The slider is dragged, so its handle grows under the cursor. */
  .stSlider [role="slider"], .stSlider [data-baseweb="slider"] div[role]{
    transition:box-shadow .12s ease, transform .12s ease;
  }
  .stSlider [data-baseweb="slider"]:hover [role="slider"]{
    box-shadow:0 0 0 6px rgba(21,97,109,.16);
  }
  .stSlider [data-baseweb="slider"]{ padding-top:.3rem; }

  /* Table rows highlight under the pointer because you read across them and
     lose your place otherwise. */
  .stDataFrame{ border:1px solid var(--rule); border-radius:3px; }
  .stDataFrame [role="row"]:hover{ background:var(--stone) !important; }

  /* The expander is a disclosure control, so the whole header responds. */
  [data-testid="stExpander"] summary{ transition:background .12s ease; }
  [data-testid="stExpander"] summary:hover{ background:var(--stone); }

  /* Links underline on hover rather than changing colour — colour is spoken
     for by the three arms and must not start meaning something else. */
  .stApp a{ color:var(--pred); text-decoration:none;
            border-bottom:1px solid rgba(21,97,109,.35); transition:border-color .12s ease; }
  .stApp a:hover{ border-bottom-color:var(--pred); }

  hr{ border-color:var(--rule) !important; margin:1.8rem 0 !important; }

  @media (prefers-reduced-motion: reduce){
    *{ transition:none !important; animation:none !important; }
  }
</style>""")


# ---------------------------------------------------------------- html bits
def eyebrow(text: str) -> str:
    return f'<span class="eyebrow">{text}</span>'


def section(title: str, sub: str):
    st.html(f'<div class="sec"><h2>{title}</h2><p>{sub}</p></div>')


def stat_row(label: str, value: str, note: str, colour: str = INK) -> str:
    """One ruled row: what was measured on the left, the figure on the right.

    Label left / figure right rather than label-above-figure. Stacked, this was
    a stat rail lifted from a dashboard; ruled and aligned, it reads as a table
    of results, which is what it is.
    """
    return (f'<div class="row"><span class="lbl">{label}</span>'
            f'<span><span class="statv" style="color:{colour}">{value}</span>'
            f'<span class="statn">{note}</span></span></div>')


def pod_gauge(n: int, colour: str, slots: int = 8) -> str:
    """n filled slots out of `slots`, so headroom is visible, not implied."""
    n = int(n or 0)
    # color as well as background: the glow uses currentColor, so each lit slot
    # haloes in its own arm colour rather than in ink.
    return ('<div class="pods">'
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
    scenario is switched. Three stale numbers in a masthead would be worse than
    none, and this file used to carry exactly that.
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


def best_arm(means: dict) -> tuple[str, float, float] | None:
    """Lowest-p99 non-baseline arm, and its deltas against the baseline.

    Picked from the data rather than asserted: on the step scenario the winner
    is the floor arm, on the ramp there is only one candidate, and hardcoding
    either would go stale the first time a run is added.
    """
    rivals = [p for p in means if p != "A"]
    if not rivals or "A" not in means:
        return None
    b = min(rivals, key=lambda p: means[p]["p99"])
    lat = (1 - means[b]["p99"] / means["A"]["p99"]) * 100
    cost = (means[b]["pod_seconds"] / means["A"]["pod_seconds"] - 1) * 100
    return b, lat, cost


# ---------------------------------------------------------------- overview
def page_overview():
    """The answer, with no controls to operate first."""
    ramp = load_replay("replay.json")
    step = load_replay("replay-step.json")

    if not (ramp or step):
        st.html('<h1>Predictive Autoscaling</h1>')
        st.error("No replay data in bench/. Run `make replay-data` with "
                 "`make forward-prom` running.")
        return

    st.html(f"""
<div class="pagehead">
  <h1>Capacity that arrives<br>before the traffic does.</h1>
  <p class="lede">Kubernetes' HPA scales on CPU that has already risen, and a pod here
  takes 19 seconds to pass its readiness probe. This forecasts the request rate 60
  seconds ahead and scales before the load lands — then A/B tests that against the
  stock HPA under byte-identical traffic.</p>
</div>""")

    st.html("<div style='height:2.2rem'></div>")

    head = ramp or step
    hm = arm_means(head)
    win = best_arm(hm)

    left, right = st.columns([1.15, 1], gap="large")
    with left:
        if win:
            _, lat, cost = win
            st.html(f"""
<div>
  {eyebrow("Slowest 1% of responses &mdash; gradual ramp")}
  <div class="hero">{lat:.0f}%</div>
  <p class="hero-note">lower p99 than the stock HPA on identical traffic, for {cost:+.0f}% more
  pod-seconds. Both numbers are reported together on purpose: a latency win
  bought with unlimited compute is not a win.</p>
</div>""")
    with right:
        rows = ""
        if win:
            b, _, _ = win
            rows += stat_row("Response time, slowest 1%",
                             f"{hm['A']['p99']:.0f} → {hm[b]['p99']:.0f} ms",
                             "stock HPA → forecast", PRED)
            rows += stat_row("Compute used",
                             f"{hm['A']['pod_seconds']:,.0f} → {hm[b]['pod_seconds']:,.0f}",
                             "pod-seconds over the 20-minute run")
        rows += stat_row("Forecast quality", "64.5% lower cost",
                         "than the one-line naive forecast, over 4 backtest folds")
        st.html(f'<div class="figblock">{rows}</div>')

    # ---- the two scenarios, side by side -----------------------------------
    section("Two kinds of traffic",
            "The same system, tested against an event it can anticipate and one it cannot. "
            "The second is the honest half.")

    # Both cards go out in ONE html block as a CSS grid, rather than one card per
    # st.columns() cell. Streamlit wraps each cell in three nested divs that size
    # to their content and outrank any height rule aimed at them, so the shorter
    # card stopped well above its neighbour. A grid the page owns gets equal
    # heights for free from `align-items: stretch`.
    def scenario_card(key: str, title: str, body: str, means: dict, prefixes: str) -> str:
        figs = "".join(
            f'<div>{eyebrow(ARMS[p][0])}<span class="statv" '
            f'style="font-size:1.3rem;color:{ARMS[p][1]}">{means[p]["p99"]:.0f} ms</span></div>'
            for p in prefixes if p in means)
        return (f'<div class="card keyed" style="--key:{ARMS[prefixes[-1]][1]}">'
                f'{eyebrow(key)}<h3>{title}</h3>{body}'
                f'<div class="cardfigs">{figs}</div></div>')

    cards = ""
    if ramp:
        cards += scenario_card(
            "Gradual ramp", "The forecast wins",
            f'<p>{SCENARIOS["Gradual ramp"]["blurb"]}</p>',
            arm_means(ramp), "AB")
    if step:
        cards += scenario_card(
            "Instant spike", "The forecast loses, then wins differently",
            f'<p>{SCENARIOS["Instant spike"]["blurb"]}</p>'
            f'<p>Forecasting alone was <b style="color:{BASE}">worse</b> than doing '
            'nothing — it withdrew pods while the spike was still running. Letting it '
            "raise the HPA's <i>floor</i> instead fixed that: the forecast can add "
            'capacity early but can never take it away.</p>',
            arm_means(step), "ABC")
    st.html(f'<div class="cardgrid">{cards}</div>')

    # ---- how ----------------------------------------------------------------
    section("How it works",
            "Four steps, every 30 seconds, with the reactive autoscaler still underneath.")

    steps = [
        ("01", "Measure", "Prometheus scrapes the app every 15 seconds. That interval is "
                          "the resolution of everything downstream."),
        ("02", "Forecast", "A gradient-boosted model predicts the request rate 60 seconds "
                           "ahead — the measured time for a pod to become useful."),
        ("03", "Convert", "Predicted rate ÷ 20 req/s per pod, the measured capacity of one "
                          "replica, with 10% headroom."),
        ("04", "Apply", "Raise the autoscaler's floor. Capacity can arrive early, but only "
                        "real CPU is allowed to take it away."),
    ]
    for col, (n, title, body) in zip(st.columns(4, gap="medium"), steps):
        with col:
            st.html(f'<div class="step"><b>{n}</b><h3>{title}</h3><p>{body}</p></div>')

    st.html(f"""
<div style="margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--rule)">
  <p style="color:{FAINT};font-size:.82rem;margin:0">
  Every figure was measured on a local kind cluster — 51 hours of recorded traffic,
  three 20-minute runs per arm, identical load in every arm. The traffic is synthetic;
  the measurements are not.</p>
</div>""")


# ---------------------------------------------------------------- replay
def page_replay():
    available = [n for n, s in SCENARIOS.items()
                 if (ROOT / "bench" / s["file"]).exists()]
    if not available:
        st.error("No replay file found in bench/. Run `make replay-data` first "
                 "(it needs `make forward-prom` running).")
        return

    st.html(f'<div class="pagehead">{eyebrow("Recorded benchmark &middot; 20 minutes")}'
            '<h1 style="font-size:2.2rem">Benchmark replay</h1>'
            '<p class="lede">Scrub through a run that already happened. Nothing is '
            'computed live — these are the recordings the published results came '
            'from.</p></div>')

    # A key, before any controls. "Arm" is this project's word and nothing on the
    # page defines it; p99 and pod-seconds are standard but the reason they are
    # always quoted together is not.
    st.html(f"""
<div class="note">
  <p><b>Three arms, same traffic.</b> Each 20-minute run is replayed against all
  three scaling policies: <b style="color:{BASE}">Stock HPA</b> reacts to CPU,
  <b style="color:{PRED}">Predictive</b> lets the forecast set the replica count
  outright, and <b style="color:{FLOOR}">Predictive + floor</b> lets it set the
  HPA's <code>minReplicas</code> instead — so the forecast can add capacity early
  but never take it away. The floor arm was only run on the instant spike.</p>
  <p><b>Two numbers, always together.</b> <b>Slowest 1%</b> is p99 response time,
  what your unluckiest users actually feel. <b>Compute</b> is pod-seconds:
  replicas multiplied by the seconds they ran. Quoting either one alone is how a
  benchmark gets to look better than it is.</p>
</div>""")

    # ---- controls, all in one row, in the order you need them ---------------
    # Previously these were spread across three separate rows with the play
    # control below the fold. Choosing what to watch is one decision, so it is
    # one strip.
    st.html("<div style='height:1.4rem'></div>")
    c1, c2, c3 = st.columns([1.5, 1.2, 1], gap="medium")
    with c1:
        scen_name = st.segmented_control("Scenario", available, default=available[0],
                                         width="stretch")
    scen = SCENARIOS[scen_name or available[0]]
    data = load_replay(scen["file"])
    grouped = group_runs(data)
    means = arm_means(data)

    with c2:
        which = st.segmented_control("Run", list(grouped), default=list(grouped)[0],
                                     format_func=lambda i: f"Run {i}", width="stretch")
    arms = grouped[which or list(grouped)[0]]
    with c3:
        playing = st.toggle("Play", value=False,
                            help="Replay the run from the beginning")

    # Opens at the END of the run, not the start. At t=0 every figure reads zero
    # and every chart is blank, so the page's first impression was an empty
    # instrument and the reader had to discover that dragging was mandatory.
    # Landing on the finished run shows the result immediately; scrubbing left
    # then rewinds it, which is the direction people expect from a recording.
    #
    # No key= on the slider: with a key, Streamlit restores the widget from its
    # own stored state and ignores `value` on every rerun, so Play could never
    # move it. Keyless + explicit value means the playhead is ours to set.
    t = st.slider("Position in the run", 0, RUN_SECONDS,
                  value=st.session_state.get("t", RUN_SECONDS), step=20, format="%d s")
    st.session_state["t"] = t

    phase = next(text for until, text in scen["phases"] if t < until)
    st.html(f"""
<div style="display:flex;gap:1rem;align-items:baseline;padding:.9rem 1.1rem;
            background:var(--card);border:1px solid var(--rule);
            border-radius:10px;margin:.2rem 0 1.6rem">
  <b class="mono" style="color:{PRED};font-size:.95rem;white-space:nowrap">
    {t // 60}:{t % 60:02d}</b>
  <span style="color:{MUTED};font-size:.92rem;line-height:1.5">{phase}</span>
</div>""")

    # ---- one column per arm -------------------------------------------------
    # The whole panel is one HTML block rather than st.metric in nested columns.
    # At three arms those nested columns are ~200px wide, and Streamlit's metric
    # ellipsised both the label and the value — "SLOWEST …" over "99 …" — while
    # the wrapped third heading pushed that column out of line with the other two.
    present = [p for p in ARMS if p in arms]
    for col, prefix in zip(st.columns(len(present), gap="medium"), present):
        run = arms[prefix]
        name, colour, kind, _dash = ARMS[prefix]
        rate = value_at(run, "rate", t) or 0
        pods = value_at(run, "pods", t) or 0
        p99 = value_at(run, "p99", t)

        d = decision_at(run, t)
        if d:
            # The two forecasting arms act through different levers, and the note
            # has to say which — "adding a pod" would be a lie in floor mode,
            # where the controller only moves minReplicas and the HPA decides
            # whether a pod actually appears.
            act = {"scale_up": " &middot; <b>adding a pod now</b>",
                   "floor_up": " &middot; <b>raising the hpa's floor now</b>",
                   }.get(d["action"], "")
            note = (f"Model: now <b>{d['now']:.0f}/s</b>, expects "
                    f"<b>{d['pred']:.0f}/s</b> in 60 s &rarr; wants "
                    f"<b>{d['pods_target']} pods</b>{act}")
        elif run["arm"] == "baseline":
            note = "No forecast — this version only reacts to what already happened."
        else:
            note = "&nbsp;"

        stats = [("Traffic", f"{rate:.0f}/s"), ("Pods", f"{pods}"),
                 ("Slowest 1%", f"{p99} ms" if p99 else "–")]
        with col:
            st.html(
                f'<div class="armhead" style="--key:{colour}">'
                f'<b>{name}</b><span>{kind}</span></div>'
                + pod_gauge(pods, colour)
                + '<div class="armstats">'
                + "".join(f'<div><span class="eyebrow">{l}</span><b>{v}</b></div>'
                          for l, v in stats)
                + f'</div><p class="armnote">{note}</p>')

    # ---- charts -------------------------------------------------------------
    # Response time is the claim, so it gets the full width and twice the height;
    # pods and traffic are the mechanism and sit together beneath it. Three equal
    # stacked charts made the reader scroll to find out which one mattered.
    section("What happened", "Drawn only up to the playhead, so the run unfolds as you scrub.")

    # Both scales are passed explicitly rather than left to Altair's default
    # ordering: an arm must keep its colour AND its dash when a scenario has two
    # arms instead of three, or the reader relearns the key on every switch.
    names = [ARMS[p][0] for p in present]
    scale = alt.Scale(domain=names, range=[ARMS[p][1] for p in present])
    dashes = alt.Scale(domain=names, range=[ARMS[p][3] for p in present])

    def chart(key: str, title: str, height: int):
        frames = []
        full = []                       # every point, playhead ignored
        for prefix in present:
            df = series(arms[prefix], key)
            full.append(df[key])
            df = df[df.t <= t].rename(columns={key: "value"})
            df["arm"] = ARMS[prefix][0]
            frames.append(df)
        sub = pd.concat(frames, ignore_index=True)

        # The axes are scaled to the WHOLE run, not to what has been drawn yet.
        # Two reasons, both about not lying: a y-axis that grows as you scrub
        # makes an early spike look identical to a late one, and at t=0 there is
        # nothing to plot at all — an empty chart that returns None would drop
        # the panel out of the page and shift everything below it.
        allv = pd.concat(full, ignore_index=True).dropna()
        ymax = float(allv.max()) * 1.08 if len(allv) else 1.0

        return (alt.Chart(sub)
                .mark_line(interpolate="step-after" if key == "pods" else "linear",
                           strokeWidth=2)
                .encode(
                    # Tick counts are capped: left to itself Altair labelled every
                    # 50 seconds, which is 25 labels on a 1200-second axis and
                    # unreadable once the chart is half-width.
                    x=alt.X("t:Q", title="seconds into run",
                            axis=alt.Axis(tickCount=7, format="d"),
                            scale=alt.Scale(domain=[0, RUN_SECONDS])),
                    y=alt.Y("value:Q", title=None,
                            axis=alt.Axis(tickCount=4),
                            scale=alt.Scale(domain=[0, ymax], nice=False)),
                    color=alt.Color("arm:N", scale=scale, title=None,
                                    legend=alt.Legend(orient="top", offset=4)),
                    # Dash as well as colour. On the traffic chart all three arms
                    # are offered identical load and sit exactly on top of one
                    # another, so colour alone shows only whichever drew last.
                    strokeDash=alt.StrokeDash("arm:N", scale=dashes, title=None,
                                              legend=alt.Legend(orient="top", offset=4)),
                    tooltip=["arm", "t", "value"])
                .properties(height=height, title=title)
                .configure_view(strokeWidth=0)
                .configure_axis(grid=True, gridColor=RULE, domainColor=RULE,
                                tickColor=RULE, labelColor=FAINT, titleColor=FAINT,
                                labelFont="IBM Plex Mono", labelFontSize=10,
                                titleFont="IBM Plex Sans", titleFontSize=11)
                .configure_title(color=INK, fontSize=14, anchor="start", offset=10,
                                 font="Newsreader", fontWeight=600)
                .configure_legend(labelColor=MUTED, symbolType="stroke",
                                  labelFont="IBM Plex Sans", labelFontSize=12))

    st.altair_chart(chart("p99", "Response time of the slowest 1% (ms)", 260),
                    width="stretch")
    a, b = st.columns(2, gap="medium")
    with a:
        st.altair_chart(chart("pods", "Pods running", 180), width="stretch")
    with b:
        st.altair_chart(chart("rate", "Requests arriving per second", 180),
                        width="stretch")

    # ---- verdict ------------------------------------------------------------
    section("What this run measured",
            f"This single run only. The overview page averages all {len(grouped)} runs "
            "per arm, which is the figure worth quoting.")

    st.dataframe(pd.DataFrame([
        {"Version": ARMS[p][0],
         "Slowest 1%": f"{arms[p]['summary']['p99']} ms",
         "Typical": f"{arms[p]['summary']['p50']} ms",
         "Compute used": f"{arms[p]['summary']['pod_seconds']:,} pod-s"}
        for p in present]), hide_index=True, width="stretch")

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
                f"**{ARMS[p][0]}** — p99 **{lat:.0f}% lower** than the stock HPA "
                f"({sa['p99']} ms → {s['p99']} ms), using **{cost:+.0f}% compute**.")
    st.caption("A negative 'faster' is a real result, reported rather than dropped.")

    # One frame per rerun, advanced only once the whole page above has drawn.
    # The sleep is what makes it watchable rather than a flicker; the slider
    # stays draggable throughout, which matters more than smoothness because
    # the point is reading the numbers at a chosen instant.
    if playing:
        # Pressing Play on a finished run means "watch it again", so it rewinds
        # rather than sitting inert at the end — which is what the old
        # disabled-at-the-end toggle did, and it read as broken.
        st.session_state["t"] = 0 if t >= RUN_SECONDS else t + 20
        time.sleep(0.4)
        st.rerun()


# ---------------------------------------------------------------- live
@st.cache_resource
def load_model():
    import joblib
    p = ROOT / "models/forecaster.joblib"
    return joblib.load(p) if p.exists() else None


@st.cache_data(ttl=30)
def prometheus_reachable() -> bool:
    """Cheap probe, so the page can explain itself instead of throwing.

    Away from the cluster this is always False: Prometheus runs on the laptop
    that ran the experiment. Saying so plainly is better than showing a visitor
    a connection error they cannot act on.
    """
    try:
        import requests
        return requests.get("http://localhost:9090/-/healthy", timeout=2).status_code == 200
    except Exception:
        return False


def page_live():
    st.html(f'{eyebrow("Reads Prometheus and the model right now")}'
            '<h1 style="font-size:2rem">Live forecast</h1>')

    if not prometheus_reachable():
        st.html(f"""
<div class="card" style="margin-top:1.4rem">
  <h3>This page only works on the machine running the cluster</h3>
  <p>It reads Prometheus at <code>localhost:9090</code> and asks the trained model what
  traffic is coming in the next 60 seconds. Prometheus is not reachable from here, so
  there is nothing live to read.</p>
  <p style="margin-top:.7rem">Everything the project measured is on
  <b style="color:{PRED}">Overview</b> and <b style="color:{PRED}">Benchmark replay</b>,
  which need nothing running.</p>
</div>""")
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

    c1, c2, c3 = st.columns(3, gap="medium")
    c1.metric("Traffic now", f"{now_rate:.1f}/s")
    c2.metric(f"Expected in {ahead}s", f"{pred:.1f}/s", f"{pred - now_rate:+.1f}")
    c3.metric("Pods this needs", want)

    hist = df.tail(120).copy()
    chart = (alt.Chart(hist).mark_line(color=PRED, strokeWidth=2)
             .encode(x=alt.X("ts:T", title=None),
                     y=alt.Y("y:Q", title="requests / second"),
                     tooltip=["ts:T", "y:Q"])
             .properties(height=240, title="Last 30 minutes"))
    rule = alt.Chart(pd.DataFrame({"y": [pred]})).mark_rule(
        color=BASE, strokeDash=[4, 4], strokeWidth=2).encode(y="y:Q")
    st.altair_chart(
        (chart + rule)
        .configure_view(strokeWidth=0)
        .configure_axis(grid=True, gridColor=RULE, domainColor=RULE,
                        tickColor=RULE, labelColor=FAINT, titleColor=FAINT,
                        labelFont="IBM Plex Mono", labelFontSize=10)
        .configure_title(color=INK, fontSize=14, anchor="start", offset=10,
                         font="Newsreader", fontWeight=600),
        width="stretch")
    st.caption(f"Dashed line is the forecast for {ahead} seconds from now. If it simply "
               "tracks the current value, the model is behaving like the naive baseline "
               "and something upstream is wrong.")

    log = ROOT / "logs/decisions.csv"
    if log.exists():
        section("Recent controller decisions", "The tail of logs/decisions.csv.")
        st.dataframe(pd.read_csv(log).tail(12).iloc[::-1],
                     hide_index=True, width="stretch")

    if auto:
        time.sleep(15)
        st.rerun()


# ---------------------------------------------------------------- shell
# Masthead, navigation strip, spec strip — then the page. Laid out as a document
# head rather than an app shell: there is no sidebar, because a persistent left
# rail with a brand block and a stat list is somebody else's product furniture,
# and this content is a report with three sections.
inject_style()

st.html("""
<div class="mast">
  <span class="wordmark">Predictive Autoscaling for Kubernetes</span>
  <span class="prov">A/B benchmark &middot; kind cluster &middot; 3 runs per arm</span>
</div>""")

# required=True so the strip cannot be clicked into an empty state — with a
# deselectable control, clicking the current page blanks the whole app.
page = st.segmented_control(
    "View", ["Overview", "Benchmark replay", "Live forecast"],
    default="Overview", required=True, label_visibility="collapsed")

live_ok = prometheus_reachable()
st.html(
    '<div class="spec">'
    + "".join(f"<div><span>{k}</span><b>{v}</b></div>" for k, v in SPECS)
    + (f'<div class="{"live" if live_ok else "off"}"><span>prometheus</span>'
       f'<b>{"connected" if live_ok else "offline"}</b></div>')
    + "</div>")

{"Overview": page_overview,
 "Benchmark replay": page_replay,
 "Live forecast": page_live}[page]()
