---
theme: default
background: https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Cosmos DB Performance
  Request Units and cost optimization for AZ-204
drawings:
  persist: false
transition: slide-left
title: Performance Provisioning
mdc: true
---

# Cosmos DB Performance Provisioning

Understanding Request Units

<div class="abs-bottom-10 left-10">
  <carbon-dashboard class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: Cosmos DB charges you for two main things: storage and compute.
search_anchor: Cosmos DB charges you for
-->
<v-click>

<div class="text-xl mt-8">
Explore Cosmos DB performance provisioning<br/>Control both performance and cost
</div>

</v-click>

---
layout: section
---

# Cosmos DB Pricing

---

# Two Main Charges

<!--
METADATA:
sentence: Storage is straightforward - it's a flat rate based on the amount of data you store, and this rate is the same regardless of your performance level.
search_anchor: Storage is straightforward - it's
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-data-base class="text-5xl text-blue-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Storage</div>
    <div class="text-sm mt-2 opacity-70">Flat rate based on data stored</div>
    <div class="text-sm opacity-70">Same rate regardless of performance</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Cosmos DB measures compute in terms of Request Units, or RUs.
search_anchor: Cosmos DB measures compute in
-->
<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-dashboard class="text-5xl text-green-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Compute</div>
    <div class="text-sm mt-2 opacity-70">Measured in Request Units (RUs)</div>
    <div class="text-sm opacity-70">All access operations charged</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Compute, however, is where things get interesting.
search_anchor: Compute, however, is where things
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
This is where things get interesting
</div>

</v-click>

---

# Request Units

<v-click>

<div class="mt-4">
  <carbon-activity class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: You pay for all access operations - reads, writes, deletes, updates, and queries.
search_anchor: You pay for all access
-->
<v-click>

<div class="mt-8 text-xl text-center">
All operations consume RUs
</div>

</v-click>

<!--
METADATA:
sentence: You pay for all access operations - reads, writes, deletes, updates, and queries.
search_anchor: You pay for all access
-->
<v-click>

<div class="mt-12 grid grid-cols-2 gap-8">
  <div class="text-center">
    <carbon-view class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Reads</div>
  </div>
  <div class="text-center">
    <carbon-edit class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Writes</div>
  </div>
  <div class="text-center">
    <carbon-delete class="text-5xl text-red-400" />
    <div class="text-sm mt-3">Deletes</div>
  </div>
  <div class="text-center">
    <carbon-search class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Queries</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: With serverless, you pay only for the RUs you actually consume.
search_anchor: serverless, you pay only for
-->
<v-click>

<div class="mt-12 text-center text-lg">
You pay for every access
</div>

</v-click>

---
layout: section
---

# Provisioning Models

---

# Two Payment Options

<!--
METADATA:
sentence: With serverless, you pay only for the RUs you actually consume.
search_anchor: serverless, you pay only for
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-cloud class="text-5xl text-blue-400 mt-1" />
  <div>
    <div class="text-xl font-bold text-blue-400">Serverless</div>
    <div class="text-sm mt-2 opacity-70">Pay only for RUs consumed</div>
    <div class="text-sm opacity-70">Great for dev/test</div>
    <div class="text-sm opacity-70">Unpredictable workloads</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This can be more cost-effective for consistent, high-volume workloads.
search_anchor: This can be more cost-effective
-->
<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-plan class="text-5xl text-green-400 mt-1" />
  <div>
    <div class="text-xl font-bold text-green-400">Provisioned</div>
    <div class="text-sm mt-2 opacity-70">Fixed RUs per second</div>
    <div class="text-sm opacity-70">Pay whether used or not</div>
    <div class="text-sm opacity-70">Cost-effective for consistent workloads</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Workload{Workload Type?} -->|Occasional| Serverless[Serverless<br/>Pay-per-use]
    Workload -->|Consistent| Provisioned[Provisioned<br/>Fixed capacity]
    style Workload fill:#0078d4
    style Serverless fill:#51cf66
    style Provisioned fill:#ffd43b
