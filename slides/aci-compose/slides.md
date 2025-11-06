---
theme: default
layout: cover
---

# Distributed Apps on Azure Container Instances

<div class="abs-bottom-4">
  <iconify-icon icon="logos:docker-icon" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Distributed Apps on Azure Container Instances - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this lab on Distributed Apps on Azure Container Instances.

</div>

---

---
layout: center
---

# Overview

<div class="text-xl mt-8" v-click>

Azure Container Instances, or ACI, is the simplest container platform available on Azure. It allows you to run containers without having to manage virtual machines or adopt a higher-level orchestratio

</div>

---

---
layout: center
---

# What You'll Learn

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> specific features and configuration options.
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> specific configurations.
</div>

</div>

---

---
layout: center
---

# Integration with Azure Services

<div class="text-xl mt-8" v-click>

ACI doesn't exist in isolation - it integrates seamlessly with other Azure services. We'll demonstrate this integration by connecting our containerized applications to Azure Storage services, includin

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">Container Groups</h3>
<p class="text-sm">ACI organizes multiple containers into groups that share the same network space, making it easy to b</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Resource Specification</h3>
<p class="text-sm">Unlike Docker Desktop, ACI requires you to specify CPU and memory requirements upfront so Azure can </p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Deployment Models</h3>
<p class="text-sm">You'll see the differences and similarities between ACI's YAML format and the Docker Compose format,</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Container Updates</h3>
<p class="text-sm">We'll explore how ACI handles configuration changes and what happens under the hood when you update </p>
</div>

</div>