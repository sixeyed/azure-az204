---
theme: default
layout: cover
---

# Azure Durable Functions: Fan-Out/Fan-In Pattern

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-azure" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Azure Durable Functions: Fan-Out/Fan-In Pattern - Introduction

<div class="text-xl mt-8" v-click>

**Duration:** 2-3 minutes
**Format:** Presentation with slides

</div>

---

---
layout: center
---

# SLIDE 1: Title Slide

<div class="text-xl mt-8" v-click>

**Visual:** Azure Durable Functions logo with "Fan-Out/Fan-In Pattern"

</div>

---

---
layout: center
---

# SLIDE 2: The Challenge of Parallel Processing

<div class="text-xl mt-8" v-click>

**Visual:** Diagram showing sequential vs. parallel processing timelines

</div>

---

---
layout: center
---

# SLIDE 3: What is Fan-Out/Fan-In?

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

**Visual:** Animation showing one orchestrator fanning out to multiple activities, then collecting results back...

</div>

---

---
layout: center
---

# SLIDE 4: Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">Visual:</h3>
<p class="text-sm">Three boxes showing Orchestrator Function, Activity Functions, and Durable Task Framework</p>
</div>

</div>

---

---
layout: center
---

# SLIDE 5: Real-World Use Cases

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> 
</div>

</div>

---

---
layout: two-cols
---

# SLIDE 6: The HTTP Orchestration Advantage

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Visual:: Diagram showing HTTP trigger returning status URLs
</div>

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>

---

---
layout: center
---

# SLIDE 7: AZ-204 Exam Focus

<div class="text-xl mt-8" v-click>

**Visual:** Checklist with exam topics highlighted

</div>

---

---
layout: center
---

# SLIDE 8: What You'll Build Today

<div class="text-xl mt-8" v-click>

**Visual:** Architecture diagram of the quote engine application

</div>

---

---
layout: center
---

# SLIDE 9: Preview of the Pattern

<div class="text-xl mt-8" v-click>

**Visual:** Code snippet showing the fan-out pattern structure

</div>

---

---
layout: center
---

# SLIDE 10: Let's Get Started

<div class="text-xl mt-8" v-click>

**Visual:** "Ready to Code" with lab exercise preview

</div>