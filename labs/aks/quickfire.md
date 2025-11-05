# Azure Kubernetes Service (AKS) - Quickfire Questions

## Question 1
What is Azure Kubernetes Service (AKS)?


- A) Database service
- B) VM service
- C) Managed Kubernetes service simplifying cluster deployment and management
- D) Storage service

**Answer: C**
AKS provides managed Kubernetes, handling control plane management, upgrades, and monitoring.
---
## Question 2
What does "managed" mean in AKS?


- A) Self-managed
- B) Microsoft manages everything
- C) Azure manages control plane (API server, etcd); you manage worker nodes
- D) Fully automated, no control

**Answer: C**
Azure handles control plane availability, upgrades, patching; you manage node pools and workloads.
---
## Question 3
What are node pools in AKS?


- A) Network pools
- B) Groups of nodes with same VM size/configuration within cluster
- C) Storage pools
- D) Database pools

**Answer: B**
Node pools enable different VM sizes for different workloads (e.g., CPU-intensive, GPU, spot instances).
---
## Question 4
Is the AKS control plane free?


- A) Per-request pricing
- B) Expensive
- C) Fixed monthly fee
- D) Yes, you only pay for worker nodes (VMs), not control plane

**Answer: D**
AKS control plane is free; costs are for VM nodes, storage, networking, and associated resources.
---
## Question 5
What container registry integrates best with AKS?


- A) Azure Container Registry (ACR) with native integration and managed identity
- B) Local registry only
- C) No registry support
- D) Docker Hub only

**Answer: A**
ACR integrates seamlessly with AKS, supporting managed identity authentication.
---
## Question 6
Can AKS scale automatically?


- A) Fixed size
- B) Manual only
- C) Yes, using cluster autoscaler (nodes) and Horizontal Pod Autoscaler (pods)
- D) No scaling

**Answer: C**
Cluster autoscaler adds/removes nodes; HPA scales pod replicas based on metrics.
---
## Question 7
What networking options does AKS support?


- A) One option
- B) kubenet (basic) and Azure CNI (advanced VNet integration)
- C) Public only
- D) No networking

**Answer: B**
Kubenet for simple scenarios; Azure CNI for VNet integration, private IPs, network policies.
---
## Question 8
Can AKS integrate with Azure Active Directory?


- A) Not supported
- B) Only local accounts
- C) No authentication
- D) Yes, for Kubernetes RBAC using Azure AD identities

**Answer: D**
Azure AD integration enables RBAC using organization identities and groups.
---
## Question 9
What monitoring is available for AKS?


- A) Only basic metrics
- B) Manual logging only
- C) Container Insights (Azure Monitor), Prometheus, Grafana
- D) No monitoring

**Answer: C**
Container Insights provides comprehensive monitoring, metrics, and log analytics.
---
## Question 10
Can you run Windows containers on AKS?


- A) Windows only
- B) Yes, AKS supports Windows Server node pools alongside Linux nodes
- C) Linux only
- D) Not supported

**Answer: B**
AKS supports heterogeneous clusters with Linux and Windows node pools.