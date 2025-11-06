---
theme: default
layout: cover
---

# Securing Apps with Key Vault and Virtual Networks

<div class="abs-bottom-4">
  <iconify-icon icon="carbon:network-4" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Securing Apps with Key Vault and Virtual Networks - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this lab on securing Azure applications using Key Vault and Virtual Networks. In this session, we'll explore how to build truly secure applications in Azure by combining two powerful securi

</div>

---

---
layout: center
---

# The Security Challenge

<div class="text-xl mt-8" v-click>

When building applications in Azure, we face two major security challenges. First, how do we manage credentials securely? Connection strings, API keys, and other secrets need to be stored somewhere, a

</div>

---

---
layout: center
---

# The Ideal Azure Application

<div class="text-xl mt-8" v-click>

The ideal application in Azure uses managed identities for all authentication and restricted virtual networks for all communication. This approach means there are no credentials to manage and store, a

</div>

---

---
layout: center
---

# What We'll Build

<div class="text-xl mt-8" v-click>

In this lab, we'll deploy a web application that uses Blob Storage for data persistence. The connection details for the storage account will be stored in Azure Key Vault, which we'll restrict to only 

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">Managed Identity</h3>
<p class="text-sm">An automatically managed identity in Azure Active Directory that your application can use to authent</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Virtual Networks</h3>
<p class="text-sm">Isolated networks in Azure that allow you to control network traffic between resources. You can rest</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Service Endpoints</h3>
<p class="text-sm">Enable private connectivity from your VNet to Azure services over the Azure backbone network, withou</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">VNet Integration</h3>
<p class="text-sm">Allows App Service apps to make outbound calls into your Virtual Network, enabling them to access re</p>
</div>

</div>

---

---
layout: two-cols
---

# The Architecture

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