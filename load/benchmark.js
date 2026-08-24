import http from 'k6/http';
import { check } from 'k6';

// THE EXAM PAPER. Both arms sit the same one.
//
// Zero randomness anywhere in this file - no rand(), no spikes at random
// minutes, no per-cycle variation. daily.js is deliberately unpredictable
// because a forecaster has to earn its keep against surprise; a BENCHMARK is
// the opposite. If the two arms faced different traffic, any difference in
// p99 would be unattributable, and running it three times each would measure
// the randomness rather than the policy.
//
// 20 minutes, three phases:
//
//   0-5    steady at STEADY_RPS      both arms settle to their baseline pods
//   5-9    step to 4x STEADY_RPS     THE EVENT - this is what is being measured
//   9-20   back to steady            recovery and scale-down behaviour
//
// The step at minute 5 is a step, not a ramp: reactive scaling is slowest when
// load arrives faster than pods can boot, and a gradual ramp would let the HPA
// keep up and hide the very lag this project exists to demonstrate.
const TARGET = __ENV.TARGET || 'http://traffic-app/work';

// Chosen so BOTH policies target the same pod count, leaving timing as the
// only variable. Measured on this cluster:
//
//   HPA at 90% of a 400m request settles at ~16.8 req/s per pod
//   the controller uses the measured 20 req/s per pod, x1.1 headroom
//
//   steady 20 req/s -> HPA 2 pods (the floor), controller 2 pods
//   spike  80 req/s -> HPA 5 pods,             controller ceil(80*1.1/20) = 5
//
// The earlier 30 -> 120 version put the baseline at 82% CPU before the spike
// even started, and a 4x step is past what CPU-based scaling can track at all
// (utilisation caps at 100% once the pod hits its limit, so the HPA can only
// grow 1.11x per cycle). See bench/discarded/README.md.
const STEADY_RPS = Number(__ENV.STEADY_RPS || 20);
const SPIKE_MULT = Number(__ENV.SPIKE_MULT || 4);
const SPIKE = Math.round(STEADY_RPS * SPIKE_MULT);

export const options = {
  scenarios: {
    bench: {
      // Arrival rate, not VUs. With VUs, throughput is VUs/latency, so the arm
      // that scales better serves MORE requests - and comparing p99 across
      // arms that handled different request counts is not a comparison. A
      // fixed arrival rate means both arms are offered identical work and only
      // their latency can differ.
      executor: 'ramping-arrival-rate',
      startRate: STEADY_RPS,
      timeUnit: '1s',
      stages: [
        { duration: '5m', target: STEADY_RPS },   // settle
        { duration: '1s', target: SPIKE },        // the step
        { duration: '4m', target: SPIKE },        // hold the spike
        { duration: '1s', target: STEADY_RPS },   // release
        { duration: '11m', target: STEADY_RPS },  // recover
      ],
      // Sized for the spike at degraded latency: if k6 runs out of VUs it
      // silently drops iterations, which shows up as the load DISAPPEARING
      // exactly when the app is struggling - flattering whichever arm is
      // coping worse.
      preAllocatedVUs: 100,
      // 800 was not enough in run A1: latency hit 14s under collapse, so
      // holding 120 req/s needed ~1700 concurrent VUs and k6 dropped 4,213
      // iterations. Dropped iterations silently REDUCE the offered load at
      // exactly the moment the app is struggling, which flatters whichever
      // arm is coping worse. A valid run must report dropped_iterations = 0.
      maxVUs: 3000,
    },
  },
  // Same reason as daily.js: kube-proxy balances per TCP connection, so reused
  // keep-alive sockets would pin traffic onto a few pods and the extra pods
  // either arm launched would sit idle.
  noConnectionReuse: true,
  summaryTrendStats: ['avg', 'p(50)', 'p(95)', 'p(99)', 'max'],
};

export default function () {
  const res = http.get(TARGET);
  check(res, { 'status is 200': (r) => r.status === 200 });
}

// k6 runs in a pod, so a file written here would die with the pod. Emitting
// the JSON to stdout between markers lets `kubectl logs` carry it out intact,
// past the per-second progress lines.
export function handleSummary(data) {
  return {
    stdout:
      '\n===BENCH_JSON_START===\n' +
      JSON.stringify({ run: __ENV.RUN_NAME || 'unnamed', metrics: data.metrics }) +
      '\n===BENCH_JSON_END===\n',
  };
}
