---
theme: default
background: https://images.unsplash.com/photo-1563986768494-4dee2763ff3f?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Application Gateway with WAF
  Layer 7 load balancing and security for AZ-204
drawings:
  persist: false
transition: slide-left
title: Application Gateway
mdc: true
---

# Application Gateway

Layer 7 Load Balancer with Web Application Firewall

<div class="abs-bottom-10 left-10">
  <carbon-network-4 class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Azure Application Gateway<br/>with Web Application Firewall
</div>

</v-click>

<v-click>

<div class="text-lg mt-6 opacity-70">
Traffic management and security
</div>

</v-click>

---
layout: section
---

# What is Application Gateway?

---

# Layer 7 Load Balancer

<v-click>

<div class="mt-4">
  <carbon-network-4 class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Azure's layer 7 load balancer
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Layer7[Layer 7<br/>Application Layer] --> HTTP[HTTP Routing]
    Layer4[Layer 4<br/>Network Layer] --> IP[IP Routing]
    style Layer7 fill:#51cf66
    style Layer4 fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Operates at application layer, not network layer
</div>

</v-click>

---

# Intelligent Routing

<v-click>

<div class="mt-8 text-center text-xl">
Routes traffic based on HTTP request attributes
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Request[HTTP Request] --> Check{Application Gateway}
    Check -->|domain.com| App1[App 1]
    Check -->|api.domain.com| App2[App 2]
    Check -->|domain.com/admin| App3[App 3]
    style Check fill:#0078d4
    style App1 fill:#51cf66
    style App2 fill:#51cf66
    style App3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Domain name and URL path-based routing
</div>

</v-click>

---

# Health Monitoring

<v-click>

<div class="mt-8">

```mermaid
graph TB
    AppGW[Application Gateway] -->|Monitor| Backend1[Backend 1 ✓]
    AppGW -->|Monitor| Backend2[Backend 2 ✓]
    AppGW -->|Skip| Backend3[Backend 3 ❌]
    style AppGW fill:#0078d4
    style Backend1 fill:#51cf66
    style Backend2 fill:#51cf66
    style Backend3 fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Continuously monitors backend health
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg opacity-70">
Traffic only goes to healthy instances
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg text-green-400">
High availability + Optimal performance
</div>

</v-click>

---
layout: section
---

# Web Application Firewall

---

# WAF Overview

<v-click>

<div class="mt-4">
  <carbon-security class="text-6xl text-red-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Optional but powerful security feature
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Request[HTTP Request] --> WAF[WAF Inspection]
    WAF -->|Clean| Backend[Backend]
    WAF -->|Malicious| Block[❌ Blocked]
    style WAF fill:#ff6b6b
    style Backend fill:#51cf66
    style Block fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Inspects headers and body for malicious payloads
</div>

</v-click>

---

# The Key Benefit

<v-click>

<div class="mt-12 text-center text-2xl">
Attacks prevented at WAF layer
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Attack[Attack Request] --> WAF[WAF]
    WAF -->|Blocked| Stop[❌ Stopped]
    Backend[Backend Services] -.->|Never Reached| Safe[✓ Safe]
    style Attack fill:#ff6b6b
    style WAF fill=#0078d4
    style Stop fill:#ff6b6b
    style Backend fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Critical security boundary for applications
</div>

</v-click>

---
layout: section
---

# Lab Objectives

---

# What We'll Build

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-add class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Deploy App Gateway with WAF and OWASP ruleset</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-network-4 class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Configure multi-site routing to ACI containers</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-red-400 mt-1">3</div>
  <div>
    <carbon-security class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Test WAF by simulating attack patterns</span>
  </div>
</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# Layer 7 Load Balancing

<v-click>

<div class="mt-8 text-center text-xl">
Routing decisions based on application-level data
</div>

</v-click>

<v-click>

<div class="mt-12 grid grid-cols-3 gap-6">
  <div class="text-center">
    <carbon-data-1 class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">HTTP Headers</div>
  </div>
  <div class="text-center">
    <carbon-cookie class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Cookies</div>
  </div>
  <div class="text-center">
    <carbon-url class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">URL Paths</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Much more flexible than network-level load balancing
</div>

</v-click>

---

# OWASP Ruleset

<v-click>

<div class="mt-4">
  <carbon-shield class="text-6xl text-red-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Open Web Application Security Project
</div>

</v-click>

<v-click>

<div class="mt-12 text-lg text-center">
Organization behind OWASP Top 10 security risks
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    OWASP[OWASP Ruleset] --> SQL[SQL Injection]
    OWASP --> XSS[Cross-Site Scripting]
    OWASP --> CSRF[CSRF]
    OWASP --> Other[Other Vulnerabilities]
    style OWASP fill:#ff6b6b
    style SQL fill:#0078d4
    style XSS fill:#0078d4
    style CSRF fill:#0078d4
    style Other fill:#0078d4
```

