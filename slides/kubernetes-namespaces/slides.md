---
theme: default
layout: cover
---

# Kubernetes Namespaces

<div class="abs-bottom-4">
  <iconify-icon icon="logos:kubernetes" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# SLIDE 1: Title Slide

<div class="text-xl mt-8" v-click>

**[ON SCREEN: "Kubernetes Namespaces: Isolating Workloads"]**

</div>

---

---
layout: center
---

# SLIDE 2: What Are Namespaces?

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

**[ON SCREEN: Diagram showing a Kubernetes cluster divided into separate namespace sections]**...

</div>

---

---
layout: center
---

# SLIDE 3: Use Cases & Scenarios

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> 
</div>

</div>

---

---
layout: two-cols
---

# SLIDE 4: Resource Isolation Benefits

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> [ON SCREEN: Bullet points appearing one by one]: Why does this matter? Namespaces give you three major benefits:
</div>

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>

---

---
layout: center
---

# SLIDE 5: Multi-Tenancy

<div class="text-xl mt-8" v-click>

**[ON SCREEN: Diagram showing multiple teams sharing one cluster safely]**

</div>

---

---
layout: center
---

# SLIDE 6: AZ-204 Relevance

<div class="text-xl mt-8" v-click>

**[ON SCREEN: AZ-204 exam topics highlighted]**

</div>

---

---
layout: center
---

# SLIDE 7: What We'll Cover Today

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> on lab, we're going to explore:
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> --
</div>

</div>

---

---
layout: center
---

# SLIDE 8: Important Considerations

<div class="text-xl mt-8" v-click>

**[ON SCREEN: Key points with icons]**

</div>

---

---
layout: center
---

# SLIDE 9: Let's Get Started

<div class="text-xl mt-8" v-click>

**[ON SCREEN: Terminal window ready to go]**

</div>