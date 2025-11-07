---
theme: default
background: https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure SignalR Service
  Real-time two-way communication for AZ-204
drawings:
  persist: false
transition: slide-left
title: SignalR
mdc: true
---

# Azure SignalR Service

Real-Time Two-Way Communication

<div class="abs-bottom-10 left-10">
  <carbon-chat class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Azure SignalR Service<br/>Enable real-time communication in your apps
</div>

</v-click>

---
layout: section
---

# What is SignalR?

---

# Two-Way Communication

<v-click>

<div class="mt-4">
  <carbon-arrows-horizontal class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Real-time, two-way communication over internet
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Push updates to browsers in real-time
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Server[Web Server] -.->|Push Updates| Client1[Browser 1]
    Server -.->|Push Updates| Client2[Browser 2]
    Client1 -.->|Send Message| Server
    Client2 -.->|Send Message| Server
    style Server fill:#0078d4
    style Client1 fill:#51cf66
    style Client2 fill:#51cf66
```

</div>

</v-click>

---

# Use Cases

<v-click>

<div class="mt-8 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-chat class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Live Chat</div>
  </div>
  <div class="text-center">
    <carbon-dashboard class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Real-Time Dashboards</div>
  </div>
  <div class="text-center">
    <carbon-collaborate class="text-5xl text-purple-400" />
    <div class="text-sm mt-3">Collaborative Editing</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 grid grid-cols-3 gap-8">
  <div class="text-center">
    <carbon-notification class="text-5xl text-orange-400" />
    <div class="text-sm mt-3">Live Notifications</div>
  </div>
  <div class="text-center">
    <carbon-chart-line class="text-5xl text-red-400" />
    <div class="text-sm mt-3">Stock Tickers</div>
  </div>
  <div class="text-center">
    <carbon-game-wireless class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Gaming</div>
  </div>
</div>

</v-click>

---

# Microsoft's WebSockets for .NET

<v-click>

<div class="mt-12 text-center text-xl">
SignalR is Microsoft's customization of WebSockets
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-lg opacity-70">
Optimized for .NET applications
</div>

</v-click>

---
layout: section
---

# The Scaling Challenge

---

# Self-Hosted Problem

<v-click>

<div class="mt-8 text-center text-xl">
Each server instance maintains own client list
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    UserA[User A] --> Server1[Server 1<br/>Client List]
    UserB[User B] --> Server2[Server 2<br/>Client List]
    UserA -.->|Message| UserB
    style UserA fill:#ffd43b
    style UserB fill:#ff6b6b
    style Server1 fill:#0078d4
    style Server2 fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-red-400">
User A's message doesn't reach User B
</div>

</v-click>

---

# The Disconnect

<v-click>

<div class="mt-12 text-center text-xl">
User A connects to Server One
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
User B connects to Server Two
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-orange-400">
User A sends message
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Server One broadcasts to its clients only
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
User B never sees the message
</div>

</v-click>

---
layout: section
---

# Azure SignalR Service

---

# Centralized Hub

<v-click>

<div class="mt-4">
  <carbon-cloud-services class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Moves SignalR into managed component
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Web1[Web Server 1] --> SignalR[Azure SignalR Service<br/>Central Hub]
    Web2[Web Server 2] --> SignalR
    SignalR --> Client1[Client 1]
    SignalR --> Client2[Client 2]
    SignalR --> Client3[Client 3]
    style Web1 fill:#0078d4
    style Web2 fill:#0078d4
    style SignalR fill:#51cf66
    style Client1 fill:#ffd43b
    style Client2 fill:#ffd43b
    style Client3 fill:#ffd43b
```

</div>

</v-click>

---

# How It Works

<v-click>

<div class="mt-12 text-center text-xl">
App doesn't handle client connections directly
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Simply sends notifications to SignalR Service
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Service broadcasts to all connected clients
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Regardless of which web server they connected through
</div>

</v-click>

---

# Three Key Benefits

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-scale class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Scalability</span>
    <div class="text-sm mt-2 opacity-70">Run as many web servers as needed</div>
    <div class="text-sm opacity-70">No connection management worries</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-clean class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Simplified Infrastructure</span>
    <div class="text-sm mt-2 opacity-70">No additional backend for client state</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-checkmark-outline class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Azure-Managed Reliability</span>
    <div class="text-sm mt-2 opacity-70">High availability and automatic scaling</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Authentication Options

---

# Two Approaches

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-password class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Connection Strings with Access Keys</div>
    <div class="text-sm mt-2 opacity-70">Quick setup and testing</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-10 flex items-start gap-4">
  <carbon-id-management class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Managed Identities</div>
    <div class="text-sm mt-2 opacity-70">Production best practice</div>
    <div class="text-sm opacity-70">No credentials in app configuration</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Managed Identities for production
</div>

</v-click>

---
layout: section
---

# Important Distinction

---

# Broadcasting, Not Persistence

<v-click>

<div class="mt-12 text-center text-xl text-orange-400">
SignalR Service is for real-time broadcasting
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-red-400">
NOT data persistence
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Clients disconnect and reconnect
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Previous messages not automatically restored
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Need state? Use database separately
</div>

</v-click>

---
layout: section
---

# What We'll Build

---

# Hands-On Lab

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-development class="text-4xl text-blue-400" />
  <span class="text-lg">Run chat app locally</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-4xl text-orange-400" />
  <span class="text-lg">Observe scaling challenges</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-green-400" />
  <span class="text-lg">Integrate with Azure SignalR Service</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-purple-400" />
  <span class="text-lg">Deploy to Azure App Service</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-id-management class="text-4xl text-red-400" />
  <span class="text-lg">Configure Managed Identities</span>
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
Build real-time communication into your apps
</div>

</v-click>

</div>
