---
theme: default
layout: cover
---

# Azure Front Door

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

Welcome to this lab on Azure Front Door

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Azure Front Door?

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

Azure Front Door is Microsoft's modern cloud CDN that provides fast, reliable, and secure access to your applications. Think of it as Application Gate...

</div>

---

---
layout: center
---

# Key Features

<div class="text-xl mt-8" v-click>

Front Door brings together several critical capabilities:

</div>

---

---
layout: center
---

# Evolution of Azure Services

<div class="text-xl mt-8" v-click>

Front Door represents the evolution of various Azure load balancing and CDN services. It combines the best features of Traffic Manager, Content Delivery Network, and Application Gateway into a single,

</div>

---

---
layout: center
---

# Use Cases

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> Global load balancing across multiple regions
</div>

<div v-click>
<iconify-icon icon="mdi:cog" /> CDN capabilities for static content
</div>

<div v-click>
<iconify-icon icon="mdi:code-braces" /> Web application firewall protection
</div>

<div v-click>
<iconify-icon icon="mdi:test-tube" /> SSL offloading and certificate management
</div>

<div v-click>
<iconify-icon icon="mdi:lightning-bolt" /> Advanced routing based on URL paths or headers
</div>

</div>

---

---
layout: center
---

# Lab Overview

<div class="text-xl mt-8" v-click>

In this lab, we'll create and configure Azure Front Door with Web Application Firewall. We'll deploy backend applications in multiple regions, configure Front Door to route traffic between them, and a

</div>