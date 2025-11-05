# Service Bus Messaging - AZ-204 Exam Introduction

Great work with Service Bus! This is a critical component of the "Connect to and Consume Azure Services" domain, accounting for 20-25% of the AZ-204 exam.

## What We'll Cover

**Point-to-point queuing patterns** must be understood. Queues provide FIFO ordering where each message is consumed by exactly one receiver. Messages are delivered in order they're sent (guaranteed with sessions), and PeekLock vs ReceiveAndDelete modes determine message settlement behavior. The exam tests understanding of when queues are appropriate versus other messaging patterns.

**Message sessions for FIFO guarantees** are frequently tested. Sessions provide guaranteed FIFO delivery, stateful processing with session state storage, and related message grouping. Messages with the same SessionId are processed in order. The exam presents scenarios like customer orders that must be processed sequentially or multi-step workflows needing state tracking.

**Dead-letter queue handling** is an exam favorite. Messages move to DLQ when max delivery count is exceeded (default 10), message TTL expires with dead-lettering enabled, or application code explicitly dead-letters them. The exam tests understanding of when and how to process the dead-letter queue.

**Service Bus vs Queue Storage** appears frequently on the exam. Service Bus supports 256 KB messages (Standard) or 1 MB (Premium), FIFO guarantees with sessions, topics/subscriptions, duplicate detection, transactions, and dead-letter queues. Queue Storage has 64 KB messages, no FIFO guarantee, no topics, but lower cost. The exam tests choosing the appropriate service based on requirements.

**Message settlement methods** need to be memorized. Complete marks successful processing and removes from queue. Abandon returns to queue and increments delivery count. Dead-letter moves to DLQ as unprocessable. Defer saves for later processing by sequence number. The exam tests understanding of when to use each method.

**Topics and subscriptions for pub-sub** enable one-to-many communication. Each subscription gets its own copy of matching messages, filters (SQL, correlation, boolean) determine which messages each subscription receives, and subscriptions act as independent queues. The exam tests scenarios where multiple components need to react to the same event.

We'll cover **duplicate detection** (requires MessageId and must be enabled at creation), **scheduled messages** (for delayed processing), **transactions** (atomic operations across messages), **tier differences** (Basic for queues only, Standard adds topics, Premium adds VNet integration and larger messages), and **common scenarios** about implementing reliable messaging, handling failures, and scaling message processing.

Master Service Bus for the AZ-204!
