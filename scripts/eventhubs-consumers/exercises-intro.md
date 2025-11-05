# Event Hubs Consumers - Exercises Introduction

We've covered Event Hubs as Azure's big data streaming platform with focus on partitioned consumer patterns for reliable, scalable event processing. Now let's implement a production-ready event consumer.

## What You'll Do

You'll start by **creating an Event Hub namespace with Standard SKU** (required for multiple consumer groups and partitions). You'll configure **partitions** (units of parallelism) and **consumer groups** (independent processing pipelines). Then you'll set up **blob storage for checkpoints** - this is where consumers track which events they've processed.

Next, you'll run **the Event Hubs client library** that automatically handles checkpoint recording. You'll **run multiple consumers** and watch as they automatically distribute partition ownership. When you start a second consumer, it claims some partitions from the first consumer. When you stop a consumer, the remaining consumers automatically take over its partitions. This is **automatic rebalancing** in action - no manual coordination required!

You'll **demonstrate checkpoint-based processing** by publishing events, watching them get processed, then deliberately crashing a consumer. When you restart it, it resumes from the last checkpoint rather than reprocessing everything. This is **at-least-once delivery** - some events might be processed twice (if the consumer crashed before checkpointing), but none are lost.

You'll enable **Event Hub Capture** to automatically archive events to Avro format in blob storage. This provides long-term retention and enables batch processing scenarios alongside real-time processing.

The **challenge** involves using **different consumer groups** for independent processing. The real-time pipeline processes events immediately, while the auditing pipeline can process the same events at its own pace. Consumer groups enable multiple applications to read the same event stream independently.

Let's build reliable event processing!