</div>

</v-click>

---

# WAF Modes

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-view class="text-5xl text-blue-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Detection Mode</div>
    <div class="text-sm mt-2 opacity-70">Logs suspicious requests</div>
    <div class="text-sm opacity-70">But allows them through</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-locked class="text-5xl text-red-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Prevention Mode</div>
    <div class="text-sm mt-2 opacity-70">Actively blocks attacks</div>
    <div class="text-sm opacity-70">Stops threats before they reach apps</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
We'll use Prevention mode
</div>

</v-click>

---
layout: section
---

# Architecture Overview

---

# What We're Building

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Internet[Internet<br/>Public IP + DNS] --> AppGW[Application Gateway<br/>+ WAF]
    AppGW --> ACI1[ACI Container 1]
    AppGW --> ACI2[ACI Container 2]
    AppGW --> ACI3[ACI Container 3]
    style Internet fill:#ffd43b
    style AppGW fill:#0078d4
    style ACI1 fill=#51cf66
    style ACI2 fill:#51cf66
    style ACI3 fill:#51cf66
```

</div>

</v-click>

---

# Traffic Flow

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-yellow-400 mt-1">1</div>
  <div>
    <carbon-network-3 class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Public IP + DNS name for client connections</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">2</div>
  <div>
    <carbon-network-4 class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Application Gateway in dedicated subnet</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-red-400 mt-1">3</div>
  <div>
    <carbon-security class="text-3xl inline-block" />
    <span class="ml-3 text-lg">WAF inspects all traffic first</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">4</div>
  <div>
    <carbon-container-software class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Routes to appropriate ACI container by domain</span>
  </div>
</div>

</v-click>

---

# Security Checkpoint

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Request[All Traffic] --> WAF[WAF<br/>Security Checkpoint]
    WAF -->|Approved| Backend[Backend Services]
    WAF -->|Blocked| Stop[❌]
    style WAF fill:#ff6b6b
    style Backend fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Security boundary before any backend service
</div>

</v-click>

---
layout: section
---

# Prerequisites

---

# What You'll Need

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-blue-400" />
  <span class="text-lg">Active Azure subscription with resource permissions</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-command-line class="text-4xl text-green-400" />
  <span class="text-lg">Azure CLI installed and authenticated</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-purple-400" />
  <span class="text-lg">Basic networking concepts (IP, DNS)</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-docker class="text-4xl text-orange-400" />
  <span class="text-lg">Docker Desktop (optional - for GoTestWAF tool)</span>
</div>

</v-click>

---
layout: section
---

# What You'll Learn

---

# Learning Outcomes

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-add class="text-3xl text-blue-400 mt-1" />
  <span>Create and configure Application Gateway with WAF</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-network-4 class="text-3xl text-green-400 mt-1" />
  <span>Set up multi-site routing to different backend pools</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-security class="text-3xl text-red-400 mt-1" />
  <span>Test and validate WAF security rules</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-search class="text-3xl text-purple-400 mt-1" />
  <span>Troubleshoot common issues (502 errors, etc.)</span>
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
Creating our Application Gateway infrastructure
</div>

</v-click>

</div>
