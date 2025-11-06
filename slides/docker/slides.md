---
theme: default
layout: cover
---

# Docker 101

<div class="abs-bottom-4">
  <iconify-icon icon="logos:docker-icon" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to Docker 101

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# The Problem Statement

<div class="text-xl mt-8" v-click>

So let's start with a question: How would you run a .NET application on Azure?

</div>

---

---
layout: center
---

# Enter Docker

<div class="text-xl mt-8" v-click>

This is where Docker comes in.

</div>

---

---
layout: two-cols
---

# Key Benefits

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> The beauty of Docker is consistency
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Docker also makes scaling easier
</div>

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>

---

---
layout: center
---

# What We'll Cover

<div v-click>

```mermaid
graph LR
    A[Run pre-built container images]
    B[Work with different types of .]
    C[Build your own custom Docker i]
    D[Package and run your own .NET ]
    A --> B
    B --> C
    C --> D

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
    style E fill:#fce4ec,stroke:#e91e63
```

</div>

---

---
layout: center
class: text-center
---

# Getting Started

<div class="mt-12">

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> line interface, which works similarly to the Azure CLI. It has built-in help, supports various subcommands, and gives you complete control over your container environment.
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>