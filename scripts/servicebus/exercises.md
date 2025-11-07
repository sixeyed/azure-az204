# Service Bus Messaging

## Reference

Service Bus is Azure's high-throughput, reliable message queue service designed for enterprise-grade messaging. Unlike simpler queuing systems, Service Bus stores messages until they're successfully processed, offers advanced features like dead-letter queues for problematic messages, and provides the durability guarantees needed for distributed systems. The standard messaging patterns you'll implement with queues enable fire-and-forget communication where publishers send messages without needing to know which component will process them or even if any component is currently running. This decoupling is fundamental to building resilient, scalable cloud applications.

## Create a Service Bus Namespace & Queue

Service Bus starts with creating a namespace, which serves as a container for your messaging entities. Let's explore the options before committing to a configuration.

**Navigate to the Portal**: We're opening the Azure Portal and searching for "service bus" to understand what's available. When creating a namespace, you'll see that the namespace name becomes your subdomain at servicebus.windows.net, which is why it must be globally unique. The pricing tiers are critical to understand because they define not just cost but capabilities.

**Understanding Pricing Tiers**: The Basic tier provides queues with a maximum message size of 256 KB and pay-per-use pricing, perfect for development and learning. Standard tier adds topics and subscriptions for pub-sub patterns while maintaining the 256 KB message limit. Premium tier offers dedicated resources, supports messages up to 1 MB, provides predictable performance, and includes virtual network integration for enhanced security. For this lab, Basic tier is sufficient since we're working with queues only.

**TLS Configuration**: You can set the minimum TLS level for consumers, ensuring secure communication. Modern applications should use TLS 1.2 or higher.

After exploring the Portal, we'll switch to the CLI for resource creation since it's more suitable for automation and repeatability.

**Create Resource Group**: We're creating a resource group called "labs-servicebus" in West Europe with tags to help track resources created for this course. The tags parameter with "courselabs=azure" is a best practice for organizing and managing lab resources, especially when you're running multiple experiments.

**Create the Namespace**: We're using az servicebus namespace create with the Basic SKU. Remember to choose a unique name - something like "sb-yourname-001" works well since Service Bus namespaces must be globally unique across Azure. The location should match your resource group for consistency.

**Understanding the Output**: The JSON output includes your serviceBusEndpoint, which shows that communication happens over HTTPS. This endpoint follows the pattern your-namespace-name.servicebus.windows.net and is what applications will connect to.

**Explore in Portal**: Opening the namespace in the Portal reveals several management sections. The Overview shows metrics and key information. The Queues section is currently empty. Shared access policies show the RootManageSharedAccessKey created by default, providing full administrative access to the namespace. These shared access tokens work similarly to storage account keys, but with a one-to-one relationship between policies and tokens, allowing fine-grained permission control.

**Create a Queue**: We're creating a queue named "echo" using az servicebus queue create. This is our messaging destination where publishers will send and subscribers will receive messages. The command is straightforward - specify the resource group, queue name, and namespace.

**Explore Queue in Portal**: Refreshing the Portal shows the new "echo" queue. Click into it to see the metrics on message counts, currently showing zero since we haven't sent anything. The Shared access policies blade provides queue-level access control separate from namespace-level policies, useful when you need different permissions for different queues. The Messages section lets you peek at queue contents without consuming messages, which is invaluable for debugging.

---

## Run a .NET Subscriber

Understanding how subscribers work is fundamental to Service Bus messaging. A subscriber connects to the queue and continuously polls for messages.

**Understanding the Subscriber Pattern**: The subscriber application in Program.cs creates a Service Bus client, establishes a receiver for the "echo" queue, enters an infinite loop listening for messages, processes each message by printing its content, and critically, acknowledges successful processing by calling CompleteMessageAsync. This acknowledgement tells Service Bus the message was handled successfully and can be removed from the queue. Without acknowledgement, messages would reappear for processing, ensuring at-least-once delivery semantics.

**Understanding AMQP**: Service Bus uses Advanced Message Queuing Protocol, an open standard implemented by many messaging systems including RabbitMQ. This standardization means Service Bus can serve as a drop-in replacement for other AMQP-compliant systems, providing flexibility in your architecture choices.

**Get Connection String**: Your application needs credentials to connect. We're using az servicebus namespace authorization-rule keys list to retrieve the connection string for RootManageSharedAccessKey. The query parameter extracts just the primaryConnectionString, and the tsv output format gives us the raw value without JSON formatting. This connection string contains everything the application needs - the endpoint, the key name, and the shared access key itself.

