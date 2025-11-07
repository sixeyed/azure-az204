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

<!--
METADATA:
sentence: Today we're diving into Kubernetes Namespaces, one of the most powerful features for organizing and isolating workloads in your cluster.
search_anchor: Today we're diving into Kubernetes
-->
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

<!--
METADATA:
sentence: Think of them as virtual clusters within your physical cluster.
search_anchor: Think of them as virtual
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Virtual clusters within your physical cluster
</div>

</v-click>

<!--
METADATA:
sentence: They're containers for other Kubernetes resources, giving you a way to divide your cluster into separate, isolated environments.
search_anchor: They're containers for other Kubernetes
-->
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

<!--
METADATA:
sentence: One of the coolest things about Kubernetes is that you can run any type of application.
search_anchor: One of the coolest things
-->
<v-click>

<div class="mt-12 text-center text-xl">
Run any type of application
</div>

</v-click>

<!--
METADATA:
sentence: Many organizations want to migrate their entire application landscape onto Kubernetes.
search_anchor: Many organizations want to migrate
-->
<v-click>

<div class="mt-8 text-center text-xl">
Migrate entire application landscape onto Kubernetes
</div>

</v-click>

<!--
METADATA:
sentence: But without a way to segregate the cluster, operations could get really messy, really fast.
search_anchor: But without a way to
-->
<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
Without segregation: chaos
</div>

</v-click>

<!--
METADATA:
sentence: That's where namespaces come in.
search_anchor: That's where namespaces come in
-->
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

<!--
METADATA:
sentence: On your production cluster, you might create a different namespace for each application.
search_anchor: your production cluster, you might
-->
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

<!--
METADATA:
sentence: On your non-production cluster, you might organize by environment.
search_anchor: your non-production cluster, you might
-->
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

<!--
METADATA:
sentence: This way, your dev team can experiment freely without worrying about breaking the test environment.
search_anchor: This way, your dev team
-->
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

<!--
METADATA:
sentence: You can apply resource quotas per namespace, preventing one application from consuming all your cluster resources.
search_anchor: You can apply resource quotas
-->
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

<!--
METADATA:
sentence: Your junior developers might have access to the dev namespace but not production.
search_anchor: Your junior developers might have
-->
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

<!--
METADATA:
sentence: Instead of using complex label selectors everywhere, you can organize resources naturally by namespace.
search_anchor: Instead of using complex label
-->
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

<!--
METADATA:
sentence: Namespaces let you safely run multiple teams, projects, or even customers on the same Kubernetes cluster.
search_anchor: Namespaces let you safely run
-->
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

<!--
METADATA:
sentence: Each tenant gets their own namespace with strict isolation, resource limits, and access controls.
search_anchor: Each tenant gets their own
-->
<v-click>

<div class="mt-12 text-center text-xl">
Strict isolation, resource limits, and access controls
</div>

</v-click>

<!--
METADATA:
sentence: This is huge for cost optimization.
search_anchor: This is huge for cost
-->
<v-click>

<div class="mt-8 text-center text-2xl text-green-400">
Cost optimization
</div>

</v-click>

<!--
METADATA:
sentence: Instead of spinning up separate clusters for every team or project, you can consolidate workloads while maintaining the security and isolation you need.
search_anchor: Instead of spinning up separate
-->
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

<!--
METADATA:
sentence: Microsoft expects you to understand how to implement Azure solutions, and that includes container-based deployments.
search_anchor: Microsoft expects you to understand
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-container-software class="text-4xl text-blue-400" />
  <span class="text-lg">Implement Azure solutions with containers</span>
</div>

</v-click>

<!--
METADATA:
sentence: Second, how to deploy applications into specific namespaces.
search_anchor: Second, how to deploy applications
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document-tasks class="text-4xl text-green-400" />
  <span class="text-lg">Organize applications properly</span>
</div>

</v-click>

