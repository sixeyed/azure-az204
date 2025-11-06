---
theme: default
layout: cover
---

# Virtual Networks

<div class="abs-bottom-4">
  <iconify-icon icon="carbon:network-4" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lab on Azure Virtual Networks

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What are Virtual Networks?

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

Virtual Networks, or VNets as they're commonly called, are private networks in Azure. They allow your services to communicate with each other securely...

</div>

---

---
layout: center
---

# Why Virtual Networks Matter

<div class="text-xl mt-8" v-click>

Virtual Networks are a core component in deploying secure solutions in Azure. If you're building production applications, you should aim to use VNets for all your services, provided those services sup

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

# Naming Requirements

<div class="text-xl mt-8" v-click>

Here's a nice detail: unlike many Azure resources, VNet names don't need to be globally unique. They just need to be unique within the Resource Group. This gives you more flexibility in your naming co

</div>

---

---
layout: center
---

# What You'll Learn

<div v-click>

```mermaid
graph LR
    A[Explore Virtual Networks throu]
    B[Create VNets and subnets using]
    C[Deploy a Virtual Machine into ]
    D[Understand the networking reso]
    E[Learn about Azure Resource Man]
    A --> B
    B --> C
    C --> D
    D --> E

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
    style E fill:#fce4ec,stroke:#e91e63
```

</div>