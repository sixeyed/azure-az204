---
theme: default
background: https://images.unsplash.com/photo-1633265486064-086b219458ec?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure Sign-In
  Foundation of working with Azure - AZ-204
drawings:
  persist: false
transition: slide-left
title: Sign-In
mdc: true
---

# Azure Sign-In

Foundation of Working with Azure

<div class="abs-bottom-10 left-10">
  <carbon-login class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: What You'll Learn Azure uses Microsoft accounts for authentication and authorization.
search_anchor: What You'll Learn Azure uses
-->
<v-click>

<div class="text-xl mt-8">
Explore Azure authentication<br/>Essential foundation for all Azure work
</div>

</v-click>

---
layout: section
---

# Azure Accounts and Subscriptions

---

# Your Identity

<v-click>

<div class="mt-4">
  <carbon-user class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: In a corporate environment, your account would be managed by your organization's Azure Active Directory.
search_anchor: corporate environment, your account would
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Microsoft account = your identity in Azure
</div>

</v-click>

<!--
METADATA:
sentence: This single account can have access to one or more Azure Subscriptions.
search_anchor: This single account can have
-->
<v-click>

<div class="mt-12 text-center text-xl">
Single account can access multiple Subscriptions
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Account[Microsoft Account] --> Sub1[Subscription 1]
    Account --> Sub2[Subscription 2]
    Account --> Sub3[Subscription 3]
    Sub1 --> Resources1[Resources & Billing]
    Sub2 --> Resources2[Resources & Billing]
    Sub3 --> Resources3[Resources & Billing]
    style Account fill:#51cf66
    style Sub1 fill:#0078d4
    style Sub2 fill:#0078d4
    style Sub3 fill:#0078d4
