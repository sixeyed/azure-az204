---
theme: default
layout: cover
---

# Azure Kubernetes Service

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

Welcome to this lesson on Azure Kubernetes Service, or AKS

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is AKS?

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

Kubernetes is an open-source platform for managing containerized applications. While Kubernetes itself is open-source, many vendors provide their own ...

</div>

---

---
layout: center
---

# Why Use AKS?

<div class="text-xl mt-8" v-click>

AKS simplifies many complex tasks that would otherwise require significant expertise and effort:

</div>

---

---
layout: center
---

# Key Features to Explore

<div class="text-xl mt-8" v-click>

Let's look at what you can configure when creating an AKS cluster:

</div>

---

---
layout: center
---

# Production Considerations

<div class="text-xl mt-8" v-click>

Now, it's important to understand that production-grade AKS deployments can get quite complicated. You'll need to consider networking, security policies, monitoring, and high availability. However, fo

</div>

---

---
layout: center
---

# What's Next

<div class="text-xl mt-8" v-click>

In this lesson, we'll walk through creating an AKS cluster, deploying a sample application, and exploring how Kubernetes works in the Azure environment. You'll use the same Kubernetes tools and YAML s

</div>