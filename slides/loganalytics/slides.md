---
theme: default
layout: cover
---

# Log Analytics

<div class="abs-bottom-4">
  <iconify-icon icon="carbon:chart-line" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lab on Azure Log Analytics

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Log Analytics?

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

Log Analytics is the centralized data store for all sorts of log collection in Azure. It serves as the backbone for Azure's monitoring infrastructure....

</div>

---

---
layout: center
---

# Why KQL Matters

<div class="text-xl mt-8" v-click>

KQL is not just for interactive queries. You'll use it to:
- Power dashboards with custom visualizations
- Create intelligent alerts based on complex conditions
- Test and refine queries before using 

</div>

---

---
layout: center
---

# What We'll Cover

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> on experience with:
</div>

</div>

---

---
layout: center
---

# The Sample Application

<div class="text-xl mt-8" v-click>

We'll work with a Fulfilment Processor application that runs in Azure Container Instances. This application generates logs and metrics that flow through Application Insights into Log Analytics.

</div>

---

---
layout: center
class: text-center
---

# Prerequisites

<div class="mt-12">

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> An active Azure subscription
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Azure CLI installed and configured
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Basic understanding of Azure Monitor concepts
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Familiarity with the Azure Portal
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# Let's Get Started

<div class="text-xl mt-8" v-click>

By the end of this lab, you'll be comfortable writing KQL queries to extract insights from your application data. You'll understand how to navigate the Log Analytics interface, and you'll have created

</div>