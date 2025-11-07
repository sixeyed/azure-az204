---
theme: default
background: https://images.unsplash.com/photo-1494412651409-8963ce7935a7?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Container Instances
  Introduction to ACI for AZ-204
drawings:
  persist: false
transition: slide-left
title: Azure Container Instances
mdc: true
---

# Azure Container Instances

Simplest Way to Run Containers in Azure

<div class="abs-bottom-10 left-10">
  <carbon-container-software class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome to Azure Container Instances

<!--
METADATA:
sentence: In this session, we'll explore one of Azure's simplest and most efficient ways to run containerized applications in the cloud.
search_anchor: this session, we'll explore one
-->
<v-click>

<div class="text-xl mt-8">
Explore one of Azure's simplest and most efficient ways<br/>to run containerized applications in the cloud
</div>

</v-click>

---
layout: two-cols
---

# What is ACI?

<v-click>

<div class="mt-4">
  <carbon-container-software class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Container Instances?
search_anchor: What is Azure Container Instances
-->
<v-click>

<div class="mt-6 text-lg">
Managed container service
</div>

</v-click>

<!--
METADATA:
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="mt-2 text-lg">
Run Docker containers in Azure
</div>

</v-click>

::right::

<v-click>

<div class="mt-20">

```mermaid
graph LR
    A[Docker Container] --> B[ACI]
    B --> C[Running in Azure]
    style B fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: No idle virtual machines consuming your budget.
search_anchor: No idle virtual machines consuming
-->
<v-click>

<div class="mt-8 text-center text-sm opacity-70">
No VMs • No orchestration
</div>

</v-click>

---
layout: center
---

<div class="text-center">

<v-click>

<carbon-docker class="text-8xl inline-block text-blue-500" />

</v-click>

<v-click>

<carbon-arrow-right class="text-6xl inline-block mx-8" />

</v-click>

<v-click>

<carbon-command-line class="text-6xl inline-block text-gray-500" />

</v-click>

<v-click>

<carbon-arrow-right class="text-6xl inline-block mx-8" />

</v-click>

<v-click>

<carbon-cloud class="text-8xl inline-block text-blue-400" />

</v-click>

</div>

<!--
METADATA:
sentence: With ACI, you can take that exact same container and run it in Azure with just a single command.
search_anchor: ACI, you can take that
-->
<v-click>

<div class="text-center mt-12 text-xl">
From local Docker to Azure with a single command
</div>

</v-click>

<!--
METADATA:
sentence: No servers to provision, no clusters to configure - just your application running in the cloud.
search_anchor: No servers to provision, no
-->
<v-click>

<div class="text-center mt-6 text-lg opacity-70">
No servers • No clusters • Just your application
</div>

</v-click>

---
layout: section
---

# Key Benefits

---

# Portability

<v-click>

<div class="mt-4">
  <carbon-copy-link class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph LR
    A[Docker Desktop] -->|Same Container| B[ACI]
    style A fill:#2496ed
    style B fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: If it works in Docker Desktop, it works in ACI.
search_anchor: If it works in Docker
-->
<v-click>

<div class="text-center mt-12 text-xl">
If it works in Docker Desktop, it works in ACI
</div>

</v-click>

<!--
METADATA:
sentence: This is the fundamental promise of containerization.
search_anchor: This is the fundamental promise
-->
<v-click>

<div class="text-center mt-4 text-lg opacity-70">
The fundamental promise of containerization
</div>

</v-click>

---

# Simplicity

<v-click>

<div class="mt-4">
  <carbon-checkmark-outline class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Simplicity: Unlike Azure Kubernetes Service or Azure App Service, ACI has minimal configuration.
search_anchor: Simplicity: Unlike Azure Kubernetes Service
-->
<v-click>

<div class="mt-8 text-lg">
Minimal configuration required:
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Container Instances?
search_anchor: What is Azure Container Instances
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-image class="text-3xl" />
  <span>Container image</span>
</div>

</v-click>

<!--
METADATA:
sentence: You specify an image, some compute resources, and you're running.
search_anchor: You specify an image, some
-->
<v-click>

<div class="mt-2 flex items-center gap-4">
  <carbon-chip class="text-3xl" />
  <span>Compute resources</span>
</div>

</v-click>

<!--
METADATA:
sentence: It's the fastest and simplest way to run a container in Azure.
search_anchor: It's the fastest and simplest
-->
<v-click>

<div class="mt-2 flex items-center gap-4">
  <carbon-play class="text-3xl text-green-500" />
  <span>Ready to run</span>
</div>

</v-click>

<!--
METADATA:
sentence: Simplicity: Unlike Azure Kubernetes Service or Azure App Service, ACI has minimal configuration.
search_anchor: Simplicity: Unlike Azure Kubernetes Service
-->
<v-click>

<div class="mt-8 text-center text-sm opacity-60">
Unlike AKS or App Service - no complex setup
</div>

</v-click>

---

# Speed

<v-click>

<div class="mt-4">
  <carbon-meter-alt class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="mt-8 text-2xl text-center">
Containers start in <span class="text-purple-400 font-bold">seconds</span>
</div>

</v-click>

<!--
METADATA:
sentence: Cost-effectiveness: You pay per second for exactly what you use.
search_anchor: Cost-effectiveness: You pay per second
-->
<v-click>

<div class="mt-12 text-lg">
Perfect for:
</div>

</v-click>

<!--
METADATA:
sentence: This makes it perfect for burst workloads, task automation, or development and testing scenarios.
search_anchor: This makes it perfect for
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-flash class="text-3xl text-yellow-400" />
  <span>Burst workloads</span>
</div>

</v-click>

<!--
METADATA:
sentence: This makes it perfect for burst workloads, task automation, or development and testing scenarios.
search_anchor: This makes it perfect for
-->
<v-click>

<div class="mt-2 flex items-center gap-4">
  <carbon-task class="text-3xl text-blue-400" />
  <span>Task automation</span>
</div>

</v-click>

<!--
METADATA:
sentence: This makes it perfect for burst workloads, task automation, or development and testing scenarios.
search_anchor: This makes it perfect for
-->
<v-click>

<div class="mt-2 flex items-center gap-4">
  <carbon-code class="text-3xl text-green-400" />
  <span>Development & testing</span>
</div>

</v-click>

---

# Cost-effectiveness

<v-click>

<div class="mt-4">
  <carbon-piggy-bank class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Cost-effectiveness: You pay per second for exactly what you use.
search_anchor: Cost-effectiveness: You pay per second
-->
<v-click>

<div class="mt-8 text-xl text-center">
Pay per second for exactly what you use
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TD
    A[Traditional VMs] -->|Always Running| B[💰 Constant Cost]
    C[ACI] -->|On-Demand| D[💚 Only When Used]
    style A fill:#ff6b6b
    style C fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: No idle virtual machines consuming your budget.
search_anchor: No idle virtual machines consuming
-->
<v-click>

<div class="text-center mt-8 text-lg opacity-70">
No idle virtual machines consuming your budget
</div>

</v-click>

---
layout: section
---

# When to Use ACI

---

# ACI Use Cases

<!--
METADATA:
sentence: DNS Name Label: ACI provides automatic DNS naming.
search_anchor: DNS Name Label: ACI provides
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-application-web class="text-4xl text-blue-400" />
  <span class="text-lg">Simple web applications</span>
</div>

</v-click>

<!--
METADATA:
sentence: DNS Name Label: ACI provides automatic DNS naming.
search_anchor: DNS Name Label: ACI provides
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-batch-job class="text-4xl text-purple-400" />
  <span class="text-lg">Batch processing</span>
</div>

</v-click>

<!--
METADATA:
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-assembly-cluster class="text-4xl text-green-400" />
  <span class="text-lg">Build agents (CI/CD)</span>
</div>

</v-click>

<!--
METADATA:
sentence: This makes it perfect for burst workloads, task automation, or development and testing scenarios.
search_anchor: This makes it perfect for
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-script class="text-4xl text-orange-400" />
  <span class="text-lg">Development and testing</span>
</div>

</v-click>

<!--
METADATA:
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-events class="text-4xl text-red-400" />
  <span class="text-lg">Event-driven applications</span>
</div>

</v-click>

<!--
METADATA:
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="mt-8 text-center text-sm opacity-60">
Single containers without complex orchestration needs
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
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-analytics class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Explore ACI capabilities through Azure Portal</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Container Instances?
search_anchor: What is Azure Container Instances
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">2</div>
  <div>
    <carbon-deploy class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Deploy containers using Azure CLI</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">3</div>
  <div>
    <carbon-dashboard class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Manage running containers</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: If it works in Docker Desktop, it works in ACI.
search_anchor: If it works in Docker
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">4</div>
  <div>
    <carbon-docker class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Use Docker CLI integration</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">5</div>
  <div>
    <carbon-compare class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Work with Linux and Windows containers</span>
  </div>
</div>

</v-click>

---
layout: section
---

# Architecture Overview

---

# What Azure Handles

<v-click>

<div class="mt-4">
  <carbon-cloud-services class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Container Instances?
search_anchor: What is Azure Container Instances
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-chip class="text-3xl" />
  <span>Compute infrastructure</span>
</div>

</v-click>

<!--
METADATA:
sentence: DNS Name Label: ACI provides automatic DNS naming.
search_anchor: DNS Name Label: ACI provides
-->
<v-click>

<div class="mt-3 flex items-center gap-4">
  <carbon-network-3 class="text-3xl" />
  <span>Network configuration and DNS</span>
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Container Instances?
search_anchor: What is Azure Container Instances
-->
<v-click>

<div class="mt-3 flex items-center gap-4">
  <carbon-document class="text-3xl" />
  <span>Storage for container logs</span>
</div>

</v-click>

<!--
METADATA:
sentence: It's the fastest and simplest way to run a container in Azure.
search_anchor: It's the fastest and simplest
-->
<v-click>

<div class="mt-3 flex items-center gap-4">
  <carbon-security class="text-3xl" />
  <span>Security and isolation</span>
</div>

</v-click>

---

# What You Control

<v-click>

<div class="mt-4">
  <carbon-settings-adjust class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Container Instances?
search_anchor: What is Azure Container Instances
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-image class="text-3xl" />
  <span>Container image to run</span>
</div>

</v-click>

<!--
METADATA:
sentence: Resource Allocation: You specify exactly how much CPU and memory your container needs, with granular control from fractional CPUs to multiple cores.
search_anchor: Resource Allocation: You specify exactly
-->
<v-click>

<div class="mt-3 flex items-center gap-4">
  <carbon-chip class="text-3xl" />
  <span>CPU and memory allocation</span>
</div>

</v-click>

<!--
METADATA:
sentence: Networking: Containers can expose ports to the internet or remain private.
search_anchor: Networking: Containers can expose ports
-->
<v-click>

<div class="mt-3 flex items-center gap-4">
  <carbon-port-output class="text-3xl" />
  <span>Network ports to expose</span>
</div>

</v-click>

<!--
METADATA:
sentence: You specify an image, some compute resources, and you're running.
search_anchor: You specify an image, some
-->
<v-click>

<div class="mt-3 flex items-center gap-4">
  <carbon-data-1 class="text-3xl" />
  <span>Environment variables and configuration</span>
</div>

</v-click>

<!--
METADATA:
sentence: You specify an image, some compute resources, and you're running.
search_anchor: You specify an image, some
-->
<v-click>

<div class="mt-3 flex items-center gap-4">
  <carbon-renew class="text-3xl" />
  <span>Restart policies and lifecycle</span>
</div>

</v-click>

---
layout: two-cols
---

# Architecture

<v-click>

```mermaid
graph TB
    subgraph Azure
        ACI[ACI Container]
        ACI --> Compute[Compute]
        ACI --> Network[Network]
        ACI --> Storage[Storage]
        ACI --> Security[Security]
    end
    style ACI fill:#0078d4
    style Azure fill:#e3f2fd
