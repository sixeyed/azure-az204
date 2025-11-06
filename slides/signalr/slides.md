---
theme: default
layout: cover
---

# Azure SignalR Service

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-azure" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Azure SignalR Service - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this module on Azure SignalR Service. In this session, we'll explore how Azure enables real-time, two-way communication between web applications and clients.

</div>

---

---
layout: center
---

# What is SignalR?

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

SignalR is a technology designed for two-way communication over the internet. It allows web applications to push updates to browsers in real-time, sup...

</div>

---

---
layout: center
---

# The Scaling Challenge

<div class="text-xl mt-8" v-click>

Here's the problem: imagine you're running a chat application with two web servers. User A connects to Server One, and User B connects to Server Two. When User A sends a message, Server One broadcasts

</div>

---

---
layout: center
---

# Azure SignalR Service

<div class="text-xl mt-8" v-click>

Azure SignalR Service moves SignalR functionality into its own managed component. Instead of your web application dealing with client connections directly, it simply sends update notifications to the 

</div>

---

---
layout: two-cols
---

# Service Architecture

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

# Authentication Options

<div class="text-xl mt-8" v-click>

Azure SignalR Service supports multiple authentication methods. You can use connection strings with access keys for quick setup and testing. For production scenarios, you'll want to use Managed Identi

</div>

---

---
layout: center
---

# Important Distinction

<div class="text-xl mt-8" v-click>

One critical thing to understand: SignalR Service is for real-time broadcasting, not data persistence. When clients disconnect and reconnect, previous messages are not automatically restored. If your 

</div>

---

---
layout: center
---

# Use Cases

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> Real-time chat applications
</div>

<div v-click>
<iconify-icon icon="mdi:cog" /> Live dashboards and monitoring tools
</div>

<div v-click>
<iconify-icon icon="mdi:code-braces" /> Collaborative applications
</div>

<div v-click>
<iconify-icon icon="mdi:test-tube" /> Gaming platforms
</div>

<div v-click>
<iconify-icon icon="mdi:lightning-bolt" /> IoT device telemetry displays
</div>

</div>