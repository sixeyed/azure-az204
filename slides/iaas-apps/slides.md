---
theme: default
background: https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## IaaS Apps
  Traditional application deployment for AZ-204
drawings:
  persist: false
transition: slide-left
title: IaaS Apps
mdc: true
---

# IaaS Apps

Deploying Traditional Applications

<div class="abs-bottom-10 left-10">
  <carbon-virtual-machine class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Deploy applications using Azure IaaS<br/>Traditional workload migration path
</div>

</v-click>

---
layout: section
---

# What You'll Learn

---

# IaaS for Traditional Apps

<v-click>

<div class="mt-4">
  <carbon-virtual-machine class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Deploy traditional applications using IaaS resources
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg">
While PaaS is often the end goal
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
IaaS provides straightforward migration path
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
For existing workloads
</div>

</v-click>

---
layout: section
---

# Lab Scenario

---

# Legacy .NET Framework Application

<v-click>

<div class="mt-8 text-center text-xl">
The kind many organizations still run
</div>

</v-click>

<v-click>

<div class="mt-12 grid grid-cols-2 gap-8">
  <div class="text-center">
    <carbon-logo-windows class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Windows Server</div>
  </div>
  <div class="text-center">
    <carbon-data-base class="text-6xl text-green-400" />
    <div class="text-sm mt-3">SQL Server</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Both fully supported in Azure
</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# Infrastructure-as-a-Service

<v-click>

<div class="mt-4">
  <carbon-settings class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Complete control over virtual machines
</div>

</v-click>

<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-settings-adjust class="text-4xl text-blue-400" />
  <span class="text-lg">Manage operating system</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-app class="text-4xl text-green-400" />
  <span class="text-lg">Control runtime environment</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-application class="text-4xl text-purple-400" />
  <span class="text-lg">Configure applications</span>
</div>

</v-click>

---

# When to Use IaaS

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-migrate class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Migrating to Cloud</div>
    <div class="text-sm mt-2 opacity-70">Lift and shift existing applications</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-settings class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Specific OS Config</div>
    <div class="text-sm mt-2 opacity-70">Applications need specific configurations</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-security class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Full Control</div>
    <div class="text-sm mt-2 opacity-70">Need complete infrastructure control</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What We'll Build

---

# Complete Application Environment

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-base class="text-4xl text-blue-400" />
  <span class="text-lg">SQL Database for application data</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-virtual-machine class="text-4xl text-green-400" />
  <span class="text-lg">Windows Server 2022 virtual machine</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-application-web class="text-4xl text-purple-400" />
  <span class="text-lg">IIS web server hosting .NET Framework app</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-orange-400" />
  <span class="text-lg">Network configuration for secure connectivity</span>
</div>

</v-click>

---

# Architecture

<v-click>

<div class="mt-8">

```mermaid
graph TB
    VNet[Virtual Network] --> VM[Windows Server VM<br/>+ IIS]
    VM --> SQL[Azure SQL Database]
    VM --> App[.NET Framework 4.8<br/>Application]
    style VNet fill:#0078d4
    style VM fill:#51cf66
    style SQL fill:#ffd43b
    style App fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Straightforward architecture
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
VM in virtual network connected to SQL Database
</div>

</v-click>

---
layout: section
---

# Prerequisites

---

# What You Need

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-blue-400" />
  <span class="text-lg">Active Azure subscription</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-command-line class="text-4xl text-green-400" />
  <span class="text-lg">Azure CLI installed and configured</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-screen class="text-4xl text-purple-400" />
  <span class="text-lg">Remote Desktop client for Windows VMs</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-script class="text-4xl text-orange-400" />
  <span class="text-lg">Basic familiarity with PowerShell</span>
</div>

</v-click>

---

# Time to Complete

<v-click>

<div class="mt-12 text-center text-2xl">
Approximately 45 minutes
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Including resource provisioning time
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Create[Create Resources<br/>~15 min] --> Configure[Configure<br/>~20 min]
    Configure --> Deploy[Deploy App<br/>~10 min]
    style Create fill:#0078d4
    style Configure fill:#ffd43b
    style Deploy fill:#51cf66
```

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
Create Azure resources and deploy the application
</div>

</v-click>

</div>
