# Kubernetes Pods: AZ-204 Exam Focus

Great work! This pods lab is foundational for the "Implement containerized solutions" objective in the AZ-204 exam. Understanding pod architecture is essential for all Kubernetes work.

## What We'll Cover

We'll examine pod architecture as the atomic unit in Kubernetes where one or more containers share network namespace, storage volumes, and IPC namespace. Know that while pods can run multiple containers, single-container pods are most common.

We'll explore the container runtime with Azure Kubernetes Service supporting containerd for OCI-compliant container execution. Understand image pulling from Azure Container Registry, container startup and shutdown hooks, and restart policies.

You'll master resource management critical for the exam: requests define minimum guaranteed resources used by scheduler for placement decisions, limits define maximum resources preventing container resource exhaustion, and over-commitment occurs when limits exceed node capacity but requests fit.

The exam tests pod networking concepts including pod-to-pod communication via cluster network, DNS-based service discovery using cluster DNS, network policies for traffic control between pods, and Azure CNI versus kubenet networking modes in AKS.

We'll cover multi-container patterns that appear on the exam: sidecar containers for auxiliary functions like logging agents, init containers for setup tasks before main containers start, and ephemeral containers for debugging running pods without rebuilding images.

You'll understand pod lifecycle states tested in exam scenarios: Pending when waiting for scheduling or image pulls, Running with at least one container executing, Succeeded for completed batch jobs, Failed when containers exit with errors, and Unknown when kubelet communication fails.

The exam includes security contexts with runAsNonRoot preventing root execution, fsGroup setting volume permissions, capabilities controlling Linux privileges, and Azure Policy enforcing pod security standards across AKS.

Master pod concepts, resource management, and security configuration for the AZ-204!
