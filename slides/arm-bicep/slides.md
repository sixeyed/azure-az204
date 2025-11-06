---
theme: default
layout: cover
---

# ARM Templates with Bicep

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

Welcome to this lab on ARM Templates with Bicep

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What Are ARM Templates?

<div v-click>

```mermaid
graph LR
    A[Your Application] --> B[Package as Container]
    B --> C[Deploy to Azure]
    C --> D[Running in Cloud]

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
```

</div>

<div class="mt-8 text-center" v-click>

ARM templates represent an important evolution in cloud infrastructure management. The concepts behind them - infrastructure as code, parameterized de...

</div>

---

---
layout: center
---

# Enter Bicep

<div class="text-xl mt-8" v-click>

This is where Bicep comes in. Bicep is the evolution of ARM templates - a new tool that uses a custom domain-specific language to define Azure resources in a simpler and more manageable way.

</div>

---

---
layout: two-cols
---

# Key Advantages of Bicep

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> There are several advantages to using Bicep over traditional ARM JSON templates:
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> First, the syntax is cleaner
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Second, parameters and variables have simple, readable names like "location" and "storageSku" - no complex bracket notation required
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Third, and this is important, templates can include comments
</div>

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>

---

---
layout: center
---

# Deployment Workflow

<div class="text-xl mt-8" v-click>

Here's the great news about Bicep: you don't need any additional tools to deploy Bicep files. The Azure CLI and PowerShell modules understand Bicep natively.

</div>

---

---
layout: center
---

# Bicep Tools

<div class="text-xl mt-8" v-click>

Bicep includes powerful tooling that bridges the gap between old and new. With the Bicep CLI, you can:

</div>

---

---
layout: center
---

# Why This Matters

<div class="text-xl mt-8" v-click>

Bicep is now the preferred way of using ARM. While JSON templates are still supported and many existing projects use them, Microsoft is investing heavily in Bicep as the future of Azure infrastructure

</div>