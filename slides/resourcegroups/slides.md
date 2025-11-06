---
theme: default
layout: cover
---

# Resource Groups

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

Welcome to this tutorial on Azure Resource Groups

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What are Resource Groups?

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

Resource Groups, or RGs, are containers for all other Azure resources. Think of them as organizational folders that hold everything your application n...

</div>

---

---
layout: two-cols
---

# Key Benefits

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> There are several important benefits to using Resource Groups:
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> First, management permissions can be applied at the Resource Group level
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Second, Resource Groups make cleanup incredibly easy
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Third, they provide a way to organize your resources logically, which becomes increasingly important as your Azure footprint grows
</div>

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>

---

---
layout: center
---

# Regions and Location

<div class="text-xl mt-8" v-click>

One important concept to understand is that Resource Groups themselves have a location - a specific Azure region. This region determines where the metadata about your Resource Group is stored.

</div>

---

---
layout: center
---

# Tags

<div class="text-xl mt-8" v-click>

Tags are simple key-value pairs that you can attach to Resource Groups and other resources. They're incredibly useful for organizing and managing resources at scale. For example, you might use an "env

</div>

---

---
layout: center
---

# What's Next

<div class="text-xl mt-8" v-click>

In this lab, we'll explore Resource Groups hands-on. We'll create them using both the Azure Portal and the Azure CLI, learn how to query and filter them, and practice managing them. By the end, you'll

</div>