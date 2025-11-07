---
theme: default
background: https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## App Service Configuration
  Health monitoring and auto-healing for AZ-204
drawings:
  persist: false
transition: slide-left
title: Configuration & Admin
mdc: true
---

# App Service Configuration

Enterprise-Grade Platform Features

<div class="abs-bottom-10 left-10">
  <carbon-settings-adjust class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: What You'll Learn App Service gives you enterprise-grade capabilities out of the box.
search_anchor: What You'll Learn App Service
-->
<v-click>

<div class="text-xl mt-8">
Explore App Service configuration and administration<br/>Enterprise capabilities out of the box
</div>

</v-click>

---
layout: section
---

# PaaS vs IaaS Management

---

# The PaaS Advantage

<!--
METADATA:
sentence: In this session, we'll explore how Azure App Service provides powerful platform-as-a-service features that would require significant effort to implement in an infrastructure-as-a-service deployment.
search_anchor: this session, we'll explore how
-->
<v-click>

<div class="mt-8 text-center text-xl">
App Service provides features that require significant effort in IaaS
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    IaaS[IaaS Deployment] -->|Manual| Config1[Config Files]
    IaaS -->|Manual| Health1[Health Monitoring]
    IaaS -->|Manual| Scale1[Scaling Setup]
    PaaS[App Service PaaS] -->|Built-in| Config2[App Settings]
    PaaS -->|Built-in| Health2[Health Checks]
    PaaS -->|Built-in| Scale2[Auto-Healing]
    style IaaS fill:#ff6b6b
    style PaaS fill:#51cf66
    style Config2 fill:#0078d4
    style Health2 fill:#0078d4
    style Scale2 fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: And finally, configuring auto-heal capabilities to automatically restart failed instances without manual intervention.
search_anchor: finally, configuring auto-heal capabilities to
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
No server logins or manual file editing
</div>

</v-click>

---
layout: section
---

# Configuration Management

---

# Environment-Specific Settings

<v-click>

<div class="mt-4">
  <carbon-settings class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: They're perfect for managing settings across different environments without changing your code.
search_anchor: They're perfect for managing settings
-->
<v-click>

<div class="mt-8 text-xl text-center">
Different settings for different environments
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Settings[App Settings] --> Dev[Dev Environment]
    Settings --> Test[Test Environment]
    Settings --> Prod[Production]
    style Settings fill:#0078d4
    style Dev fill:#51cf66
    style Test fill:#ffd43b
    style Prod fill:#ff6b6b
```

</div>

</v-click>

<!--
METADATA:
sentence: You'll learn how to configure health endpoints and have Azure automatically monitor your application's health.
search_anchor: You'll learn how to configure
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Managed through Azure portal or CLI
</div>

</v-click>

<!--
METADATA:
sentence: They're perfect for managing settings across different environments without changing your code.
search_anchor: They're perfect for managing settings
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
No code changes required
</div>

</v-click>

---
layout: section
---

# Lab Overview

---

# Deliberate Failure Scenario

<!--
METADATA:
sentence: Lab Overview In this lab, we'll work with a REST API - a random number generator service.
search_anchor: Lab Overview In this lab
-->
<v-click>

<div class="mt-8 text-center text-xl">
Random number generator REST API
</div>

</v-click>

<!--
METADATA:
sentence: We're going to deliberately configure it to fail, and then we'll use App Service features to handle those failures gracefully.
search_anchor: We're going to deliberately configure
-->
<v-click>

<div class="mt-12 text-center text-lg">
Configure it to fail, then handle gracefully
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Start[Healthy API] --> Requests[Handle Requests]
    Requests -->|After N requests| Fail[Unhealthy State]
    Fail --> Detect[Health Check Detects]
    Detect --> Action[Auto-Heal Takes Action]
    Action --> Start
    style Start fill:#51cf66
    style Requests fill:#0078d4
    style Fail fill:#ff6b6b
    style Detect fill:#ffd43b
    style Action fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: This simulates real-world scenarios where applications can enter an unhealthy state.
search_anchor: This simulates real-world scenarios where
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Simulates real-world failure scenarios
</div>

</v-click>

---

# What We'll Cover

<!--
METADATA:
sentence: Second, implementing App Service health checks.
search_anchor: Second, implementing App Service health
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-settings class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Deploy app with failure-inducing settings</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Second, implementing App Service health checks.
search_anchor: Second, implementing App Service health
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-health-cross class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Implement App Service health checks</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Third, scaling your application to multiple instances.
search_anchor: Third, scaling your application to
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-scale class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Scale to multiple instances</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: And finally, configuring auto-heal capabilities to automatically restart failed instances without manual intervention.
search_anchor: finally, configuring auto-heal capabilities to
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-restart class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Configure auto-heal capabilities</span>
  </div>
</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# App Settings

<v-click>

<div class="mt-4">
  <carbon-parameter class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Key Concepts The main concepts we'll explore are: App Settings - These are environment variables that override your application's default configuration.
search_anchor: Key Concepts The main concepts
-->
<v-click>

<div class="mt-8 text-xl text-center">
Environment variables that override defaults
</div>

</v-click>

<!--
METADATA:
sentence: They're perfect for managing settings across different environments without changing your code.
search_anchor: They're perfect for managing settings
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-code class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Application Code</div>
    <div class="text-xs mt-2 opacity-70">Default values</div>
  </div>
  <div class="text-center">
    <carbon-settings class="text-6xl text-green-400" />
    <div class="text-sm mt-3">App Settings</div>
    <div class="text-xs mt-2 opacity-70">Runtime overrides</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: They're perfect for managing settings across different environments without changing your code.
search_anchor: They're perfect for managing settings
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Perfect for managing environments
</div>

</v-click>

<!--
METADATA:
sentence: They're perfect for managing settings across different environments without changing your code.
search_anchor: They're perfect for managing settings
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
No code changes needed
</div>

</v-click>

---

# Health Checks

<v-click>

<div class="mt-4">
  <carbon-health-cross class="text-6xl text-red-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Health Checks - These are endpoints in your application that return the health status.
search_anchor: Health Checks - These are
-->
<v-click>

<div class="mt-8 text-xl text-center">
Endpoints that return health status
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Azure[Azure Monitor] -->|Poll| Health[/health Endpoint]
    Health -->|200 OK| Healthy[✓ Healthy]
    Health -->|500 Error| Unhealthy[❌ Unhealthy]
    Unhealthy --> Action[Take Action]
    style Azure fill:#0078d4
    style Health fill:#ffd43b
    style Healthy fill:#51cf66
    style Unhealthy fill:#ff6b6b
    style Action fill:#ff6b6b
```

