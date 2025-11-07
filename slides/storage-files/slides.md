---
theme: default
background: https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Files Storage
  Managed file shares in the cloud - AZ-204
drawings:
  persist: false
transition: slide-left
title: Azure Files
mdc: true
---

# Azure Files Storage

Managed File Shares in the Cloud

<div class="abs-bottom-10 left-10">
  <carbon-folder-shared class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: Azure Files is a fully managed file share service in the cloud.
search_anchor: Azure Files is a fully
-->
<v-click>

<div class="text-xl mt-8">
Explore Azure Files<br/>Cloud-based file shares with SMB protocol
</div>

</v-click>

---
layout: section
---

# What is Azure Files?

---

# Managed File Share Service

<v-click>

<div class="mt-4">
  <carbon-folder-shared class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Azure Files is a fully managed file share service in the cloud.
search_anchor: Azure Files is a fully
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Fully managed file share service in the cloud
</div>

</v-click>

<!--
METADATA:
sentence: It provides shared storage that can be mounted into your filesystem, making it easy to share files between multiple applications, virtual machines, or on-premises systems.
search_anchor: It provides shared storage that
-->
<v-click>

<div class="mt-12 text-center text-xl">
Shared storage that can be mounted into filesystem
</div>

</v-click>

<!--
METADATA:
sentence: Azure Files is a fully managed file share service in the cloud.
search_anchor: Azure Files is a fully
-->
<v-click>

<div class="mt-12 text-center text-xl">
Like corporate network file share, but in Azure
</div>

</v-click>

---

# Key Benefits

<!--
METADATA:
sentence: Second, Azure Files is highly available and durable.
search_anchor: Second, Azure Files is highly
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-scale class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Scalability</div>
  </div>
  <div class="text-center">
    <carbon-renew class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Redundancy</div>
  </div>
  <div class="text-center">
    <carbon-earth class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Global Availability</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Key Features

---

# Four Main Features

<!--
METADATA:
sentence: Key Features Let's look at the main features of Azure Files: First, it uses the standard SMB protocol - Server Message Block - which is the same protocol used by Windows file shares.
search_anchor: Key Features Let's look at
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-network-3 class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Standard SMB Protocol</span>
    <div class="text-sm mt-2 opacity-70">Server Message Block - same as Windows file shares</div>
    <div class="text-sm opacity-70">No special code changes needed</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Your data is replicated within Azure to protect against hardware failures.
search_anchor: Your data is replicated within
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-checkmark-outline class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Highly Available and Durable</span>
    <div class="text-sm mt-2 opacity-70">Data replicated to protect against failures</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: You don't need to worry about maintaining file servers, applying patches, or managing hardware.
search_anchor: You don't need to worry
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-cloud-services class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Fully Managed</span>
    <div class="text-sm mt-2 opacity-70">No file servers, patches, or hardware to maintain</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: And fourth, it integrates seamlessly with both cloud and on-premises environments.
search_anchor: fourth, it integrates seamlessly with
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-hybrid-networking class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Seamless Integration</span>
    <div class="text-sm mt-2 opacity-70">Works with cloud and on-premises environments</div>
    <div class="text-sm opacity-70">Windows, Linux, and macOS</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Common Use Cases

---

# Real-World Scenarios

<!--
METADATA:
sentence: Common Use Cases Azure Files is ideal for several scenarios: Lift and shift migrations - when you're moving legacy applications that expect file shares to the cloud.
search_anchor: Common Use Cases Azure Files
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-cloud-upload class="text-4xl text-blue-400" />
  <span class="text-lg">Lift and shift migrations - legacy apps expecting file shares</span>
</div>

</v-click>

<!--
METADATA:
sentence: Shared storage for applications - when multiple VMs or containers need access to the same files.
search_anchor: Shared storage for applications -
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-share class="text-4xl text-green-400" />
  <span class="text-lg">Shared storage - multiple VMs or containers need same files</span>
</div>

</v-click>

<!--
METADATA:
sentence: Storing configuration files - that need to be accessible across multiple instances.
search_anchor: Storing configuration files - that
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-purple-400" />
  <span class="text-lg">Configuration files - accessible across multiple instances</span>
</div>

</v-click>

<!--
METADATA:
sentence: And for development and debugging - when you need shared access to logs, metrics, or diagnostic data.
search_anchor: development and debugging - when
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-debug class="text-4xl text-orange-400" />
  <span class="text-lg">Development and debugging - shared logs, metrics, diagnostics</span>
