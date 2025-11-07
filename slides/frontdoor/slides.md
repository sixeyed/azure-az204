---
theme: default
background: https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Front Door
  Global load balancing and CDN for AZ-204
drawings:
  persist: false
transition: slide-left
title: Front Door
mdc: true
---

# Azure Front Door

Global Load Balancing and Content Delivery

<div class="abs-bottom-10 left-10">
  <carbon-earth class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: What is Azure Front Door?
search_anchor: What is Azure Front Door
-->
<v-click>

<div class="text-xl mt-8">
Explore Azure Front Door<br/>Global access to your applications
</div>

</v-click>

---
layout: section
---

# What is Azure Front Door?

---

# Modern Cloud CDN

<v-click>

<div class="mt-4">
  <carbon-network-4 class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Azure Front Door is Microsoft's modern cloud CDN that provides fast, reliable, and secure access to your applications.
search_anchor: Azure Front Door is Microsoft's
-->
<v-click>

<div class="mt-8 text-xl text-center">
Microsoft's modern cloud CDN
</div>

</v-click>

<!--
METADATA:
sentence: Azure Front Door is Microsoft's modern cloud CDN that provides fast, reliable, and secure access to your applications.
search_anchor: Azure Front Door is Microsoft's
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-flash class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Fast</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Reliable</div>
  </div>
  <div class="text-center">
    <carbon-locked class="text-6xl text-red-400" />
    <div class="text-sm mt-3">Secure</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Think of it as Application Gateway, but with a global CDN built right in.
search_anchor: Think of it as Application
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Application Gateway with global CDN built in
</div>

</v-click>

---

# Regional vs Global

<v-click>

<div class="mt-8">

```mermaid
graph TB
    AppGW[Application Gateway] --> Region[Regional<br/>Single Region]
    FrontDoor[Front Door] --> Global[Global<br/>All Azure Regions]
    style AppGW fill:#ffd43b
    style Region fill:#ffd43b
    style FrontDoor fill:#51cf66
    style Global fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: While Application Gateway operates at the regional level, Front Door works globally across all Azure regions.
search_anchor: While Application Gateway operates at
-->
<v-click>

<div class="mt-12 text-center text-xl">
Application Gateway operates at regional level
</div>

</v-click>

<!--
METADATA:
sentence: While Application Gateway operates at the regional level, Front Door works globally across all Azure regions.
search_anchor: While Application Gateway operates at
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Front Door works globally across all regions
</div>

</v-click>

<!--
METADATA:
sentence: This means your users get routed to the nearest available backend, providing optimal performance regardless of where they're located.
search_anchor: This means your users get
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Users routed to nearest available backend
</div>

</v-click>

---
layout: section
---

# Key Features

---

# What Front Door Provides

<!--
METADATA:
sentence: Unlike regional load balancers, Front Door can distribute traffic across multiple regions, ensuring high availability and optimal performance for users worldwide.
search_anchor: Unlike regional load balancers, Front
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-earth class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Global Load Balancing</span>
    <div class="text-sm mt-2 opacity-70">Distribute traffic across multiple regions</div>
    <div class="text-sm opacity-70">High availability and optimal performance</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Static resources can be cached at edge locations around the world, reducing latency and improving user experience.
search_anchor: Static resources can be cached
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-network-2 class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Integrated CDN</span>
    <div class="text-sm mt-2 opacity-70">Cache static resources at edge locations</div>
    <div class="text-sm opacity-70">Reduce latency worldwide</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: You can protect your applications from common web vulnerabilities and exploits using the same WAF functionality available in Application Gateway.
search_anchor: You can protect your applications
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-security class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Web Application Firewall</span>
    <div class="text-sm mt-2 opacity-70">Protect from common vulnerabilities</div>
    <div class="text-sm opacity-70">Same WAF as Application Gateway</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Fourth, it provides DDoS protection, helping shield your applications from distributed denial of service attacks.
search_anchor: Fourth, it provides DDoS protection
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-warning class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">DDoS Protection</span>
    <div class="text-sm mt-2 opacity-70">Shield from distributed attacks</div>
  </div>
</div>

</v-click>

---

# Additional Capabilities

<!--
METADATA:
sentence: Finally, it offers intelligent routing based on performance, health, and weighted load balancing configurations.
search_anchor: Finally, it offers intelligent routing
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-direction-right class="text-4xl text-blue-400" />
  <span class="text-lg">Intelligent routing based on performance and health</span>
</div>

</v-click>

<!--
METADATA:
sentence: Finally, it offers intelligent routing based on performance, health, and weighted load balancing configurations.
search_anchor: Finally, it offers intelligent routing
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-scale class="text-4xl text-green-400" />
  <span class="text-lg">Weighted load balancing configurations</span>
</div>

</v-click>

<!--
METADATA:
sentence: In this session, we'll explore one of Azure's most powerful global load balancing and content delivery solutions.
search_anchor: this session, we'll explore one
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-purple-400" />
  <span class="text-lg">SSL offloading and certificate management</span>
</div>

</v-click>

<!--
METADATA:
sentence: Second, it includes integrated CDN capabilities.
search_anchor: Second, it includes integrated CDN
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-connected class="text-4xl text-orange-400" />
  <span class="text-lg">Session affinity for stateful applications</span>
</div>

</v-click>

<!--
METADATA:
sentence: Finally, it offers intelligent routing based on performance, health, and weighted load balancing configurations.
search_anchor: Finally, it offers intelligent routing
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-flow class="text-4xl text-red-400" />
  <span class="text-lg">Advanced routing based on URL paths or headers</span>
</div>

</v-click>

---
layout: section
---

# Evolution of Azure Services

---

# Bringing It All Together

<v-click>

<div class="mt-8">

```mermaid
graph TB
    TM[Traffic Manager] --> FD[Front Door]
    CDN[Content Delivery Network] --> FD
    AppGW[Application Gateway] --> FD
    style TM fill:#ffd43b
    style CDN fill:#ffd43b
    style AppGW fill:#ffd43b
    style FD fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: It combines the best features of Traffic Manager, Content Delivery Network, and Application Gateway into a single, comprehensive solution.
