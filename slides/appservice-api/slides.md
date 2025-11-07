---
theme: default
background: https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## App Service for Distributed Apps
  Multi-app deployments for AZ-204
drawings:
  persist: false
transition: slide-left
title: Distributed Apps
mdc: true
---

# App Service for Distributed Apps

Deploying Multiple Applications to Shared Infrastructure

<div class="abs-bottom-10 left-10">
  <carbon-network-3 class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: In this session, we'll explore how to deploy and configure multiple applications within a single App Service Plan, demonstrating a cost-effective approach to running distributed systems in Azure.
search_anchor: this session, we'll explore how
-->
<v-click>

<div class="text-xl mt-8">
Explore distributed application deployment<br/>Cost-effective multi-app hosting in Azure
</div>

</v-click>

---
layout: section
---

# Lab Overview

---

# What You'll Learn

<!--
METADATA:
sentence: In this session, we'll explore how to deploy and configure multiple applications within a single App Service Plan, demonstrating a cost-effective approach to running distributed systems in Azure.
search_anchor: this session, we'll explore how
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-apps class="text-4xl text-blue-400" />
  <span class="text-lg">Deploy multiple apps to single App Service Plan</span>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Distributed Apps - Introduction Welcome Welcome to this lab on using Azure App Service for distributed applications.
search_anchor: App Service for Distributed Apps
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-green-400" />
  <span class="text-lg">Configure app settings for component communication</span>
</div>

</v-click>

<!--
METADATA:
sentence: Configuration Management App Service provides a centralized way to manage application configuration through environment variables and application settings.
search_anchor: Configuration Management App Service provides
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-connected class="text-4xl text-purple-400" />
  <span class="text-lg">Manage environment-specific values</span>
</div>

</v-click>

<!--
METADATA:
sentence: Key Concepts App Service Plans An App Service Plan defines the compute resources for your web apps.
search_anchor: Key Concepts App Service Plans
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-scale class="text-4xl text-orange-400" />
  <span class="text-lg">Scale App Service Plans and understand SKU limits</span>
</div>

</v-click>

<!--
METADATA:
sentence: Key Concepts App Service Plans An App Service Plan defines the compute resources for your web apps.
search_anchor: Key Concepts App Service Plans
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-red-400" />
  <span class="text-lg">Configure CORS policies for cross-origin requests</span>
</div>

</v-click>

---
layout: section
---

# Application Scenario

---

# Distributed Random Number Generator

<!--
METADATA:
sentence: Key Concepts App Service Plans An App Service Plan defines the compute resources for your web apps.
search_anchor: Key Concepts App Service Plans
-->
<v-click>

<div class="mt-8 text-center text-xl">
Three components working together
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Frontend[Web Frontend] --> API[REST API<br/>.NET 6.0]
    SPA[Static SPA] --> API
    style Frontend fill:#51cf66
    style SPA fill:#ffd43b
    style API fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: Key Concepts App Service Plans An App Service Plan defines the compute resources for your web apps.
search_anchor: Key Concepts App Service Plans
-->
<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Typical microservices architecture pattern
</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# App Service Plans

<v-click>

<div class="mt-4">
  <carbon-plan class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Key Concepts App Service Plans An App Service Plan defines the compute resources for your web apps.
search_anchor: Key Concepts App Service Plans
-->
<v-click>

<div class="mt-8 text-xl text-center">
Define compute resources for web apps
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Plan[App Service Plan<br/>Shared Resources] --> App1[API App]
    Plan --> App2[Web App]
    Plan --> App3[SPA App]
    style Plan fill:#0078d4
    style App1 fill:#51cf66
    style App2 fill:#51cf66
    style App3 fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: One plan can host multiple App Services, allowing you to optimize costs by sharing infrastructure across multiple application components.
search_anchor: One plan can host multiple
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
One plan can host multiple services
</div>

</v-click>

<!--
METADATA:
sentence: One plan can host multiple App Services, allowing you to optimize costs by sharing infrastructure across multiple application components.
search_anchor: One plan can host multiple
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Optimize costs by sharing infrastructure
</div>

</v-click>

---

# Configuration Management

<v-click>

<div class="mt-4">
  <carbon-settings-adjust class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Configuration Management App Service provides a centralized way to manage application configuration through environment variables and application settings.
search_anchor: Configuration Management App Service provides
-->
<v-click>

<div class="mt-8 text-xl text-center">
Centralized configuration through environment variables
</div>

</v-click>

