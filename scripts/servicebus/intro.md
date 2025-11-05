# Service Bus Messaging - Introduction Narration Script

## Opening

Welcome to this lab on Azure Service Bus messaging. In this session, we'll explore one of Azure's most powerful messaging services - Service Bus. This is a high-throughput, reliable message queue service that enables you to build distributed applications with decoupled components.

Service Bus is particularly useful for implementing asynchronous communication patterns where reliability is critical. Messages are stored until they're processed, and there are advanced features like dead-letter queues for messages that couldn't be delivered or failed processing.

Today, we'll implement a fire-and-forget messaging pattern, where a publisher sends messages without expecting a return or even knowing which component will process them. This pattern is fundamental to building scalable, loosely-coupled systems.

## What is Service Bus?

Before we dive into the hands-on exercises, let's understand what Service Bus offers:

- **High throughput message queuing** - Handle thousands of messages per second
- **Reliable storage** - Messages are persisted until they're successfully processed
- **Advanced features** - Including dead-letter queues, message sessions, and duplicate detection
- **Standard protocol support** - Uses AMQP (Advanced Message Queuing Protocol)

Service Bus is ideal when you need guaranteed message delivery and advanced messaging patterns. If you just need simple queuing, Azure Queue Storage might be sufficient, but Service Bus provides enterprise-grade messaging capabilities.

## Creating a Service Bus Namespace and Queue

Let's start by creating our Service Bus resources. First, understand that Service Bus uses a concept called a "namespace" - this is a grouping construct that can contain multiple queues, topics, and subscriptions.

### Using the Azure Portal

You can create a Service Bus namespace through the Portal by searching for "service bus" and creating a new Service Bus resource. When you do this, note a few key points:

- The namespace name gives you a unique subdomain at `.servicebus.windows.net`
- Pricing tiers determine maximum message size, available features, and operation limits
- Basic tier supports queues only with 256 KB messages
- Standard tier adds topics and subscriptions
- Premium tier provides dedicated resources and 1 MB messages

### Using the Azure CLI

For this lab, we'll use the CLI for better repeatability. Let's start by creating a resource group:

```bash
az group create -n labs-servicebus --tags courselabs=azure -l westeurope
```

Now, create a Service Bus namespace. We'll use the Basic SKU for this introductory lab:

```bash
az servicebus namespace create \
  -g labs-servicebus \
  --location westeurope \
  --sku Basic \
  -n <sb-name>
```

Replace `<sb-name>` with your unique namespace name. The output includes the service bus endpoint - notice that communication happens over HTTPS, ensuring secure message transmission.

### Exploring the Namespace

Once created, open your Service Bus namespace in the Azure Portal. You'll see several important sections:

- **Queues** - Where we'll create our message queues
- **Shared access policies** - Used for authentication and authorization

Shared access tokens work similarly to storage accounts, with one key difference: there's a one-to-one relationship between policies and tokens. Each policy defines specific permissions like Send, Listen, or Manage.

### Creating a Queue

With the Basic SKU, queues are your only messaging option. Let's create one:

```bash
az servicebus queue create \
  -g labs-servicebus \
  --name echo \
  --namespace-name <sb-name>
```

In the Portal, you can now see your queue with metrics showing message counts. There's also a Shared access policies tab at the queue level, enabling fine-grained permissions. For example, you could give one application Send-only permissions to one queue and Listen-only permissions to another.

## Running a .NET Subscriber

Now for the interesting part - let's run applications that use our queue. Subscribers listen on a queue in an infinite loop, processing messages as they arrive.

### Understanding the Subscriber Pattern

In a distributed application, you typically have:
- Multiple components, each subscribing to different queues
- Multiple instances of each component for scalability
- Standard protocol support (AMQP) for interoperability

Service Bus uses AMQP, which is an industry-standard protocol. This means Service Bus can be a drop-in replacement for other queue technologies like RabbitMQ.

### The Subscriber Application

Our subscriber application is straightforward:
- It subscribes to the queue using the Service Bus client library
- When it receives a message, it prints the contents
- Then it acknowledges that the message has been processed

This acknowledgement is crucial - it tells Service Bus the message was successfully handled and can be removed from the queue.

### Getting Your Connection String

First, retrieve your connection string. This contains the endpoint and credentials needed to connect:

```bash
az servicebus namespace authorization-rule keys list \
  -n RootManageSharedAccessKey \
  -g labs-servicebus \
  --query primaryConnectionString \
  -o tsv \
  --namespace-name <sb-name>
```

