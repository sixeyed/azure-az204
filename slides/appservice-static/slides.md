---
theme: default
layout: cover
---

# App Service for Static Web Apps

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-azure" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# App Service for Static Web Apps - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this lab on Azure Static Web Apps and App Service for static content.

</div>

---

---
layout: center
---

# What are Static Web Apps?

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

Azure Static Web Apps is a service designed specifically for modern web applications that consist of static content - HTML, CSS, JavaScript - and opti...

</div>

---

---
layout: center
---

# What You'll Learn

<div v-click>

```mermaid
graph LR
    A[Creating a Static Web App from]
    B[Continuous Deployment]
    C[Traditional App Service for St]
    D[Mixed Content Scenarios]
    A --> B
    B --> C
    C --> D

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
    style E fill:#fce4ec,stroke:#e91e63
```

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
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> A GitHub account (free accounts are sufficient)
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Git installed on your local machine
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# Key Differences

<div class="text-xl mt-8" v-click>

Before we begin, let's understand the key differences:

</div>