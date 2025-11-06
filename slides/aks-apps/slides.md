---
theme: default
background: https://images.unsplash.com/photo-1563986768494-4dee2763ff3f?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Securing AKS Apps with Key Vault and VNets
  Defense-in-depth security for AZ-204
drawings:
  persist: false
transition: slide-left
title: Securing AKS Apps
mdc: true
---

# Securing AKS Apps

Key Vault and Virtual Networks

<div class="abs-bottom-10 left-10">
  <carbon-security class="text-8xl text-red-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Securing Azure Kubernetes Service applications<br/>with Key Vault and Virtual Networks
</div>

</v-click>

<v-click>

<div class="text-lg mt-6 opacity-70">
Defense-in-depth security patterns
</div>

</v-click>

---
layout: section
---

# Concept Overview

---

# Security in AKS

<v-click>

<div class="mt-4">
  <carbon-security class="text-6xl text-red-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Security should be a primary concern
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    AKS[AKS<br/>Managed Environment] --> Azure[Azure<br/>Manages K8s]
    You[You] --> Resources[Secure Resources]
    Resources --> Storage[Storage Accounts]
    Resources --> KV[Key Vaults]
    style AKS fill:#326ce5
    style Azure fill:#0078d4
    style You fill:#ff6b6b
    style Storage fill:#ffd43b
    style KV fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg text-red-400">
Your responsibility: Secure sensitive resources
</div>

</v-click>

---

# Key Concepts

<v-click>

<div class="mt-8 text-center text-xl">
We'll work with several key concepts today
</div>

</v-click>

<v-click>

<div class="mt-12 grid grid-cols-2 gap-8">
  <div class="text-center">
    <carbon-network-3 class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Azure CNI Networking</div>
  </div>
  <div class="text-center">
    <carbon-network-overlay class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Service Endpoints</div>
  </div>
  <div class="text-center">
    <carbon-user-identification class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Managed Identities</div>
  </div>
  <div class="text-center">
    <carbon-locked class="text-5xl text-red-400" />
    <div class="text-sm mt-3">Network Security</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Azure Network Provider for AKS

---

# Default: kubenet

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Pods[Pods] --> Kubenet[kubenet<br/>Separate Address Space]
    Kubenet --> VNet[Virtual Network]
    style Kubenet fill:#ff6b6b
    style VNet fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Pods get IP addresses from separate address space
</div>

</v-click>

---

# Azure CNI

<v-click>

<div class="mt-4">
  <carbon-network-3 class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Container Network Interface
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Pods[Pods] --> CNI[Azure CNI]
    CNI --> Subnet[VNet Subnet]
    Subnet --> VNet[Virtual Network]
    style CNI fill:#51cf66
    style Subnet fill:#0078d4
    style VNet fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
AKS clusters run inside Azure Virtual Networks
</div>

</v-click>

---

# The Power of Azure CNI

<v-click>

<div class="mt-8 text-center text-xl">
Each Pod gets IP address directly from VNet subnet
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Pod1[Pod<br/>10.1.0.10] --> Subnet[VNet Subnet<br/>10.1.0.0/24]
    Pod2[Pod<br/>10.1.0.11] --> Subnet
    Pod3[Pod<br/>10.1.0.12] --> Subnet
    style Pod1 fill:#51cf66
    style Pod2 fill:#51cf66
    style Pod3 fill:#51cf66
    style Subnet fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg text-green-400">
Pods are first-class citizens in Azure network infrastructure
</div>

</v-click>

---

# Benefits

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-blue-400" />
  <span class="text-lg">Communicate directly with other Azure resources</span>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-security class="text-4xl text-red-400" />
  <span class="text-lg">Resources can identify Pods by subnet</span>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-locked class="text-4xl text-purple-400" />
  <span class="text-lg">Restrict access based on Pod subnet</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Powerful security capabilities
</div>

</v-click>

---
layout: section
---

# Service Endpoints and Network Security

---

# Virtual Network Service Endpoints

<v-click>

<div class="mt-4">
  <carbon-network-overlay class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Many Azure services support service endpoints
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-locked class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Key Vault</div>
  </div>
  <div class="text-center">
    <carbon-data-storage class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Storage Accounts</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg opacity-70">
And many more Azure services
</div>

</v-click>

---

# What Service Endpoints Do

<v-click>

<div class="mt-8 text-center text-xl">
Secure services to specific subnets
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Internet[Internet ❌] -->|Blocked| KV[Key Vault]
    Subnet[AKS Subnet ✓] -->|Allowed| KV
    style Internet fill:#ff6b6b
    style Subnet fill:#51cf66
    style KV fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Only accept traffic from specific subnets
</div>

</v-click>

---

# Reducing Attack Surface

<v-click>

<div class="mt-8 text-center text-2xl">
Before:
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg">
Key Vault accessible from entire Internet<br/>
<span class="text-sm opacity-70">(even with authentication)</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-4xl">↓</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-2xl">
After:
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg text-green-400">
Key Vault only accepts connections from AKS subnet
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Dramatically reduced attack surface
</div>

</v-click>

---
layout: section
---

# Managed Identities for Authentication

---

# Azure Managed Identities

<v-click>

<div class="mt-4">
  <carbon-user-identification class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Authentication handled through managed identities
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Pod[Pod] --> Addon[AKS KeyVault Add-on]
    Addon --> MI[Managed Identity]
    MI --> KV[Key Vault]
    style Pod fill:#51cf66
    style Addon fill:#326ce5
    style MI fill:#ff6b6b
    style KV fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Especially powerful in AKS
