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

<!--
METADATA:
sentence: A Persistent Volume Claim is your application's request for storage.
search_anchor: Persistent Volume Claim is your
-->
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

<!--
METADATA:
sentence: By default, when a container writes data to its filesystem, that data lives inside the container.
search_anchor: By default, when a container
-->
<v-click>

<div class="mt-8 text-xl text-center">
Container writes data to filesystem
</div>

</v-click>

<!--
METADATA:
sentence: By default, when a container writes data to its filesystem, that data lives inside the container.
search_anchor: By default, when a container
-->
<v-click>

<div class="mt-8 text-center text-xl">
Data lives inside container
</div>

</v-click>

<!--
METADATA:
sentence: When the container restarts or gets replaced, all that data disappears.
search_anchor: When the container restarts or
-->
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

<!--
METADATA:
sentence: Imagine running a database where all your data vanishes every time a pod restarts.
search_anchor: Imagine running a database where
-->
<v-click>

<div class="mt-12 text-center text-xl">
Imagine a database where all data vanishes
</div>

</v-click>

<!--
METADATA:
sentence: Imagine running a database where all your data vanishes every time a pod restarts.
search_anchor: Imagine running a database where
-->
<v-click>

<div class="mt-8 text-center text-xl text-red-400">
Every time a pod restarts
</div>

</v-click>

<!--
METADATA:
sentence: We need storage that persists beyond the lifecycle of individual containers and pods.
search_anchor: We need storage that persists
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
We need storage that persists
</div>

</v-click>

<!--
METADATA:
sentence: We need storage that persists beyond the lifecycle of individual containers and pods.
search_anchor: We need storage that persists
-->
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

<!--
METADATA:
sentence: The application doesn't need to know if that's an Azure Disk, an AWS EBS volume, or local storage.
search_anchor: application doesn't need to know
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Application doesn't need to know infrastructure
</div>

</v-click>

<!--
METADATA:
sentence: Instead of your application having to know whether it's running on AWS, Azure, or on-premises hardware, Kubernetes provides a clean separation between storage consumers and storage providers.
search_anchor: Instead of your application having
-->
<v-click>

<div class="mt-12 text-center text-xl">
Running on AWS, Azure, or on-premises?
</div>

</v-click>

<!--
METADATA:
sentence: The application doesn't need to know if that's an Azure Disk, an AWS EBS volume, or local storage.
search_anchor: application doesn't need to know
-->
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

<!--
METADATA:
sentence: Think of it like this: a Persistent Volume is the actual storage resource, like a disk or network file share.
search_anchor: Think of it like this
-->
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

<!--
METADATA:
sentence: A Persistent Volume Claim is your application's request for storage.
search_anchor: Persistent Volume Claim is your
-->
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

<!--
METADATA:
sentence: Your application says "I need 100 gigabytes of storage with read-write access" and Kubernetes handles the rest.
search_anchor: Your application says "I need
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Kubernetes handles the rest
</div>

</v-click>

---

# Portable Applications

<!--
METADATA:
sentence: Your application says "I need 100 gigabytes of storage with read-write access" and Kubernetes handles the rest.
search_anchor: Your application says "I need
-->
<v-click>

<div class="mt-12 text-center text-xl">
Application says: "I need storage"
</div>

</v-click>

<!--
METADATA:
sentence: The application doesn't need to know if that's an Azure Disk, an AWS EBS volume, or local storage.
search_anchor: application doesn't need to know
-->
<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Not: "Give me an Azure Disk"
</div>

</v-click>

<!--
METADATA:
sentence: This abstraction is powerful because it keeps your application portable.
search_anchor: This abstraction is powerful because
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Abstraction keeps applications portable
</div>

</v-click>

<!--
METADATA:
sentence: You don't need to pre-create volumes.
search_anchor: You don't need to pre-create
-->
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

<!--
METADATA:
sentence: Storage Classes define these different types of storage available in your cluster.
search_anchor: Storage Classes define these different
-->
<v-click>

<div class="mt-8 text-center text-xl">
Production clusters have different storage types
</div>

</v-click>

<!--
METADATA:
sentence: You might have fast SSD storage for databases, slower but cheaper storage for backups, or shared file systems for applications that need concurrent access.
search_anchor: You might have fast SSD
-->
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

<!--
METADATA:
sentence: Storage Classes define these different types of storage available in your cluster.
search_anchor: Storage Classes define these different
-->
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

<!--
METADATA:
sentence: You don't need to pre-create volumes.
search_anchor: You don't need to pre-create
-->
<v-click>

<div class="mt-12 text-center text-xl">
No need to pre-create volumes
</div>

</v-click>