search_anchor: It combines the best features
-->
<v-click>

<div class="mt-12 text-center text-xl">
Combines best features of multiple services
</div>

</v-click>

<!--
METADATA:
sentence: It combines the best features of Traffic Manager, Content Delivery Network, and Application Gateway into a single, comprehensive solution.
search_anchor: It combines the best features
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Single, comprehensive solution
</div>

</v-click>

---

# Microsoft's Recommendation

<v-click>

<div class="mt-4">
  <carbon-favorite class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Front Door?
search_anchor: What is Azure Front Door
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Front Door is now the preferred option
</div>

</v-click>

<!--
METADATA:
sentence: Microsoft now recommends Front Door as the preferred option for the frontend to your HTTP services.
search_anchor: Microsoft now recommends Front Door
-->
<v-click>

<div class="mt-12 text-center text-lg">
For frontend to your HTTP services
</div>

</v-click>

<!--
METADATA:
sentence: This includes Web Apps, API Management domains, and any other HTTP-based applications you want to expose to users.
search_anchor: This includes Web Apps, API
-->
<v-click>

<div class="mt-8 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-application-web class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Web Apps</div>
  </div>
  <div class="text-center">
    <carbon-api class="text-5xl text-green-400" />
    <div class="text-sm mt-3">API Management</div>
  </div>
  <div class="text-center">
    <carbon-network-3 class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">HTTP Applications</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Use Cases

---

# When to Use Front Door

<!--
METADATA:
sentence: Unlike regional load balancers, Front Door can distribute traffic across multiple regions, ensuring high availability and optimal performance for users worldwide.
search_anchor: Unlike regional load balancers, Front
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-earth class="text-4xl text-blue-400" />
  <span class="text-lg">Global load balancing across multiple regions</span>
</div>

</v-click>

<!--
METADATA:
sentence: Second, it includes integrated CDN capabilities.
search_anchor: Second, it includes integrated CDN
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-2 class="text-4xl text-green-400" />
  <span class="text-lg">CDN capabilities for static content</span>
</div>

</v-click>

<!--
METADATA:
sentence: Third, it supports Web Application Firewall integration.
search_anchor: Third, it supports Web Application
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-purple-400" />
  <span class="text-lg">Web application firewall protection</span>
</div>

</v-click>

<!--
METADATA:
sentence: In this session, we'll explore one of Azure's most powerful global load balancing and content delivery solutions.
search_anchor: this session, we'll explore one
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-orange-400" />
  <span class="text-lg">SSL offloading and certificate management</span>
</div>

</v-click>

<!--
METADATA:
sentence: Finally, it offers intelligent routing based on performance, health, and weighted load balancing configurations.
search_anchor: Finally, it offers intelligent routing
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-flow class="text-4xl text-red-400" />
  <span class="text-lg">Advanced routing based on URL paths or headers</span>
</div>

</v-click>

<!--
METADATA:
sentence: Second, it includes integrated CDN capabilities.
search_anchor: Second, it includes integrated CDN
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-connected class="text-4xl text-blue-500" />
  <span class="text-lg">Session affinity for stateful applications</span>
</div>

</v-click>

---
layout: section
---

# Lab Overview

---

# What We'll Build

<!--
METADATA:
sentence: What is Azure Front Door?
search_anchor: What is Azure Front Door
-->
<v-click>

<div class="mt-8 text-center text-xl">
Create and configure Azure Front Door with WAF
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Users[Users Worldwide] --> FD[Front Door + WAF]
    FD --> Region1[Backend<br/>Region 1]
    FD --> Region2[Backend<br/>Region 2]
    style Users fill:#51cf66
    style FD fill:#0078d4
    style Region1 fill:#ffd43b
    style Region2 fill:#ffd43b
```

</div>

</v-click>

<!--
METADATA:
sentence: We'll deploy backend applications in multiple regions, configure Front Door to route traffic between them, and apply security policies to protect against common threats.
search_anchor: We'll deploy backend applications in
-->
<v-click>

<div class="mt-12 text-center text-xl">
Deploy backends in multiple regions
</div>

</v-click>

<!--
METADATA:
sentence: We'll deploy backend applications in multiple regions, configure Front Door to route traffic between them, and apply security policies to protect against common threats.
search_anchor: We'll deploy backend applications in
-->
<v-click>

<div class="mt-4 text-center text-xl">
Configure traffic routing and security policies
</div>

</v-click>

---

# Learning Outcomes

<!--
METADATA:
sentence: By the end of this lab, you'll understand how to architect and implement a globally distributed application using Azure Front Door.
search_anchor: By the end of this
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-diagram class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Architect</div>
  </div>
  <div class="text-center">
    <carbon-deployment-pattern class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Implement</div>
  </div>
  <div class="text-center">
    <carbon-earth class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Globally Distributed</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: What is Azure Front Door?
search_anchor: What is Azure Front Door
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Using Azure Front Door
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
sentence: What is Azure Front Door?
search_anchor: What is Azure Front Door
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: By the end of this lab, you'll understand how to architect and implement a globally distributed application using Azure Front Door.
search_anchor: By the end of this
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Build a globally distributed application
</div>

</v-click>

</div>
