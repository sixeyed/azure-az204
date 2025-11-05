# Event Hubs Consumers - AZ-204 Exam Introduction

Excellent work with Event Hubs! This is a key topic for AZ-204's "Develop message-based solutions" domain (10-15% of exam).

## What We'll Cover

**Partition architecture** is fundamental. Partitions are ordered sequences of events that enable parallelism and scale. Partition count is set at creation and **cannot be changed** (critical exam gotcha). Each partition has independent throughput, so 4 partitions = 4x throughput. The exam tests understanding of partition constraints and how they affect scaling.

**Consumer groups** enable multiple independent processing pipelines. The default group ($Default) is always available. Additional groups enable scenarios like real-time processing + batch analytics + auditing, all reading the same events independently. Each consumer group maintains its own checkpoints. The exam tests when to use multiple consumer groups versus multiple consumers in one group.

**Retention policies** define how long events are stored. Basic tier: 1 day. Standard tier: 1-7 days. Premium tier: up to 90 days. The exam tests understanding of retention requirements and choosing appropriate SKUs. Note that captured events (in blob storage) can be kept indefinitely regardless of Event Hub retention.

**The partitioned consumer pattern** with at-least-once delivery guarantees is heavily tested. Consumers use checkpoints to track progress, automatically rebalance when consumers fail, and may process some events multiple times (before checkpoint) but never lose events. The exam tests understanding of delivery guarantees and designing idempotent processing.

**SKU differences** must be memorized. Basic: 1-32 partitions, 1 consumer group, 1 day retention, no capture. Standard: 1-32 partitions, 20 consumer groups, 1-7 day retention, capture available. Premium/Dedicated: higher throughput, longer retention, network isolation. The exam tests choosing appropriate SKUs based on requirements.

**Checkpoint mechanisms** use blob storage to record consumer progress (container + blob per partition per consumer group). Checkpoints enable fault tolerance, prevent reprocessing all events after failures, but require idempotent processing because some events may be processed multiple times. The exam tests understanding of checkpoint behavior.

**When to use Event Hubs vs Service Bus** is a common scenario question. Event Hubs for: high-throughput event streaming, telemetry ingestion, distributed tracing, clickstream analysis. Service Bus for: enterprise messaging, guaranteed order within queues/topics, transactions, sessions. The exam tests choosing the right service.

We'll cover **CLI commands** for namespaces, event hubs, and consumer groups, **scaling with throughput units** (Basic/Standard) or processing units (Premium), **common troubleshooting** (partition balancing, checkpoint failures), and **integration with Event Grid and Kafka protocol**.

Master Event Hubs for the AZ-204!
