import http from 'k6/http';
import { check } from 'k6';

export const options = {
  vus: 5,
  duration: '2m',

  // k6's default summary reports p95 but not p99, and p99 is the number the
  // whole project is judged on — without this the headline metric never prints.
  summaryTrendStats: ['avg', 'p(95)', 'p(99)', 'max'],
};

export default function () {
  // Port 5000 is the local end of `make forward-app`, so this hits the Service
  // and therefore only Ready pods — the same path the benchmark will use.
  const res = http.get('http://localhost:5000/work');

  // Without this a flood of 502s during a scale-up would look like a fast run
  // rather than a broken one, since k6 times failures just as happily.
  check(res, { 'status is 200': (r) => r.status === 200 });

  // No sleep(): 5 VUs re-request the moment each response lands, which is what
  // "constantly" means here. See the note about closed-loop load before reusing
  // this shape for the actual A/B scenario.
}
