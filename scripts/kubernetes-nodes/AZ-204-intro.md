# Kubernetes Nodes: AZ-204 Exam Focus

Great work! This nodes lab supports the "Implement containerized solutions" objective in the AZ-204 exam. Understanding cluster infrastructure and workload placement is essential for Azure Kubernetes Service.

## What We'll Cover

We'll examine node architecture in Azure Kubernetes Service where nodes are Azure Virtual Machines running the kubelet agent. Understand VM sizes, availability zones, and node pools as fundamental AKS concepts the exam tests.

We'll explore resource management with node capacity versus allocatable resources. Capacity is total node resources while allocatable excludes system reservations. Know that resource requests determine scheduling while limits control runtime usage.

You'll master pod scheduling mechanisms including resource requests and limits for scheduler placement decisions, node selectors for hardware-specific requirements, node affinity and anti-affinity for complex placement rules, taints and tolerations for dedicated node protection, and pod priority for critical workload guarantees.

The exam tests Azure-specific node concepts including node pools for grouping nodes with different VM sizes, system node pool for AKS system components, user node pools for application workloads, and autoscaling with cluster autoscaler adding/removing nodes based on demand.

We'll cover maintenance operations that the exam includes: cordoning nodes to prevent new scheduling, draining nodes to evict pods gracefully, and upgrading AKS node pools with rolling updates maintaining availability.

You'll understand monitoring and troubleshooting with Azure Monitor tracking node metrics, node conditions indicating health status, and resource pressure scenarios causing scheduling failures.

Master node management, scheduling strategies, and AKS-specific configurations for the AZ-204!
