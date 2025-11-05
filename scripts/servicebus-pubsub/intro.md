# Service Bus Publish-Subscribe - Introduction Script

## Opening

Welcome to this lab on Azure Service Bus Publish-Subscribe messaging. In this session, we're going to explore one of the most important patterns in asynchronous messaging: the publish-subscribe pattern, or pub-sub.

## What is Publish-Subscribe?

The publish-subscribe pattern is a messaging pattern where the component sending messages is called the publisher, and there can be zero or many components that subscribe to receive those messages. The key characteristic is that every subscriber gets a copy of each message.

This pattern is particularly powerful for building extensible architectures. You can add new subscribers with new functionality at any time, without making any changes to existing components. This decoupling is one of the fundamental principles of cloud-native application design.

## Service Bus Topics

In Azure Service Bus, we implement the pub-sub pattern using topics. You might remember from a previous lab that we used Service Bus queues for point-to-point messaging. Topics are different - they're designed for one-to-many communication.

When you publish a message to a topic, it gets forwarded to all active subscriptions on that topic. Each subscription acts as an independent message queue, receiving a copy of every message published to the topic.

## Real-World Example

Let me give you a practical example. Imagine you're building an e-commerce application. When a customer places an order, you publish an "order-created" message to a topic. You might have multiple subscriptions listening:

- A fulfilment subscription processes the shipping request
- An analytics subscription aggregates sales data
- An audit subscription logs the order details for compliance
- A notification subscription sends confirmation emails

Each of these components operates independently, processes messages at its own pace, and can be added or removed without affecting the others.

## Lab Objectives

In this lab, we'll:

1. Create a Service Bus namespace with Standard tier to support topics
2. Create a topic with specific time-to-live and size configurations
3. Add multiple subscriptions to demonstrate pub-sub messaging
4. Publish messages to the topic using a .NET application
5. Consume messages from different subscriptions
6. Explore what happens with multiple consumers

By the end of this lab, you'll understand how to design scalable, decoupled messaging architectures using Azure Service Bus topics.

Let's get started.
