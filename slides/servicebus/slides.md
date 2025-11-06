---
theme: default
layout: cover
---

# Service Bus Messaging

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

Welcome to this lab on Azure Service Bus messaging

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What is Service Bus?

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

Before we dive into the hands-on exercises, let's understand what Service Bus offers:...

</div>

---

---
layout: center
---

# Creating a Service Bus Namespace and Queue

<div class="text-xl mt-8" v-click>

Let's start by creating our Service Bus resources. First, understand that Service Bus uses a concept called a "namespace" - this is a grouping construct that can contain multiple queues, topics, and s

</div>

---

---
layout: center
---

# Running a .NET Subscriber

<div class="text-xl mt-8" v-click>

Now for the interesting part - let's run applications that use our queue. Subscribers listen on a queue in an infinite loop, processing messages as they arrive.

</div>

---

---
layout: center
---

# Running the Publisher

<div class="text-xl mt-8" v-click>

With our subscriber listening, let's send some messages. We have a publisher application that sends messages in batches.

</div>

---

---
layout: center
---

# Demonstrating Reliability

<div class="text-xl mt-8" v-click>

Service Bus's reliability features are what make it enterprise-grade. Let's test them.

</div>

---

---
layout: center
---

# Demonstrating Scalability

<div class="text-xl mt-8" v-click>

Service Bus also supports horizontal scaling. Let's see how multiple subscribers share the workload.

</div>

---

---
layout: center
---

# Lab Challenge

<div class="text-xl mt-8" v-click>

Now it's your turn to experiment. Here are two scenarios to explore:

</div>

---

---
layout: center
---

# Key Takeaways

<div class="text-xl mt-8" v-click>

Before we wrap up, let's review what we've learned:

</div>

---

---
layout: center
---

# Cleanup

<div class="text-xl mt-8" v-click>

When you're done experimenting, clean up your resources:

</div>

---

---
layout: center
---

# Next Steps

<div class="text-xl mt-8" v-click>

This lab covered the fundamentals of Service Bus queues. To continue learning:

</div>