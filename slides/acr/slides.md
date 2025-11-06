---
theme: default
layout: cover
---

# Azure Container Registry

<div class="abs-bottom-4">
  <iconify-icon icon="logos:docker-icon" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# What is Azure Container Registry?

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

Azure Container Registry, or ACR, is Azure's private container registry service. While open source applications are commonly published to public regis...

</div>

---

---
layout: center
---

# Why Use a Private Registry?

<div class="text-xl mt-8" v-click>

Public registries like Docker Hub are excellent for sharing open source software, but for your production applications, you need:

</div>

---

---
layout: center
---

# Key Features of ACR

<div class="text-xl mt-8" v-click>

Azure Container Registry offers several important capabilities:

</div>

---

---
layout: center
---

# Registry Naming and DNS

<div class="text-xl mt-8" v-click>

When you create an ACR instance, you choose a registry name that becomes your DNS hostname:

</div>

---

---
layout: center
---

# Understanding Container Registry Concepts

<div class="text-xl mt-8" v-click>

Before diving into the exercises, it's important to understand a few key concepts:

</div>

---

---
layout: center
---

# What You'll Learn

<div v-click>

```mermaid
graph LR
    A[Portal exploration]
    B[CLI creation]
    C[Image management]
    D[Custom builds]
    E[Portal management]
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