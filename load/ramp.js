import http from 'k6/http';
import { check } from 'k6';

// THE SECOND EXAM PAPER: a PREDICTABLE load change.
//
// benchmark.js is a 4x step with no precursor. Measured there: the controller
// provisioned correctly (5 pods vs the HPA's 3) and still did not beat it on
// p99, because a forecaster reading lag features has nothing to forecast FROM
// until the step has already happened. Both policies are blind for the first
// 30-60s, pods take ~19s to boot, and the queued latency is already paid.
// That is a real limitation and it belongs in the writeup - but it tests the
// one thing this model cannot do.
//
// A ramp is what predictive scaling is FOR. Load climbs over 6 minutes, so
// diff_4, slope_12 and roll_mean_4 all carry the trend, and a 60s-ahead
// forecast can put pods in place before the traffic that needs them arrives.
// The HPA cannot do this even in principle: it acts on CPU that has already
// risen, then waits out the pod start-up it could have started earlier.
//
// Same 20-minute length, same steady floor and same peak as benchmark.js, so
// the two scenarios are directly comparable. Zero randomness, again: three
// runs per arm must differ only in the arm.
//
//   0-4    steady 20 req/s      both arms settle to the 2-pod floor
//   4-10   ramp 20 -> 80        THE EVENT - gradual, therefore forecastable
//   10-14  plateau 80           did either arm arrive with enough capacity?
//   14-20  ramp 80 -> 20        scale-down behaviour, which is where the
//                               asymmetric MAX_SCALE_DOWN_PER_CYCLE shows up
const TARGET = __ENV.TARGET || 'http://traffic-app/work';
const LOW = Number(__ENV.STEADY_RPS || 20);
const HIGH = Number(__ENV.PEAK_RPS || 80);

export const options = {
  scenarios: {
    ramp: {
      // Arrival rate, not VUs - otherwise the better-scaling arm serves more
      // requests and the p99 comparison is between different workloads.
      executor: 'ramping-arrival-rate',
      startRate: LOW,
      timeUnit: '1s',
      stages: [
        { duration: '4m', target: LOW },
        { duration: '6m', target: HIGH },   // ramping-arrival-rate interpolates
        { duration: '4m', target: HIGH },
        { duration: '6m', target: LOW },
      ],
      preAllocatedVUs: 100,
      // Generous: if k6 runs out of VUs it drops iterations, which removes load
      // exactly when the app is struggling and flatters whichever arm is coping
      // worse. A valid run reports dropped_iterations = 0.
      maxVUs: 3000,
    },
  },
  // kube-proxy balances per TCP connection, so reused keep-alive sockets pin
  // traffic to a few pods and whatever either arm launches sits idle.
  noConnectionReuse: true,
  summaryTrendStats: ['avg', 'p(50)', 'p(95)', 'p(99)', 'max'],
};

export default function () {
  const res = http.get(TARGET);
  check(res, { 'status is 200': (r) => r.status === 200 });
}

export function handleSummary(data) {
  return {
    stdout:
      '\n===BENCH_JSON_START===\n' +
      JSON.stringify({ run: __ENV.RUN_NAME || 'unnamed', metrics: data.metrics }) +
      '\n===BENCH_JSON_END===\n',
  };
}
