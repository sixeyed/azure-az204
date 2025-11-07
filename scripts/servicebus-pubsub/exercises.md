# Service Bus Publish-Subscribe

## Reference

One of the fundamental patterns in asynchronous messaging is publish-subscribe, commonly called pub-sub. The pattern is elegant in its simplicity - the component sending messages is the publisher, and there can be zero or many components subscribing to receive those messages, with each subscriber getting their own copy. This architecture enables extensibility because new subscribers can be added to introduce new functionality without requiring any changes to existing components or the publisher itself. The decoupling is complete - publishers don't know or care who's consuming their messages, and subscribers don't know or care where messages originate.

In Service Bus, topics implement the pub-sub pattern. While queues provide point-to-point communication, topics enable one-to-many distribution. Understanding when to use each pattern is fundamental to designing messaging architectures.

## Create a Service Bus Namespace & Topic

Service Bus topics require at least Standard tier, which is our first important consideration. Basic tier only supports queues.

**Create Resource Group**: We're creating a resource group called "labs-servicebus-pubsub" in West Europe with tags for tracking. This organization helps manage resources and understand costs associated with specific labs.

**Create Namespace**: We're creating a namespace with Standard SKU and minimum TLS 1.2 for security. The Standard tier is required for topics and subscriptions - this is a key distinction from the Basic tier we might use for simple queuing scenarios. Choose a unique namespace name since it becomes part of your servicebus.windows.net domain.

**Explore in Portal**: Opening the namespace reveals that it's a container for multiple messaging entities. You can create both queues and topics within a single namespace, organizing related messaging resources together.

**Create Topic in Portal**: Clicking to create a topic exposes some interesting configuration options. Time to live, or TTL, defines how long messages remain available if no subscribers pick them up. This prevents indefinite message accumulation when subscribers are slow or offline. Maximum topic size controls storage capacity since topics must store messages before forwarding them to subscriptions.

**Create Topic with CLI**: We're creating a topic called "broadcast" with az servicebus topic create. The max-size parameter set to 2048 specifies two gigabytes of storage. The default-message-time-to-live parameter uses ISO 8601 duration format, which looks cryptic but is powerful. P0DT0H10M1S means zero days, zero hours, ten minutes, and one second - giving us a ten-minute message lifetime.

**Create Queue for Comparison**: Creating a queue with similar settings but smaller size helps illustrate the differences. The queue gets 1024 megabytes of storage and just one minute TTL.

**Compare in Portal**: Looking at both the topic and queue in the Portal, they appear similar initially - both are destinations where publishers send messages. But look closely at the topic blade. You'll see a Subscriptions section that doesn't exist for queues. This is the fundamental difference - you can listen directly on a queue, but topics require subscriptions. Publishers send to topics, and subscriptions receive copies.

---

## Create Subscriptions

Subscriptions are the routing mechanism that makes pub-sub work. They're like independent message channels.

**Understanding Subscriptions**: Publishers send messages to the topic as a single destination. The topic then forwards copies to all subscriptions. Each subscription maintains its own independent queue of messages. In a store application, you might publish an order-created message to a topic, with subscriptions for different concerns - a fulfillment subscription processing shipping requests, an analytics subscription summarizing sales data, and an auditing subscription recording transaction details. Each processes the same event for different purposes.

**Create Subscriptions**: We're creating two subscriptions named "web" and "desktop" using az servicebus topic subscription create. These might represent different client applications or different deployment contexts. Each subscription is created for a specific topic and just needs a name.

**Check Message Counts**: You can view subscription details including message counts using az servicebus topic subscription show. The messageCount property tells you how many messages are waiting in that particular subscription. Querying just the message count gives focused information without the full JSON output.

**Initial State**: Both subscriptions show zero messages, which makes sense - we haven't published anything yet. The subscriptions exist and are ready to receive, but there's no data flowing.

---

## Publish Messages to the Topic

Publishing to topics uses the same code as sending to queues, which is a powerful abstraction in the Service Bus SDK.

**Understanding Authorization**: Every namespace has a root access policy with full permissions, but following the principle of least privilege, we should create specific policies with only the required rights. This is both a security best practice and what you'd do in production.

**Create Publisher Policy**: We're creating an authorization rule named "publisher" using az servicebus topic authorization-rule create. The rights parameter is set to just Send - not Listen or Manage. This ensures that if these credentials are compromised, they can only publish messages, not consume them or modify the topic configuration. This compartmentalization is fundamental to security.

**Get Connection String**: Using az servicebus topic authorization-rule keys list, we retrieve the connection string for the publisher role. The query parameter extracts just the primaryConnectionString, and tsv output gives us the raw value. This connection string contains the endpoint, policy name, and shared access key - everything the application needs to authenticate.

