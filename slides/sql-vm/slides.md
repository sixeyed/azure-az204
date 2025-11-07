---
theme: default
background: https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## SQL Server VMs
  Complete SQL Server control in Azure - AZ-204
drawings:
  persist: false
transition: slide-left
title: SQL VMs
mdc: true
---

# SQL Server Virtual Machines

Complete Control in Azure

<div class="abs-bottom-10 left-10">
  <carbon-virtual-machine class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore SQL Server VMs<br/>When you need full SQL Server features
</div>

</v-click>

---
layout: section
---

# Why SQL Server VMs?

---

# Feature Gaps

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Managed SQL options should be preferred
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Azure SQL Database and SQL Managed Instance
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-orange-400">
But they don't support 100% of SQL Server features
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Datacenter[SQL Server<br/>Datacenter] -.->|Not All Features| Managed[Managed<br/>SQL Options]
    Datacenter -->|All Features| VM[SQL Server VM]
    style Datacenter fill:#ffd43b
    style Managed fill:#ff6b6b
    style VM fill:#51cf66
```

</div>

</v-click>

---

# When You Need Features

<v-click>

<div class="mt-12 text-center text-xl">
Occasions where you need a feature
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-red-400">
Not available in managed options
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
That's where SQL VMs come in
</div>

</v-click>

---
layout: section
---

# Complete Control

---

# Set Up Your Way

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
SQL VM service provides complete control
</div>

</v-click>

<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-settings class="text-4xl text-blue-400" />
  <span class="text-lg">Configure operating system exactly as needed</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-base class="text-4xl text-green-400" />
  <span class="text-lg">Deploy SQL Server your way</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-purple-400" />
  <span class="text-lg">Access to all SQL Server features</span>
</div>

</v-click>

---
layout: section
---

# What We'll Cover

---

# Lab Topics

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-browser class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Explore Azure SQL Options</span>
    <div class="text-sm mt-2 opacity-70">Linux and Windows variants</div>
    <div class="text-sm opacity-70">Different SQL Server versions and SKUs</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-terminal class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Create VM with Azure CLI</span>
    <div class="text-sm mt-2 opacity-70">Find right VM image</div>
    <div class="text-sm opacity-70">SQL Server 2019 Standard on Windows Server 2022</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-deployment-pattern class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Register with SQL IaaS Extension</span>
    <div class="text-sm mt-2 opacity-70">Transform to managed-like service</div>
    <div class="text-sm opacity-70">Enhanced management capabilities</div>
  </div>
</div>

</v-click>

---

# More Lab Topics

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-network-3 class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Configure Public Access</span>
    <div class="text-sm mt-2 opacity-70">Set up SQL authentication</div>
    <div class="text-sm opacity-70">Username and password</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-red-400 mt-1">5</div>
  <div>
    <carbon-code class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Real-World Use Case</span>
    <div class="text-sm mt-2 opacity-70">User-Defined Function calling .NET code</div>
    <div class="text-sm opacity-70">Not available in managed options</div>
  </div>
</div>

</v-click>

---
layout: section
---

# SQL IaaS Extension

---

# Enhanced Management

<v-click>

<div class="mt-8 text-center text-xl">
Register VM with SQL Server IaaS extension
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    VM[Standard VM] --> Register[Register with<br/>SQL IaaS Extension]
    Register --> Enhanced[Enhanced<br/>Management]
    style VM fill:#ffd43b
    style Register fill:#0078d4
    style Enhanced fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Transforms VM into managed-like service
</div>

</v-click>

---
layout: section
---

# Feature Example

---

# User-Defined Functions

<v-click>

<div class="mt-8 text-center text-xl">
Create UDF that calls .NET code
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-orange-400">
Requires direct file system access
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-orange-400">
Requires elevated SQL Server permissions
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
Not available with managed database options
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Perfect example of why you might need SQL VMs
</div>

</v-click>

---
layout: section
---

# Trade-offs

---

# Managed vs VMs

<v-click>

<div class="mt-8 flex justify-center gap-16">
  <div class="text-center">
    <carbon-cloud-services class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Managed SQL</div>
    <div class="text-xs mt-2 text-green-400">Automatic maintenance</div>
    <div class="text-xs mt-1 text-green-400">High availability built-in</div>
    <div class="text-xs mt-1 text-red-400">Some features missing</div>
  </div>
  <div class="text-center">
    <carbon-virtual-machine class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">SQL VMs</div>
    <div class="text-xs mt-2 text-green-400">All SQL Server features</div>
    <div class="text-xs mt-1 text-green-400">Complete control</div>
    <div class="text-xs mt-1 text-red-400">You manage OS/patches</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Choose managed when possible
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Use VMs when you need specific features
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
Explore SQL Server VMs in Azure
</div>

</v-click>

</div>