```

</v-click>

::right::

<v-click>

<div class="mt-20 ml-8">

```mermaid
graph TB
    You[You Configure]
    You --> Image[Image]
    You --> Resources[CPU/RAM]
    You --> Ports[Ports]
    You --> Config[Config]
    style You fill:#51cf66
```

</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# Container Registry

<v-click>

<div class="mt-4">
  <carbon-catalog class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Container Instances?
search_anchor: What is Azure Container Instances
-->
<v-click>

<div class="mt-8 text-lg">
Where your container images are stored
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph LR
    A[Docker Hub<br/>Public] --> C[ACI]
    B[Azure Container Registry<br/>Private] --> C
    D[Other Registries] --> C
    style A fill:#2496ed
    style B fill:#0078d4
    style C fill:#51cf66
```

</div>

</v-click>

---

# DNS Name Label

<v-click>

<div class="mt-4">
  <carbon-network-3 class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: DNS Name Label: ACI provides automatic DNS naming.
search_anchor: DNS Name Label: ACI provides
-->
<v-click>

<div class="mt-8 text-lg text-center">
ACI provides automatic DNS naming
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph LR
    A[Your DNS Prefix] --> B[myapp]
    B --> C[myapp.eastus.azurecontainer.io]
    style C fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: You can assign a friendly DNS prefix and ACI creates a full domain name for accessing your container.
