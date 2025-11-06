---
theme: default
layout: cover
---

# Virtual Machine Scale Sets - Windows

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

Welcome to this lab on Virtual Machine Scale Sets for Windows

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What Are Virtual Machine Scale Sets?

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

When you need to run multiple instances of your application, you could create individual VMs - each with their own IP addresses and public IPs. But th...

</div>

---

---
layout: center
---

# Lab Overview

<div class="text-xl mt-8" v-click>

In this lab, we'll be working with a Windows application that's already been captured as a custom VM image. We'll use this image to create a VMSS and explore the key features.

</div>

---

---
layout: center
class: text-center
---

# Prerequisites

<div class="mt-12">

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> image" that contains a Windows application with IIS configured.
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> vmss-win" with that image already in place.
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# Portal Exploration

<div class="text-xl mt-8" v-click>

Let's start by looking at VMSS in the Azure Portal. When you search for Virtual Machine Scale Sets and begin creating one, you'll notice several important configuration options.

</div>

---

---
layout: center
---

# What's Next

<div class="text-xl mt-8" v-click>

Now that we understand what VMSS provides, let's move on to actually creating one from our custom image and getting our application running across multiple instances.

</div>