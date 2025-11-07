---
theme: default
background: https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes Services
  Networking made simple for AZ-204
drawings:
  persist: false
transition: slide-left
title: Services
mdc: true
---

# Kubernetes Services

Networking Made Simple

<div class="abs-bottom-10 left-10">
  <carbon-network-3 class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Kubernetes Services<br/>Essential for networking and service discovery
</div>

</v-click>

---
layout: section
---

# The Problem - Pod IP Addresses

---

# Dynamic Addresses Challenge

<v-click>

<div class="mt-4">
  <carbon-warning class="text-6xl text-red-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Every Pod gets its own IP address
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Sounds great, right?
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-red-400">
But... IP only exists for Pod lifetime
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Pod1[Pod<br/>IP: 10.1.2.3] --> Crash[Crashes]
    Crash --> New[New Pod<br/>IP: 10.1.2.9]
    style Pod1 fill:#51cf66
    style Crash fill:#ff6b6b
    style New fill:#51cf66
```

</div>

</v-click>

---

# Constantly Changing

<v-click>

<div class="mt-12 text-center text-xl">
Pod crashes and gets replaced
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Application scales up or down
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
IP addresses change
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
How do other parts reliably communicate?
</div>

</v-click>

---
layout: section
---

# What is a Kubernetes Service?

---

# Networking Abstraction

<v-click>

<div class="mt-4">
  <carbon-network-3 class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Stable IP address and DNS name
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
For accessing a group of Pods
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Service[Service<br/>Stable IP + DNS] --> Pod1[Pod 1]
    Service --> Pod2[Pod 2]
    Service --> Pod3[Pod 3]
    style Service fill:#51cf66
    style Pod1 fill:#0078d4
    style Pod2 fill:#0078d4
    style Pod3 fill:#0078d4
```

</div>

</v-click>

---

# Load Balancer with Service Discovery

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-network-overlay class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Load Balancing</div>
  </div>
  <div class="text-center">
    <carbon-search class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Service Discovery</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Uses label selectors to find target Pods
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Loose coupling
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Replace, scale, or update Pods without breaking connectivity
</div>

</v-click>

---
layout: section
---

# Service Type - ClusterIP

---

# Internal Communication

<v-click>

<div class="mt-4">
  <carbon-network-3 class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
ClusterIP: Default service type
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
IP address only accessible within cluster
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Frontend[Frontend Pods] --> Service[ClusterIP Service]
    Service --> Backend1[Backend Pod 1]
    Service --> Backend2[Backend Pod 2]
    Service --> Backend3[Backend Pod 3]
    style Frontend fill:#ffd43b
    style Service fill:#51cf66
    style Backend1 fill:#0078d4
    style Backend2 fill:#0078d4
    style Backend3 fill:#0078d4
```

</div>

</v-click>

---

# Perfect for Microservices

<v-click>

<div class="mt-12 text-center text-xl">
Frontend communicates with backend API
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Regardless of how many backend Pods
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Or when they get replaced
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Reliable</div>
  </div>
  <div class="text-center">
    <carbon-renew class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Resilient</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Service Type - NodePort

---

# Static Port on Nodes

<v-click>

<div class="mt-4">
  <carbon-server class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Exposes application on static port on each node
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Typically port range 30000-32767
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Traffic[External Traffic] --> Node1[Node 1:30123]
    Traffic --> Node2[Node 2:30123]
    Traffic --> Node3[Node 3:30123]
    Node1 --> Service[Service]
    Node2 --> Service
    Node3 --> Service
    Service --> Pods[Pods]
    style Traffic fill:#ffd43b
    style Service fill:#51cf66
    style Pods fill:#0078d4
```

</div>

</v-click>

---

# Use Cases

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-development class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Development</div>
  </div>
  <div class="text-center">
    <carbon-test-tool class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Testing</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Direct access without cloud load balancer
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Traffic to any node routes to Pods
</div>

</v-click>

---
layout: section
---

# Service Type - LoadBalancer

---

# Production External Access

<v-click>

<div class="mt-4">
  <carbon-cloud-services class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
