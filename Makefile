# Ports live here and nowhere else, so changing one is a single edit.
APP_PORT  = 5000
PROM_PORT = 9090

# These are names, not files. Without this line a stray file called "build" or
# "deploy" would make the target look up to date and silently stop running.
.PHONY: run build load deploy pods forward-app forward-prom \
        load-start load-stop capacity collect

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

# Reach the app from the Mac at localhost:$(APP_PORT).
forward-app:
	kubectl port-forward svc/traffic-app $(APP_PORT):80

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
	while true; do python collect.py; sleep 600; done
