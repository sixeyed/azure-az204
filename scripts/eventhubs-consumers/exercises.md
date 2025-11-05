# Event Hubs Partitioned Consumers - Exercise Walkthrough

## Exercise 1: Create the Foundation Resources

Let's start by creating the core infrastructure. We need an Event Hub namespace and a Storage Account.

### Creating the Event Hub Namespace

First, we'll create a resource group to hold everything:

```bash
az group create -n labs-eventhubs-consumers --tags courselabs=azure -l westeurope
```

Now let's create the Event Hub namespace. Notice we're using the Standard SKU - this is important because the Basic SKU doesn't support the partitioned consumer features we need:

```bash
az eventhubs namespace create --min-tls 1.2 --capacity 2 --sku Standard -g labs-eventhubs-consumers -l westeurope -n <your-unique-namespace-name>
```

We're setting minimum TLS to 1.2 for security, and capacity to 2 throughput units to handle our expected load.

### Creating the Storage Account

Next, we need a Storage Account. The consumer library will use blob storage to track which events have been processed:

```bash
az storage account create --sku Standard_ZRS -g labs-eventhubs-consumers -l westeurope -n <your-unique-storage-name>
```

We're using Zone-Redundant Storage for reliability within the region.

Now let's create two blob containers. One will store consumer checkpoints, and the other will store captured events:

```bash
az storage container create -n checkpoints -g labs-eventhubs-consumers --account-name <your-storage-name>

az storage container create -n devicelogs -g labs-eventhubs-consumers --account-name <your-storage-name>
```

Important note: There's no direct link between the Event Hub and Storage Account at the infrastructure level. They're only connected through the consumer code.

### Exploring Networking Options

Open the Event Hub namespace in the Azure Portal. In the left menu, you'll see a Networking option. This is where you can configure:

- Public network access
- Private endpoints for VNet integration
- Firewall rules to restrict access by IP address

This is useful for enterprise scenarios where Event Hubs should only be accessible from within your virtual network.

## Exercise 2: Configure the Event Hub and Consumer Groups

Now let's create the actual Event Hub and set up consumer groups.

### Creating the Event Hub

The partition count is a critical decision. More partitions allow more parallel processing but cost more. Fewer partitions save money but limit scale. And remember - once set, you cannot change it.

```bash
az eventhubs eventhub create --name devicelogs --partition-count 5 --message-retention 2 -g labs-eventhubs-consumers --namespace-name <your-namespace-name>
```

We're creating 5 partitions and setting retention to 2 days. The Standard SKU allows up to 7 days of retention, which is helpful when consumers fall behind during peak periods.

### Working with Consumer Groups

Open the Event Hub in the Portal and look at the Consumer Groups tab. You'll see a default group called "$Default". Every Event Hub has this. Try to delete it - you'll find you cannot. The default group is always present.

Let's create two additional consumer groups using the CLI:

```bash
az eventhubs eventhub consumer-group create -n processing --eventhub-name devicelogs -g labs-eventhubs-consumers --namespace-name <your-namespace-name>

az eventhubs eventhub consumer-group create -n auditing --eventhub-name devicelogs -g labs-eventhubs-consumers --namespace-name <your-namespace-name>
```

Consumer groups allow different components to read the same event stream independently. They're conceptually similar to Service Bus topics - each group gets all the data but can process it at its own pace.

The processing group might have multiple consumers for high throughput, while the auditing group might have just one consumer for sequential logging.

## Exercise 3: Publish Events and Configure Capture

Now let's start sending events to our Event Hub.

### Publishing Events

We'll use a .NET producer application. First, we need the connection string:

```bash
az eventhubs namespace authorization-rule keys list -n RootManageSharedAccessKey --query primaryConnectionString -o tsv -g labs-eventhubs-consumers --namespace-name <your-namespace-name>
```

This gives you a connection string that looks like: Endpoint=sb://NAMESPACE.servicebus.windows.net/;SharedAccessKeyName=KEYNAME;SharedAccessKey=KEYVALUE

Now let's publish 100 batches of 50 events each - that's 5,000 events total:

```bash
dotnet run --project ./src/eventhubs/producer -ProducerCount 100 -BatchSize 50 -cs '<your-connection-string>'
```