**Run Publisher**: We're starting the publisher using dotnet run, specifying the topic name as "broadcast" with -topic, and passing the connection string with -cs. Quote the connection string since it contains special characters that shells might interpret.

**Observe Publishing**: Watch the publisher send batches of messages. After a few batches, stop it with Ctrl+C to demonstrate message accumulation.

**Check Subscription Counts**: Using az servicebus topic subscription show for both web and desktop subscriptions, query just the messageCount. Both subscriptions have identical counts. This demonstrates the pub-sub pattern perfectly - the topic forwarded all messages to all subscriptions. Each subscription maintains its own independent copy of every message.

**Explore in Portal**: Opening a subscription in the Portal and using Service Bus Explorer lets you peek at message contents without consuming them. This tool is invaluable for debugging message structure and verifying content during development.

---

## Receive Messages from a Subscription

Receiving from subscriptions requires Listen rights rather than Send rights.

**Create Subscriber Policy**: We're creating another authorization rule named "subscriber" with Listen rights using az servicebus topic authorization-rule create. This separation of concerns means subscribers can only consume messages, not send them. Different parts of your application get different credentials with appropriate permissions.

**Get Subscriber Connection String**: Using the same keys list command but for the subscriber authorization rule retrieves the listener credentials.

**Run Subscriber**: We're starting a subscriber on the web subscription using dotnet run with the subscriber project. The parameters include -topic set to "broadcast", -subscription set to "web" to indicate which subscription to consume from, and the subscriber connection string. This is different from queue consumption which only needs the queue name - subscriptions require both topic and subscription names.

**Message Expiry**: If messages haven't expired based on the ten-minute TTL we set earlier, you'll see them immediately. This demonstrates the importance of understanding TTL settings in your messaging architecture. If too much time has passed, messages will be gone.

**Real-Time Messaging**: Leave the subscriber running and start the publisher again in another terminal. Watch both windows - the publisher logs when it sends each batch, and the subscriber prints the messages it receives. This is asynchronous messaging in action. The components are completely decoupled, communicating only through the Service Bus topic without any direct connection.

---

## Receive Messages from Both Subscriptions

Independent subscriptions enable different processing speeds and different consumer concerns.

**Compare Message Counts**: One subscriber is consuming from the web subscription, but desktop has no consumers. Running az servicebus topic subscription show for both reveals an important characteristic. The web subscription shows zero messages because they've all been delivered to the consumer and acknowledged. The desktop subscription shows every message that's been published and hasn't expired yet.

**Understanding Independence**: Each subscription maintains its own independent message queue. Messages consumed from one subscription don't affect other subscriptions. This is the power of pub-sub - different consumers can operate at completely different speeds and with different levels of reliability without impacting each other.

**Start Desktop Subscriber**: Starting a subscriber for the desktop subscription in a new terminal shows interesting behavior. The desktop subscriber immediately processes all the backlogged messages rapidly. Meanwhile, the web subscriber waits for new messages since it's already caught up. This demonstrates how different consumers can have wildly different states - one caught up, one with a backlog - without affecting each other's operation.

**Steady State**: Once the desktop subscriber processes its backlog, both subscribers are caught up and wait for new messages. When the publisher sends new messages, both subscribers receive their own copy simultaneously. The fan-out pattern works beautifully - one message published, multiple subscribers receive independent copies to process at their own pace.

---

## Lab

Service Bus reliability and scalability enable sophisticated architectures, but understanding the behavior requires experimentation.

**Multiple Subscribers on Same Subscription**: What happens if you have multiple subscribers listening on the same subscription? Do they all get copies of every message, or does Service Bus distribute messages between them? Start two or more instances of the subscriber on the web subscription and observe the behavior carefully. This is a different pattern from multiple subscriptions - you're testing competing consumers within a single subscription.

**Multiple Publishers**: What happens with multiple publishers sending to the same topic simultaneously? Start two publisher instances in separate terminals. Does message ordering change? Do all subscribers still receive all messages? Are there any unexpected behaviors?

**Understanding Implications**: These experiments reveal fundamental messaging patterns. Multiple subscribers on the same subscription implement the competing consumers pattern for load balancing. Multiple subscriptions implement the fan-out pattern for independent processing. Understanding both patterns is crucial for designing distributed systems.

---

## Cleanup

Proper cleanup prevents ongoing charges and keeps your subscription organized.

**Delete Resource Group**: We're using az group delete with -y to confirm without prompting and --no-wait to return immediately without waiting for completion. This removes everything - the namespace, topics, queues, subscriptions, and all authorization rules we created. The deletion happens asynchronously in the background.
