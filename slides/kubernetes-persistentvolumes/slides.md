---
theme: default
background: https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes Persistent Volumes
  Storage that survives pod restarts - AZ-204
drawings:
  persist: false
transition: slide-left
title: Persistent Volumes
mdc: true
---

# Kubernetes Persistent Volumes

Storage That Survives Pod Restarts

<div class="abs-bottom-10 left-10">
  <carbon-data-storage class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Persistent Volumes and Claims<br/>Critical for stateful applications
</div>

</v-click>

---
layout: section
---

# The Storage Challenge

---

# The Problem

<v-click>

<div class="mt-4">
  <carbon-warning class="text-6xl text-red-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Container writes data to filesystem
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Data lives inside container
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
Container restarts → All data disappears
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Write[Container<br/>Writes Data] --> Store[Data in Container]
    Store --> Crash[Container Crashes]
    Crash --> Lost[Data Lost ❌]
    style Write fill:#ffd43b
    style Store fill:#ffd43b
    style Crash fill:#ff6b6b
    style Lost fill:#ff6b6b
```

</div>

</v-click>

---

# Not Good for Production

<v-click>

<div class="mt-12 text-center text-xl">
Imagine a database where all data vanishes
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-red-400">
Every time a pod restarts
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
We need storage that persists
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Beyond lifecycle of individual containers and pods
</div>

</v-click>

---
layout: section
---

# The Kubernetes Storage Abstraction

---

# Clean Separation

<v-click>

<div class="mt-4">
  <carbon-network-overlay class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Application doesn't need to know infrastructure
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Running on AWS, Azure, or on-premises?
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl opacity-70">
Application doesn't care
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    App[Application] --> PVC[Persistent Volume Claim<br/>Abstraction Layer]
    PVC --> PV[Persistent Volume<br/>Actual Storage]
    PV --> Azure[Azure Disk]
    PV --> AWS[AWS EBS]
    PV --> Local[Local Storage]
    style App fill:#ffd43b
    style PVC fill:#51cf66
    style PV fill:#0078d4
```

</div>

</v-click>

---

# Two Key Resources

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-data-storage class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Persistent Volume (PV)</span>
    <div class="text-sm mt-2 opacity-70">The actual storage resource</div>
    <div class="text-sm opacity-70">Like a disk or network file share</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-document-blank class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Persistent Volume Claim (PVC)</span>
    <div class="text-sm mt-2 opacity-70">Application's request for storage</div>
    <div class="text-sm opacity-70">"I need 100 GB with read-write access"</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Kubernetes handles the rest
</div>

</v-click>

---

# Portable Applications

<v-click>

<div class="mt-12 text-center text-xl">
Application says: "I need storage"
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Not: "Give me an Azure Disk"
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Abstraction keeps applications portable
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-cloud class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Azure</div>
  </div>
  <div class="text-center">
    <carbon-cloud class="text-6xl text-orange-400" />
    <div class="text-sm mt-3">AWS</div>
  </div>
  <div class="text-center">
    <carbon-server class="text-6xl text-green-400" />
    <div class="text-sm mt-3">On-Premises</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Storage Classes and Dynamic Provisioning

---

# Multiple Storage Options

<v-click>

<div class="mt-8 text-center text-xl">
Production clusters have different storage types
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-flash class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Fast SSD</div>
    <div class="text-xs mt-2 opacity-70">Databases</div>
  </div>
  <div class="text-center">
    <carbon-data-storage class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Standard HDD</div>
    <div class="text-xs mt-2 opacity-70">Backups</div>
  </div>
  <div class="text-center">
    <carbon-share class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Shared Files</div>
    <div class="text-xs mt-2 opacity-70">Concurrent access</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Storage Classes define these options
</div>

</v-click>

---

# Dynamic Provisioning Magic

<v-click>

<div class="mt-8">

```mermaid
graph LR
    PVC[Create<br/>PVC] --> K8s[Kubernetes]
    K8s --> Storage[Storage Class]
    Storage --> Provision[Auto-Provision<br/>Storage]
    Provision --> Ready[Ready to Use]
    style PVC fill:#ffd43b
    style K8s fill:#0078d4
    style Storage fill:#51cf66
    style Provision fill:#51cf66
    style Ready fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
No need to pre-create volumes
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Describe what you need, storage provisioner creates it
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Makes scaling and managing applications much simpler
</div>

</v-click>

---
layout: section
---

# Access Modes

---

# How Storage Can Be Accessed

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-document class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">ReadWriteOnce (RWO)</div>
    <div class="text-sm mt-2 opacity-70">One node can mount for read-write</div>
    <div class="text-sm mt-2 text-green-400">Most common for databases</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-view class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">ReadOnlyMany (ROX)</div>
    <div class="text-sm mt-2 opacity-70">Multiple nodes can mount read-only</div>
    <div class="text-sm mt-2 text-green-400">Shared read-only data</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-share class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">ReadWriteMany (RWX)</div>
    <div class="text-sm mt-2 opacity-70">Multiple nodes with write access</div>
    <div class="text-sm mt-2 text-green-400">Shared file systems</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Choose based on application requirements
</div>

</v-click>

---
layout: section
---

# AZ-204 Exam Relevance

---

# Critical Exam Topics

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-blue-400" />
  <span class="text-lg">Azure Disk integration with AKS</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-share class="text-4xl text-green-400" />
  <span class="text-lg">Azure Files for shared storage</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-base class="text-4xl text-purple-400" />
  <span class="text-lg">Stateful application patterns</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document-blank class="text-4xl text-orange-400" />
  <span class="text-lg">PVC configuration and binding</span>
</div>

</v-click>

---

# What You Need to Know

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-decision-tree class="text-4xl text-blue-400" />
  <span class="text-lg">When to use managed disks vs file shares</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-green-400" />
  <span class="text-lg">Configure persistent volume claims</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-application class="text-4xl text-purple-400" />
  <span class="text-lg">How applications consume persistent storage in AKS</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Data persistence strategies for different workloads
</div>

</v-click>

---
layout: section
---

# What's Next

---

# Hands-On Examples

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-flash class="text-4xl text-blue-400" />
  <span class="text-lg">Azure Disk for single-node access</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-share class="text-4xl text-green-400" />
  <span class="text-lg">Azure Files for multi-node sharing</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-purple-400" />
  <span class="text-lg">Deploy stateful applications</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-orange-400" />
  <span class="text-lg">Work with storage classes</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Different storage options in action
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
Let's Get Hands-On!
</div>

</v-click>

<v-click>

<div class="text-xl mt-6 opacity-70">
Master persistent storage in Kubernetes
</div>

</v-click>

</div>
