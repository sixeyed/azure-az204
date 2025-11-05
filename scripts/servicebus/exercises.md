# Service Bus Messaging - Hands-On Exercises Narration Script

## Exercise Overview

Welcome to the hands-on exercises for Azure Service Bus. In this session, you'll get practical experience with Service Bus queues, publishers, subscribers, and reliability features. By the end, you'll understand how to build scalable, reliable messaging solutions in Azure.

## Prerequisites Check

Before we begin, make sure you have Azure CLI installed and authenticated, .NET 6 SDK installed for running the sample applications, an active Azure subscription, and access to the lab source code.

Let's verify your .NET installation by running dotnet --version. You should see version 6.0 or later displayed in the output.

## Exercise 1: Create Service Bus Resources

### Step 1: Create Resource Group

Let's start by creating a dedicated resource group for this lab. We're using the az group create command with the -n parameter set to "labs-servicebus", adding a tag with "courselabs=azure" so we can track lab resources, and using the -l parameter to specify West Europe as our location. The output confirms the resource group is created in West Europe.

### Step 2: Understand Service Bus Tiers

Before creating the namespace, let's understand the pricing tiers. Basic tier provides queues only with a 256 KB maximum message size and pay-per-use pricing. Standard tier adds topics and subscriptions while keeping the 256 KB message limit. Premium tier offers dedicated resources, supports 1 MB messages, and provides predictable performance. For this lab, we'll use Basic tier to keep costs low since we only need queue functionality.

### Step 3: Create Service Bus Namespace

Create the namespace using az servicebus namespace create. Remember, a namespace is a container for queues, topics, and subscriptions - it's the top-level organizational unit in Service Bus. We're specifying the resource group with -g, setting the location to West Europe, using --sku Basic for the pricing tier, and providing a unique namespace name with -n. Replace the placeholder with something unique, like "sb-yourname-001" since Service Bus namespaces must be globally unique.

What to observe in the output: The serviceBusEndpoint shows your HTTPS endpoint, the location confirms deployment region, and the sku confirms Basic tier. The namespace is now accessible at your-namespace-name.servicebus.windows.net.

### Step 4: Explore in Portal

Open the Azure Portal and navigate to your Service Bus namespace. Take a moment to explore the different sections. The Overview blade shows metrics and key information about your namespace. The Queues section is currently empty since we haven't created any yet. Under Shared access policies, you'll see the RootManageSharedAccessKey created by default - this provides full administrative access to the namespace. The Metrics section will show activity once we start sending messages, giving you visibility into throughput, message counts, and errors.

### Step 5: Create a Queue

Now create your first queue named "echo" using az servicebus queue create. We're specifying the resource group with -g, the queue name with --name, and identifying which namespace to create it in with --namespace-name.

In the Portal, refresh and you'll see the "echo" queue appear. Click on it to explore its configuration. The Overview shows message count metrics, currently zero since we haven't sent anything yet. The Shared access policies blade provides queue-level access control, separate from namespace-level policies. The Messages section allows you to peek at messages without removing them from the queue, which is incredibly useful for debugging.

## Exercise 2: Run a Subscriber Application

### Step 1: Understand the Subscriber Code

Before running the subscriber, let's understand what it does. The subscriber application connects to the Service Bus namespace, creates a receiver for the "echo" queue, enters an infinite loop listening for messages, prints the content when a message arrives, and acknowledges the message by calling CompleteMessageAsync. The acknowledgement is critical - it tells Service Bus the message was processed successfully and can be removed from the queue. Without this, messages would reappear for processing again.

### Step 2: Get Connection String

To connect, your application needs a connection string. We're using az servicebus namespace authorization-rule keys list with -n set to RootManageSharedAccessKey, specifying the resource group and namespace, and querying for the primaryConnectionString with --query and -o tsv to get just the value. This returns a connection string in the format "Endpoint=sb://namespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=your-key". Copy this entire string - you'll need it for the next step.

### Step 3: Run the Subscriber

Start the subscriber application using dotnet run with --project pointing to src/servicebus/subscriber and the -cs parameter containing your connection string. Important: Keep the single quotes around the connection string to prevent shell interpretation of special characters.

