import http from 'k6/http';
import { check } from 'k6';

// One "day" is 60 real minutes. This shape is the whole training signal: a
// repeatable diurnal curve the forecaster can anticipate, plus random spikes it
// cannot — so a model that just memorises the mean gets punished on both.
const CYCLE_MIN = 60;

// k6 resolves its stage list once at init, so "forever" is really "long
// enough": 168 cycles = 7 real days of collection. Raise it or wrap the run.
const CYCLES = 168;

// Every 7th day is light, so the model has to key off day-of-week and not just
// minute-of-day — the most common way a naive forecaster quietly overfits.
const WEEKEND_EVERY = 7;
const WEEKEND_SCALE = 0.5;

const rand = (lo, hi) => lo + Math.random() * (hi - lo);
const lerp = (a, b, t) => a + (b - a) * t;

// Minute-by-minute VU target across one ordinary day.
function baseCurve(m) {
  if (m < 10) return rand(2, 4);                 // 0-10   quiet overnight
  if (m < 25) return lerp(4, 30, (m - 10) / 15); // 10-25  morning ramp
  if (m < 45) return rand(25, 35);               // 25-45  busy plateau
  return lerp(30, 3, (m - 45) / 15);             // 45-60  evening taper
}

function buildDay(cycle) {
  const day = [];
  for (let m = 0; m < CYCLE_MIN; m++) day.push(baseCurve(m));

  // 2-3 spikes of 3-4x lasting 2-4 minutes. These are the events that make
  // over-provisioning cheap insurance and under-provisioning expensive, which
  // is exactly the asymmetry the q=0.90 quantile is chosen to respect.
  const spikes = Math.floor(rand(2, 4));
  for (let s = 0; s < spikes; s++) {
    const start = Math.floor(rand(5, CYCLE_MIN - 5));
    const len = Math.floor(rand(2, 5));
    const mult = rand(3, 4);
    for (let m = start; m < Math.min(start + len, CYCLE_MIN); m++) day[m] *= mult;
  }

  const scale = cycle % WEEKEND_EVERY === WEEKEND_EVERY - 1 ? WEEKEND_SCALE : 1;
  return day.map((v) => Math.max(1, Math.round(v * scale)));
}

function buildStages() {
  const stages = [];
  for (let c = 0; c < CYCLES; c++) {
    // One stage per minute: ramping-vus interpolates between targets, so this
    // gives smooth curves and sharp spikes from the same flat list.
    for (const target of buildDay(c)) stages.push({ duration: '1m', target });
  }
  return stages;
}

export const options = {
  scenarios: {
    daily: {
      executor: 'ramping-vus',
      startVUs: 2,
      stages: buildStages(),
      // Default 30s would blur every taper and spike decay the model is meant
      // to learn from.
      gracefulRampDown: '10s',
    },
  },
  summaryTrendStats: ['avg', 'p(95)', 'p(99)', 'max'],
};

export default function () {
  // Port 5000 is the local end of `make forward-app`.
  const res = http.get('http://localhost:5000/work');
  check(res, { 'status is 200': (r) => r.status === 200 });
}
