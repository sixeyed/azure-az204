---
theme: default
layout: cover
---

# Azure Files Storage

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

Welcome to this lab on Azure Files Storage

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Azure Files?

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

Azure Files is a fully managed file share service in the cloud. It provides shared storage that can be mounted into your filesystem, making it easy to...

</div>

---

---
layout: center
---

# Key Features

<div class="text-xl mt-8" v-click>

Let's look at the main features of Azure Files:

</div>

---

---
layout: center
---

# Common Use Cases

<div class="grid grid-cols-1 gap-4 mt-8">



</div>

---

---
layout: center
---

# How it Works

<div class="text-xl mt-8" v-click>

Azure Files is a feature of Azure Storage Accounts. When you create a storage account, you can create one or more file shares within it. Each share has a quota that defines its maximum capacity.

</div>

---

---
layout: center
---

# Lab Overview

<div class="text-xl mt-8" v-click>

In today's lab, we'll walk through the complete Azure Files experience. We'll start by creating a storage account and file share. Then we'll upload files and explore different ways to access them.

</div>