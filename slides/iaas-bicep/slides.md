---
theme: default
background: https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## IaaS with Bicep
  Automated application deployment for AZ-204
drawings:
  persist: false
transition: slide-left
title: IaaS Bicep
mdc: true
---

# IaaS with Bicep

Automating Application Deployment

<div class="abs-bottom-10 left-10">
  <carbon-deployment-pattern class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: IaaS Bicep - Introduction Narration Script Opening Welcome to this lab on automating application deployment with Infrastructure as a Service using Bicep.
search_anchor: IaaS Bicep - Introduction Narration
-->
<v-click>

<div class="text-xl mt-8">
Automate application deployment with IaaS<br/>Using Bicep for Infrastructure as Code
</div>

</v-click>

---
layout: section
---

# The IaaS Automation Story

---

# IaaS Doesn't Mean Manual

<v-click>

<div class="mt-4">
  <carbon-warning class="text-6xl text-red-400" />
</div>

</v-click>

<!--
METADATA:
sentence: The IaaS Automation Story When we think about Infrastructure as a Service, it's easy to imagine manually logging into virtual machines and deploying applications by hand.
search_anchor: IaaS Automation Story When we
-->
<v-click>

<div class="mt-8 text-xl text-center text-red-400">
Easy to imagine: logging in and deploying by hand
</div>

</v-click>

<!--
METADATA:
sentence: But that's not how we work in modern cloud environments.
search_anchor: But that's not how we
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
But that's not how we work in modern cloud
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Manual[Manual Deployment] -.->|❌ Old Way| Slow[Slow + Error Prone]
    Auto[Automated IaaS] -->|✓ Modern| Fast[Fast + Reliable]
    style Manual fill:#ff6b6b
    style Slow fill:#ff6b6b
    style Auto fill:#51cf66
    style Fast fill:#51cf66
