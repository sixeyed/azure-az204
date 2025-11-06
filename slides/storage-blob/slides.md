---
theme: default
layout: cover
---

# Azure Blob Storage

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-azure" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# AZ-204 Exam Preparation

<div class="text-xl mt-8" v-click>

*Duration: 2-3 minutes*

</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this session on Azure Blob Storage, one of the core topics you'll encounter on the AZ-204 exam

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Azure Blob Storage?

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

Azure Blob Storage is Microsoft's object storage solution for the cloud. Think of it as a massively scalable cloud-based file storage system - similar...

</div>

---

---
layout: center
---

# Why Not Use a Database?

<div class="text-xl mt-8" v-click>

A common question developers ask is: "Why use Blob Storage instead of storing files in my database?" The answer is simple - databases aren't optimized for large binary files. Storing files in a relati

</div>

---

---
layout: center
---

# Common Use Cases

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> 
</div>

</div>

---

---
layout: center
---

# Key Concepts for AZ-204

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">Blob Types</h3>
<p class="text-sm">Azure supports three types of blobs. Block blobs are the most common - these are for text and binary</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Access Tiers</h3>
<p class="text-sm">Not all data needs the same level of performance. Azure offers three access tiers. The Hot tier is f</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Security and Access Control</h3>
<p class="text-sm">Blob Storage offers multiple security options. You can use Shared Access Signatures, or SAS tokens, </p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Lifecycle Management</h3>
<p class="text-sm">Instead of manually managing when files move between tiers or get deleted, you can create policies t</p>
</div>

</div>

---

---
layout: center
---

# What We'll Cover in the Labs

<div v-click>

```mermaid
graph LR
    A[on experience with all of thes]
    B[focused content will dive deep]
    C[--]
    A --> B
    B --> C

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
---

# Why This Matters for AZ-204

<div class="text-xl mt-8" v-click>

Blob Storage accounts for a significant portion of the "Develop for Azure Storage" domain on the AZ-204 exam, which makes up 15 to 20 percent of the total exam. You'll see questions about when to use 

</div>

---

---
layout: center
---

# Closing

<div class="text-xl mt-8" v-click>

In the next video, we'll dive into the hands-on exercises where you'll work directly with Blob Storage using the Azure CLI. You'll create containers, upload files, work with SAS tokens, and see firsth

</div>