```

</div>

</v-click>

---

# Subscriptions

<!--
METADATA:
sentence: Each Subscription is a logical container for your Azure resources and has its own billing and access management.
search_anchor: Each Subscription is a logical
-->
<v-click>

<div class="mt-12 text-center text-xl">
Logical container for Azure resources
</div>

</v-click>

<!--
METADATA:
sentence: Why Learn Multiple Access Methods?
search_anchor: Why Learn Multiple Access Methods
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-receipt class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Own Billing</div>
  </div>
  <div class="text-center">
    <carbon-user-access class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Access Management</div>
  </div>
</div>

</v-click>

---

# Account Types

<!--
METADATA:
sentence: In a corporate environment, your account would be managed by your organization's Azure Active Directory.
search_anchor: corporate environment, your account would
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-enterprise class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Corporate Environment</div>
    <div class="text-sm mt-2 opacity-70">Managed by organization's Azure Active Directory</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: For learning and personal projects, you can create your own Microsoft account and Azure Subscription.
search_anchor: learning and personal projects, you
-->
<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-user class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Personal / Learning</div>
    <div class="text-sm mt-2 opacity-70">Create own Microsoft account and Subscription</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Three Ways to Access Azure

---

# Access Methods

<!--
METADATA:
sentence: It's great for exploration and visual management, but it's not easily automated.
search_anchor: It's great for exploration and
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-browser class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Azure Portal</span>
    <div class="text-sm mt-2 opacity-70">Web-based graphical interface</div>
    <div class="text-sm opacity-70">Great for exploration and visual management</div>
    <div class="text-sm mt-2 text-red-400">Not easily automated</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The Azure CLI - A cross-platform command-line tool that provides a scriptable, repeatable way to manage Azure resources.
search_anchor: Azure CLI - A cross-platform
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-terminal class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Azure CLI</span>
    <div class="text-sm mt-2 opacity-70">Cross-platform command-line tool</div>
    <div class="text-sm opacity-70">Scriptable and repeatable</div>
    <div class="text-sm mt-2 text-green-400">Recommended for developers</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The Azure Cloud Shell - A browser-based shell environment that comes with Azure tools pre-installed and configured.
search_anchor: Azure Cloud Shell - A
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-cloud-app class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Azure Cloud Shell</span>
    <div class="text-sm mt-2 opacity-70">Browser-based shell environment</div>
    <div class="text-sm opacity-70">Azure tools pre-installed</div>
    <div class="text-sm mt-2 text-green-400">No local installation needed</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Azure Portal

---

# Web-Based Interface

<v-click>

<div class="mt-4">
  <carbon-browser class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Three Ways to Access Azure There are three primary ways to interact with Azure: The Azure Portal - A web-based graphical interface where you can browse services, create resources, and manage your Azure environment.
search_anchor: Three Ways to Access Azure
-->
<v-click>

<div class="mt-8 text-xl text-center">
Browse services, create resources, manage environment
</div>

</v-click>

<!--
METADATA:
sentence: It's great for exploration and visual management, but it's not easily automated.
search_anchor: It's great for exploration and
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Visual exploration</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Easy discovery</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: It's great for exploration and visual management, but it's not easily automated.
search_anchor: It's great for exploration and
-->
<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Not easily automated
</div>

</v-click>

---
layout: section
---

# Azure CLI

---

# Command-Line Power

<v-click>

<div class="mt-4">
  <carbon-terminal class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: The Azure CLI - A cross-platform command-line tool that provides a scriptable, repeatable way to manage Azure resources.
search_anchor: Azure CLI - A cross-platform
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Cross-platform command-line tool
</div>

</v-click>

<!--
METADATA:
sentence: The Azure CLI - A cross-platform command-line tool that provides a scriptable, repeatable way to manage Azure resources.
search_anchor: Azure CLI - A cross-platform
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-document-tasks class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Scriptable</div>
  </div>
  <div class="text-center">
    <carbon-renew class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Repeatable</div>
  </div>
  <div class="text-center">
    <carbon-deployment-pattern class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Automate</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This is the recommended approach for developers and anyone who needs to automate Azure operations.
search_anchor: This is the recommended approach
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Recommended for developers
</div>

</v-click>

---
layout: section
---

# Azure Cloud Shell

---

# Browser-Based Shell

<v-click>

<div class="mt-4">
  <carbon-cloud-app class="text-6xl text-purple-400" />
</div>

</v-click>

<!--
METADATA:
sentence: The Azure Cloud Shell - A browser-based shell environment that comes with Azure tools pre-installed and configured.
search_anchor: Azure Cloud Shell - A
-->
<v-click>

<div class="mt-8 text-xl text-center">
Azure tools pre-installed and configured
</div>

</v-click>

<!--
METADATA:
sentence: Perfect for when you can't install the CLI locally but need command-line access to Azure.
search_anchor: Perfect for when you can't
-->
<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">No local installation required</span>
</div>

</v-click>

<!--
METADATA:
sentence: Why Learn Multiple Access Methods?
search_anchor: Why Learn Multiple Access Methods
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Access from any browser</span>
</div>

</v-click>

<!--
METADATA:
sentence: What You'll Learn Azure uses Microsoft accounts for authentication and authorization.
search_anchor: What You'll Learn Azure uses
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Already authenticated</span>
</div>

</v-click>

---
layout: section
---

# Why Learn Multiple Methods?

---

# Different Strengths

<!--
METADATA:
sentence: It's great for exploration and visual management, but it's not easily automated.
search_anchor: It's great for exploration and
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-browser class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Portal</div>
    <div class="text-sm mt-2 opacity-70">Discovery and visual exploration</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The Azure CLI - A cross-platform command-line tool that provides a scriptable, repeatable way to manage Azure resources.
search_anchor: Azure CLI - A cross-platform
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-terminal class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">CLI</div>
    <div class="text-sm mt-2 opacity-70">Automation and repeatable deployments</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The Azure Cloud Shell - A browser-based shell environment that comes with Azure tools pre-installed and configured.
search_anchor: Azure Cloud Shell - A
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-cloud-app class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Cloud Shell</div>
    <div class="text-sm mt-2 opacity-70">Quick access without local installation</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Let's begin by exploring the Azure Portal.
search_anchor: Let's begin by exploring the
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Use all three depending on the task
</div>

</v-click>

---

# Important Skill

<!--
METADATA:
sentence: Understanding when to use each approach is an important skill.
search_anchor: Understanding when to use each
-->
<v-click>

<div class="mt-12 text-center text-xl">
Understanding when to use each approach
</div>

</v-click>

<!--
METADATA:
sentence: The Azure CLI - A cross-platform command-line tool that provides a scriptable, repeatable way to manage Azure resources.
search_anchor: Azure CLI - A cross-platform
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-decision-tree class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Right Tool</div>
  </div>
  <div class="text-center">
    <carbon-time class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Right Time</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Right Task</div>
  </div>
</div>

</v-click>

---
layout: section
---

# What's Next

---

# Explore the Portal

<!--
METADATA:
sentence: Let's begin by exploring the Azure Portal.
search_anchor: Let's begin by exploring the
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-browser class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Navigate Azure Portal</div>
  </div>
  <div class="text-center">
    <carbon-cloud-services class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Discover Services</div>
  </div>
  <div class="text-center">
    <carbon-document-view class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Understand Layout</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Let's begin by exploring the Azure Portal.
search_anchor: Let's begin by exploring the
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Foundation for all Azure development
</div>

</v-click>

---
layout: center
class: text-center
---

<div>

<v-click>

<carbon-play-outline class="text-8xl text-green-400 inline-block" />

</v-click>

<!--
METADATA:
sentence: Let's begin by exploring the Azure Portal.
search_anchor: Let's begin by exploring the
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Begin!
</div>

</v-click>

<!--
METADATA:
sentence: Let's begin by exploring the Azure Portal.
search_anchor: Let's begin by exploring the
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Start your Azure journey
</div>

</v-click>

</div>
