# Service Bus Publish-Subscribe - Exercises Script

## Exercise 1: Creating the Service Bus Namespace and Topic

Let's begin by creating our Azure resources. First, we'll create a resource group for this lab.

We're using the az group create command to create a resource group named "labs-servicebus-pubsub" in the West Europe region. The command includes a tag parameter set to "courselabs=azure" which helps us identify and track resources created for this course - this is a best practice for organizing resources.

Now, here's an important point about Service Bus tiers. To use topics, we need at least the Standard tier. The Basic tier only supports queues. So when we create our namespace, we're specifying the Standard tier with the --sku parameter and also ensuring we're using TLS 1.2 for security with the --min-tls parameter set to 1.2. Remember to use your own unique namespace name since Service Bus namespaces must be globally unique across Azure.

Let's open the namespace in the Azure Portal. You can see that namespaces act as containers - they can hold multiple queues and topics. This organizational structure helps you manage related messaging entities together.

Now let's create a topic. In the Portal, we're clicking on "Topics" and then "Add Topic". Notice there are some interesting configuration options here - time to live, or TTL, which defines how long messages remain available if no subscribers pick them up, and maximum topic size, since topics store messages before forwarding them to subscriptions, we can control storage limits to manage costs and capacity.

We can create the topic using the CLI as well. Let's create a topic called "broadcast" with a 10-minute TTL and a maximum size of 2 gigabytes. We're using the az servicebus topic create command with the max-size parameter set to 2048 megabytes, and the default-message-time-to-live parameter set to P0DT0H10M1S - that duration format might look strange, it's an ISO 8601 duration meaning 0 days, 0 hours, 10 minutes, and 1 second. The -n flag specifies the topic name "broadcast", -g points to our resource group, and --namespace-name identifies which namespace this topic belongs to.

For comparison, let's also create a queue with similar settings but smaller size using az servicebus queue create. We're setting the max-size to 1024 megabytes and the TTL to just 1 minute for the queue named "command".

Now, if we look at both in the Portal, they appear similar at first - they're both destinations where publishers can send messages. But look closely at the topic. What do you see that the queue doesn't have? That's right - subscriptions. This is the key difference. You can listen directly on a queue, but with a topic, consumers need a subscription to listen on. This is the fundamental difference between point-to-point messaging with queues and publish-subscribe messaging with topics.

## Exercise 2: Creating Subscriptions

Subscriptions are like routing channels. Publishers send messages to the topic as a whole, and every subscription receives a copy. In practice, you typically have multiple subscriptions, each with one or more components listening. This is the fan-out pattern in action - one message published, multiple subscribers receive it.

Let's create two subscriptions for our broadcast topic - one called "web" and one called "desktop". These might represent different client applications in a real system. We're using the az servicebus topic subscription create command for each, specifying the subscription name with --name, the topic name with --topic-name, the resource group, and the namespace name.

We can check the details of a subscription, including how many messages are waiting, using the az servicebus topic subscription show command. We can also query just the message count using the --query parameter set to messageCount to get specific information without all the JSON output.

Right now, both subscriptions show zero messages, which makes sense since we haven't published anything yet. The subscriptions are ready and waiting, but there's no data flowing through them.

## Exercise 3: Publishing Messages

Now let's publish some messages. We have a .NET application that can publish to Service Bus. The interesting thing is that the publisher code is identical whether it's sending to a queue or a topic - from the sender's perspective, it doesn't need to know the difference. The Service Bus client abstracts this complexity.

Before we can send messages, we need proper authorization. Every namespace has a root access policy with full permissions, but following the principle of least privilege, we should create a specific policy with only the permissions we need. This is a security best practice - don't give more access than necessary.

Let's create an authorization rule that only allows sending to our topic using az servicebus topic authorization-rule create. We're specifying the topic name, naming the rule "publisher", and setting the rights to just "Send" - not Listen or Manage, only Send. This ensures that if these credentials are compromised, they can only be used to publish messages, not consume them or modify the topic configuration.

Now we can get the connection string for this publisher role using az servicebus topic authorization-rule keys list. We're querying specifically for the primaryConnectionString with --query, and using -o tsv to get just the value without JSON formatting. This connection string contains everything the application needs to authenticate and connect to the topic.

