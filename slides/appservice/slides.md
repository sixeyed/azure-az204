---
theme: default
layout: cover
---

# App Service for Web Apps

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

Welcome to this lab on Azure App Service for Web Apps

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# Understanding PaaS vs IaaS

<div class="text-xl mt-8" v-click>

Before we dive in, let's understand the difference between Infrastructure-as-a-Service and Platform-as-a-Service.

</div>

---

---
layout: center
---

# What is Azure App Service?

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

Azure App Service is one of Azure's most popular PaaS offerings. It's a fully managed platform for building, deploying, and scaling web applications. ...

</div>

---

---
layout: center
---

# What We'll Build Today

<div class="text-xl mt-8" v-click>

In this lab, you'll create an App Service deployment by pushing source code directly from your local machine. Azure will compile and configure the application for you automatically.

</div>

---

---
layout: center
class: text-center
---

# Lab Prerequisites

<div class="mt-12">

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> An active Azure subscription
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Azure CLI installed and configured
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Git installed on your local machine
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Access to the course repository with the sample application code
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What to Expect

<div class="text-xl mt-8" v-click>

The entire deployment process will take just a few minutes. You'll see how Azure handles compilation, configuration, and deployment automatically. By the end, you'll have a live web application runnin

</div>