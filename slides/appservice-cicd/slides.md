---
theme: default
background: https://images.unsplash.com/photo-1556075798-4825dfaaf498?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## App Service CI/CD
  Continuous deployment for AZ-204
drawings:
  persist: false
transition: slide-left
title: CI/CD
mdc: true
---

# App Service CI/CD

Continuous Integration and Deployment

<div class="abs-bottom-10 left-10">
  <carbon-deployment-pattern class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Automate deployments to Azure App Service<br/>Using GitHub and deployment slots
</div>

</v-click>

---
layout: section
---

# What is App Service CI/CD?

---

# Two Powerful Features

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-logo-github class="text-5xl text-blue-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Deployments</div>
    <div class="text-sm mt-2 opacity-70">Automatically triggered on Git push</div>
    <div class="text-sm opacity-70">Eliminates manual deployment steps</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-test-tool class="text-5xl text-green-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Deployment Slots</div>
    <div class="text-sm mt-2 opacity-70">Deploy to staging before production</div>
    <div class="text-sm opacity-70">Test thoroughly, then promote</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Ensures application always up to date
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Reduces risk and ensures quality
</div>

</v-click>

---
layout: section
---

# Lab Overview

---

# Working with Random Number API

<v-click>

<div class="mt-8 text-center text-xl">
.NET Core API demonstrating CI/CD concepts
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Repo[GitHub Repo] -->|1. Manual| Azure[Azure App Service]
    Repo -->|2. Auto Deploy| Azure
    Azure --> Staging[Staging Slot]
    Staging -->|Swap| Prod[Production]
    style Repo fill:#51cf66
    style Azure fill:#0078d4
    style Staging fill:#ffd43b
    style Prod fill:#ff6b6b
```

</div>

</v-click>

---

# What We'll Do

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-logo-github class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Deploy from your own GitHub repository</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-deploy class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Set up manual deployment first</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-continuous-deployment class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Configure continuous deployment</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-test-tool class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create staging slot for testing</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-red-400 mt-1">5</div>
  <div>
    <carbon-swap-horizontal class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Swap slots to promote to production</span>
  </div>
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
  <carbon-logo-github class="text-4xl text-purple-400" />
  <span class="text-lg">GitHub account with fork of lab repository</span>
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
  <carbon-version-major class="text-4xl text-orange-400" />
  <span class="text-lg">Basic understanding of Git and GitHub workflows</span>
</div>

</v-click>

---
layout: section
---

# Why This Matters

---

# Essential Modern Practices

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-checkmark-outline class="text-4xl text-blue-400" />
  <span class="text-lg">Reduce manual errors in deployment</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-flash class="text-4xl text-green-400" />
  <span class="text-lg">Enable faster iteration and feedback cycles</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-repeat class="text-4xl text-purple-400" />
  <span class="text-lg">Provide consistent, repeatable process</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-orange-400" />
  <span class="text-lg">Safe testing before production release</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Critical knowledge for AZ-204 exam
</div>

</v-click>

---

# CI/CD Pipeline Flow

<v-click>

<div class="mt-8">

```mermaid
graph LR
    Code[Code Change] --> Push[Git Push]
    Push --> Build[Automated Build]
    Build --> Test[Run Tests]
    Test --> Deploy[Deploy to Staging]
    Deploy --> Verify[Verify & Test]
    Verify --> Swap[Swap to Production]
    style Code fill:#51cf66
    style Push fill:#0078d4
    style Build fill:#0078d4
    style Test fill:#0078d4
    style Deploy fill:#ffd43b
    style Verify fill:#ffd43b
    style Swap fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Progressively enhance deployment pipeline
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
Build your CI/CD pipeline
</div>

</v-click>

</div>
