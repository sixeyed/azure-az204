---
theme: default
background: https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Kubernetes Service
  Managed Kubernetes for AZ-204
drawings:
  persist: false
transition: slide-left
title: Azure Kubernetes Service
mdc: true
---

# Azure Kubernetes Service

Managed Kubernetes on Azure

<div class="abs-bottom-10 left-10">
  <carbon-kubernetes class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome to AKS

<!--
METADATA:
sentence: In this video, we'll explore one of Azure's most powerful container orchestration services.
search_anchor: this video, we'll explore one
-->
<v-click>

<div class="text-xl mt-8">
Explore one of Azure's most powerful<br/>container orchestration services
</div>

</v-click>

---
layout: section
---

# What is AKS?

---

# Kubernetes

<v-click>

<div class="mt-4">
  <carbon-kubernetes class="text-8xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Kubernetes is an open-source platform for managing containerized applications.
search_anchor: Kubernetes is an open-source platform
-->
<v-click>

<div class="mt-8 text-xl text-center">
Open-source platform for managing<br/>containerized applications
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    A[Open Source<br/>Kubernetes] --> B[Vendor Packages]
    B --> C[AKS]
    B --> D[EKS]
    B --> E[GKE]
    style A fill:#326ce5
    style C fill:#0078d4
```

</div>

</v-click>

---

# Azure Kubernetes Service (AKS)

<v-click>

<div class="mt-4">
  <carbon-logo-microsoft-azure class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Azure Kubernetes Service, or AKS, is Microsoft's managed Kubernetes offering.
search_anchor: Azure Kubernetes Service, or AKS
-->
<v-click>

<div class="mt-8 text-xl text-center">
Microsoft's managed Kubernetes offering
</div>

</v-click>

<!--
METADATA:
sentence: With AKS, you get all the power of Kubernetes without the overhead of managing the infrastructure.
search_anchor: AKS, you get all the
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-checkmark-filled class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Full Kubernetes Power</div>
  </div>
  <div class="text-center">
    <carbon-close-filled class="text-5xl text-red-400" />
    <div class="text-sm mt-3">No Infrastructure Overhead</div>
  </div>
</div>

</v-click>

---

# How AKS Works

<!--
METADATA:
sentence: You create an AKS cluster and deploy your applications using the standard Kubernetes model.
search_anchor: You create an AKS cluster
-->
<v-click>

<div class="mt-4 text-center text-xl">
You create cluster and deploy applications
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph TB
    You[You] -->|Deploy| Apps[Applications]
    Apps --> Cluster[AKS Cluster]
    Azure[Azure] -->|Manages| Infrastructure[VMs + Kubernetes]
    Infrastructure --> Cluster
    style You fill:#51cf66
    style Azure fill:#0078d4
    style Cluster fill:#326ce5
```

</div>

</v-click>

<!--
METADATA:
sentence: Behind the scenes, Azure handles the heavy lifting - provisioning virtual machines for your cluster nodes, installing and configuring Kubernetes, and maintaining the entire infrastructure.
search_anchor: Behind the scenes, Azure handles
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Azure handles provisioning, configuring, and maintaining infrastructure
</div>

</v-click>

---

# Behind the Scenes

<!--
METADATA:
sentence: Behind the scenes, Azure handles the heavy lifting - provisioning virtual machines for your cluster nodes, installing and configuring Kubernetes, and maintaining the entire infrastructure.
search_anchor: Behind the scenes, Azure handles
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-virtual-machine class="text-4xl text-blue-400" />
  <span class="text-lg">Provisioning virtual machines for cluster nodes</span>
</div>

</v-click>

<!--
METADATA:
sentence: You create an AKS cluster and deploy your applications using the standard Kubernetes model.
search_anchor: You create an AKS cluster
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-installation class="text-4xl text-green-400" />
  <span class="text-lg">Installing and configuring Kubernetes</span>
</div>

</v-click>

<!--
METADATA:
sentence: With AKS, you get all the power of Kubernetes without the overhead of managing the infrastructure.
search_anchor: AKS, you get all the
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-tools class="text-4xl text-purple-400" />
  <span class="text-lg">Maintaining the entire infrastructure</span>
</div>

</v-click>

<!--
METADATA:
sentence: Node pools are groups of nodes that share the same configuration.
search_anchor: Node pools are groups of
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Azure does the heavy lifting
</div>

</v-click>

---
layout: section
---

# Why Use AKS?

---

# Simplifying Complex Tasks

<!--
METADATA:
sentence: AKS simplifies many complex tasks that would otherwise require significant expertise and effort: First, scaling your cluster.
search_anchor: AKS simplifies many complex tasks
-->
<v-click>

