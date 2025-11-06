---
theme: default
layout: cover
---

# Docker Multi-Stage Builds

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

Welcome to this session on Docker Multi-Stage Builds

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What Are Multi-Stage Builds?

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

Multi-stage builds use the standard Dockerfile syntax with a key difference: they contain multiple FROM commands, each representing a separate build s...

</div>

---

---
layout: center
---

# Why Use Multi-Stage Builds?

<div class="text-xl mt-8" v-click>

You won't see multi-stage builds used everywhere, but they offer significant advantages:

</div>

---

---
layout: center
---

# The Basic Pattern

<div class="text-xl mt-8" v-click>

A typical multi-stage Dockerfile follows this pattern:

</div>

---

---
layout: center
---

# Language Support

<div class="text-xl mt-8" v-click>

Multi-stage builds work with all major programming languages. Docker Hub provides official images for:

</div>

---

---
layout: center
---

# What We'll Cover

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> stage build to understand the mechanics
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> stage builds
</div>

</div>