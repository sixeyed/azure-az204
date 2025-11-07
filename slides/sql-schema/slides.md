---
theme: default
background: https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Deploying Database Schemas
  Working with existing database structures - AZ-204
drawings:
  persist: false
transition: slide-left
title: SQL Schema
mdc: true
---

# Deploying Database Schemas

Working with Existing Database Structures

<div class="abs-bottom-10 left-10">
  <carbon-data-base class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Deploy existing database schemas to Azure<br/>Using Microsoft's data tier application packages
</div>

</v-click>

---
layout: section
---

# The Problem

---

# Empty Database Challenge

<v-click>

<div class="mt-4">
  <carbon-warning class="text-6xl text-orange-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Azure SQL Database starts empty
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Fine if using ORM like Entity Framework
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Creates its own schema automatically
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
But what about existing databases?
</div>

</v-click>

---

# Real-World Scenarios

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-enterprise class="text-4xl text-blue-400" />
  <span class="text-lg">Legacy applications</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-base class="text-4xl text-green-400" />
  <span class="text-lg">Database designed outside application code</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-upload class="text-4xl text-purple-400" />
  <span class="text-lg">Migrating from on-premises SQL Server</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-package class="text-4xl text-orange-400" />
  <span class="text-lg">Packaged application with own database</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Need to deploy pre-existing schema
</div>

</v-click>

---
layout: section
---

# The Solution

---

# Package and Deploy

<v-click>

<div class="mt-4">
  <carbon-package class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Microsoft provides packaging format
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Schema[Database Schema<br/>+ Data] --> Package[Package File]
    Package --> Upload[Upload to Azure]
    Upload --> Deploy[Deploy to<br/>Azure SQL]
    Deploy --> Ready[Ready for<br/>Application]
    style Schema fill:#ffd43b
    style Package fill:#51cf66
    style Upload fill:#0078d4
    style Deploy fill:#0078d4
    style Ready fill:#51cf66
```

</div>

</v-click>

---
layout: section
---

# Key Concepts

---

# Two File Formats

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-document-multiple class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Bacpac Files</span>
    <div class="text-sm mt-2 opacity-70">Schema AND data together</div>
    <div class="text-sm opacity-70">Complete backup - structure + content</div>
    <div class="text-sm mt-2 text-green-400">Export and import entire database</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-document-blank class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Dacpac Files</span>
    <div class="text-sm mt-2 opacity-70">Schema only - no data</div>
    <div class="text-sm opacity-70">Tables, procedures, views, objects</div>
    <div class="text-sm mt-2 text-green-400">Deploy structure, app populates data</div>
  </div>
</div>

</v-click>

---

# Choose the Right Format

<v-click>

<div class="mt-12 flex justify-center gap-16">
  <div class="text-center">
    <carbon-document-multiple class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Bacpac</div>
    <div class="text-xs mt-2 opacity-70">Schema + Data</div>
    <div class="text-xs mt-1 text-green-400">Complete migration</div>
  </div>
  <div class="text-center">
    <carbon-document-blank class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Dacpac</div>
    <div class="text-xs mt-2 opacity-70">Schema Only</div>
    <div class="text-xs mt-1 text-green-400">Fresh deployment</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What We'll Build

---

# Lab Scenario

<v-click>

<div class="mt-8 text-center text-xl">
Deploy existing Bacpac file to Azure SQL Database
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg">
Simple assets management database
</div>

</v-click>

<v-click>

<div class="mt-8 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-location class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Locations</div>
  </div>
  <div class="text-center">
    <carbon-category class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Asset Types</div>
  </div>
  <div class="text-center">
    <carbon-document class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Assets</div>
  </div>
</div>

</v-click>

---

# Lab Steps

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-server class="text-4xl text-blue-400" />
  <span class="text-lg">Create Azure SQL Server</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-upload class="text-4xl text-green-400" />
  <span class="text-lg">Upload Bacpac to Azure Storage</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-purple-400" />
  <span class="text-lg">Import schema and data to new database</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark-outline class="text-4xl text-orange-400" />
  <span class="text-lg">Verify deployment by querying data</span>
</div>

</v-click>

---
layout: section
---

# Why This Matters

---

# Critical Skill

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Migrating existing databases to Azure
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-enterprise class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Legacy Systems</div>
  </div>
  <div class="text-center">
    <carbon-package class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Packaged Apps</div>
  </div>
  <div class="text-center">
    <carbon-cloud-upload class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Cloud Migration</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Essential for cloud developers
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
Deploy existing databases to Azure
</div>

</v-click>

</div>
