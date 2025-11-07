---
theme: default
background: https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## AKS with KeyVault Secret Storage
  CSI Driver integration for AZ-204
drawings:
  persist: false
transition: slide-left
title: AKS KeyVault Integration
mdc: true
---

# AKS with Key Vault

Secure Secret Storage using CSI Driver

<div class="abs-bottom-10 left-10">
  <carbon-locked class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: AKS with KeyVault Secret Storage - Introduction Opening Welcome to this lab on integrating Azure Kubernetes Service with Azure Key Vault for secure secret storage.
search_anchor: AKS with KeyVault Secret Storage
-->
<v-click>

<div class="text-xl mt-8">
Integrating Azure Kubernetes Service<br/>with Azure Key Vault for secure secret storage
</div>

</v-click>

---
layout: section
---

# Container Storage Interface

---

# What is CSI?

<v-click>

<div class="mt-4">
  <carbon-data-storage class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: What is the Container Storage Interface?
search_anchor: What is the Container Storage
-->
<v-click>

<div class="mt-8 text-xl text-center">
Container Storage Interface
</div>

</v-click>

<!--
METADATA:
sentence: Kubernetes has a powerful, pluggable storage architecture called the Container Storage Interface, or CSI.
search_anchor: Kubernetes has a powerful, pluggable
-->
<v-click>

<div class="mt-12 text-lg text-center">
Kubernetes' pluggable storage architecture
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph LR
    K8s[Kubernetes] --> CSI[CSI]
    CSI --> Storage1[Block Storage]
    CSI --> Storage2[File Systems]
    CSI --> Storage3[Specialized Storage]
    style K8s fill:#326ce5
    style CSI fill:#0078d4
```

</v-click>

---

# CSI Flexibility

<!--
METADATA:
sentence: This architecture allows different types of storage systems to be connected to a Kubernetes cluster and made available as volumes inside your Pod containers.
search_anchor: This architecture allows different types
-->
<v-click>

<div class="mt-8 text-center text-xl">
Different storage systems connect to Kubernetes
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    CSI[Container Storage Interface]
    CSI --> Block[Block Storage<br/>Disks]
    CSI --> Files[File Systems<br/>NFS, SMB]
    CSI --> Special[Specialized<br/>Providers]
    style CSI fill:#326ce5
    style Block fill:#51cf66
    style Files fill:#ffd43b
    style Special fill:#ff6b6b
```

</div>

</v-click>

<!--
METADATA:
sentence: This architecture allows different types of storage systems to be connected to a Kubernetes cluster and made available as volumes inside your Pod containers.
search_anchor: This architecture allows different types
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Made available as volumes inside Pod containers
</div>

</v-click>

---
layout: section
---

# KeyVault as a Storage Provider

---

# The Game-Changer

<v-click>

<div class="mt-4">
  <carbon-security class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: KeyVault as a Storage Provider Azure Kubernetes Service includes an add-on that enables Azure Key Vault as a storage provider through the Secrets Store CSI Driver.
search_anchor: KeyVault as a Storage Provider
-->
<v-click>

<div class="mt-8 text-xl text-center">
Azure Key Vault as a storage provider
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    AKS[AKS CSI Driver] --> KV[Key Vault]
    KV --> Pod[Pod Volume]
    style AKS fill:#326ce5
    style KV fill:#0078d4
    style Pod fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: The beauty of CSI is its flexibility.
search_anchor: beauty of CSI is its
-->
<v-click>

<div class="mt-8 text-center text-lg">
Through the Secrets Store CSI Driver
</div>

</v-click>

---

# What You Can Do

<!--
METADATA:
sentence: This is a game-changer for security and configuration management.
search_anchor: This is a game-changer for
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document class="text-4xl text-blue-400" />
  <span class="text-lg">Store sensitive configuration files in Key Vault</span>
</div>

</v-click>

