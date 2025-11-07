---
theme: default
background: https://images.unsplash.com/photo-1667372393119-3d4c48d07fc9?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Kubernetes Deployments
  Managing containerized applications for AZ-204
drawings:
  persist: false
transition: slide-left
title: Deployments
mdc: true
---

# Kubernetes Deployments

Essential Controllers for Managing Applications

<div class="abs-bottom-10 left-10">
  <carbon-deployment-pattern class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<!--
METADATA:
sentence: That's where Deployments come in.
search_anchor: That's where Deployments come in
-->
<v-click>

<div class="text-xl mt-8">
Explore Kubernetes Deployments<br/>Critical for AKS and AZ-204
</div>

</v-click>

---
layout: section
---

# Why Not Create Pods Directly?

---

# The Problem with Direct Pods

<v-click>

<div class="mt-4">
  <carbon-warning class="text-6xl text-red-400" />
</div>

</v-click>

<!--
METADATA:
sentence: Can't I just create Pods directly?" Well, technically yes, but that would be like building a house with no foundation.
search_anchor: Can't I just create Pods
-->
<v-click>

<div class="mt-8 text-xl text-center text-red-400">
Creating Pods directly is like building without foundation
</div>

</v-click>

<!--
METADATA:
sentence: You can't update them to release new versions of your application.
search_anchor: You can't update them to
-->
<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-close class="text-4xl text-red-400" />
  <span class="text-lg">Can't update to new versions</span>
</div>

</v-click>

<!--
METADATA:
sentence: You can't easily scale them.
search_anchor: You can't easily scale them
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-close class="text-4xl text-red-400" />
  <span class="text-lg">Can't easily scale</span>
</div>

</v-click>

<!--
METADATA:
sentence: And if a Pod crashes, it's gone forever.
search_anchor: if a Pod crashes, it's
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-close class="text-4xl text-red-400" />
  <span class="text-lg">Pod crashes = gone forever</span>
</div>

</v-click>

---
layout: section
---

# Deployments as Controllers

---

# Smart Managers

<v-click>

<div class="mt-4">
  <carbon-network-4 class="text-6xl text-green-400" />
</div>

</v-click>

<!--
METADATA:
sentence: That's where Deployments come in.
search_anchor: That's where Deployments come in
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Deployments are controllers
</div>

</v-click>

<!--
METADATA:
sentence: When you create Pods directly, you're stuck.
search_anchor: When you create Pods directly
-->
<v-click>

<div class="mt-12 text-center text-xl">
They create and manage Pods for you
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Deployment[Deployment<br/>Controller] --> Pod1[Pod 1]
    Deployment --> Pod2[Pod 2]
    Deployment --> Pod3[Pod 3]
    style Deployment fill:#51cf66
    style Pod1 fill:#0078d4
    style Pod2 fill:#0078d4
    style Pod3 fill:#0078d4
