# Event Hubs Partitioned Consumers - Exercise Walkthrough

## Exercise 1: Create the Foundation Resources

Let's start by creating the core infrastructure. We need an Event Hub namespace and a Storage Account to support our partitioned consumer pattern.

### Creating the Event Hub Namespace

First, we'll create a resource group called "labs-eventhubs-consumers" in West Europe with the courselabs tag to hold everything for this lab.

Now let's create the Event Hub namespace. Notice we're using the Standard SKU - this is important because the Basic SKU doesn't support the consumer group and partitioning features we need for this exercise. The Standard tier unlocks capabilities like multiple consumer groups, longer message retention, and higher throughput limits.

We're setting minimum TLS to 1.2 for security compliance, which is a best practice requirement for most organizations. The capacity parameter is set to 2 throughput units - each throughput unit provides 1 MB per second ingress and 2 MB per second egress, so we have 2 MB/s in and 4 MB/s out capacity.

### Creating the Storage Account

Next, we need a Storage Account. The consumer library will use blob storage to track which events have been processed - this checkpoint mechanism is how consumers maintain their position in the event stream.

We're using Zone-Redundant Storage which replicates data synchronously across three availability zones within the region. This provides excellent reliability without the cost of geo-redundancy.

Now let's create two blob containers. One will store consumer checkpoints - these are small files that record which events each consumer has processed. The other will store captured events - Event Hubs can automatically archive all events to blob storage, which we'll configure later.

It's important to understand that there's no direct link between the Event Hub and Storage Account at the infrastructure level. They're independent resources. The connection only exists through the consumer application code that uses both services.

### Exploring Networking Options

Open the Event Hub namespace in the Azure Portal. In the left menu, you'll see a Networking option. This is where you can configure various network security features.

You can control public network access - completely open, completely restricted, or somewhere in between. You can configure private endpoints to connect your Event Hub to a virtual network, keeping traffic within Azure's backbone. And you can set up firewall rules to restrict access by specific IP addresses.

This networking layer is useful for enterprise scenarios where Event Hubs should only be accessible from within your corporate network or specific Azure resources, not from the public internet.

## Exercise 2: Configure the Event Hub and Consumer Groups

Now let's create the actual Event Hub instance and set up consumer groups.

### Creating the Event Hub

The partition count is a critical decision that affects both scalability and cost. More partitions allow more parallel processing by supporting more concurrent consumers, but each partition has a cost. Fewer partitions save money but limit your ability to scale out.

Here's the key constraint - once you set the partition count, you cannot change it. The only way to change partition count is to create a new Event Hub and migrate your workload. So think carefully about your scaling needs.

We're creating 5 partitions for this lab and setting retention to 2 days. The Standard SKU allows up to 7 days of retention, which is helpful when consumers fall behind during maintenance windows or peak load periods - the events are still available when the consumer catches up.

### Working with Consumer Groups

Open the Event Hub in the Portal and navigate to the Consumer Groups tab. You'll see a default group called "$Default" - every Event Hub includes this automatically. Try to delete it - you'll find you cannot. The default group is protected and always present.

Let's create two additional consumer groups using the CLI. We're creating a "processing" group and an "auditing" group.

Consumer groups allow different applications or components to read the same event stream independently. They're conceptually similar to Service Bus topics with multiple subscriptions - each consumer group gets all the data but can process it at its own pace with its own checkpoint state.

The processing group might have multiple consumer instances for high throughput parallel processing, while the auditing group might have just one consumer for sequential logging. They don't interfere with each other - each maintains its own position in the stream.

## Exercise 3: Publish Events and Configure Capture

Now let's start sending events to our Event Hub.

### Publishing Events

We'll use a .NET producer application to send events. First, we need the connection string from the RootManageSharedAccessKey authorization rule. We're querying for just the primaryConnectionString and outputting it in TSV format.

This connection string looks like "Endpoint=sb://namespace.servicebus.windows.net/;SharedAccessKeyName=keyname;SharedAccessKey=keyvalue". It contains everything the application needs to connect and authenticate.

Now let's publish a substantial amount of test data - 100 batches with 50 events each, giving us 5,000 events total. We're running the producer application with parameters specifying the batch count, batch size, and connection string.

You'll see output showing batches being sent to different partitions. The Event Hub client library automatically distributes events across partitions using a round-robin or hash-based approach for load balancing. Each partition receives a portion of the events.

### Enabling Capture

The Standard SKU includes a powerful feature called Capture - it automatically stores all events to blob storage in Apache Avro format. This is perfect for long-term archival, compliance requirements, or batch analytics.

Open the Event Hub in the Portal and navigate to the Capture configuration. Set the output format to Avro - this is a compact binary format with schema information embedded. Turn Capture to On. Set the Size window to the minimum value - this controls how large the file gets before capture creates a new file. Enable "Do not emit empty files when no events occur" to avoid creating unnecessary empty files during quiet periods.

Select your devicelogs blob container as the destination. Leave the other settings at defaults and save the configuration.

