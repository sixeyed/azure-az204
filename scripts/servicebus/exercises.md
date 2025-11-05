# Service Bus Messaging - Hands-On Exercises Narration Script

## Exercise Overview

Welcome to the hands-on exercises for Azure Service Bus. In this session, you'll get practical experience with Service Bus queues, publishers, subscribers, and reliability features. By the end, you'll understand how to build scalable, reliable messaging solutions in Azure.

## Prerequisites Check

Before we begin, make sure you have:

- Azure CLI installed and authenticated
- .NET 6 SDK installed (for running the sample applications)
- An active Azure subscription
- Access to the lab source code

Let's verify your .NET installation:

```bash
dotnet --version
```

You should see version 6.0 or later.

## Exercise 1: Create Service Bus Resources

### Step 1: Create Resource Group

Let's start by creating a dedicated resource group for this lab. We'll tag it so we can track lab resources:

```bash
az group create -n labs-servicebus --tags courselabs=azure -l westeurope
```

The output confirms the resource group is created in West Europe.

### Step 2: Understand Service Bus Tiers

Before creating the namespace, let's understand the pricing tiers:

- **Basic**: Queues only, 256 KB max message size, pay-per-use
- **Standard**: Adds topics and subscriptions, 256 KB messages
- **Premium**: Dedicated resources, 1 MB messages, predictable performance

For this lab, we'll use Basic tier to keep costs low.

### Step 3: Create Service Bus Namespace

Create the namespace. Remember, a namespace is a container for queues, topics, and subscriptions:

```bash
az servicebus namespace create \
  -g labs-servicebus \
  --location westeurope \
  --sku Basic \
  -n <sb-name>
```

Replace `<sb-name>` with something unique, like `sb-yourname-001`.

**What to observe in the output:**
- The `serviceBusEndpoint` - this is your HTTPS endpoint
- The `location` - confirms deployment region
- The `sku` - confirms Basic tier

The namespace is now accessible at `<sb-name>.servicebus.windows.net`.

### Step 4: Explore in Portal

Open the Azure Portal and navigate to your Service Bus namespace. Take a moment to explore:

- **Overview** - Shows metrics and key information
- **Queues** - Currently empty
- **Shared access policies** - Shows `RootManageSharedAccessKey` by default
- **Metrics** - Will show activity once we start sending messages

### Step 5: Create a Queue

Now create your first queue named "echo":

```bash
az servicebus queue create \
  -g labs-servicebus \
  --name echo \
  --namespace-name <sb-name>
```

In the Portal, refresh and you'll see the "echo" queue appear. Click it to explore:

- **Overview** - Message count metrics (currently zero)
- **Shared access policies** - Queue-level access control
- **Messages** - Can peek at messages without removing them

## Exercise 2: Run a Subscriber Application

### Step 1: Understand the Subscriber Code

Before running the subscriber, let's understand what it does. The subscriber application:

1. Connects to the Service Bus namespace
2. Creates a receiver for the "echo" queue
3. Enters an infinite loop, listening for messages
4. When a message arrives, it prints the content
5. Acknowledges the message (calls `CompleteMessageAsync`)

The acknowledgement is critical - it tells Service Bus the message was processed successfully.

### Step 2: Get Connection String

To connect, your application needs a connection string:

```bash
az servicebus namespace authorization-rule keys list \
  -n RootManageSharedAccessKey \
  -g labs-servicebus \
  --query primaryConnectionString \
  -o tsv \
  --namespace-name <sb-name>
```

This returns a connection string like:
```
Endpoint=sb://<namespace>.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=<sas-key>
```

Copy this entire string - you'll need it for the next step.

### Step 3: Run the Subscriber

Start the subscriber application:

```bash
dotnet run --project src/servicebus/subscriber -cs '<servicebus-connection-string>'
```

**Important:** Replace `<servicebus-connection-string>` with your actual connection string. Keep the single quotes to prevent shell interpretation.

The application starts and displays:
```
Listening for messages on queue: echo
Press Ctrl+C to exit
```

The subscriber is now waiting for messages. Keep this terminal window open.

## Exercise 3: Run a Publisher Application

### Step 1: Understand the Publisher Code

The publisher application:

1. Connects to the Service Bus namespace
2. Creates a sender for the "echo" queue
3. Sends messages in batches (more efficient than individual sends)
4. Waits between batches to simulate realistic workloads

Batch sending is a best practice - it reduces network overhead and improves throughput.

### Step 2: Run the Publisher

