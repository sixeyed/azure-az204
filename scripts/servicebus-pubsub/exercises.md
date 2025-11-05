# Service Bus Publish-Subscribe - Exercises Script

## Exercise 1: Creating the Service Bus Namespace and Topic

Let's begin by creating our Azure resources. First, we'll create a resource group for this lab.

```
az group create -n labs-servicebus-pubsub --tags courselabs=azure -l westeurope
```

Now, here's an important point about Service Bus tiers. To use topics, we need at least the Standard tier. The Basic tier only supports queues. So when we create our namespace, we'll specify Standard tier and also ensure we're using TLS 1.2 for security.

```
az servicebus namespace create -g labs-servicebus-pubsub --sku Standard --min-tls 1.2 -l westeurope -n <sb-name>
```

Remember to use your own unique namespace name.

Let's open the namespace in the Azure Portal. You can see that namespaces act as containers - they can hold multiple queues and topics.

Now let's create a topic. Click on "Topics" and then "Add Topic". Notice there are some interesting configuration options here:

- Time to live, or TTL - this defines how long messages remain available if no subscribers pick them up
- Maximum topic size - since topics store messages before forwarding them to subscriptions, we can control storage limits

We can create the topic using the CLI as well. Let's create a topic called "broadcast" with a 10-minute TTL and a maximum size of 2 gigabytes.

```
az servicebus topic create --max-size 2048 --default-message-time-to-live P0DT0H10M1S -n broadcast -g labs-servicebus-pubsub --namespace-name <sb-name>
```

That duration format might look strange - it's P0DT0H10M1S, which means 0 days, 0 hours, 10 minutes, and 1 second.

For comparison, let's also create a queue with similar settings but smaller size:

```
az servicebus queue create --max-size 1024 --default-message-time-to-live P0DT0H1M0S -n command -g labs-servicebus-pubsub --namespace-name <sb-name>
```

Now, if we look at both in the Portal, they appear similar at first - they're both destinations where publishers can send messages. But look closely at the topic. What do you see that the queue doesn't have?

That's right - subscriptions. This is the key difference. You can listen directly on a queue, but with a topic, consumers need a subscription to listen on.

## Exercise 2: Creating Subscriptions

Subscriptions are like routing channels. Publishers send messages to the topic as a whole, and every subscription receives a copy. In practice, you typically have multiple subscriptions, each with one or more components listening.

Let's create two subscriptions for our broadcast topic - one called "web" and one called "desktop". These might represent different client applications in a real system.

```
az servicebus topic subscription create --name web --topic-name broadcast -g labs-servicebus-pubsub --namespace-name <sb-name>

az servicebus topic subscription create --name desktop --topic-name broadcast -g labs-servicebus-pubsub --namespace-name <sb-name>
```

We can check the details of a subscription, including how many messages are waiting:

```
az servicebus topic subscription show --name desktop --topic-name broadcast -g labs-servicebus-pubsub --namespace-name <sb-name>
```

Or query just the message count:

```
az servicebus topic subscription show --name web --topic-name broadcast --query messageCount -g labs-servicebus-pubsub --namespace-name <sb-name>
```

Right now, both subscriptions show zero messages, which makes sense since we haven't published anything yet.

## Exercise 3: Publishing Messages

Now let's publish some messages. We have a .NET application that can publish to Service Bus. The interesting thing is that the publisher code is identical whether it's sending to a queue or a topic - from the sender's perspective, it doesn't need to know the difference.

Before we can send messages, we need proper authorization. Every namespace has a root access policy with full permissions, but following the principle of least privilege, we should create a specific policy with only the permissions we need.

Let's create an authorization rule that only allows sending to our topic:

```
az servicebus topic authorization-rule create --topic-name broadcast --name publisher --rights Send -g labs-servicebus-pubsub --namespace-name <sb-name>
```

Now we can get the connection string for this publisher role:

