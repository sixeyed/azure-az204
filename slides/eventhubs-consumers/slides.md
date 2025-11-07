---
theme: default
background: https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Event Hubs Partitioned Consumers
  Reliable stream processing for AZ-204
drawings:
  persist: false
transition: slide-left
title: Partitioned Consumers
mdc: true
---

# Event Hubs Partitioned Consumers

Reliable Stream Processing at Scale

<div class="abs-bottom-10 left-10">
  <carbon-data-stream class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Event Hubs partitioned consumers<br/>Process event streams reliably at scale
</div>

</v-click>

---
layout: section
---

# What is Event Hubs?

---

# Big Data Streaming Platform

<v-click>

<div class="mt-4">
  <carbon-flow-stream class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Azure's event ingestion service
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-send-alt class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Event Ingestion</div>
  </div>
  <div class="text-center">
    <carbon-data-stream class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Data Streaming</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Consuming events at scale requires careful handling
</div>

</v-click>

---
layout: section
---

# The Challenge

---

# Problems to Solve

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-bookmark class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Track Progress</span>
    <div class="text-sm mt-2 opacity-70">Where did we leave off after restart?</div>
    <div class="text-sm opacity-70">Don't miss events or process duplicates</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-scale class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Scale Processing</span>
    <div class="text-sm mt-2 opacity-70">Single consumer can't keep up</div>
    <div class="text-sm opacity-70">Multiple consumers without duplicate work</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-availability class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">High Availability</span>
    <div class="text-sm mt-2 opacity-70">If one consumer fails</div>
    <div class="text-sm opacity-70">Others pick up the work automatically</div>
  </div>
</div>

</v-click>

---
layout: section
---

# The Solution

---

# Built into Client Libraries

<v-click>

<div class="mt-4">
  <carbon-checkmark-outline class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Microsoft has built this logic for you
</div>

</v-click>

<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-data-backup class="text-4xl text-blue-400" />
  <span class="text-lg">Recording processed offset using blob storage</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-reset class="text-4xl text-green-400" />
  <span class="text-lg">Resume where consumer left off</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-scale class="text-4xl text-purple-400" />
  <span class="text-lg">Multiple consumers running at scale</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-renew class="text-4xl text-orange-400" />
  <span class="text-lg">Automatic failover when consumer fails</span>
</div>

</v-click>

---

# How It Works

<v-click>

<div class="mt-8">

```mermaid
graph TB
    EventHub[Event Hub] --> Consumer1[Consumer 1]
    EventHub --> Consumer2[Consumer 2]
    Consumer1 -->|Checkpoint| Blob[Blob Storage<br/>State Store]
    Consumer2 -->|Checkpoint| Blob
    Consumer1 -.->|Fails| Consumer2
    style EventHub fill:#0078d4
    style Consumer1 fill:#51cf66
    style Consumer2 fill:#51cf66
    style Blob fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Blob storage as simple state store
</div>

</v-click>

---
layout: section
---

# What We'll Build

---

# Device Logging Scenario

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create Event Hub namespace (Standard SKU)</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-partition class="text-4xl text-green-400" />
  <span class="text-lg">Set up Event Hub with multiple partitions</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-multiple class="text-4xl text-purple-400" />
  <span class="text-lg">Configure consumer groups</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-backup class="text-4xl text-orange-400" />
  <span class="text-lg">Use blob storage to track progress</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-collaborate class="text-4xl text-red-400" />
  <span class="text-lg">Run multiple consumers and observe workload sharing</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-save class="text-4xl text-blue-500" />
  <span class="text-lg">Enable Event Hub Capture</span>
</div>

</v-click>

---

# Competing Consumer Pattern

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Stream[Event Stream] --> Part1[Partition 1]
    Stream --> Part2[Partition 2]
    Stream --> Part3[Partition 3]
    Part1 --> C1[Consumer 1]
    Part2 --> C2[Consumer 2]
    Part3 --> C1
    style Stream fill:#0078d4
    style Part1 fill:#51cf66
    style Part2 fill:#51cf66
    style Part3 fill:#51cf66
    style C1 fill:#ffd43b
    style C2 fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Multiple consumers reading from same stream
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Library manages partition ownership and failover
</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# Partitions

<v-click>

<div class="mt-4">
  <carbon-data-partition class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Event stream split into multiple partitions
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Events[Events] --> P1[Partition 1]
    Events --> P2[Partition 2]
    Events --> P3[Partition 3]
    P1 --> Process1[Parallel Processing]
    P2 --> Process2[Parallel Processing]
    P3 --> Process3[Parallel Processing]
    style Events fill:#0078d4
    style P1 fill:#51cf66
    style P2 fill:#51cf66
    style P3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Allows parallel processing and increases throughput
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg text-red-400">
Partition count set at creation - cannot be changed
</div>

</v-click>

---

# Consumer Groups

<v-click>

<div class="mt-4">
  <carbon-user-multiple class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Logical views of the event stream
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Stream[Event Stream] --> Group1[Consumer Group 1<br/>Real-time Processing]
    Stream --> Group2[Consumer Group 2<br/>Auditing]
    style Stream fill:#0078d4
    style Group1 fill:#51cf66
    style Group2 fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Different groups process same events at different speeds
</div>

</v-click>

---

# Checkpoints

<v-click>

<div class="mt-4">
  <carbon-bookmark class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Record position in event stream
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Process[Process Events] --> Checkpoint[Store Offset]
    Checkpoint --> Blob[Blob Storage]
    Restart[Consumer Restarts] --> Read[Read Offset]
    Read --> Blob
    Read --> Resume[Resume Processing]
    style Process fill:#0078d4
    style Checkpoint fill:#51cf66
    style Blob fill:#ffd43b
    style Resume fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Resume from where they left off after restart
</div>

</v-click>

---

# At-Least-Once Delivery

<v-click>

<div class="mt-8 text-center text-xl">
Delivery guarantee
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Every event processed at least once
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-orange-400">
Events might be processed more than once
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
If consumer crashes between processing and checkpointing
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Design for idempotent processing
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
See these concepts in action
</div>

</v-click>

</div>
