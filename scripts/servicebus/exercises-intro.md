# Service Bus Messaging - Exercises Introduction

We've covered Service Bus as a high-throughput, reliable message queue service for building distributed applications with decoupled components. Now let's implement fire-and-forget messaging patterns with guaranteed delivery.

## What You'll Do

You'll start by **creating a Service Bus namespace and queue** using Azure CLI, understanding that a namespace is a grouping construct that can contain multiple queues, topics, and subscriptions. You'll select the Basic SKU for this introductory lab, which supports queues with 256 KB messages.

Then you'll **run a .NET subscriber application** that listens on the queue in an infinite loop, processing messages as they arrive. The subscriber demonstrates a critical pattern: it acknowledges messages after processing by calling CompleteMessageAsync, which tells Service Bus the message was successfully handled and can be removed from the queue.

You'll **run a publisher application** that sends messages in batches to demonstrate a best practice: batch messaging. Instead of making separate connections for each message, batching groups messages together for much better throughput and efficiency.

Next comes **testing reliability** by stopping the subscriber while the publisher continues running. Messages accumulate in the queue, safely persisted to disk until a consumer becomes available. When you restart the subscriber, it picks up exactly where it left off - no messages are lost. This reliability is the key insight: Service Bus stores messages until it receives a completion acknowledgement.

You'll also **test horizontal scaling** by running multiple subscriber instances simultaneously. Watch as Service Bus distributes messages across all available subscribers automatically - each message is processed by exactly one subscriber with no duplication. This is load balancing in action through the competing consumers pattern.

The key learning: Service Bus provides reliable, high-throughput messaging with built-in horizontal scaling, message persistence until acknowledgement, and standard protocol support through AMQP for interoperability.

Let's build reliable messaging systems with Service Bus!
