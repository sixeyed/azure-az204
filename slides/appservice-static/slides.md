---
theme: default
background: https://images.unsplash.com/photo-1547658719-da2b51169166?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Static Web Apps
  Modern static site hosting for AZ-204
drawings:
  persist: false
transition: slide-left
title: Static Web Apps
mdc: true
---

# Azure Static Web Apps

Modern Hosting for Static Content

<div class="abs-bottom-10 left-10">
  <carbon-document class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: App Service for Static Web Apps - Introduction Welcome to this lab on Azure Static Web Apps and App Service for static content.
search_anchor: App Service for Static Web
-->
<v-click>

<div class="text-xl mt-8">
Explore Azure Static Web Apps and App Service<br/>For static content hosting
</div>

</v-click>

---
layout: section
---

# The Context

---

# App Service Capabilities

<!--
METADATA:
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="mt-8 text-center text-xl">
App Service excels at complex web applications
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Code[Source Code] --> Compile[Compile]
    Compile --> Package[Package]
    Package --> Deploy[Deploy]
    style Code fill:#51cf66
    style Compile fill:#0078d4
    style Package fill:#0078d4
    style Deploy fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: In this lab, we'll explore two different approaches for hosting static web content in Azure.
search_anchor: this lab, we'll explore two
-->
<v-click>

<div class="mt-12 text-center text-xl">
But there's a simpler option for static content
</div>

</v-click>

<!--
METADATA:
sentence: Azure Static Web Apps is a service designed specifically for modern web applications that consist of static content - HTML, CSS, JavaScript - and optionally serverless API backends.
search_anchor: Azure Static Web Apps is
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
HTML, CSS, JavaScript without backend processing
</div>

</v-click>

---
layout: section
---

# What are Static Web Apps?

---

# Purpose-Built Service

<v-click>

<div class="mt-4">
  <carbon-document class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="mt-8 text-xl text-center">
Designed for modern web applications
</div>

</v-click>

<!--
METADATA:
sentence: Azure Static Web Apps is a service designed specifically for modern web applications that consist of static content - HTML, CSS, JavaScript - and optionally serverless API backends.
search_anchor: Azure Static Web Apps is
-->
<v-click>

<div class="mt-12 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-html class="text-6xl text-orange-400" />
    <div class="text-sm mt-3">HTML</div>
  </div>
  <div class="text-center">
    <carbon-data-structured class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">CSS</div>
  </div>
  <div class="text-center">
    <carbon-script class="text-6xl text-yellow-400" />
    <div class="text-sm mt-3">JavaScript</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Static Web Apps is a service designed specifically for modern web applications that consist of static content - HTML, CSS, JavaScript - and optionally serverless API backends.
search_anchor: Azure Static Web Apps is
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Plus optional serverless API backends
</div>

</v-click>

---

# Deployment Model

<!--
METADATA:
sentence: Unlike traditional App Service deployments, Static Web Apps are deployed directly from a Git repository, with automated build and deployment workflows managed through GitHub Actions or Azure DevOps.
search_anchor: Unlike traditional App Service deployments
-->
<v-click>

<div class="mt-8 text-center text-xl">
Deploy directly from Git repository
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Repo[GitHub Repo] -->|Fork| Your[Your Fork]
    Your -->|Connect| Azure[Azure Config]
    Azure -->|Creates| Actions[GitHub Actions]
    Actions -->|Deploy| Live[Live Site]
    style Repo fill:#51cf66
    style Your fill:#51cf66
    style Azure fill:#0078d4
    style Actions fill:#ffd43b
    style Live fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: Unlike traditional App Service deployments, Static Web Apps are deployed directly from a Git repository, with automated build and deployment workflows managed through GitHub Actions or Azure DevOps.
search_anchor: Unlike traditional App Service deployments
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Automated build and deployment workflows
</div>

</v-click>

<!--
METADATA:
sentence: Unlike traditional App Service deployments, Static Web Apps are deployed directly from a Git repository, with automated build and deployment workflows managed through GitHub Actions or Azure DevOps.
search_anchor: Unlike traditional App Service deployments
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Managed through GitHub Actions or Azure DevOps
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
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-logo-github class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create Static Web App from GitHub</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Continuous Deployment - You'll make changes to your content and see how GitHub Actions automatically deploy those changes to your live site.
search_anchor: Continuous Deployment - You'll make
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-continuous-deployment class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Experience continuous deployment</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Static Web Apps - Introduction Welcome to this lab on Azure Static Web Apps and App Service for static content.
search_anchor: App Service for Static Web
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-application-web class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Compare with traditional App Service</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Mixed Content Scenarios - You'll deploy a Node.js application that serves both static content and dynamic endpoints, exploring how to handle authentication and identity providers.
search_anchor: Mixed Content Scenarios - You'll
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-hybrid-networking class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Deploy mixed content scenarios</span>
  </div>
</div>

</v-click>

---
layout: section
---

# Prerequisites

---

# What You Need

<!--
METADATA:
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-blue-400" />
  <span class="text-lg">Active Azure subscription</span>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Static Web Apps - Introduction Welcome to this lab on Azure Static Web Apps and App Service for static content.
