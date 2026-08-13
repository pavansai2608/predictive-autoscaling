# Ports live here and nowhere else, so changing one is a single edit.
APP_PORT  = 5000
PROM_PORT = 9090

# These are names, not files. Without this line a stray file called "build" or
# "deploy" would make the target look up to date and silently stop running.
.PHONY: run build load deploy pods forward-app forward-prom

# Local dev loop: 1s warm-up instead of 15s, and restart on every save.
run:
	STARTUP_DELAY_S=1 uvicorn app.main:app --reload --port $(APP_PORT)

# Bake the app image. Re-run this before `load` after any code change.
build:
	docker build -t traffic-app:v1 .

# Copy the image into the kind node — imagePullPolicy: Never has no registry to fall back on.
load:
	kind load docker-image traffic-app:v1 --name autoscale

# Apply every manifest in k8s/ (deployment + service).
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
