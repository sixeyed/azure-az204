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

<!--
METADATA:
sentence: Let's explore how Kubernetes handles networking and service discovery.
search_anchor: Let's explore how Kubernetes handles
-->
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

<!--
METADATA:
sentence: That IP address only exists for the lifetime of the Pod.
search_anchor: That IP address only exists
-->
<v-click>

<div class="mt-8 text-xl text-center">
Every Pod gets its own IP address
</div>

</v-click>

<!--
METADATA:
sentence: First up is ClusterIP, which is the default type.
search_anchor: First up is ClusterIP, which
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Sounds great, right?
</div>

</v-click>

<!--
METADATA:
sentence: That IP address only exists for the lifetime of the Pod.
search_anchor: That IP address only exists
-->
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

<!--
METADATA:
sentence: When a Pod crashes and gets replaced, or when you scale your application, those IP addresses change.
search_anchor: When a Pod crashes and
-->
<v-click>

<div class="mt-12 text-center text-xl">
Pod crashes and gets replaced
</div>

</v-click>

<!--
METADATA:
sentence: When a Pod crashes and gets replaced, or when you scale your application, those IP addresses change.
search_anchor: When a Pod crashes and
-->
<v-click>

<div class="mt-8 text-center text-xl">
Application scales up or down
</div>

</v-click>

<!--
METADATA:
sentence: When a Pod crashes and gets replaced, or when you scale your application, those IP addresses change.
search_anchor: When a Pod crashes and
-->
<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
IP addresses change
</div>

</v-click>

<!--
METADATA:
sentence: So how do other parts of your application reliably communicate with these constantly changing Pods?
search_anchor: So how do other parts
-->
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

<!--
METADATA:
sentence: That IP address only exists for the lifetime of the Pod.
search_anchor: That IP address only exists
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Stable IP address and DNS name
</div>

</v-click>

<!--
METADATA:
sentence: This means your Pods can communicate using friendly DNS names instead of IP addresses.
search_anchor: This means your Pods can
-->
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

<!--
METADATA:
sentence: Think of it as a load balancer with built-in service discovery.
search_anchor: Think of it as a
-->
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

<!--
METADATA:
sentence: Services use label selectors to find their target Pods.
search_anchor: Services use label selectors to
-->
<v-click>

<div class="mt-12 text-center text-xl">
Uses label selectors to find target Pods
</div>

</v-click>

<!--
METADATA:
sentence: Alright, let's get building!
search_anchor: Alright, let's get building
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Loose coupling
</div>

</v-click>

<!--
METADATA:
sentence: This loose coupling means you can replace, scale, or update Pods without breaking connectivity.
search_anchor: This loose coupling means you
-->
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

<!--
METADATA:
sentence: First up is ClusterIP, which is the default type.
search_anchor: First up is ClusterIP, which
-->
<v-click>

<div class="mt-8 text-xl text-center">
ClusterIP: Default service type
</div>

</v-click>

<!--
METADATA:
sentence: ClusterIP Services get an IP address that's only accessible within the cluster.
search_anchor: ClusterIP Services get an IP
-->
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

<!--
METADATA:
sentence: For example, your frontend Pods can reliably communicate with your backend API using a ClusterIP Service, regardless of how many backend Pods are running or when they get replaced.
search_anchor: example, your frontend Pods can
-->
<v-click>

<div class="mt-12 text-center text-xl">
Frontend communicates with backend API
</div>

</v-click>

<!--
METADATA:
sentence: For example, your frontend Pods can reliably communicate with your backend API using a ClusterIP Service, regardless of how many backend Pods are running or when they get replaced.
search_anchor: example, your frontend Pods can
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Regardless of how many backend Pods
</div>

</v-click>

<!--
METADATA:
sentence: Alright, let's get building!
search_anchor: Alright, let's get building
-->
<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Or when they get replaced
</div>

</v-click>

<!--
METADATA:
sentence: Alright, let's get building!
search_anchor: Alright, let's get building
-->
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

