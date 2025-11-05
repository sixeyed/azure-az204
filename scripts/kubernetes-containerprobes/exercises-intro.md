# Kubernetes Container Probes: Exercises Introduction

We've covered the three types of container probes and why they're essential for production-ready applications. Now let's deploy real applications with different probe configurations and see how Kubernetes responds to failures.

## What You'll Do

You'll start with self-healing apps using readiness probes. You'll deploy the whoami application and intentionally trigger it to return 503 errors. Without readiness probes, Kubernetes keeps sending traffic to the failed pod, causing user errors.

Then you'll add readiness probe configuration that checks the /health endpoint every five seconds. When a pod fails its readiness check, Kubernetes automatically removes it from service endpoints, isolating the problem while keeping the container running.

Next, you'll implement self-repairing apps with liveness probes. These don't just isolate unhealthy pods - they actually restart them. You'll watch as a failed pod first becomes not ready, then after multiple liveness probe failures, the pod restarts and rejoins the service automatically.

You'll explore other probe types beyond HTTP probes. TCP socket checks work perfectly for databases and non-HTTP services, simply verifying the port is accepting connections. Exec probes run commands inside containers for custom health check logic that can't be expressed as HTTP or TCP checks.

The lab challenge presents a Random Number Generator API with reliability problems. You'll need to configure both readiness probes to stop traffic to failed pods and liveness probes to restart them, running five replicas with health checks on the /healthz endpoint.

The key learning: Container probes enable self-healing infrastructure - detect problems with readiness probes, isolate failed pods from traffic, and automatically recover with liveness probes, all without manual intervention.
