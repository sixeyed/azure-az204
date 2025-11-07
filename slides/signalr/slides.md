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

<!--
METADATA:
sentence: This is where Azure SignalR Service comes in.
search_anchor: This is where Azure SignalR
-->
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

<!--
METADATA:
sentence: SignalR is a technology designed for two-way communication over the internet.
search_anchor: SignalR is a technology designed
-->
<v-click>

<div class="mt-8 text-xl text-center text-green-400">
Real-time, two-way communication over internet
</div>

</v-click>

<!--
METADATA:
sentence: It allows web applications to push updates to browsers in real-time, supporting asynchronous delivery to the front end.
search_anchor: It allows web applications to
-->
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

<!--
METADATA:
sentence: Think of scenarios like live chat applications, real-time dashboards, collaborative editing tools, or live notification systems - all of these benefit from SignalR's capabilities.
search_anchor: Think of scenarios like live
-->
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

<!--
METADATA:
sentence: SignalR is Microsoft's customization of WebSockets for .NET.
search_anchor: SignalR is Microsoft's customization of
-->
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

<!--
METADATA:
sentence: SignalR is Microsoft's customization of WebSockets for .NET.
search_anchor: SignalR is Microsoft's customization of
-->
<v-click>

<div class="mt-12 text-center text-xl">
SignalR is Microsoft's customization of WebSockets
</div>

</v-click>

<!--
METADATA:
sentence: SignalR is Microsoft's customization of WebSockets for .NET.
search_anchor: SignalR is Microsoft's customization of
-->
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

<!--
METADATA:
sentence: When you run SignalR in your own application server, each server instance maintains its own list of connected clients.
search_anchor: When you run SignalR in
-->
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

<!--
METADATA:
sentence: User B never sees the message because they're connected to a different server instance.
search_anchor: User B never sees the
-->
<v-click>

<div class="mt-12 text-center text-xl text-red-400">
User A's message doesn't reach User B
</div>

</v-click>

---

# The Disconnect

<!--
METADATA:
sentence: User A connects to Server One, and User B connects to Server Two.
search_anchor: User A connects to Server
-->
<v-click>

<div class="mt-12 text-center text-xl">
User A connects to Server One
</div>

</v-click>

<!--
METADATA:
sentence: User A connects to Server One, and User B connects to Server Two.
search_anchor: User A connects to Server
-->
<v-click>

<div class="mt-8 text-center text-xl">
User B connects to Server Two
</div>

</v-click>

<!--
METADATA:
sentence: When User A sends a message, Server One broadcasts it - but only to clients connected to Server One.
search_anchor: When User A sends a
-->
<v-click>

<div class="mt-12 text-center text-xl text-orange-400">
User A sends message
</div>

</v-click>

<!--
METADATA:
sentence: When User A sends a message, Server One broadcasts it - but only to clients connected to Server One.
search_anchor: When User A sends a
-->
<v-click>

<div class="mt-8 text-center text-xl">
Server One broadcasts to its clients only
</div>

</v-click>

<!--
METADATA:
sentence: User B never sees the message because they're connected to a different server instance.
search_anchor: User B never sees the
-->
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

<!--
METADATA:
sentence: Azure SignalR Service Azure SignalR Service moves SignalR functionality into its own managed component.
search_anchor: Azure SignalR Service Azure SignalR
-->
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

<!--
METADATA:
sentence: The SignalR Service handles all client connections centrally.
search_anchor: SignalR Service handles all client
-->
<v-click>

<div class="mt-12 text-center text-xl">
App doesn't handle client connections directly
</div>

</v-click>

<!--
METADATA:
sentence: Instead of your web application dealing with client connections directly, it simply sends update notifications to the SignalR Service.
search_anchor: Instead of your web application
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Simply sends notifications to SignalR Service
</div>

</v-click>

<!--
METADATA:
sentence: The service then broadcasts that message to all connected clients, whether they're connected through the same server or different instances.
search_anchor: service then broadcasts that message
-->
<v-click>

<div class="mt-12 text-center text-xl">
Service broadcasts to all connected clients
</div>

</v-click>

<!--
METADATA:
sentence: The service acts as a central hub that broadcasts messages to all connected clients, regardless of which web server they originally connected through.
search_anchor: service acts as a central
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Regardless of which web server they connected through
</div>

</v-click>

---

# Three Key Benefits