**Run the Subscriber**: We're starting the subscriber using dotnet run with the connection string passed as a parameter. The single quotes around the connection string are important because it contains special characters like semicolons and equals signs that shells might interpret incorrectly. The application displays "Listening for messages on queue: echo" and "Press Ctrl+C to exit", indicating it's actively polling the queue. Keep this terminal open so the subscriber continues running.

---

## Reliable & Scalable Messaging

Service Bus provides powerful reliability and scalability features that distinguish it from simpler messaging systems.

**Test Message Persistence**: Let's demonstrate Service Bus's reliability by stopping the subscriber while the publisher continues sending. Note the last batch number your subscriber processed, then press Ctrl+C to stop it. The publisher continues running in its terminal, sending batch after batch. These messages don't disappear - they're stored in the Service Bus queue, safely persisted to disk, waiting for a consumer.

**Observe Accumulation**: In the Azure Portal, navigate to your queue's Overview blade and watch the Active Message Count increase with each batch. This metric shows messages waiting for processing. Service Bus is durably storing every message even though no subscriber is listening.

**Restart the Subscriber**: Using the same dotnet run command, start the subscriber again. Watch carefully - it immediately starts processing messages from where the queue left off, not where the previous subscriber instance stopped. You'll see it receive and process every message that accumulated during the downtime.

**Understanding the Guarantees**: No messages were lost during the subscriber's downtime. Service Bus persisted them until a consumer became available and acknowledged their successful processing. This reliability is essential for distributed systems where you need guarantees that work won't be lost during deployments, updates, or temporary failures. Deployment updates don't cause message loss, network issues don't result in dropped work, and maintenance windows don't impact message delivery.

**Test Horizontal Scaling**: Service Bus supports the competing consumers pattern where multiple subscribers share the workload from a single queue. With your first subscriber still running, open another terminal and start a second subscriber using the exact same command. Now watch both terminals carefully.

**Observe Load Distribution**: Messages are distributed between the two subscribers in approximately round-robin fashion. Subscriber one might receive message one, message three, and message five, while subscriber two receives message two, message four, and message six. Critically, each message is processed by exactly one subscriber - there's no duplication of work. Service Bus handles the distribution logic automatically.

**Test Scaling Behavior**: Stop one subscriber by pressing Ctrl+C. The remaining subscriber takes over all message processing, handling the full load alone. The throughput decreases because you have fewer processors, but no messages are lost. Start the subscriber again and load distribution resumes immediately - both subscribers start receiving messages in roughly equal proportions.

**Understanding Horizontal Scaling**: This is a powerful capability. You can add more subscribers to handle increased load without any configuration changes or code modifications. During quiet periods, you can remove subscribers to save resources. Service Bus handles all the distribution mechanics, implementing a robust competing consumers pattern that's essential for building scalable cloud applications.

---

## Lab

Messaging systems need to handle complex real-world scenarios. Service Bus is designed for reliability and scale, but understanding its behavior under different conditions requires experimentation.

**Multiple Publishers**: What happens when multiple systems publish to the same queue simultaneously? Run two publisher instances in separate terminal windows using the same connection string. Observe how the subscriber handles messages from different publishers. Can you tell which publisher sent which message based on the message content? Does message ordering change when multiple publishers are active? Are all messages still processed exactly once, or do you see duplication or loss?

**Acknowledgement Testing**: Understanding message acknowledgement is crucial. Stop all subscribers to start fresh, then run a subscriber with the -ack False flag to disable acknowledgement. Let it process several messages, watching the output. Stop and restart the subscriber. What happens to the messages it already processed? Do they reappear?

**Understanding Why**: Without acknowledgement, Service Bus doesn't know messages were processed successfully. When the subscriber restarts, Service Bus re-delivers those messages because they were never completed. The messages remained in the queue, invisible to other consumers but not removed. This demonstrates why proper acknowledgement is critical for exactly-once processing semantics. Without it, you get at-least-once delivery, which can cause duplicate processing.

---

## Cleanup

Proper resource cleanup prevents ongoing charges and keeps your subscription organized.

**Delete Resource Group**: We're removing everything we created using az group delete. The -y flag confirms the deletion without prompting, and --no-wait returns immediately without waiting for the deletion to complete. The deletion happens asynchronously in the background, which is useful for large resource groups.

**Verify Deletion**: After a few minutes, you can verify the resource group is gone using az group list with a query filter. This should return an empty array, confirming successful cleanup.
