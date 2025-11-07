---
theme: default
background: https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure App Service
  PaaS for web applications - AZ-204
drawings:
  persist: false
transition: slide-left
title: Azure App Service
mdc: true
---

# Azure App Service

Platform-as-a-Service for Web Apps

<div class="abs-bottom-10 left-10">
  <carbon-application-web class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Azure App Service for Web Apps<br/>One of Azure's most popular PaaS offerings
</div>

</v-click>

---
layout: section
---

# Understanding PaaS vs IaaS

---

# IaaS: Infrastructure-as-a-Service

<v-click>

<div class="mt-4">
  <carbon-virtual-machine class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Complete Control
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-checkmark class="text-3xl text-green-400" />
  <span>Access to host machine configuration</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-checkmark class="text-3xl text-green-400" />
  <span>Control over OS, runtime, server config</span>
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-red-400">
Significant Management Overhead
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-3xl text-red-400" />
  <span>Patching, updates, security, scaling</span>
</div>

</v-click>

---

# PaaS: Platform-as-a-Service

<v-click>

<div class="mt-4">
  <carbon-application-web class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Focus on Your Application
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    You[You] -->|Manage| App[Application Code]
    Azure[Azure] -->|Manages| Infra[Servers + OS + Runtime + Scaling]
    style You fill:#51cf66
    style App fill:#51cf66
    style Azure fill:#0078d4
    style Infra fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Azure handles infrastructure management
</div>

</v-click>

---

# The Trade-Off

<v-click>

<div class="mt-8 flex justify-center gap-16">
  <div class="text-center">
    <div class="text-xl font-bold text-red-400 mb-4">IaaS</div>
    <carbon-warning class="text-6xl text-red-400" />
    <div class="text-sm mt-4">More Control</div>
    <div class="text-sm">More Management</div>
  </div>
  <div class="text-center">
    <div class="text-xl font-bold text-green-400 mb-4">PaaS</div>
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-4">Less Control</div>
    <div class="text-sm">Less Management</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Application must fit within PaaS constraints
</div>

</v-click>

---
layout: section
---

# What is Azure App Service?

---

# Fully Managed Platform

<v-click>

<div class="mt-4">
  <carbon-application-web class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
One of Azure's most popular PaaS offerings
</div>

</v-click>

<v-click>

<div class="mt-12 text-lg text-center">
Build, deploy, and scale web applications
</div>

</v-click>

---

# Supported Languages

<v-click>

<div class="mt-8 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-logo-dotnet class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">.NET</div>
  </div>
  <div class="text-center">
    <carbon-logo-java class="text-6xl text-red-400" />
    <div class="text-sm mt-3">Java</div>
  </div>
  <div class="text-center">
    <carbon-logo-nodejs class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Node.js</div>
  </div>
  <div class="text-center">
    <carbon-logo-python class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Python</div>
  </div>
  <div class="text-center">
    <carbon-code class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">PHP</div>
  </div>
  <div class="text-center">
    <carbon-application class="text-6xl text-orange-400" />
    <div class="text-sm mt-3">More...</div>
  </div>
</div>

</v-click>

---

# Key Features

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-scale class="text-4xl text-blue-400" />
  <span class="text-lg">Built-in auto-scaling capabilities</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-green-400" />
  <span class="text-lg">Continuous deployment from various sources</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-logo-github class="text-4xl text-purple-400" />
  <span class="text-lg">Integration with Azure DevOps and GitHub</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-test-tool class="text-4xl text-orange-400" />
  <span class="text-lg">Staging environments for testing</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-network-4 class="text-4xl text-red-400" />
  <span class="text-lg">Built-in load balancing</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-locked class="text-4xl text-blue-500" />
  <span class="text-lg">Automatic HTTPS</span>
</div>

</v-click>

---
layout: section
---

# What We'll Build Today

---

# Lab Overview

<v-click>

<div class="mt-8 text-center text-xl">
Push source code directly from local machine
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Local[Local Code] -->|Git Push| Azure[Azure]
    Azure -->|Compile & Configure| Running[Running App]
    style Local fill:#51cf66
    style Azure fill:#0078d4
    style Running fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Azure handles everything automatically
</div>

</v-click>

---

# What We'll Do

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-add class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create an App Service Plan</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-application-web class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create a Web App for Git deployment</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-deploy class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Deploy ASP.NET app by pushing code</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-settings-adjust class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Configure application settings</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-red-400 mt-1">5</div>
  <div>
    <carbon-search class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Explore deployment and runtime environment</span>
  </div>
</div>

</v-click>

---
layout: section
---

# Lab Prerequisites

---

# What You'll Need

<v-click>

<div class="mt-6 flex items-center gap-4">
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
  <carbon-version-major class="text-4xl text-purple-400" />
  <span class="text-lg">Git installed on local machine</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-folder class="text-4xl text-orange-400" />
  <span class="text-lg">Access to course repository with sample code</span>
</div>

</v-click>

---
layout: section
---

# What to Expect

---

# The Deployment Experience

<v-click>

<div class="mt-8 text-center text-2xl text-green-400">
Entire process takes just a few minutes
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Push[Git Push] --> Compile[Azure Compiles]
    Compile --> Configure[Azure Configures]
    Configure --> Deploy[Azure Deploys]
    Deploy --> Live[Live Web App]
    style Push fill:#51cf66
    style Compile fill:#0078d4
    style Configure fill:#0078d4
    style Deploy fill:#0078d4
    style Live fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Azure handles everything automatically
</div>

</v-click>

---

# The Outcome

<v-click>

<div class="mt-12 text-center text-2xl">
Live web application running on Azure
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-close class="text-6xl text-red-400" />
    <div class="text-sm mt-3">No VMs</div>
  </div>
  <div class="text-center">
    <carbon-close class="text-6xl text-red-400" />
    <div class="text-sm mt-3">No Infrastructure</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Just Your App</div>
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
Deploy your first App Service web application
</div>

</v-click>

</div>
