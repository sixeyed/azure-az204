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

<!--
METADATA:
sentence: --- What is Azure Blob Storage?
search_anchor: --- What is Azure Blob
-->
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

<!--
METADATA:
sentence: Think of it as a massively scalable cloud-based file storage system - similar to Dropbox, but designed specifically for applications.
search_anchor: Think of it as a
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Massively scalable cloud-based file storage
</div>

</v-click>

<!--
METADATA:
sentence: Think of it as a massively scalable cloud-based file storage system - similar to Dropbox, but designed specifically for applications.
search_anchor: Think of it as a
-->
<v-click>

<div class="mt-12 text-center text-xl">
Similar to Dropbox
</div>

</v-click>

<!--
METADATA:
sentence: Think of it as a massively scalable cloud-based file storage system - similar to Dropbox, but designed specifically for applications.
search_anchor: Think of it as a
-->
<v-click>

<div class="mt-8 text-center text-xl">
But designed specifically for applications
</div>

</v-click>

---

# Storage Backend for Apps

<!--
METADATA:
sentence: While you could use Blob Storage for personal file storage, its real power comes from being a storage backend for your applications.
search_anchor: While you could use Blob
-->
<v-click>

<div class="mt-12 text-center text-xl">
Could use for personal file storage
</div>

</v-click>

<!--
METADATA:
sentence: Third, application data and logs.
search_anchor: Third, application data and logs
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Real power: application storage backend
</div>

</v-click>

<!--
METADATA:
sentence: When your users need to upload files - whether that's images, documents, videos, or any other type of file - Blob Storage is the answer.
search_anchor: When your users need to
-->
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

<!--
METADATA:
sentence: Append blobs are optimized for append operations, making them perfect for logs.
search_anchor: Append blobs are optimized for
-->
<v-click>

<div class="mt-8 text-center text-xl text-red-400">
Databases not optimized for large binary files
</div>

</v-click>

<!--
METADATA:
sentence: --- Why Not Use a Database?
search_anchor: --- Why Not Use a
-->
<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-warning class="text-4xl text-red-400" />
  <span class="text-lg">Bloat database size</span>
</div>

</v-click>

<!--
METADATA:
sentence: Storing files in a relational database can quickly bloat your database size, slow down queries, and increase costs significantly.
search_anchor: Storing files in a relational
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-4xl text-red-400" />
  <span class="text-lg">Slow down queries</span>
</div>

</v-click>

<!--
METADATA:
sentence: Storing files in a relational database can quickly bloat your database size, slow down queries, and increase costs significantly.
search_anchor: Storing files in a relational
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-4xl text-red-400" />
  <span class="text-lg">Increase costs significantly</span>
</div>

</v-click>

<!--
METADATA:
sentence: --- What is Azure Blob Storage?
search_anchor: --- What is Azure Blob
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Blob Storage is purpose-built for files
</div>

</v-click>

---

# Optimized for Files

<!--
METADATA:
sentence: --- Why Not Use a Database?
search_anchor: --- Why Not Use a
-->
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

<!--
METADATA:
sentence: When users upload profile pictures, documents, or videos to your application, those files should go into Blob Storage.
search_anchor: When users upload profile pictures
-->
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

<!--
METADATA:
sentence: Second, static website hosting.
search_anchor: Second, static website hosting
-->
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

<!--
METADATA:
sentence: Third, application data and logs.
search_anchor: Third, application data and logs
-->
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

<!--
METADATA:
sentence: Serve video and audio files directly to browsers or media players.
search_anchor: Serve video and audio files
-->
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

<!--
METADATA:
sentence: Block blobs are the most common - these are for text and binary data.
search_anchor: Block blobs are the most
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-document class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Block Blobs</div>
    <div class="text-sm mt-2 opacity-70">Most common - text and binary data</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Append blobs are optimized for append operations, making them perfect for logs.
search_anchor: Append blobs are optimized for
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-add class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Append Blobs</div>
    <div class="text-sm mt-2 opacity-70">Optimized for append operations - perfect for logs</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Page blobs are designed for random read and write operations, which is why they're used for virtual hard disk files.
search_anchor: Page blobs are designed for
-->
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

<!--
METADATA:
sentence: The Hot tier is for frequently accessed data - it's fast but more expensive for storage.
search_anchor: Hot tier is for frequently
-->
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

<!--
METADATA:
sentence: The Cool tier is for data you access infrequently, stored for at least 30 days - it costs less to store but more to access.
search_anchor: Cool tier is for data
-->
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

