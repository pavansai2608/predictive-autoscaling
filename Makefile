# Ports live here and nowhere else, so changing one is a single edit.
# 8000, not 5000: macOS Control Center holds 5000 for AirPlay Receiver, and when
# something else is listening there a failed connection comes back as an instant
# 403 rather than an error — which once let k6 report 12.5M healthy iterations
# while delivering nothing at all. 8000 also matches the container's port.
APP_PORT  = 8000
PROM_PORT = 9090

# Use the venv's interpreters when they exist, otherwise whatever is on PATH.
# Without this, every target here fails with "No such file or directory" unless
# you remembered to `source .venv/bin/activate` first — which is a bad way to
# find out your dashboard is fine and your shell was not.
VENV      ?= .venv
PY        := $(shell [ -x $(VENV)/bin/python ] && echo $(VENV)/bin/python || echo python)
STREAMLIT := $(shell [ -x $(VENV)/bin/streamlit ] && echo $(VENV)/bin/streamlit || echo streamlit)

# These are names, not files. Without this line a stray file called "build" or
# "deploy" would make the target look up to date and silently stop running.
.PHONY: run build load deploy pods forward-prom \
        load-start load-stop capacity collect bench ui retrain

# Local dev loop: 1s warm-up instead of 15s, and restart on every save.
run:
	STARTUP_DELAY_S=1 uvicorn app.main:app --reload --port $(APP_PORT)

# Bake the app image. Re-run this before `load` after any code change.
build:
	docker build -t traffic-app:v1 .

# Copy the image into the kind node — imagePullPolicy: Never has no registry to fall back on.
load:
	kind load docker-image traffic-app:v1 --name autoscale

# Apply every manifest in k8s/ (deployment, service, servicemonitor, hpa).
# NOT recursive, so k8s/load/ is skipped on purpose — the load generator and
# the capacity Job are started explicitly, never as a side effect of deploying.
deploy:
	kubectl apply -f k8s/

# Watch the rollout; the 0/1 -> 1/1 flip is the 15s readiness gap.
pods:
	kubectl get pods -w

# There is deliberately NO forward-app target. `kubectl port-forward svc/...`
# resolves the Service to ONE pod and pins every request to it, so laptop-side
# load could never show a benefit from scaling. k6 runs in-cluster instead
# (k8s/load/k6.yaml) and reaches the app directly, so nothing on the Mac needs
# port 5000 or 8000 at all.

# Reach the Prometheus UI at localhost:$(PROM_PORT).
forward-prom:
	kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus $(PROM_PORT):9090

# --- load generation, IN-CLUSTER --------------------------------------------
# k6 runs as a pod, not on the Mac. `kubectl port-forward svc/traffic-app`
# resolves the Service to ONE pod and pins all traffic to it (measured: 6.94
# req/s on one pod, 0.00 on the other three), so laptop-side load can never
# demonstrate a benefit from scaling. Sending to the ClusterIP from inside the
# cluster lets kube-proxy spread connections across every Ready endpoint.

# Ship load/ into a ConfigMap and start the generator. The rollout restart is
# required: editing a ConfigMap does not restart pods already mounting it, so
# without it a script change silently keeps running the old version.
load-start:
	kubectl create configmap k6-scripts --from-file=load/ --dry-run=client -o yaml | kubectl apply -f -
	kubectl apply -f k8s/load/k6.yaml
	kubectl scale deploy/k6-load --replicas=1
	kubectl rollout restart deploy/k6-load

load-stop:
	kubectl scale deploy/k6-load --replicas=0

# Step 25: one pod's capacity. Requires 1 replica and no HPA, or you measure
# the cluster's ability to scale rather than a single pod's ceiling.
capacity:
	kubectl delete job k6-capacity --ignore-not-found
	kubectl create configmap k6-scripts --from-file=load/ --dry-run=client -o yaml | kubectl apply -f -
	kubectl apply -f k8s/load/k6-capacity.yaml
	kubectl wait --for=condition=complete job/k6-capacity --timeout=15m
	kubectl logs job/k6-capacity | tail -25

