---
theme: default
background: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Cosmos DB Table API
  Modern replacement for Table Storage - AZ-204
drawings:
  persist: false
transition: slide-left
title: Table API
mdc: true
---

# Cosmos DB Table API

Modern Scalable Table Storage

<div class="abs-bottom-10 left-10">
  <carbon-data-table class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: The Cosmos DB Table API is a straight replacement for Azure Table Storage.
search_anchor: Cosmos DB Table API is
-->
<v-click>

<div class="text-xl mt-8">
Explore Cosmos DB Table API<br/>Easy migration from Azure Table Storage
</div>

</v-click>

---
layout: section
---

# What is Table API?

---

# Direct Replacement

<v-click>

<div class="mt-4">
  <carbon-upgrade class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: The Cosmos DB Table API is a straight replacement for Azure Table Storage.
search_anchor: Cosmos DB Table API is
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Straight replacement for Azure Table Storage
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Old[Azure Table<br/>Storage] -->|Upgrade| New[Cosmos DB<br/>Table API]
    style Old fill:#ffd43b
    style New fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: It's designed specifically to offer easy migration paths for older applications that were built with Table Storage.
search_anchor: It's designed specifically to offer
-->
<v-click>

<div class="mt-12 text-center text-xl">
Designed for easy migration
</div>

</v-click>

<!--
METADATA:
sentence: It's designed specifically to offer easy migration paths for older applications that were built with Table Storage.
search_anchor: It's designed specifically to offer
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
For older applications built with Table Storage
</div>

</v-click>

---

# Zero Code Changes

<v-click>

<div class="mt-4">
  <carbon-checkmark-outline class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Why Use Cosmos DB Table API?
search_anchor: Why Use Cosmos DB Table
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Use Cosmos Table API without changing applications
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    App[Existing Application] --> Config[Change Connection String]
    Config --> CosmosAPI[Cosmos Table API]
    CosmosAPI --> Benefits[All Cosmos Benefits]
    style App fill:#0078d4
    style Config fill:#ffd43b
    style CosmosAPI fill:#51cf66
    style Benefits fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: This matches the original Table Storage architecture, making migration even more straightforward.
search_anchor: This matches the original Table
-->
<v-click>

<div class="mt-12 text-center text-xl">
Move to modern storage with minimal effort
</div>

</v-click>

---
layout: section
---

# Why Use Table API?

---

# Upgrade Path for Legacy Apps

<!--
METADATA:
sentence: If you have legacy applications using Azure Table Storage, the Table API gives you an upgrade path without rewriting code.
search_anchor: If you have legacy applications
-->
<v-click>

<div class="mt-8 text-center text-xl">
If you have legacy applications using Table Storage
</div>

</v-click>

<!--
METADATA:
sentence: If you have legacy applications using Azure Table Storage, the Table API gives you an upgrade path without rewriting code.
search_anchor: If you have legacy applications
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Table API gives you an upgrade path
</div>

</v-click>

<!--
METADATA:
sentence: If you have legacy applications using Azure Table Storage, the Table API gives you an upgrade path without rewriting code.
search_anchor: If you have legacy applications
-->
<v-click>

<div class="mt-12 text-center text-xl">
Without rewriting code
</div>

</v-click>

---

# All the Cosmos Benefits

<!--
METADATA:
sentence: You get all the benefits of Cosmos DB - global distribution, guaranteed low latency, multiple consistency models, and enterprise-grade SLA - while keeping your existing table storage code.
search_anchor: You get all the benefits
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-earth class="text-4xl text-blue-400" />
  <span class="text-lg">Global distribution</span>
</div>

</v-click>

<!--
METADATA:
sentence: You get all the benefits of Cosmos DB - global distribution, guaranteed low latency, multiple consistency models, and enterprise-grade SLA - while keeping your existing table storage code.
search_anchor: You get all the benefits
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-flash class="text-4xl text-green-400" />
  <span class="text-lg">Guaranteed low latency</span>
</div>

</v-click>

<!--
METADATA:
sentence: You get all the benefits of Cosmos DB - global distribution, guaranteed low latency, multiple consistency models, and enterprise-grade SLA - while keeping your existing table storage code.
search_anchor: You get all the benefits
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-connected class="text-4xl text-purple-400" />
  <span class="text-lg">Multiple consistency models</span>
</div>

</v-click>

<!--
METADATA:
sentence: This demonstrates the true power of the Table API - seamless migration with zero code changes.
search_anchor: This demonstrates the true power
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-certificate-check class="text-4xl text-orange-400" />
  <span class="text-lg">Enterprise-grade SLA</span>
</div>

</v-click>

<!--
METADATA:
sentence: You get all the benefits of Cosmos DB - global distribution, guaranteed low latency, multiple consistency models, and enterprise-grade SLA - while keeping your existing table storage code.
search_anchor: You get all the benefits
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
While keeping existing table storage code
</div>

</v-click>

---
layout: section
---

# Lab Overview

---

