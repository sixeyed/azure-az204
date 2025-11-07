---
theme: default
background: https://images.unsplash.com/photo-1516110833967-0b5716ca1387?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Durable Functions - Human Interaction
  Workflows that wait for people - AZ-204
drawings:
  persist: false
transition: slide-left
title: Human Interaction
mdc: true
---

# Durable Functions: Human Interaction

Workflows That Wait for People

<div class="abs-bottom-10 left-10">
  <carbon-user-activity class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore the Human Interaction pattern<br/>Essential for real-world serverless applications
</div>

</v-click>

---
layout: section
---

# The Challenge

---

# Workflows That Wait

<v-click>

<div class="mt-8 text-center text-xl">
Common business scenarios
</div>

</v-click>

<v-click>

<div class="mt-12 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-document-tasks class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Purchase Approval</div>
  </div>
  <div class="text-center">
    <carbon-password class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Password Reset</div>
  </div>
  <div class="text-center">
    <carbon-ticket class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Support Review</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
All need to pause and wait for a person
</div>

</v-click>

---

# Traditional Approach Problems

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-warning class="text-4xl text-red-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Store in Database</div>
    <div class="text-sm mt-2 opacity-70">Security risks with sensitive data</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-money class="text-4xl text-orange-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Keep Service Running</div>
    <div class="text-sm mt-2 opacity-70">Expensive and inefficient</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Durable Functions solve this elegantly
</div>

</v-click>

---
layout: section
---

# The Durable Solution

---

# Pause Without Running

<v-click>

<div class="mt-4">
  <carbon-sleep class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Functions pause for extended periods
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg">
Minutes, hours, even days
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Start[Function Starts] --> Wait[Pause]
    Wait -.->|No Compute| Sleep[Suspended]
    Sleep -.->|No Cost| Sleep
    Response[Human Response] --> Resume[Resume]
    style Start fill:#0078d4
    style Wait fill:#ffd43b
    style Sleep fill:#gray
    style Response fill=#51cf66
    style Resume fill:#51cf66
```

</div>

</v-click>

---

# Key Advantages

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-close class="text-4xl text-green-400" />
  <span class="text-lg">No compute resources consumed during wait</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-green-400" />
  <span class="text-lg">No sensitive data in external storage</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-reset class="text-4xl text-green-400" />
  <span class="text-lg">Resumes exactly where it left off</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Perfect for human-in-the-loop workflows
</div>

</v-click>

---
layout: section
---

# Key Components

---

# Two Core Concepts

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-send class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">External Events</span>
    <div class="text-sm mt-2 opacity-70">Send information into running orchestration</div>
    <div class="text-sm opacity-70">Wakes up waiting function</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-time class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Durable Timers</span>
    <div class="text-sm mt-2 opacity-70">Humans don't always respond promptly</div>
    <div class="text-sm opacity-70">Set timeout window for response</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Start[Send Request] --> Wait[Wait for Response]
    Wait -->|Event Received| Success[Process Response]
    Wait -->|Timeout| Fail[Handle Timeout]
    style Start fill:#0078d4
    style Wait fill:#ffd43b
    style Success fill:#51cf66
    style Fail fill:#ff6b6b
```

</div>

</v-click>

---
layout: section
---

# Real-World Example

---

# Two-Factor Authentication

<v-click>

<div class="mt-8 text-center text-xl">
How it works
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Phone[Receive Phone Number] --> Send[Send SMS Code]
    Send --> Wait[Wait for Response]
    Wait -->|Correct Code<br/>Within Time| Auth[Authenticated ✓]
    Wait -->|Wrong Code<br/>or Timeout| Fail[Authentication Failed ❌]
    style Phone fill:#0078d4
    style Send fill:#0078d4
    style Wait fill:#ffd43b
    style Auth fill=#51cf66
    style Fail fill:#ff6b6b
```

</div>

</v-click>

---

# The Flow

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-phone class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Function receives phone number</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-send class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Sends SMS with verification code</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-time class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Waits for user response (with timeout)</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-orange-400 mt-1">4</div>
  <div>
    <carbon-checkmark class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Validates code and timing</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Integrates with Twilio for SMS
</div>

</v-click>

---
layout: section
---

# Why This Matters for AZ-204

---

# Exam Focus Areas

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-event class="text-4xl text-blue-400" />
  <span class="text-lg">Know when to use external events vs other triggers</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-time class="text-4xl text-green-400" />
  <span class="text-lg">Understand durable timers and timeout logic</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-decision-tree class="text-4xl text-purple-400" />
  <span class="text-lg">Recognize scenarios for this pattern</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Practical solution for production applications
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Appears in workflow and state management questions
</div>

</v-click>

---
layout: section
---

# What You'll Learn Today

---

# Lab Objectives

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings class="text-4xl text-blue-400" />
  <span class="text-lg">Set up Twilio account for SMS</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-flow class="text-4xl text-green-400" />
  <span class="text-lg">Build orchestration with verification codes</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-laptop class="text-4xl text-purple-400" />
  <span class="text-lg">Test locally with Storage Emulator</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud class="text-4xl text-orange-400" />
  <span class="text-lg">Deploy to Azure</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-api class="text-4xl text-red-400" />
  <span class="text-lg">Work with HTTP endpoints for events and status</span>
</div>

</v-click>

---

# Hands-On Experience

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-code class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Build Pattern</div>
  </div>
  <div class="text-center">
    <carbon-test-tool class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Test Workflow</div>
  </div>
  <div class="text-center">
    <carbon-deployment-pattern class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Deploy to Production</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
One of the most powerful patterns in Azure Functions
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
Let's Get Started!
</div>

</v-click>

<v-click>

<div class="text-xl mt-6 opacity-70">
Build powerful human-in-the-loop workflows
</div>

</v-click>

</div>