<!--
METADATA:
sentence: This architecture provides several key benefits: First, scalability - you can run as many web server instances as needed without worrying about connection management.
search_anchor: This architecture provides several key
-->
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

<!--
METADATA:
sentence: Second, simplified infrastructure - you don't need to maintain additional backend infrastructure for managing client state across servers.
search_anchor: Second, simplified infrastructure - you
-->
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

<!--
METADATA:
sentence: Third, Azure-managed reliability - the service is fully managed by Azure, providing high availability and automatic scaling.
search_anchor: Third, Azure-managed reliability - the
-->
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

<!--
METADATA:
sentence: You can use connection strings with access keys for quick setup and testing.
search_anchor: You can use connection strings
-->
<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-password class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Connection Strings with Access Keys</div>
    <div class="text-sm mt-2 opacity-70">Quick setup and testing</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: For production scenarios, you'll want to use Managed Identities, which eliminate the need to store sensitive credentials in your application configuration.
search_anchor: production scenarios, you'll want to
-->
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

<!--
METADATA:
sentence: For production scenarios, you'll want to use Managed Identities, which eliminate the need to store sensitive credentials in your application configuration.
search_anchor: production scenarios, you'll want to
-->
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

<!--
METADATA:
sentence: Important Distinction One critical thing to understand: SignalR Service is for real-time broadcasting, not data persistence.
search_anchor: Important Distinction One critical thing
-->
<v-click>

<div class="mt-12 text-center text-xl text-orange-400">
SignalR Service is for real-time broadcasting
</div>

</v-click>

<!--
METADATA:
sentence: Important Distinction One critical thing to understand: SignalR Service is for real-time broadcasting, not data persistence.
search_anchor: Important Distinction One critical thing
-->
<v-click>

<div class="mt-12 text-center text-xl text-red-400">
NOT data persistence
</div>

</v-click>

<!--
METADATA:
sentence: When clients disconnect and reconnect, previous messages are not automatically restored.
search_anchor: When clients disconnect and reconnect
-->
<v-click>

<div class="mt-12 text-center text-xl">
Clients disconnect and reconnect
</div>

</v-click>

<!--
METADATA:
sentence: When clients disconnect and reconnect, previous messages are not automatically restored.
search_anchor: When clients disconnect and reconnect
-->
<v-click>

<div class="mt-8 text-center text-xl">
Previous messages not automatically restored
</div>

</v-click>

<!--
METADATA:
sentence: If your application needs to maintain state - like preserving chat history - you'll need to implement that separately using a database or other storage solution.
search_anchor: If your application needs to
-->
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

<!--
METADATA:
sentence: The Scaling Challenge Here's the problem: imagine you're running a chat application with two web servers.
search_anchor: Scaling Challenge Here's the problem
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-development class="text-4xl text-blue-400" />
  <span class="text-lg">Run chat app locally</span>
</div>

</v-click>

<!--
METADATA:
sentence: The Scaling Challenge Here's the problem: imagine you're running a chat application with two web servers.
search_anchor: Scaling Challenge Here's the problem
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-warning class="text-4xl text-orange-400" />
  <span class="text-lg">Observe scaling challenges</span>
</div>

</v-click>

<!--
METADATA:
sentence: This is where Azure SignalR Service comes in.
search_anchor: This is where Azure SignalR
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-cloud-services class="text-4xl text-green-400" />
  <span class="text-lg">Integrate with Azure SignalR Service</span>
</div>

</v-click>

<!--
METADATA:
sentence: We'll deploy the application to Azure App Service and configure secure authentication using Managed Identities.
search_anchor: We'll deploy the application to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-deployment-pattern class="text-4xl text-purple-400" />
  <span class="text-lg">Deploy to Azure App Service</span>
</div>

</v-click>

<!--
METADATA:
sentence: We'll deploy the application to Azure App Service and configure secure authentication using Managed Identities.
search_anchor: We'll deploy the application to
-->
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

<!--
METADATA:
sentence: Let's get started with the practical exercises.
search_anchor: Let's get started with the
-->
<v-click>

<div class="text-4xl mt-8 font-bold">
Let's Get Started!
</div>

</v-click>

<!--
METADATA:
sentence: In this session, we'll explore how Azure enables real-time, two-way communication between web applications and clients.
search_anchor: this session, we'll explore how
-->
<v-click>

<div class="text-xl mt-6 opacity-70">
Build real-time communication into your apps
</div>

</v-click>

</div>
