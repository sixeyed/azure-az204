---
theme: default
background: https://images.unsplash.com/photo-1516110833967-0b5716ca1387?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Durable Functions - Chained Pattern
  Stateful workflows for AZ-204
drawings:
  persist: false
transition: slide-left
title: Chained Pattern
mdc: true
---

# Azure Durable Functions

Chained Pattern for Sequential Workflows

<div class="abs-bottom-10 left-10">
  <carbon-flow class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Azure Durable Functions<br/>Orchestrate sequential workflows in serverless
</div>

</v-click>

---
layout: section
---

# The Challenge

---

# Regular Functions Limitations

<v-click>

<div class="mt-8 text-center text-xl">
Multiple steps in specific order
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    F1[Function 1] -->|Blob| F2[Function 2]
    F2 -->|Queue| F3[Function 3]
    F3 -->|Table| F4[Function 4]
    style F1 fill:#ffd43b
    style F2 fill:#ffd43b
    style F3 fill:#ffd43b
    style F4 fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg text-red-400">
This works, but has serious limitations
</div>

</v-click>

---

# The Problems

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-warning class="text-4xl text-red-400 mt-1" />
  <div>
    <div class="text-lg font-bold">No Order Guarantee</div>
    <div class="text-sm mt-2 opacity-70">Can't guarantee exact running order</div>
    <div class="text-sm opacity-70">Distributed triggers are unpredictable</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-data-base class="text-4xl text-orange-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Data Passing Complex</div>
    <div class="text-sm mt-2 opacity-70">Need intermediate storage</div>
    <div class="text-sm opacity-70">Complicated state management</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-view class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">No Workflow Status</div>
    <div class="text-sm mt-2 opacity-70">No single place to see overall status</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-reset class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Messy Error Handling</div>
    <div class="text-sm mt-2 opacity-70">Retry logic spread across functions</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Enter Durable Functions

---

# Stateful Workflows in Serverless

<v-click>

<div class="mt-4">
  <carbon-flow class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Durable Functions let you write stateful workflows
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl">
The key word: Stateful
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Orchestrator[Orchestrator] --> Activity1[Activity A]
    Activity1 --> Activity2[Activity B]
    Activity2 --> Activity3[Activity C]
    Framework[Durable Framework] -.->|Manages State| Orchestrator
    style Orchestrator fill:#0078d4
    style Activity1 fill:#51cf66
    style Activity2 fill:#51cf66
    style Activity3 fill:#51cf66
    style Framework fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Framework automatically manages state
</div>

</v-click>

---

# How It Works

<v-click>

<div class="mt-8 text-center text-xl">
Write an orchestrator that calls activity functions
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-flow class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Orchestrator</div>
    <div class="text-xs mt-2 opacity-70">Controls workflow</div>
  </div>
  <div class="text-center">
    <carbon-task class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Activities</div>
    <div class="text-xs mt-2 opacity-70">Do one thing well</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Orchestrator manages data flow and execution order
</div>

</v-click>

---
layout: section
---

# The Chained Pattern

---

# Pipeline Execution

<v-click>

<div class="mt-4">
  <carbon-diagram class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Output of one step becomes input to next
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Trigger[Trigger] --> Orch[Orchestrator]
    Orch --> A[Activity A]
    A -->|Result| B[Activity B]
    B -->|Result| C[Activity C]
    style Trigger fill:#51cf66
    style Orch fill:#0078d4
    style A fill:#ffd43b
    style B fill:#ffd43b
    style C fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Each step runs after previous one completes
</div>

</v-click>

---

# Defined in Code

<v-click>

<div class="mt-8 text-center text-xl">
Entire workflow in one place
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-view class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">See the Logic</div>
  </div>
  <div class="text-center">
    <carbon-flow-data class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Understand Flow</div>
  </div>
  <div class="text-center">
    <carbon-settings-adjust class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Manage as Unit</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Beautiful simplicity
</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# The Components

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-flow class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Orchestrator Function</span>
    <div class="text-sm mt-2 opacity-70">Conductor of workflow</div>
    <div class="text-sm opacity-70">Defines what runs and in what order</div>
    <div class="text-sm mt-2 text-red-400">Must be deterministic!</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-task class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Activity Functions</span>
    <div class="text-sm mt-2 opacity-70">Workers that do actual tasks</div>
    <div class="text-sm opacity-70">Use ActivityTrigger binding</div>
    <div class="text-sm opacity-70">Can only be called by orchestrator</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-play class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Durable Client</span>
    <div class="text-sm mt-2 opacity-70">Starts the orchestration</div>
    <div class="text-sm opacity-70">DurableClient binding</div>
  </div>
</div>

</v-click>

---

# State Management

<v-click>

<div class="mt-4">
  <carbon-data-backup class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Automatic progress saving
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Orch[Orchestrator Running] --> Save[Framework Saves State]
    Save --> Fail[Something Fails]
    Fail --> Restore[Framework Restores]
    Restore --> Continue[Continue from Checkpoint]
    style Orch fill:#0078d4
    style Save fill=#51cf66
    style Fail fill:#ff6b6b
    style Restore fill:#ffd43b
    style Continue fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Reliability without writing state management code
</div>

</v-click>

---
layout: section
---

# Real-World Use Cases

---

# Perfect Scenarios

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-structured class="text-4xl text-blue-400" />
  <span class="text-lg">Data processing pipelines</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-shopping-cart class="text-4xl text-green-400" />
  <span class="text-lg">Order processing workflows</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-settings class="text-4xl text-purple-400" />
  <span class="text-lg">System initialization sequences</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-batch-job class="text-4xl text-orange-400" />
  <span class="text-lg">Batch operations with transformations</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Any sequential workflow with dependencies
</div>

</v-click>

---
layout: section
---

# What You'll Build

---

# Health Monitoring System

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Timer[Timer Trigger] --> Orch[Orchestrator]
    Orch --> Blob[WriteBlob<br/>Save Heartbeat]
    Blob --> SB[NotifySubscribers<br/>Publish to Service Bus]
    SB --> Log[WriteLog<br/>Record to Table Storage]
    style Timer fill:#51cf66
    style Orch fill:#0078d4
    style Blob fill:#ffd43b
    style SB fill:#ffd43b
    style Log fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Coordinate multiple Azure services
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
In a reliable, sequential workflow
</div>

</v-click>

---

# Development Approach

<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <carbon-laptop class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Test Locally</div>
    <div class="text-xs mt-2 opacity-70">Storage Emulator</div>
  </div>
  <div class="text-center">
    <carbon-arrow-right class="text-6xl text-gray-400" />
  </div>
  <div class="text-center">
    <carbon-cloud class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Deploy to Azure</div>
    <div class="text-xs mt-2 opacity-70">Production Environment</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Fast development cycle
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
Build something great with durable functions
</div>

</v-click>

</div>
