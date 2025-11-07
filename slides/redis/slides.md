---
theme: default
background: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Cache for Redis
  Caching and messaging for AZ-204
drawings:
  persist: false
transition: slide-left
title: Redis Cache
mdc: true
---

# Azure Cache for Redis

Performance Through Caching and Messaging

<div class="abs-bottom-10 left-10">
  <carbon-flash class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: Azure Cache for Redis - Introduction What is Redis?
search_anchor: Azure Cache for Redis -
-->
<v-click>

<div class="text-xl mt-8">
Explore Azure Cache for Redis<br/>Boost performance with caching and messaging
</div>

</v-click>

---
layout: section
---

# What is Redis?

---

# Popular Open-Source Technology

<v-click>

<div class="mt-4">
  <carbon-data-base class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Redis is a popular open-source technology that combines the functionality of a message queue and a data store.
search_anchor: Redis is a popular open-source
-->
<v-click>

<div class="mt-8 text-xl text-center">
Combines message queue and data store
</div>

</v-click>

<!--
METADATA:
sentence: It's incredibly lightweight and has a straightforward programming interface, making it a go-to choice for developers worldwide.
search_anchor: It's incredibly lightweight and has
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-flash class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Lightweight</div>
  </div>
  <div class="text-center">
    <carbon-code class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Simple API</div>
  </div>
  <div class="text-center">
    <carbon-earth class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Worldwide</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: It's incredibly lightweight and has a straightforward programming interface, making it a go-to choice for developers worldwide.
search_anchor: It's incredibly lightweight and has
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Go-to choice for developers
</div>

</v-click>

---
layout: section
---

# Common Use Cases

---

# Two Key Scenarios

<!--
METADATA:
sentence: Think of scenarios where you have data that's expensive to compute or retrieve, but doesn't change frequently.
search_anchor: Think of scenarios where you
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-data-backup class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Cache for Non-Critical Data</span>
    <div class="text-sm mt-2 opacity-70">Expensive to compute or retrieve</div>
    <div class="text-sm opacity-70">Doesn't change frequently</div>
    <div class="text-sm opacity-70">Dramatically improve performance</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Second, for asynchronous communication where reliable messaging isn't required.
search_anchor: Second, for asynchronous communication where
-->
<v-click>

<div class="mt-10 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-send class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Asynchronous Communication</span>
    <div class="text-sm mt-2 opacity-70">Simple pub-sub messaging</div>
    <div class="text-sm opacity-70">Speed matters more than guaranteed delivery</div>
    <div class="text-sm opacity-70">Reliable messaging not required</div>
  </div>
</div>

</v-click>

---

# The Caching Pattern

<v-click>

<div class="mt-8">

```mermaid
graph LR
    App[Application] --> Check{In Cache?}
    Check -->|Yes| Return[Return Cached]
    Check -->|No| Compute[Compute/Retrieve]
    Compute --> Store[Store in Cache]
    Store --> Return
    style App fill:#0078d4
    style Check fill:#ffd43b
    style Return fill:#51cf66
    style Compute fill:#ff6b6b
    style Store fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Welcome to this lab on Azure Cache for Redis.
search_anchor: Welcome to this lab on
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Fast retrieval on cache hits
</div>

</v-click>

---
layout: section
---

# Azure Cache for Redis

---

# Fully Managed Service

<v-click>

<div class="mt-4">
  <carbon-cloud-services class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: It's essentially a drop-in replacement for running your own Redis cluster, but without the operational overhead.
search_anchor: It's essentially a drop-in replacement
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Drop-in replacement for Redis cluster
</div>

</v-click>

<!--
METADATA:
sentence: It's essentially a drop-in replacement for running your own Redis cluster, but without the operational overhead.
search_anchor: It's essentially a drop-in replacement
-->
<v-click>

<div class="mt-12 text-center text-xl">
Without operational overhead
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    You[Your Application] --> Azure[Azure Cache for Redis]
    Azure -.->|Manages| Provision[Provisioning & Scaling]
    Azure -.->|Manages| Patch[Patching & Updates]
    Azure -.->|Manages| HA[High Availability]
    Azure -.->|Manages| Security[Security & Access]
    style You fill:#0078d4
    style Azure fill:#51cf66
```

</div>

</v-click>

---

# What Microsoft Handles

<!--
METADATA:
sentence: Let's start by understanding what Redis is and why it's valuable in cloud applications.
search_anchor: Let's start by understanding what
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-settings class="text-4xl text-blue-400" />
  <span class="text-lg">Provisioning and scaling</span>
