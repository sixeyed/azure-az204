---
theme: default
background: https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes Pods
  The foundation of container orchestration - AZ-204
drawings:
  persist: false
transition: slide-left
title: Pods
mdc: true
---

# Kubernetes Pods

The Foundation of Container Orchestration

<div class="abs-bottom-10 left-10">
  <carbon-container-software class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: Understanding Pods is essential for the AZ-204 exam and for working with Azure Kubernetes Service in the real world.
search_anchor: Understanding Pods is essential for
-->
<v-click>

<div class="text-xl mt-8">
Explore Kubernetes Pods<br/>Essential for AZ-204 and Azure Kubernetes Service
</div>

</v-click>

---
layout: section
---

# What is a Pod?

---

# Smallest Deployable Unit

<v-click>

<div class="mt-4">
  <carbon-container-software class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: It's not the container itself, but rather a wrapper around one or more containers.
search_anchor: It's not the container itself
-->
<v-click>

<div class="mt-8 text-xl text-center">
Not the container itself
</div>

</v-click>

<!--
METADATA:
sentence: It's not the container itself, but rather a wrapper around one or more containers.
search_anchor: It's not the container itself
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
A wrapper around one or more containers
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Pod[Pod] --> Container1[Container 1]
    Pod --> Container2[Container 2]
    style Pod fill:#51cf66
    style Container1 fill:#0078d4
    style Container2 fill:#0078d4
```

</div>

</v-click>

---

# Pod's Job

<!--
METADATA:
sentence: The Pod's job is pretty straightforward - it ensures your containers keep running.
search_anchor: Pod's job is pretty straightforward
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Ensure containers keep running
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Running[Container Running] --> Crash[Container Crashes]
    Crash --> Detect[Pod Detects]
    Detect --> Restart[Auto-Restart]
    Restart --> Running
    style Running fill:#51cf66
    style Crash fill:#ff6b6b
    style Detect fill:#ffd43b
    style Restart fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: This is the first layer of high availability that Kubernetes provides.
search_anchor: This is the first layer
-->
<v-click>

<div class="mt-12 text-center text-xl">
First layer of high availability
</div>

</v-click>

---
layout: section
---

# Pod Architecture

---

# What's Inside

<!--
METADATA:
sentence: Every Pod gets its own unique IP address within the cluster network.
search_anchor: Every Pod gets its own
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-network-3 class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Unique IP Address</div>
    <div class="text-sm mt-2 opacity-70">Every Pod gets own IP in cluster network</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: All containers inside that Pod share the same network namespace, which means they can communicate with each other using localhost.
search_anchor: All containers inside that Pod
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-share class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Shared Network Namespace</div>
    <div class="text-sm mt-2 opacity-70">All containers share same network</div>
    <div class="text-sm opacity-70">Communicate using localhost</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Pods can also share storage volumes between containers.
search_anchor: Pods can also share storage
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-data-storage class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Shared Storage Volumes</div>
    <div class="text-sm mt-2 opacity-70">Containers can access same data</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Single vs Multi-Container Pods

---

# Most Common: Single Container

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Pod1[Pod] --> App[Application<br/>Container]
    style Pod1 fill:#51cf66
    style App fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: You should also understand how Pods communicate within a cluster.
search_anchor: You should also understand how
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Simplest and most common pattern
</div>

</v-click>

---

# Multi-Container Patterns

<!--
METADATA:
sentence: Common patterns include sidecar containers for logging or monitoring, adapter containers that standardize output, and ambassador containers that proxy connections.
search_anchor: Common patterns include sidecar containers
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-document-tasks class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Sidecar</div>
    <div class="text-sm mt-2 opacity-70">Logging or monitoring containers</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Common patterns include sidecar containers for logging or monitoring, adapter containers that standardize output, and ambassador containers that proxy connections.
search_anchor: Common patterns include sidecar containers
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-settings-adjust class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Adapter</div>
    <div class="text-sm mt-2 opacity-70">Standardize output from main container</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Common patterns include sidecar containers for logging or monitoring, adapter containers that standardize output, and ambassador containers that proxy connections.
search_anchor: Common patterns include sidecar containers
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-network-3 class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Ambassador</div>
    <div class="text-sm mt-2 opacity-70">Proxy connections</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The key thing to remember is that containers in the same Pod are always scheduled together on the same node.
search_anchor: key thing to remember is
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Containers always scheduled together on same node
</div>

</v-click>

---
layout: section
---

# Pod Lifecycle

---

# State Transitions

<v-click>

<div class="mt-8">

```mermaid
graph LR
    Pending[Pending<br/>Scheduling] --> Running[Running<br/>Executing]
    Running --> Succeeded[Succeeded<br/>Completed ✓]
    Running --> Failed[Failed<br/>Error ❌]
    style Pending fill:#ffd43b
    style Running fill:#51cf66
    style Succeeded fill:#51cf66
    style Failed fill:#ff6b6b
