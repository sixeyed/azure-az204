# Kubernetes Container Probes: AZ-204 Exam Focus

Great work! This container probes lab directly supports the "Implement containerized solutions" objective in the AZ-204 exam. Understanding container health monitoring is essential for developing production-ready applications in Azure Kubernetes Service.

## What We'll Cover

We'll examine the three probe types that the exam expects you to distinguish. Readiness probes determine if containers are ready to receive traffic - removing pods from service endpoints when they fail. Liveness probes determine if containers need restarting - killing and recreating pods when they fail. Startup probes disable other checks until applications finish initializing - preventing false-positive failures during long startup times.

We'll explore the three implementation methods you need to understand. HTTP probes make GET requests expecting success status codes, perfect for REST APIs and web applications. TCP probes check if ports are accepting connections, ideal for databases and non-HTTP services. Exec probes run commands inside containers for custom health check logic.

The exam tests your knowledge of probe configuration parameters including initialDelaySeconds for startup wait time, periodSeconds for check frequency, timeoutSeconds for response deadlines, failureThreshold for consecutive failures before action, and successThreshold for consecutive successes after failure.

You'll master container lifecycle management - how startup probes run first before enabling readiness and liveness probes, how failed readiness probes remove pods from endpoints immediately while keeping them running, and how failed liveness probes trigger container restarts incrementing the restart count.

We'll cover Azure Kubernetes Service integration with probe failures appearing in Azure Monitor container insights, Application Insights for correlating probe failures with application telemetry, and Log Analytics for analyzing patterns in container restarts and health check results.

The exam includes best practices: always implement health check endpoints that verify functionality, use both readiness and liveness probes in production, set appropriate timeouts and thresholds to avoid unnecessary restarts, and design health endpoints that check dependencies not just process existence.

Master container probe configuration and troubleshooting for the AZ-204!
