---
theme: default
layout: cover
---

# ARM Templates

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-azure" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this module on Azure Resource Manager templates, or ARM templates

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What Are ARM Templates?

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

So far in this course, we've been using the Azure CLI to create and manage resources. This is what we call an imperative approach - you tell Azure exa...

</div>

---

---
layout: center
---

# Understanding ARM Template Structure

<div class="text-xl mt-8" v-click>

Let's look at what an ARM template contains. Open the simple storage account template in your lab files. You'll see it has multiple blocks in the JSON:

</div>

---

---
layout: center
---

# The Storage Account Resource

<div class="text-xl mt-8" v-click>

Let's examine the storage account resource definition. You'll see several key elements:

</div>

---

---
layout: center
---

# Desired State Deployment

<div class="text-xl mt-8" v-click>

Here's where ARM templates really shine. When you deploy an ARM template, Azure compares what you've described in the template with what currently exists in your subscription. It then makes only the c

</div>

---

---
layout: center
---

# What's Next

<div class="text-xl mt-8" v-click>

In the exercises, we'll deploy ARM templates using the Azure CLI, explore the what-if feature to preview changes, and see how ARM templates help you identify and fix configuration drift.

</div>