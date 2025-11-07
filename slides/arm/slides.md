---
theme: default
background: https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## ARM Templates
  Declarative infrastructure for AZ-204
drawings:
  persist: false
transition: slide-left
title: ARM Templates
mdc: true
---

# Azure Resource Manager Templates

Declarative Infrastructure as Code

<div class="abs-bottom-10 left-10">
  <carbon-document-tasks class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: In this lab, we'll explore the declarative approach to infrastructure deployment in Azure.
search_anchor: this lab, we'll explore the
-->
<v-click>

<div class="text-xl mt-8">
Explore ARM templates<br/>The declarative approach to Azure infrastructure
</div>

</v-click>

---
layout: section
---

# Imperative vs Declarative

---

# The Imperative Approach

<v-click>

<div class="mt-4">
  <carbon-command-line class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: This is what we call an imperative approach - you tell Azure exactly what to do, step by step.
search_anchor: This is what we call
-->
<v-click>

<div class="mt-8 text-xl text-center">
Azure CLI: Tell Azure exactly what to do
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Step1[Check if exists] --> Step2[Create if missing]
    Step2 --> Step3[Update if exists]
    Step3 --> Step4[Configure settings]
    Step4 --> Step5[Repeat for each resource]
    style Step1 fill:#0078d4
    style Step2 fill:#0078d4
    style Step3 fill:#0078d4
    style Step4 fill:#0078d4
    style Step5 fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: Think of them as inputs to your template.
search_anchor: Think of them as inputs
-->
<v-click>

<div class="mt-8 text-center text-lg text-red-400">
Lots of checks needed
</div>

</v-click>

<!--
METADATA:
sentence: But there's a challenge with this approach: you need to add lots of checks to make sure you're not trying to create resources that already exist.
search_anchor: But there's a challenge with
-->
<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Can't create resources that already exist
</div>

</v-click>

---

# The Declarative Approach

<v-click>

<div class="mt-4">
  <carbon-document-tasks class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Instead of telling Azure HOW to do something, you describe WHAT you want the end result to be, and the tooling figures out whether it needs to create or update resources.
search_anchor: Instead of telling Azure HOW
-->
<v-click>

<div class="mt-8 text-xl text-center">
Describe WHAT you want, not HOW to do it
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Desired[Desired State<br/>in Template] --> Tool[Azure Figures Out]
    Tool --> Create[Create New]
    Tool --> Update[Update Existing]
    Tool --> Skip[Skip Unchanged]
    style Desired fill:#51cf66
    style Tool fill:#0078d4
    style Create fill:#ffd43b
    style Update fill:#ffd43b
    style Skip fill:#ffd43b
