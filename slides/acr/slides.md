---
theme: default
background: https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Container Registry
  Private container registry service for AZ-204
drawings:
  persist: false
transition: slide-left
title: Azure Container Registry
mdc: true
---

# Azure Container Registry

Private Container Registry for Azure

<div class="abs-bottom-10 left-10">
  <carbon-catalog class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: section
---

# What is Azure Container Registry?

---

# Azure Container Registry (ACR)

<v-click>

<div class="mt-4">
  <carbon-catalog class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-8 text-xl text-center">
Azure's private container registry service
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    A[Public Registry<br/>Docker Hub] --> B[Open Source Apps]
    C[Private Registry<br/>ACR] --> D[Your Apps]
    style A fill:#2496ed
    style C fill:#0078d4
    style D fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Secure, private registries with full Azure integration
</div>

</v-click>

---
layout: section
---

# Why Use a Private Registry?

---

# Public vs Private

<!--
METADATA:
sentence: Why Use a Private Registry?
search_anchor: Why Use a Private Registry
-->
<v-click>

<div class="mt-4 flex justify-center gap-16">
  <div class="text-center">
    <carbon-open-panel-filled-right class="text-6xl text-blue-500" />
    <div class="text-xl mt-4">Docker Hub</div>
    <div class="text-sm mt-2 opacity-70">Public</div>
  </div>
  <div class="text-center">
    <carbon-locked class="text-6xl text-green-400" />
    <div class="text-xl mt-4">ACR</div>
    <div class="text-sm mt-2 opacity-70">Private</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: While open source applications are commonly published to public registries like Docker Hub, organizations need secure, private registries for their own applications.
search_anchor: While open source applications are
-->
<v-click>

<div class="mt-12 text-center text-xl">
Docker Hub: Excellent for open source
</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-6 text-center text-xl">
ACR: Essential for production applications
</div>

</v-click>

---

# What You Need for Production

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-red-400" />
  <div>
    <div class="text-lg font-bold">Security and access control</div>
    <div class="text-sm mt-1 opacity-70">Keep proprietary images private</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-location class="text-4xl text-blue-400" />
  <div>
    <div class="text-lg font-bold">Regional deployment</div>
    <div class="text-sm mt-1 opacity-70">Store images near compute for faster pulls</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-logo-microsoft-azure class="text-4xl text-green-400" />
  <div>
    <div class="text-lg font-bold">Azure integration</div>
    <div class="text-sm mt-1 opacity-70">Azure AD authentication and RBAC</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-certificate class="text-4xl text-purple-400" />
  <div>
    <div class="text-lg font-bold">Compliance</div>
    <div class="text-sm mt-1 opacity-70">Meet organizational storage requirements</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Key Features of ACR

---

# SKU Tiers

<v-click>

<div class="mt-8">

```mermaid
graph LR
    A[Basic] --> B[Standard] --> C[Premium]
    style A fill:#51cf66
    style B fill:#ffd43b
    style C fill:#ff6b6b
```

</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-12 text-center text-xl">
Multiple SKU tiers with different features
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <div class="text-2xl font-bold text-green-400">Basic</div>
    <div class="text-sm mt-2">Cost-effective</div>
  </div>
  <div class="text-center">
    <div class="text-2xl font-bold text-yellow-400">Standard</div>
    <div class="text-sm mt-2">Production</div>
  </div>
  <div class="text-center">
    <div class="text-2xl font-bold text-red-400">Premium</div>
    <div class="text-sm mt-2">Enterprise</div>
  </div>
</div>

</v-click>

---

# Premium Features

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-location-company class="text-4xl text-blue-400" />
  <span class="text-lg">Geo-replication across Azure regions</span>
</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-green-400" />
  <span class="text-lg">Private networking with Azure Private Link</span>
</div>

</v-click>

<!--
METADATA:
sentence: Why Use a Private Registry?
search_anchor: Why Use a Private Registry
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-purple-400" />
  <span class="text-lg">Customer-managed encryption keys</span>
</div>

</v-click>

<!--
METADATA:
sentence: Why Use a Private Registry?
search_anchor: Why Use a Private Registry
-->
<v-click>

<div class="mt-8 text-center text-sm opacity-60">
Premium SKU only
</div>

</v-click>

---