<!--
METADATA:
sentence: This Service type exposes your application on a static port on each node in your cluster, typically in the range 30000 to 32767.
search_anchor: This Service type exposes your
-->
<v-click>

<div class="mt-8 text-xl text-center">
Exposes application on static port on each node
</div>

</v-click>

<!--
METADATA:
sentence: This Service type exposes your application on a static port on each node in your cluster, typically in the range 30000 to 32767.
search_anchor: This Service type exposes your
-->
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

<!--
METADATA:
sentence: Alright, let's get building!
search_anchor: Alright, let's get building
-->
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

<!--
METADATA:
sentence: NodePort is useful for development and testing, or when you need direct access to your cluster without a cloud load balancer.
search_anchor: NodePort is useful for development
-->
<v-click>

<div class="mt-12 text-center text-xl">
Direct access without cloud load balancer
</div>

</v-click>

<!--
METADATA:
sentence: Any traffic hitting any node's IP address on that specific port gets routed to your Pods.
search_anchor: Any traffic hitting any node's
-->
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

<!--
METADATA:
sentence: When you create a LoadBalancer Service on AKS, Azure automatically provisions an Azure Load Balancer for you.
search_anchor: When you create a LoadBalancer
-->
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

<!--
METADATA:
sentence: When you create a LoadBalancer Service on AKS, Azure automatically provisions an Azure Load Balancer for you.
search_anchor: When you create a LoadBalancer
-->
<v-click>

<div class="mt-12 text-center text-xl">
Azure automatically provisions Azure Load Balancer
</div>

</v-click>

<!--
METADATA:
sentence: This gives you a public IP address that distributes traffic across your Pods.
search_anchor: This gives you a public
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Public IP address
</div>

</v-click>

<!--
METADATA:
sentence: This gives you a public IP address that distributes traffic across your Pods.
search_anchor: This gives you a public
-->
<v-click>

<div class="mt-8 text-center text-xl">
Distributes traffic across your Pods
</div>

</v-click>

<!--
METADATA:
sentence: It's the most straightforward way to expose applications to the internet on managed Kubernetes platforms.
search_anchor: It's the most straightforward way
-->
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

<!--
METADATA:
sentence: Every Service automatically gets a DNS entry in the cluster's internal DNS server.
search_anchor: Every Service automatically gets a
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Every Service gets DNS entry automatically
</div>

</v-click>

<!--
METADATA:
sentence: Every Service automatically gets a DNS entry in the cluster's internal DNS server.
search_anchor: Every Service automatically gets a
-->
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

<!--
METADATA:
sentence: This means your Pods can communicate using friendly DNS names instead of IP addresses.
search_anchor: This means your Pods can
-->
<v-click>

<div class="mt-12 text-center text-xl">
Communicate using DNS names, not IP addresses
</div>

</v-click>

<!--
METADATA:
sentence: When you create a Service named "my-api," any Pod in the same namespace can reach it using that name.
search_anchor: When you create a Service
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Service named "my-api"
</div>

</v-click>

<!--
METADATA:
sentence: When you create a Service named "my-api," any Pod in the same namespace can reach it using that name.
search_anchor: When you create a Service
-->
<v-click>

<div class="mt-8 text-center text-xl">
Any Pod in same namespace can reach it using that name
</div>

</v-click>

<!--
METADATA:
sentence: Kubernetes handles all the DNS resolution and routing behind the scenes.
search_anchor: Kubernetes handles all the DNS
-->
<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Kubernetes handles all DNS resolution and routing
</div>

</v-click>

<!--
METADATA:
sentence: Alright, let's get building!
search_anchor: Alright, let's get building
-->
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

<!--
METADATA:
sentence: Let's explore how Kubernetes handles networking and service discovery.
search_anchor: Let's explore how Kubernetes handles
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-blue-400" />
  <span class="text-lg">Configure networking for containerized apps in AKS</span>
</div>

</v-click>