```

</div>

</v-click>

<!--
METADATA:
sentence: The alternative is the declarative approach.
search_anchor: alternative is the declarative approach
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Tooling handles the complexity
</div>

</v-click>

---
layout: section
---

# What Are ARM Templates?

---

# JSON-Based Infrastructure

<v-click>

<div class="mt-4">
  <carbon-document-blank class="text-6xl text-blue-400" />
</div>

</v-click>

<!--
METADATA:
sentence: ARM templates are JSON files that model the desired state of your Azure resources.
search_anchor: ARM templates are JSON files
-->
<v-click>

<div class="mt-8 text-xl text-center">
JSON files modeling desired Azure state
</div>

</v-click>

<!--
METADATA:
sentence: They can live in source control alongside your application code, giving you version control and repeatability for your infrastructure.
search_anchor: They can live in source
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-version-major class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Version Control</div>
  </div>
  <div class="text-center">
    <carbon-repeat class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Repeatability</div>
  </div>
  <div class="text-center">
    <carbon-code class="text-6xl text-orange-400" />
    <div class="text-sm mt-3">Alongside Code</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Let's get started with the hands-on exercises.
search_anchor: Let's get started with the
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Infrastructure lives with application code
</div>

</v-click>

---
layout: section
---

# Template Structure

---

# Key Components

<!--
METADATA:
sentence: Think of them as inputs to your template.
search_anchor: Think of them as inputs
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-parameter class="text-5xl text-blue-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Parameters</div>
    <div class="text-sm mt-2 opacity-70">Values that change per deployment</div>
    <div class="text-sm opacity-70">Think of them as inputs</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: They help keep your template clean and maintainable.
search_anchor: They help keep your template
-->
<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-variable class="text-5xl text-green-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Variables</div>
    <div class="text-sm mt-2 opacity-70">Values used throughout template</div>
    <div class="text-sm opacity-70">Keep template clean and maintainable</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Finally, we have resources - this is where you declare the actual Azure resources to create, using the variables and parameters you've defined.
search_anchor: Finally, we have resources -
-->
<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-cube class="text-5xl text-purple-400 mt-1" />
  <div>
    <div class="text-xl font-bold">Resources</div>
    <div class="text-sm mt-2 opacity-70">Actual Azure resources to create</div>
    <div class="text-sm opacity-70">Using parameters and variables</div>
  </div>
</div>

</v-click>

---

# Template Flow

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Params[Parameters<br/>Inputs] --> Vars[Variables<br/>Computed Values]
    Vars --> Resources[Resources<br/>Azure Resources]
    style Params fill:#51cf66
    style Vars fill:#ffd43b
    style Resources fill:#0078d4
```

</div>

</v-click>

<!--
METADATA:
sentence: The name and location are read from parameters - this makes the template reusable.
search_anchor: name and location are read
-->
<v-click>

<div class="mt-12 text-center text-xl">
Parameters feed into variables
</div>

</v-click>

<!--
METADATA:
sentence: The Storage Account Resource Let's examine the storage account resource definition.
search_anchor: Storage Account Resource Let's examine
-->
<v-click>

<div class="mt-4 text-center text-xl">
Variables used in resource definitions
</div>

</v-click>

---
layout: section
---

# Storage Account Example

---

# Resource Definition Elements

<!--
METADATA:
sentence: In this case, it's Microsoft.Storage/storageAccounts with a specific API version.
search_anchor: this case, it's Microsoft.Storage/storageAccounts with
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-data-class class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Type & API Version</div>
    <div class="text-sm mt-2 opacity-70">Microsoft.Storage/storageAccounts</div>
    <div class="text-sm opacity-70">Specific API version for consistency</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The name and location are read from parameters - this makes the template reusable.
search_anchor: name and location are read
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-label class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Name & Location</div>
    <div class="text-sm mt-2 opacity-70">Read from parameters</div>
    <div class="text-sm opacity-70">Makes template reusable</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The SKU is read from a variable - we've set it to Standard_LRS.
search_anchor: SKU is read from a
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-pricing-traditional class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">SKU</div>
    <div class="text-sm mt-2 opacity-70">Read from variable</div>
    <div class="text-sm opacity-70">Standard_LRS in this example</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Notice we're setting supportsHttpsTrafficOnly to true, ensuring secure access.
search_anchor: Notice we're setting supportsHttpsTrafficOnly to
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-settings class="text-4xl text-orange-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Properties</div>
    <div class="text-sm mt-2 opacity-70">Configuration details</div>
    <div class="text-sm opacity-70">supportsHttpsTrafficOnly: true</div>
  </div>
</div>

</v-click>

---

# Consistency Benefits

<!--
METADATA:
sentence: You can deploy the same template to different regions or with different names.
search_anchor: You can deploy the same
-->
<v-click>

<div class="mt-8 text-center text-xl">
Everyone who deploys gets the same result
</div>

</v-click>

<!--
METADATA:
sentence: When you share this template, anyone who deploys it will get exactly the same type of storage account: version 2, with Standard LRS redundancy, and HTTPS-only access.
search_anchor: When you share this template
-->
<v-click>