Wait a couple of minutes for capture to process the events you've already sent, then check the devicelogs container in your Storage Account. You'll see a folder structure organized hierarchically by event hub name, namespace, partition ID, year, month, day, hour, minute, and second. Each Avro file captures a slice of time.

This structure makes it easy to locate events from specific time periods. For example, if you need all events from a particular hour, you can navigate directly to that folder. The Avro files are compressed and efficient, perfect for long-term storage and batch analysis with tools like Spark or Azure Data Factory.

## Exercise 4: Run the Partitioned Consumer

Now for the main event - running consumers that use the partitioned consumer pattern with checkpointing.

### Understanding the Consumer Code

The consumer application uses the EventProcessorClient from the Azure SDK. The code might look complex at first, but most of it is just setup and configuration. The key conceptual points are what matter.

The consumer connects to both Event Hubs for reading events and Storage for maintaining checkpoints. It specifies which consumer group to use - remember, different consumer groups maintain independent positions. It processes events in batches for efficiency rather than one at a time. And it calls UpdateCheckpoint periodically to record its progress in blob storage.

The checkpoint is the key to reliability. By storing the sequence number offset in blob storage, the consumer can resume from exactly where it left off after any interruption - planned shutdown, crash, or network issue.

### Running a Single Consumer

Let's start one consumer instance. You'll need both the Event Hub connection string and the Storage connection string.

The Event Hub connection string comes from the namespace authorization rule, and the Storage connection string comes from the storage account. Now we run the processor application, passing both connection strings as parameters.

Watch the output. You'll see log messages every 100 events showing which partitions are being processed. The single consumer will gradually take ownership of all 5 partitions. The Event Hubs SDK manages partition assignment automatically - this consumer claims partitions until it has balanced ownership.

When processing finishes, run the consumer again. Notice something important: it doesn't process the same events again. The checkpoint mechanism is working - the consumer knows where it left off in each partition and continues from there.

### Testing Checkpointing

The checkpoint provides an "at-least-once" delivery guarantee. Every event will be processed at least once, but some might be processed twice in certain failure scenarios.

Why might duplicates occur? A consumer could process a batch of events and then crash before updating the checkpoint. When it restarts, it processes those events again because the checkpoint wasn't updated. This is acceptable in many scenarios, but it's important to understand. Ideally, your processing logic should be idempotent - processing the same event multiple times produces the same result as processing it once.

## Exercise 5: Scaling with Multiple Consumers

The real power of this pattern is horizontal scaling. Open two more terminal windows and start a consumer in each - you'll now have three consumers total, all in the same consumer group.

Now publish more events using the producer application again - another 100 batches of 50 events each.

Watch all three terminal windows simultaneously. You'll see the work is automatically distributed - each consumer processes events from different partitions. Some consumers might own 2 partitions while others own 1 or 2, depending on how the ownership balances. The Event Hubs SDK automatically manages partition ownership distribution using a lease mechanism stored in the Storage Account.

Check the checkpoints container in your Storage Account. You'll see multiple checkpoint files - one per consumer per partition owned. This is how consumers coordinate without needing a central coordinator service. The coordination is peer-to-peer through shared storage.

### Testing Failover

Now for the dramatic part - stop one of the consumers midway through processing. Just terminate the process. Watch what happens to the other consumers.

After a brief delay (usually 10-30 seconds), the remaining consumers detect that one consumer has dropped out. They automatically rebalance partition ownership, taking over the abandoned partitions. The work continues with no manual intervention required.

This is automatic high availability in action. When a consumer fails, the remaining consumers pick up its partitions and keep processing. When you start a new consumer, it automatically claims some partitions to help with the load. This elasticity is essential for production systems.

### Using Different Consumer Groups

Try starting a consumer with the auditing consumer group instead of the default processing group. You'll pass a -g parameter specifying "auditing".

This consumer processes all events from the beginning of the retention window, because the auditing group has never been used before. Each consumer group maintains its own checkpoint state, completely independent of other groups.

This is how you can have multiple independent processing pipelines reading the same event stream. One pipeline might process events for real-time analytics, another for auditing and compliance, and another for machine learning model training - all reading the same events but maintaining different processing positions.

## Key Takeaways

We've seen how Event Hubs partitioned consumers provide several critical capabilities for production event processing systems.

Reliable processing is achieved through checkpoint-based resumption - consumers can restart from exactly where they left off. Automatic scaling across multiple consumer instances allows you to handle varying load by adding or removing consumers dynamically. High availability comes through automatic failover - when a consumer fails, others take over its partitions.

Independent processing pipelines are enabled through consumer groups - different applications can process the same events independently. And long-term event storage through Capture ensures you never lose data and can perform batch analytics on historical events.

This pattern is essential for building production-grade event processing systems on Azure. It combines reliability, scalability, and flexibility in a way that's difficult to achieve with other approaches.

Understanding these patterns and their trade-offs is crucial for the AZ-204 exam and for building real-world cloud applications.
