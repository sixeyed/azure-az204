# Azure Kubernetes Service (AKS) - Quickfire Questions

## Question 1
What is Azure Kubernetes Service (AKS)?

- A) VM service
- B) Managed Kubernetes service simplifying cluster deployment and management
- C) Storage service
- D) Database service

**Answer: B**
AKS provides managed Kubernetes, handling control plane management, upgrades, and monitoring.

---

## Question 2
What does "managed" mean in AKS?

- A) Fully automated, no control
- B) Azure manages control plane (API server, etcd); you manage worker nodes
- C) Microsoft manages everything
- D) Self-managed

**Answer: B**
Azure handles control plane availability, upgrades, patching; you manage node pools and workloads.

---

## Question 3
What are node pools in AKS?

- A) Storage pools
- B) Groups of nodes with same VM size/configuration within cluster
- C) Database pools
- D) Network pools

**Answer: B**
Node pools enable different VM sizes for different workloads (e.g., CPU-intensive, GPU, spot instances).

---

## Question 4
Is the AKS control plane free?

- A) Expensive
- B) Yes, you only pay for worker nodes (VMs), not control plane
- C) Fixed monthly fee
- D) Per-request pricing

**Answer: B**
AKS control plane is free; costs are for VM nodes, storage, networking, and associated resources.

---

## Question 5
What container registry integrates best with AKS?

- A) Docker Hub only
- B) Azure Container Registry (ACR) with native integration and managed identity
- C) No registry support
- D) Local registry only

**Answer: B**
ACR integrates seamlessly with AKS, supporting managed identity authentication.

---

## Question 6
Can AKS scale automatically?

- A) Manual only
- B) Yes, using cluster autoscaler (nodes) and Horizontal Pod Autoscaler (pods)
- C) No scaling
- D) Fixed size

**Answer: B**
Cluster autoscaler adds/removes nodes; HPA scales pod replicas based on metrics.

---

## Question 7
What networking options does AKS support?

- A) One option
- B) kubenet (basic) and Azure CNI (advanced VNet integration)
- C) No networking
- D) Public only

**Answer: B**
Kubenet for simple scenarios; Azure CNI for VNet integration, private IPs, network policies.

---

## Question 8
Can AKS integrate with Azure Active Directory?

- A) No authentication
- B) Yes, for Kubernetes RBAC using Azure AD identities
- C) Only local accounts
- D) Not supported

**Answer: B**
Azure AD integration enables RBAC using organization identities and groups.

---

## Question 9
What monitoring is available for AKS?

- A) No monitoring
- B) Container Insights (Azure Monitor), Prometheus, Grafana
- C) Only basic metrics
- D) Manual logging only

**Answer: B**
Container Insights provides comprehensive monitoring, metrics, and log analytics.

---

## Question 10
Can you run Windows containers on AKS?

- A) Linux only
- B) Yes, AKS supports Windows Server node pools alongside Linux nodes
- C) Windows only
- D) Not supported

**Answer: B**
AKS supports heterogeneous clusters with Linux and Windows node pools.
