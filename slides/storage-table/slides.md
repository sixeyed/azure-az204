---
theme: default
layout: cover
---

# Azure Table Storage

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

Welcome to this module on Azure Table Storage

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Azure Table Storage?

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

Azure Table Storage is a simple, scalable NoSQL database service that you can host in an Azure Storage Account. Unlike traditional relational database...

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">entities</h3>
<p class="text-sm">. Think of entities as your data items, similar to rows in a SQL database or documents in MongoDB.</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">partition key</h3>
<p class="text-sm">. This is part of the entity's unique identifier. It's a grouping mechanism that Azure uses to deter</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">row key</h3>
<p class="text-sm">. This is the unique part of the entity's identifier. Together, the partition key and row key form a</p>
</div>

</div>

---

---
layout: center
---

# Flexibility and Schema Design

<div class="text-xl mt-8" v-click>

One of Table Storage's interesting characteristics is its schema flexibility. Unlike SQL databases with rigid schemas, Table Storage entities can have different properties. You can have:

</div>

---

---
layout: center
---

# When to Use Table Storage

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> Simple, fast access to large amounts of structured data
</div>

<div v-click>
<iconify-icon icon="mdi:cog" /> A cost-effective storage solution for semi-structured data
</div>

<div v-click>
<iconify-icon icon="mdi:code-braces" /> High availability and durability without complex setup
</div>

<div v-click>
<iconify-icon icon="mdi:test-tube" /> Integration with existing Azure services and workflows
</div>

</div>

---

---
layout: center
---

# Module Overview

<div class="text-xl mt-8" v-click>

In this module, we'll work through practical examples of:

</div>