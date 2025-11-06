---
theme: default
layout: cover
---

# AKS with KeyVault Secret Storage

<div class="abs-bottom-4">
  <iconify-icon icon="logos:kubernetes" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lab on integrating Azure Kubernetes Service with Azure Key Vault for secure secret storage

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is the Container Storage Interface?

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

Kubernetes has a powerful, pluggable storage architecture called the Container Storage Interface, or CSI. This architecture allows different types of ...

</div>

---

---
layout: center
---

# KeyVault as a Storage Provider

<div class="text-xl mt-8" v-click>

Azure Kubernetes Service includes an add-on that enables Azure Key Vault as a storage provider through the Secrets Store CSI Driver. This is a game-changer for security and configuration management.

</div>

---

---
layout: center
---

# Why This Matters

<div class="text-xl mt-8" v-click>

Traditional approaches to secrets management in Kubernetes involve storing secrets as Kubernetes Secret objects. While these are base64 encoded, they're still stored in the cluster's etcd database.

</div>

---

---
layout: center
---

# What We'll Cover

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> on enabled
</div>

</div>

---

---
layout: center
---

# Use Cases

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> Share secrets across multiple clusters or applications
</div>

<div v-click>
<iconify-icon icon="mdi:cog" /> Comply with security requirements that mandate centralized secret storage
</div>

<div v-click>
<iconify-icon icon="mdi:code-braces" /> Rotate secrets without redeploying your applications
</div>

<div v-click>
<iconify-icon icon="mdi:test-tube" /> Audit all access to sensitive configuration data
</div>

</div>