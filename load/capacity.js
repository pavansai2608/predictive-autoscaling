import http from 'k6/http';
import { check } from 'k6';

// ONE POD'S CAPACITY, measured rather than guessed.
//
// This is the number that converts a forecast in requests/second into a pod
// count (`CAPACITY_PER_POD` in src/controller.py). Get it wrong and every
// decision the controller makes is wrong in the same direction — and nothing
// in the forecast metrics will show it, because the forecast is still correct.
//
// Method: scale the deployment to 1 replica, delete the HPA so nothing else
// moves, then walk the ARRIVAL RATE upward in steps. Capacity is the last step
// where p95 latency is still flat. Past that point the pod is queueing, and
// latency climbs while throughput does not.
//
//   kubectl delete hpa traffic-app
//   kubectl scale deploy/traffic-app --replicas=1
//   make capacity
//
// Arrival rate, not VUs: a closed-loop VU test can never overload the pod
// (each user waits for its own response), so it measures how slow the pod got,
// never where it broke.
const TARGET = __ENV.TARGET || 'http://traffic-app/work';

// Steps in requests/second. Wide enough to bracket a pod limited to 400m CPU
// doing 30ms of work per request — theory says ~13 req/s, so the interesting
// region is 4-24 and the top steps exist to prove the knee is real.
const STEPS = (__ENV.STEPS || '4,8,12,16,20,24,28').split(',').map(Number);
const STEP_SECONDS = Number(__ENV.STEP_SECONDS || 45);

export const options = {
  scenarios: {
    ramp: {
      executor: 'ramping-arrival-rate',
      startRate: STEPS[0],
      timeUnit: '1s',
      // duration 0 makes each target a STEP rather than a ramp: jump to the
      // rate, hold it, jump again. A smooth ramp would smear the knee across
      // the whole run and there would be nothing to read off.
      stages: STEPS.flatMap((r) => [
        { duration: '0s', target: r },
        { duration: `${STEP_SECONDS}s`, target: r },
      ]),
      preAllocatedVUs: 20,
      maxVUs: 300,
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
  check(res, { 'status is 200': (r) => r.status === 200 });
}
