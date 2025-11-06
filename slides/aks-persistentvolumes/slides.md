---
theme: default
layout: cover
---

# Kubernetes Storage

<div class="abs-bottom-4">
  <iconify-icon icon="logos:kubernetes" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Kubernetes Storage - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this lab on Kubernetes Storage in Azure Kubernetes Service. In this session, we'll explore how to manage persistent storage for your containerized applications running in AKS.

</div>

---

---
layout: center
---

# What We'll Cover

<div v-click>

```mermaid
graph LR
    A[these are storage units that y]
    B[only files. This is perfect fo]
    C[they can be replaced at any ti]
    A --> B
    B --> C

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

# Storage Concepts in Kubernetes

<div class="text-xl mt-8" v-click>

We'll be working with several storage concepts in this lab:

</div>

---

---
layout: center
---

# The Demo Application

<div class="text-xl mt-8" v-click>

For this lab, we'll be using a simple .NET 6.0 background worker application. This app reads configuration from files and writes data to various locations. It's perfect for demonstrating different sto

</div>

---

---
layout: center
---

# Environment Setup

<div class="text-xl mt-8" v-click>

We'll start by working with a local Kubernetes cluster running in Docker Desktop. This gives us a fast iteration cycle for learning the concepts. Then we'll move to an Azure Kubernetes Service cluster

</div>