```

</div>

</v-click>

---

# Full Control + Automation

<!--
METADATA:
sentence: IaaS doesn't mean manual - it means we have full control over our infrastructure, and we can automate every aspect of it.
search_anchor: IaaS doesn't mean manual -
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
IaaS means full control over infrastructure
</div>

</v-click>

<!--
METADATA:
sentence: IaaS doesn't mean manual - it means we have full control over our infrastructure, and we can automate every aspect of it.
search_anchor: IaaS doesn't mean manual -
-->
<v-click>

<div class="mt-12 text-center text-xl">
And we can automate every aspect of it
</div>

</v-click>

<!--
METADATA:
sentence: IaaS doesn't mean manual - it means we have full control over our infrastructure, and we can automate every aspect of it.
search_anchor: IaaS doesn't mean manual -
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-settings class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Full Control</div>
  </div>
  <div class="text-center">
    <carbon-add class="text-6xl text-green-400" />
  </div>
  <div class="text-center">
    <carbon-automation class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Complete Automation</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What We'll Build

---

# Complete Automated Stack

<!--
METADATA:
sentence: What We'll Build The scenario we're working with is a .NET web application that needs a SQL Server backend.
search_anchor: What We'll Build The scenario
-->
<v-click>

<div class="mt-8 text-center text-xl">
.NET web application with SQL Server backend
</div>

</v-click>

<!--
METADATA:
sentence: In a traditional environment, this might take hours or days to set up: provisioning VMs, configuring networks, installing SQL Server, deploying the application, and setting up all the configuration.
search_anchor: traditional environment, this might take
-->
<v-click>

<div class="mt-12 text-center text-lg">
Traditional environment might take hours or days:
</div>

</v-click>

<!--
METADATA:
sentence: In a traditional environment, this might take hours or days to set up: provisioning VMs, configuring networks, installing SQL Server, deploying the application, and setting up all the configuration.
search_anchor: traditional environment, this might take
-->
<v-click>

<div class="mt-8 grid grid-cols-2 gap-6">
  <div class="text-sm opacity-70">Provision VMs</div>
  <div class="text-sm opacity-70">Configure networks</div>
  <div class="text-sm opacity-70">Install SQL Server</div>
  <div class="text-sm opacity-70">Deploy application</div>
  <div class="text-sm opacity-70">Set up configuration</div>
  <div class="text-sm opacity-70">Test everything</div>
</div>

</v-click>

<!--
METADATA:
sentence: With Bicep and Azure IaaS, we can automate all of that into a repeatable, reliable deployment that runs in minutes.
search_anchor: Bicep and Azure IaaS, we
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
With Bicep and Azure IaaS: Minutes
</div>

</v-click>

---
layout: section
---

# The Bicep Approach

---

# Modular Infrastructure Files

<v-click>

<div class="mt-4">
  <carbon-document-multiple class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: The Bicep Approach What makes this approach powerful is how Bicep lets us split our infrastructure model across multiple files.
search_anchor: Bicep Approach What makes this
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Split infrastructure across multiple files
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Main[Main Template] --> Network[network.bicep<br/>Core networking]
    Main --> DB[database.bicep<br/>Database resources]
    Main --> VM[vm.bicep<br/>Application VMs]
    style Main fill:#0078d4
    style Network fill:#51cf66
    style DB fill:#51cf66
    style VM fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: The Automation Story But we're not stopping at infrastructure.
search_anchor: Automation Story But we're not
-->
<v-click>

<div class="mt-8 text-center text-xl">
Clean, modular, maintainable
</div>

</v-click>

---

# Not One Massive Template

<!--
METADATA:
sentence: One of the most powerful features we'll demonstrate is the VM custom script extension.
search_anchor: One of the most powerful
-->
<v-click>

<div class="mt-12 flex justify-center gap-16">
  <div class="text-center">
    <carbon-document class="text-6xl text-red-400" />
    <div class="text-sm mt-3">Single Huge File</div>
    <div class="text-xs mt-2 opacity-70">Hard to read</div>
    <div class="text-xs opacity-70">Hard to maintain</div>
  </div>
  <div class="text-center">
    <carbon-document-multiple class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Modular Files</div>
    <div class="text-xs mt-2 opacity-70">Easy to read</div>
    <div class="text-xs opacity-70">Easy to maintain</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: With Bicep and Azure IaaS, we can automate all of that into a repeatable, reliable deployment that runs in minutes.
search_anchor: Bicep and Azure IaaS, we
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Files reference each other and share variables
</div>

</v-click>

---
layout: section
---

# Beyond Infrastructure

---

# VM Custom Script Extension

<v-click>

<div class="mt-4">
  <carbon-script class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: This lets us run PowerShell scripts automatically when the VM is created - scripts that can install dependencies, deploy applications, and configure everything exactly how we need it.
search_anchor: This lets us run PowerShell
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Run PowerShell scripts automatically when VM is created
</div>

</v-click>

<!--
METADATA:
sentence: By the end of this lab, we'll have a fully automated deployment pipeline.
search_anchor: By the end of this
-->
<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-download class="text-4xl text-blue-400" />
  <span class="text-lg">Install dependencies</span>
</div>

</v-click>

<!--
METADATA:
sentence: By the end of this lab, we'll have a fully automated deployment pipeline.
search_anchor: By the end of this
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-green-400" />
  <span class="text-lg">Deploy applications</span>
</div>

</v-click>

<!--
METADATA:
sentence: This lets us run PowerShell scripts automatically when the VM is created - scripts that can install dependencies, deploy applications, and configure everything exactly how we need it.
search_anchor: This lets us run PowerShell
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings-adjust class="text-4xl text-purple-400" />
  <span class="text-lg">Configure everything exactly as needed</span>
</div>

</v-click>

---

# Fully Automated Deployment

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Deploy[Run Deployment] --> Infra[Create Infrastructure]
    Infra --> Script[Execute Custom Scripts]
    Script --> Install[Install Dependencies]
    Install --> App[Deploy Application]
    App --> Config[Configure Services]
    Config --> Ready[✓ Ready to Use]
    style Deploy fill:#0078d4
    style Infra fill:#ffd43b
    style Script fill:#ffd43b
    style Install fill:#ffd43b
    style App fill=#ffd43b
    style Config fill:#ffd43b
    style Ready fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Run a few commands, and you'll have a complete application stack running in Azure, with no manual intervention required.
search_anchor: Run a few commands, and
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
No manual intervention required
</div>

</v-click>

---

# The Power of Automation

<!--
METADATA:
sentence: Run a few commands, and you'll have a complete application stack running in Azure, with no manual intervention required.
search_anchor: Run a few commands, and
-->
<v-click>

<div class="mt-8 text-center text-xl">
Run a few commands
</div>

</v-click>

<!--
METADATA:
sentence: Run a few commands, and you'll have a complete application stack running in Azure, with no manual intervention required.
search_anchor: Run a few commands, and
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Get complete application stack
</div>

</v-click>

<v-click>

<div class="mt-12">

```bash
az deployment group create \
  --resource-group my-rg \
  --template-file main.bicep
```

</div>

</v-click>

<!--
METADATA:
sentence: With Bicep and Azure IaaS, we can automate all of that into a repeatable, reliable deployment that runs in minutes.
search_anchor: Bicep and Azure IaaS, we
-->
<v-click>

<div class="mt-12 text-center text-xl">
Everything deployed and configured
</div>

</v-click>

<!--
METADATA:
sentence: Run a few commands, and you'll have a complete application stack running in Azure, with no manual intervention required.
search_anchor: Run a few commands, and
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Infrastructure + Application + Configuration
</div>

</v-click>

---

# Repeatable and Reliable

<!--
METADATA:
sentence: With Bicep and Azure IaaS, we can automate all of that into a repeatable, reliable deployment that runs in minutes.
search_anchor: Bicep and Azure IaaS, we
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-repeat class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Repeatable</div>
    <div class="text-xs mt-2 opacity-70">Same every time</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Reliable</div>
    <div class="text-xs mt-2 opacity-70">No human error</div>
  </div>
  <div class="text-center">
    <carbon-flash class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Fast</div>
    <div class="text-xs mt-2 opacity-70">Minutes not hours</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: In this lab, we're going to demonstrate the power of combining IaaS with Infrastructure as Code using Bicep.
search_anchor: this lab, we're going to
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
This is the power of IaaS + Infrastructure as Code
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
sentence: The Automation Story But we're not stopping at infrastructure.
search_anchor: Automation Story But we're not
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: By the end of this lab, we'll have a fully automated deployment pipeline.
search_anchor: By the end of this
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Build a fully automated deployment pipeline
</div>

</v-click>

</div>