With that connection string, we can run our publisher application using dotnet run. We're passing the -topic parameter set to "broadcast" to specify which topic to publish to, and -cs with our connection string. Make sure to quote the connection string since it contains special characters that might confuse the shell.

Watch as the application sends batches of messages. You'll see output indicating how many messages are being sent in each batch. After a few batches, let's stop it with Ctrl-C to demonstrate how subscription message counts accumulate.

Now let's check our subscriptions using the az servicebus topic subscription show command for both the "web" and "desktop" subscriptions, querying just the messageCount. Both subscriptions have the same message count. This demonstrates the pub-sub pattern in action - the topic forwarded all messages to all subscriptions. Each subscription maintains its own independent copy of every message.

If we open the Portal and navigate to one of the subscriptions, we can use the Service Bus Explorer to actually peek at the messages and see their content. This built-in tool is incredibly useful for debugging and verifying message structure without consuming them.

## Exercise 4: Receiving Messages from a Subscription

To receive messages, we need another authorization rule, this time with Listen rights rather than Send. We're using az servicebus topic authorization-rule create again, naming this rule "subscriber" and setting the rights to "Listen". This ensures the subscriber application can only consume messages, not send them.

Let's get the connection string for this subscriber using the same keys list command we used before, but this time for the subscriber authorization rule.

Now we'll run a subscriber on the web subscription using dotnet run with the subscriber project. We're specifying the -topic parameter as "broadcast", the -subscription parameter as "web" to indicate which subscription to consume from, and passing the subscriber connection string.

If messages haven't expired, you should see them being processed immediately. Remember, we set a 10-minute TTL earlier, so if more time has passed since we published the messages, they'll be gone. This demonstrates the importance of understanding TTL settings in your messaging architecture.

Let's leave this subscriber running and, in another terminal, start the publisher again using the same command we used before. Watch what happens in real-time. The publisher logs when it sends each batch, and the subscriber prints all the messages it receives simultaneously. This is asynchronous messaging in action - the publisher and subscriber are completely decoupled, communicating only through the Service Bus topic.

## Exercise 5: Multiple Subscriptions

We have one subscriber consuming from the web subscription, but the desktop subscription doesn't have any consumers yet. Let's compare the message counts using az servicebus topic subscription show for both subscriptions.

The web subscription shows zero messages because they've all been delivered to our consumer and acknowledged. But the desktop subscription has accumulated every message that's been published and hasn't expired yet. This demonstrates an important characteristic - each subscription maintains its own independent message queue. Messages consumed from one subscription don't affect other subscriptions.

Now let's start a subscriber for the desktop subscription in a new terminal using the same dotnet run command but with the -subscription parameter set to "desktop".

Look at what happens. The desktop subscriber immediately starts processing all the backlogged messages, printing them rapidly one after another. Meanwhile, the web subscriber is waiting for new messages since it's already caught up. This shows how different consumers can operate at completely different speeds without affecting each other.

Once the desktop subscriber has processed its backlog, both subscribers are caught up, and they'll both receive new messages simultaneously as the publisher sends them. You can see the fan-out pattern working beautifully - one message published, and both subscribers receive their own copy to process independently.

This demonstrates an important characteristic of subscriptions - each one maintains its own independent message queue, and consumers can process at their own pace without affecting other subscriptions. This is powerful for building systems where different components have different processing capabilities and requirements.

## Lab Challenge

Now it's time for you to explore on your own. Service Bus is designed to be reliable and scalable. Subscriptions can model different processes that operate at different speeds. But here's the question: What happens if you have multiple subscribers listening on the same subscription? And what if you have multiple publishers publishing to the same topic?

Try experimenting with these scenarios. Start multiple instances of the subscriber on the same subscription, or multiple publishers sending to the broadcast topic. Observe the behavior carefully - does each message get processed once or multiple times? How does Service Bus distribute messages when you have competing consumers? What happens to message ordering with multiple publishers?

Think about what this means for designing distributed systems. Understanding these patterns is crucial for building reliable, scalable messaging architectures in Azure.

## Cleanup

When you're finished experimenting, don't forget to clean up your resources to avoid ongoing charges. We're using az group delete with the -y flag to confirm without prompting and --no-wait to return immediately without waiting for the operation to complete. This removes the resource group and everything inside it - the namespace, topics, subscriptions, and all authorization rules we created.
