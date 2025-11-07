# Event Hubs Partitioned Consumers

## Reference

Processing a partitioned stream of events reliably requires careful logic that would be complex to build yourself. Microsoft has built this capability into client libraries for various languages, handling the intricate details of distributed event processing. The library takes care of recording the processed offset using blob storage as a simple state store, ensuring that each consumer picks up exactly where it left off in the event stream. It supports running at scale with multiple consumers working in parallel, and when one consumer fails, the others automatically pick up its partitions and continue processing. This coordination happens automatically without requiring external orchestration services.

This partitioned consumer pattern is fundamental to building production-grade event processing systems on Azure. Understanding how it achieves reliability, scalability, and high availability is crucial for architecting real-world solutions.

## Create an Event Hub Namespace & Storage Account

The foundation of the partitioned consumer pattern requires two services working together - Event Hubs for the event stream and Storage for checkpoint coordination.

**Create Resource Group**: We're creating a resource group called "labs-eventhubs-consumers" in West Europe with tags for tracking. This organization keeps all related resources together for easy management and cleanup.

**Create Event Hub Namespace**: We're using Standard SKU because Basic doesn't support the features we need for this pattern. Standard tier unlocks multiple consumer groups, longer message retention up to seven days, and higher throughput limits. We're setting minimum TLS to 1.2 for security compliance, which is best practice for most organizations. The capacity parameter is set to 2 throughput units - each throughput unit provides 1 MB per second ingress and 2 MB per second egress, giving us 2 MB/s in and 4 MB/s out capacity.

**Create Storage Account**: The consumer library uses blob storage to track which events have been processed. This checkpoint mechanism is how consumers maintain their position in the event stream. We're using Zone-Redundant Storage which replicates data synchronously across three availability zones within the region, providing excellent reliability without the cost of geo-redundancy.

**Create Blob Containers**: We're creating two containers. The checkpoints container stores consumer progress - these are small files recording which events each consumer has processed. The devicelogs container will store captured events when we enable the Capture feature later. Event Hubs can automatically archive all events to blob storage, creating a permanent record.

**Understanding the Architecture**: There's no direct infrastructure link between the Event Hub and Storage Account. They're independent Azure resources. The connection only exists in the consumer application code that uses both services together. This separation of concerns provides flexibility - you could use different storage accounts for different purposes or swap storage without changing the Event Hub configuration.

**Explore Networking Options**: Opening the Event Hub namespace in the Portal reveals a Networking section with several security features. You can control public network access completely, configure private endpoints to connect your Event Hub to a virtual network keeping traffic within Azure's backbone, and set up firewall rules restricting access by specific IP addresses. This networking layer is essential for enterprise scenarios where Event Hubs should only be accessible from within your corporate network or specific Azure resources.

---

## Create an Event Hub & Consumer Groups

Creating the Event Hub itself involves critical decisions that can't be changed later.

**Understanding Partition Count**: The partition count is set at creation and can never be changed. This makes it a critical architectural decision. More partitions allow more parallel processing by supporting more concurrent consumers, but each partition has a cost. Fewer partitions save money but limit your scaling ability. The only way to change partition count is creating a new Event Hub and migrating your workload.

**Create Event Hub**: We're creating an Event Hub named "devicelogs" with 5 partitions. This gives us room to run up to 5 concurrent consumers per consumer group. We're setting retention to 2 days - Standard SKU allows up to 7 days. Longer retention is helpful when consumers fall behind during maintenance windows or peak load periods. The events remain available when consumers catch up rather than being lost.

**Default Consumer Group**: Opening the Event Hub in the Portal and checking the Consumer groups tab shows a default group called "$Default" present in every Event Hub. Try to delete it - you'll find you cannot. The default group is protected and always present. This ensures there's always at least one consumer group available.

**Create Additional Consumer Groups**: We're creating two additional consumer groups using the CLI - a "processing" group and an "auditing" group. Consumer groups allow different applications or components to read the same event stream independently. They're conceptually similar to Service Bus topics with multiple subscriptions - each consumer group gets all the data but can process it at its own pace with its own checkpoint state.

