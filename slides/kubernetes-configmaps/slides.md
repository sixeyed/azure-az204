---
theme: default
background: https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes ConfigMaps
  Externalizing configuration for AZ-204
drawings:
  persist: false
transition: slide-left
title: ConfigMaps
mdc: true
---

# Kubernetes ConfigMaps

Externalizing Application Configuration

<div class="abs-bottom-10 left-10">
  <carbon-settings class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Kubernetes ConfigMaps<br/>Separate configuration from container images
</div>

</v-click>

---
layout: section
---

# What Are ConfigMaps?

---

# Configuration Store

<v-click>

<div class="mt-4">
  <carbon-document class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Kubernetes object storing configuration data
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
As key-value pairs
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Image[Container Image] --> App[Application]
    ConfigMap[ConfigMap] --> App
    style Image fill:#0078d4
    style ConfigMap fill:#51cf66
    style App fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Code completely separate from configuration
</div>

</v-click>

---

# Two Main Formats

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-parameter class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Key-Value Pairs</span>
    <div class="text-sm mt-2 opacity-70">Read as environment variables</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-document-blank class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Full Text Files</span>
    <div class="text-sm mt-2 opacity-70">JSON or YAML configuration files</div>
    <div class="text-sm opacity-70">Mounted into filesystem</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Why ConfigMaps Matter

---

# The Traditional Problem

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Change[Config Change] --> Rebuild[Rebuild Image]
    Rebuild --> Test[Test Again]
    Test --> Deploy[Redeploy]
    style Change fill:#ff6b6b
    style Rebuild fill:#ff6b6b
    style Test fill:#ff6b6b
    style Deploy fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Slow, error-prone, against immutable infrastructure
</div>

</v-click>

---

# The ConfigMap Solution

<v-click>

<div class="mt-8">

```mermaid
graph LR
    Image[Build Image Once] --> Dev[Dev ConfigMap]
    Image --> Staging[Staging ConfigMap]
    Image --> Prod[Prod ConfigMap]
    style Image fill:#51cf66
    style Dev fill:#0078d4
    style Staging fill:#0078d4
    style Prod fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Same image, different configurations
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Twelve-Factor App methodology in action
</div>

</v-click>

---

# Separation of Concerns

<v-click>

<div class="mt-12 flex justify-center gap-16">
  <div class="text-center">
    <carbon-code class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Developers</div>
    <div class="text-xs mt-2 opacity-70">Focus on code</div>
  </div>
  <div class="text-center">
    <carbon-settings class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Operations</div>
    <div class="text-xs mt-2 opacity-70">Manage configuration</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
No hardcoded values in images
</div>

</v-click>

---
layout: section
---

# ConfigMaps in AKS

---

# Azure Integration

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-locked class="text-4xl text-blue-400" />
  <span class="text-lg">Integrate with Azure Key Vault for secrets</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings-adjust class="text-4xl text-green-400" />
  <span class="text-lg">Use with Azure App Configuration</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-purple-400" />
  <span class="text-lg">Manage through Azure DevOps pipelines</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-id-management class="text-4xl text-orange-400" />
  <span class="text-lg">Work with AKS managed identities</span>
</div>

</v-click>

---
layout: section
---

# Two Methods of Using ConfigMaps

---

# Environment Variables

<v-click>

<div class="mt-4">
  <carbon-parameter class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Inject as environment variables
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg">
Perfect for simple settings:
</div>

</v-click>

<v-click>

<div class="mt-8 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-flag class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Feature Flags</div>
  </div>
  <div class="text-center">
    <carbon-api class="text-5xl text-green-400" />
    <div class="text-sm mt-3">API Endpoints</div>
  </div>
  <div class="text-center">
    <carbon-version class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Version Numbers</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Application reads like any environment variable
</div>

</v-click>

---

# Volume Mounts

<v-click>

<div class="mt-4">
  <carbon-document-blank class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Mount as files in filesystem
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    ConfigMap[ConfigMap<br/>File Contents] --> Mount[Mount at Path]
    Mount --> Container[Container<br/>Filesystem]
    style ConfigMap fill:#51cf66
    style Mount fill:#ffd43b
    style Container fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Better for complex configuration files
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
JSON settings, XML config, etc.
</div>

</v-click>

---
layout: section
---

# AZ-204 Exam Connection

---

# Key Exam Topics

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Implement containerized solutions</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Configure application settings</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Manage configuration across environments</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Essential knowledge areas
</div>

</v-click>

---

# What You'll Be Tested On

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-decision-tree class="text-4xl text-blue-400" />
  <span class="text-lg">ConfigMaps vs Secrets</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-base class="text-4xl text-green-400" />
  <span class="text-lg">Mounting configuration as volumes</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-renew class="text-4xl text-purple-400" />
  <span class="text-lg">Updating running applications</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-structured class="text-4xl text-orange-400" />
  <span class="text-lg">Configuration hierarchy</span>
</div>

</v-click>

---
layout: section
---

# What You'll Learn Today

---

# Lab Objectives

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create ConfigMaps using YAML manifests</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-parameter class="text-4xl text-green-400" />
  <span class="text-lg">Inject as environment variables</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-base class="text-4xl text-purple-400" />
  <span class="text-lg">Mount as files</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-chart-network class="text-4xl text-orange-400" />
  <span class="text-lg">Understand configuration hierarchy</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Best practices for externalizing configuration
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
Master Kubernetes configuration management
</div>

</v-click>

</div>
