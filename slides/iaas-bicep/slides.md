---
theme: default
layout: cover
---

# IaaS Bicep

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-bicep" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lab on automating application deployment with Infrastructure as a Service using Bicep.

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# The IaaS Automation Story

<div class="text-xl mt-8" v-click>

When we think about Infrastructure as a Service, it's easy to imagine manually logging into virtual machines and deploying applications by hand. But that's not how we work in modern cloud environments

</div>

---

---
layout: center
---

# What We'll Build

<div class="text-xl mt-8" v-click>

The scenario we're working with is a .NET web application that needs a SQL Server backend. In a traditional environment, this might take hours or days to set up: provisioning VMs, configuring networks

</div>

---

---
layout: center
---

# The Bicep Approach

<div class="text-xl mt-8" v-click>

What makes this approach powerful is how Bicep lets us split our infrastructure model across multiple files. Instead of one massive template that's hard to read and maintain, we can organize our infra

</div>

---

---
layout: center
---

# The Automation Story

<div class="text-xl mt-8" v-click>

But we're not stopping at infrastructure. One of the most powerful features we'll demonstrate is the VM custom script extension. This lets us run PowerShell scripts automatically when the VM is create

</div>