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

<!--
METADATA:
sentence: Securing AKS Apps with Key Vault and Virtual Networks - Introduction Opening Welcome to this lab on securing Azure Kubernetes Service applications with Key Vault and Virtual Networks.
search_anchor: Securing AKS Apps with Key
-->
<v-click>

<div class="text-xl mt-8">
Securing Azure Kubernetes Service applications<br/>with Key Vault and Virtual Networks
</div>

</v-click>

<!--
METADATA:
sentence: In this session, we'll explore how to implement defense-in-depth security patterns by leveraging Azure's networking capabilities to restrict access to sensitive resources.
search_anchor: this session, we'll explore how
-->
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

<!--
METADATA:
sentence: Concept Overview When running applications in AKS, security should be a primary concern.
search_anchor: Concept Overview When running applications
-->
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

<!--
METADATA:
sentence: In this session, we'll explore how to implement defense-in-depth security patterns by leveraging Azure's networking capabilities to restrict access to sensitive resources.
search_anchor: this session, we'll explore how
-->
<v-click>

<div class="mt-8 text-center text-lg text-red-400">
Your responsibility: Secure sensitive resources
</div>

</v-click>

---

# Key Concepts

<!--
METADATA:
sentence: Let me explain the key concepts we'll be working with today.
search_anchor: Let me explain the key
-->
<v-click>

<div class="mt-8 text-center text-xl">
We'll work with several key concepts today
</div>

</v-click>

<!--
METADATA:
sentence: Service Endpoints and Network Security Many Azure services support virtual network service endpoints.
search_anchor: Service Endpoints and Network Security
-->
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

<!--
METADATA:
sentence: All Pods will have IP addresses from our subnet.
search_anchor: All Pods will have IP
-->
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

<!--
METADATA:
sentence: However, Azure also supports the Azure CNI - Container Network Interface - which allows AKS clusters to run inside Azure Virtual Networks.
search_anchor: However, Azure also supports the
-->
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

<!--
METADATA:
sentence: However, Azure also supports the Azure CNI - Container Network Interface - which allows AKS clusters to run inside Azure Virtual Networks.
search_anchor: However, Azure also supports the
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
AKS clusters run inside Azure Virtual Networks
</div>

</v-click>

---

# The Power of Azure CNI

<!--
METADATA:
sentence: When you use Azure CNI, each Pod in your cluster gets an IP address directly from the VNet subnet.
search_anchor: When you use Azure CNI
-->
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

<!--
METADATA:
sentence: This is powerful because now your Pods are first-class citizens in your Azure network infrastructure.
search_anchor: This is powerful because now
-->
<v-click>

<div class="mt-8 text-center text-lg text-green-400">
Pods are first-class citizens in Azure network infrastructure
</div>

</v-click>

---

# Benefits

<!--
METADATA:
sentence: They can communicate directly with other Azure resources, and more importantly, those resources can identify and restrict access based on the subnet the Pods are running in.
search_anchor: They can communicate directly with
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-blue-400" />
  <span class="text-lg">Communicate directly with other Azure resources</span>
</div>

</v-click>

<!--
METADATA:
sentence: All Pods will have IP addresses from our subnet.
search_anchor: All Pods will have IP
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-security class="text-4xl text-red-400" />
  <span class="text-lg">Resources can identify Pods by subnet</span>
</div>

</v-click>

<!--
METADATA:
sentence: They can communicate directly with other Azure resources, and more importantly, those resources can identify and restrict access based on the subnet the Pods are running in.
search_anchor: They can communicate directly with
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-locked class="text-4xl text-purple-400" />
  <span class="text-lg">Restrict access based on Pod subnet</span>
</div>

</v-click>

<!--
METADATA:
sentence: This is powerful because now your Pods are first-class citizens in your Azure network infrastructure.
search_anchor: This is powerful because now
-->
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

<!--
METADATA:
sentence: Service Endpoints and Network Security Many Azure services support virtual network service endpoints.
search_anchor: Service Endpoints and Network Security
-->
<v-click>

<div class="mt-8 text-xl text-center">
Many Azure services support service endpoints
</div>

</v-click>

<!--
METADATA:
sentence: This includes Key Vault and Storage Accounts.
search_anchor: This includes Key Vault and
-->
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

<!--
METADATA:
sentence: Service Endpoints and Network Security Many Azure services support virtual network service endpoints.
search_anchor: Service Endpoints and Network Security
-->
<v-click>

<div class="mt-12 text-center text-lg opacity-70">
And many more Azure services
</div>

</v-click>

---

# What Service Endpoints Do

<!--
METADATA:
sentence: Service endpoints allow you to secure these services to only accept traffic from specific subnets in your virtual network.
search_anchor: Service endpoints allow you to
-->
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

