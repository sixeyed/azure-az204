---
theme: default
layout: cover
---

# AKS Ingress and Application Gateway

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

Welcome to this lab on Ingress and Application Gateway in Azure Kubernetes Service

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# The Challenge

<div class="text-xl mt-8" v-click>

When you start running applications on Kubernetes, you quickly face a networking challenge. While you can route traffic using LoadBalancer Services that give you public IP addresses, this approach doe

</div>

---

---
layout: center
---

# The Solution

<div class="text-xl mt-8" v-click>

Instead of multiple IP addresses, you want a single entry point that routes incoming traffic based on HTTP domain names. This means a single Kubernetes cluster can serve multiple domains - like myapp.

</div>

---

---
layout: center
---

# What is Azure Application Gateway?

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

Azure Application Gateway is a web traffic load balancer that enables you to manage traffic to your web applications. It's more than just a standard l...

</div>

---

---
layout: center
---

# Application Gateway Ingress Controller

<div class="text-xl mt-8" v-click>

When you combine Application Gateway with AKS, the Application Gateway acts as an ingress controller. This means it automatically configures itself based on the Kubernetes Ingress resources you create

</div>

---

---
layout: center
---

# Lab Overview

<div class="text-xl mt-8" v-click>

In this lab, you'll:
1. Create an Azure Application Gateway with proper networking setup
2. Deploy an AKS cluster integrated with the Application Gateway
3. Use the AGIC add-on to connect them togethe

</div>