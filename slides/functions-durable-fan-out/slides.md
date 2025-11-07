---
theme: default
background: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Durable Functions - Fan-Out/Fan-In
  Parallel processing for AZ-204
drawings:
  persist: false
transition: slide-left
title: Fan-Out/Fan-In
mdc: true
---

# Durable Functions: Fan-Out/Fan-In

Parallel Processing at Scale

<div class="abs-bottom-10 left-10">
  <carbon-network-overlay class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore the Fan-Out/Fan-In pattern<br/>Build scalable, efficient cloud applications
</div>

</v-click>

---
layout: section
---

# The Challenge

---

# Sequential vs Parallel

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Sequential[Sequential Processing] --> Time1[5s + 3s + 7s]
    Time1 --> Total1[= 15 seconds]

    Parallel[Parallel Processing] --> Time2[max(5s, 3s, 7s)]
    Time2 --> Total2[= 7 seconds]

    style Sequential fill:#ff6b6b
    style Total1 fill:#ff6b6b
    style Parallel fill:#51cf66
    style Total2 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
That's the power of parallel processing
</div>

</v-click>

---

# The Problem Statement

<v-click>

<div class="mt-8 text-center text-xl">
Multiple external service calls
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-warehouse class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Check Inventory</div>
  </div>
  <div class="text-center">
    <carbon-money class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Get Price Quotes</div>
  </div>
  <div class="text-center">
    <carbon-checkmark class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Validate Data</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Sequential = Sum of all calls
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-xl text-green-400">
Parallel = Slowest call only
</div>

</v-click>

---
layout: section
---

# What is Fan-Out/Fan-In?

---

# Three Key Phases

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Orch[Orchestrator] -->|Fan Out| A1[Activity 1]
    Orch -->|Fan Out| A2[Activity 2]
    Orch -->|Fan Out| A3[Activity 3]
    A1 -->|Fan In| Results[Collect Results]
    A2 -->|Fan In| Results
    A3 -->|Fan In| Results
    Results --> Process[Process Together]
    style Orch fill:#0078d4
    style A1 fill:#51cf66
    style A2 fill:#51cf66
    style A3 fill:#51cf66
    style Results fill:#ffd43b
    style Process fill:#ffd43b
```

</div>

</v-click>

---

# How It Works

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-send-alt class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Fan Out</span>
    <div class="text-sm mt-2 opacity-70">Start multiple activities in parallel</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-time class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Wait</span>
    <div class="text-sm mt-2 opacity-70">Orchestrator waits for all to complete</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-data-collection class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Fan In</span>
    <div class="text-sm mt-2 opacity-70">Collect all results and process together</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Like delegating tasks to a team
</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# The Components

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-flow class="text-4xl text-blue-400" />
  <span class="text-lg">Orchestrator Function - your coordinator</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-task class="text-4xl text-green-400" />
  <span class="text-lg">Activity Functions - the workers</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-backup class="text-4xl text-purple-400" />
  <span class="text-lg">Durable Task Framework - manages everything</span>
</div>

</v-click>

---

# What Makes It Special

<v-click>

<div class="mt-4">
  <carbon-data-base class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
State persisted in Azure Storage
</div>

</v-click>

<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-time class="text-4xl text-blue-400" />
  <span class="text-lg">Can wait for minutes or hours</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-repeat class="text-4xl text-green-400" />
  <span class="text-lg">Automatic retry for failed activities</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark-outline class="text-4xl text-purple-400" />
  <span class="text-lg">Perfect for long-running transactions</span>
</div>

</v-click>

---
layout: section
---

# Real-World Use Cases

---

# When to Use This Pattern

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-shopping-cart class="text-4xl text-blue-400" />
  <span class="text-lg">Get quotes from multiple suppliers</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-structured class="text-4xl text-green-400" />
  <span class="text-lg">Process data by splitting into chunks</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark-outline class="text-4xl text-purple-400" />
  <span class="text-lg">Validate against multiple services simultaneously</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-collection class="text-4xl text-orange-400" />
  <span class="text-lg">Aggregate data from multiple sources</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Multiple independent calls with complete results
</div>

</v-click>

---
layout: section
---

# HTTP Orchestration

---

# Instant Response with Status Tracking

<v-click>

<div class="mt-8">

```mermaid
graph TB
    HTTP[HTTP Trigger] --> Start[Start Orchestration]
    Start --> URLs[Return Status URLs]
    URLs --> Client[Client]
    Client -->|Poll| Status[Check Status]
    Client -->|Wait| Complete[Get Results]
    style HTTP fill:#51cf66
    style Start fill:#0078d4
    style URLs fill:#ffd43b
    style Client fill:#0078d4
    style Complete fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Perfect for responsive UIs
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
No need to keep connection open
</div>

</v-click>

---

# Status URLs

<v-click>

<div class="mt-8 text-center text-xl">
HTTP trigger returns URLs for:
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-query class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Check Status</div>
  </div>
  <div class="text-center">
    <carbon-time class="text-6xl text-green-400" />
    <div class="text-sm mt-3">See Progress</div>
  </div>
  <div class="text-center">
    <carbon-checkmark class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Get Results</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What You'll Build

---

# Quote Engine Application

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Request[Quote Request] --> Orch[Orchestrator]
    Orch -->|Parallel| S1[Supplier 1]
    Orch -->|Parallel| S2[Supplier 2]
    Orch -->|Parallel| S3[Supplier 3]
    S1 --> Collect[Collect Quotes]
    S2 --> Collect
    S3 --> Collect
    Collect --> Best[Select Cheapest]
    style Request fill:#51cf66
    style Orch fill:#0078d4
    style S1 fill:#ffd43b
    style S2 fill:#ffd43b
    style S3 fill:#ffd43b
    style Best fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Call three suppliers in parallel
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-xl">
Wait for all responses
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-xl text-green-400">
Select cheapest option
</div>

</v-click>

---

# The Code is Elegant

<v-click>

<div class="mt-8">

```csharp
// Start multiple activities
var tasks = new List<Task<Quote>>();
tasks.Add(context.CallActivityAsync<Quote>("GetQuote", "Supplier1"));
tasks.Add(context.CallActivityAsync<Quote>("GetQuote", "Supplier2"));
tasks.Add(context.CallActivityAsync<Quote>("GetQuote", "Supplier3"));

// Wait for all to complete
await Task.WhenAll(tasks);

// Process results
var cheapest = tasks.Select(t => t.Result).OrderBy(q => q.Price).First();
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Powerful, efficient, straightforward
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
Build this pattern yourself
</div>

</v-click>

</div>
