---
theme: default
background: https://images.unsplash.com/photo-1614064548237-d3e02bf29b5d?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes Troubleshooting
  Diagnosing and fixing application issues - AZ-204
drawings:
  persist: false
transition: slide-left
title: Troubleshooting
mdc: true
---

# Kubernetes Troubleshooting

Where Theory Meets Reality

<div class="abs-bottom-10 left-10">
  <carbon-debug class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Master troubleshooting in Kubernetes<br/>Essential skill for AZ-204 and production
</div>

</v-click>

---
layout: section
---

# Why Troubleshooting Matters

---

# The Complexity Challenge

<v-click>

<div class="mt-4">
  <carbon-warning class="text-6xl text-orange-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Kubernetes is incredibly powerful
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
But also complex
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-orange-400">
Valid YAML ≠ Working Application
</div>

</v-click>

---

# Spelling vs Meaning

<v-click>

<div class="mt-12 text-center text-xl">
Kubernetes validates YAML syntax
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-red-400">
But not whether your app will work
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    YAML[Valid YAML] --> K8s[Kubernetes<br/>Accepts]
    K8s --> Broken[Broken<br/>Application ❌]
    style YAML fill:#51cf66
    style K8s fill:#0078d4
    style Broken fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Checks spelling and grammar, not meaning
</div>

</v-click>

---

# Time Investment

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
You'll spend significant time tracking down issues
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-debug class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Diagnose</div>
  </div>
  <div class="text-center">
    <carbon-tools-alt class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Fix</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Verify</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Common Points of Failure

---

# Where Things Go Wrong

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-deployment-pattern class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Deployment → ReplicaSet → Pods</span>
    <div class="text-sm mt-2 opacity-70">Label selectors must match</div>
    <div class="text-sm opacity-70">Mismatched labels = no Pods created</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-network-3 class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Service → Pods</span>
    <div class="text-sm mt-2 opacity-70">Selectors and port configuration</div>
    <div class="text-sm opacity-70">Wrong values = app unreachable</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-container-software class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Container Configuration</span>
    <div class="text-sm mt-2 opacity-70">Image names, commands, resources, probes</div>
    <div class="text-sm opacity-70">Can fail silently</div>
  </div>
</div>

</v-click>

---

# Loose Coupling Problem

<v-click>

<div class="mt-12 text-center text-xl">
Components are loosely coupled
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
Typo in one place can break everything
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Kubernetes won't tell you directly what's wrong
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Label[Label Typo] -.-> Service[Service Can't<br/>Find Pods]
    Service -.-> Users[Users Get<br/>503 Errors]
    style Label fill:#ff6b6b
    style Service fill:#ffd43b
    style Users fill:#ff6b6b
```

</div>

</v-click>

---
layout: section
---

# Your Troubleshooting Toolkit

---

# Essential kubectl Commands

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-view class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">kubectl get</span>
    <div class="text-sm mt-2 opacity-70">High-level status of resources</div>
    <div class="text-sm opacity-70">Is Pod running? Pending? Crashing?</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-document-view class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">kubectl describe</span>
    <div class="text-sm mt-2 opacity-70">Diagnostic deep-dive</div>
    <div class="text-sm opacity-70">Events, configuration, error messages</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-document class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">kubectl logs</span>
    <div class="text-sm mt-2 opacity-70">What's happening inside container</div>
    <div class="text-sm opacity-70">When container starts but behaves incorrectly</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-network-3 class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">kubectl port-forward</span>
    <div class="text-sm mt-2 opacity-70">Bypass Service layer, connect directly to Pod</div>
    <div class="text-sm opacity-70">Isolate: container problem or networking?</div>
  </div>
</div>

</v-click>

---
layout: section
---

# The Systematic Approach

---

# Top-Down Methodology

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Deployment[1. Check Deployment] --> RS[2. Did it create ReplicaSet?]
    RS --> Pods[3. Did ReplicaSet create Pods?]
    Pods --> Running[4. Are Pods running?]
    Running --> Network[5. Check Networking]
    Network --> Service[6. Does Service have endpoints?]
    Service --> Selectors[7. Do selectors match?]
    Selectors --> Ports[8. Are ports correct?]
    style Deployment fill:#51cf66
    style RS fill:#51cf66
    style Pods fill:#51cf66
    style Running fill:#51cf66
    style Network fill:#0078d4
    style Service fill:#0078d4
    style Selectors fill:#0078d4
    style Ports fill:#0078d4
```

</div>

</v-click>

---

# Start from Top

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Check Deployment first
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Did it create a ReplicaSet?
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg">
Did ReplicaSet create Pods?
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg">
Are Pods actually running?
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Then move to networking
</div>

</v-click>

---

# Avoid Jumping to Conclusions

<v-click>

<div class="mt-12 text-center text-xl">
Systematic approach keeps you from missing root cause
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Methodical</div>
  </div>
  <div class="text-center">
    <carbon-data-view-alt class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Thorough</div>
  </div>
  <div class="text-center">
    <carbon-rule class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Repeatable</div>
  </div>
</div>

</v-click>

---
layout: section
---

# AZ-204 Exam Relevance

---

# What Microsoft Expects

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-data-view-alt class="text-4xl text-blue-400" />
  <span class="text-lg">Container monitoring</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-debug class="text-4xl text-green-400" />
  <span class="text-lg">Diagnostics strategies</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-tools-alt class="text-4xl text-purple-400" />
  <span class="text-lg">Troubleshooting approaches</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Not just writing manifests - debugging them
</div>

</v-click>

---

# Practical Skills

<v-click>

<div class="mt-12 text-center text-xl">
This lab gives hands-on practice
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
With exact scenarios the exam tests
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-test-tool class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Diagnose</div>
  </div>
  <div class="text-center">
    <carbon-tools-alt class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Fix</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Verify</div>
  </div>
</div>

</v-click>

---
layout: section
---

# The Challenge

---

# Broken Application

<v-click>

<div class="mt-12 text-center text-xl text-orange-400">
Application with multiple issues
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Your mission: diagnose and fix
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Until app runs successfully
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-search class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Find Issues</div>
  </div>
  <div class="text-center">
    <carbon-tools-alt class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Apply Fixes</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Test Success</div>
  </div>
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

<v-click>

<div class="text-4xl mt-8 font-bold">
Ready to Troubleshoot!
</div>

</v-click>

<v-click>

<div class="text-xl mt-6 opacity-70">
Put your diagnostic skills to the test
</div>

</v-click>

</div>
