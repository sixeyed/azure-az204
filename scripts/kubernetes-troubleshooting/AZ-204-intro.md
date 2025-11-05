# Kubernetes Troubleshooting: AZ-204 Exam Focus

Great work! This troubleshooting lab addresses the "Monitor, troubleshoot, and optimize Azure solutions" objective in the AZ-204 exam. Diagnostic skills are essential for Azure Kubernetes Service.

## What We'll Cover

We'll examine pod troubleshooting commands the exam tests including kubectl get pods for status overview, kubectl describe pod for detailed events and conditions, kubectl logs for container output with --previous flag for crashed containers, and kubectl exec for interactive debugging inside running containers.

We'll explore common pod problems that appear in exam scenarios. Pending status indicates scheduling failures from insufficient resources, node selector mismatches, or taint/toleration issues. CrashLoopBackOff suggests application errors requiring log investigation. ImagePullBackOff indicates registry authentication or image naming problems. Error status points to configuration issues or missing dependencies.

You'll master networking troubleshooting where service DNS resolution failures require checking CoreDNS status and service configurations, connection timeouts suggest network policy blocks or health probe failures, and Ingress routing problems need controller logs and rule validation.

The exam tests configuration troubleshooting including missing ConfigMaps or Secrets causing ContainerCreating status, incorrect volume mounts preventing pod startup, environment variable errors from typos or missing keys, and RBAC denying service account permissions.

We'll cover Azure-specific troubleshooting where AKS node issues appear in Azure Portal diagnostics, Azure Monitor Container Insights provides cluster and pod metrics, Log Analytics queries analyze logs across services, and Azure Support creates diagnostic logs for Microsoft support.

You'll understand resource exhaustion scenarios tested on the exam including nodes hitting capacity limits preventing new pod scheduling, resource quotas blocking namespace deployments, memory pressure causing pod evictions, and disk pressure from full nodes.

The exam includes systematic debugging approaches: start with pod status, check events for error messages, examine logs for application errors, verify configuration and secrets, test network connectivity, check node and cluster health, and review Azure-specific integrations.

Master troubleshooting methodology, kubectl diagnostic commands, and Azure monitoring tools for the AZ-204!