<div class="mt-8 text-center text-xl">
AKS simplifies tasks that require<br/>significant expertise and effort
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Complex[Complex Tasks] --> AKS[AKS]
    AKS --> Simple[Simple Operations]
    style Complex fill:#ff6b6b
    style AKS fill:#0078d4
    style Simple fill:#51cf66
```

</div>

</v-click>

---

# Benefit 1: Scaling

<v-click>

<div class="mt-4">
  <carbon-scale class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: This will give you a solid foundation before tackling more complex scenarios.
search_anchor: This will give you a
-->
<v-click>

<div class="mt-8 text-xl text-center">
Need more capacity?
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph LR
    A[3 Nodes] -->|Scale Up| B[10 Nodes]
    B -->|Scale Down| C[5 Nodes]
    style A fill:#51cf66
    style B fill:#0078d4
    style C fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: AKS makes it easy to add or remove nodes as your workload changes.
search_anchor: AKS makes it easy to
-->
<v-click>

<div class="mt-8 text-center text-lg">
Easy to add or remove nodes as workload changes
</div>

</v-click>

---

# Benefit 2: Upgrades

<v-click>

<div class="mt-4">
  <carbon-upgrade class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Keeping Kubernetes up to date can be challenging, but AKS streamlines the upgrade process.
search_anchor: Keeping Kubernetes up to date
-->
<v-click>

<div class="mt-8 text-xl text-center">
Keeping Kubernetes up to date
</div>

</v-click>

<!--
METADATA:
sentence: Keeping Kubernetes up to date can be challenging, but AKS streamlines the upgrade process.
search_anchor: Keeping Kubernetes up to date
-->
<v-click>

<div class="mt-8 flex justify-center gap-16">
  <div class="text-center">
    <carbon-warning class="text-6xl text-red-400" />
    <div class="text-lg mt-4">Manual K8s</div>
    <div class="text-sm mt-2 opacity-70">Complex & risky</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-lg mt-4">AKS</div>
    <div class="text-sm mt-2 opacity-70">Streamlined process</div>
  </div>
</div>

</v-click>

---

# Benefit 3: Integration

<v-click>

<div class="mt-4">
  <carbon-integration class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph TB
    AKS[AKS Cluster]
    AKS --> ACR[Container Registry]
    AKS --> Storage[Azure Storage]
    AKS --> Monitor[Azure Monitor]
    AKS --> AAD[Azure AD]
    style AKS fill:#0078d4
    style ACR fill:#51cf66
    style Storage fill:#51cf66
    style Monitor fill:#51cf66
    style AAD fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Container Registry Integration: AKS can be integrated with Azure Container Registry, or ACR.
search_anchor: Container Registry Integration: AKS can
-->
<v-click>

<div class="mt-8 text-center text-xl">
Seamless integration with Azure services
</div>

</v-click>

<!--
METADATA:
sentence: AKS integrates seamlessly with other Azure services, creating a cohesive cloud ecosystem for your applications.
search_anchor: AKS integrates seamlessly with other
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Creating a cohesive cloud ecosystem
</div>

</v-click>

---
layout: section
---

# Key Features to Explore

---

# Node Configuration

<v-click>

<div class="mt-4">
  <carbon-virtual-machine class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Node pools are groups of nodes that share the same configuration.
search_anchor: Node pools are groups of
-->
<v-click>

<div class="mt-8 text-xl text-center">
Specify the number of nodes
</div>

</v-click>

<!--
METADATA:
sentence: Node Pools: This is a powerful feature.
search_anchor: Node Pools: This is a
-->
<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <div class="text-4xl font-bold text-blue-400">3</div>
    <div class="text-sm mt-2">Nodes</div>
  </div>
  <div class="text-4xl opacity-50">×</div>
  <div class="text-center">
    <div class="text-4xl font-bold text-green-400">D4s_v3</div>
    <div class="text-sm mt-2">VM Size</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: AKS makes it easy to add or remove nodes as your workload changes.
search_anchor: AKS makes it easy to
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Choose VM size that matches your workload
</div>

</v-click>

---

# Presets

<v-click>

<div class="mt-4">
  <carbon-settings-adjust class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Presets: Azure provides preset configurations to help you get started quickly with common scenarios.
search_anchor: Presets: Azure provides preset configurations
-->
<v-click>

<div class="mt-8 text-xl text-center">
Azure provides preset configurations
</div>

</v-click>

<!--
METADATA:
sentence: Presets: Azure provides preset configurations to help you get started quickly with common scenarios.
search_anchor: Presets: Azure provides preset configurations
-->
<v-click>

<div class="mt-12 grid grid-cols-3 gap-6">
  <div class="text-center">
    <carbon-code class="text-4xl text-blue-400" />
    <div class="text-sm mt-2">Development</div>
  </div>
  <div class="text-center">
    <carbon-enterprise class="text-4xl text-purple-400" />
    <div class="text-sm mt-2">Production</div>
  </div>
  <div class="text-center">
    <carbon-data-enrichment class="text-4xl text-orange-400" />
    <div class="text-sm mt-2">Batch Processing</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Let's get started with hands-on exercises.
search_anchor: Let's get started with hands-on
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Get started quickly with common scenarios
</div>

</v-click>

---

# Node Pools

<v-click>

<div class="mt-4">
  <carbon-deployment-pattern class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Node pools are groups of nodes that share the same configuration.
search_anchor: Node pools are groups of
-->
<v-click>

<div class="mt-8 text-xl text-center">
Groups of nodes with same configuration
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph TB
    subgraph Cluster
        Pool1[Pool 1: 10 Linux Nodes]
        Pool2[Pool 2: 5 Linux + GPU]
        Pool3[Pool 3: 2 Windows Nodes]
    end
    style Pool1 fill:#51cf66
    style Pool2 fill:#ff6b6b
    style Pool3 fill:#ffd43b
```

