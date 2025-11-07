---
theme: default
background: https://images.unsplash.com/photo-1614064548237-d3e02bf29b5d?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes Secrets
  Secure configuration management for AZ-204
drawings:
  persist: false
transition: slide-left
title: Secrets
mdc: true
---

# Kubernetes Secrets

Secure Configuration Management

<div class="abs-bottom-10 left-10">
  <carbon-locked class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: We'll explore how secrets appear inside containers.
search_anchor: We'll explore how secrets appear
-->
<v-click>

<div class="text-xl mt-8">
Explore Kubernetes Secrets<br/>Essential for secure application configuration
</div>

</v-click>

---
layout: section
---

# The Problem with ConfigMaps

---

# Plain Text Limitation

<v-click>

<div class="mt-4">
  <carbon-warning class="text-6xl text-red-400" />
</div>

</v-click>

<!--
METADATA:
sentence: ConfigMaps are fantastic for general settings, but there's a major limitation: they store everything in plain text.
search_anchor: ConfigMaps are fantastic for general
-->
<v-click>

<div class="mt-8 text-xl text-center">
ConfigMaps store everything in plain text
</div>

</v-click>

<!--
METADATA:
sentence: Anyone with access to your cluster can read those values.
search_anchor: Anyone with access to your
-->
<v-click>

<div class="mt-12 text-center text-xl text-red-400">
Anyone with cluster access can read values
</div>

</v-click>

<!--
METADATA:
sentence: So what happens when you need to store passwords, API keys, or connection strings?
search_anchor: So what happens when you
-->
<v-click>

<div class="mt-12 text-center text-2xl">
What about passwords, API keys, connection strings?
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Config[ConfigMap] --> Plain[Plain Text]
    Plain --> Anyone[Anyone Can Read]
    style Config fill:#ffd43b
    style Plain fill:#ff6b6b
    style Anyone fill:#ff6b6b
