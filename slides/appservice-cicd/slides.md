---
theme: default
layout: cover
---

# App Service CI/CD

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

Welcome to this lab on Azure App Service Continuous Integration and Continuous Deployment

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is App Service CI/CD?

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

Azure App Service provides two powerful features for continuous deployment:...

</div>

---

---
layout: center
---

# Lab Overview

<div class="text-xl mt-8" v-click>

In this lab, we'll be working with a random number API. We'll:

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
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> A GitHub account with a fork of the lab repository
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Azure CLI installed and configured
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Basic understanding of Git and GitHub workflows
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# Why This Matters

<div class="text-xl mt-8" v-click>

Continuous Integration and Deployment are essential practices in modern software development. They:

</div>

---

---
layout: center
---

# Let's Get Started

<div class="text-xl mt-8" v-click>

We'll begin by setting up our Azure resources and configuring the initial deployment from GitHub. Then we'll progressively enhance our deployment pipeline with automation and staging environments.

</div>