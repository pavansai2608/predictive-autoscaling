# Discarded runs

`A1-4x-on-30.json` — steady 30 req/s, spike to 120. p99 15,647ms, 641 dropped
iterations, HPA reached only 4 of the ~7 pods needed.

Not a rigged result, but the wrong experiment. Two reasons:

1. At 30 req/s on the 2-pod floor, average CPU was already 82% against a 90%
   HPA target. The baseline began the run at the edge of its own trigger.

2. Once a pod saturates its 400m limit, CPU utilisation reads 100% and cannot
   go higher — a pod at 3x overload is indistinguishable from one at 1.01x. The
   HPA can therefore only grow replicas by 100/90 = 1.11 per cycle, so a 4x step
   is beyond what it can track at all. The run measured that blindness rather
   than reaction timing.

Both are true findings about CPU-based autoscaling and worth a paragraph in the
README. They are not what this project set out to measure, which is whether
forecasting delivers capacity EARLIER than reacting to it.

Replaced by steady 20 req/s -> spike 80, where the HPA (which settles at
~16.8 req/s per pod, measured) and the controller (20 req/s per pod, measured)
both target 5 pods — so the only variable left is when those pods arrive.