<!--
METADATA:
sentence: These settings are injected into your application at runtime, making it easy to deploy the same code across different environments with different configurations.
search_anchor: These settings are injected into
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-code class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Same Code</div>
  </div>
  <div class="text-center">
    <carbon-arrow-right class="text-6xl text-gray-400" />
  </div>
  <div class="text-center">
    <carbon-earth class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Different Environments</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: These settings are injected into your application at runtime, making it easy to deploy the same code across different environments with different configurations.
search_anchor: These settings are injected into
-->
<v-click>

<div class="mt-12 text-center text-lg">
Settings injected at runtime
</div>

</v-click>

<!--
METADATA:
sentence: Configuration Management App Service provides a centralized way to manage application configuration through environment variables and application settings.
search_anchor: Configuration Management App Service provides
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Deploy once, configure per environment
</div>

</v-click>

---

# Deployment with az webapp up

<!--
METADATA:
sentence: One plan can host multiple App Services, allowing you to optimize costs by sharing infrastructure across multiple application components.
search_anchor: One plan can host multiple
-->
<v-click>

<div class="mt-8 text-center text-xl">
Convenient shortcut combining multiple steps
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Start[az webapp up] --> Create[Create App Service]
    Create --> Package[Package Application]
    Package --> Deploy[Deploy to Azure]
    style Start fill:#51cf66
    style Create fill:#0078d4
    style Package fill:#0078d4
    style Deploy fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: In this session, we'll explore how to deploy and configure multiple applications within a single App Service Plan, demonstrating a cost-effective approach to running distributed systems in Azure.
search_anchor: this session, we'll explore how
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
All in a single command
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
sentence: Configuration Management App Service provides a centralized way to manage application configuration through environment variables and application settings.
search_anchor: Configuration Management App Service provides
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-command-line class="text-4xl text-blue-400" />
  <span class="text-lg">Azure CLI installed and configured</span>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Distributed Apps - Introduction Welcome Welcome to this lab on using Azure App Service for distributed applications.
search_anchor: App Service for Distributed Apps
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-green-400" />
  <span class="text-lg">Active Azure subscription</span>
</div>

</v-click>

<!--
METADATA:
sentence: Key Concepts App Service Plans An App Service Plan defines the compute resources for your web apps.
search_anchor: Key Concepts App Service Plans
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-api class="text-4xl text-purple-400" />
  <span class="text-lg">Basic understanding of REST APIs</span>
</div>

</v-click>

<!--
METADATA:
sentence: These settings are injected into your application at runtime, making it easy to deploy the same code across different environments with different configurations.
search_anchor: These settings are injected into
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-terminal class="text-4xl text-orange-400" />
  <span class="text-lg">Familiarity with command-line tools</span>
</div>

</v-click>

---
layout: section
---

# What You'll Build

---

# The Outcome

<!--
METADATA:
sentence: App Service for Distributed Apps - Introduction Welcome Welcome to this lab on using Azure App Service for distributed applications.
search_anchor: App Service for Distributed Apps
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-api class="text-4xl text-blue-400" />
  <span class="text-lg">REST API deployed to Azure App Service</span>
</div>

</v-click>

<!--
METADATA:
sentence: These settings are injected into your application at runtime, making it easy to deploy the same code across different environments with different configurations.
search_anchor: These settings are injected into
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-application-web class="text-4xl text-green-400" />
  <span class="text-lg">Web application consuming the API</span>
</div>

</v-click>

<!--
METADATA:
sentence: One plan can host multiple App Services, allowing you to optimize costs by sharing infrastructure across multiple application components.
search_anchor: One plan can host multiple
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-purple-400" />
  <span class="text-lg">Proper configuration connecting components</span>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Distributed Apps - Introduction Welcome Welcome to this lab on using Azure App Service for distributed applications.
search_anchor: App Service for Distributed Apps
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-scale class="text-4xl text-orange-400" />
  <span class="text-lg">Understanding of App Service scaling</span>
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Distributed Apps - Introduction Welcome Welcome to this lab on using Azure App Service for distributed applications.
search_anchor: App Service for Distributed Apps
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-red-400" />
  <span class="text-lg">CORS configuration for secure API access</span>
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
sentence: Key Concepts App Service Plans An App Service Plan defines the compute resources for your web apps.
search_anchor: Key Concepts App Service Plans
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: App Service for Distributed Apps - Introduction Welcome Welcome to this lab on using Azure App Service for distributed applications.
search_anchor: App Service for Distributed Apps
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Build your distributed application on App Service
</div>

</v-click>

</div>
