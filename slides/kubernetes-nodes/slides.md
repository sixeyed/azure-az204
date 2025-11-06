---
theme: default
layout: cover
---

# Kubernetes Nodes

<div class="abs-bottom-4">
  <iconify-icon icon="logos:kubernetes" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Kubernetes Nodes - Introduction Script

<div class="text-xl mt-8" v-click>

**Duration:** 2-3 minutes
**Target:** AZ-204 exam candidates

</div>

---

---
layout: center
---

# Slide 1: Title Slide

<div class="text-xl mt-8" v-click>

Welcome back! In this lesson, we're diving into Kubernetes Nodes - the fundamental building blocks of your cluster infrastructure. Understanding nodes is essential for the AZ-204 exam, especially when

</div>

---

---
layout: center
---

# Slide 2: What Are Kubernetes Nodes?

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

So, what exactly is a node? In Kubernetes, a node is simply a worker machine - it could be a virtual machine or a physical server. Nodes are where you...

</div>

---

---
layout: two-cols
---

# Slide 3: Node Architecture

<div v-click>

```mermaid
graph TB
    User[Your Application] --> Azure[Azure Platform]
    Azure --> Compute[Compute]
    Azure --> Network[Network]
    Azure --> Storage[Storage]
    Azure --> Security[Security]

    style User fill:#e3f2fd,stroke:#2196f3
    style Azure fill:#0078d4,stroke:#fff,color:#fff
    style Compute fill:#4caf50,stroke:#fff,color:#fff
    style Network fill:#ff9800,stroke:#fff,color:#fff
    style Storage fill:#9c27b0,stroke:#fff,color:#fff
    style Security fill:#e91e63,stroke:#fff,color:#fff
```

</div>

::right::

<div class="mt-8">

<div v-click>
<h3>Azure Manages</h3>
<ul>

</ul>
</div>

<div v-click class="mt-4">
<h3>You Control</h3>
<ul>

</ul>
</div>

</div>

---

---
layout: center
---

# Slide 4: Node Pools in AKS

<div class="text-xl mt-8" v-click>

When working with Azure Kubernetes Service, you'll encounter node pools. A node pool is a group of nodes within a cluster that all have the same configuration.

</div>

---

---
layout: center
---

# Slide 5: Node Capacity and Resources

<div class="text-xl mt-8" v-click>

Every node has a certain capacity - CPU cores, memory, and storage. Kubernetes tracks these resources carefully. When you request resources for your pods, Kubernetes uses this information to decide wh

</div>

---

---
layout: center
---

# Slide 6: AZ-204 Exam Relevance

<div class="text-xl mt-8" v-click>

For the AZ-204 exam, you need to know how to:
- Inspect and query node information using kubectl
- Understand node capacity and resource allocation
- Work with node labels and selectors
- Troubleshoot

</div>

---

---
layout: center
---

# Slide 7: Tools We'll Use

<div class="text-xl mt-8" v-click>

The primary tool for working with nodes is kubectl - the Kubernetes command-line interface. Throughout this lesson, you'll learn essential kubectl commands like:
- kubectl get nodes - to list nodes
- 

</div>

---

---
layout: center
---

# Slide 8: What's Next

<div class="text-xl mt-8" v-click>

In the exercises that follow, we'll get hands-on with kubectl. You'll learn how to examine nodes, query their properties, and extract specific information using different output formats.

</div>