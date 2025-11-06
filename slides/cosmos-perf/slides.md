---
theme: default
layout: cover
---

# Cosmos DB Performance Provisioning

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

Welcome to this lab on Cosmos DB Performance Provisioning

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Cosmos DB Pricing?

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

Cosmos DB charges you for two main things: storage and compute....

</div>

---

---
layout: center
---

# Provisioning Models

<div class="text-xl mt-8" v-click>

You have two main options for how you pay for these Request Units:

</div>

---

---
layout: center
---

# Why This Matters

<div class="text-xl mt-8" v-click>

Cost is often cited as a concern when considering Cosmos DB. But here's the truth - if you plan appropriately and understand how RUs work, Cosmos DB can actually be very cost-effective. The key is kno

</div>

---

---
layout: center
---

# What You'll Learn

<div v-click>

```mermaid
graph LR
    A[Create a Cosmos DB account and]
    B[Understand how Request Units a]
    C[Measure RU consumption for dif]
    D[See how data modeling choices ]
    E[Use techniques like point read]
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

---

---
layout: center
---

# The Lab Scenario

<div class="text-xl mt-8" v-click>

We'll be working with a shop database containing product information. You'll create containers with different configurations, load data in different formats, and run queries to see exactly how many Re

</div>