search_anchor: App Service for Static Web
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-command-line class="text-4xl text-green-400" />
  <span class="text-lg">Azure CLI installed and configured</span>
</div>

</v-click>

<!--
METADATA:
sentence: In this lab, we'll explore two different approaches for hosting static web content in Azure.
search_anchor: this lab, we'll explore two
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-logo-github class="text-4xl text-purple-400" />
  <span class="text-lg">GitHub account (free accounts sufficient)</span>
</div>

</v-click>

<!--
METADATA:
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-version-major class="text-4xl text-orange-400" />
  <span class="text-lg">Git installed on local machine</span>
</div>

</v-click>

---
layout: section
---

# Key Differences

---

# Static Web Apps vs App Service

<!--
METADATA:
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="mt-4 text-lg font-bold text-blue-400">Static Web Apps:</div>

</v-click>

<!--
METADATA:
sentence: Unlike traditional App Service deployments, Static Web Apps are deployed directly from a Git repository, with automated build and deployment workflows managed through GitHub Actions or Azure DevOps.
search_anchor: Unlike traditional App Service deployments
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-checkmark class="text-2xl text-green-400 mt-1" />
  <div>
    <div class="text-base">Deploy directly from Git repositories</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="mt-2 flex items-start gap-3">
  <carbon-checkmark class="text-2xl text-green-400 mt-1" />
  <div>
    <div class="text-base">Automatic build via GitHub Actions</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="mt-2 flex items-start gap-3">
  <carbon-checkmark class="text-2xl text-green-400 mt-1" />
  <div>
    <div class="text-base">Optimized for JAMstack applications</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Static Web Apps - Introduction Welcome to this lab on Azure Static Web Apps and App Service for static content.
search_anchor: App Service for Static Web
-->
<v-click>

<div class="mt-2 flex items-start gap-3">
  <carbon-checkmark class="text-2xl text-green-400 mt-1" />
  <div>
    <div class="text-base">No App Service Plan required</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="mt-2 flex items-start gap-3">
  <carbon-checkmark class="text-2xl text-green-400 mt-1" />
  <div>
    <div class="text-base">Built-in staging from pull requests</div>
  </div>
</div>

</v-click>

---

# App Service with Static Content

<!--
METADATA:
sentence: App Service for Static Web Apps - Introduction Welcome to this lab on Azure Static Web Apps and App Service for static content.
search_anchor: App Service for Static Web
-->
<v-click>

<div class="mt-4 text-lg font-bold text-purple-400">App Service:</div>

</v-click>

<!--
METADATA:
sentence: Continuous Deployment - You'll make changes to your content and see how GitHub Actions automatically deploy those changes to your live site.
search_anchor: Continuous Deployment - You'll make
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-settings class="text-2xl text-blue-400 mt-1" />
  <div>
    <div class="text-base">More control over deployment methods</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Static Web Apps - Introduction Welcome to this lab on Azure Static Web Apps and App Service for static content.
search_anchor: App Service for Static Web
-->
<v-click>

<div class="mt-2 flex items-start gap-3">
  <carbon-settings-adjust class="text-2xl text-blue-400 mt-1" />
  <div>
    <div class="text-base">Full range of App Service management options</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Static Web Apps - Introduction Welcome to this lab on Azure Static Web Apps and App Service for static content.
search_anchor: App Service for Static Web
-->
<v-click>

<div class="mt-2 flex items-start gap-3">
  <carbon-hybrid-networking class="text-2xl text-blue-400 mt-1" />
  <div>
    <div class="text-base">Mix static and dynamic content flexibly</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Static Web Apps - Introduction Welcome to this lab on Azure Static Web Apps and App Service for static content.
search_anchor: App Service for Static Web
-->
<v-click>

<div class="mt-2 flex items-start gap-3">
  <carbon-plan class="text-2xl text-blue-400 mt-1" />
  <div>
    <div class="text-base">Requires an App Service Plan</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Static Web Apps - Introduction Welcome to this lab on Azure Static Web Apps and App Service for static content.
search_anchor: App Service for Static Web
-->
<v-click>

<div class="mt-2 flex items-start gap-3">
  <carbon-application-web class="text-2xl text-blue-400 mt-1" />
  <div>
    <div class="text-base">Familiar model if already using App Service</div>
  </div>
</div>

</v-click>

---

# Continuous Deployment Flow

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Change[Make Changes] --> Commit[Commit to Repo]
    Commit --> Actions[GitHub Actions<br/>Triggered]
    Actions --> Build[Build Static Site]
    Build --> Deploy[Deploy to Azure]
    Deploy --> Live[Live Site Updated]
    style Change fill:#51cf66
    style Commit fill:#51cf66
    style Actions fill:#ffd43b
    style Build fill:#0078d4
    style Deploy fill:#0078d4
    style Live fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: Continuous Deployment - You'll make changes to your content and see how GitHub Actions automatically deploy those changes to your live site.
search_anchor: Continuous Deployment - You'll make
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Changes automatically deployed to live site
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
sentence: What are Static Web Apps?
search_anchor: What are Static Web Apps
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: In this lab, we'll explore two different approaches for hosting static web content in Azure.
search_anchor: this lab, we'll explore two
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
See these differences in action
</div>

</v-click>

</div>
