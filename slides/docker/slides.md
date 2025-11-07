---
theme: default
background: https://images.unsplash.com/photo-1493946740644-2d8a1f1a6aff?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Docker 101
  Container fundamentals for AZ-204
drawings:
  persist: false
transition: slide-left
title: Docker 101
mdc: true
---

# Docker 101

Container Fundamentals

<div class="abs-bottom-10 left-10">
  <carbon-docker class="text-8xl text-blue-500 opacity-80" />
</div>

---
layout: center
---

# Welcome to Docker

<!--
METADATA:
sentence: In this lab, we're going to explore one of the most important technologies for deploying applications in the cloud: Docker containers.
search_anchor: this lab, we're going to
-->
<v-click>

<div class="text-xl mt-8">
Explore one of the most important technologies<br/>for deploying applications in the cloud
</div>

</v-click>

---
layout: section
---

# The Problem Statement

---

# How to Run a .NET App on Azure?

<!--
METADATA:
sentence: But this approach has some significant challenges.
search_anchor: But this approach has some
-->
<v-click>

<div class="mt-12 text-center text-xl">
Traditional approach:
</div>

</v-click>

<!--
METADATA:
sentence: No need to provision and configure new VMs from scratch.
search_anchor: No need to provision and
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <span>Provision a virtual machine</span>
</div>

</v-click>

<!--
METADATA:
sentence: Need to handle more traffic?
search_anchor: Need to handle more traffic
-->
<v-click>

<div class="mt-4 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">2</div>
  <span>Connect to it</span>
</div>

</v-click>

<!--
METADATA:
sentence: First, it's hard to automate all those steps.
search_anchor: First, it's hard to automate
-->
<v-click>

<div class="mt-4 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">3</div>
  <span>Install .NET</span>
</div>

</v-click>

<!--
METADATA:
sentence: You're managing not just your application, but the entire infrastructure around it.
search_anchor: You're managing not just your
-->
<v-click>

<div class="mt-4 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">4</div>
  <span>Download application binaries</span>
</div>

</v-click>

<!--
METADATA:
sentence: You'll see the Docker whale icon in your taskbar.
search_anchor: You'll see the Docker whale
-->
<v-click>

<div class="mt-4 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">5</div>
  <span>Set up configuration</span>
</div>

</v-click>

<!--
METADATA:
sentence: Just run more containers from the same image.
search_anchor: Just run more containers from
-->
<v-click>

<div class="mt-4 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">6</div>
  <span>Start the app</span>
</div>

</v-click>

---

# Significant Challenges

<!--
METADATA:
sentence: First, it's hard to automate all those steps.
search_anchor: First, it's hard to automate
-->
<v-click>

<div class="mt-10 flex items-center gap-4">
  <carbon-warning class="text-5xl text-red-400" />
  <div>
    <div class="text-xl font-bold">Hard to Automate</div>
    <div class="text-sm mt-2 opacity-70">Many manual steps</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Second, it's time-consuming to spin up a new instance.
search_anchor: Second, it's time-consuming to spin
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-time class="text-5xl text-orange-400" />
  <div>
    <div class="text-xl font-bold">Time-Consuming</div>
    <div class="text-sm mt-2 opacity-70">Slow to spin up new instances</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: And third, it's difficult to keep multiple instances in sync.
search_anchor: third, it's difficult to keep
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-misuse class="text-5xl text-purple-400" />
  <div>
    <div class="text-xl font-bold">Difficult to Sync</div>
    <div class="text-sm mt-2 opacity-70">Keeping multiple instances consistent</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: You're managing not just your application, but the entire infrastructure around it.
search_anchor: You're managing not just your
-->
<v-click>

<div class="mt-10 text-center text-xl text-red-400">
Managing application AND infrastructure
</div>

</v-click>

---

# What About App Service?

<!--
METADATA:
sentence: Now, you could use Azure App Service instead, which simplifies things.
search_anchor: Now, you could use Azure
-->
<v-click>

<div class="mt-12 text-center text-xl">
Azure App Service simplifies things...
</div>

</v-click>

<!--
METADATA:
sentence: Alright, let's get started with our first container.
search_anchor: Alright, let's get started with
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-checkmark class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Less Setup</div>
  </div>
  <div class="text-center">
    <carbon-warning class="text-6xl text-orange-400" />
    <div class="text-sm mt-3">Still Requires Config</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: But there's still a lot to set up, and you end up with a different hosting environment than what you have running locally on your development machine.
search_anchor: But there's still a lot
-->
<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Different hosting environment than local dev
</div>

</v-click>

