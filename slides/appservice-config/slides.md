---
theme: default
layout: cover
---

# App Service Configuration and Administration

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-azure" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# App Service Configuration and Administration - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this lab on App Service Configuration and Administration. In this session, we'll explore how Azure App Service provides powerful platform-as-a-service features that would require significan

</div>

---

---
layout: center
---

# What You'll Learn

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> grade capabilities out of the box. One of the most important aspects is configuration management. Your applications need different settings for different environments, and App Service lets you manage these without logging into servers or manually editing configuration files.
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> in health monitoring. It can automatically detect when your application instances are unhealthy and take action to keep your service online. This is critical for production applications where availability is paramount.
</div>

</div>

---

---
layout: center
---

# Lab Overview

<div class="text-xl mt-8" v-click>

In this lab, we'll work with a REST API - a random number generator service. We're going to deliberately configure it to fail, and then we'll use App Service features to handle those failures graceful

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">App Settings</h3>
<p class="text-sm">- These are environment variables that override your application's default configuration. They're pe</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Health Checks</h3>
<p class="text-sm">- These are endpoints in your application that return the health status. App Service can poll these </p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Auto-Healing</h3>
<p class="text-sm">- This feature automatically restarts application instances based on rules you define, such as HTTP </p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Instance Management</h3>
<p class="text-sm">- When you run multiple instances, App Service acts as a load balancer, routing traffic only to heal</p>
</div>

</div>