# Seamless Migration Demo

<!--
METADATA:
sentence: We'll run an application that writes to Table Storage, and then we'll switch it to using Cosmos DB with just a configuration change.
search_anchor: We'll run an application that
-->
<v-click>

<div class="mt-8 text-center text-xl">
Run application writing to Table Storage
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    App[Application] -->|Step 1| TableStorage[Azure Table Storage]
    App -->|Step 2| Config[Change Config]
    Config -->|Step 3| Cosmos[Cosmos DB Table API]
    style App fill:#0078d4
    style TableStorage fill:#ffd43b
    style Config fill:#51cf66
    style Cosmos fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: We'll run an application that writes to Table Storage, and then we'll switch it to using Cosmos DB with just a configuration change.
search_anchor: We'll run an application that
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Just a configuration change
</div>

</v-click>

<!--
METADATA:
sentence: This demonstrates the true power of the Table API - seamless migration with zero code changes.
search_anchor: This demonstrates the true power
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Zero code changes required
</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# Simpler Structure

<!--
METADATA:
sentence: Why Use Cosmos DB Table API?
search_anchor: Why Use Cosmos DB Table
-->
<v-click>

<div class="mt-8 text-center text-xl">
Unlike other Cosmos DB APIs
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    OtherAPI[Other APIs] --> Account1[Account]
    Account1 --> DB[Database]
    DB --> Container[Container]

    TableAPI[Table API] --> Account2[Account]
    Account2 --> Tables[Tables]

    style OtherAPI fill:#ffd43b
    style TableAPI fill:#51cf66
    style Tables fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Unlike other Cosmos DB APIs that have hierarchies like Account, Database, and Container, the Table API has a simpler structure: Account level Table(s) directly under the account There are no collections or containers in between.
search_anchor: Unlike other Cosmos DB APIs
-->
<v-click>

<div class="mt-12 text-center text-xl">
No collections or containers in between
</div>

</v-click>

<!--
METADATA:
sentence: This matches the original Table Storage architecture, making migration even more straightforward.
search_anchor: This matches the original Table
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Matches original Table Storage architecture
</div>

</v-click>

---

# Two-Level Hierarchy

<!--
METADATA:
sentence: What is Cosmos DB Table API?
search_anchor: What is Cosmos DB Table
-->
<v-click>

<div class="mt-12 flex justify-center gap-16">
  <div class="text-center">
    <carbon-cloud-services class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Account Level</div>
  </div>
  <div class="text-center">
    <carbon-arrow-right class="text-6xl text-gray-400" />
  </div>
  <div class="text-center">
    <carbon-data-table class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Tables</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This matches the original Table Storage architecture, making migration even more straightforward.
search_anchor: This matches the original Table
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Makes migration even more straightforward
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
sentence: What is Cosmos DB Table API?
search_anchor: What is Cosmos DB Table
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create Cosmos DB account with Table API</span>
</div>

</v-click>

<!--
METADATA:
sentence: We'll run an application that writes to Table Storage, and then we'll switch it to using Cosmos DB with just a configuration change.
search_anchor: We'll run an application that
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-table class="text-4xl text-green-400" />
  <span class="text-lg">Create tables using Portal and CLI</span>
</div>

</v-click>

<!--
METADATA:
sentence: It's designed specifically to offer easy migration paths for older applications that were built with Table Storage.
search_anchor: It's designed specifically to offer
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-purple-400" />
  <span class="text-lg">Deploy app that writes to Table Storage</span>
</div>

</v-click>

<!--
METADATA:
sentence: We'll run an application that writes to Table Storage, and then we'll switch it to using Cosmos DB with just a configuration change.
search_anchor: We'll run an application that
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-orange-400" />
  <span class="text-lg">Switch to Cosmos DB with connection string change</span>
</div>

</v-click>

<!--
METADATA:
sentence: Why Use Cosmos DB Table API?
search_anchor: Why Use Cosmos DB Table
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-search class="text-4xl text-red-400" />
  <span class="text-lg">Query data using Table API</span>
</div>

</v-click>

---

# The Migration Experience

<v-click>

<div class="mt-8">

```mermaid
graph LR
    Original[Original App<br/>Table Storage] -->|Update Config| Migrated[Same App<br/>Cosmos Table API]
    style Original fill:#ffd43b
    style Migrated fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: What is Cosmos DB Table API?
search_anchor: What is Cosmos DB Table
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
That's the power of Table API
</div>

</v-click>

<!--
METADATA:
sentence: This demonstrates the true power of the Table API - seamless migration with zero code changes.
search_anchor: This demonstrates the true power
-->
<v-click>

<div class="mt-8 text-center text-xl">
Seamless migration
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
sentence: Key Concepts Before we dive in, let's understand the structure.
search_anchor: Key Concepts Before we dive
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: What is Cosmos DB Table API?
search_anchor: What is Cosmos DB Table
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Experience seamless migration to Cosmos DB
</div>

</v-click>

</div>