<div class="mt-12 grid grid-cols-2 gap-8">
  <div class="text-center">
    <carbon-version class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Version 2</div>
  </div>
  <div class="text-center">
    <carbon-data-backup class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Standard LRS</div>
  </div>
  <div class="text-center">
    <carbon-locked class="text-6xl text-red-400" />
    <div class="text-sm mt-3">HTTPS Only</div>
  </div>
  <div class="text-center">
    <carbon-earth class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Any Region</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The alternative is the declarative approach.
search_anchor: alternative is the declarative approach
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Key benefit of declarative approach
</div>

</v-click>

---
layout: section
---

# Desired State Deployment

---

# How ARM Templates Work

<!--
METADATA:
sentence: You can deploy the same template to different regions or with different names.
search_anchor: You can deploy the same
-->
<v-click>

<div class="mt-8 text-center text-xl">
Azure compares template to current state
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Template[Template<br/>Desired State] --> Compare{Compare}
    Current[Current State] --> Compare
    Compare -->|Missing| Create[Create Resource]
    Compare -->|Different| Update[Update Resource]
    Compare -->|Same| Skip[No Action]
    style Template fill:#51cf66
    style Current fill:#ffd43b
    style Compare fill:#0078d4
    style Create fill:#0078d4
    style Update fill:#0078d4
    style Skip fill:#gray
```

</div>

</v-click>

<!--
METADATA:
sentence: It then makes only the changes necessary to reach that desired state.
search_anchor: It then makes only the
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Makes only necessary changes
</div>

</v-click>

---

# Idempotent Deployments

<v-click>

<div class="mt-4">
  <carbon-repeat class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: This means ARM templates are idempotent - you can run the same deployment multiple times and get the same result, regardless of the current state.
search_anchor: This means ARM templates are
-->
<v-click>

<div class="mt-8 text-xl text-center">
Run same deployment multiple times
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Deploy1[Deploy #1] --> State1[Desired State]
    Deploy2[Deploy #2] --> State2[Desired State]
    Deploy3[Deploy #3] --> State3[Desired State]
    State1 -.->|Same| Result[Consistent Result]
    State2 -.->|Same| Result
    State3 -.->|Same| Result
    style Deploy1 fill:#0078d4
    style Deploy2 fill:#0078d4
    style Deploy3 fill:#0078d4
    style Result fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: This means ARM templates are idempotent - you can run the same deployment multiple times and get the same result, regardless of the current state.
search_anchor: This means ARM templates are
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Same result regardless of current state
</div>

</v-click>

---
layout: section
---

# What's Next

---

# In the Exercises

<!--
METADATA:
sentence: What Are ARM Templates?
search_anchor: What Are ARM Templates
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-blue-400" />
  <span class="text-lg">Deploy ARM templates using Azure CLI</span>
</div>

</v-click>

<!--
METADATA:
sentence: What's Next In the exercises, we'll deploy ARM templates using the Azure CLI, explore the what-if feature to preview changes, and see how ARM templates help you identify and fix configuration drift.
search_anchor: What's Next In the exercises
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-search class="text-4xl text-green-400" />
  <span class="text-lg">Explore what-if feature to preview changes</span>
</div>

</v-click>

<!--
METADATA:
sentence: What's Next In the exercises, we'll deploy ARM templates using the Azure CLI, explore the what-if feature to preview changes, and see how ARM templates help you identify and fix configuration drift.
search_anchor: What's Next In the exercises
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-4xl text-orange-400" />
  <span class="text-lg">Identify and fix configuration drift</span>
</div>

</v-click>

<!--
METADATA:
sentence: In this lab, we'll explore the declarative approach to infrastructure deployment in Azure.
search_anchor: this lab, we'll explore the
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Hands-on with declarative infrastructure
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
sentence: Let's get started with the hands-on exercises.
search_anchor: Let's get started with the
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: What Are ARM Templates?
search_anchor: What Are ARM Templates
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Explore ARM templates hands-on
</div>

</v-click>

</div>