</div>

</v-click>

<!--
METADATA:
sentence: App Service can poll these endpoints and take action when they return error codes.
search_anchor: App Service can poll these
-->
<v-click>

<div class="mt-8 text-center text-lg">
App Service polls and takes action on errors
</div>

</v-click>

---

# Auto-Healing

<v-click>

<div class="mt-4">
  <carbon-restart class="text-6xl text-orange-400" />
</div>

</v-click>

<!--
METADATA:
sentence: And finally, configuring auto-heal capabilities to automatically restart failed instances without manual intervention.
search_anchor: finally, configuring auto-heal capabilities to
-->
<v-click>

<div class="mt-8 text-xl text-center">
Automatically restart failed instances
</div>

</v-click>

<!--
METADATA:
sentence: Auto-Healing - This feature automatically restarts application instances based on rules you define, such as HTTP errors, slow responses, or memory thresholds.
search_anchor: Auto-Healing - This feature automatically
-->
<v-click>

<div class="mt-12 text-center text-lg">
Based on rules you define:
</div>

</v-click>

<!--
METADATA:
sentence: Auto-Healing - This feature automatically restarts application instances based on rules you define, such as HTTP errors, slow responses, or memory thresholds.
search_anchor: Auto-Healing - This feature automatically
-->
<v-click>

<div class="mt-8 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-warning class="text-5xl text-red-400" />
    <div class="text-sm mt-3">HTTP Errors</div>
  </div>
  <div class="text-center">
    <carbon-time class="text-5xl text-orange-400" />
    <div class="text-sm mt-3">Slow Responses</div>
  </div>
  <div class="text-center">
    <carbon-data-base class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Memory Thresholds</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: And finally, configuring auto-heal capabilities to automatically restart failed instances without manual intervention.
search_anchor: finally, configuring auto-heal capabilities to
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
No manual intervention required
</div>

</v-click>

---

# Instance Management

<v-click>

<div class="mt-4">
  <carbon-network-4 class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Third, scaling your application to multiple instances.
search_anchor: Third, scaling your application to
-->
<v-click>

<div class="mt-8 text-xl text-center">
Multiple instances with load balancing
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    LB[Load Balancer] --> I1[Instance 1<br/>✓ Healthy]
    LB --> I2[Instance 2<br/>❌ Unhealthy]
    LB --> I3[Instance 3<br/>✓ Healthy]
    I1 --> Traffic1[Receives Traffic]
    I2 -.->|No Traffic| NoTraffic[Isolated]
    I3 --> Traffic2[Receives Traffic]
    style LB fill:#0078d4
    style I1 fill:#51cf66
    style I2 fill:#ff6b6b
    style I3 fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Third, scaling your application to multiple instances.
search_anchor: Third, scaling your application to
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Traffic routed only to healthy instances
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
sentence: Let's get started and see these features in action.
search_anchor: Let's get started and see
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: Let's get started and see these features in action.
search_anchor: Let's get started and see
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
See health monitoring and auto-healing in action
</div>

</v-click>

</div>
