# Service Bus Publish-Subscribe - AZ-204 Exam Introduction

Excellent work with pub-sub messaging! This pattern is essential for the AZ-204 exam's messaging section.

## What We'll Cover

**Understanding pub-sub versus queuing patterns** is frequently tested. Queues provide point-to-point communication where each message is consumed by exactly one receiver. Topics provide publish-subscribe where one or more senders publish to multiple subscribers, and each subscription gets a copy. The exam presents scenarios requiring you to choose the appropriate pattern.

**Service Bus tier selection** must be memorized. Basic tier supports queues only with maximum 256 KB messages. Standard tier supports both queues and topics with 256 KB messages. Premium tier provides enhanced performance, message size up to 100 MB, and VNet integration. The exam may present scenarios where you need to choose the appropriate tier based on requirements like "need topics" or "need VNet integration."

**Topics and subscriptions architecture** needs to be understood. Topics are destinations for publishers sending messages. Subscriptions are independent receivers getting copies of topic messages. Each subscription gets its own copy of matching messages. Messages are forwarded to all subscriptions. Subscriptions can have filters and rules. The exam tests understanding of how messages flow through this architecture.

**Subscription filters** appear on the exam. SQL filters are flexible but slower, using expressions like "priority='high' AND region='east'". Correlation filters are more efficient (recommended) for simple property matching. Boolean filters include TrueFilter (receives all messages, the default) and FalseFilter (receives no messages). The exam tests choosing the appropriate filter type.

**Authorization and security** is critical. Shared Access Signatures (SAS) provide authorization rules with specific rights including Send, Listen, or Manage. Principle of least privilege means creating specific policies for publishers (Send rights) and subscribers (Listen rights). Connection strings contain endpoint and credentials. Azure Active Directory integration for more advanced scenarios. The exam tests understanding of when to use different authorization approaches.

**Message Time-to-Live (TTL)** controls message expiration. Can be set at topic level as default for all messages. Can be overridden per message. Prevents old messages from accumulating. Uses ISO 8601 duration format like P0DT0H10M1S. The exam may ask you to configure TTL for specific business requirements.

We'll cover **competing consumers pattern** (multiple receivers on same subscription), **working with CLI commands** (`az servicebus topic create`, `az servicebus topic subscription create`, `az servicebus topic authorization-rule create`), **application development** with Azure.Messaging.ServiceBus SDK, and **common scenarios** about implementing fan-out messaging, filtering messages to different subscribers, and designing multi-subscriber architectures.

Master pub-sub patterns for the AZ-204!
