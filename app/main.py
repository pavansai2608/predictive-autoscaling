"""The app under test.

Deliberately CPU-bound and slow to start. Those two properties are the whole
experiment: slow start is why reactive scaling arrives too late, and CPU-bound
means a pod has finite capacity, so adding pods actually buys throughput.
"""

import asyncio
import logging
import os
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# Read once at import. Env can't change inside a running pod, and /work sits on
# the latency path we're measuring — no getenv in the hot loop.
WORK_MS = int(os.getenv("WORK_MS", "30"))
STARTUP_DELAY_S = float(os.getenv("STARTUP_DELAY_S", "15"))

# uvicorn's own logger, so this lands in the same stream and format as
# "Application startup complete" instead of vanishing into an unconfigured root.
log = logging.getLogger("uvicorn.error")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # uvicorn awaits lifespan startup BEFORE binding the socket, so during this
    # sleep the port isn't even listening. That's the point: it reproduces the
    # real gap between "pod scheduled" and "pod can serve traffic", which is
    # exactly the delay stock HPA cannot hide. This value is also what sets the
    # forecast horizon N later on.
    log.info("warming up for %.1fs before serving...", STARTUP_DELAY_S)
    await asyncio.sleep(STARTUP_DELAY_S)
    log.info("ready: WORK_MS=%d STARTUP_DELAY_S=%.1f", WORK_MS, STARTUP_DELAY_S)
    yield


app = FastAPI(lifespan=lifespan)

# The hinge of the whole loop: Prometheus scrapes /metrics every 15s, and the
# http_requests_total counter exposed here is the raw signal collect.py records
# and the forecaster learns from. No metrics, no history, no model.
Instrumentator().instrument(app).expose(app)


# Sync def, NOT async def: FastAPI runs sync handlers in a threadpool. An async
# handler that busy-loops would pin the event loop, so a single in-flight
# request would stall every new connection — the benchmark would then measure
# event-loop starvation rather than pod capacity.
@app.get("/work")
def work():
    deadline = time.perf_counter() + WORK_MS / 1000.0
    while time.perf_counter() < deadline:
        pass  # a real CPU burn; sleeping would leave the pod idle and never scale
    return {"ok": True}


# async def and zero CPU: a sync handler would queue behind the threadpool once
# /work saturates it, so the probe would fail exactly when the pod is busiest
# and Kubernetes would restart pods mid-benchmark.
@app.get("/healthz")
async def healthz():
    return {"ok": True}