**Understanding Consumer Group Use Cases**: The processing group might have multiple consumer instances for high-throughput parallel processing, while the auditing group might have just one consumer for sequential logging. They don't interfere with each other - each maintains its own position in the stream. One could be caught up while another is processing events from hours ago, and neither affects the other.

---

## Publish Events and Configure Capture

Now let's populate the Event Hub with events and enable archival.

**Get Connection String**: We're using az eventhubs namespace authorization-rule keys list to retrieve the RootManageSharedAccessKey connection string. The query parameter extracts just the primaryConnectionString, and tsv output gives us the raw value. This connection string looks like "Endpoint=sb://namespace.servicebus.windows.net/;SharedAccessKeyName=keyname;SharedAccessKey=keyvalue" and contains everything the application needs to connect and authenticate.

**Publish Test Data**: We're running the producer application to send 100 batches of 50 events each, giving us 5,000 events total. Watch the output carefully - you'll see batches being sent to different partitions. The Event Hub client library automatically distributes events across partitions using round-robin or hash-based approaches for load balancing. Each partition receives a portion of the events.

**Understanding Publishing Semantics**: The publishing process is identical regardless of how many consumer groups exist. The publisher doesn't know or care about consumer groups - it just sends events to the Event Hub. The Event Hub service then makes those events available to all consumer groups. For production, you'd create a dedicated access policy with just Send permissions rather than using RootManageSharedAccessKey.

**Enable Capture**: Standard SKU includes a powerful feature called Capture that automatically stores all events to blob storage in Apache Avro format. This is perfect for long-term archival, compliance requirements, or batch analytics. Opening the Event Hub in the Portal and navigating to Capture configuration lets you enable it.

**Configure Capture Settings**: Set output format to Avro - this is a compact binary format with schema information embedded. Turn Capture to On. Slide the Size window down to the minimum - this controls how large files get before Capture creates a new one. Enable "Do not emit empty files when no events occur" to avoid creating unnecessary empty files during quiet periods. Select your devicelogs blob container as the destination.

**Explore Captured Events**: After a couple minutes for Capture to process existing events, check the devicelogs container in your Storage Account. You'll see a hierarchical folder structure organized by event hub name, namespace, partition ID, year, month, day, hour, minute, and second. Each Avro file captures a time slice of events. This structure makes locating events from specific time periods trivial - need all events from a particular hour? Navigate directly to that folder. The Avro files are compressed and efficient, perfect for long-term storage and batch analysis with tools like Spark or Azure Data Factory.

---

## Run Processing Consumers

Now we'll run consumers using the partitioned consumer pattern with checkpointing.

**Understanding the Consumer Code**: The consumer application in Program.cs uses EventProcessorClient from the Azure SDK. The code might look complex initially, but most of it is configuration and setup. The conceptual points are what matter. The consumer connects to both Event Hubs for reading events and Storage for maintaining checkpoints. It specifies which consumer group to use, remembering that different consumer groups maintain independent positions. It processes events in batches for efficiency rather than one at a time. The UpdateCheckpoint call is where progress gets recorded in blob storage.

**Understanding Checkpoints**: The checkpoint is the key to reliability. By storing the sequence number offset in blob storage, the consumer can resume from exactly where it left off after any interruption - planned shutdown, crash, or network issue. This is what distinguishes reliable event processing from simple polling.

**Run Single Consumer**: We're starting one consumer instance, which requires both the Event Hub connection string and the Storage connection string. Running the processor application with both connection strings passed as parameters starts the consumption. Watch the output - you'll see log messages every 100 events showing which partitions are being processed. The single consumer will gradually take ownership of all 5 partitions. The Event Hubs SDK manages partition assignment automatically - this consumer claims partitions until it achieves balanced ownership.

**Test Checkpoint Recovery**: When processing finishes, run the consumer again. Notice something crucial - it doesn't process the same events again. The checkpoint mechanism is working perfectly. The consumer knows where it left off in each partition and continues from there. This is the reliability guarantee in action.