```

</div>

</v-click>

---
layout: section
---

# What Are Kubernetes Secrets?

---

# Designed for Sensitive Data

<v-click>

<div class="mt-4">
  <carbon-locked class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: [On screen: Secret object diagram with lock icon] Kubernetes Secrets are designed specifically for sensitive data.
search_anchor: [On screen: Secret object diagram
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Specifically for sensitive information
</div>

</v-click>

<!--
METADATA:
sentence: They use the same familiar API as ConfigMaps, so you can inject them as environment variables or mount them as files.
search_anchor: They use the same familiar
-->
<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Same familiar API as ConfigMaps</span>
</div>

</v-click>

<!--
METADATA:
sentence: They use the same familiar API as ConfigMaps, so you can inject them as environment variables or mount them as files.
search_anchor: They use the same familiar
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Inject as environment variables or mount as files</span>
</div>

</v-click>

<!--
METADATA:
sentence: But Secrets have additional safeguards built in.
search_anchor: But Secrets have additional safeguards
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Additional safeguards built in</span>
</div>

</v-click>

---

# Built-In Safeguards

<!--
METADATA:
sentence: They're base-64 encoded at rest, and depending on your cluster configuration, they can be encrypted in the Kubernetes database.
search_anchor: They're base-64 encoded at rest
-->
<v-click>

<div class="mt-12 flex items-start gap-4">
  <carbon-encryption class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Base-64 Encoded</div>
    <div class="text-sm mt-2 opacity-70">At rest in Kubernetes</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: They're base-64 encoded at rest, and depending on your cluster configuration, they can be encrypted in the Kubernetes database.
search_anchor: They're base-64 encoded at rest
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-security class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Encryption Available</div>
    <div class="text-sm mt-2 opacity-70">Can be encrypted in Kubernetes database</div>
    <div class="text-sm opacity-70">Depending on cluster configuration</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Anyone with access to your cluster can read those values.
search_anchor: Anyone with access to your
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-user-access class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Access Controls</div>
    <div class="text-sm mt-2 opacity-70">RBAC integration</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Secret Types

---

# Three Ways to Create

<!--
METADATA:
sentence: You can encode values in base-64 and define them directly in YAML.
search_anchor: You can encode values in
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-code class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Base-64 in YAML</span>
    <div class="text-sm mt-2 opacity-70">Encode values and define in YAML</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: You can use plain text in your YAML files when they're properly secured.
search_anchor: You can use plain text
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-document-blank class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Plain Text in YAML</span>
    <div class="text-sm mt-2 opacity-70">When files are properly secured</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: So where does real security come from?
search_anchor: So where does real security
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-folder class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">From Files</span>
    <div class="text-sm mt-2 opacity-70">Separate security teams from dev teams</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Each approach has its use cases, and we'll explore all of them in the hands-on exercises.
search_anchor: Each approach has its use
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Each approach has its use cases
</div>

</v-click>

---
layout: section
---

# Security Considerations

---

# Important Truth

<!--
METADATA:
sentence: We'll work with base-64 encoding and decoding.
search_anchor: We'll work with base-64 encoding
-->
<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
Base-64 encoding is NOT encryption
</div>

</v-click>

<!--
METADATA:
sentence: It's trivially easy to decode.
search_anchor: It's trivially easy to decode
-->
<v-click>

<div class="mt-12 text-center text-xl">
Trivially easy to decode
</div>

</v-click>

<!--
METADATA:
sentence: So where does real security come from?
search_anchor: So where does real security
-->
<v-click>

<div class="mt-12 text-center text-xl">
So where does real security come from?
</div>

</v-click>

---

# Real Security Sources

<!--
METADATA:
sentence: Anyone with access to your cluster can read those values.
search_anchor: Anyone with access to your
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-user-access class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Access Controls</div>
    <div class="text-sm mt-2 opacity-70">RBAC limiting who can read secrets</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: That's where Secrets come in.
search_anchor: That's where Secrets come in
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-encryption class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Encryption at Rest</div>
    <div class="text-sm mt-2 opacity-70">Encrypt secrets in cluster database</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This includes creating and managing secrets, integrating with Azure Key Vault, and following security best practices.
search_anchor: This includes creating and managing
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-cloud-services class="text-4xl text-purple-400 mt-1" />
  <div>
    <div class="text-lg font-bold">External Secret Management</div>
    <div class="text-sm mt-2 opacity-70">Integrate with Azure Key Vault</div>
    <div class="text-sm opacity-70">Pull secrets at runtime</div>
  </div>
</div>

</v-click>

---

# Production Best Practice

<!--
METADATA:
sentence: It comes from access controls, from encrypting secrets at rest in your cluster, and increasingly, from integrating with dedicated secret management systems like Azure Key Vault.
search_anchor: It comes from access controls
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Use dedicated secret management systems
</div>

</v-click>

<!--
METADATA:
sentence: In production environments, you'll want to use solutions like the Secrets Store CSI driver or external secrets operators to pull secrets from Azure Key Vault at runtime.
search_anchor: production environments, you'll want to
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-locked class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Secrets Store CSI driver</div>
  </div>
  <div class="text-center">
    <carbon-network-overlay class="text-6xl text-green-400" />
    <div class="text-sm mt-3">External Secrets Operator</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: This includes creating and managing secrets, integrating with Azure Key Vault, and following security best practices.
search_anchor: This includes creating and managing
-->
<v-click>

<div class="mt-12 text-center text-xl">
Integrate with Azure Key Vault at runtime
</div>

</v-click>

---
layout: section
---

# AZ-204 Exam Relevance

---

# Key Exam Topics

<!--
METADATA:
sentence: That's where Secrets come in.
search_anchor: That's where Secrets come in
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-settings class="text-4xl text-blue-400" />
  <span class="text-lg">Configure secure application settings in AKS</span>
</div>

</v-click>

<!--
METADATA:
sentence: That's where Secrets come in.
search_anchor: That's where Secrets come in
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-green-400" />
  <span class="text-lg">Create and manage secrets</span>
</div>

</v-click>

<!--
METADATA:
sentence: This includes creating and managing secrets, integrating with Azure Key Vault, and following security best practices.
search_anchor: This includes creating and managing
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-purple-400" />
  <span class="text-lg">Integrate with Azure Key Vault</span>
</div>

</v-click>

<!--
METADATA:
sentence: This includes creating and managing secrets, integrating with Azure Key Vault, and following security best practices.
search_anchor: This includes creating and managing
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-security class="text-4xl text-orange-400" />
  <span class="text-lg">Follow security best practices</span>
</div>

</v-click>

---

# Critical Knowledge

<!--
METADATA:
sentence: You can encode values in base-64 and define them directly in YAML.
search_anchor: You can encode values in
-->
<v-click>

<div class="mt-12 text-center text-xl">
Understand the difference
</div>

</v-click>

<!--
METADATA:
sentence: That's where Secrets come in.
search_anchor: That's where Secrets come in
-->
<v-click>

<div class="mt-12 flex justify-center gap-16">
  <div class="text-center">
    <carbon-settings class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">ConfigMaps</div>
    <div class="text-xs mt-2 opacity-70">General config</div>
  </div>
  <div class="text-center">
    <carbon-locked class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Secrets</div>
    <div class="text-xs mt-2 opacity-70">Sensitive data</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: You'll also need to know how secrets differ from ConfigMaps and when to use each.
search_anchor: You'll also need to know
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Know when to use each
</div>

</v-click>

---
layout: section
---

# What We'll Cover

---

# Lab Objectives

<!--
METADATA:
sentence: --- Slide 7: What We'll Cover [On screen: Agenda with checkboxes] In the exercises ahead, we'll create secrets using different methods.
search_anchor: --- Slide 7: What We'll
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create secrets using different methods</span>
</div>

</v-click>

<!--
METADATA:
sentence: We'll explore how secrets appear inside containers.
search_anchor: We'll explore how secrets appear
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-explore class="text-4xl text-green-400" />
  <span class="text-lg">Explore how secrets appear inside containers</span>
</div>

</v-click>

<!--
METADATA:
sentence: We'll work with base-64 encoding and decoding.
search_anchor: We'll work with base-64 encoding
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-encryption class="text-4xl text-purple-400" />
  <span class="text-lg">Work with base-64 encoding and decoding</span>
</div>

</v-click>

<!--
METADATA:
sentence: And we'll look at how to structure your deployments to separate secret management from application deployment.
search_anchor: we'll look at how to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document-tasks class="text-4xl text-orange-400" />
  <span class="text-lg">Structure deployments to separate concerns</span>
</div>

</v-click>

<!--
METADATA:
sentence: The hands-on labs will give you the practical experience you need to confidently answer questions about secret management on the exam.
search_anchor: hands-on labs will give you
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Practical experience for exam confidence
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
sentence: Get your terminal ready, and let's start securing some configuration data!
search_anchor: Get your terminal ready, and
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: Get your terminal ready, and let's start securing some configuration data!
search_anchor: Get your terminal ready, and
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Secure your configuration data
</div>

</v-click>

</div>
