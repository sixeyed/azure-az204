---
theme: default
layout: cover
---

# Azure Container Instances

<div class="abs-bottom-4">
  <iconify-icon icon="logos:docker-icon" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to the Azure Container Instances lab

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Azure Container Instances?

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

Azure Container Instances, or ACI, is a managed container service that lets you run Docker containers in Azure without managing any virtual machines o...

</div>

---

---
layout: two-cols
---

# Key Benefits

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Portability: Your Docker containers run the same way everywhere. If it works in Docker Deskto
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Simplicity: Unlike Azure Kubernetes Service or Azure App Service, ACI has minimal configurat
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Speed: ACI containers start in seconds. This makes it perfect for burst workloads, task
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Cost-effectiveness: You pay per second for exactly what you use. No idle virtual machines consuming 
</div>

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>

---

---
layout: center
---

# When to Use ACI

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> Simple web applications: Single container apps that don't need complex orchestration
</div>

<div v-click>
<iconify-icon icon="mdi:cog" /> Batch processing: Run tasks on-demand and tear them down when complete
</div>

<div v-click>
<iconify-icon icon="mdi:code-braces" /> Build agents: Temporary CI/CD build environments
</div>

<div v-click>
<iconify-icon icon="mdi:test-tube" /> Development and testing: Quick environment spin-up without infrastructure overhead
</div>

<div v-click>
<iconify-icon icon="mdi:lightning-bolt" /> Event-driven applications: Combined with Azure Functions or Logic Apps for responsive w
</div>

</div>

---

---
layout: center
---

# What We'll Cover

<div v-click>

```mermaid
graph LR
    A[Explore ACI capabilities]
    B[Deploy containers]
    C[Manage running containers]
    D[Use Docker CLI integration]
    E[Work with different container ]
    A --> B
    B --> C
    C --> D
    D --> E

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
    style E fill:#fce4ec,stroke:#e91e63
```

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
<li>The underlying compute infrastructure</li><li>Network configuration and DNS</li><li>Storage for container logs</li>
</ul>
</div>

<div v-click class="mt-4">
<h3>You Control</h3>
<ul>
<li>The container image to run</li><li>CPU and memory allocation</li><li>Network ports to expose</li>
</ul>
</div>

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">Container Registry</h3>
<p class="text-sm">Where your container images are stored. This could be Docker Hub (public), Azure Container Registry </p>
</div>

<div v-click>
<h3 class="text-xl font-bold">DNS Name Label</h3>
<p class="text-sm">ACI provides automatic DNS naming. You can assign a friendly DNS prefix and ACI creates a full domai</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Resource Allocation</h3>
<p class="text-sm">You specify exactly how much CPU and memory your container needs, with granular control from fractio</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Networking</h3>
<p class="text-sm">Containers can expose ports to the internet or remain private. ACI handles all the underlying networ</p>
</div>

</div>

---

---
layout: center
class: text-center
---

# Prerequisites

<div class="mt-12">

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Azure CLI installed and configured
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Docker Desktop installed (for Docker integration exercises)
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> An active Azure subscription
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Basic familiarity with Docker and containers
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>