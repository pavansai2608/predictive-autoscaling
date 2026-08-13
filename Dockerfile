# Python 3.11, not the 3.14 in .venv: every wheel we need has a 3.11 build, and
# this image only ever runs the app — the forecaster stays on the host.
FROM python:3.11-slim

# Unbuffered stdout, or uvicorn's logs sit in a pipe buffer and `kubectl logs`
# shows nothing while the pod warms up — exactly the window we need to watch.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# /srv rather than /app, so the package inside doesn't become /app/app. Keeping
# the repo-root layout means "app.main:app" is the same string here as locally.
WORKDIR /srv

# Requirements copied and installed before the source: pip only re-runs when the
# dependencies actually change, so editing main.py rebuilds in seconds instead
# of refetching every wheel.
COPY app/requirements.txt app/requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

COPY app/ app/

EXPOSE 8000

# Exec form, so uvicorn is PID 1 and receives SIGTERM directly. Under a shell it
# would not, and every scale-down would burn the full 30s termination grace
# period — which lands straight in the pod-seconds we are benchmarking.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