```

</div>

</v-click>

<!--
METADATA:
sentence: They start in a Pending state while Kubernetes schedules them and pulls the container images.
search_anchor: They start in a Pending
-->
<v-click>

<div class="mt-12 flex items-start gap-4">
  <div class="text-3xl text-yellow-400 mt-1">1</div>
  <div>
    <div class="text-lg font-bold">Pending</div>
    <div class="text-sm mt-2 opacity-70">Kubernetes schedules, pulls images</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Then they move to Running when at least one container is executing.
search_anchor: Then they move to Running
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <div class="text-lg font-bold">Running</div>
    <div class="text-sm mt-2 opacity-70">At least one container executing</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Eventually, they'll reach a terminal state - either Succeeded if all containers completed successfully, or Failed if any container terminated with an error.
search_anchor: Eventually, they'll reach a terminal
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">3</div>
  <div>
    <div class="text-lg font-bold">Terminal State</div>
    <div class="text-sm mt-2 opacity-70">Succeeded (completed) or Failed (error)</div>
  </div>
</div>

</v-click>

---

# Understanding Lifecycle

<!--
METADATA:
sentence: Understanding this lifecycle is crucial for troubleshooting.
search_anchor: Understanding this lifecycle is crucial
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Crucial for troubleshooting
</div>

</v-click>

<!--
METADATA:
sentence: Understanding this lifecycle is crucial for troubleshooting.
search_anchor: Understanding this lifecycle is crucial
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-view class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Check Status</div>
  </div>
  <div class="text-center">
    <carbon-debug class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Debug Issues</div>
  </div>
  <div class="text-center">
    <carbon-data-view-alt class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Monitor Health</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Working with Pods

---

# kubectl Commands

<!--
METADATA:
sentence: Common operations include deploying Pods from YAML files, checking their status, viewing logs, and even executing commands inside running containers.
search_anchor: Common operations include deploying Pods
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-blue-400" />
  <span class="text-lg">Deploy Pods from YAML files</span>
</div>

</v-click>

<!--
METADATA:
sentence: Think of a Pod as the smallest deployable unit in Kubernetes.
search_anchor: Think of a Pod as
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-view class="text-4xl text-green-400" />
  <span class="text-lg">Check Pod status</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document class="text-4xl text-purple-400" />
  <span class="text-lg">View logs</span>
</div>

</v-click>

<!--
METADATA:
sentence: Pods can also share storage volumes between containers.
search_anchor: Pods can also share storage
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-terminal class="text-4xl text-orange-400" />
  <span class="text-lg">Execute commands inside containers</span>
</div>

</v-click>

---

# Declarative Approach

<!--
METADATA:
sentence: You describe the desired state, and Kubernetes works to maintain it.
search_anchor: You describe the desired state
-->
<v-click>

<div class="mt-12 text-center text-xl">
Describe desired state in YAML
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    YAML[YAML File<br/>Desired State] --> K8s[Kubernetes]
    K8s --> Works[Works to Maintain It]
    style YAML fill:#ffd43b
    style K8s fill:#0078d4
    style Works fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: The declarative approach using YAML is what makes Kubernetes powerful.
search_anchor: declarative approach using YAML is
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
What makes Kubernetes powerful
</div>

</v-click>

---
layout: section
---

# AZ-204 Exam Relevance

---

# What You Need to Know

<!--
METADATA:
sentence: Ready to see Pods in action?
search_anchor: Ready to see Pods in
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create and configure Pods</span>
</div>

</v-click>

<!--
METADATA:
sentence: Understanding this lifecycle is crucial for troubleshooting.
search_anchor: Understanding this lifecycle is crucial
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-flow class="text-4xl text-green-400" />
  <span class="text-lg">Understand Pod lifecycle</span>
</div>

</v-click>

<!--
METADATA:
sentence: --- SLIDE 2: What is a Pod?
search_anchor: --- SLIDE 2: What is
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-container-software class="text-4xl text-purple-400" />
  <span class="text-lg">Multi-container Pod patterns</span>
</div>

</v-click>

<!--
METADATA:
sentence: --- SLIDE 2: What is a Pod?
search_anchor: --- SLIDE 2: What is
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-debug class="text-4xl text-orange-400" />
  <span class="text-lg">Troubleshoot Pod issues</span>
</div>

</v-click>

<!--
METADATA:
sentence: You should also understand how Pods communicate within a cluster.
search_anchor: You should also understand how
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-red-400" />
  <span class="text-lg">Pod communication within cluster</span>
</div>

</v-click>

---

# Foundation Knowledge

<!--
METADATA:
sentence: Ready to see Pods in action?
search_anchor: Ready to see Pods in
-->
<v-click>

<div class="mt-12 text-center text-xl">
Pods form the foundation
</div>

</v-click>

<!--
METADATA:
sentence: This knowledge forms the foundation for more advanced topics like Deployments, Services, and StatefulSets that build on top of Pods.
search_anchor: This knowledge forms the foundation
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-deployment-pattern class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Deployments</div>
  </div>
  <div class="text-center">
    <carbon-network-3 class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Services</div>
  </div>
  <div class="text-center">
    <carbon-data-base class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">StatefulSets</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This knowledge forms the foundation for more advanced topics like Deployments, Services, and StatefulSets that build on top of Pods.
search_anchor: This knowledge forms the foundation
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Advanced topics build on top of Pods
</div>

</v-click>

---
layout: section
---

# What's Next

---

# Hands-On Exercises

<!--
METADATA:
sentence: Ready to see Pods in action?
search_anchor: Ready to see Pods in
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-blue-400" />
  <span class="text-lg">Deploy first Pods</span>
</div>

</v-click>

<!--
METADATA:
sentence: --- [End of intro video]
search_anchor: --- [End of intro video]
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-explore class="text-4xl text-green-400" />
  <span class="text-lg">Explore from inside</span>
</div>

</v-click>

<!--
METADATA:
sentence: You should also understand how Pods communicate within a cluster.
search_anchor: You should also understand how
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-purple-400" />
  <span class="text-lg">See how Pods communicate</span>
</div>

</v-click>

<!--
METADATA:
sentence: Today we're diving into one of the most fundamental concepts in Kubernetes - Pods.
search_anchor: Today we're diving into one
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-container-software class="text-4xl text-orange-400" />
  <span class="text-lg">Work with multi-container Pods</span>
</div>

</v-click>

<!--
METADATA:
sentence: Ready to see Pods in action?
search_anchor: Ready to see Pods in
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
See Pods in action!
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
sentence: Ready to see Pods in action?
search_anchor: Ready to see Pods in
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Ready to Go!
</div>

</v-click>

<!--
METADATA:
sentence: Today we're diving into one of the most fundamental concepts in Kubernetes - Pods.
search_anchor: Today we're diving into one
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Build a solid foundation with Kubernetes Pods
</div>

</v-click>

</div>
