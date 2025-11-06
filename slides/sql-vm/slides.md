---
theme: default
layout: cover
---

# SQL Server VMs

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-sql" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lab on SQL Server Virtual Machines in Azure

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# Why SQL Server VMs?

<div class="text-xl mt-8" v-click>

While managed SQL Server databases like Azure SQL Database and SQL Managed Instance should be your preferred choice for most scenarios, they don't support 100% of the features you get with SQL Server 

</div>

---

---
layout: center
---

# What We'll Cover

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> SQL Server 2019 Standard on Windows Server 2022 - and create our virtual machine.
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> world use case: creating a custom User-Defined Function that calls .NET code. This is a feature that isn't available with managed database options because you need direct access to the file system and elevated SQL Server permissions.
</div>

</div>

---

---
layout: center
---

# Lab Scenario

<div class="text-xl mt-8" v-click>

Throughout this lab, you'll be working with placeholder values. When you see resource names like "labs-sql-vm", locations like "westeurope", or VM names like "sql01", remember to substitute these with

</div>

---

---
layout: center
class: text-center
---

# Prerequisites

<div class="mt-12">

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Azure CLI installed and configured
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Access to an Azure subscription
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Basic familiarity with Azure Resource Groups and Virtual Machines
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Understanding of SQL Server fundamentals
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>