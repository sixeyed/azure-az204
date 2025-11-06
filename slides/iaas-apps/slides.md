---
theme: default
layout: cover
---

# IaaS Apps

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

Welcome to this lab on deploying applications using Azure Infrastructure-as-a-Service.

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What You'll Learn

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> on lab, you'll learn how to deploy traditional applications to Azure using IaaS resources. While Platform-as-a-Service solutions are often the end goal for cloud-native applications, IaaS provides a straightforward migration path for existing workloads.
</div>

</div>

---

---
layout: center
---

# Lab Scenario

<div class="text-xl mt-8" v-click>

Today, we'll be working with a legacy .NET Framework application - the kind of application many organizations still run in production. This application uses Windows Server and SQL Server, both of whic

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">



</div>

---

---
layout: center
---

# What We'll Build

<div class="text-xl mt-8" v-click>

We'll create a complete application environment including:
- A SQL Database to store application data
- A Windows Server virtual machine running the latest Windows Server 2022
- An IIS web server host

</div>

---

---
layout: center
class: text-center
---

# Prerequisites

<div class="mt-12">

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> An active Azure subscription
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Azure CLI installed and configured
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> A Remote Desktop client for connecting to Windows VMs
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Basic familiarity with PowerShell commands
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: two-cols
---

# Lab Architecture

<div v-click>

```mermaid
graph TB
    User[Your Application] --> Azure[Azure Platform]
    Azure --> Compute[Compute]
    Azure --> Network[Network]
    Azure --> Storage[Storage]
    Azure --> Security[Security]

    style User fill:#e3f2fd,stroke:#2196f3
    style Azure fill:#0078d4,stroke:#fff,color:#fff
    style Compute fill:#4caf50,stroke:#fff,color:#fff
    style Network fill:#ff9800,stroke:#fff,color:#fff
    style Storage fill:#9c27b0,stroke:#fff,color:#fff
    style Security fill:#e91e63,stroke:#fff,color:#fff
```

</div>

::right::

<div class="mt-8">

<div v-click>
<h3>Azure Manages</h3>
<ul>

</ul>
</div>

<div v-click class="mt-4">
<h3>You Control</h3>
<ul>

</ul>
</div>

</div>

---

---
layout: center
---

# Time to Complete

<div class="text-xl mt-8" v-click>

This lab typically takes about 45 minutes to complete, including resource provisioning time.

</div>