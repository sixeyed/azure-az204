---
theme: default
background: https://images.unsplash.com/photo-1597852074816-d933c7d2b988?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes Storage
  Persistent volumes in AKS for AZ-204
drawings:
  persist: false
transition: slide-left
title: Kubernetes Storage
mdc: true
---

# Kubernetes Storage

Managing Persistent Data in AKS

<div class="abs-bottom-10 left-10">
  <carbon-data-storage class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore persistent storage<br/>for containerized applications in AKS
</div>

</v-click>

---
layout: section
---

# What We'll Cover

---

# Kubernetes Storage Abstractions

<v-click>

<div class="mt-4">
  <carbon-data-storage class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Kubernetes provides abstractions for generic storage
</div>

</v-click>

<v-click>

<div class="mt-12 text-lg text-center">
Works across all clusters
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph LR
    K8s[Kubernetes<br/>Volumes] --> Local[Local Cluster]
    K8s --> AKS[AKS]
    K8s --> Other[Other K8s]
    style K8s fill:#326ce5
    style AKS fill:#0078d4
```

</v-click>

---

# Volumes

<v-click>

<div class="mt-8 text-xl text-center">
Storage units mounted into application Pods
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Pod[Pod] --> Mount[Volume Mount]
    Mount --> Volume[Volume]
    Volume --> Storage[Azure Storage]
    style Pod fill:#326ce5
    style Volume fill:#ffd43b
    style Storage fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Appears as part of container filesystem
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Actually stored outside the container
</div>

</v-click>

---

# The Power of External Storage

<v-click>

<div class="mt-8 text-center text-xl">
In AKS: Backed by Azure resources
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-data-1 class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Managed Disks</div>
  </div>
  <div class="text-center">
    <carbon-folder class="text-6xl text-green-400" />
    <div class="text-sm mt-3">File Shares</div>
  </div>
</div>

</v-click>

---

# Two Important Capabilities

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-4xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-document class="text-4xl inline-block" />
    <div class="mt-2 text-lg">Push configuration settings as read-only files</div>
    <div class="mt-1 text-sm opacity-70">Manage config without rebuilding images</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-4xl text-green-400 mt-1">2</div>
  <div>
    <carbon-save class="text-4xl inline-block" />
    <div class="mt-2 text-lg">Store application state outside container</div>
    <div class="mt-1 text-sm opacity-70">Critical for ephemeral containers</div>
  </div>
</div>

</v-click>

---

# Why External Storage Matters

<v-click>

<div class="mt-8">

```mermaid
graph LR
    Container1[Container v1] -->|Dies| X[❌]
    Container2[Container v2] -->|Starts| Data[(External Data)]
    Data -->|Persists| Container2
    style Container1 fill:#ff6b6b
    style Container2 fill:#51cf66
    style Data fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Containers are ephemeral - can be replaced anytime
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-xl text-green-400">
External storage ensures state persists
</div>

</v-click>

---
layout: section
---

# Storage Concepts in Kubernetes

---

# Volumes and Volume Mounts

<v-click>

<div class="mt-4">
  <carbon-data-storage class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Basic building blocks
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Pod[Pod Level] --> Volume[Volume Definition]
    Container[Container] --> Mount[Volume Mount]
    Mount -->|Connects to| Volume
    Volume -->|Path:| Path[/data]
    style Pod fill:#326ce5
    style Volume fill:#ffd43b
    style Mount fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Volume defined at Pod level, mounted to container paths
</div>

</v-click>

---

# ConfigMaps as Volumes

<v-click>

<div class="mt-4">
  <carbon-document class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Mount ConfigMaps as read-only volumes
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    CM[ConfigMap] -->|Mount| Volume[Read-Only Volume]
    Volume -->|Inject| Container[Container]
    style CM fill:#ffd43b
    style Volume fill:#ff6b6b
    style Container fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Inject configuration files into containers
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-sm opacity-70">
Clean separation of configuration from images
</div>