</div>

</v-click>

<!--
METADATA:
sentence: This gives you tremendous flexibility in how you run different types of workloads.
search_anchor: This gives you tremendous flexibility
-->
<v-click>

<div class="mt-8 text-center text-lg">
Tremendous flexibility for different workload types
</div>

</v-click>

---

# Node Pool Example

<!--
METADATA:
sentence: AKS makes it easy to add or remove nodes as your workload changes.
search_anchor: AKS makes it easy to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <div class="w-12 h-12 bg-green-500 rounded flex items-center justify-center">
    <carbon-linux-alt class="text-2xl text-white" />
  </div>
  <div>
    <div class="text-lg">Pool 1: 10 Linux nodes</div>
    <div class="text-sm opacity-70">General workloads</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: For example, you might have ten Linux nodes in one pool, five Linux servers with GPUs in another pool, and two Windows servers in a third pool - all within the same cluster.
search_anchor: example, you might have ten
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <div class="w-12 h-12 bg-red-500 rounded flex items-center justify-center">
    <carbon-chip class="text-2xl text-white" />
  </div>
  <div>
    <div class="text-lg">Pool 2: 5 Linux nodes with GPUs</div>
    <div class="text-sm opacity-70">ML/AI workloads</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: AKS makes it easy to add or remove nodes as your workload changes.
search_anchor: AKS makes it easy to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <div class="w-12 h-12 bg-yellow-500 rounded flex items-center justify-center">
    <carbon-logo-windows class="text-2xl text-white" />
  </div>
  <div>
    <div class="text-lg">Pool 3: 2 Windows nodes</div>
    <div class="text-sm opacity-70">.NET workloads</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Node pools are groups of nodes that share the same configuration.
search_anchor: Node pools are groups of
-->
<v-click>

<div class="mt-8 text-center text-sm opacity-60">
All within the same cluster!
</div>

</v-click>

---

# Security

<v-click>

<div class="mt-4">
  <carbon-security class="text-6xl text-red-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Security: AKS clusters can be secured using standard Kubernetes Role-Based Access Control, or RBAC, which integrates directly with Azure Active Directory accounts.
search_anchor: Security: AKS clusters can be
-->
<v-click>

<div class="mt-8 text-xl text-center">
Kubernetes Role-Based Access Control (RBAC)
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    User[User] -->|Authenticate| AAD[Azure AD]
    AAD -->|RBAC| AKS[AKS Cluster]
    style AAD fill:#0078d4
    style AKS fill:#326ce5
```

</div>

</v-click>

<!--
METADATA:
sentence: Security: AKS clusters can be secured using standard Kubernetes Role-Based Access Control, or RBAC, which integrates directly with Azure Active Directory accounts.
search_anchor: Security: AKS clusters can be
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Integrates directly with Azure Active Directory
</div>

</v-click>

---

# Container Registry Integration

<v-click>

<div class="mt-4">
  <carbon-catalog class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Container Registry Integration: AKS can be integrated with Azure Container Registry, or ACR.
search_anchor: Container Registry Integration: AKS can
-->
<v-click>

<div class="mt-8 text-xl text-center">
AKS integrates with Azure Container Registry (ACR)
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    ACR[ACR<br/>Private Images] -->|No Extra Auth| AKS[AKS Cluster]
    style ACR fill:#0078d4
    style AKS fill:#326ce5
```

</div>

</v-click>

<!--
METADATA:
sentence: This means you can run containers from private ACR images without any extra authentication configuration.
search_anchor: This means you can run
-->
<v-click>

<div class="mt-8 text-center text-lg">
Run private containers without extra authentication
</div>

</v-click>

---
layout: section
---

# Production Considerations

---

# Production-Grade AKS

<v-click>