```
az servicebus topic authorization-rule keys list --topic-name broadcast --name publisher --query primaryConnectionString -o tsv -g labs-servicebus-pubsub --namespace-name <sb-name>
```

With that connection string, we can run our publisher application. Make sure to quote the connection string:

```
dotnet run --project src/servicebus/publisher -topic broadcast -cs '<publisher-connection-string>'
```

Watch as the application sends batches of messages. After a few batches, let's stop it with Ctrl-C.

Now let's check our subscriptions:

```
az servicebus topic subscription show --name web --topic-name broadcast --query messageCount -g labs-servicebus-pubsub --namespace-name <sb-name>

az servicebus topic subscription show --name desktop --topic-name broadcast --query messageCount -g labs-servicebus-pubsub --namespace-name <sb-name>
```

Both subscriptions have the same message count. This demonstrates the pub-sub pattern in action - the topic forwarded all messages to all subscriptions.

If we open the Portal and navigate to one of the subscriptions, we can use the Service Bus Explorer to actually peek at the messages and see their content.

## Exercise 4: Receiving Messages from a Subscription

To receive messages, we need another authorization rule, this time with Listen rights:

```
az servicebus topic authorization-rule create --topic-name broadcast --name subscriber --rights Listen -g labs-servicebus-pubsub --namespace-name <sb-name>
```

Let's get the connection string:

```
az servicebus topic authorization-rule keys list --topic-name broadcast --name subscriber --query primaryConnectionString -o tsv -g labs-servicebus-pubsub --namespace-name <sb-name>
```

Now we'll run a subscriber on the web subscription:

```
dotnet run --project src/servicebus/subscriber -topic broadcast -subscription web -cs '<subscriber-connection-string>'
```

If messages haven't expired, you should see them being processed. Remember, we set a 10-minute TTL, so if more time has passed, the messages will be gone.

Let's leave this subscriber running and, in another terminal, start the publisher again:

```
dotnet run --project src/servicebus/publisher -topic broadcast -cs '<publisher-connection-string>'
```

Watch what happens. The publisher logs when it sends each batch, and the subscriber prints all the messages it receives in real-time.

## Exercise 5: Multiple Subscriptions

We have one subscriber consuming from the web subscription, but the desktop subscription doesn't have any consumers yet. Let's compare the message counts:

```
az servicebus topic subscription show --name web --topic-name broadcast --query messageCount -g labs-servicebus-pubsub --namespace-name <sb-name>

az servicebus topic subscription show --name desktop --topic-name broadcast --query messageCount -g labs-servicebus-pubsub --namespace-name <sb-name>
```

The web subscription shows zero messages because they've all been delivered to our consumer. But the desktop subscription has accumulated every message that's been published and hasn't expired yet.

Now let's start a subscriber for the desktop subscription in a new terminal:

```
dotnet run --project src/servicebus/subscriber -topic broadcast -subscription desktop -cs '<subscriber-connection-string>'
```

Look at what happens. The desktop subscriber immediately starts processing all the backlogged messages, printing them rapidly. Meanwhile, the web subscriber is waiting for new messages since it's already caught up.

Once the desktop subscriber has processed its backlog, both subscribers are caught up, and they'll both receive new messages simultaneously as the publisher sends them.

This demonstrates an important characteristic of subscriptions - each one maintains its own independent message queue, and consumers can process at their own pace without affecting other subscriptions.

## Lab Challenge

Now it's time for you to explore on your own. Service Bus is designed to be reliable and scalable. Subscriptions can model different processes that operate at different speeds. But here's the question:

What happens if you have multiple subscribers listening on the same subscription? And what if you have multiple publishers publishing to the same topic?

Try experimenting with these scenarios. Start multiple instances of the subscriber on the same subscription, or multiple publishers. Observe the behavior and think about what this means for designing distributed systems.

## Cleanup

When you're finished experimenting, don't forget to clean up your resources:

```
az group delete -y --no-wait -n labs-servicebus-pubsub
```

This will delete everything we created in this lab.
