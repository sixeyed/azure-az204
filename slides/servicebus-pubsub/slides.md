---
theme: default
layout: cover
---

# Service Bus Publish-Subscribe

<div class="abs-bottom-4">
  <iconify-icon icon="mdi:bus" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lab on Azure Service Bus Publish-Subscribe messaging

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Publish-Subscribe?

<div v-click>

```mermaid
graph LR
    A[Your Application] --> B[Package as Container]
    B --> C[Deploy to Azure]
    C --> D[Running in Cloud]

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
```

</div>

<div class="mt-8 text-center" v-click>

The publish-subscribe pattern is a messaging pattern where the component sending messages is called the publisher, and there can be zero or many compo...

</div>

---

---
layout: center
---

# Service Bus Topics

<div class="text-xl mt-8" v-click>

In Azure Service Bus, we implement the pub-sub pattern using topics. You might remember from a previous lab that we used Service Bus queues for point-to-point messaging. Topics are different - they're

</div>

---

---
layout: center
---

# Real-World Example

<div class="text-xl mt-8" v-click>

Let me give you a practical example. Imagine you're building an e-commerce application. When a customer places an order, you publish an "order-created" message to a topic. You might have multiple subs

</div>

---

---
layout: center
---

# Lab Objectives

<div class="text-xl mt-8" v-click>

In this lab, we'll:

</div>