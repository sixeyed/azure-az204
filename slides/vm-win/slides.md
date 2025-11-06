---
theme: default
layout: cover
---

# Virtual Machines - Windows: Introduction

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

Welcome to this lab on Windows Virtual Machines in Azure

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# Why Windows VMs Matter

<div class="text-xl mt-8" v-click>

Virtual Machines are one of the core compute options in Azure, and Windows VMs serve an important role beyond traditional server workloads. They're particularly useful as workstation machines that you

</div>

---

---
layout: center
---

# What We'll Cover

<div class="mt-8">



</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">VM Sizes</h3>
<p class="text-sm">Azure offers different VM sizes with varying CPU cores, memory, and storage capacity. Windows requir</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">OS Images</h3>
<p class="text-sm">Each OS image has a URN (Uniform Resource Name) that identifies the publisher, offer, SKU, and versi</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Disks</h3>
<p class="text-sm">VMs have an OS disk for the operating system and can have additional data disks attached. We'll work</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Network Access</h3>
<p class="text-sm">Unlike Linux VMs which typically use SSH on port 22, Windows VMs use Remote Desktop Protocol on port</p>
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
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> An active Azure subscription
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> The Azure CLI installed and authenticated
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> A Remote Desktop client - built-in on Windows, Microsoft Remote Desktop on Mac, or Remmina on Linux
</div>

<div v-click>
<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> A strong password ready for the VM admin account
</div>

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>