</div>

</v-click>

---

# The Benefits

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-close class="text-4xl text-red-400" />
  <span class="text-lg">No credentials in application code</span>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-logo-microsoft-azure class="text-4xl text-blue-400" />
  <span class="text-lg">Identity managed by Azure</span>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-renew class="text-4xl text-green-400" />
  <span class="text-lg">Rotated automatically</span>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-user-access class="text-4xl text-purple-400" />
  <span class="text-lg">Granted specific permissions via RBAC</span>
</div>

</v-click>

---
layout: section
---

# The Lab Scenario

---

# Asset Manager Application

<v-click>

<div class="mt-8 text-center text-xl">
Deploy Asset Manager app to AKS
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    App[Asset Manager] --> Blob[Azure Blob Storage]
    Blob --> Secrets[Connection String<br/>Sensitive!]
    Secrets --> KV[Key Vault]
    style App fill:#51cf66
    style Blob fill:#0078d4
    style Secrets fill:#ff6b6b
    style KV fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Uses Blob Storage for data persistence
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Connection string stored in Key Vault
</div>

</v-click>

---

# Security Architecture - Layer 1

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400">1</div>
  <div>
    <carbon-network-3 class="text-3xl inline-block" />
    <span class="ml-3 text-lg">AKS cluster runs inside dedicated VNet</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph TB
    subgraph VNet [Virtual Network]
        subgraph AKS Subnet
            Pod1[Pod]
            Pod2[Pod]
            Pod3[Pod]
        end
    end
    style Pod1 fill:#51cf66
    style Pod2 fill:#51cf66
    style Pod3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Using Azure CNI networking
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-sm opacity-70">
All Pods have IP addresses from subnet
</div>

</v-click>

---

# Security Architecture - Layer 2

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400">2</div>
  <div>
    <carbon-locked class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Key Vault locked to AKS subnet only</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Internet[Internet ❌] -->|Denied| KV[Key Vault]
    Pods[AKS Pods ✓] -->|Allowed| KV
    style Internet fill:#ff6b6b
    style Pods fill:#51cf66
    style KV fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Firewall rules deny all except AKS subnet
</div>

</v-click>

---

# Security Architecture - Layer 3

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400">3</div>
  <div>
    <carbon-data-storage class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Storage Account locked to AKS subnet</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Internet[Internet ❌] -->|Denied| Storage[Storage Account]
    Pods[AKS Pods ✓] -->|Allowed| Storage
    style Internet fill:#ff6b6b
    style Pods fill:#51cf66
    style Storage fill:#0078d4
```

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Only AKS Pods can access stored data
</div>

</v-click>

---

# Security Architecture - Layer 4

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400">4</div>
  <div>
    <carbon-folder class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Secrets mounted as Pod filesystem volumes</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    KV[Key Vault] -->|CSI Driver| Volume[Pod Volume]
    Volume --> App[Application]
    style KV fill:#0078d4
    style Volume fill:#ffd43b
    style App fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
AKS KeyVault Secrets Provider add-on
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-sm opacity-70">
Seamlessly available to application
</div>

</v-click>

---
layout: section
---

# Security Benefits

---

# Multiple Layers of Security

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-blue-400" />
  <div>
    <div class="text-lg font-bold">Network isolation</div>
    <div class="text-sm opacity-70">Resources only accessible from specific subnets</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-identification class="text-4xl text-green-400" />
  <div>
    <div class="text-lg font-bold">Identity-based access</div>
    <div class="text-sm opacity-70">No credentials in code or environment variables</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-purple-400" />
  <div>
    <div class="text-lg font-bold">Principle of least privilege</div>
    <div class="text-sm opacity-70">Each component has only needed permissions</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-shield class="text-4xl text-red-400" />
  <div>
    <div class="text-lg font-bold">Defense in depth</div>
    <div class="text-sm opacity-70">Multiple security controls protecting same resources</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What You'll Learn

---

# Lab Objectives

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-network-3 class="text-3xl text-blue-400 mt-1" />
  <span class="text-base">Deploy AKS cluster into VNet using Azure CNI</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-network-overlay class="text-3xl text-green-400 mt-1" />
  <span class="text-base">Configure service endpoints for Key Vault and Storage</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-locked class="text-3xl text-purple-400 mt-1" />
  <span class="text-base">Restrict Key Vault access using network rules</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-user-access class="text-3xl text-orange-400 mt-1" />
  <span class="text-base">Grant AKS managed identity access to Key Vault secrets</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-deploy class="text-3xl text-red-400 mt-1" />
  <span class="text-base">Deploy apps consuming Key Vault secrets as mounted volumes</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-data-storage class="text-3xl text-blue-500 mt-1" />
  <span class="text-base">Secure Storage Accounts with VNet firewall rules</span>
</div>

</v-click>

---

# Production Pattern

<v-click>

<div class="mt-8 text-center text-xl">
Critical pattern for production AKS deployments
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-security class="text-6xl text-red-400" />
    <div class="text-sm mt-3">Security</div>
  </div>
  <div class="text-center">
    <carbon-certificate class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Compliance</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg text-green-400">
Where security and compliance are requirements
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
Setting up our secure infrastructure
</div>

</v-click>

</div>