<!--
METADATA:
sentence: What is the Container Storage Interface?
search_anchor: What is the Container Storage
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-folder class="text-4xl text-green-400" />
  <span class="text-lg">Mount them as volumes in container folders</span>
</div>

</v-click>

<!--
METADATA:
sentence: The beauty of CSI is its flexibility.
search_anchor: beauty of CSI is its
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-red-400" />
  <span class="text-lg">Keep data secure outside of Kubernetes</span>
</div>

</v-click>

<!--
METADATA:
sentence: This is a game-changer for security and configuration management.
search_anchor: This is a game-changer for
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Game-changer for security and configuration management
</div>

</v-click>

---
layout: section
---

# Why This Matters

---

# Traditional Approach

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Secrets[Secrets] --> K8sSecret[Kubernetes Secret Object]
    K8sSecret --> etcd[etcd Database]
    etcd --> Pod[Pod]
    style K8sSecret fill:#ff6b6b
    style etcd fill:#ff6b6b
    style Pod fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: While these are base64 encoded, they're still stored in the cluster's etcd database.
search_anchor: While these are base64 encoded
-->
<v-click>

<div class="mt-8 text-center text-lg">
Secrets are base64 encoded
</div>

</v-click>

<!--
METADATA:
sentence: While these are base64 encoded, they're still stored in the cluster's etcd database.
search_anchor: While these are base64 encoded
-->
<v-click>

<div class="mt-4 text-center text-lg text-red-400">
But still stored in the cluster's etcd database
</div>

</v-click>

---

# Key Vault CSI Approach

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Secrets[Secrets] --> KV[Key Vault]
    KV -->|CSI Driver| Pod[Pod Volume<br/>In Memory]
    style KV fill:#0078d4
    style Pod fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: In this session, we'll explore how to leverage the Container Storage Interface to mount Key Vault secrets directly into your Kubernetes pods.
search_anchor: this session, we'll explore how
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Secrets remain in Azure Key Vault
</div>

</v-click>

<!--
METADATA:
sentence: In this session, we'll explore how to leverage the Container Storage Interface to mount Key Vault secrets directly into your Kubernetes pods.
search_anchor: this session, we'll explore how
-->
<v-click>

<div class="mt-6 text-center text-lg opacity-70">
Never exist as Kubernetes objects in your cluster
</div>

</v-click>

---

# Key Vault Security Features

<!--
METADATA:
sentence: This is a game-changer for security and configuration management.
search_anchor: This is a game-changer for
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-chip class="text-4xl text-purple-400" />
  <span class="text-lg">Hardware security module protection</span>
</div>

</v-click>

<!--
METADATA:
sentence: The beauty of CSI is its flexibility.
search_anchor: beauty of CSI is its
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document-tasks class="text-4xl text-blue-400" />
  <span class="text-lg">Audit logging</span>
</div>

</v-click>

<!--
METADATA:
sentence: What is the Container Storage Interface?
search_anchor: What is the Container Storage
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-access class="text-4xl text-green-400" />
  <span class="text-lg">Azure RBAC integration</span>
</div>

</v-click>

<!--
METADATA:
sentence: This is a game-changer for security and configuration management.
search_anchor: This is a game-changer for
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-center class="text-4xl text-orange-400" />
  <span class="text-lg">Centralized secret management across clusters</span>
</div>

</v-click>

---

# Secret Materialization

<v-click>

<div class="mt-8">

```mermaid
graph LR
    KV[Key Vault<br/>Encrypted Storage] -->|Mount| Memory[Pod Memory<br/>Runtime Only]
    Memory -->|Never Stored| NoK8s[❌ Kubernetes]
    style KV fill:#0078d4
    style Memory fill:#51cf66
    style NoK8s fill:#ff6b6b
```

</div>

</v-click>

<!--
METADATA:
sentence: While these are base64 encoded, they're still stored in the cluster's etcd database.
search_anchor: While these are base64 encoded
-->
<v-click>

<div class="mt-12 text-center text-xl">
Secrets materialized in memory only
</div>