**Understanding At-Least-Once Delivery**: The checkpoint provides an "at-least-once" delivery guarantee. Every event will be processed at least once, but some might be processed twice in certain failure scenarios. Why might duplicates occur? A consumer could process a batch of events and then crash before updating the checkpoint. When it restarts, it processes those events again because the checkpoint wasn't updated. This is acceptable in many scenarios, but you need to understand the implications. Ideally, your processing logic should be idempotent - processing the same event multiple times produces the same result as processing it once.

---

## Scaling with Multiple Consumers

The real power of this pattern emerges when running multiple consumers in parallel.

**Start Multiple Consumers**: Open two more terminal windows and start a consumer in each. You now have three consumers total, all in the same consumer group. Now publish more events using the producer application - another 100 batches of 50 events each.

**Observe Load Distribution**: Watch all three terminal windows simultaneously. The work is automatically distributed - each consumer processes events from different partitions. Some consumers might own 2 partitions while others own 1 or 2, depending on how ownership balances. The Event Hubs SDK automatically manages partition ownership distribution using a lease mechanism stored in the Storage Account.

**Explore Coordination Mechanism**: Check the checkpoints container in your Storage Account. You'll see multiple checkpoint files - one per consumer per partition owned. This is how consumers coordinate without needing a central coordinator service. The coordination is peer-to-peer through shared storage. Each consumer claims ownership of partitions by writing lease blobs, and other consumers respect those claims.

**Test Automatic Failover**: Now for the dramatic demonstration - stop one of the consumers midway through processing by terminating the process. Watch what happens to the other consumers. After a brief delay, usually 10-30 seconds, the remaining consumers detect that one consumer has dropped out. They automatically rebalance partition ownership, taking over the abandoned partitions. The work continues with no manual intervention required.

**Understanding High Availability**: This is automatic high availability in action. When a consumer fails, remaining consumers pick up its partitions and keep processing. When you start a new consumer, it automatically claims some partitions to help with the load. This elasticity is essential for production systems that need to handle failures gracefully and scale dynamically.

**Test Different Consumer Groups**: Start a consumer with the auditing consumer group instead of the default processing group by passing a -g parameter specifying "auditing". This consumer processes all events from the beginning of the retention window because the auditing group has never been used before. Each consumer group maintains its own checkpoint state, completely independent of other groups.

**Understanding Independent Processing Pipelines**: This demonstrates how you can have multiple independent processing pipelines reading the same event stream. One pipeline might process events for real-time analytics, another for auditing and compliance, and another for machine learning model training - all reading the same events but maintaining different processing positions. This is the power of consumer groups.

---

## Lab

The partitioned consumer pattern enables sophisticated production scenarios worth exploring.

**Multiple Consumers Load Balancing**: With three consumers running in the same consumer group, observe how work distribution changes over time. Does each consumer process roughly the same number of events? How long does rebalancing take when you add or remove consumers? Understanding these dynamics helps with capacity planning.

**Failover Recovery**: Stop a consumer midway through processing and observe how remaining consumers take over. Check the Storage Account to see how partition ownership changes. How long before the failed consumer's partitions are reassigned? This recovery time matters for high-availability requirements.

**Multiple Consumer Groups**: Start consumers in different consumer groups and verify they process events independently. The processing group and auditing group should each maintain their own progress through the event stream without affecting each other. This demonstrates true isolation.

**Checkpoint Inspection**: Explore the checkpoint blobs in your Storage Account. Open one to see its JSON structure. You'll find the offset, sequence number, and partition information. Understanding this structure helps diagnose consumer issues in production.

---

## Cleanup

Proper cleanup prevents ongoing charges and maintains subscription hygiene.

**Delete Resource Group**: We're using az group delete with -y to confirm without prompting and --no-wait to return immediately. This removes everything - the namespace, Event Hub, storage account, containers, and all data. The deletion happens asynchronously in the background.
