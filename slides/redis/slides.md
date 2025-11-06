---
theme: default
layout: cover
---

# Azure Cache for Redis

<div class="abs-bottom-4">
  <iconify-icon icon="logos:redis" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# What is Redis?

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

Welcome to this lab on Azure Cache for Redis. Let's start by understanding what Redis is and why it's valuable in cloud applications....

</div>

---

---
layout: center
---

# Common Use Cases

<div class="grid grid-cols-1 gap-4 mt-8">



</div>

---

---
layout: center
---

# Azure Cache for Redis

<div class="text-xl mt-8" v-click>

Azure Cache for Redis is a fully managed service that implements the Redis API. It's essentially a drop-in replacement for running your own Redis cluster, but without the operational overhead.

</div>

---

---
layout: center
---

# What We'll Cover

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> Using it as a data cache to improve application performance
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> Using it as a message queue for publishing and subscribing to events
</div>

</div>

---

---
layout: two-cols
---

# Key Benefits

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Performance: In-memory data storage provides sub-millisecond response times
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Simplicity: Straightforward API with simple commands
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Flexibility: Can be used for caching, messaging, or both
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Managed Service: Azure handles infrastructure, patching, and availability
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Cost-Effective: Basic tiers provide excellent value for non-critical workloads
</div>

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>