<!--
METADATA:
sentence: The Archive tier is for data you rarely access, stored for at least 180 days - this is the cheapest option, but accessing archived data can take hours.
search_anchor: Archive tier is for data
-->
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

<!--
METADATA:
sentence: You can use Shared Access Signatures, or SAS tokens, to provide time-limited access to specific blobs without sharing your storage account keys.
search_anchor: You can use Shared Access
-->
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

<!--
METADATA:
sentence: Stored access policies give you even more control by allowing you to revoke access tokens.
search_anchor: Stored access policies give you
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-document-tasks class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Stored Access Policies</div>
    <div class="text-sm mt-2 opacity-70">More control, can revoke access tokens</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: And Azure AD integration provides enterprise-grade identity-based access control.
search_anchor: Azure AD integration provides enterprise-grade
-->
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

<!--
METADATA:
sentence: Third, application data and logs.
search_anchor: Third, application data and logs
-->
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

<!--
METADATA:
sentence: This is crucial for cost optimization.
search_anchor: This is crucial for cost
-->
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

<!--
METADATA:
sentence: Third, application data and logs.
search_anchor: Third, application data and logs
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create storage accounts and containers</span>
</div>

</v-click>

<!--
METADATA:
sentence: Serve video and audio files directly to browsers or media players.
search_anchor: Serve video and audio files
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-upload class="text-4xl text-green-400" />
  <span class="text-lg">Upload files in bulk</span>
</div>

</v-click>

<!--
METADATA:
sentence: Third, application data and logs.
search_anchor: Third, application data and logs
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-password class="text-4xl text-purple-400" />
  <span class="text-lg">Generate and manage SAS tokens</span>
</div>

</v-click>

<!--
METADATA:
sentence: Azure offers three access tiers.
search_anchor: Azure offers three access tiers
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document-tasks class="text-4xl text-orange-400" />
  <span class="text-lg">Work with stored access policies</span>
</div>

</v-click>

<!--
METADATA:
sentence: Azure offers three access tiers.
search_anchor: Azure offers three access tiers
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-temperature class="text-4xl text-red-400" />
  <span class="text-lg">Experiment with access tiers</span>
</div>

</v-click>

---

# Advanced Topics

<!--
METADATA:
sentence: The exam-focused content will dive deeper into metadata management, lifecycle policies, blob versioning, and static website hosting - all topics that frequently appear on the AZ-204 exam.
search_anchor: exam-focused content will dive deeper
-->
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

<!--
METADATA:
sentence: Second, static website hosting.
search_anchor: Second, static website hosting
-->
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

<!--
METADATA:
sentence: --- Why Not Use a Database?
search_anchor: --- Why Not Use a
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
15-20% of total exam
</div>

</v-click>

<!--
METADATA:
sentence: --- What is Azure Blob Storage?
search_anchor: --- What is Azure Blob
-->
<v-click>

<div class="mt-8 text-center text-xl">
"Develop for Azure Storage" domain
</div>

</v-click>

<!--
METADATA:
sentence: Azure offers three access tiers.
search_anchor: Azure offers three access tiers
-->
<v-click>

<div class="mt-12 text-center text-xl">
Frequent exam questions about:
</div>

</v-click>

<!--
METADATA:
sentence: You'll see questions about when to use which blob type, how to implement lifecycle policies, how to secure blob access with SAS tokens, and how to optimize costs with access tiers.
search_anchor: You'll see questions about when
-->
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

<!--
METADATA:
sentence: Almost every cloud application needs to handle file storage at some point, and Blob Storage is Azure's answer to that need.
search_anchor: Almost every cloud application needs
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Almost every cloud application needs file storage
</div>

</v-click>

<!--
METADATA:
sentence: --- What is Azure Blob Storage?
search_anchor: --- What is Azure Blob
-->
<v-click>

<div class="mt-12 text-center text-2xl">
Blob Storage is Azure's answer
</div>

</v-click>

<!--
METADATA:
sentence: More importantly, understanding Blob Storage is fundamental to building real-world Azure solutions.
search_anchor: More importantly, understanding Blob Storage
-->
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

<!--
METADATA:
sentence: Let's get started with Azure Blob Storage!
search_anchor: Let's get started with Azure
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: --- What is Azure Blob Storage?
search_anchor: --- What is Azure Blob
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Master Azure Blob Storage
</div>

</v-click>

</div>
