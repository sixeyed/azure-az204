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

<!--
METADATA:
sentence: If you're preparing for the AZ-204 exam or working with Azure Kubernetes Service in production, this is where theory meets reality.
search_anchor: If you're preparing for the
-->
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

<!--
METADATA:
sentence: --- Slide 1: Why Troubleshooting Matters (30 seconds) Here's the thing about Kubernetes - it's incredibly powerful, but it's also complex.
search_anchor: --- Slide 1: Why Troubleshooting
-->
<v-click>

<div class="mt-8 text-xl text-center">
Kubernetes is incredibly powerful
</div>

</v-click>

<!--
METADATA:
sentence: --- Slide 1: Why Troubleshooting Matters (30 seconds) Here's the thing about Kubernetes - it's incredibly powerful, but it's also complex.
search_anchor: --- Slide 1: Why Troubleshooting
-->
<v-click>

<div class="mt-8 text-center text-xl">
But also complex
</div>

</v-click>

<!--
METADATA:
sentence: You can have perfectly valid specs that still produce a completely broken application.
search_anchor: You can have perfectly valid
-->
<v-click>

<div class="mt-12 text-center text-2xl text-orange-400">
Valid YAML ≠ Working Application
</div>

</v-click>

---

# Spelling vs Meaning

<!--
METADATA:
sentence: When you deploy an application, Kubernetes validates that your YAML syntax is correct, but it doesn't guarantee your app will actually work.
search_anchor: When you deploy an application
-->
<v-click>

<div class="mt-12 text-center text-xl">
Kubernetes validates YAML syntax
</div>

</v-click>

<!--
METADATA:
sentence: Get any of these wrong, and your app becomes unreachable.
search_anchor: Get any of these wrong
-->
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

<!--
METADATA:
sentence: Think of it like this: Kubernetes checks your spelling and grammar, but not whether your sentences make sense.
search_anchor: Think of it like this
-->
<v-click>

<div class="mt-12 text-center text-xl">
Checks spelling and grammar, not meaning
</div>

</v-click>

---

# Time Investment

<!--
METADATA:
sentence: And trust me, you'll spend a significant amount of your time tracking down these issues.
search_anchor: trust me, you'll spend a
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
You'll spend significant time tracking down issues
</div>

</v-click>

<!--
METADATA:
sentence: Your mission: diagnose the problems and fix them until the app runs successfully.
search_anchor: Your mission: diagnose the problems
-->
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

<!--
METADATA:
sentence: Do the selectors match?
search_anchor: Do the selectors match
-->
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

<!--
METADATA:
sentence: Services route traffic based on selectors and port configurations.
search_anchor: Services route traffic based on
-->
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

<!--
METADATA:
sentence: Third, container configuration - image names, commands, resource requests, and health probes.
search_anchor: Third, container configuration - image
-->
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

<!--
METADATA:
sentence: These components are loosely coupled.
search_anchor: These components are loosely coupled
-->
<v-click>

<div class="mt-12 text-center text-xl">
Components are loosely coupled
</div>

</v-click>

<!--
METADATA:
sentence: A typo in one place can break everything, but Kubernetes won't tell you directly what's wrong.
search_anchor: typo in one place can
-->
<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
Typo in one place can break everything
</div>

</v-click>

<!--
METADATA:
sentence: A typo in one place can break everything, but Kubernetes won't tell you directly what's wrong.
search_anchor: typo in one place can
-->
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

<!--
METADATA:
sentence: Let me walk you through the essentials: Start with "kubectl get" - this gives you the high-level status of your resources.
search_anchor: Let me walk you through
-->
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

<!--
METADATA:
sentence: Next, "kubectl describe" - this is your diagnostic deep-dive.
search_anchor: Next, "kubectl describe" - this
-->
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

<!--
METADATA:
sentence: Don't forget "kubectl logs" - when your container actually starts but behaves incorrectly, the logs tell you what's happening inside.
search_anchor: Don't forget "kubectl logs" -
-->
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

<!--
METADATA:
sentence: And finally, "kubectl port-forward" - this lets you bypass the Service layer and connect directly to a Pod, helping you isolate whether the problem is in the container or the networking configuration.
search_anchor: finally, "kubectl port-forward" - this
-->
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

<!--
METADATA:
sentence: Check your Deployment first - did it create a ReplicaSet?
search_anchor: Check your Deployment first -
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Check Deployment first
</div>