You'll see output showing batches being sent to different partitions. The Event Hub client automatically distributes events across partitions for load balancing.

### Enabling Capture

The Standard SKU includes a powerful feature called Capture - it automatically stores all events to blob storage in Avro format.

Open the Event Hub in the Portal and configure Capture:

1. Set the output format to Avro
2. Turn Capture On
3. Set the Size window to minimum (the smallest file size before capture)
4. Enable "Do not emit empty files when no events occur"
5. Select your devicelogs blob container

Leave other settings at defaults and save.

Wait a couple of minutes, then check the devicelogs container in your Storage Account. You'll see a folder structure organized by date and time:

```
devicelogs/EVENT_HUB_NAME/NAMESPACE/PARTITION_ID/YEAR/MONTH/DAY/HOUR/MINUTE/SECOND.avro
```

This structure makes it easy to locate events from specific time periods. The Avro files are compressed and efficient, perfect for long-term storage and batch analysis.

## Exercise 4: Run the Partitioned Consumer

Now for the main event - running consumers that use the partitioned consumer pattern.

### Understanding the Consumer Code

The consumer application uses the EventProcessorClient from the Azure SDK. The code might look complex, but most of it is just setup. The key points are:

- It connects to both Event Hubs and Storage
- It specifies which consumer group to use
- It processes events in batches
- It calls UpdateCheckpoint to record progress

The checkpoint is the key to reliability. By storing the offset in blob storage, the consumer can resume after any interruption.

### Running a Single Consumer

Let's start one consumer. You'll need both connection strings:

```bash
# Event Hub connection string
az eventhubs namespace authorization-rule keys list -n RootManageSharedAccessKey --query primaryConnectionString -o tsv -g labs-eventhubs-consumers --namespace-name <your-namespace-name>

# Storage connection string
az storage account show-connection-string --query connectionString -o tsv -g labs-eventhubs-consumers -n <your-storage-name>

# Run the consumer
dotnet run --project ./src/eventhubs/processor -cs '<event-hub-connection-string>' -scs '<storage-connection-string>'
```

Watch the output. You'll see log messages every 100 events, showing which partitions are being processed. The single consumer will eventually take ownership of all 5 partitions.

When processing finishes, run the consumer again. Notice something important: it doesn't process the same events again. The checkpoint mechanism is working - the consumer knows where it left off.

### Testing Checkpointing

The checkpoint provides an "at-least-once" delivery guarantee. Every event will be processed at least once, but some might be processed twice.

Why? A consumer could process events and crash before updating the checkpoint. When it restarts, it processes those events again. This is acceptable in many scenarios, but your processing logic should be idempotent when possible.

## Exercise 5: Scaling with Multiple Consumers

The real power of this pattern is scaling. Open two more terminal windows and start a consumer in each - three consumers total.

Now publish more events:

```bash
dotnet run --project ./src/eventhubs/producer -ProducerCount 100 -BatchSize 50 -cs '<your-connection-string>'
```

Watch all three terminal windows. You'll see the work is distributed - each consumer processes events from different partitions. The Event Hubs library automatically manages partition ownership.

Check the checkpoints container in your Storage Account. You'll see multiple checkpoint files - one per consumer per partition. This is how consumers coordinate without needing a central coordinator.

### Testing Failover

Stop one of the consumers midway through processing. Watch what happens to the other consumers. They'll detect that a consumer has dropped out and rebalance - taking over the abandoned partitions.

This is automatic high availability. No manual intervention needed.

### Using Different Consumer Groups

Try starting a consumer with the auditing consumer group:

```bash
dotnet run --project ./src/eventhubs/processor -cs '<event-hub-connection-string>' -scs '<storage-connection-string>' -g auditing
```

This consumer processes all events from the beginning, because the auditing group has never been used before. Each consumer group maintains its own checkpoint state, completely independent of other groups.

This is how you can have multiple independent processing pipelines reading the same event stream.

## Key Takeaways

We've seen how Event Hubs partitioned consumers provide:

- Reliable processing with checkpoint-based resumption
- Automatic scaling across multiple consumer instances
- High availability with automatic failover
- Independent processing pipelines with consumer groups
- Long-term event storage with Capture

This pattern is essential for building production-grade event processing systems on Azure.
