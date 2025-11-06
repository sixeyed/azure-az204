---
theme: default
layout: cover
---

# Securing AKS Apps with Key Vault and Virtual Networks

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

Welcome to this lab on securing Azure Kubernetes Service applications with Key Vault and Virtual Networks

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# Concept Overview

<div class="text-xl mt-8" v-click>

When running applications in AKS, security should be a primary concern. While AKS provides a managed Kubernetes environment, it's our responsibility to secure the resources our applications use - thin

</div>

---

---
layout: center
---

# Azure Network Provider for AKS

<div class="text-xl mt-8" v-click>

By default, AKS can use kubenet networking, where Pods get IP addresses from a separate address space. However, Azure also supports the Azure CNI - Container Network Interface - which allows AKS clust

</div>

---

---
layout: center
---

# Service Endpoints and Network Security

<div class="text-xl mt-8" v-click>

Many Azure services support virtual network service endpoints. This includes Key Vault and Storage Accounts. Service endpoints allow you to secure these services to only accept traffic from specific s

</div>

---

---
layout: center
---

# Managed Identities for Authentication

<div class="text-xl mt-8" v-click>

Authentication is handled through Azure Managed Identities. We've seen this pattern before in other labs, but it's especially powerful in AKS. The AKS KeyVault add-on creates a managed identity that c

</div>

---

---
layout: center
---

# The Lab Scenario

<div class="text-xl mt-8" v-click>

In today's lab, we'll deploy a sample application called Asset Manager to AKS. This application uses Azure Blob Storage to persist data. The connection string for the storage account contains sensitiv

</div>

---

---
layout: two-cols
---

# Security Benefits

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> This architecture provides multiple layers of security:
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Network isolation: Resources are only accessible from specific subnets
Identity-based access: No credentials stored in code or environment variables
Principle of least privilege: Each component has only the permissions it needs
Defense in depth: Multiple security controls protecting the same resources
</div>

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>

---

---
layout: center
---

# What You'll Learn

<div v-click>

```mermaid
graph LR
    A[Deploy an AKS cluster into a v]
    B[Configure service endpoints on]
    C[Restrict Key Vault access usin]
    D[Grant AKS managed identity acc]
    E[Deploy applications that consu]
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