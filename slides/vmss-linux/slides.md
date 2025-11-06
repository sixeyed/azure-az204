---
theme: default
layout: cover
---

# Virtual Machine Scale Sets - Linux: Introduction

<div class="abs-bottom-4">
  <iconify-icon icon="bi:pc-display" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lab on Virtual Machine Scale Sets with Linux

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# Context and Motivation

<div class="text-xl mt-8" v-click>

When working with VM Scale Sets, you have two main approaches for getting your application running on instances. The first approach is to use a custom image that contains your application pre-installe

</div>

---

---
layout: center
---

# What is cloud-init?

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

cloud-init is a powerful cross-platform system for configuring new machines. It allows you to automate all the usual steps for deploying pre-requisite...

</div>

---

---
layout: center
---

# Lab Objectives

<div class="text-xl mt-8" v-click>

In this lab, you'll learn how to:

</div>

---

---
layout: center
---

# What You'll Build

<div class="text-xl mt-8" v-click>

We'll start by creating a single VM with a cloud-init script to understand how the system works. Then we'll move to a full VM Scale Set running Nginx web servers, where each instance is automatically 

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
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Basic familiarity with Linux and shell commands
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> Understanding of VM Scale Sets from previous labs
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> init works with a single VM.
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>