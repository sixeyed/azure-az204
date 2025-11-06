---
theme: default
layout: cover
---

# Azure Storage Accounts

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

Welcome to this lab on Azure Storage Accounts

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What are Storage Accounts?

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

Azure Storage Accounts are a managed storage service that allows you to store data in the cloud. You have complete control over who can access your da...

</div>

---

---
layout: center
---

# What We'll Cover

<div v-click>

```mermaid
graph LR
    A[on experience with:]
    B[Creating storage accounts usin]
    C[Understanding performance and ]
    D[Working with blob containers]
    E[Managing public and private ac]
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

# Redundancy Options

<div class="text-xl mt-8" v-click>

Before we dive into the exercises, let's talk about data redundancy. Azure offers several levels of replication:

</div>

---

---
layout: center
class: text-center
---

# Getting Started

<div class="mt-12">

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> on exercises. We'll begin by exploring the options available when creating a Storage Account, then move on to creating one ourselves using the Azure CLI.
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>