</v-click>

<!--
METADATA:
sentence: It's not limited to traditional block storage or file systems.
search_anchor: It's not limited to traditional
-->
<v-click>

<div class="mt-6 text-center text-lg opacity-70">
When mounted into pod's filesystem
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
sentence: KeyVault as a Storage Provider Azure Kubernetes Service includes an add-on that enables Azure Key Vault as a storage provider through the Secrets Store CSI Driver.
search_anchor: KeyVault as a Storage Provider
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-add class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create AKS cluster with Key Vault add-on enabled</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: What is the Container Storage Interface?
search_anchor: What is the Container Storage
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">2</div>
  <div>
    <carbon-user-identification class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Configure managed identity permissions</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This is a game-changer for security and configuration management.
search_anchor: This is a game-changer for
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">3</div>
  <div>
    <carbon-security class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create and configure Key Vault</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This is a game-changer for security and configuration management.
search_anchor: This is a game-changer for
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">4</div>
  <div>
    <carbon-document-add class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Define SecretProviderClass for volume mounts</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: KeyVault as a Storage Provider Azure Kubernetes Service includes an add-on that enables Azure Key Vault as a storage provider through the Secrets Store CSI Driver.
search_anchor: KeyVault as a Storage Provider
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">5</div>
  <div>
    <carbon-deploy class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Deploy app that consumes secrets as files</span>
  </div>
</div>

</v-click>

---
layout: section
---

# Use Cases

---

# When to Use This Pattern

<!--
METADATA:
sentence: While these are base64 encoded, they're still stored in the cluster's etcd database.
search_anchor: While these are base64 encoded
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-share class="text-4xl text-blue-400" />
  <span class="text-lg">Share secrets across multiple clusters or applications</span>
</div>

</v-click>

<!--
METADATA:
sentence: What is the Container Storage Interface?
search_anchor: What is the Container Storage
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-certificate-check class="text-4xl text-green-400" />
  <span class="text-lg">Comply with centralized secret storage requirements</span>
</v-click>

<!--
METADATA:
sentence: While these are base64 encoded, they're still stored in the cluster's etcd database.
search_anchor: While these are base64 encoded
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-renew class="text-4xl text-purple-400" />
  <span class="text-lg">Rotate secrets without redeploying applications</span>
</div>

</v-click>

<!--
METADATA:
sentence: This is a game-changer for security and configuration management.
search_anchor: This is a game-changer for
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document-view class="text-4xl text-orange-400" />
  <span class="text-lg">Audit all access to sensitive configuration data</span>
</div>

</v-click>

---

# Architecture Overview

<v-click>

```mermaid
graph TB
    App[Application Pod] -->|Reads File| Volume[Mounted Volume]
    Volume -->|CSI Driver| KV[Key Vault]
    MI[Managed Identity] -->|Authenticates| KV
    style App fill:#51cf66
    style Volume fill:#ffd43b
    style KV fill:#0078d4
    style MI fill:#ff6b6b
```

</v-click>

<!--
METADATA:
sentence: It's not limited to traditional block storage or file systems.
search_anchor: It's not limited to traditional
-->
<v-click>

<div class="mt-8 text-center text-xl">
Secrets flow from Key Vault to Pod filesystem
</div>

</v-click>

<!--
METADATA:
sentence: KeyVault as a Storage Provider Azure Kubernetes Service includes an add-on that enables Azure Key Vault as a storage provider through the Secrets Store CSI Driver.
search_anchor: KeyVault as a Storage Provider
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Managed identity handles authentication automatically
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
sentence: What is the Container Storage Interface?
search_anchor: What is the Container Storage
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: KeyVault as a Storage Provider Azure Kubernetes Service includes an add-on that enables Azure Key Vault as a storage provider through the Secrets Store CSI Driver.
search_anchor: KeyVault as a Storage Provider
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Hands-on exercises with Key Vault CSI Driver
</div>

</v-click>

</div>
