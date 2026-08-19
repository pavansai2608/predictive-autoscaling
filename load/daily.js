import http from 'k6/http';
import { check } from 'k6';

// TARGET IS THE CLUSTER-INTERNAL SERVICE, and this script is meant to run in a
// pod, not on the Mac. That is not a convenience — it is a correctness fix.
//
// `kubectl port-forward svc/traffic-app` resolves the Service to ONE pod and
// pins every request to it. Measured on 2026-08-19 with 4 replicas Ready:
// one pod served 6.94 req/s and the other three served 0.00. Load offered that
// way can never show a benefit from scaling, because the pods you add never
// receive anything. Sending to the ClusterIP from inside the cluster lets
// kube-proxy spread each connection across all Ready endpoints — which is also
// how traffic would actually arrive in production.
const TARGET = __ENV.TARGET || 'http://traffic-app/work';

// Requests/second at the top of the busy plateau. Everything below is a
// fraction of this, so the whole diurnal shape rescales from one number.
// Set it from MEASURED single-pod capacity x the pod count you want the
// plateau to need — not from a guess.
const PEAK_RPS = Number(__ENV.PEAK_RPS || 80);

// One "day" is 60 real minutes. CYCLES is resolved once at init, so this is
// "long enough" rather than forever: 168 cycles = 7 real days.
const CYCLE_MIN = 60;
const CYCLES = 168;

// Every 7th day is light, so the model has to key off day-of-week and not just
// minute-of-day — the most common way a naive forecaster quietly overfits.
const WEEKEND_EVERY = 7;
const WEEKEND_SCALE = 0.5;

const rand = (lo, hi) => lo + Math.random() * (hi - lo);
const lerp = (a, b, t) => a + (b - a) * t;

// Minute-by-minute load across one ordinary day, as a FRACTION of PEAK_RPS.
function baseCurve(m) {
  if (m < 10) return rand(0.10, 0.18);              // 0-10   quiet overnight
  if (m < 25) return lerp(0.18, 1.0, (m - 10) / 15); // 10-25  morning ramp
  if (m < 45) return rand(0.85, 1.0);                // 25-45  busy plateau
  return lerp(1.0, 0.12, (m - 45) / 15);             // 45-60  evening taper
}

function buildDay(cycle) {
  const day = [];
  for (let m = 0; m < CYCLE_MIN; m++) day.push(baseCurve(m));

  // 2-3 spikes of 2-3x lasting 2-4 minutes. These are the events that make
  // over-provisioning cheap insurance and under-provisioning expensive, which
  // is exactly the asymmetry the q=0.90 quantile is chosen to respect.
  const spikes = Math.floor(rand(2, 4));
  for (let s = 0; s < spikes; s++) {
    const start = Math.floor(rand(5, CYCLE_MIN - 5));
    const len = Math.floor(rand(2, 5));
    const mult = rand(2, 3);
    for (let m = start; m < Math.min(start + len, CYCLE_MIN); m++) day[m] *= mult;
  }

  const scale = cycle % WEEKEND_EVERY === WEEKEND_EVERY - 1 ? WEEKEND_SCALE : 1;
  // Clamped to 2.2x peak: a spike the cluster cannot physically serve stops
  // being a demand signal and becomes a queue-depth measurement instead.
  return day.map((v) => Math.max(2, Math.round(v * scale * PEAK_RPS)))
            .map((v) => Math.min(v, Math.round(PEAK_RPS * 2.2)));
}

function buildStages() {
  const stages = [];
  for (let c = 0; c < CYCLES; c++) {
    // One stage per minute: ramping-arrival-rate interpolates between targets,
    // so this gives smooth curves and sharp spikes from the same flat list.
    for (const target of buildDay(c)) stages.push({ duration: '1m', target });
  }
  return stages;
}

export const options = {
  scenarios: {
    daily: {
      // ramping-ARRIVAL-RATE, not ramping-vus. With VUs, each user fires its
      // next request the instant the last response lands, so requests/second
      // = VUs / latency — and latency falls as pods are added. The recorded
      // "demand" would then be partly an OUTPUT of the autoscaler, and the
      // forecaster would be learning its own control loop. An arrival rate is
      // offered load: identical whether 2 pods or 20 are serving it.
      executor: 'ramping-arrival-rate',
      startRate: Math.max(2, Math.round(PEAK_RPS * 0.12)),
      timeUnit: '1s',
      stages: buildStages(),
      // Generous headroom: when the app saturates, latency climbs and k6 needs
      // more concurrent VUs to keep the arrival rate on schedule. Too few and
      // k6 silently drops iterations, which looks like falling demand.
      preAllocatedVUs: 50,
      maxVUs: 400,
    },
  },
  // ONE CONNECTION PER REQUEST. kube-proxy load balances at L4 — it picks a
  // backend when a TCP connection is established, not per request — and k6
  // reuses keep-alive connections by default. Measured: with reuse on, a
  // single VU's connection pinned 13.05 req/s onto one pod while two other
  // Ready pods sat at 0.00, which is the same failure the port-forward had.
  // A real service is reached by many independent clients; one load generator
  // holding one socket is the artefact. This applies identically to both
  // benchmark arms, so it cannot bias the comparison.
  noConnectionReuse: true,
  summaryTrendStats: ['avg', 'p(95)', 'p(99)', 'max'],
};

export default function () {
  const res = http.get(TARGET);
  // Without this a flood of 502s during a scale-up would look like a fast run
  // rather than a broken one, since k6 times failures just as happily.
  check(res, { 'status is 200': (r) => r.status === 200 });
}