The application starts and displays "Listening for messages on queue: echo" along with "Press Ctrl+C to exit". The subscriber is now waiting for messages, continuously polling the queue. Keep this terminal window open so it continues running.

## Exercise 3: Run a Publisher Application

### Step 1: Understand the Publisher Code

The publisher application connects to the Service Bus namespace, creates a sender for the "echo" queue, sends messages in batches which is more efficient than individual sends since it reduces network overhead, and waits between batches to simulate realistic workloads. Batch sending is a best practice - it significantly improves throughput and reduces costs.

### Step 2: Run the Publisher

Open a new terminal window and run the publisher using dotnet run with --project pointing to src/servicebus/publisher and -cs containing the same connection string you used for the subscriber. Use the exact same connection string value.

### Step 3: Observe Message Flow

Watch what happens in both terminal windows. In the publisher window, you'll see "Sending batch 1...", "Sent 10 messages", "Waiting...", and then "Sending batch 2..." continuing with more batches. In the subscriber window simultaneously, you'll see "Received message: Message 1 from batch 1", followed by message 2, message 3, and so on as messages are processed in real-time.

In the Azure Portal, navigate to your queue and watch the message count metrics. You might see brief spikes when batches are sent, followed by quick drops as the subscriber processes them. This is real-time messaging in action - the decoupled architecture allows publishers and subscribers to operate independently.

## Exercise 4: Test Message Persistence

Now we'll test Service Bus's reliability features to see how it handles failures.

### Step 1: Note Current Progress

Look at your subscriber window and note the last batch number it processed. For example, you might see "Received message: Message 10 from batch 5". Remember this batch number - it's important for verifying that no messages are lost.

### Step 2: Stop the Subscriber

In the subscriber window, press Ctrl+C on Windows and Linux or Cmd+C on Mac to stop it. The subscriber shuts down gracefully and stops processing messages. The connection to Service Bus is terminated.

### Step 3: Let Messages Accumulate

Keep the publisher running in its terminal. It continues sending batches - you'll see "Sending batch 6...", "Sending batch 7...", "Sending batch 8..." in the publisher output. But there's no subscriber to process them. Where do these messages go? They're stored in the Service Bus queue, safely persisted to disk, waiting to be processed when a consumer becomes available.

### Step 4: Check the Portal

In the Azure Portal, go to your queue's Overview blade and watch the "Active Message Count" increase. Each batch adds 10 messages to the count. You can see the number growing steadily as the publisher continues. This demonstrates message persistence - messages are safely stored even when no subscribers are active. This is fundamentally different from in-memory messaging systems.

### Step 5: Restart the Subscriber

Now restart the subscriber using the exact same command: dotnet run --project src/servicebus/subscriber -cs with your connection string. Watch carefully what happens. The subscriber immediately starts processing messages from where the queue left off - you'll see "Received message: Message 1 from batch 6", followed by message 2, message 3, and so on.

Critical observation: No messages were lost during the downtime. The subscriber picked up all messages sent while it was offline. It doesn't matter that the original subscriber process terminated - Service Bus persisted the messages, and the new subscriber process retrieves them seamlessly.

### Why This Matters

This reliability is essential for distributed systems. Subscribers can restart without losing messages, making deployments and updates safe. Deployment updates don't cause message loss - you can safely deploy new versions of your application. Temporary failures don't impact message delivery - network issues, crashes, or maintenance windows don't lose data. Service Bus stores messages until it receives a completion acknowledgement, only then removing messages from the queue. This durability guarantee is the foundation of reliable asynchronous messaging.

## Exercise 5: Test Horizontal Scaling

### Step 1: Understand Load Balancing

Service Bus supports multiple subscribers consuming from the same queue, and messages are distributed across subscribers automatically. This is automatic load balancing - Service Bus handles the distribution logic, implementing a competing consumers pattern where multiple instances process messages in parallel.

### Step 2: Run a Second Subscriber

