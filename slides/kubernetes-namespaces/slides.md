---
theme: default
background: https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes Namespaces
  Isolating workloads for AZ-204
drawings:
  persist: false
transition: slide-left
title: Namespaces
mdc: true
---

# Kubernetes Namespaces

Isolating Workloads

<div class="abs-bottom-10 left-10">
  <carbon-folder class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Kubernetes Namespaces<br/>Essential for organizing and isolating workloads
</div>

</v-click>

---
layout: section
---

# What Are Namespaces?

---

# Virtual Clusters

<v-click>

<div class="mt-4">
  <carbon-collaborate class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Virtual clusters within your physical cluster
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Containers for other Kubernetes resources
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Cluster[Physical Cluster] --> NS1[Namespace: E-commerce]
    Cluster --> NS2[Namespace: Inventory]
    Cluster --> NS3[Namespace: Customer Portal]
    NS1 --> Pods1[Pods & Services]
    NS2 --> Pods2[Pods & Services]
    NS3 --> Pods3[Pods & Services]
    style Cluster fill:#0078d4
    style NS1 fill:#51cf66
    style NS2 fill:#51cf66
    style NS3 fill:#51cf66
```

</div>

</v-click>

---

# Why Namespaces?

<v-click>

<div class="mt-12 text-center text-xl">
Run any type of application
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Migrate entire application landscape onto Kubernetes
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
Without segregation: chaos
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
With namespaces: organized and safe
</div>

</v-click>

---
layout: section
---

# Use Cases & Scenarios

---

# Real-World Examples

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-application class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Production Cluster</div>
    <div class="text-sm mt-2 opacity-70">Different namespace per application</div>
    <div class="text-sm mt-2">E-commerce → ns: ecommerce</div>
    <div class="text-sm">Inventory → ns: inventory</div>
    <div class="text-sm">Customer Portal → ns: portal</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-development class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Non-Production Cluster</div>
    <div class="text-sm mt-2 opacity-70">Organize by environment</div>
    <div class="text-sm mt-2">ns: development</div>
    <div class="text-sm">ns: testing</div>
    <div class="text-sm">ns: uat</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Dev team can experiment without breaking test
</div>

</v-click>

---
layout: section
---

# Resource Isolation Benefits

---

# Three Major Benefits

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-chart-bar class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Resource Isolation</span>
    <div class="text-sm mt-2 opacity-70">Apply resource quotas per namespace</div>
    <div class="text-sm opacity-70">Prevent one app from consuming all resources</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-security class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Security Boundaries</span>
    <div class="text-sm mt-2 opacity-70">Role-Based Access Control per namespace</div>
    <div class="text-sm opacity-70">Junior devs access dev, not production</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-clean class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Simplified Management</span>
    <div class="text-sm mt-2 opacity-70">No complex label selectors everywhere</div>
    <div class="text-sm opacity-70">Natural organization by namespace</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Multi-Tenancy

---

# Enterprise Scenarios

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Multiple teams, projects, or customers on same cluster
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Cluster[Shared Cluster] --> Team1[Team A Namespace<br/>Isolated]
    Cluster --> Team2[Team B Namespace<br/>Isolated]
    Cluster --> Team3[Team C Namespace<br/>Isolated]
    Team1 --> Limits1[Resource Limits<br/>Access Controls]
    Team2 --> Limits2[Resource Limits<br/>Access Controls]
    Team3 --> Limits3[Resource Limits<br/>Access Controls]
    style Cluster fill:#0078d4
    style Team1 fill:#51cf66
    style Team2 fill:#51cf66
    style Team3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Strict isolation, resource limits, and access controls
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-2xl text-green-400">
Cost optimization
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Consolidate workloads while maintaining security
</div>

</v-click>

---
layout: section
---

# AZ-204 Exam Relevance

---

# Key Exam Topics

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-container-software class="text-4xl text-blue-400" />
  <span class="text-lg">Implement Azure solutions with containers</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document-tasks class="text-4xl text-green-400" />
  <span class="text-lg">Organize applications properly</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-purple-400" />
  <span class="text-lg">Implement proper security boundaries</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings-adjust class="text-4xl text-orange-400" />
  <span class="text-lg">Manage resources efficiently</span>
</div>

</v-click>

---

# Essential Knowledge Areas

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-folder class="text-4xl text-blue-400" />
  <span class="text-lg">Resource organization strategies</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-access class="text-4xl text-green-400" />
  <span class="text-lg">RBAC implementation</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-development class="text-4xl text-purple-400" />
  <span class="text-lg">Environment separation strategies</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Works exactly same in Azure Kubernetes Service
</div>

</v-click>

---
layout: section
---

# What We'll Cover Today

---

# Lab Overview

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create and manage namespaces with kubectl</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-green-400" />
  <span class="text-lg">Deploy applications into specific namespaces</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-purple-400" />
  <span class="text-lg">Explore service discovery and DNS resolution</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-tools class="text-4xl text-orange-400" />
  <span class="text-lg">Practical tools for working with namespaces</span>
</div>

</v-click>

---
layout: section
---

# Important Considerations

---

# Key Points to Remember

<v-click>

<div class="mt-12 text-center text-xl">
Namespaces introduce some complexity
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Need to be more explicit about where things live
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
But the safeguards are absolutely worth it
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Confident multi-workload</div>
  </div>
  <div class="text-center">
    <carbon-scale class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">No compromise on scale</div>
  </div>
  <div class="text-center">
    <carbon-security class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">No compromise on security</div>
  </div>
</div>

</v-click>

---

# Structure Rules

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Cluster[Cluster] --> NS1[Namespace A]
    Cluster --> NS2[Namespace B]
    Cluster --> NS3[Namespace C]
    NS1 --> Pod1[Pods]
    NS2 --> Pod2[Pods]
    NS3 --> Pod3[Pods]
    style Cluster fill:#0078d4
    style NS1 fill:#51cf66
    style NS2 fill:#51cf66
    style NS3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Namespaces can't be nested
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-xl">
Single-level hierarchy
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Keep your organization strategy simple and clear
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
Master namespace organization and isolation
</div>

</v-click>

</div>
