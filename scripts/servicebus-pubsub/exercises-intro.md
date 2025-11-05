# Service Bus Publish-Subscribe - Exercises Introduction

We've covered the publish-subscribe pattern where publishers send messages without knowing which subscribers will receive them, and every subscriber gets a copy of each message. Now let's implement the fan-out pattern for extensible architectures.

## What You'll Do

You'll start by **creating a Service Bus namespace with Standard tier** since the Basic tier only supports queues - topics require Standard or higher. Understanding tier requirements is important: Basic supports queues only, Standard adds topics and subscriptions, and Premium adds dedicated resources and larger messages.

Then you'll **create a Service Bus topic** with specific time-to-live and size configurations. Topics are destinations for publishers to send messages, supporting multiple subscriptions where messages are forwarded to all active subscriptions.

You'll **create multiple subscriptions** on the topic - one called "web" and one called "desktop" representing different client applications. These subscriptions act as independent message queues, each receiving a copy of every message published to the topic. This is the fan-out pattern in action.

Next, you'll **create authorization rules** following the principle of least privilege. You'll create separate policies: one with Send-only rights for publishers and another with Listen-only rights for subscribers. This security best practice ensures that if credentials are compromised, they can only be used for their intended purpose.

You'll **run a publisher application** that sends messages to the topic. From the publisher's perspective, the code is identical to sending to a queue - it doesn't need to know the difference. Service Bus abstracts the complexity.

Then you'll **run subscriber applications** on different subscriptions and observe how each subscription maintains its own independent message state. Messages consumed from one subscription don't affect other subscriptions - each processes at its own pace.

The key learning: Topics enable publish-subscribe messaging where one message reaches multiple subscribers, each subscription maintains independent state, and subscribers can be added or removed without affecting the system. This decoupling is fundamental to cloud-native application design.

Let's build scalable pub-sub systems with Service Bus topics!