With your first subscriber still running, open a third terminal window and start another subscriber using the exact same dotnet run --project src/servicebus/subscriber command with your connection string. Now you have three terminal windows: Terminal 1 running the publisher, Terminal 2 running Subscriber 1, and Terminal 3 running Subscriber 2.

### Step 3: Observe Load Distribution

Watch both subscriber terminals carefully. You'll see messages distributed between them. Subscriber 1 might show "Received message: Message 1 from batch 10", "Received message: Message 3 from batch 10", and "Received message: Message 5 from batch 10". Meanwhile, Subscriber 2 shows "Received message: Message 2 from batch 10", "Received message: Message 4 from batch 10", and "Received message: Message 6 from batch 10".

Service Bus distributes messages in a round-robin fashion, approximately. Each message is processed by exactly one subscriber - there's no duplication. This ensures each piece of work is done once, maintaining exactly-once processing semantics.

### Step 4: Test Scaling Behavior

Stop one subscriber by pressing Ctrl+C. Watch the remaining subscriber - it takes over all message processing, handling the full load alone. The throughput decreases because there's only one processor now, but no messages are lost.

Start the subscriber again using the same command. Load distribution resumes immediately - both subscribers start receiving messages again in roughly equal proportions. This is horizontal scaling in action: Add more subscribers to handle increased load, improving throughput and reducing latency. Remove subscribers to save resources during quiet periods. Service Bus handles the distribution automatically without any configuration changes or code modifications.

## Exercise 6: Portal Metrics

### Viewing Queue Metrics

In the Azure Portal, navigate to your queue and click Metrics in the left menu. Add charts for Incoming Messages showing messages published to the queue, Outgoing Messages showing messages delivered and acknowledged, and Active Messages showing messages waiting in the queue for processing.

### Understanding the Metrics

With both publisher and subscribers running, incoming and outgoing rates should be similar - what goes in comes out. The active message count should stay low, typically near zero, indicating messages are processed quickly. Stop all subscribers and watch the changes: Incoming messages continue at the same rate since the publisher keeps running, Outgoing messages stop completely because there are no consumers, and Active message count increases steadily as messages accumulate in the queue.

This visual feedback helps you monitor queue health in production. High active message counts indicate either too many publishers or too few subscribers. The backlog depth tells you if you need to scale out consumers. These metrics are crucial for capacity planning and troubleshooting.

## Lab Challenge: Experimentation Time

Now that you understand the basics, try these challenges on your own.

### Challenge 1: Multiple Publishers

Scenario: Multiple systems publishing to the same queue, simulating a real-world scenario where different services send work items.

Tasks: Run two publisher instances simultaneously in separate terminal windows. Observe how subscribers handle messages from different publishers - can you tell which publisher sent which message? Does message ordering change when multiple publishers are active? Are all messages still processed exactly once, or do you see any duplication or loss?

### Challenge 2: Reliability Without Acknowledgement

Scenario: Understanding message acknowledgement and its importance for reliability.

Tasks: Stop all existing subscribers to start fresh. Run a subscriber with the command: dotnet run --project src/servicebus/subscriber -cs with your connection string and -ack False to disable acknowledgement. Let it process several messages, watching the output. Stop and restart the subscriber. What happens to the messages it already processed? Do they reappear?

Question: Why does this happen? What does it teach you about acknowledgement importance?

Hint: Without acknowledgement, Service Bus doesn't know messages were processed. When the subscriber restarts, Service Bus re-delivers those messages because they were never completed. The messages remain in the queue, invisible but not removed, until acknowledged or until they expire. This demonstrates why proper acknowledgement is critical for exactly-once processing.

### Challenge 3: Exceeding Queue Capacity

Scenario: Understanding queue limits and what happens when capacity is reached.

Tasks: Check your queue's maximum size in the Portal under Properties - with Basic tier, queues have a 1 GB limit by default. What happens if you try to send messages when the queue is full? How does the publisher application behave? Does it receive an error, and if so, what kind?

## Key Learnings

Let's review what you've learned through these exercises.

### About Service Bus Architecture

Namespace serves as a container for messaging entities, providing organization and security boundaries. Queue enables point-to-point messaging channels where each message has exactly one consumer. Connection String contains endpoint and credentials, providing everything applications need to connect securely.

