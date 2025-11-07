---
theme: default
background: https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Key Vault Access Security
  Network and identity security for AZ-204
drawings:
  persist: false
transition: slide-left
title: Key Vault Security
mdc: true
---

# Securing Key Vault Access

Defense in Depth for Sensitive Data

<div class="abs-bottom-10 left-10">
  <carbon-security class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Key Vault security<br/>Lock down access to sensitive data
</div>

</v-click>

---
layout: section
---

# Why Security Matters

---

# Your Most Sensitive Data

<v-click>

<div class="mt-4">
  <carbon-locked class="text-6xl text-red-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Key Vaults store critical secrets
</div>

</v-click>

<v-click>

<div class="mt-12 grid grid-cols-2 gap-8">
  <div class="text-center">
    <carbon-password class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Passwords</div>
  </div>
  <div class="text-center">
    <carbon-data-connected class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Connection Strings</div>
  </div>
  <div class="text-center">
    <carbon-api class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">API Keys</div>
  </div>
  <div class="text-center">
    <carbon-certificate class="text-5xl text-orange-400" />
    <div class="text-sm mt-3">Certificates</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Misconfiguration could expose everything
</div>

</v-click>

---
layout: section
---

# Two Layers of Security

---

# Defense in Depth

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Request[Incoming Request] --> Layer1{Network Security}
    Layer1 -->|Blocked| Deny1[❌ Access Denied]
    Layer1 -->|Allowed| Layer2{Identity Security}
    Layer2 -->|Unauthorized| Deny2[❌ Access Denied]
    Layer2 -->|Authorized| Grant[✓ Access Granted]
    style Request fill:#0078d4
    style Layer1 fill:#ffd43b
    style Layer2 fill:#ffd43b
    style Deny1 fill:#ff6b6b
    style Deny2 fill:#ff6b6b
    style Grant fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Both layers work together
</div>

</v-click>

---

# Layer 1: Network Security

<v-click>

<div class="mt-4">
  <carbon-network-3 class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Controls whether request can reach Key Vault
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-16">
  <div class="text-center">
    <carbon-earth class="text-6xl text-orange-400" />
    <div class="text-sm mt-3">Default: Any Network</div>
  </div>
  <div class="text-center">
    <carbon-arrow-right class="text-6xl text-gray-400" />
  </div>
  <div class="text-center">
    <carbon-network-4 class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Restrict: Specific VNets</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
First line of defense
</div>

</v-click>

---

# Layer 2: Identity Security

<v-click>

<div class="mt-4">
  <carbon-user-certification class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Caller must authenticate as authorized principal
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg">
Azure uses "principal" for any identity
</div>

</v-click>

<v-click>

<div class="mt-8 grid grid-cols-2 gap-8">
  <div class="text-center">
    <carbon-user class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">User Accounts</div>
  </div>
  <div class="text-center">
    <carbon-user-multiple class="text-5xl text-green-400" />
    <div class="text-sm mt-3">User Groups</div>
  </div>
  <div class="text-center">
    <carbon-application class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Service Principals</div>
  </div>
  <div class="text-center">
    <carbon-id-management class="text-5xl text-orange-400" />
    <div class="text-sm mt-3">Managed Identities</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What We'll Cover

---

# Lab Flow

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-add class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create Key Vault and store secret</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-network-3 class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Lock down network access to specific VNet</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-virtual-machine class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create VM in that network</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-id-management class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Configure managed identity</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Defense in depth in action
</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# Access Policies

<v-click>

<div class="mt-4">
  <carbon-security class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Define what principals can do
</div>

</v-click>

<v-click>

<div class="mt-12 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-view class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Secrets</div>
  </div>
  <div class="text-center">
    <carbon-locked class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Keys</div>
  </div>
  <div class="text-center">
    <carbon-certificate class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Certificates</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg">
Configured in Key Vault itself
</div>

</v-click>

---

# Service Endpoints

<v-click>

<div class="mt-4">
  <carbon-data-connected class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Allow Azure services to communicate with VNet resources
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    KV[Key Vault] -->|Service Endpoint| Subnet[VNet Subnet]
    Subnet --> VM[VM Resources]
    style KV fill:#0078d4
    style Subnet fill:#51cf66
    style VM fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Secure connectivity without public internet
</div>

</v-click>

---

# Managed Identities

<v-click>

<div class="mt-4">
  <carbon-id-management class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Azure-managed identities for Azure services
</div>

</v-click>

<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-close class="text-4xl text-green-400" />
  <span class="text-lg">No passwords to manage</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-close class="text-4xl text-green-400" />
  <span class="text-lg">No credentials in code</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Azure handles everything automatically</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Secure authentication without credential management
</div>

</v-click>

---

# The Complete Flow

<v-click>

<div class="mt-8">

```mermaid
graph TB
    VM[VM with<br/>Managed Identity] -->|Network Request| Endpoint[Service Endpoint]
    Endpoint -->|Through VNet| KV[Key Vault]
    KV -->|Check Identity| Auth{Authorized?}
    Auth -->|Yes| Secret[Return Secret]
    Auth -->|No| Deny[Access Denied]
    style VM fill:#0078d4
    style Endpoint fill:#51cf66
    style KV fill:#0078d4
    style Secret fill:#51cf66
    style Deny fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Both layers protecting your secrets
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
Implement defense in depth for Key Vault
</div>

</v-click>

</div>
