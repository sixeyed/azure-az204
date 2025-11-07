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

<!--
METADATA:
sentence: What are Storage Accounts?
search_anchor: What are Storage Accounts
-->
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

<!--
METADATA:
sentence: Azure Storage Accounts are a managed storage service that allows you to store data in the cloud.
search_anchor: Azure Storage Accounts are a
-->
<v-click>

<div class="mt-8 text-xl text-center">
Store data in the cloud
</div>

</v-click>

<!--
METADATA:
sentence: You have complete control over who can access your data - you can make it publicly accessible, restrict it to specific users, or limit access to other Azure services.
search_anchor: You have complete control over
-->
<v-click>

<div class="mt-12 text-lg">
Complete control over access:
</div>

</v-click>

<!--
METADATA:
sentence: You have complete control over who can access your data - you can make it publicly accessible, restrict it to specific users, or limit access to other Azure services.
search_anchor: You have complete control over
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-globe class="text-3xl text-green-400" />
  <span>Publicly accessible</span>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Storage Accounts - Introduction Opening Welcome to this lab on Azure Storage Accounts.
search_anchor: Azure Storage Accounts - Introduction
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-locked class="text-3xl text-red-400" />
  <span>Restricted to specific users</span>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Storage Accounts - Introduction Opening Welcome to this lab on Azure Storage Accounts.
search_anchor: Azure Storage Accounts - Introduction
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-logo-microsoft-azure class="text-3xl text-blue-400" />
  <span>Limited to Azure services</span>
</div>

</v-click>

---

# Key Benefits

<!--
METADATA:
sentence: Your data is automatically replicated across multiple locations to ensure high availability and durability.
search_anchor: Your data is automatically replicated
-->
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

<!--
METADATA:
sentence: And you're not locked into a single configuration - you can choose different performance levels based on your specific needs and budget.
search_anchor: you're not locked into a
-->
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

<!--
METADATA:
sentence: What are Storage Accounts?
search_anchor: What are Storage Accounts
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Creating storage accounts using Azure CLI</span>
</div>

</v-click>

<!--
METADATA:
sentence: One of the key benefits of Storage Accounts is built-in redundancy.
search_anchor: One of the key benefits
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-copy class="text-4xl text-green-400" />
  <span class="text-lg">Understanding performance and redundancy levels</span>
</div>

</v-click>

<!--
METADATA:
sentence: Getting Started Let's get started with our hands-on exercises.
search_anchor: Getting Started Let's get started
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-blob class="text-4xl text-purple-400" />
  <span class="text-lg">Working with blob containers</span>
</div>

</v-click>

<!--
METADATA:
sentence: This is the most cost-effective option and protects against hardware failures.
search_anchor: This is the most cost-effective
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-red-400" />
  <span class="text-lg">Managing public and private access</span>
</div>

</v-click>

<!--
METADATA:
sentence: What are Storage Accounts?
search_anchor: What are Storage Accounts
-->
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

<!--
METADATA:
sentence: Azure offers several levels of replication: Locally Redundant Storage - or LRS - replicates your data within a single datacenter.
search_anchor: Azure offers several levels of
-->
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

<!--
METADATA:
sentence: Azure offers several levels of replication: Locally Redundant Storage - or LRS - replicates your data within a single datacenter.
search_anchor: Azure offers several levels of
-->
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

<!--
METADATA:
sentence: This is the most cost-effective option and protects against hardware failures.
search_anchor: This is the most cost-effective
-->
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

<!--
METADATA:
sentence: Zone Redundant Storage - or ZRS - replicates your data across multiple datacenters within a single region.
search_anchor: Zone Redundant Storage - or
-->
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

<!--
METADATA:
sentence: This provides better availability than LRS.
search_anchor: This provides better availability than
-->
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

<!--
METADATA:
sentence: Geo-Redundant Storage - or GRS - replicates your data across different regions entirely.
search_anchor: Geo-Redundant Storage - or GRS
-->
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

<!--
METADATA:
sentence: This gives you the highest level of protection, but comes at a higher cost.
search_anchor: This gives you the highest
-->
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

<!--
METADATA:
sentence: Your data becomes more secure with wider replication, but you'll pay more for that additional protection.
search_anchor: Your data becomes more secure
-->
<v-click>

<div class="mt-12 text-center text-2xl">
More secure with wider replication
</div>

</v-click>

<!--
METADATA:
sentence: Your data becomes more secure with wider replication, but you'll pay more for that additional protection.
search_anchor: Your data becomes more secure
-->
<v-click>

<div class="mt-6 text-center text-xl opacity-70">
But you pay more for additional protection
</div>

</v-click>

---

# Redundancy Comparison

<!--
METADATA:
sentence: This is the most cost-effective option and protects against hardware failures.
search_anchor: This is the most cost-effective
-->
<v-click>

<div class="mt-8">

| Level | Protection | Cost |
|-------|-----------|------|
| LRS | Hardware failures | $ |
| ZRS | DC failures | $$ |
| GRS | Regional disasters | $$$ |

</div>

</v-click>

<!--
METADATA:
sentence: And you're not locked into a single configuration - you can choose different performance levels based on your specific needs and budget.
search_anchor: you're not locked into a
-->
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

<!--
METADATA:
sentence: What We'll Cover In this lab, we'll explore the basics of Azure Storage Accounts.
search_anchor: What We'll Cover In this
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-search class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Explore options in Azure Portal</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: What are Storage Accounts?
search_anchor: What are Storage Accounts
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-command-line class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create storage account using Azure CLI</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: You'll learn how to create storage accounts, understand different redundancy options, and work with blob storage to upload both small and large files.
search_anchor: You'll learn how to create
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-data-blob class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Work with blob containers and files</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This is the most cost-effective option and protects against hardware failures.
search_anchor: This is the most cost-effective
-->
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

<!--
METADATA:
sentence: Getting Started Let's get started with our hands-on exercises.
search_anchor: Getting Started Let's get started
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: What are Storage Accounts?
search_anchor: What are Storage Accounts
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Hands-on with Azure Storage Accounts
</div>

</v-click>

</div>
