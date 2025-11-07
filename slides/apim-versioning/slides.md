---
theme: default
background: https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## API Management: Versioning
  Managing API changes for AZ-204
drawings:
  persist: false
transition: slide-left
title: API Versioning
mdc: true
---

# API Versioning

Managing Changes with Backward Compatibility

<div class="abs-bottom-10 left-10">
  <carbon-version class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: API Management: API Changes & Versioning - Introduction Welcome to this lab on API Management versioning and revisions.
search_anchor: API Management: API Changes &
-->
<v-click>

<div class="text-xl mt-8">
Explore API versioning and revisions<br/>in Azure API Management
</div>

</v-click>

---
layout: section
---

# Why API Versioning Matters

---

# APIs as Contracts

<v-click>

<div class="mt-4">
  <carbon-document-tasks class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Why API Versioning Matters APIs are meant to be explicitly defined contracts between your service and its consumers.
search_anchor: Why API Versioning Matters APIs
-->
<v-click>

<div class="mt-8 text-xl text-center">
APIs are explicitly defined contracts
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    API[Your API<br/>Contract] --> Client1[Client App 1]
    API --> Client2[Client App 2]
    API --> Client3[Client App 3]
    style API fill:#0078d4
    style Client1 fill:#51cf66
    style Client2 fill:#51cf66
    style Client3 fill=#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: When you publish an API, clients build their applications against that contract.
search_anchor: When you publish an API
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Clients build applications against that contract
</div>

</v-click>

---

# The Challenge

<!--
METADATA:
sentence: But what happens when you need to make changes?
search_anchor: But what happens when you
-->
<v-click>

<div class="mt-12 text-center text-2xl">
What happens when you need to make changes?
</div>

</v-click>

<v-click>

<div class="mt-12">
  <carbon-warning class="text-8xl text-orange-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Versions are for breaking changes.
search_anchor: Versions are for breaking changes
-->
<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Breaking changes could break existing clients
</div>

</v-click>

---

# The Solution: Versioning

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Versioning[Versioning Scheme] --> V1[API v1.0]
    Versioning --> V2[API v2.0]
    V1 --> Old[Old Clients]
    V2 --> New[New Clients]
    style Versioning fill:#0078d4
    style V1 fill:#51cf66
    style V2 fill:#ffd43b
    style Old fill:#51cf66
    style New fill=#ffd43b
```

</div>

</v-click>

<!--
METADATA:
sentence: Versions are for breaking changes.
search_anchor: Versions are for breaking changes
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Support multiple versions simultaneously
</div>

</v-click>

<!--
METADATA:
sentence: This gives your clients time to migrate at their own pace.
search_anchor: This gives your clients time
-->
<v-click>

<div class="mt-6 text-center text-lg opacity-70">
Give clients time to migrate at their own pace
</div>

</v-click>

---
layout: section
---

# Revisions vs Versions

---

# Two Types of Changes

<!--
METADATA:
sentence: Versions are for breaking changes.
search_anchor: Versions are for breaking changes
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-4xl text-green-400 mt-1">1</div>
  <div>
    <carbon-renew class="text-4xl inline-block text-green-400" />
    <div class="ml-3 mt-2">
      <div class="text-xl font-bold">Revisions</div>
      <div class="text-sm mt-2 opacity-70">Non-breaking changes</div>
    </div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Versions are for breaking changes.
search_anchor: Versions are for breaking changes
-->
<v-click>

<div class="mt-10 flex items-start gap-4">
  <div class="text-4xl text-red-400 mt-1">2</div>
  <div>
    <carbon-version class="text-4xl inline-block text-red-400" />
    <div class="ml-3 mt-2">
      <div class="text-xl font-bold">Versions</div>
      <div class="text-sm mt-2 opacity-70">Breaking changes</div>
    </div>
  </div>
</div>

</v-click>

---

# Revisions: Non-Breaking

<v-click>

<div class="mt-4">
  <carbon-renew class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Think of adding optional parameters to an existing operation.
search_anchor: Think of adding optional parameters
-->
<v-click>

<div class="mt-8 text-xl text-center">
Add optional parameters to existing operations
</div>

</v-click>

<v-click>

<div class="mt-12">

```javascript
// Original API
GET /api/random