</div>

</v-click>

<!--
METADATA:
sentence: Let's start by understanding what Redis is and why it's valuable in cloud applications.
search_anchor: Let's start by understanding what
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-upgrade class="text-4xl text-green-400" />
  <span class="text-lg">Patching and updates</span>
</div>

</v-click>

<!--
METADATA:
sentence: Let's start by understanding what Redis is and why it's valuable in cloud applications.
search_anchor: Let's start by understanding what
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-availability class="text-4xl text-purple-400" />
  <span class="text-lg">High availability configurations</span>
</div>

</v-click>

<!--
METADATA:
sentence: Let's start by understanding what Redis is and why it's valuable in cloud applications.
search_anchor: Let's start by understanding what
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-orange-400" />
  <span class="text-lg">Security and access control</span>
</div>

</v-click>

<!--
METADATA:
sentence: A cache can dramatically improve your application's performance by storing these results for quick retrieval.
search_anchor: cache can dramatically improve your
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Focus on your application, not infrastructure
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
sentence: A cache can dramatically improve your application's performance by storing these results for quick retrieval.
search_anchor: cache can dramatically improve your
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-data-backup class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Use Redis as data cache</span>
    <div class="text-sm mt-2 opacity-70">Improve application performance</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Redis is a popular open-source technology that combines the functionality of a message queue and a data store.
search_anchor: Redis is a popular open-source
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-send class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Use Redis as message queue</span>
    <div class="text-sm mt-2 opacity-70">Publish and subscribe to events</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Let's start by understanding what Redis is and why it's valuable in cloud applications.
search_anchor: Let's start by understanding what
-->
<v-click>

<div class="mt-12 text-center text-xl">
Work with real application
</div>

</v-click>

<!--
METADATA:
sentence: Azure Cache for Redis - Introduction What is Redis?
search_anchor: Azure Cache for Redis -
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
See capabilities firsthand
</div>

</v-click>

---
layout: section
---

# Key Benefits

---

# Why Choose Redis?

<!--
METADATA:
sentence: A cache can dramatically improve your application's performance by storing these results for quick retrieval.
search_anchor: cache can dramatically improve your
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-flash class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Performance</span>
    <div class="text-sm mt-2 opacity-70">In-memory storage</div>
    <div class="text-sm opacity-70">Sub-millisecond response times</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: It's incredibly lightweight and has a straightforward programming interface, making it a go-to choice for developers worldwide.
search_anchor: It's incredibly lightweight and has
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-clean class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Simplicity</span>
    <div class="text-sm mt-2 opacity-70">Straightforward API</div>
    <div class="text-sm opacity-70">Simple commands</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Second, for asynchronous communication where reliable messaging isn't required.
search_anchor: Second, for asynchronous communication where
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-grid class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Flexibility</span>
    <div class="text-sm mt-2 opacity-70">Caching, messaging, or both</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Azure Cache for Redis Azure Cache for Redis is a fully managed service that implements the Redis API.
search_anchor: Azure Cache for Redis Azure
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-cloud-services class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Managed Service</span>
    <div class="text-sm mt-2 opacity-70">Azure handles infrastructure</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Think of scenarios where you have data that's expensive to compute or retrieve, but doesn't change frequently.
search_anchor: Think of scenarios where you
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-red-400 mt-1">5</div>
  <div>
    <carbon-money class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Cost-Effective</span>
    <div class="text-sm mt-2 opacity-70">Basic tiers provide excellent value</div>
  </div>
</div>

</v-click>

---

# Performance Impact

<v-click>

<div class="mt-8">

```mermaid
graph LR
    NoCache[Without Cache<br/>500ms] -.->|Slow| X[❌]
    Cache[With Redis Cache<br/>5ms] -->|Fast| Check[✓]
    style NoCache fill:#ff6b6b
    style Cache fill:#51cf66
    style Check fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Azure Cache for Redis - Introduction What is Redis?
search_anchor: Azure Cache for Redis -
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
100x faster response times
</div>

</v-click>

<!--
METADATA:
sentence: Welcome to this lab on Azure Cache for Redis.
search_anchor: Welcome to this lab on
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Typical improvement with in-memory caching
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
sentence: Welcome to this lab on Azure Cache for Redis.
search_anchor: Welcome to this lab on
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: Azure Cache for Redis - Introduction What is Redis?
search_anchor: Azure Cache for Redis -
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
See Azure Cache for Redis in action
</div>

</v-click>

</div>