</v-click>

---

# EmptyDir Volumes

<v-click>

<div class="mt-4">
  <carbon-folder class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Temporary storage with Pod lifecycle
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Pod[Pod Created] --> Empty[EmptyDir Created]
    Container1[Container Restarts] -->|Data Survives| Empty
    PodDelete[Pod Deleted] -->|EmptyDir Gone| X[❌]
    style Pod fill:#51cf66
    style Empty fill:#ffd43b
    style PodDelete fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Survives container restarts, not Pod deletion
</div>

</v-click>

---

# PersistentVolumeClaims

<v-click>

<div class="mt-4">
  <carbon-data-1 class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Requests for persistent storage
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    PVC[PVC Request] -->|Specify Size| K8s[Kubernetes]
    K8s -->|Provisions| Storage[Persistent Storage]
    Storage -->|Outlives| Pods[Pods]
    style PVC fill:#ffd43b
    style K8s fill:#326ce5
    style Storage fill:#0078d4
    style Pods fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Storage outlives individual Pods
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-sm opacity-70">
Kubernetes provisions based on storage classes
</div>

</v-click>

---
layout: section
---

# The Demo Application

---

# .NET 6.0 Background Worker

<v-click>

<div class="mt-4">
  <carbon-application class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-lg">
Simple application that:
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document class="text-3xl text-blue-400" />
  <span>Reads configuration from files</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-save class="text-3xl text-green-400" />
  <span>Writes data to various locations</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Perfect for demonstrating storage patterns
</div>

</v-click>

---

# Application Write Locations

<v-click>

<div class="mt-8 flex justify-center gap-16">
  <div class="text-center">
    <carbon-document-blank class="text-6xl text-orange-400" />
    <div class="text-lg mt-4">Cache File</div>
  </div>
  <div class="text-center">
    <carbon-data-base class="text-6xl text-blue-400" />
    <div class="text-lg mt-4">Database File</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Apply different volume types to each location
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg opacity-70">
See exactly how each storage type behaves
</div>

</v-click>

---
layout: section
---

# Environment Setup

---

# Two Environments

<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <carbon-docker class="text-6xl text-blue-500" />
    <div class="text-lg mt-4">Docker Desktop</div>
    <div class="text-sm mt-2 opacity-70">Local K8s</div>
  </div>
  <div class="text-4xl opacity-50">→</div>
  <div class="text-center">
    <carbon-logo-microsoft-azure class="text-6xl text-blue-400" />
    <div class="text-lg mt-4">AKS</div>
    <div class="text-sm mt-2 opacity-70">Cloud Production</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Start local for fast iteration
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-xl">
Move to AKS for production patterns
</div>

</v-click>

---

# The Beauty of Kubernetes

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Spec[Application Spec] --> Local[Docker Desktop<br/>Local Disk]
    Spec --> AKS[AKS<br/>Azure Storage]
    style Spec fill:#326ce5
    style Local fill:#51cf66
    style AKS fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Same specifications work identically
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg">
Different implementations underneath
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-sm opacity-70">
Application doesn't know or care
</div>

</v-click>

---

# Storage Implementation

<v-click>

<div class="mt-8 flex justify-center gap-16">
  <div class="text-center">
    <div class="text-xl font-bold text-blue-500">Docker Desktop</div>
    <div class="mt-4">
      <carbon-data-1 class="text-5xl" />
      <div class="text-sm mt-2">Local Disk</div>
    </div>
  </div>
  <div class="text-4xl opacity-50">≠</div>
  <div class="text-center">
    <div class="text-xl font-bold text-blue-400">AKS</div>
    <div class="mt-4">
      <carbon-cloud-services class="text-5xl" />
      <div class="text-sm mt-2">Azure Storage</div>
    </div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
But our application specs remain the same!
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
Setting up environment and deploying our application
</div>

</v-click>

</div>
