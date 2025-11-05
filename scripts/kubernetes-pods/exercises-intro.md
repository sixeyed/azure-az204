# Kubernetes Pods: Exercises Introduction

We've covered how pods are the smallest deployable units in Kubernetes that can contain one or more containers sharing network and storage. Now let's create and manage pods directly.

## What You'll Do

You'll create your first pod using kubectl run for quick imperative creation and kubectl apply with YAML manifests for declarative management. You'll understand that while you can create pods directly, Deployments are preferred for production.

Then you'll explore pod networking where all containers in a pod share the same IP address and can communicate via localhost. You'll see how pods get unique IPs from the cluster network enabling pod-to-pod communication.

You'll work with multi-container pods including sidecar patterns for logging and monitoring, ambassador patterns for proxy functionality, and adapter patterns for standardizing interfaces. Containers in pods share volumes and network namespace.

Next, you'll examine pod lifecycle understanding pending status during scheduling, running status when containers are active, succeeded status for completed jobs, failed status when containers exit with errors, and unknown status for communication failures.

You'll configure resource requests and limits where requests guarantee minimum resources for scheduling and limits cap maximum usage preventing resource exhaustion. Kubernetes uses these for bin-packing pods onto nodes efficiently.

You'll explore pod security contexts including running as non-root users, setting file system groups, defining capabilities, and using security policies. Azure Policy for Kubernetes enforces pod security standards.

The lab challenge asks you to debug pod issues using kubectl describe, kubectl logs, and kubectl exec commands essential for troubleshooting failed containers and investigating runtime behavior.

The key learning: While pods are rarely created directly in production, understanding pod concepts is fundamental as Deployments, StatefulSets, and DaemonSets all manage pods following these same principles.