// Revision - add optional parameters
GET /api/random?min=1&max=100
```

</div>

</v-click>

<!--
METADATA:
sentence: Consumers don't need to update their code because the changes are backward compatible.
search_anchor: Consumers don't need to update
-->
<v-click>

<div class="mt-8 text-center text-lg text-green-400">
Consumers don't need to update their code
</div>

</v-click>

<!--
METADATA:
sentence: They use defaults if the new parameters aren't provided.
search_anchor: They use defaults if the
-->
<v-click>

<div class="mt-4 text-center text-sm opacity-70">
Defaults used if new parameters aren't provided
</div>

</v-click>

---

# Versions: Breaking Changes

<v-click>

<div class="mt-4">
  <carbon-version class="text-6xl text-red-400" />
</div>

</v-click>

<!--
METADATA:
sentence: These require a new API version because existing clients would break if you changed the original.
search_anchor: These require a new API
-->
<v-click>

<div class="mt-8 text-xl text-center text-red-400">
Require a new API version
</div>

</v-click>

<!--
METADATA:
sentence: Versions are for breaking changes.
search_anchor: Versions are for breaking changes
-->
<v-click>

<div class="mt-12 text-lg">
Breaking changes include:
</div>

</v-click>

<!--
METADATA:
sentence: For example, making optional parameters mandatory, or changing response structures.
search_anchor: example, making optional parameters mandatory
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-3xl text-red-400" />
  <span>Making optional parameters mandatory</span>
</div>

</v-click>

<!--
METADATA:
sentence: For example, making optional parameters mandatory, or changing response structures.
search_anchor: example, making optional parameters mandatory
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-warning class="text-3xl text-red-400" />
  <span>Changing response structures</span>
</div>

</v-click>

<!--
METADATA:
sentence: For example, making optional parameters mandatory, or changing response structures.
search_anchor: example, making optional parameters mandatory
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-warning class="text-3xl text-red-400" />
  <span>Removing operations or fields</span>
</div>

</v-click>

---

# Revision Example

<v-click>

<div class="mt-8">

```mermaid
graph LR
    V1[v1.0] --> V1.1[v1.1 Revision]
    style V1 fill:#51cf66
    style V1.1 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8">

```javascript
// v1.0
GET /api/random
// Returns: { "number": 42 }

// v1.1 (revision)
GET /api/random?min=10&max=50
// Still works: GET /api/random
// Returns: { "number": 33 }
```

</div>

</v-click>

<!--
METADATA:
sentence: Consumers don't need to update their code because the changes are backward compatible.
search_anchor: Consumers don't need to update
-->
<v-click>

<div class="mt-6 text-center text-lg text-green-400">
Backward compatible!
</div>

</v-click>

---

# Version Example

<v-click>

<div class="mt-8">

```mermaid
graph TB
    V1[v1.0] --> V2[v2.0 NEW VERSION]
    style V1 fill:#51cf66
    style V2 fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-8">

```javascript
// v1.0
GET /api/v1/random
// Optional params

// v2.0 (breaking change)
GET /api/v2/random?min=required&max=required
// Mandatory params - breaks v1 clients!
```

</div>

</v-click>

<!--
METADATA:
sentence: Consumers don't need to update their code because the changes are backward compatible.
search_anchor: Consumers don't need to update
-->
<v-click>

<div class="mt-6 text-center text-lg text-red-400">
Not backward compatible
</div>

</v-click>

---
layout: section
---

# Deployment Slots

---

# The Power of Deployment Slots

<v-click>

<div class="mt-4">
  <carbon-deployment-pattern class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: This is where versioning becomes critical.
search_anchor: This is where versioning becomes
-->
<v-click>

<div class="mt-8 text-xl text-center">
APIM versioning + App Service deployment slots
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    APIM[APIM] --> Slot1[Production Slot<br/>v1.0]
    APIM --> Slot2[Staging Slot<br/>v2.0]
    APIM --> Slot3[Dev Slot<br/>v3.0-preview]
    style APIM fill:#0078d4
    style Slot1 fill:#51cf66
    style Slot2 fill:#ffd43b
    style Slot3 fill:#ff6b6b
```

</div>

</v-click>

<!--
METADATA:
sentence: You can run multiple versions of your application code simultaneously, and APIM routes requests to the correct backend based on your versioning scheme.
search_anchor: You can run multiple versions
-->
<v-click>

<div class="mt-8 text-center text-lg">
Run multiple versions of application code simultaneously
</div>

</v-click>

---

# Routing Based on Version