# Core Features

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-certificate-check class="text-4xl text-green-400" />
  <span class="text-lg">Content trust - Sign and verify images</span>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-webhook class="text-4xl text-blue-400" />
  <span class="text-lg">Webhooks for automation triggers</span>
</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-integration class="text-4xl text-purple-400" />
  <span class="text-lg">Seamless integration with Azure services</span>
</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-8 text-center text-sm opacity-70">
Works with ACI, AKS, and more
</div>

</v-click>

---

# Geo-replication

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Primary[Primary Registry<br/>East US] --> West[Replica<br/>West US]
    Primary --> Europe[Replica<br/>Europe]
    Primary --> Asia[Replica<br/>Asia]
    style Primary fill:#0078d4
    style West fill:#51cf66
    style Europe fill:#51cf66
    style Asia fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-8 text-center text-xl">
Replicate across multiple Azure regions
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Faster pulls, lower latency worldwide
</div>

</v-click>

---
layout: section
---

# Registry Naming and DNS

---

# Registry Name Becomes DNS

<v-click>

<div class="mt-8">

```mermaid
graph LR
    A[Registry Name] --> B[mycompanyregistry]
    B --> C[mycompanyregistry.azurecr.io]
    style A fill:#ffd43b
    style B fill:#0078d4
    style C fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="mt-12 text-center">
  <div class="text-lg">Registry name: <span class="text-blue-400 font-mono">mycompanyregistry</span></div>
</div>

</v-click>

<!--
METADATA:
sentence: Why Use a Private Registry?
search_anchor: Why Use a Private Registry
-->
<v-click>

<div class="mt-4 text-center">
  <div class="text-lg">Login server: <span class="text-green-400 font-mono">mycompanyregistry.azurecr.io</span></div>
</div>

</v-click>

---

# Naming Rules

<v-click>

<div class="mt-8">
  <carbon-information class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Why Use a Private Registry?
search_anchor: Why Use a Private Registry
-->
<v-click>

<div class="mt-12 text-center text-xl">
Registry name must be:
</div>

</v-click>

<!--
METADATA:
sentence: Why Use a Private Registry?
search_anchor: Why Use a Private Registry
-->
<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <carbon-globe class="text-4xl text-green-400" />
    <div class="text-sm mt-2">Globally unique</div>
  </div>
  <div class="text-center">
    <carbon-text-lowercase class="text-4xl text-blue-400" />
    <div class="text-sm mt-2">Lowercase only</div>
  </div>
  <div class="text-center">
    <carbon-data-1 class="text-4xl text-purple-400" />
    <div class="text-sm mt-2">Letters & numbers</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Understanding Container Registry Concepts

---

# Container Registries

<v-click>

<div class="mt-4">
  <carbon-catalog class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Understanding Container Registry Concepts Before diving into the exercises, it's important to understand a few key concepts: Container Registries are services that host container images.
search_anchor: Understanding Container Registry Concepts Before
-->
<v-click>

<div class="mt-8 text-xl text-center">
Services that host container images
</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-8 grid grid-cols-2 gap-6">
  <div class="flex items-center gap-3">
    <carbon-data-storage class="text-3xl text-green-400" />
    <span>Storage for images</span>
  </div>
  <div class="flex items-center gap-3">
    <carbon-api class="text-3xl text-blue-400" />
    <span>Push/pull API</span>
  </div>
  <div class="flex items-center gap-3">
    <carbon-password class="text-3xl text-purple-400" />
    <span>Authentication</span>
  </div>
  <div class="flex items-center gap-3">
    <carbon-security class="text-3xl text-red-400" />
    <span>Image scanning</span>
  </div>
</div>

</v-click>

---

# Docker Image Names

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-8 text-center">
  <code class="text-lg">myregistry.azurecr.io/labs-acr/nginx:alpine-2204</code>
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    A[Registry Domain] --> B[Repository Path] --> C[Tag]
    style A fill:#ff6b6b
    style B fill:#51cf66
    style C fill:#ffd43b
```

