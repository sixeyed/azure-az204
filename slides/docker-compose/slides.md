---
theme: default
layout: cover
---

# Docker Compose

<div class="abs-bottom-4">
  <iconify-icon icon="logos:docker-icon" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lesson on Docker Compose

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Docker Compose?

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

Docker Compose is two things: first, it's a specification for describing distributed applications that run in containers. Second, it's a command-line ...

</div>

---

---
layout: center
---

# Why Use Docker Compose?

<div class="text-xl mt-8" v-click>

You might be wondering - why not just use docker run commands? Well, there are several compelling reasons.

</div>

---

---
layout: center
---

# The Compose Specification

<div class="text-xl mt-8" v-click>

Docker Compose files are written in YAML format. A typical Compose file defines several key elements:

</div>

---

---
layout: center
---

# CLI Tools

<div class="text-xl mt-8" v-click>

There are actually two versions of the Docker Compose CLI you might encounter.

</div>

---

---
layout: center
---

# When to Use Docker Compose

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> Development environments where you need to run multiple services locally
</div>

<div v-click>
<iconify-icon icon="mdi:cog" /> Testing multi-container applications
</div>

<div v-click>
<iconify-icon icon="mdi:code-braces" /> Defining application architecture that will later be deployed to orchestrators like Kubernetes or Azure Container Instances
</div>

<div v-click>
<iconify-icon icon="mdi:test-tube" /> Small production deployments where you don't need full orchestration
</div>

</div>

---

---
layout: center
---

# Looking Ahead

<div class="text-xl mt-8" v-click>

In the exercises that follow, we'll start simple with a single Nginx container in Compose, then move on to a multi-container distributed application. We'll see how to debug connectivity issues, update

</div>