What you'll typically use in production on AKS
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Internet[Internet] --> Azure[Azure Load Balancer<br/>Auto-Provisioned]
    Azure --> Service[LoadBalancer Service]
    Service --> Pod1[Pod 1]
    Service --> Pod2[Pod 2]
    Service --> Pod3[Pod 3]
    style Internet fill:#ffd43b
    style Azure fill:#51cf66
    style Service fill:#51cf66
    style Pod1 fill:#0078d4
    style Pod2 fill:#0078d4
    style Pod3 fill:#0078d4
```

</div>

</v-click>

---

# Azure Integration

<v-click>

<div class="mt-12 text-center text-xl">
Azure automatically provisions Azure Load Balancer
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Public IP address
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Distributes traffic across your Pods
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Most straightforward way to expose to internet
</div>

</v-click>

---
layout: section
---

# Service Discovery with DNS

---

# Automatic DNS Entries

<v-click>

<div class="mt-4">
  <carbon-earth class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Every Service gets DNS entry automatically
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
In cluster's internal DNS server
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Pod[Pod] -->|"my-api"| DNS[Cluster DNS]
    DNS -->|Resolves| Service[Service IP]
    Service --> Target[Target Pods]
    style Pod fill:#ffd43b
    style DNS fill:#51cf66
    style Service fill:#51cf66
    style Target fill:#0078d4
```

</div>

</v-click>

---

# Friendly Names

<v-click>

<div class="mt-12 text-center text-xl">
Communicate using DNS names, not IP addresses
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Service named "my-api"
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Any Pod in same namespace can reach it using that name
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Kubernetes handles all DNS resolution and routing
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Simple</div>
  </div>
  <div class="text-center">
    <carbon-rocket class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Powerful</div>
  </div>
</div>

</v-click>

---
layout: section
---

# AZ-204 Exam Relevance

---

# Key Exam Topics

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-blue-400" />
  <span class="text-lg">Configure networking for containerized apps in AKS</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-decision-tree class="text-4xl text-green-400" />
  <span class="text-lg">Differences between Service types</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-earth class="text-4xl text-purple-400" />
  <span class="text-lg">Service discovery with DNS</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-orange-400" />
  <span class="text-lg">Integration with Azure Load Balancer</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-tag class="text-4xl text-red-400" />
  <span class="text-lg">Label selectors and traffic routing</span>
</div>

</v-click>

---

# Exam Scenarios

<v-click>

<div class="mt-12 text-center text-xl">
Frequently appear in exam questions about
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-deployment-pattern class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Deploying</div>
  </div>
  <div class="text-center">
    <carbon-settings-adjust class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Managing</div>
  </div>
  <div class="text-center">
    <carbon-container-software class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Containerized Solutions</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What's Next

---

# Hands-On Lab

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create all three Service types</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-earth class="text-4xl text-green-400" />
  <span class="text-lg">Explore DNS resolution</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-overlay class="text-4xl text-purple-400" />
  <span class="text-lg">See traffic routing in real-time</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-4xl text-orange-400" />
  <span class="text-lg">Test scenarios: Pod failures and scaling</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Practical experience for real-world scenarios
</div>

</v-click>

---

# Summary

<v-click>

<div class="mt-8 text-center text-xl">
Services provide stable networking endpoints
</div>

</v-click>

<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <carbon-network-3 class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">ClusterIP</div>
    <div class="text-xs mt-2 opacity-70">Internal</div>
  </div>
  <div class="text-center">
    <carbon-server class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">NodePort</div>
    <div class="text-xs mt-2 opacity-70">Direct access</div>
  </div>
  <div class="text-center">
    <carbon-cloud-services class="text-5xl text-green-400" />
    <div class="text-sm mt-3">LoadBalancer</div>
    <div class="text-xs mt-2 opacity-70">Production</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Automatic service discovery through DNS
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Resilient and scalable applications
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
Let's Get Building!
</div>

</v-click>

<v-click>

<div class="text-xl mt-6 opacity-70">
Master Kubernetes networking
</div>

</v-click>

</div>