# Copy Prometheus history into data/traffic.parquet every 10 minutes. The
# 6h lookback means running LESS often than every 6 hours loses history
# permanently; every 10 minutes just means a crash costs at most 10 minutes.
collect:
	while true; do $(PY) collect.py; sleep 600; done

# --- the A/B benchmark -------------------------------------------------------
# One 20-minute run:   make bench RUN=A1
#
# Records the k6 summary to bench/<RUN>.json plus the run's start/end epoch to
# bench/<RUN>.start and .end. Pod-seconds is not captured live: Prometheus
# already stores the replica count and keeps 15 days, so analyze.py replays the
# window afterwards. That is half the result — a latency win bought with far
# more compute is not a win, and a benchmark reporting only p99 is not honest.
#
# The continuous daily.js load MUST be off (`make load-stop`) or both arms are
# serving a second, uncontrolled workload on top of the exam paper.
# SCRIPT selects the scenario, default benchmark.js (the 4x step). Use
# SCRIPT=ramp.js for the predictable-ramp scenario — the one a forecaster can
# actually anticipate. Run names should say which: A1s/B1s for step,
# A1r/B1r for ramp, or the two scenarios' results get averaged together.
bench:
	@test -n "$(RUN)" || (echo "usage: make bench RUN=A1 [SCRIPT=ramp.js]"; exit 1)
	@test "$$(kubectl get deploy k6-load -o jsonpath='{.spec.replicas}')" = "0" \
	  || (echo "ERROR: daily.js load is still running — run 'make load-stop' first"; exit 1)
	kubectl delete job k6-benchmark --ignore-not-found
	kubectl create configmap k6-scripts --from-file=load/ --dry-run=client -o yaml | kubectl apply -f -
	@mkdir -p bench
	@sed -e 's/PLACEHOLDER/$(RUN)/' -e 's/SCRIPTNAME/$(or $(SCRIPT),benchmark.js)/' \
	  k8s/load/k6-benchmark.yaml | kubectl apply -f -
	@echo "run $(RUN) started — 20 minutes"
	@date -u +%s > bench/$(RUN).start
	kubectl wait --for=condition=complete job/k6-benchmark --timeout=30m
	@kubectl logs job/k6-benchmark \
	  | sed -n '/===BENCH_JSON_START===/,/===BENCH_JSON_END===/p' \
	  | sed '1d;$$d' > bench/$(RUN).json
	@date -u +%s > bench/$(RUN).end
	@echo "wrote bench/$(RUN).json  (window $(RUN).start -> $(RUN).end)"

# --- the UI ------------------------------------------------------------------
# Two pages. "Benchmark replay" needs nothing but bench/replay.json, so it works
# with the cluster switched off. "Live forecast" needs `make forward-prom` and
# traffic running, and is the view that shows a forecast beside what actually
# happened next — the only check that catches train/serve skew.
ui:
	$(STREAMLIT) run dashboard.py

# Re-freeze the benchmark runs out of Prometheus. Only needed after new runs;
# Prometheus keeps 15 days, this file keeps them forever.
replay-data:
	$(PY) export_replay.py

# --- keeping the model current -----------------------------------------------
# Scores a freshly-trained candidate against the live model on data collected
# SINCE the live model was trained, and swaps only on a real improvement. Safe
# to run on a timer: with no new data it declines and says so.
#
# To schedule it daily at 3am (`crontab -e`), noting that cron has almost no
# PATH and no venv, so both must be spelled out:
#
#   0 3 * * * cd /path/to/predictive-autoscaling && .venv/bin/python retrain.py \
#             >> logs/retrain.log 2>&1
#
# It only reads data/traffic.parquet, so `make collect` has to be running too —
# otherwise it will keep finding nothing new, correctly and forever.
retrain:
	$(PY) retrain.py

retrain-check:
	$(PY) retrain.py --dry-run
