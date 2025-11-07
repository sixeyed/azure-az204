---
theme: default
background: https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Cosmos DB
  Planet-scale database for AZ-204
drawings:
  persist: false
transition: slide-left
title: Azure Cosmos DB
mdc: true
---

# Azure Cosmos DB

Planet-Scale Globally Distributed Database

<div class="abs-bottom-10 left-10">
  <carbon-data-base class="text-8xl text-purple-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Azure Cosmos DB<br/>Globally distributed, multi-model database
</div>

</v-click>

<v-click>

<div class="text-lg mt-6 opacity-70">
Designed for planet-scale applications
</div>

</v-click>

---
layout: section
---

# What is Cosmos DB?

---

# Planet-Scale Database

<v-click>

<div class="mt-4">
  <carbon-earth class="text-8xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Start[Start Small<br/>Localized] --> Expand[Expand Global<br/>Replication]
    Expand --> Scale[Handle Any Load]
    style Start fill:#51cf66
    style Expand fill:#ffd43b
    style Scale fill:#0078d4
```

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Start small, expand globally
</div>

</v-click>

---

# Multi-Model Support

<v-click>

<div class="mt-8 text-center text-xl">
Single product, different storage drivers
</div>

</v-click>

<v-click>

<div class="mt-12 grid grid-cols-3 gap-6">
  <div class="text-center">
    <carbon-data-1 class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">NoSQL</div>
  </div>
  <div class="text-center">
    <carbon-data-base class="text-5xl text-green-400" />
    <div class="text-sm mt-3">MongoDB</div>
  </div>
  <div class="text-center">
    <carbon-network-3 class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Cassandra</div>
  </div>
  <div class="text-center">
    <carbon-share class="text-5xl text-orange-400" />
    <div class="text-sm mt-3">Gremlin (Graph)</div>
  </div>
  <div class="text-center">
    <carbon-table class="text-5xl text-red-400" />
    <div class="text-sm mt-3">Table</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Different storage approaches, consistent management
</div>

</v-click>

---
layout: section
---

# Understanding the NoSQL Driver

---

# Naming Confusion

<v-click>

<div class="mt-4">
  <carbon-warning class="text-6xl text-orange-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
NoSQL is the native driver for Cosmos DB
</div>

</v-click>

<v-click>

<div class="mt-12 text-lg text-center text-red-400">
Previously called the "SQL" driver
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-portal class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Portal: "NoSQL"</div>
  </div>
  <div class="text-center">
    <carbon-command-line class="text-5xl text-green-400" />
    <div class="text-sm mt-3">CLI: "SQL"</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Keep this in mind to avoid confusion
</div>

</v-click>

---
layout: section
---

# Why Choose Cosmos DB?

---

# Intelligent Partitioning

<v-click>

<div class="mt-4">
  <carbon-data-enrichment class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Spreads data across multiple storage locations
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Data[Your Data] --> P1[Partition 1]
    Data --> P2[Partition 2]
    Data --> P3[Partition 3]
    P1 -->|Read/Write| App[Applications]
    P2 -->|Read/Write| App
    P3 -->|Read/Write| App
    style Data fill:#0078d4
    style P1 fill:#51cf66
    style P2 fill:#51cf66
    style P3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
All locations can be read from and written to simultaneously
</div>

</v-click>

---

# Automatic Scaling

<v-click>

<div class="mt-12 text-center text-xl">
Need more capacity?
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Current[3 Partitions] -->|Add More| Scaled[6 Partitions]
    style Current fill:#ffd43b
    style Scaled fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Cosmos DB simply adds more partitions
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg opacity-70">
Completely managed for you
</div>

</v-click>

---
layout: section
---

# Key Capabilities

---

# Global Distribution

<v-click>

<div class="mt-4">
  <carbon-earth-filled class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Primary[Primary<br/>East US] --> West[West US]
    Primary --> Europe[West Europe]
    Primary --> Asia[East Asia]
    style Primary fill:#0078d4
    style West fill:#51cf66
    style Europe fill:#51cf66
    style Asia fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Replicate across multiple Azure regions worldwide
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Data closer to users = reduced latency
</div>

</v-click>

---

# Flexible Consistency Levels

<v-click>

<div class="mt-6 grid grid-cols-2 gap-6">
  <div>
    <carbon-locked class="text-5xl text-red-400" />
    <div class="text-lg mt-3 font-bold">Strong</div>
    <div class="text-sm mt-2 opacity-70">Critical data</div>
  </div>
  <div>
    <carbon-renew class="text-5xl text-orange-400" />
    <div class="text-lg mt-3 font-bold">Bounded Staleness</div>
    <div class="text-sm mt-2 opacity-70">Predictable lag</div>
  </div>
  <div>
    <carbon-network-overlay class="text-5xl text-yellow-400" />
    <div class="text-lg mt-3 font-bold">Session</div>
    <div class="text-sm mt-2 opacity-70">User sessions</div>
  </div>
  <div>
    <carbon-data-enrichment class="text-5xl text-green-400" />
    <div class="text-lg mt-3 font-bold">Consistent Prefix</div>
    <div class="text-sm mt-2 opacity-70">Ordered updates</div>
  </div>
  <div>
    <carbon-forward class="text-5xl text-blue-400" />
    <div class="text-lg mt-3 font-bold">Eventual</div>
    <div class="text-sm mt-2 opacity-70">Lowest latency</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Five consistency levels - choose based on needs
</div>

</v-click>

---

# Guaranteed Performance

<v-click>

<div class="mt-8 text-center text-xl">
Service Level Agreements for:
</div>

</v-click>

<v-click>

<div class="mt-10 grid grid-cols-2 gap-8">
  <div class="flex items-center gap-4">
    <carbon-meter-alt class="text-4xl text-blue-400" />
    <span>Throughput</span>
  </div>
  <div class="flex items-center gap-4">
    <carbon-time class="text-4xl text-green-400" />
    <span>Latency</span>
  </div>
  <div class="flex items-center gap-4">
    <carbon-checkmark-outline class="text-4xl text-purple-400" />
    <span>Availability</span>
  </div>
  <div class="flex items-center gap-4">
    <carbon-data-check class="text-4xl text-orange-400" />
    <span>Consistency</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Predictable performance at any scale
</div>

</v-click>

---
layout: section
---

# Cost Considerations

---

# Enterprise-Grade Database

<v-click>

<div class="mt-4">
  <carbon-currency-dollar class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Pricing based on Request Units (RUs)
</div>

</v-click>

<v-click>

<div class="mt-12 text-lg text-center">
Computational resources needed for operations
</div>

</v-click>

---

# Pricing Options

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-meter-alt class="text-5xl text-blue-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Provisioned Throughput</div>
    <div class="text-sm mt-2 opacity-70">Free tier available, set price caps</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-cloud class="text-5xl text-green-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Serverless</div>
    <div class="text-sm mt-2 opacity-70">Development and smaller workloads</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-scale class="text-5xl text-purple-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Autoscale</div>
    <div class="text-sm mt-2 opacity-70">Adjusts automatically based on demand</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 text-center text-lg text-orange-400">
⚠️ Understand pricing before production deployment
</div>

</v-click>

---
layout: section
---

# Real-World Use Cases

---

# Perfect For

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-iot-platform class="text-4xl text-blue-400" />
  <div>
    <div class="text-lg font-bold">IoT and Telemetry</div>
    <div class="text-sm opacity-70">Massive volumes from connected devices</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-shopping-cart class="text-4xl text-green-400" />
  <div>
    <div class="text-lg font-bold">Retail and E-commerce</div>
    <div class="text-sm opacity-70">Product catalogs, global transactions</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-game-console class="text-4xl text-purple-400" />
  <div>
    <div class="text-lg font-bold">Gaming</div>
    <div class="text-sm opacity-70">Player profiles, leaderboards, low latency</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-application-mobile class="text-4xl text-orange-400" />
  <div>
    <div class="text-lg font-bold">Web and Mobile Apps</div>
    <div class="text-sm opacity-70">Data distributed close to users</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-chart-line class="text-4xl text-red-400" />
  <div>
    <div class="text-lg font-bold">Financial Services</div>
    <div class="text-sm opacity-70">Strong consistency guarantees</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Important Concepts

---

# Terminology

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-identification class="text-4xl text-blue-400" />
  <div>
    <div class="text-lg font-bold">Account</div>
    <div class="text-sm opacity-70">Top-level resource containing databases</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-base class="text-4xl text-green-400" />
  <div>
    <div class="text-lg font-bold">Database</div>
    <div class="text-sm opacity-70">Container for collections of data</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-container-software class="text-4xl text-purple-400" />
  <div>
    <div class="text-lg font-bold">Container</div>
    <div class="text-sm opacity-70">Similar to table, flexible schema</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document class="text-4xl text-orange-400" />
  <div>
    <div class="text-lg font-bold">Items</div>
    <div class="text-sm opacity-70">Individual records in containers</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-enrichment class="text-4xl text-red-400" />
  <div>
    <div class="text-lg font-bold">Partition Key</div>
    <div class="text-sm opacity-70">Property to distribute data - critical for performance</div>
  </div>
</div>

</v-click>

---

# Hierarchy

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Account[Cosmos DB Account] --> DB1[Database]
    DB1 --> Container1[Container]
    Container1 --> Item1[Item 1]
    Container1 --> Item2[Item 2]
    Container1 --> Item3[Item 3]
    style Account fill:#0078d4
    style DB1 fill:#ffd43b
    style Container1 fill:#ff6b6b
    style Item1 fill:#51cf66
    style Item2 fill:#51cf66
    style Item3 fill:#51cf66
```

</div>

</v-click>

---
layout: section
---

# What's Next

---

# Lab Objectives

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-add class="text-3xl text-blue-400 mt-1" />
  <span>Create Cosmos DB account</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-data-base class="text-3xl text-green-400 mt-1" />
  <span>Set up database with NoSQL driver</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-application class="text-3xl text-purple-400 mt-1" />
  <span>Run sample app with Entity Framework</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-search class="text-3xl text-orange-400 mt-1" />
  <span>Explore Data Explorer in Azure Portal</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-password class="text-3xl text-red-400 mt-1" />
  <span>Retrieve connection strings via Portal and CLI</span>
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
Build globally distributed applications with Cosmos DB
</div>

</v-click>

</div>