```

</div>

</v-click>

---

# Declarative Approach

<!--
METADATA:
sentence: Let's explore what makes them so powerful.
search_anchor: Let's explore what makes them
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
"Here's what I want"
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Describe[Describe<br/>Desired State] --> K8s[Kubernetes]
    K8s --> Makes[Makes It Happen]
    style Describe fill:#51cf66
    style K8s fill:#0078d4
    style Makes fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: You describe your desired state in YAML, and Kubernetes figures out how to get there.
search_anchor: You describe your desired state
-->
<v-click>

<div class="mt-12 text-center text-xl">
Kubernetes figures out how to get there
</div>

</v-click>

---
layout: section
---

# Key Features

---

# Four Superpowers

<!--
METADATA:
sentence: You describe your desired state in YAML, and Kubernetes figures out how to get there.
search_anchor: You describe your desired state
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-document-tasks class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Declarative Updates</span>
    <div class="text-sm mt-2 opacity-70">Describe desired state in YAML</div>
    <div class="text-sm opacity-70">Kubernetes figures out how</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: When you release a new version, Deployments gradually replace old Pods with new ones, keeping your application available the whole time.
search_anchor: When you release a new
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-renew class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Rolling Updates</span>
    <div class="text-sm mt-2 opacity-70">Gradually replace old Pods with new</div>
    <div class="text-sm opacity-70">Application stays available</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: If something goes wrong, you can roll back to a previous version with a single command.
search_anchor: If something goes wrong, you
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-undo class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Easy Rollbacks</span>
    <div class="text-sm mt-2 opacity-70">Something wrong?</div>
    <div class="text-sm opacity-70">Roll back with single command</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Just update a number in your YAML or run a quick scale command.
search_anchor: Just update a number in
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-scale class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Simple Scaling</span>
    <div class="text-sm mt-2 opacity-70">Update replica count</div>
    <div class="text-sm opacity-70">In YAML or quick command</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Deployment Structure

---

# Three Main Parts

<!--
METADATA:
sentence: The Deployment uses a template to create Pods and a label selector to identify which Pods it owns.
search_anchor: Deployment uses a template to
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-tag class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Selector</span>
    <div class="text-sm mt-2 opacity-70">Which Pods does this Deployment manage?</div>
    <div class="text-sm opacity-70">Uses labels to identify</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The replica count specifies how many copies of your Pod you want running.
search_anchor: replica count specifies how many
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-hashtag class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Replica Count</span>
    <div class="text-sm mt-2 opacity-70">How many copies to run?</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: And the template is your Pod specification, the blueprint for creating new Pods.
search_anchor: template is your Pod specification
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-document-blank class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Template</span>
    <div class="text-sm mt-2 opacity-70">Pod specification blueprint</div>
    <div class="text-sm opacity-70">No name field - auto-generated</div>
  </div>
</div>

</v-click>

---

# YAML Structure

<v-click>

<div class="mt-8">

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: myapp:v1
```

</div>

</v-click>

---
layout: section
---

# Rolling Updates in Action

---

# Zero Downtime Updates

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Start[v1 Pods Running] --> Create[Create v2 Pod]
    Create --> Ready[Wait Until Ready]
    Ready --> Term[Terminate v1 Pod]
    Term --> More{More to Update?}
    More -->|Yes| Create
    More -->|No| Done[All Updated ✓]
    style Start fill:#0078d4
    style Create fill:#51cf66
    style Ready fill:#ffd43b
    style Term fill:#ff6b6b
    style Done fill:#51cf66