<!--
METADATA:
sentence: You just describe what you need, and the storage provisioner creates it for you.
search_anchor: You just describe what you
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Describe what you need, storage provisioner creates it
</div>

</v-click>

<!--
METADATA:
sentence: This makes scaling and managing applications much simpler.
search_anchor: This makes scaling and managing
-->
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

<!--
METADATA:
sentence: Read-Write Once means one node can mount it for reading and writing.
search_anchor: Read-Write Once means one node
-->
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

<!--
METADATA:
sentence: Read-Only Many allows multiple nodes to mount it read-only.
search_anchor: Read-Only Many allows multiple nodes
-->
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

<!--
METADATA:
sentence: And Read-Write Many lets multiple nodes mount it with write access.
search_anchor: Read-Write Many lets multiple nodes
-->
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

<!--
METADATA:
sentence: The mode you choose depends on your application's requirements.
search_anchor: mode you choose depends on
-->
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

<!--
METADATA:
sentence: The real magic happens with dynamic provisioning.
search_anchor: real magic happens with dynamic
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-blue-400" />
  <span class="text-lg">Azure Disk integration with AKS</span>
</div>

</v-click>

<!--
METADATA:
sentence: A Persistent Volume Claim is your application's request for storage.
search_anchor: Persistent Volume Claim is your
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-share class="text-4xl text-green-400" />
  <span class="text-lg">Azure Files for shared storage</span>
</div>

</v-click>

<!--
METADATA:
sentence: This abstraction is powerful because it keeps your application portable.
search_anchor: This abstraction is powerful because
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-base class="text-4xl text-purple-400" />
  <span class="text-lg">Stateful application patterns</span>
</div>

</v-click>

<!--
METADATA:
sentence: Read-Write Once means one node can mount it for reading and writing.
search_anchor: Read-Write Once means one node
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document-blank class="text-4xl text-orange-400" />
  <span class="text-lg">PVC configuration and binding</span>
</div>

</v-click>

---

# What You Need to Know

<!--
METADATA:
sentence: The exam expects you to know when to use managed disks versus file shares, how to configure persistent volume claims, and how applications consume persistent storage in AKS.
search_anchor: exam expects you to know
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-decision-tree class="text-4xl text-blue-400" />
  <span class="text-lg">When to use managed disks vs file shares</span>
</div>

</v-click>

<!--
METADATA:
sentence: A Persistent Volume Claim is your application's request for storage.
search_anchor: Persistent Volume Claim is your
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-green-400" />
  <span class="text-lg">Configure persistent volume claims</span>
</div>

</v-click>

<!--
METADATA:
sentence: A Persistent Volume Claim is your application's request for storage.
search_anchor: Persistent Volume Claim is your
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-application class="text-4xl text-purple-400" />
  <span class="text-lg">How applications consume persistent storage in AKS</span>
</div>

</v-click>

<!--
METADATA:
sentence: You'll encounter scenarios about stateful applications, data persistence strategies, and choosing the right storage solution for different workload types.
search_anchor: You'll encounter scenarios about stateful
-->
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

<!--
METADATA:
sentence: And Read-Write Many lets multiple nodes mount it with write access.
search_anchor: Read-Write Many lets multiple nodes
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-flash class="text-4xl text-blue-400" />
  <span class="text-lg">Azure Disk for single-node access</span>
</div>

</v-click>

<!--
METADATA:
sentence: And Read-Write Many lets multiple nodes mount it with write access.
search_anchor: Read-Write Many lets multiple nodes
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-share class="text-4xl text-green-400" />
  <span class="text-lg">Azure Files for multi-node sharing</span>
</div>

</v-click>

<!--
METADATA:
sentence: That's obviously not going to work for production applications.
search_anchor: That's obviously not going to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-purple-400" />
  <span class="text-lg">Deploy stateful applications</span>
</div>

</v-click>

<!--
METADATA:
sentence: When you request storage, you specify how it can be accessed.
search_anchor: When you request storage, you
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-orange-400" />
  <span class="text-lg">Work with storage classes</span>
</div>

</v-click>

<!--
METADATA:
sentence: In the next section, we'll walk through practical examples showing different storage options in action.
search_anchor: next section, we'll walk through
-->
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

<!--
METADATA:
sentence: --- Closing (10 seconds) Alright, now that we've covered the concepts, let's get hands-on.
search_anchor: --- Closing (10 seconds) Alright
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Hands-On!
</div>

</v-click>

<!--
METADATA:
sentence: When your application creates a Persistent Volume Claim, Kubernetes can automatically provision the storage on-demand.
search_anchor: When your application creates a
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Master persistent storage in Kubernetes
</div>

</v-click>

</div>