<!--
METADATA:
sentence: Service endpoints allow you to secure these services to only accept traffic from specific subnets in your virtual network.
search_anchor: Service endpoints allow you to
-->
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

<!--
METADATA:
sentence: Even though the vault is technically accessible via the Internet, the firewall rules will deny all traffic except what comes from our Pods.
search_anchor: Even though the vault is
-->
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

<!--
METADATA:
sentence: Second, we'll configure the Key Vault to only accept connections from the AKS subnet.
search_anchor: Second, we'll configure the Key
-->
<v-click>

<div class="mt-6 text-center text-lg text-green-400">
Key Vault only accepts connections from AKS subnet
</div>

</v-click>

<!--
METADATA:
sentence: This dramatically reduces your attack surface.
search_anchor: This dramatically reduces your attack
-->
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

<!--
METADATA:
sentence: Managed Identities for Authentication Authentication is handled through Azure Managed Identities.
search_anchor: Managed Identities for Authentication Authentication
-->
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

<!--
METADATA:
sentence: We've seen this pattern before in other labs, but it's especially powerful in AKS.
search_anchor: We've seen this pattern before
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Especially powerful in AKS
</div>

</v-click>

---

# The Benefits

<!--
METADATA:
sentence: This means your application code never needs to handle credentials for accessing Key Vault.
search_anchor: This means your application code
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-close class="text-4xl text-red-400" />
  <span class="text-lg">No credentials in application code</span>
</div>

</v-click>

<!--
METADATA:
sentence: Managed Identities for Authentication Authentication is handled through Azure Managed Identities.
search_anchor: Managed Identities for Authentication Authentication
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-logo-microsoft-azure class="text-4xl text-blue-400" />
  <span class="text-lg">Identity managed by Azure</span>
</div>

</v-click>

<!--
METADATA:
sentence: The identity is managed by Azure, rotated automatically, and can be granted specific permissions through Azure RBAC or Key Vault access policies.
search_anchor: identity is managed by Azure
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-renew class="text-4xl text-green-400" />
  <span class="text-lg">Rotated automatically</span>
</div>

</v-click>

<!--
METADATA:
sentence: The identity is managed by Azure, rotated automatically, and can be granted specific permissions through Azure RBAC or Key Vault access policies.
search_anchor: identity is managed by Azure
-->
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

<!--
METADATA:
sentence: The Lab Scenario In today's lab, we'll deploy a sample application called Asset Manager to AKS.
search_anchor: Lab Scenario In today's lab
-->
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

<!--
METADATA:
sentence: This application uses Azure Blob Storage to persist data.
search_anchor: This application uses Azure Blob
-->
<v-click>

<div class="mt-8 text-center text-lg">
Uses Blob Storage for data persistence
</div>

</v-click>

<!--
METADATA:
sentence: The connection string for the storage account contains sensitive credentials, so we'll store it in Azure Key Vault.
search_anchor: connection string for the storage
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Connection string stored in Key Vault
</div>

</v-click>

---

# Security Architecture - Layer 1

<!--
METADATA:
sentence: Here's what makes this scenario interesting from a security perspective: First, the AKS cluster will run inside a dedicated VNet using Azure CNI networking.
search_anchor: Here's what makes this scenario
-->
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

<!--
METADATA:
sentence: Here's what makes this scenario interesting from a security perspective: First, the AKS cluster will run inside a dedicated VNet using Azure CNI networking.
search_anchor: Here's what makes this scenario
-->
<v-click>

<div class="mt-8 text-center text-lg">
Using Azure CNI networking
</div>

</v-click>

<!--
METADATA:
sentence: All Pods will have IP addresses from our subnet.
search_anchor: All Pods will have IP
-->
<v-click>

<div class="mt-4 text-center text-sm opacity-70">
All Pods have IP addresses from subnet
</div>

</v-click>

---

# Security Architecture - Layer 2

<!--
METADATA:
sentence: Second, we'll configure the Key Vault to only accept connections from the AKS subnet.
search_anchor: Second, we'll configure the Key
-->
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

<!--
METADATA:
sentence: Even though the vault is technically accessible via the Internet, the firewall rules will deny all traffic except what comes from our Pods.
search_anchor: Even though the vault is
-->
<v-click>

<div class="mt-8 text-center text-lg">
Firewall rules deny all except AKS subnet
</div>

</v-click>

---

# Security Architecture - Layer 3

<!--
METADATA:
sentence: Second, we'll configure the Key Vault to only accept connections from the AKS subnet.
search_anchor: Second, we'll configure the Key
-->
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

<!--
METADATA:
sentence: Third, we'll extend this same pattern to the Storage Account itself - locking it down so only the AKS Pods can access the stored data.
search_anchor: Third, we'll extend this same
-->
<v-click>