<!--
METADATA:
sentence: Second, security boundaries.
search_anchor: Second, security boundaries
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-purple-400" />
  <span class="text-lg">Implement proper security boundaries</span>
</div>

</v-click>

<!--
METADATA:
sentence: You need to know how to organize applications, implement proper security boundaries, and manage resources efficiently.
search_anchor: You need to know how
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings-adjust class="text-4xl text-orange-400" />
  <span class="text-lg">Manage resources efficiently</span>
</div>

</v-click>

---

# Essential Knowledge Areas

<!--
METADATA:
sentence: Keep your organization strategy simple and clear.
search_anchor: Keep your organization strategy simple
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-folder class="text-4xl text-blue-400" />
  <span class="text-lg">Resource organization strategies</span>
</div>

</v-click>

<!--
METADATA:
sentence: Third, simplified management.
search_anchor: Third, simplified management
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-access class="text-4xl text-green-400" />
  <span class="text-lg">RBAC implementation</span>
</div>

</v-click>

<!--
METADATA:
sentence: You'll need to demonstrate knowledge of resource organization, RBAC implementation, and environment separation strategies.
search_anchor: You'll need to demonstrate knowledge
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-development class="text-4xl text-purple-400" />
  <span class="text-lg">Environment separation strategies</span>
</div>

</v-click>

<!--
METADATA:
sentence: In Azure Kubernetes Service, namespaces work exactly the same way as standard Kubernetes, so everything we cover today applies directly to your AKS deployments.
search_anchor: Azure Kubernetes Service, namespaces work
-->
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

<!--
METADATA:
sentence: Also, remember: namespaces can't be nested.
search_anchor: Also, remember: namespaces can't be
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create and manage namespaces with kubectl</span>
</div>

</v-click>

<!--
METADATA:
sentence: Second, how to deploy applications into specific namespaces.
search_anchor: Second, how to deploy applications
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-green-400" />
  <span class="text-lg">Deploy applications into specific namespaces</span>
</div>

</v-click>

<!--
METADATA:
sentence: Third, how namespaces affect service discovery and DNS resolution.
search_anchor: Third, how namespaces affect service
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-purple-400" />
  <span class="text-lg">Explore service discovery and DNS resolution</span>
</div>

</v-click>

<!--
METADATA:
sentence: And finally, we'll look at some practical tools that make working with namespaces much easier.
search_anchor: finally, we'll look at some
-->
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

<!--
METADATA:
sentence: That's where namespaces come in.
search_anchor: That's where namespaces come in
-->
<v-click>

<div class="mt-12 text-center text-xl">
Namespaces introduce some complexity
</div>

</v-click>

<!--
METADATA:
sentence: You need to be more explicit about where things live.
search_anchor: You need to be more
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Need to be more explicit about where things live
</div>

</v-click>

<!--
METADATA:
sentence: But the safeguards they provide are absolutely worth it.
search_anchor: But the safeguards they provide
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
But the safeguards are absolutely worth it
</div>

</v-click>

<!--
METADATA:
sentence: With namespaces, you can confidently run multiple workloads on a single cluster without compromising scale or security.
search_anchor: namespaces, you can confidently run
-->
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

<!--
METADATA:
sentence: Also, remember: namespaces can't be nested.
search_anchor: Also, remember: namespaces can't be
-->
<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Namespaces can't be nested
</div>

</v-click>

<!--
METADATA:
sentence: It's a single-level hierarchy.
search_anchor: It's a single-level hierarchy
-->
<v-click>

<div class="mt-4 text-center text-xl">
Single-level hierarchy
</div>

</v-click>

<!--
METADATA:
sentence: Keep your organization strategy simple and clear.
search_anchor: Keep your organization strategy simple
-->
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

<!--
METADATA:
sentence: So let's get started!
search_anchor: So let's get started
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: Keep your organization strategy simple and clear.
search_anchor: Keep your organization strategy simple
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Master namespace organization and isolation
</div>

</v-click>

</div>
