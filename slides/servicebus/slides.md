---
theme: default
background: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Service Bus Messaging
  Enterprise messaging for AZ-204
drawings:
  persist: false
transition: slide-left
title: Service Bus
mdc: true
---

# Azure Service Bus Messaging

Enterprise-Grade Message Queuing

<div class="abs-bottom-10 left-10">
  <carbon-send class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome

<v-click>

<div class="text-xl mt-8">
Explore Azure Service Bus<br/>Build decoupled, distributed applications
</div>

</v-click>

---
layout: section
---

# What is Service Bus?

---

# Powerful Messaging Service

<v-click>

<div class="mt-4">
  <carbon-send-alt class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center text-green-400">
High-throughput, reliable message queue
</div>

</v-click>

<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-flash class="text-4xl text-blue-400" />
  <span class="text-lg">Thousands of messages per second</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-data-backup class="text-4xl text-green-400" />
  <span class="text-lg">Messages stored until processed</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings-adjust class="text-4xl text-purple-400" />
  <span class="text-lg">Advanced features for enterprise needs</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-locked class="text-4xl text-orange-400" />
  <span class="text-lg">AMQP protocol support</span>
</div>

</v-click>

---

# Key Capabilities

<v-click>

<div class="mt-8 flex items-start gap-4">
  <carbon-warning class="text-4xl text-red-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Dead-Letter Queues</div>
    <div class="text-sm mt-2 opacity-70">Handle messages that couldn't be processed</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-flow class="text-4xl text-blue-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Message Sessions</div>
    <div class="text-sm mt-2 opacity-70">FIFO processing guarantees</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <carbon-checkmark-outline class="text-4xl text-green-400 mt-1" />
  <div>
    <div class="text-lg font-bold">Duplicate Detection</div>
    <div class="text-sm mt-2 opacity-70">Prevent duplicate message processing</div>
  </div>
</div>

</v-click>

---
layout: section
---

# Fire-and-Forget Pattern

---

# Asynchronous Communication

<v-click>

<div class="mt-8">

```mermaid
graph LR
    Publisher[Publisher] -->|Send| Queue[Service Bus Queue]
    Queue -->|Process| Consumer[Consumer]
    style Publisher fill:#0078d4
    style Queue fill:#51cf66
    style Consumer fill:#ffd43b
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Publisher sends without expecting return
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Doesn't know which component processes
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Fundamental to scalable, loosely-coupled systems
</div>

</v-click>

---
layout: section
---

# Service Bus Concepts

---

# Namespace and Queues

<v-click>

<div class="mt-8">

```mermaid
graph TB
    NS[Service Bus Namespace<br/>example.servicebus.windows.net] --> Q1[Queue 1]
    NS --> Q2[Queue 2]
    NS --> Q3[Queue 3]
    style NS fill:#0078d4
    style Q1 fill:#51cf66
    style Q2 fill:#51cf66
    style Q3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Namespace: grouping construct
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Contains multiple queues, topics, and subscriptions
</div>

</v-click>

---

# Pricing Tiers

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-pricing-traditional class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Basic</span>
    <div class="text-sm mt-2 opacity-70">Queues only, 256 KB messages</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-green-400 mt-1">2</div>
  <div>
    <carbon-pricing-traditional class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Standard</span>
    <div class="text-sm mt-2 opacity-70">Adds topics and subscriptions</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-3xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-pricing-premium class="text-3xl inline-block" />
    <span class="ml-3 text-lg font-bold">Premium</span>
    <div class="text-sm mt-2 opacity-70">Dedicated resources, 1 MB messages</div>
  </div>
</div>

</v-click>

---

# Access Control

<v-click>

<div class="mt-4">
  <carbon-security class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Shared access policies and tokens
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-send class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Send</div>
  </div>
  <div class="text-center">
    <carbon-view class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Listen</div>
  </div>
  <div class="text-center">
    <carbon-settings class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Manage</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Fine-grained permissions per policy
</div>

</v-click>

---
layout: section
---

# Subscriber Pattern

---

# How Subscribers Work

<v-click>

<div class="mt-8 text-center text-xl">
Listen on queue in infinite loop
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Sub[Subscriber] -->|1. Receive| Msg[Message]
    Msg -->|2. Process| Handle[Handle Message]
    Handle -->|3. Acknowledge| Complete[Complete]
    Complete -->|Loop| Sub
    style Sub fill:#0078d4
    style Msg fill:#ffd43b
    style Handle fill:#ffd43b
    style Complete fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
Acknowledgement is crucial
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Tells Service Bus message was handled
</div>

</v-click>

---

# Distributed Application

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-application class="text-4xl text-blue-400" />
  <span class="text-lg">Multiple components subscribe to different queues</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-scale class="text-4xl text-green-400" />
  <span class="text-lg">Multiple instances for scalability</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-3 class="text-4xl text-purple-400" />
  <span class="text-lg">AMQP standard protocol support</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Drop-in replacement for RabbitMQ
</div>

</v-click>

---
layout: section
---

# Demonstrating Reliability

---

# Message Persistence

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Pub[Publisher] -->|Sends| Queue[Queue Stores]
    Queue -.->|Subscriber Offline| Wait[Messages Wait]
    Wait -->|Subscriber Returns| Sub[Subscriber Processes]
    style Pub fill:#0078d4
    style Queue fill:#51cf66
    style Wait fill:#ffd43b
    style Sub fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
No messages lost
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Messages persist until acknowledged
</div>

</v-click>

---

# Key Insight

<v-click>

<div class="mt-12 text-center text-2xl">
Service Bus stores messages until completion
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Completed: Skip</div>
  </div>
  <div class="text-center">
    <carbon-time class="text-6xl text-orange-400" />
    <div class="text-sm mt-3">Uncompleted: Process</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Ensures requests aren't lost or duplicated
</div>

</v-click>

---
layout: section
---

# Demonstrating Scalability

---

# Load Balancing

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Queue[Service Bus Queue] --> Sub1[Subscriber 1]
    Queue --> Sub2[Subscriber 2]
    Queue --> Sub3[Subscriber 3]
    style Queue fill:#0078d4
    style Sub1 fill:#51cf66
    style Sub2 fill:#51cf66
    style Sub3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
Subscribers take turns receiving messages
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl text-green-400">
No message duplication
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Each message processed by exactly one subscriber
</div>

</v-click>

---

# Horizontal Scaling

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-scale class="text-6xl text-blue-400" />
    <div class="text-sm mt-3">Add Instances</div>
  </div>
  <div class="text-center">
    <carbon-flash class="text-6xl text-green-400" />
    <div class="text-sm mt-3">Increase Throughput</div>
  </div>
  <div class="text-center">
    <carbon-checkmark-outline class="text-6xl text-purple-400" />
    <div class="text-sm mt-3">Automatic Distribution</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Service Bus automatically distributes work
</div>

</v-click>

---
layout: section
---

# Key Takeaways

---

# What We Learned

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Reliable, high-throughput messaging</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Point-to-point with queues</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Built-in horizontal scaling</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Acknowledgement prevents loss/duplication</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-checkmark class="text-4xl text-green-400" />
  <span class="text-lg">Industry-standard AMQP protocol</span>
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
Build distributed systems with Service Bus
</div>

</v-click>

</div>
