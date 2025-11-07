---
theme: default
background: https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Storage Accounts
  Managed cloud storage for AZ-204
drawings:
  persist: false
transition: slide-left
title: Azure Storage
mdc: true
---

# Azure Storage Accounts

Highly Available, Secure, Scalable Storage

<div class="abs-bottom-10 left-10">
  <carbon-data-storage class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Azure Storage Accounts<br/>Fundamental building blocks of Azure
</div>

</v-click>

---
layout: section
---

# What are Storage Accounts?

---

# Managed Storage Service

<v-click>

<div class="mt-4">
  <carbon-data-storage class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Store data in the cloud
</div>

</v-click>

<v-click>

<div class="mt-12 text-lg">
Complete control over access:
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-globe class="text-3xl text-green-400" />
  <span>Publicly accessible</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-locked class="text-3xl text-red-400" />
  <span>Restricted to specific users</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-logo-microsoft-azure class="text-3xl text-blue-400" />
  <span>Limited to Azure services</span>
</div>

</v-click>

---

# Key Benefits

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-copy class="text-5xl text-green-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Built-in Redundancy</div>
    <div class="text-sm mt-2 opacity-70">Data replicated across multiple locations</div>
    <div class="text-sm opacity-70">High availability and durability</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-settings-adjust class="text-5xl text-purple-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Flexible Configuration</div>
    <div class="text-sm mt-2 opacity-70">Different performance levels</div>
    <div class="text-sm opacity-70">Based on needs and budget</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What We'll Cover

---

# Lab Objectives

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Creating storage accounts using Azure CLI</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-copy class="text-4xl text-green-400" />
  <span class="text-lg">Understanding performance and redundancy levels</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-blob class="text-4xl text-purple-400" />
  <span class="text-lg">Working with blob containers</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-red-400" />
  <span class="text-lg">Managing public and private access</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-1 class="text-4xl text-orange-400" />
  <span class="text-lg">Storing VM disks in storage accounts</span>
</div>

</v-click>

---
layout: section
---

# Redundancy Options

---

# Data Replication Levels

<v-click>

<div class="mt-8 text-center text-xl">
Azure offers several levels of replication
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Data[Your Data] --> LRS[LRS<br/>Same DC]
    Data --> ZRS[ZRS<br/>Same Region]
    Data --> GRS[GRS<br/>Different Regions]
    style LRS fill:#51cf66
    style ZRS fill:#ffd43b
    style GRS fill:#ff6b6b
```

</div>

</v-click>

---

# LRS: Locally Redundant Storage

<v-click>

<div class="mt-4">
  <carbon-data-center class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Replicates within a single datacenter
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    subgraph Datacenter
        Copy1[Copy 1]
        Copy2[Copy 2]
        Copy3[Copy 3]
    end
    style Copy1 fill:#51cf66
    style Copy2 fill:#51cf66
    style Copy3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <carbon-currency-dollar class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Most Cost-Effective</div>
  </div>
  <div class="text-center">
    <carbon-checkmark class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Hardware Protection</div>
  </div>
</div>

</v-click>

---

# ZRS: Zone Redundant Storage

<v-click>

<div class="mt-4">
  <carbon-location class="text-6xl text-yellow-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Replicates across multiple datacenters
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    subgraph Single Region
        DC1[Datacenter 1]
        DC2[Datacenter 2]
        DC3[Datacenter 3]
    end
    style DC1 fill:#ffd43b
    style DC2 fill:#ffd43b
    style DC3 fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg text-green-400">
Better availability than LRS
</div>

</v-click>

---

# GRS: Geo-Redundant Storage

<v-click>

<div class="mt-4">
  <carbon-location-company class="text-6xl text-red-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Replicates across different regions
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Primary[Primary Region] --> Secondary[Secondary Region]
    style Primary fill:#0078d4
    style Secondary fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <carbon-shield class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Highest Protection</div>
  </div>
  <div class="text-center">
    <carbon-currency-dollar class="text-5xl text-red-400" />
    <div class="text-sm mt-3">Higher Cost</div>
  </div>
</div>

</v-click>

---

# The Key Takeaway

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Wider[Wider Replication] -->|More| Secure[Security]
    Secure -->|But| Cost[Higher Cost]
    style Wider fill:#51cf66
    style Secure fill:#0078d4
    style Cost fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl">
More secure with wider replication
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-xl opacity-70">
But you pay more for additional protection
</div>

</v-click>

---

# Redundancy Comparison

<v-click>

<div class="mt-8">

| Level | Protection | Cost |
|-------|-----------|------|
| LRS | Hardware failures | $ |
| ZRS | DC failures | $$ |
| GRS | Regional disasters | $$$ |

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg">
Choose based on your requirements and budget
</div>

</v-click>

---
layout: section
---

# Getting Started

---

# Lab Flow

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-search class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Explore options in Azure Portal</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-command-line class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create storage account using Azure CLI</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-data-blob class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Work with blob containers and files</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-test-tool class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Test public and private access</span>
  </div>
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
Hands-on with Azure Storage Accounts
</div>

</v-click>

</div>