### About Message Flow

Publishers send messages to queues using the Service Bus SDK. Subscribers receive and process messages, pulling them from the queue. Batching improves throughput by reducing network round trips. Acknowledgement confirms successful processing, ensuring messages aren't lost.

### About Reliability

Messages persist until acknowledged, providing durability guarantees. Subscribers can restart without losing messages, enabling safe deployments. Message ordering is generally maintained within the queue, following FIFO principles for most scenarios.

### About Scalability

Multiple subscribers share the workload using the competing consumers pattern. Service Bus distributes messages automatically without additional configuration. Each message is processed exactly once, avoiding duplicate work. Easy to scale out by adding instances - just start more subscriber processes pointing to the same queue.

### Best Practices Observed

Use batch sending for better performance, reducing network overhead and costs. Always acknowledge messages after processing to ensure reliability. Handle connection strings securely, using Azure Key Vault or managed identities in production. Monitor queue metrics in production, watching for backlog growth and throughput issues. Scale subscribers based on queue depth, adding capacity when active message count grows.

## Common Issues and Solutions

### Issue: "Unauthorized" Errors

Cause: Invalid or expired connection string, or insufficient permissions on the authorization rule.

Solution: Re-fetch the connection string using the Azure CLI. Ensure you copied the entire string without truncating it. Check for extra spaces or line breaks that might have been introduced during copy-paste. Verify the authorization rule has the necessary permissions for your operation.

### Issue: Messages Not Appearing

Cause: Wrong queue name or namespace in the connection string or application configuration.

Solution: Verify queue name matches exactly - it's case-sensitive, so "Echo" is different from "echo". Check namespace name in connection string matches your actual namespace. Confirm queue exists in Portal by navigating to your namespace and viewing the queue list.

### Issue: Duplicate Message Processing

Cause: Not calling CompleteMessageAsync after processing, or exceptions preventing acknowledgement.

Solution: Ensure subscriber acknowledges messages after successful processing. Check for exceptions preventing acknowledgement - use try-catch blocks around CompleteMessageAsync. Use PeekLock mode which is the default, allowing you to complete or abandon messages explicitly.

## Cleanup

When you're finished with the exercises, proper cleanup is important.

### Step 1: Stop Applications

Stop all running applications by pressing Ctrl+C in each terminal window. Verify all processes are stopped by checking that no dotnet processes are still running in the background.

### Step 2: Delete Resources

Delete the resource group and all contained resources using az group delete with -y to confirm without prompting and --no-wait to return immediately without waiting for deletion to complete. This removes everything we created - the namespace, queues, authorization rules, and the resource group itself.

### Step 3: Verify Deletion

After a few minutes, verify the resource group is gone using az group list with a query filter for our specific resource group name. This should return an empty array, confirming deletion was successful.

## Next Steps

Congratulations! You've completed the hands-on exercises for Service Bus queues. You now have practical experience with creating Service Bus namespaces and queues, publishing messages in batches, subscribing to queues and processing messages, and testing reliability and scalability features.

To continue learning, explore Topics and Subscriptions for pub-sub messaging patterns implementing fan-out scenarios. Learn about Message Sessions for FIFO ordering guarantees and stateful message processing. Study Dead-Letter Queues for handling unprocessable messages and implementing retry logic. Review AZ-204 Scenarios focusing on exam-focused Service Bus patterns and best practices.

The AZ-204 exam lab builds on these fundamentals with advanced features like duplicate detection, scheduled messages, and transaction support. You're now ready to tackle those more complex scenarios!

## Additional Resources

For deeper learning, explore the Service Bus documentation at Microsoft Learn, covering architecture, features, and best practices. Check out the Service Bus SDK for .NET on NuGet for detailed API documentation. Review the AMQP protocol overview to understand the underlying wire protocol. Complete the Microsoft Learn Service Bus module for structured learning paths aligned with certification goals.

Thank you for working through these exercises! You now have hands-on experience with Azure Service Bus and understand the fundamentals of building reliable messaging solutions in the cloud.