search_anchor: You can assign a friendly
-->
<v-click>

<div class="mt-8 text-center text-sm opacity-70">
Assign a friendly DNS prefix → ACI creates full domain name
</div>

</v-click>

---

# Resource Allocation

<v-click>

<div class="mt-4">
  <carbon-chip class="text-6xl text-orange-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Resource Allocation: You specify exactly how much CPU and memory your container needs, with granular control from fractional CPUs to multiple cores.
search_anchor: Resource Allocation: You specify exactly
-->
<v-click>

<div class="mt-8 text-lg text-center">
Specify exactly how much CPU and memory you need
</div>

</v-click>

<!--
METADATA:
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <div class="text-3xl font-bold text-blue-400">0.5</div>
    <div class="text-sm mt-2">CPU Cores</div>
  </div>
  <div class="text-4xl opacity-50">→</div>
  <div class="text-center">
    <div class="text-3xl font-bold text-green-400">4</div>
    <div class="text-sm mt-2">CPU Cores</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Resource Allocation: You specify exactly how much CPU and memory your container needs, with granular control from fractional CPUs to multiple cores.
search_anchor: Resource Allocation: You specify exactly
-->
<v-click>

<div class="mt-8 text-center text-lg">
Granular control: fractional CPUs to multiple cores
</div>