<!--
METADATA:
sentence: This can lead to the classic "it works on my machine" problem.
search_anchor: This can lead to the
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
"It works on my machine" problem
</div>

</v-click>

---
layout: section
---

# Enter Docker

---

# The Docker Approach

<v-click>

<div class="mt-4">
  <carbon-docker class="text-8xl text-blue-500" />
</div>

</v-click>

<!--
METADATA:
sentence: With Docker, you build all your application components and dependencies into a package called an image.
search_anchor: Docker, you build all your
-->
<v-click>

<div class="mt-12 text-center text-xl">
Build components and dependencies into a package
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Build[Build] --> Image[Image<br/>Blueprint]
    Image --> Container[Container<br/>Running Instance]
    style Build fill:#ffd43b
    style Image fill:#2496ed
    style Container fill:#51cf66
```

</div>

</v-click>

---

# Docker Image

<v-click>

<div class="mt-4">
  <carbon-document-blank class="text-6xl text-blue-500" />
</div>

</v-click>

<!--
METADATA:
sentence: A container is a running instance of that image.
search_anchor: container is a running instance
-->
<v-click>

<div class="mt-8 text-xl text-center">
A blueprint - static package
</div>

</v-click>

<!--
METADATA:
sentence: Think of a Docker image as a blueprint - it's a static package that contains everything your application needs to run: your code, the runtime, system tools, libraries, and settings.
search_anchor: Think of a Docker image
-->
<v-click>

<div class="mt-12 text-lg">
Contains everything your app needs:
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-code class="text-3xl text-green-400" />
  <span>Your code</span>
</div>

</v-click>

<!--
METADATA:
sentence: Key Benefits The beauty of Docker is consistency.
search_anchor: Key Benefits The beauty of
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-chip class="text-3xl text-blue-400" />
  <span>The runtime</span>
</div>

</v-click>

<!--
METADATA:
sentence: Need to handle more traffic?
search_anchor: Need to handle more traffic
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-application class="text-3xl text-purple-400" />
  <span>System tools and libraries</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-settings class="text-3xl text-orange-400" />
  <span>Settings</span>
</div>

</v-click>

---

# Run Anywhere

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Image[Docker Image] --> Dev[Developer Laptop]
    Image --> Test[Test Environment]
    Image --> Prod[Production Azure]
    style Image fill:#2496ed
    style Dev fill:#51cf66
    style Test fill:#51cf66
    style Prod fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Just run more containers from the same image.
search_anchor: Just run more containers from
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Behaves exactly the same way everywhere
</div>

</v-click>

<!--
METADATA:
sentence: Once you've built an image, you can run it anywhere that has Docker installed, and it will behave exactly the same way.
search_anchor: Once you've built an image
-->
<v-click>

<div class="mt-6 text-center text-lg opacity-70">
Anywhere that has Docker installed
</div>

</v-click>

---

# Docker Container

<v-click>

<div class="mt-4">
  <carbon-container-software class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: A container is a running instance of that image.
search_anchor: container is a running instance
-->
<v-click>

<div class="mt-8 text-xl text-center">
A running instance of an image
</div>

</v-click>

<!--
METADATA:
sentence: It's lightweight, portable, and isolated from other containers and the host system.
search_anchor: It's lightweight, portable, and isolated
-->
<v-click>

<div class="mt-12 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-ibm-cloud-bare-metal-servers-vpc class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Lightweight</div>
  </div>
  <div class="text-center">
    <carbon-delivery class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Portable</div>
  </div>
  <div class="text-center">
    <carbon-locked class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Isolated</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: It's lightweight, portable, and isolated from other containers and the host system.
search_anchor: It's lightweight, portable, and isolated
-->
<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Isolated from other containers and host system
</div>

</v-click>

---
layout: section
---

# Key Benefits

---

# Consistency

<v-click>

<div class="mt-4">
  <carbon-checkmark-outline class="text-8xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Just run more containers from the same image.
search_anchor: Just run more containers from
-->
<v-click>

<div class="mt-12 text-center text-2xl">
Container starts from exactly the same image
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Laptop[Your Laptop] -->|Same Image| Test[Test Env]
    Test -->|Same Image| Azure[Production Azure]
    style Laptop fill:#51cf66
    style Test fill:#51cf66
    style Azure fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: This eliminates environment-specific bugs and makes deployments much more reliable.
search_anchor: This eliminates environment-specific bugs and
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Eliminates environment-specific bugs
</div>

</v-click>

---

# Scaling Made Easy

<!--
METADATA:
sentence: Need to handle more traffic?
search_anchor: Need to handle more traffic
-->
<v-click>

<div class="mt-8 text-center text-xl">
Need to handle more traffic?
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Image[Docker Image] --> C1[Container 1]
    Image --> C2[Container 2]
    Image --> C3[Container 3]
    Image --> C4[Container 4]
    style Image fill:#2496ed
    style C1 fill:#51cf66
    style C2 fill:#51cf66
    style C3 fill:#51cf66
    style C4 fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Just run more containers from the same image.
search_anchor: Just run more containers from
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Just run more containers from the same image
</div>

</v-click>

<!--
METADATA:
sentence: No need to provision and configure new VMs from scratch.
search_anchor: No need to provision and
-->
<v-click>

<div class="mt-6 text-center text-lg opacity-70">
No need to provision and configure new VMs
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
sentence: Just run more containers from the same image.
search_anchor: Just run more containers from
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-play class="text-4xl text-blue-400" />
  <span class="text-lg">Run pre-built container images from public registries</span>
</div>

</v-click>

<!--
METADATA:
sentence: Alright, let's get started with our first container.
search_anchor: Alright, let's get started with
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-logo-dotnet class="text-4xl text-purple-400" />
  <span class="text-lg">Work with different .NET container images</span>
</div>

</v-click>

<!--
METADATA:
sentence: You'll see the Docker whale icon in your taskbar.
search_anchor: You'll see the Docker whale
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-build-tool class="text-4xl text-green-400" />
  <span class="text-lg">Build your own custom Docker images</span>
</div>

</v-click>

<!--
METADATA:
sentence: Then you use that image to run instances of your applications called containers.
search_anchor: Then you use that image
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-package class="text-4xl text-orange-400" />
  <span class="text-lg">Package and run your own .NET applications</span>
</div>

</v-click>

---

# Beyond This Lab

<!--
METADATA:
sentence: Just run more containers from the same image.
search_anchor: Just run more containers from
-->
<v-click>

<div class="mt-12 text-center text-xl">
These same containers can be deployed to:
</div>

</v-click>

<!--
METADATA:
sentence: Now, you could use Azure App Service instead, which simplifies things.
search_anchor: Now, you could use Azure
-->
<v-click>

<div class="mt-10 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-container-software class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Azure Container Instances</div>
  </div>
  <div class="text-center">
    <carbon-application class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Azure Container Apps</div>
  </div>
  <div class="text-center">
    <carbon-kubernetes class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Azure Kubernetes Service</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Getting Started

---

# Prerequisites

<!--
METADATA:
sentence: Getting Started Before we dive into the exercises, make sure you have Docker Desktop installed and running.
search_anchor: Getting Started Before we dive
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-docker class="text-5xl text-blue-500" />
  <div>
    <div class="text-xl font-bold">Docker Desktop</div>
    <div class="text-sm mt-2 opacity-70">Installed and running</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: A container is a running instance of that image.
search_anchor: container is a running instance
-->
<v-click>

<div class="mt-10 flex items-center gap-4">
  <carbon-logo-linux class="text-5xl text-orange-400" />
  <div>
    <div class="text-xl font-bold">Linux Container Mode</div>
    <div class="text-sm mt-2 opacity-70">Windows users: ensure Linux mode is enabled</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Docker also makes scaling easier.
search_anchor: Docker also makes scaling easier
-->
<v-click>

<div class="mt-10 flex items-center gap-4">
  <carbon-command-line class="text-5xl text-green-400" />
  <div>
    <div class="text-xl font-bold">Docker CLI</div>
    <div class="text-sm mt-2 opacity-70">Command-line interface</div>
  </div>
</div>

</v-click>

---

# Docker CLI

<v-click>

<div class="mt-8">

```bash
docker --help
docker run --help
docker build --help
```

</div>

</v-click>

<!--
METADATA:
sentence: Need to handle more traffic?
search_anchor: Need to handle more traffic
-->
<v-click>

<div class="mt-8 text-center text-xl">
Similar to Azure CLI
</div>

</v-click>

<!--
METADATA:
sentence: It has built-in help, supports various subcommands, and gives you complete control over your container environment.
search_anchor: It has built-in help, supports
-->
<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <carbon-help class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Built-in help</div>
  </div>
  <div class="text-center">
    <carbon-terminal class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Subcommands</div>
  </div>
  <div class="text-center">
    <carbon-settings class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Complete control</div>
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

<!--
METADATA:
sentence: Alright, let's get started with our first container.
search_anchor: Alright, let's get started with
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: Alright, let's get started with our first container.
search_anchor: Alright, let's get started with
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Run your first container
</div>

</v-click>

</div>