</v-click>

<!--
METADATA:
sentence: Did that ReplicaSet create Pods?
search_anchor: Did that ReplicaSet create Pods
-->
<v-click>

<div class="mt-8 text-center text-lg">
Did it create a ReplicaSet?
</div>

</v-click>

<!--
METADATA:
sentence: Did that ReplicaSet create Pods?
search_anchor: Did that ReplicaSet create Pods
-->
<v-click>

<div class="mt-6 text-center text-lg">
Did ReplicaSet create Pods?
</div>

</v-click>

<!--
METADATA:
sentence: Are those Pods actually running?
search_anchor: Are those Pods actually running
-->
<v-click>

<div class="mt-6 text-center text-lg">
Are Pods actually running?
</div>

</v-click>

<!--
METADATA:
sentence: Then move to networking.
search_anchor: Then move to networking
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Then move to networking
</div>

</v-click>

---

# Avoid Jumping to Conclusions

<!--
METADATA:
sentence: This systematic approach keeps you from jumping to conclusions and missing the actual root cause.
search_anchor: This systematic approach keeps you
-->
<v-click>

<div class="mt-12 text-center text-xl">
Systematic approach keeps you from missing root cause
</div>

</v-click>

<!--
METADATA:
sentence: Did that ReplicaSet create Pods?
search_anchor: Did that ReplicaSet create Pods
-->
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

<!--
METADATA:
sentence: Then move to networking.
search_anchor: Then move to networking
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-data-view-alt class="text-4xl text-blue-400" />
  <span class="text-lg">Container monitoring</span>
</div>

</v-click>

<!--
METADATA:
sentence: Did that ReplicaSet create Pods?
search_anchor: Did that ReplicaSet create Pods
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-debug class="text-4xl text-green-400" />
  <span class="text-lg">Diagnostics strategies</span>
</div>

</v-click>

<!--
METADATA:
sentence: --- Slide 3: Your Troubleshooting Toolkit (45 seconds) So how do we diagnose these problems?
search_anchor: --- Slide 3: Your Troubleshooting
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-tools-alt class="text-4xl text-purple-400" />
  <span class="text-lg">Troubleshooting approaches</span>
</div>

</v-click>

<!--
METADATA:
sentence: You won't just be writing manifests - you'll be debugging them.
search_anchor: You won't just be writing
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Not just writing manifests - debugging them
</div>

</v-click>

---

# Practical Skills

<!--
METADATA:
sentence: This lab gives you hands-on practice with the exact scenarios the exam tests.
search_anchor: This lab gives you hands-on
-->
<v-click>

<div class="mt-12 text-center text-xl">
This lab gives hands-on practice
</div>

</v-click>

<!--
METADATA:
sentence: This lab gives you hands-on practice with the exact scenarios the exam tests.
search_anchor: This lab gives you hands-on
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
With exact scenarios the exam tests
</div>

</v-click>

<!--
METADATA:
sentence: Your mission: diagnose the problems and fix them until the app runs successfully.
search_anchor: Your mission: diagnose the problems
-->
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

<!--
METADATA:
sentence: In this lab, you'll encounter a broken application with multiple issues.
search_anchor: this lab, you'll encounter a
-->
<v-click>

<div class="mt-12 text-center text-xl text-orange-400">
Application with multiple issues
</div>

</v-click>

<!--
METADATA:
sentence: Your mission: diagnose the problems and fix them until the app runs successfully.
search_anchor: Your mission: diagnose the problems
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Your mission: diagnose and fix
</div>

</v-click>

<!--
METADATA:
sentence: Your mission: diagnose the problems and fix them until the app runs successfully.
search_anchor: Your mission: diagnose the problems
-->
<v-click>

<div class="mt-12 text-center text-xl">
Until app runs successfully
</div>

</v-click>

<!--
METADATA:
sentence: --- Closing (10 seconds) Alright, let's put this into practice.
search_anchor: --- Closing (10 seconds) Alright
-->
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

<!--
METADATA:
sentence: Then move to networking.
search_anchor: Then move to networking
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Ready to Troubleshoot!
</div>

</v-click>

<!--
METADATA:
sentence: Next, "kubectl describe" - this is your diagnostic deep-dive.
search_anchor: Next, "kubectl describe" - this
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Put your diagnostic skills to the test
</div>

</v-click>

</div>