<!--
METADATA:
sentence: This is perfect for internal communication between microservices.
search_anchor: This is perfect for internal
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-decision-tree class="text-4xl text-green-400" />
  <span class="text-lg">Differences between Service types</span>
</div>

</v-click>

<!--
METADATA:
sentence: Think of it as a load balancer with built-in service discovery.
search_anchor: Think of it as a
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-earth class="text-4xl text-purple-400" />
  <span class="text-lg">Service discovery with DNS</span>
</div>

</v-click>

<!--
METADATA:
sentence: Think of it as a load balancer with built-in service discovery.
search_anchor: Think of it as a
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-orange-400" />
  <span class="text-lg">Integration with Azure Load Balancer</span>
</div>

</v-click>

<!--
METADATA:
sentence: Services use label selectors to find their target Pods.
search_anchor: Services use label selectors to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-tag class="text-4xl text-red-400" />
  <span class="text-lg">Label selectors and traffic routing</span>
</div>

</v-click>

---

# Exam Scenarios

<!--
METADATA:
sentence: Every Service automatically gets a DNS entry in the cluster's internal DNS server.
search_anchor: Every Service automatically gets a
-->
<v-click>

<div class="mt-12 text-center text-xl">
Frequently appear in exam questions about
</div>

</v-click>

<!--
METADATA:
sentence: Today we're diving into one of the most essential concepts in Kubernetes: Services.
search_anchor: Today we're diving into one
-->
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

<!--
METADATA:
sentence: --- SLIDE 3: What is a Kubernetes Service?
search_anchor: --- SLIDE 3: What is
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create all three Service types</span>
</div>

</v-click>

<!--
METADATA:
sentence: Kubernetes handles all the DNS resolution and routing behind the scenes.
search_anchor: Kubernetes handles all the DNS
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-earth class="text-4xl text-green-400" />
  <span class="text-lg">Explore DNS resolution</span>
</div>

</v-click>

<!--
METADATA:
sentence: In our lab exercises, we'll create all three types of Services, explore DNS resolution, and see how traffic routing works in real-time.
search_anchor: our lab exercises, we'll create
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-overlay class="text-4xl text-purple-400" />
  <span class="text-lg">See traffic routing in real-time</span>
</div>

</v-click>

<!--
METADATA:
sentence: You'll deploy Pods, create Services with different configurations, and test scenarios like Pod failures and scaling.
search_anchor: You'll deploy Pods, create Services
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-4xl text-orange-400" />
  <span class="text-lg">Test scenarios: Pod failures and scaling</span>
</div>

</v-click>

<!--
METADATA:
sentence: This practical experience will solidify your understanding and prepare you for real-world scenarios.
search_anchor: This practical experience will solidify
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Practical experience for real-world scenarios
</div>

</v-click>

---

# Summary

<!--
METADATA:
sentence: --- SLIDE 10: Summary [On screen: Key takeaways bullet points] Quick recap: Kubernetes Services provide stable networking endpoints for dynamic Pods.
search_anchor: --- SLIDE 10: Summary [On
-->
<v-click>

<div class="mt-8 text-center text-xl">
Services provide stable networking endpoints
</div>

</v-click>

<!--
METADATA:
sentence: ClusterIP for internal communication, NodePort for direct access, and LoadBalancer for production external access.
search_anchor: ClusterIP for internal communication, NodePort
-->
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

<!--
METADATA:
sentence: Service discovery happens automatically through DNS, making your applications resilient and scalable.
search_anchor: Service discovery happens automatically through
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Automatic service discovery through DNS
</div>

</v-click>

<!--
METADATA:
sentence: Service discovery happens automatically through DNS, making your applications resilient and scalable.
search_anchor: Service discovery happens automatically through
-->
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

<!--
METADATA:
sentence: Alright, let's get building!
search_anchor: Alright, let's get building
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Building!
</div>

</v-click>

<!--
METADATA:
sentence: Let's explore how Kubernetes handles networking and service discovery.
search_anchor: Let's explore how Kubernetes handles
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Master Kubernetes networking
</div>

</v-click>

</div>