<div class="mt-4">
  <carbon-enterprise class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Production Considerations Now, it's important to understand that production-grade AKS deployments can get quite complicated.
search_anchor: Production Considerations Now, it's important
-->
<v-click>

<div class="mt-8 text-xl text-center">
Production deployments can get quite complicated
</div>

</v-click>

<!--
METADATA:
sentence: You'll need to consider networking, security policies, monitoring, and high availability.
search_anchor: You'll need to consider networking
-->
<v-click>

<div class="mt-10 grid grid-cols-2 gap-6">
  <div class="flex items-center gap-3">
    <carbon-network-3 class="text-3xl text-blue-400" />
    <span>Networking</span>
  </div>
  <div class="flex items-center gap-3">
    <carbon-security class="text-3xl text-red-400" />
    <span>Security policies</span>
  </div>
  <div class="flex items-center gap-3">
    <carbon-chart-line class="text-3xl text-green-400" />
    <span>Monitoring</span>
  </div>
  <div class="flex items-center gap-3">
    <carbon-availability class="text-3xl text-purple-400" />
    <span>High availability</span>
  </div>
</div>

</v-click>

---

# Our Approach

<!--
METADATA:
sentence: However, for learning purposes, we'll start with a simple deployment using the Azure CLI.
search_anchor: However, for learning purposes, we'll
-->
<v-click>

<div class="mt-8 text-center text-xl">
For learning purposes...
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    A[Simple Deployment] --> B[Azure CLI]
    B --> C[Solid Foundation]
    C --> D[Complex Scenarios]
    style A fill:#51cf66
    style C fill:#0078d4
    style D fill:#ffd43b
```

</div>

</v-click>

<!--
METADATA:
sentence: This will give you a solid foundation before tackling more complex scenarios.
search_anchor: This will give you a
-->
<v-click>

<div class="mt-12 text-center text-lg">
Start simple, build solid foundation
</div>

</v-click>

<!--
METADATA:
sentence: This will give you a solid foundation before tackling more complex scenarios.
search_anchor: This will give you a
-->
<v-click>

<div class="mt-4 text-center text-sm opacity-70">
Then tackle more complex scenarios
</div>

</v-click>

---
layout: section
---

# What's Next

---

# In This Lesson

<!--
METADATA:
sentence: You create an AKS cluster and deploy your applications using the standard Kubernetes model.
search_anchor: You create an AKS cluster
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Creating an AKS cluster</span>
</div>

</v-click>

<!--
METADATA:
sentence: Node Pools: This is a powerful feature.
search_anchor: Node Pools: This is a
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deploy class="text-4xl text-green-400" />
  <span class="text-lg">Deploying a sample application</span>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Kubernetes Service, or AKS, is Microsoft's managed Kubernetes offering.
search_anchor: Azure Kubernetes Service, or AKS
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-search class="text-4xl text-purple-400" />
  <span class="text-lg">Exploring how Kubernetes works in Azure</span>
</div>

</v-click>

---

# Kubernetes Portability

<v-click>

<div class="mt-8">

```mermaid
graph TB
    YAML[Kubernetes YAML]
    YAML --> AKS[AKS]
    YAML --> EKS[EKS]
    YAML --> GKE[GKE]
    YAML --> Local[Local K8s]
    style YAML fill:#326ce5
    style AKS fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: You'll use the same Kubernetes tools and YAML specifications that work on any Kubernetes cluster, demonstrating the portability and consistency that makes Kubernetes so powerful.
search_anchor: You'll use the same Kubernetes
-->
<v-click>

<div class="mt-12 text-center text-xl">
Same tools and YAML specifications
</div>

</v-click>

<!--
METADATA:
sentence: You'll use the same Kubernetes tools and YAML specifications that work on any Kubernetes cluster, demonstrating the portability and consistency that makes Kubernetes so powerful.
search_anchor: You'll use the same Kubernetes
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Work on any Kubernetes cluster
</div>

</v-click>

<!--
METADATA:
sentence: You'll use the same Kubernetes tools and YAML specifications that work on any Kubernetes cluster, demonstrating the portability and consistency that makes Kubernetes so powerful.
search_anchor: You'll use the same Kubernetes
-->
<v-click>

<div class="mt-6 text-center text-lg text-green-400">
Portability and consistency that makes Kubernetes powerful
</div>

</v-click>

---
layout: center
class: text-center
---

<div>

<v-click>

<carbon-play-outline class="text-8xl text-green-400 inline-block" />

</v-click>

<!--
METADATA:
sentence: Let's get started with hands-on exercises.
search_anchor: Let's get started with hands-on
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: Let's get started with hands-on exercises.
search_anchor: Let's get started with hands-on
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Hands-on exercises with Azure Kubernetes Service
</div>

</v-click>

</div>