</v-click>

---

# Networking

<v-click>

<div class="mt-4">
  <carbon-network-4 class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Internet[Internet] -->|Port 80/443| ACI[ACI Container]
    ACI -->|Private| VNet[Virtual Network]
    style ACI fill:#0078d4
    style Internet fill:#51cf66
    style VNet fill:#ff6b6b
```

</div>

</v-click>

<!--
METADATA:
sentence: Networking: Containers can expose ports to the internet or remain private.
search_anchor: Networking: Containers can expose ports
-->
<v-click>

<div class="mt-8 text-center text-lg">
Expose ports to internet or keep private
</div>

</v-click>

<!--
METADATA:
sentence: ACI handles all the underlying networking complexity.
search_anchor: ACI handles all the underlying
-->
<v-click>

<div class="mt-4 text-center text-sm opacity-70">
ACI handles all underlying networking complexity
</div>

</v-click>

---
layout: section
---

# Prerequisites

---

# Before You Start

<!--
METADATA:
sentence: What is Azure Container Instances?
search_anchor: What is Azure Container Instances
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-command-line class="text-4xl text-blue-400" />
  <span class="text-lg">Azure CLI installed and configured</span>
</div>

</v-click>

<!--
METADATA:
sentence: If it works in Docker Desktop, it works in ACI.
search_anchor: If it works in Docker
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-docker class="text-4xl text-blue-500" />
  <span class="text-lg">Docker Desktop installed</span>
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Container Instances?
search_anchor: What is Azure Container Instances
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-service-management class="text-4xl text-green-400" />
  <span class="text-lg">Active Azure subscription</span>
</div>

</v-click>

<!--
METADATA:
sentence: Key Benefits Portability: Your Docker containers run the same way everywhere.
search_anchor: Key Benefits Portability: Your Docker
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-book class="text-4xl text-purple-400" />
  <span class="text-lg">Basic familiarity with Docker and containers</span>
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
sentence: Speed: ACI containers start in seconds.
search_anchor: Speed: ACI containers start in
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: It's the fastest and simplest way to run a container in Azure.
search_anchor: It's the fastest and simplest
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
See how easy it is to run containers in Azure
</div>

</v-click>

</div>
