---
theme: default
layout: cover
---

# API Management

<div class="abs-bottom-4">
  <iconify-icon icon="carbon:api" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lab on Azure API Management, or APIM as we commonly call it

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is API Management?

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

So, what exactly is API Management? Think of it as a full-service solution for delivering HTTP APIs to your consumers - whether that's a public API av...

</div>

---

---
layout: center
---

# Why API Management is Powerful

<div class="text-xl mt-8" v-click>

Now, APIM is a very powerful service with lots more features beyond these core capabilities. But before we dive deep, there's something important you need to know: creating an instance of the API Mana

</div>

---

---
layout: two-cols
---

# Understanding APIM Architecture

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

# Core Concepts

<div class="text-xl mt-8" v-click>

There are three core concepts you need to understand in APIM:

</div>

---

---
layout: center
---

# APIM Service Tiers

<div class="text-xl mt-8" v-click>

Now, let's talk about the different service tiers available for API Management. Understanding these is crucial for choosing the right tier for your needs.

</div>

---

---
layout: center
---

# Backend API Deployment

<div class="text-xl mt-8" v-click>

Here's something really important to understand: APIM isn't a hosting service for your APIs. You still need to deploy your actual API logic to another service inside or outside of Azure.

</div>

---

---
layout: center
---

# The Power of Policies

<div class="text-xl mt-8" v-click>

One of the most powerful features of APIM is its policy system. Policies allow you to add inbound and outbound processing to wrap the actual logic of your API.

</div>

---

---
layout: center
---

# Developer Portal

<div class="text-xl mt-8" v-click>

The Developer Portal is another standout feature. It provides a self-service experience for your API consumers. They can browse your APIs, read documentation, sign up for access, get subscription keys

</div>

---

---
layout: center
---

# OpenAPI Integration

<div class="text-xl mt-8" v-click>

APIM has excellent support for the OpenAPI specification, formerly known as Swagger. If your backend API already publishes an OpenAPI spec, you can import it directly into APIM. This automatically cre

</div>

---

---
layout: center
---

# Production-Grade Features Out of the Box

<div class="text-xl mt-8" v-click>

Let me emphasize something important: APIM gives you production-grade features that would take weeks or months to build yourself.

</div>

---

---
layout: center
---

# Conclusion

<div class="text-xl mt-8" v-click>

In the upcoming exercises, we'll work through creating an APIM instance, deploying a backend API, importing it into APIM, configuring policies, publishing the API through the Developer Portal, and tes

</div>