---
theme: default
layout: cover
---

# Application Gateway with Web Application Firewall

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

Welcome to this lab on Azure Application Gateway with Web Application Firewall

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Application Gateway?

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

Application Gateway is Azure's layer 7 load balancer. Unlike traditional load balancers that work at the network layer, Application Gateway operates a...

</div>

---

---
layout: center
---

# Web Application Firewall Overview

<div class="text-xl mt-8" v-click>

Web Application Firewall, or WAF, is an optional but powerful security feature of Application Gateway. WAF inspects both the headers and body of HTTP requests, looking for malicious payloads that coul

</div>

---

---
layout: center
---

# Lab Objectives

<div class="text-xl mt-8" v-click>

In this lab, we'll accomplish three main objectives:

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">



</div>

---

---
layout: two-cols
---

# Architecture Overview

<div v-click>

```mermaid
graph TB
    User[Your Application] --> Azure[Azure Platform]
    Azure --> Compute[Compute]
    Azure --> Network[Network]
    Azure --> Storage[Storage]
    Azure --> Security[Security]

    style User fill:#e3f2fd,stroke:#2196f3
    style Azure fill:#0078d4,stroke:#fff,color:#fff
    style Compute fill:#4caf50,stroke:#fff,color:#fff
    style Network fill:#ff9800,stroke:#fff,color:#fff
    style Storage fill:#9c27b0,stroke:#fff,color:#fff
    style Security fill:#e91e63,stroke:#fff,color:#fff
```

</div>

::right::

<div class="mt-8">

<div v-click>
<h3>Azure Manages</h3>
<ul>

</ul>
</div>

<div v-click class="mt-4">
<h3>You Control</h3>
<ul>

</ul>
</div>

</div>

---

---
layout: center
---

# What You'll Learn

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> site routing to different backend pools, how to test and validate WAF security rules, and how to troubleshoot common issues like 502 Bad Gateway errors.
</div>

</div>