```

</div>

</v-click>

---
layout: section
---

# Why This Matters

---

# Cost Optimization

<!--
METADATA:
sentence: Why This Matters Cost is often cited as a concern when considering Cosmos DB.
search_anchor: Why This Matters Cost is
-->
<v-click>

<div class="mt-8 text-center text-xl">
Cost is often cited as a concern
</div>

</v-click>

<!--
METADATA:
sentence: Second, there's the provisioned model.
search_anchor: Second, there's the provisioned model
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
But here's the truth
</div>

</v-click>

<!--
METADATA:
sentence: The key is knowing how to test and measure your RU consumption.
search_anchor: key is knowing how to
-->
<v-click>

<div class="mt-12 text-center text-xl">
With proper planning and understanding
</div>

</v-click>

<!--
METADATA:
sentence: This can be more cost-effective for consistent, high-volume workloads.
search_anchor: This can be more cost-effective
-->
<v-click>

<div class="mt-4 text-center text-xl">
Cosmos DB can be very cost-effective
</div>

</v-click>

<!--
METADATA:
sentence: The key is knowing how to test and measure your RU consumption.
search_anchor: key is knowing how to
-->
<v-click>

<div class="mt-12 text-center text-2xl text-purple-400">
The key is knowing how to measure
</div>

</v-click>

---
layout: section
---

# What You'll Learn

---

# Lab Objectives

<!--
METADATA:
sentence: This is great for development, testing, or applications with unpredictable workloads.
search_anchor: This is great for development
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create database with fixed performance levels</span>
</div>

</v-click>

<!--
METADATA:
sentence: But here's the truth - if you plan appropriately and understand how RUs work, Cosmos DB can actually be very cost-effective.
search_anchor: But here's the truth -
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-calculate class="text-4xl text-green-400" />
  <span class="text-lg">Understand how RUs are calculated</span>
</div>

</v-click>

<!--
METADATA:
sentence: The key is knowing how to test and measure your RU consumption.
search_anchor: key is knowing how to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-chart-line class="text-4xl text-purple-400" />
  <span class="text-lg">Measure RU consumption for different queries</span>
</div>

</v-click>

<!--
METADATA:
sentence: The key is knowing how to test and measure your RU consumption.
search_anchor: key is knowing how to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-structured class="text-4xl text-orange-400" />
  <span class="text-lg">See data modeling impact on RU usage</span>
</div>

</v-click>

<!--
METADATA:
sentence: The key is knowing how to test and measure your RU consumption.
search_anchor: key is knowing how to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-focus class="text-4xl text-red-400" />
  <span class="text-lg">Use point reads to minimize costs</span>
</div>

</v-click>

<!--
METADATA:
sentence: This is great for development, testing, or applications with unpredictable workloads.
search_anchor: This is great for development
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-blue-500" />
  <span class="text-lg">Apply index policies for optimization</span>
</div>

</v-click>

---
layout: section
---

# Lab Scenario

---

# Shop Database

<!--
METADATA:
sentence: This is great for development, testing, or applications with unpredictable workloads.
search_anchor: This is great for development
-->
<v-click>

<div class="mt-8 text-center text-xl">
Product information with different configurations
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Create[Create Containers] --> Load[Load Data]
    Load --> Query[Run Queries]
    Query --> Measure[Measure RUs]
    Measure --> Optimize[Optimize]
    style Create fill:#0078d4
    style Load fill:#51cf66
    style Query fill:#ffd43b
    style Measure fill:#ff6b6b
    style Optimize fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: You'll create containers with different configurations, load data in different formats, and run queries to see exactly how many Request Units each operation consumes.
search_anchor: You'll create containers with different
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
See exactly how many RUs each operation consumes
</div>

</v-click>

---

# Practical Experience

<!--
METADATA:
sentence: By the end of this lab, you'll have practical experience measuring RU consumption and making informed decisions about how to structure your Cosmos DB solutions for optimal cost and performance.
search_anchor: By the end of this
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-analytics class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Measure Consumption</div>
  </div>
  <div class="text-center">
    <carbon-decision-tree class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Make Informed Decisions</div>
  </div>
  <div class="text-center">
    <carbon-money class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Optimize Cost</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: By the end of this lab, you'll have practical experience measuring RU consumption and making informed decisions about how to structure your Cosmos DB solutions for optimal cost and performance.
search_anchor: By the end of this
-->
<v-click>

<div class="mt-12 text-center text-xl">
Structure solutions for optimal cost and performance
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
sentence: Compute, however, is where things get interesting.
search_anchor: Compute, however, is where things
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: Cosmos DB measures compute in terms of Request Units, or RUs.
search_anchor: Cosmos DB measures compute in
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Master Request Units and cost optimization
</div>

</v-click>

</div>