<v-click>

<div class="mt-8">

```mermaid
graph LR
    Client1[Client<br/>requests v1] --> APIM[APIM]
    Client2[Client<br/>requests v2] --> APIM
    APIM -->|Routes to| V1[Backend v1.0]
    APIM -->|Routes to| V2[Backend v2.0]
    style APIM fill:#0078d4
    style V1 fill:#51cf66
    style V2 fill:#ffd43b
```

</div>

</v-click>

<!--
METADATA:
sentence: You can run multiple versions of your application code simultaneously, and APIM routes requests to the correct backend based on your versioning scheme.
search_anchor: You can run multiple versions
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
APIM routes to correct backend based on version
</div>

</v-click>

---

# Tremendous Flexibility

<!--
METADATA:
sentence: You can test new versions in isolation, perform blue-green deployments, and gradually migrate traffic between versions.
search_anchor: You can test new versions
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-test-tool class="text-4xl text-blue-400" />
  <span class="text-lg">Test new versions in isolation</span>
</div>

</v-click>

<!--
METADATA:
sentence: You can test new versions in isolation, perform blue-green deployments, and gradually migrate traffic between versions.
search_anchor: You can test new versions
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-green-400" />
  <span class="text-lg">Perform blue-green deployments</span>
</div>

</v-click>

<!--
METADATA:
sentence: You can test new versions in isolation, perform blue-green deployments, and gradually migrate traffic between versions.
search_anchor: You can test new versions
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-4 class="text-4xl text-purple-400" />
  <span class="text-lg">Gradually migrate traffic between versions</span>
</div>

</v-click>

<!--
METADATA:
sentence: They use defaults if the new parameters aren't provided.
search_anchor: They use defaults if the
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-rollback class="text-4xl text-orange-400" />
  <span class="text-lg">Quick rollback if issues arise</span>
</div>

</v-click>

---
layout: section
---

# What We'll Build

---

# Random Number Generator API

<!--
METADATA:
sentence: What We'll Build We're going to work with a Random Number Generator API.
search_anchor: What We'll Build We're going
-->
<v-click>

<div class="mt-8 text-center text-xl">
Start with v1.0
</div>

</v-click>

<v-click>

<div class="mt-8">

```mermaid
graph TB
    V1[v1.0<br/>Basic RNG] --> V1.1[v1.1<br/>Add Optional Params]
    V1.1 --> V2[v2.0<br/>Mandatory Params]
    style V1 fill:#51cf66
    style V1.1 fill:#51cf66
    style V2 fill:#ff6b6b
```

</div>

</v-click>

---

# Lab Steps

<!--
METADATA:
sentence: What We'll Build We're going to work with a Random Number Generator API.
search_anchor: What We'll Build We're going
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-version class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Create v1.0 of Random Number API</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Think of adding optional parameters to an existing operation.
search_anchor: Think of adding optional parameters
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-renew class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Add revision v1.1 with optional parameters</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Versions are for breaking changes.
search_anchor: Versions are for breaking changes
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-red-400 mt-1">3</div>
  <div>
    <carbon-version class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Publish v2.0 with breaking changes</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Versions are for breaking changes.
search_anchor: Versions are for breaking changes
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">4</div>
  <div>
    <carbon-deployment-pattern class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Use deployment slots for all versions</span>
  </div>
</div>

</v-click>

---

# The Outcome

<!--
METADATA:
sentence: Why API Versioning Matters APIs are meant to be explicitly defined contracts between your service and its consumers.
search_anchor: Why API Versioning Matters APIs
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Evolve APIs safely and professionally
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Safe[Safe Evolution] --> Support[Support Multiple Versions]
    Support --> Happy[Happy Clients]
    style Safe fill:#51cf66
    style Support fill:#0078d4
    style Happy fill:#ffd43b
```

</div>

</v-click>

<!--
METADATA:
sentence: Understanding Revisions vs Versions Azure API Management supports two types of changes: Revisions are for non-breaking changes.
search_anchor: Understanding Revisions vs Versions Azure
-->
<v-click>

<div class="mt-12 text-center text-xl">
Using Azure API Management
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
sentence: They use defaults if the new parameters aren't provided.
search_anchor: They use defaults if the
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: What We'll Build We're going to work with a Random Number Generator API.
search_anchor: What We'll Build We're going
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Build our versioned Random Number API
</div>

</v-click>

</div>
