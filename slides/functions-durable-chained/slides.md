---
theme: default
layout: cover
---

# Azure Durable Functions - Chained Pattern Introduction

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-azure" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to the Azure Durable Functions lab, where we'll explore the chained pattern

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# The Challenge with Regular Functions

<div class="text-xl mt-8" v-click>

Let's start by understanding the problem we're solving. Imagine you need to build a workflow with multiple steps that must run in a specific order. Perhaps you're processing an order: validate payment

</div>

---

---
layout: center
---

# Enter Durable Functions

<div class="text-xl mt-8" v-click>

This is where Azure Durable Functions come in. Durable Functions let you write stateful workflows in a serverless environment. The key word here is stateful - the framework automatically manages state

</div>

---

---
layout: center
---

# The Chained Pattern Explained

<div class="text-xl mt-8" v-click>

The chained pattern is one of the most common durable function patterns. Think of it as a pipeline where the output of one step becomes the input to the next step.

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">The Orchestrator Function</h3>
<p class="text-sm">This is the conductor of your workflow. It defines what activities run and in what order. The orches</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Activity Functions</h3>
<p class="text-sm">These are the workers that do the actual tasks. Each activity is a standard function that performs o</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">The Durable Client</h3>
<p class="text-sm">This is what starts the orchestration. Any function with a DurableClient binding can start an orches</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">State Management</h3>
<p class="text-sm">The durable functions framework automatically saves the orchestrator's progress. If something fails </p>
</div>

</div>

---

---
layout: center
---

# Real-World Use Cases

<div class="grid grid-cols-1 gap-4 mt-8">



</div>

---

---
layout: center
---

# How This Fits AZ-204 Exam Preparation

<div class="text-xl mt-8" v-click>

For the AZ-204 exam, you need to understand several key aspects of durable functions:

</div>

---

---
layout: center
---

# What You'll Build Today

<div class="text-xl mt-8" v-click>

In this lab, you'll build a health monitoring system using the chained pattern. The workflow starts with a timer trigger that runs periodically. The orchestrator then coordinates three activities:

</div>

---

---
layout: center
---

# Development Approach

<div class="text-xl mt-8" v-click>

You'll start by testing locally using the Azure Storage Emulator for blob and table storage, combined with a real Azure Service Bus for queue messaging. This gives you a fast development cycle without

</div>

---

---
layout: center
---

# Let's Get Started

<div class="text-xl mt-8" v-click>

By the end of this lab, you'll have hands-on experience building a real durable function with the chained pattern. You'll understand how to structure orchestrators and activities, how to pass data bet

</div>