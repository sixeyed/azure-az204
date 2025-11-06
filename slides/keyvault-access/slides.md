---
theme: default
layout: cover
---

# Securing Key Vault Access

<div class="abs-bottom-4">
  <iconify-icon icon="mdi:key" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Securing Key Vault Access - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this lab on securing Azure Key Vault access. In this session, we'll explore how to properly lock down access to your Key Vaults to ensure only authorized resources can access your sensitive

</div>

---

---
layout: center
---

# Why Key Vault Security Matters

<div class="text-xl mt-8" v-click>

Key Vaults store your most sensitive data - passwords, connection strings, API keys, and certificates. Because of this, securing access to Key Vault is absolutely critical. A misconfigured Key Vault c

</div>

---

---
layout: center
---

# Two Layers of Security

<div class="text-xl mt-8" v-click>

Azure Key Vault provides two distinct layers of security that work together:

</div>

---

---
layout: center
---

# What We'll Cover

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> based access control.
</div>

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">Access Policies</h3>
<p class="text-sm">define what a principal is allowed to do with secrets, keys, or certificates. You configure these in</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Service Endpoints</h3>
<p class="text-sm">allow Azure services like Key Vault to communicate with resources inside a virtual network subnet.</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Managed Identities</h3>
<p class="text-sm">are Azure-managed identities that Azure services can use to authenticate with other Azure services. </p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Principals</h3>
<p class="text-sm">is Azure's general term for any authenticated identity - users, groups, service principals, or manag</p>
</div>

</div>