<div class="mt-8 text-center text-lg">
Only AKS Pods can access stored data
</div>

</v-click>

---

# Security Architecture - Layer 4

<!--
METADATA:
sentence: Finally, we'll use the AKS KeyVault Secrets Provider add-on to mount the connection string secret directly into the Pod filesystem, making it seamlessly available to the application.
search_anchor: Finally, we'll use the AKS
-->
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

<!--
METADATA:
sentence: Finally, we'll use the AKS KeyVault Secrets Provider add-on to mount the connection string secret directly into the Pod filesystem, making it seamlessly available to the application.
search_anchor: Finally, we'll use the AKS
-->
<v-click>

<div class="mt-8 text-center text-lg">
AKS KeyVault Secrets Provider add-on
</div>

</v-click>

<!--
METADATA:
sentence: The Lab Scenario In today's lab, we'll deploy a sample application called Asset Manager to AKS.
search_anchor: Lab Scenario In today's lab
-->
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

<!--
METADATA:
sentence: Service endpoints allow you to secure these services to only accept traffic from specific subnets in your virtual network.
search_anchor: Service endpoints allow you to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-blue-400" />
  <div>
    <div class="text-lg font-bold">Network isolation</div>
    <div class="text-sm opacity-70">Resources only accessible from specific subnets</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This means your application code never needs to handle credentials for accessing Key Vault.
search_anchor: This means your application code
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-identification class="text-4xl text-green-400" />
  <div>
    <div class="text-lg font-bold">Identity-based access</div>
    <div class="text-sm opacity-70">No credentials in code or environment variables</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This includes Key Vault and Storage Accounts.
search_anchor: This includes Key Vault and
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-purple-400" />
  <div>
    <div class="text-lg font-bold">Principle of least privilege</div>
    <div class="text-sm opacity-70">Each component has only needed permissions</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: In this session, we'll explore how to implement defense-in-depth security patterns by leveraging Azure's networking capabilities to restrict access to sensitive resources.
search_anchor: this session, we'll explore how
-->
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

<!--
METADATA:
sentence: Here's what makes this scenario interesting from a security perspective: First, the AKS cluster will run inside a dedicated VNet using Azure CNI networking.
search_anchor: Here's what makes this scenario
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-network-3 class="text-3xl text-blue-400 mt-1" />
  <span class="text-base">Deploy AKS cluster into VNet using Azure CNI</span>
</div>

</v-click>

<!--
METADATA:
sentence: This includes Key Vault and Storage Accounts.
search_anchor: This includes Key Vault and
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-network-overlay class="text-3xl text-green-400 mt-1" />
  <span class="text-base">Configure service endpoints for Key Vault and Storage</span>
</div>

</v-click>

<!--
METADATA:
sentence: This includes Key Vault and Storage Accounts.
search_anchor: This includes Key Vault and
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-locked class="text-3xl text-purple-400 mt-1" />
  <span class="text-base">Restrict Key Vault access using network rules</span>
</div>

</v-click>

<!--
METADATA:
sentence: The AKS KeyVault add-on creates a managed identity that can authenticate to Key Vault on behalf of your Pods.
search_anchor: AKS KeyVault add-on creates a
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-user-access class="text-3xl text-orange-400 mt-1" />
  <span class="text-base">Grant AKS managed identity access to Key Vault secrets</span>
</div>

</v-click>

<!--
METADATA:
sentence: This includes Key Vault and Storage Accounts.
search_anchor: This includes Key Vault and
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-deploy class="text-3xl text-red-400 mt-1" />
  <span class="text-base">Deploy apps consuming Key Vault secrets as mounted volumes</span>
</div>

</v-click>

<!--
METADATA:
sentence: This includes Key Vault and Storage Accounts.
search_anchor: This includes Key Vault and
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-data-storage class="text-3xl text-blue-500 mt-1" />
  <span class="text-base">Secure Storage Accounts with VNet firewall rules</span>
</div>

</v-click>

---

# Production Pattern

<!--
METADATA:
sentence: We've seen this pattern before in other labs, but it's especially powerful in AKS.
search_anchor: We've seen this pattern before
-->
<v-click>

<div class="mt-8 text-center text-xl">
Critical pattern for production AKS deployments
</div>

</v-click>

<!--
METADATA:
sentence: Concept Overview When running applications in AKS, security should be a primary concern.
search_anchor: Concept Overview When running applications
-->
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

<!--
METADATA:
sentence: This includes Key Vault and Storage Accounts.
search_anchor: This includes Key Vault and
-->
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

<!--
METADATA:
sentence: Let's get started by setting up our infrastructure.
search_anchor: Let's get started by setting
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: Let's get started by setting up our infrastructure.
search_anchor: Let's get started by setting
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Setting up our secure infrastructure
</div>

</v-click>

</div>