Open a **new terminal window** and run the publisher:

```bash
dotnet run --project src/servicebus/publisher -cs '<servicebus-connection-string>'
```

Use the same connection string you used for the subscriber.

### Step 3: Observe Message Flow

Watch what happens:

**In the publisher window:**
```
Sending batch 1...
Sent 10 messages
Waiting...
Sending batch 2...
Sent 10 messages
...
```

**In the subscriber window:**
```
Received message: Message 1 from batch 1
Received message: Message 2 from batch 1
Received message: Message 3 from batch 1
...
```

**In the Azure Portal:**
- Navigate to your queue
- Watch the message count metrics
- You might see brief spikes when batches are sent

This is real-time messaging in action!

## Exercise 4: Test Message Persistence

Now we'll test Service Bus's reliability features.

### Step 1: Note Current Progress

Look at your subscriber window and note the last batch number it processed. For example:
```
Received message: Message 10 from batch 5
```

Remember "batch 5".

### Step 2: Stop the Subscriber

In the subscriber window, press **Ctrl+C** (or **Cmd+C** on Mac) to stop it.

The subscriber shuts down and stops processing messages.

### Step 3: Let Messages Accumulate

Keep the publisher running. It continues sending batches:
```
Sending batch 6...
Sending batch 7...
Sending batch 8...
```

But there's no subscriber to process them. Where do these messages go? They're stored in the Service Bus queue, waiting to be processed.

### Step 4: Check the Portal

In the Azure Portal:
- Go to your queue's Overview
- Watch the "Active Message Count" increase
- Each batch adds 10 messages

This demonstrates message persistence - messages are safely stored even when no subscribers are active.

### Step 5: Restart the Subscriber

Now restart the subscriber:

```bash
dotnet run --project src/servicebus/subscriber -cs '<servicebus-connection-string>'
```

Watch carefully. The subscriber immediately starts processing messages from where it left off:

```
Received message: Message 1 from batch 6
Received message: Message 2 from batch 6
...
```

**Critical observation:** No messages were lost. The subscriber picked up all messages sent while it was offline.

### Why This Matters

This reliability is essential for distributed systems:
- Subscribers can restart without losing messages
- Deployment updates don't cause message loss
- Temporary failures don't impact message delivery

Service Bus stores messages until it receives a completion acknowledgement. Only then are messages removed from the queue.

## Exercise 5: Test Horizontal Scaling

### Step 1: Understand Load Balancing

Service Bus supports multiple subscribers consuming from the same queue. Messages are distributed across subscribers - this is automatic load balancing.

### Step 2: Run a Second Subscriber

With your first subscriber still running, open a **third terminal window** and start another subscriber:

```bash
dotnet run --project src/servicebus/subscriber -cs '<servicebus-connection-string>'
```

Now you have:
- Terminal 1: Publisher
- Terminal 2: Subscriber 1
- Terminal 3: Subscriber 2

### Step 3: Observe Load Distribution

Watch both subscriber terminals. You'll see messages distributed between them:

**Subscriber 1:**
```
Received message: Message 1 from batch 10
Received message: Message 3 from batch 10
Received message: Message 5 from batch 10
```

**Subscriber 2:**
```
Received message: Message 2 from batch 10
Received message: Message 4 from batch 10
Received message: Message 6 from batch 10
```

Service Bus distributes messages in a round-robin fashion (approximately). Each message is processed by exactly one subscriber - there's no duplication.

### Step 4: Test Scaling Behavior

Stop one subscriber (Ctrl+C). The remaining subscriber takes over all message processing.

Start the subscriber again. Load distribution resumes.

**This is horizontal scaling:** Add more subscribers to handle increased load. Remove subscribers to save resources. Service Bus handles the distribution automatically.

## Exercise 6: Portal Metrics

### Viewing Queue Metrics

In the Azure Portal:

1. Navigate to your queue
2. Click **Metrics** in the left menu
3. Add a chart for:
   - **Incoming Messages** - Messages published
   - **Outgoing Messages** - Messages delivered
   - **Active Messages** - Messages waiting in queue

### Understanding the Metrics

With both publisher and subscribers running:
- Incoming and outgoing rates should be similar
- Active message count should stay low

Stop all subscribers:
- Incoming messages continue
- Outgoing messages stop
- Active message count increases

This visual feedback helps you monitor queue health in production.

## Lab Challenge: Experimentation Time

Now that you understand the basics, try these challenges:

### Challenge 1: Multiple Publishers