This returns a connection string that looks like:
```
Endpoint=sb://<namespace>.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=<sas-key>
```

**Important:** Keep this connection string secure - it provides full access to your Service Bus namespace.

### Running the Subscriber

Now run the subscriber application locally. You'll need the .NET 6 SDK installed:

```bash
dotnet run --project src/servicebus/subscriber -cs '<servicebus-connection-string>'
```

The application starts and waits for messages. It will continue listening until you stop it with Ctrl-C or Cmd-C.

## Running the Publisher

With our subscriber listening, let's send some messages. We have a publisher application that sends messages in batches.

### Understanding Batch Publishing

The publisher demonstrates a best practice: batch messaging. Instead of making separate connections for each message, it groups messages into batches. This is much more efficient and provides better throughput.

### Running the Publisher

In a separate terminal window, run:

```bash
dotnet run --project src/servicebus/publisher -cs '<servicebus-connection-string>'
```

The publisher sends batches of messages with delays between batches. Watch your subscriber console - you'll see messages being received and processed in real-time.

In the Azure Portal, you can also watch the metrics. With just one subscriber and one publisher, the message rate isn't high yet, but you can see the activity.

## Demonstrating Reliability

Service Bus's reliability features are what make it enterprise-grade. Let's test them.

### Testing Message Persistence

Make note of the last batch number processed by your subscriber. Now stop the subscriber (Ctrl-C or Cmd-C), but leave the publisher running.

The publisher continues sending messages. Without a subscriber, these messages accumulate in the queue. This is exactly what we want - Service Bus persists messages until they're processed.

Wait for the publisher to send a few more batches, then restart your subscriber:

```bash
dotnet run --project src/servicebus/subscriber -cs '<servicebus-connection-string>'
```

Watch what happens. The subscriber picks up where it left off, processing all the batches that were sent while it was offline. No messages were lost.

**This is the key insight:** Service Bus queues store messages until they receive a completion acknowledgement. New subscribers don't get messages that were already completed, but they do get all uncompleted messages. This ensures requests aren't lost or processed twice if a subscriber fails.

## Demonstrating Scalability

Service Bus also supports horizontal scaling. Let's see how multiple subscribers share the workload.

### Running Multiple Subscribers

With your first subscriber still running, open another terminal and start a second subscriber instance:

```bash
dotnet run --project src/servicebus/subscriber -cs '<servicebus-connection-string>'
```

Now watch both subscribers. They take turns receiving messages - Service Bus distributes the work between them. There's no message duplication; each message is processed by exactly one subscriber.

This is load balancing in action. As your message volume increases, you can scale out by adding more subscriber instances. Service Bus automatically distributes messages across all available subscribers.

## Lab Challenge

Now it's your turn to experiment. Here are two scenarios to explore:

### Challenge 1: Multiple Publishers

We've seen how multiple subscribers share the work. What about multiple publishers?

- Start multiple instances of the publisher
- How do the subscribers handle messages from different publishers?
- Does message ordering change?

### Challenge 2: Reliability Without Acknowledgement

Reliability depends on message acknowledgement. What happens when you disable it?

- Run the subscriber with the `-ack False` flag to disable acknowledgement
- Stop and restart the subscriber
- What happens to messages it already processed?

Think about why this behavior occurs and what it means for building reliable systems.

## Key Takeaways

Before we wrap up, let's review what we've learned:

1. **Service Bus provides reliable, high-throughput messaging** - Messages are persisted until acknowledged
2. **Queues enable point-to-point messaging** - Each message is processed by exactly one subscriber
3. **Horizontal scaling is built-in** - Multiple subscribers automatically share the workload
4. **Message acknowledgement is crucial** - It ensures messages aren't lost or duplicated
5. **Service Bus uses industry standards** - AMQP protocol enables interoperability

## Cleanup

When you're done experimenting, clean up your resources:

```bash
az group delete -y --no-wait -n labs-servicebus
```

This deletes the resource group and all contained resources.

## Next Steps

This lab covered the fundamentals of Service Bus queues. To continue learning:

- Explore topics and subscriptions for pub/sub patterns
- Learn about message sessions for FIFO processing
- Understand dead-letter queues for handling failures
- Study the AZ-204 exam scenarios for Service Bus

Thank you for completing this lab. Service Bus is a powerful tool for building distributed systems, and you now have hands-on experience with its core features.