```

</div>

</v-click>

<!--
METADATA:
sentence: Your application stays available throughout the entire process.
search_anchor: Your application stays available throughout
-->
<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Application stays available throughout
</div>

</v-click>

---

# Gradual Process

<!--
METADATA:
sentence: When you update your container image or configuration, the Deployment doesn't just kill all your Pods and start over.
search_anchor: When you update your container
-->
<v-click>

<div class="mt-8 text-center text-xl">
Doesn't kill all Pods and start over
</div>

</v-click>

<!--
METADATA:
sentence: No disruption to users.
search_anchor: No disruption to users
-->
<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-renew class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Gradual Replacement</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">No Downtime</div>
  </div>
  <div class="text-center">
    <carbon-user-multiple class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">No User Disruption</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: And if you notice something wrong after the update, you can roll back just as smoothly.
search_anchor: if you notice something wrong
-->
<v-click>

<div class="mt-12 text-center text-xl">
Notice something wrong?
</div>

</v-click>

<!--
METADATA:
sentence: And if you notice something wrong after the update, you can roll back just as smoothly.
search_anchor: if you notice something wrong
-->
<v-click>

<div class="mt-4 text-center text-xl text-green-400">
Roll back just as smoothly
</div>

</v-click>

---
layout: section
---

# AZ-204 Exam Relevance

---

# Key Exam Areas

<!--
METADATA:
sentence: You should know how to implement container solutions using Azure Kubernetes Service.
search_anchor: You should know how to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-container-software class="text-4xl text-blue-400" />
  <span class="text-lg">Implement container solutions with AKS</span>
</div>

</v-click>

<!--
METADATA:
sentence: That means understanding Deployment manifests, scaling strategies, and update patterns.
search_anchor: That means understanding Deployment manifests
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document class="text-4xl text-green-400" />
  <span class="text-lg">Understand Deployment manifests</span>
</div>

</v-click>

<!--
METADATA:
sentence: And fourth, simple scaling.
search_anchor: fourth, simple scaling
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-scale class="text-4xl text-purple-400" />
  <span class="text-lg">Scaling strategies</span>
</div>

</v-click>

<!--
METADATA:
sentence: That means understanding Deployment manifests, scaling strategies, and update patterns.
search_anchor: That means understanding Deployment manifests
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-renew class="text-4xl text-orange-400" />
  <span class="text-lg">Update patterns</span>
</div>

</v-click>

---

# Application Lifecycle

<!--
METADATA:
sentence: Second, rolling updates.
search_anchor: Second, rolling updates
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-blue-400" />
  <span class="text-lg">Deploy updates</span>
</div>

</v-click>

<!--
METADATA:
sentence: Third, easy rollbacks.
search_anchor: Third, easy rollbacks
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-undo class="text-4xl text-green-400" />
  <span class="text-lg">Roll back changes</span>
</div>

</v-click>

<!--
METADATA:
sentence: Your application stays available throughout the entire process.
search_anchor: Your application stays available throughout
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-availability class="text-4xl text-purple-400" />
  <span class="text-lg">Maintain application availability</span>
</div>

</v-click>

---

# Imperative vs Declarative

<!--
METADATA:
sentence: And importantly, you should understand the difference between imperative commands, which you might use for quick testing, and declarative YAML files, which are the standard for production environments.
search_anchor: importantly, you should understand the
-->
<v-click>

<div class="mt-8 flex justify-center gap-16">
  <div class="text-center">
    <carbon-terminal class="text-6xl text-orange-400" />
    <div class="text-sm mt-3">Imperative Commands</div>
    <div class="text-xs mt-2 opacity-70">Quick testing</div>
  </div>
  <div class="text-center">
    <carbon-document-blank class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Declarative YAML</div>
    <div class="text-xs mt-2 opacity-70">Production standard</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Notice the template doesn't include a name field.
search_anchor: Notice the template doesn't include
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Know the difference
</div>

</v-click>

---
layout: section
---

# What's Next

---

# Hands-On Exercises

<!--
METADATA:
sentence: That's where Deployments come in.
search_anchor: That's where Deployments come in
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-add class="text-4xl text-blue-400" />
  <span class="text-lg">Create Deployments</span>
</div>

</v-click>

<!--
METADATA:
sentence: And fourth, simple scaling.
search_anchor: fourth, simple scaling
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-scale class="text-4xl text-green-400" />
  <span class="text-lg">Scale up and down</span>
</div>

</v-click>

<!--
METADATA:
sentence: Second, rolling updates.
search_anchor: Second, rolling updates
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-renew class="text-4xl text-purple-400" />
  <span class="text-lg">Perform rolling updates</span>
</div>

</v-click>

<!--
METADATA:
sentence: Third, easy rollbacks.
search_anchor: Third, easy rollbacks
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-undo class="text-4xl text-orange-400" />
  <span class="text-lg">Practice rollbacks</span>
</div>

</v-click>

<!--
METADATA:
sentence: You'll also tackle a blue-green deployment challenge that's perfect exam prep.
search_anchor: You'll also tackle a blue-green
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-red-400" />
  <span class="text-lg">Blue-green deployment challenge</span>
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
sentence: Let's explore what makes them so powerful.
search_anchor: Let's explore what makes them
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: That's where Deployments come in.
search_anchor: That's where Deployments come in
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Master Kubernetes Deployments
</div>

</v-click>

</div>