</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="mt-8 grid grid-cols-3 gap-6 text-center">
  <div>
    <div class="text-red-400 font-mono text-sm">myregistry.azurecr.io</div>
    <div class="text-xs mt-2 opacity-70">Registry domain</div>
  </div>
  <div>
    <div class="text-green-400 font-mono text-sm">labs-acr/nginx</div>
    <div class="text-xs mt-2 opacity-70">Repository path</div>
  </div>
  <div>
    <div class="text-yellow-400 font-mono text-sm">alpine-2204</div>
    <div class="text-xs mt-2 opacity-70">Tag/version</div>
  </div>
</div>

</v-click>

---

# Image Name Examples

<!--
METADATA:
sentence: While open source applications are commonly published to public registries like Docker Hub, organizations need secure, private registries for their own applications.
search_anchor: While open source applications are
-->
<v-click>

<div class="mt-6">
  <div class="font-mono text-sm text-blue-400">docker.io/nginx:latest</div>
  <div class="text-xs mt-1 opacity-70">Public Docker Hub image</div>
</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-6">
  <div class="font-mono text-sm text-green-400">myregistry.azurecr.io/webapp:v1.2</div>
  <div class="text-xs mt-1 opacity-70">ACR with version tag</div>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-6">
  <div class="font-mono text-sm text-purple-400">myregistry.azurecr.io/team/api:latest</div>
  <div class="text-xs mt-1 opacity-70">ACR with repository path</div>
</div>

</v-click>

---

# Authentication Methods

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-avatar class="text-4xl text-blue-400" />
  <div>
    <div class="text-lg">Azure AD identity</div>
    <div class="text-sm opacity-70">For development</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Why Use a Private Registry?
search_anchor: Why Use a Private Registry
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-green-400" />
  <div>
    <div class="text-lg">Service principals</div>
    <div class="text-sm opacity-70">For CI/CD pipelines</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: While open source applications are commonly published to public registries like Docker Hub, organizations need secure, private registries for their own applications.
search_anchor: While open source applications are
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-admin class="text-4xl text-orange-400" />
  <div>
    <div class="text-lg">Admin account</div>
    <div class="text-sm opacity-70">For testing (not production)</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: ACR provides this capability with full Azure integration.
search_anchor: ACR provides this capability with
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-ibm-cloud-identity-trustcenter class="text-4xl text-purple-400" />
  <div>
    <div class="text-lg">Managed identities</div>
    <div class="text-sm opacity-70">For Azure services</div>
  </div>
</div>

</v-click>

---

# Authentication Flow

<v-click>

<div class="mt-8">

```mermaid
graph LR
    A[Your App] -->|Authenticate| B[Azure AD]
    B -->|Token| A
    A -->|Push/Pull| C[ACR]
    style A fill:#51cf66
    style B fill:#ffd43b
    style C fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry, or ACR, is Azure's private container registry service.
search_anchor: Azure Container Registry, or ACR
-->
<v-click>

<div class="mt-12 text-center text-xl">
Leverage Azure AD for secure access
</div>

</v-click>

---
layout: section
---

# What You'll Learn

---

# Lab Objectives

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-portal class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Portal exploration - SKU options and configuration</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">2</div>
  <div>
    <carbon-command-line class="text-3xl inline-block" />
    <span class="ml-3 text-lg">CLI creation - Create registry with Azure CLI</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: While open source applications are commonly published to public registries like Docker Hub, organizations need secure, private registries for their own applications.
search_anchor: While open source applications are
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">3</div>
  <div>
    <carbon-data-backup class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Image management - Pull from Docker Hub, push to ACR</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: While open source applications are commonly published to public registries like Docker Hub, organizations need secure, private registries for their own applications.
search_anchor: While open source applications are
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">4</div>
  <div>
    <carbon-build-tool class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Custom builds - Build and store your own images</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">5</div>
  <div>
    <carbon-dashboard class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Portal management - Browse and manage images</span>
  </div>
</div>

</v-click>

---
layout: center
class: text-center
---

<div>

<v-click>

<carbon-catalog class="text-8xl text-blue-400 inline-block" />

</v-click>

<!--
METADATA:
sentence: Why Use a Private Registry?
search_anchor: Why Use a Private Registry
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Ready to Build Your Private Registry!
</div>

</v-click>

<!--
METADATA:
sentence: Azure Container Registry - Introduction What is Azure Container Registry?
search_anchor: Azure Container Registry - Introduction
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Create and manage your own container registry in Azure
</div>

</v-click>

</div>