</div>

</v-click>

---
layout: section
---

# How It Works

---

# Architecture

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Storage[Storage Account] --> Share1[File Share 1]
    Storage --> Share2[File Share 2]
    Share1 --> Quota1[Quota: Max Capacity]
    Share2 --> Quota2[Quota: Max Capacity]
    Share1 --> Mount1[Mount on Clients]
    Share2 --> Mount2[Mount on Clients]
    style Storage fill:#0078d4
    style Share1 fill:#51cf66
    style Share2 fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: How it Works Azure Files is a feature of Azure Storage Accounts.
search_anchor: How it Works Azure Files
-->
<v-click>

<div class="mt-12 text-center text-xl">
Feature of Azure Storage Accounts
</div>

</v-click>

---

# Access and Authentication

<!--
METADATA:
sentence: To access a file share, clients use the storage account name and key for authentication.
search_anchor: access a file share, clients
-->
<v-click>

<div class="mt-12 text-center text-xl">
Clients use storage account name and key
</div>

</v-click>

<!--
METADATA:
sentence: You can mount the share using standard operating system commands, and once mounted, it appears as a regular drive or directory on your system.
search_anchor: You can mount the share
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Mount using standard OS commands
</div>

</v-click>

<!--
METADATA:
sentence: You can mount the share using standard operating system commands, and once mounted, it appears as a regular drive or directory on your system.
search_anchor: You can mount the share
-->
<v-click>

<div class="mt-12 text-center text-xl">
Appears as regular drive or directory
</div>

</v-click>

<!--
METADATA:
sentence: You can mount Azure file shares from Windows, Linux, and macOS machines.
search_anchor: You can mount Azure file
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-windows class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Windows</div>
  </div>
  <div class="text-center">
    <carbon-linux class="text-6xl text-orange-400" />
    <div class="text-sm mt-3">Linux</div>
  </div>
  <div class="text-center">
    <carbon-apple class="text-6xl text-gray-400" />
    <div class="text-sm mt-3">macOS</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What We'll Build

---

# Lab Overview

<!--
METADATA:
sentence: We'll start by creating a storage account and file share.
search_anchor: We'll start by creating a
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create storage account and file share</span>
</div>

</v-click>

<!--
METADATA:
sentence: Then we'll upload files and explore different ways to access them.
search_anchor: Then we'll upload files and
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-upload class="text-4xl text-green-400" />
  <span class="text-lg">Upload files to share</span>
</div>

</v-click>

<!--
METADATA:
sentence: We'll mount the share on our local machine and see how changes sync in real-time.
search_anchor: We'll mount the share on
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-folder-shared class="text-4xl text-purple-400" />
  <span class="text-lg">Mount share on local machine</span>
</div>

</v-click>

<!--
METADATA:
sentence: We'll mount the share on our local machine and see how changes sync in real-time.
search_anchor: We'll mount the share on
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-renew class="text-4xl text-orange-400" />
  <span class="text-lg">See real-time sync</span>
</div>

</v-click>

<!--
METADATA:
sentence: We'll also look at security considerations, including how to rotate storage account keys.
search_anchor: We'll also look at security
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-red-400" />
  <span class="text-lg">Security considerations and key rotation</span>
</div>

</v-click>

---

# Advanced Lab Steps

<!--
METADATA:
sentence: Finally, we'll mount the same share in an Azure Virtual Machine using cloud-init, demonstrating how you can automate file share mounting during VM provisioning.
search_anchor: Finally, we'll mount the same
-->
<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-virtual-machine class="text-4xl text-blue-400" />
  <span class="text-lg">Mount share in Azure VM using cloud-init</span>
</div>

</v-click>

<!--
METADATA:
sentence: Finally, we'll mount the same share in an Azure Virtual Machine using cloud-init, demonstrating how you can automate file share mounting during VM provisioning.
search_anchor: Finally, we'll mount the same
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Automate file share mounting during VM provisioning
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
sentence: Azure Files is a fully managed file share service in the cloud.
search_anchor: Azure Files is a fully
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: You can mount Azure file shares from Windows, Linux, and macOS machines.
search_anchor: You can mount Azure file
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Create and use Azure file shares
</div>

</v-click>

</div>
