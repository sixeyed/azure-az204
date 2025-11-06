---
theme: default
layout: cover
---

# Securing VNet Access

<div class="abs-bottom-4">
  <iconify-icon icon="carbon:network-4" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Securing VNet Access - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this lab on securing Virtual Network access in Azure.

</div>

---

---
layout: center
---

# What We'll Cover

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> or NSGs. These are the primary mechanism for defining rules that allow or deny traffic from specific sources and to specific ports. Think of them as firewalls at the network layer.
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> a way to join virtual networks together when different parts of your application need to communicate with each other, even across different networks or regions.
</div>

</div>

---

---
layout: center
---

# Real-World Scenario

<div class="text-xl mt-8" v-click>

Imagine you're building a web application with multiple tiers. Your web servers need to be accessible from the internet, but your database servers should only be reachable from within your private net

</div>

---

---
layout: center
---

# Learning Objectives

<div class="text-xl mt-8" v-click>

By the end of this lab, you'll be able to:
- Create and configure Network Security Groups with custom rules
- Understand default NSG rules and how they affect traffic
- Deploy Azure Bastion to securel

</div>