**Scenario:** Multiple systems publishing to the same queue.

**Tasks:**
1. Run two publisher instances simultaneously
2. Observe how subscribers handle messages from different publishers
3. Does message ordering change?
4. Are all messages still processed exactly once?

### Challenge 2: Reliability Without Acknowledgement

**Scenario:** Understanding message acknowledgement.

**Tasks:**
1. Stop all existing subscribers
2. Run a subscriber with: `dotnet run --project src/servicebus/subscriber -cs '<servicebus-connection-string>' -ack False`
3. Let it process several messages
4. Stop and restart the subscriber
5. What happens to the messages it already processed?

**Question:** Why does this happen? What does it teach you about acknowledgement?

<details>
<summary>Hint for Challenge 2</summary>

Without acknowledgement, Service Bus doesn't know messages were processed. When the subscriber restarts, Service Bus re-delivers those messages because they were never completed.

</details>

### Challenge 3: Exceeding Queue Capacity

**Scenario:** Understanding queue limits.

**Tasks:**
1. Check your queue's maximum size in the Portal
2. With Basic tier, queues have a 1 GB limit
3. What happens if you try to send messages when the queue is full?

## Key Learnings

Let's review what you've learned through these exercises:

### About Service Bus Architecture
- **Namespace** - Container for messaging entities
- **Queue** - Point-to-point messaging channel
- **Connection String** - Contains endpoint and credentials

### About Message Flow
- **Publishers** send messages to queues
- **Subscribers** receive and process messages
- **Batching** improves throughput
- **Acknowledgement** confirms successful processing

### About Reliability
- Messages persist until acknowledged
- Subscribers can restart without losing messages
- Message ordering is generally maintained

### About Scalability
- Multiple subscribers share the workload
- Service Bus distributes messages automatically
- Each message processed exactly once
- Easy to scale out by adding instances

### Best Practices Observed
1. Use batch sending for better performance
2. Always acknowledge messages after processing
3. Handle connection strings securely
4. Monitor queue metrics in production
5. Scale subscribers based on queue depth

## Common Issues and Solutions

### Issue: "Unauthorized" Errors

**Cause:** Invalid or expired connection string

**Solution:**
- Re-fetch the connection string
- Ensure you copied the entire string
- Check for extra spaces or line breaks

### Issue: Messages Not Appearing

**Cause:** Wrong queue name or namespace

**Solution:**
- Verify queue name matches exactly (case-sensitive)
- Check namespace name in connection string
- Confirm queue exists in Portal

### Issue: Duplicate Message Processing

**Cause:** Not calling CompleteMessageAsync

**Solution:**
- Ensure subscriber acknowledges messages
- Check for exceptions preventing acknowledgement
- Use PeekLock mode (default)

## Cleanup

When you're finished with the exercises:

### Step 1: Stop Applications

Stop all running applications:
- Press Ctrl+C in each terminal window
- Verify all processes are stopped

### Step 2: Delete Resources

Delete the resource group and all contained resources:

```bash
az group delete -y --no-wait -n labs-servicebus
```

The `--no-wait` flag returns immediately without waiting for deletion to complete. The `- y` flag confirms deletion without prompting.

### Step 3: Verify Deletion

After a few minutes, verify the resource group is gone:

```bash
az group list --query "[?name=='labs-servicebus']"
```

Should return an empty array `[]`.

## Next Steps

Congratulations! You've completed the hands-on exercises for Service Bus queues. You now have practical experience with:

- Creating Service Bus namespaces and queues
- Publishing messages
- Subscribing to queues
- Testing reliability and scalability

To continue learning:

1. **Explore Topics and Subscriptions** - Pub/sub messaging patterns
2. **Learn about Message Sessions** - FIFO ordering guarantees
3. **Study Dead-Letter Queues** - Handling unprocessable messages
4. **Review AZ-204 Scenarios** - Exam-focused Service Bus patterns

The AZ-204 exam lab builds on these fundamentals with advanced features. You're now ready to tackle those more complex scenarios!

## Additional Resources

- [Service Bus documentation](https://learn.microsoft.com/en-us/azure/service-bus-messaging/)
- [Service Bus SDK for .NET](https://www.nuget.org/packages/Azure.Messaging.ServiceBus)
- [AMQP protocol overview](http://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html)
- [Microsoft Learn: Service Bus module](https://learn.microsoft.com/en-us/training/modules/implement-message-workflows-with-service-bus/)

Thank you for working through these exercises!
