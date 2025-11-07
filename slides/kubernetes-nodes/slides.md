---
theme: default
background: https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes Nodes
  Worker machines that run your containers - AZ-204
drawings:
  persist: false
transition: slide-left
title: Nodes
mdc: true
---

# Kubernetes Nodes

The Worker Machines

<div class="abs-bottom-10 left-10">
  <carbon-server class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Kubernetes Nodes<br/>The foundation of your cluster infrastructure
</div>

</v-click>

---
layout: section
---

# What Are Kubernetes Nodes?

---

# Worker Machines

<v-click>

<div class="mt-4">
  <carbon-server class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Virtual machine or physical server
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Where your containerized applications actually run
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Control[Control Plane<br/>Manages] --> Node1[Node 1<br/>Worker]
    Control --> Node2[Node 2<br/>Worker]
    Control --> Node3[Node 3<br/>Worker]
    Node1 --> Pods1[Runs Pods]
    Node2 --> Pods2[Runs Pods]
    Node3 --> Pods3[Runs Pods]
    style Control fill:#0078d4
    style Node1 fill:#51cf66
    style Node2 fill:#51cf66
    style Node3 fill:#51cf66
```

</div>

</v-click>

---

# The Workhorses

<v-click>

<div class="mt-12 text-center text-xl">
Nodes contain services necessary to run pods
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Managed by Kubernetes control plane
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    App[Deploy Application] --> Control[Control Plane]
    Control --> Schedule[Schedule Pods]
    Schedule --> Node[Available Nodes]
    style App fill:#ffd43b
    style Control fill:#0078d4
    style Schedule fill:#51cf66
    style Node fill:#51cf66
```

</div>

</v-click>

---
layout: section
---

# Node Architecture

---

# Inside a Node

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-network-4 class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">kubelet</span>
    <div class="text-sm mt-2 opacity-70">Primary node agent</div>
    <div class="text-sm opacity-70">Communicates with control plane</div>
    <div class="text-sm opacity-70">Ensures containers are running and healthy</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-container-software class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Container Runtime</span>
    <div class="text-sm mt-2 opacity-70">Actually runs your containers</div>
    <div class="text-sm opacity-70">In AKS: typically containerd</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-network-3 class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">kube-proxy</span>
    <div class="text-sm mt-2 opacity-70">Network proxy</div>
    <div class="text-sm opacity-70">Maintains network rules</div>
    <div class="text-sm opacity-70">Enables communication to your pods</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Node Pools in AKS

---

# Grouping Nodes

<v-click>

<div class="mt-4">
  <carbon-data-structured class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Node pool: group of nodes with same configuration
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Multiple node pools in single AKS cluster
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Cluster[AKS Cluster] --> Pool1[Node Pool 1<br/>CPU-Optimized]
    Cluster --> Pool2[Node Pool 2<br/>Memory-Optimized]
    Pool1 --> Compute[Compute-Intensive<br/>Workloads]
    Pool2 --> Database[Database<br/>Workloads]
    style Cluster fill:#0078d4
    style Pool1 fill:#51cf66
    style Pool2 fill:#51cf66
```

</div>

</v-click>

---

# Different VM Sizes

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-chip class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">CPU-Optimized</div>
    <div class="text-xs mt-2 opacity-70">Compute tasks</div>
  </div>
  <div class="text-center">
    <carbon-data-base class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Memory-Optimized</div>
    <div class="text-xs mt-2 opacity-70">Databases</div>
  </div>
  <div class="text-center">
    <carbon-data-storage class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Storage-Optimized</div>
    <div class="text-xs mt-2 opacity-70">Data-intensive</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Different workloads, different requirements
</div>

</v-click>

---
layout: section
---

# Node Capacity and Resources

---

# Resource Tracking

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-chip class="text-4xl text-blue-400" />
  <span class="text-lg">CPU cores</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-base class="text-4xl text-green-400" />
  <span class="text-lg">Memory</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-storage class="text-4xl text-purple-400" />
  <span class="text-lg">Storage</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Kubernetes tracks capacity carefully
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Decides which node has enough capacity
</div>

</v-click>

---

# Resource Requests and Limits

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Pod[Pod Requests<br/>Resources] --> K8s[Kubernetes]
    K8s --> Schedule[Find Node<br/>With Capacity]
    Schedule --> Node[Schedule to Node]
    style Pod fill:#ffd43b
    style K8s fill:#0078d4
    style Schedule fill:#51cf66
    style Node fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Resource requests: what pod needs
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-xl">
Resource limits: maximum pod can use
</div>

</v-click>

---
layout: section
---

# AZ-204 Exam Relevance

---

# What You Need to Know

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-view class="text-4xl text-blue-400" />
  <span class="text-lg">Inspect and query node information with kubectl</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-chart-bar class="text-4xl text-green-400" />
  <span class="text-lg">Understand node capacity and resource allocation</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-tag class="text-4xl text-purple-400" />
  <span class="text-lg">Work with node labels and selectors</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-debug class="text-4xl text-orange-400" />
  <span class="text-lg">Troubleshoot node-related issues in AKS</span>
</div>

</v-click>

---

# AKS Handles Configuration

<v-click>

<div class="mt-12 text-center text-xl">
Don't need to install or configure nodes from scratch
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
That's handled by AKS
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
But you DO need to know how to work with them
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-search class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Query</div>
  </div>
  <div class="text-center">
    <carbon-data-view-alt class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Inspect</div>
  </div>
  <div class="text-center">
    <carbon-debug class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Troubleshoot</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Tools We'll Use

---

# kubectl Commands

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-terminal class="text-4xl text-blue-400" />
  <span class="text-lg">kubectl get nodes</span>
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-sm opacity-70">
List all nodes in cluster
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-document-view class="text-4xl text-green-400" />
  <span class="text-lg">kubectl describe nodes</span>
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-sm opacity-70">
Detailed information about nodes
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-help class="text-4xl text-purple-400" />
  <span class="text-lg">kubectl explain</span>
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-sm opacity-70">
Learn about Kubernetes resources
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Your bread and butter for cluster management
</div>

</v-click>

---
layout: section
---

# What's Next

---

# Hands-On Exercises

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-search class="text-4xl text-blue-400" />
  <span class="text-lg">Examine nodes in your cluster</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-view-alt class="text-4xl text-green-400" />
  <span class="text-lg">Query node properties</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document class="text-4xl text-purple-400" />
  <span class="text-lg">Extract information using different output formats</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Comfortable navigating node infrastructure
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Crucial for exam and real-world development
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

<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<v-click>

<div class="text-xl mt-6 opacity-70">
Explore the worker machines powering your cluster
</div>

</v-click>

</div>
