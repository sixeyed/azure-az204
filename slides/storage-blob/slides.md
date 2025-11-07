---
theme: default
background: https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Blob Storage
  Object storage solution for the cloud - AZ-204
drawings:
  persist: false
transition: slide-left
title: Blob Storage
mdc: true
---

# Azure Blob Storage

Object Storage for the Cloud

<div class="abs-bottom-10 left-10">
  <carbon-data-storage class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Azure Blob Storage<br/>Core topic for the AZ-204 exam
</div>

</v-click>

---
layout: section
---

# What is Azure Blob Storage?

---

# Object Storage Solution

<v-click>

<div class="mt-4">
  <carbon-data-storage class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Massively scalable cloud-based file storage
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Similar to Dropbox
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
But designed specifically for applications
</div>

</v-click>

---

# Storage Backend for Apps

<v-click>

<div class="mt-12 text-center text-xl">
Could use for personal file storage
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Real power: application storage backend
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-image class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Images</div>
  </div>
  <div class="text-center">
    <carbon-document class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Documents</div>
  </div>
  <div class="text-center">
    <carbon-video class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Videos</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Why Not Use a Database?

---

# Database Limitations

<v-click>

<div class="mt-8 text-center text-xl text-red-400">
Databases not optimized for large binary files
</div>

</v-click>

<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-warning class="text-4xl text-red-400" />
  <span class="text-lg">Bloat database size</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-4xl text-red-400" />
  <span class="text-lg">Slow down queries</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-4xl text-red-400" />
  <span class="text-lg">Increase costs significantly</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Blob Storage is purpose-built for files
</div>

</v-click>

---

# Optimized for Files

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-flash class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Efficient</div>
  </div>
  <div class="text-center">
    <carbon-piggy-bank class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Cost-Effective</div>
  </div>
  <div class="text-center">
    <carbon-scale class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Scalable</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Common Use Cases

---

# Real-World Applications

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-user class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">User-Generated Content</span>
    <div class="text-sm mt-2 opacity-70">Profile pictures, documents, videos</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-browser class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Static Website Hosting</span>
    <div class="text-sm mt-2 opacity-70">HTML, CSS, JavaScript, images</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-document class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Application Data and Logs</span>
    <div class="text-sm mt-2 opacity-70">Logs, backups, JSON reference data</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-video class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Media Streaming</span>
    <div class="text-sm mt-2 opacity-70">Serve video and audio to browsers</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Key Concepts for AZ-204

---

# Blob Types

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-document class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Block Blobs</div>
    <div class="text-sm mt-2 opacity-70">Most common - text and binary data</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-add class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Append Blobs</div>
    <div class="text-sm mt-2 opacity-70">Optimized for append operations - perfect for logs</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-data-storage class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Page Blobs</div>
    <div class="text-sm mt-2 opacity-70">Random read/write - used for virtual hard disks</div>
  </div>
</div>

</v-click>

---

# Access Tiers

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-flash class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Hot Tier</div>
    <div class="text-sm mt-2 opacity-70">Frequently accessed data</div>
    <div class="text-sm opacity-70">Fast but more expensive storage</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-temperature class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Cool Tier</div>
    <div class="text-sm mt-2 opacity-70">Infrequently accessed, stored 30+ days</div>
    <div class="text-sm opacity-70">Less storage cost, more access cost</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-archive class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Archive Tier</div>
    <div class="text-sm mt-2 opacity-70">Rarely accessed, stored 180+ days</div>
    <div class="text-sm opacity-70">Cheapest storage, hours to access</div>
  </div>
</div>

</v-click>

---

# Security and Access Control

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-password class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Shared Access Signatures (SAS)</div>
    <div class="text-sm mt-2 opacity-70">Time-limited access to specific blobs</div>
    <div class="text-sm opacity-70">No need to share storage account keys</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-document-tasks class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Stored Access Policies</div>
    <div class="text-sm mt-2 opacity-70">More control, can revoke access tokens</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-id-management class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Azure AD Integration</div>
    <div class="text-sm mt-2 opacity-70">Enterprise-grade identity-based access</div>
  </div>
</div>

</v-click>

---

# Lifecycle Management

<v-click>

<div class="mt-12 text-center text-xl">
Automate tier transitions and deletions
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Hot[Hot Tier<br/>0-30 days] --> Cool[Cool Tier<br/>30-180 days]
    Cool --> Archive[Archive Tier<br/>180+ days]
    Archive --> Delete[Delete<br/>After X days]
    style Hot fill:#ff6b6b
    style Cool fill:#ffd43b
    style Archive fill:#0078d4
    style Delete fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Crucial for cost optimization
</div>

</v-click>

---
layout: section
---

# What We'll Cover in Labs

---

# Hands-On Experience

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create storage accounts and containers</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-upload class="text-4xl text-green-400" />
  <span class="text-lg">Upload files in bulk</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-password class="text-4xl text-purple-400" />
  <span class="text-lg">Generate and manage SAS tokens</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document-tasks class="text-4xl text-orange-400" />
  <span class="text-lg">Work with stored access policies</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-temperature class="text-4xl text-red-400" />
  <span class="text-lg">Experiment with access tiers</span>
</div>

</v-click>

---

# Advanced Topics

<v-click>

<div class="mt-8 grid grid-cols-2 gap-8">
  <div class="text-center">
    <carbon-data-view-alt class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Metadata Management</div>
  </div>
  <div class="text-center">
    <carbon-renew class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Lifecycle Policies</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 grid grid-cols-2 gap-8">
  <div class="text-center">
    <carbon-version class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Blob Versioning</div>
  </div>
  <div class="text-center">
    <carbon-browser class="text-5xl text-orange-400" />
    <div class="text-sm mt-3">Static Website Hosting</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Why This Matters for AZ-204

---

# Exam Weight

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
15-20% of total exam
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
"Develop for Azure Storage" domain
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Frequent exam questions about:
</div>

</v-click>

<v-click>

<div class="mt-8 flex justify-center gap-12">
  <div class="text-center">
    <carbon-decision-tree class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Blob Type Selection</div>
  </div>
  <div class="text-center">
    <carbon-document-tasks class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Lifecycle Policies</div>
  </div>
  <div class="text-center">
    <carbon-security class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">SAS Tokens</div>
  </div>
</div>

</v-click>

---

# Fundamental Skill

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Almost every cloud application needs file storage
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl">
Blob Storage is Azure's answer
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-document class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Exam Success</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Real-World Solutions</div>
  </div>
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
Master Azure Blob Storage
</div>

</v-click>

</div>
