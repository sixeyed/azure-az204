---
theme: default
layout: cover
---

# Deploying Database Schemas

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

Welcome to this lab on deploying database schemas to Azure SQL Database

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# The Problem

<div class="text-xl mt-8" v-click>

When you're working with Azure SQL Database, you often start with an empty database. That's fine if your application uses an ORM like Entity Framework that can create its own schema automatically. But

</div>

---

---
layout: center
---

# The Solution

<div class="text-xl mt-8" v-click>

Microsoft provides a packaging format specifically for this purpose. You can package your database schema - and optionally the data - into a file, upload it to Azure, and deploy it to an Azure SQL Dat

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">Bacpac files</h3>
<p class="text-sm">contain both the database schema AND the data. Think of this as a complete backup of your database -</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Dacpac files</h3>
<p class="text-sm">contain only the database schema - the table definitions, stored procedures, views, and other databa</p>
</div>

</div>

---

---
layout: center
---

# What We'll Build

<div class="text-xl mt-8" v-click>

In this lab, we'll take an existing Bacpac file and deploy it to Azure SQL Database. The file contains a simple assets management database with tables for locations, asset types, and assets.

</div>