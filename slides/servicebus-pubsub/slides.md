---
theme: default
background: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Service Bus Publish-Subscribe
  Pub-sub messaging pattern for AZ-204
drawings:
  persist: false
transition: slide-left
title: Pub-Sub Pattern
mdc: true
---

# Service Bus Publish-Subscribe

The Pub-Sub Messaging Pattern

<div class="abs-bottom-10 left-10">
  <carbon-network-overlay class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore publish-subscribe with Service Bus<br/>Build extensible, decoupled architectures
</div>

</v-click>

---
layout: section
---

# What is Publish-Subscribe?

---

# The Pattern

<v-click>

<div class="mt-4">
  <carbon-send-alt class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Publisher sends messages
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Zero or many subscribers receive them
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Pub[Publisher] -->|Publish| Topic[Topic]
    Topic -->|Copy| Sub1[Subscriber 1]
    Topic -->|Copy| Sub2[Subscriber 2]
    Topic -->|Copy| Sub3[Subscriber 3]
    style Pub fill:#0078d4
    style Topic fill:#51cf66
    style Sub1 fill:#ffd43b
    style Sub2 fill:#ffd43b
    style Sub3 fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Every subscriber gets a copy
</div>

</v-click>

---

# Key Characteristic

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Add new subscribers anytime
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Without changing existing components
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-add class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Extensible</div>
  </div>
  <div class="text-center">
    <carbon-subtract class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Decoupled</div>
  </div>
  <div class="text-center">
    <carbon-network-3 class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Cloud-Native</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Service Bus Topics

---

# Topics vs Queues

<v-click>

<div class="mt-8">

```mermaid
graph TB
    subgraph Queue Pattern
        PubQ[Publisher] --> Q[Queue]
        Q --> SubQ[One Consumer]
    end

    subgraph Topic Pattern
        PubT[Publisher] --> T[Topic]
        T --> Sub1[Subscriber 1]
        T --> Sub2[Subscriber 2]
        T --> Sub3[Subscriber 3]
    end

    style Q fill:#ffd43b
    style SubQ fill:#ffd43b
    style T fill:#51cf66
    style Sub1 fill:#51cf66
    style Sub2 fill:#51cf66
    style Sub3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Queues: point-to-point
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-xl text-green-400">
Topics: one-to-many
</div>

</v-click>

---

# How Topics Work

<v-click>

<div class="mt-4">
  <carbon-network-4 class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Message published to topic
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Forwarded to all active subscriptions
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg">
Each subscription acts as independent queue
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Receives copy of every message
</div>

</v-click>

---
layout: section
---

# Real-World Example

---

# E-Commerce Order Processing

<v-click>

<div class="mt-8 text-center text-xl">
Customer places order
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Order[Order Created<br/>Published to Topic] --> Ful[Fulfilment<br/>Process Shipping]
    Order --> Ana[Analytics<br/>Aggregate Sales]
    Order --> Aud[Audit<br/>Log for Compliance]
    Order --> Not[Notification<br/>Send Email]
    style Order fill:#0078d4
    style Ful fill:#51cf66
    style Ana fill:#ffd43b
    style Aud fill:#ff6b6b
    style Not fill:#9b59b6
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Each component operates independently
</div>

</v-click>

---

# Independent Processing

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-time class="text-4xl text-blue-400" />
  <span class="text-lg">Each processes at its own pace</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-add class="text-4xl text-green-400" />
  <span class="text-lg">Add new subscriptions anytime</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-subtract class="text-4xl text-purple-400" />
  <span class="text-lg">Remove without affecting others</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
True decoupling
</div>

</v-click>

---
layout: section
---

# Lab Objectives

---

# What We'll Do

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-add class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create Service Bus namespace (Standard tier)</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-document-tasks class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create topic with TTL and size configs</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-user-multiple class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Add multiple subscriptions</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-send class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Publish messages with .NET application</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-red-400 mt-1">5</div>
  <div>
    <carbon-view class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Consume from different subscriptions</span>
  </div>
</div>

</v-click>

---

# Standard Tier Required

<v-click>

<div class="mt-4">
  <carbon-warning class="text-6xl text-orange-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Topics require Standard or Premium tier
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-16">
  <div class="text-center">
    <carbon-close class="text-6xl text-red-400" />
    <div class="text-sm mt-3">Basic</div>
    <div class="text-xs mt-2 opacity-70">Queues only</div>
  </div>
  <div class="text-center">
    <carbon-checkmark class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Standard</div>
    <div class="text-xs mt-2 opacity-70">Queues + Topics</div>
  </div>
  <div class="text-center">
    <carbon-checkmark class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Premium</div>
    <div class="text-xs mt-2 opacity-70">Dedicated resources</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Message Flow

---

# Complete Flow

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Pub[Publisher] -->|1. Publish| Topic[Topic]
    Topic -->|2. Forward| Sub1[Subscription 1]
    Topic -->|2. Forward| Sub2[Subscription 2]
    Sub1 -->|3. Consume| C1[Consumer 1]
    Sub2 -->|3. Consume| C2[Consumer 2]
    style Pub fill:#0078d4
    style Topic fill:#51cf66
    style Sub1 fill:#ffd43b
    style Sub2 fill:#ffd43b
    style C1 fill:#ff6b6b
    style C2 fill:#9b59b6
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
One message becomes many
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Each subscription gets independent copy
</div>

</v-click>

---

# Scalable Architecture

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-network-overlay class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Decoupled</div>
  </div>
  <div class="text-center">
    <carbon-add class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Extensible</div>
  </div>
  <div class="text-center">
    <carbon-scale class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Scalable</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Design distributed systems that grow
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
Build extensible pub-sub architectures
</div>

</v-click>

</div>
