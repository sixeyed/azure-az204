# Azure Service Bus Queues - Quickfire Questions

## Question 1
What is Azure Service Bus?


- A) A database service
- B) A virtual network service
- C) A monitoring service
- D) A fully managed enterprise message broker with queues and topics

**Answer: D**
Service Bus provides reliable cloud messaging as a service with advanced features like transactions, ordering, and duplicate detection.
---
## Question 2
What is the difference between Service Bus and Storage Queues?


- A) Service Bus offers advanced features (FIFO, transactions, duplicate detection, larger messages)
- B) No difference
- C) Service Bus doesn't support messaging
- D) Storage Queues are always better

**Answer: A**
Service Bus is enterprise messaging with 256KB messages, FIFO, sessions, transactions. Storage Queues are simpler, 64KB messages.
---
## Question 3
What are the Service Bus tiers?


- A) Free and Paid
- B) Small and Large
- C) Developer and Production
- D) Basic, Standard, Premium

**Answer: D**
Basic (queues only), Standard (queues + topics), Premium (high throughput, VNet, geo-disaster recovery).
---
## Question 4
What is the maximum message size in Standard tier?


- A) 256 KB
- B) 64 KB
- C) 1 MB
- D) 100 MB

**Answer: A**
Standard tier supports up to 256 KB per message. Premium supports up to 1 MB (or 100 MB with large message support).
---
## Question 5
What is FIFO ordering in Service Bus?


- A) Priority-based only
- B) Random order
- C) Newest first
- D) First-In-First-Out message ordering using sessions

**Answer: D**
Sessions enable strict FIFO ordering for related messages grouped by SessionId.
---
## Question 6
What is duplicate detection?


- A) Encryption
- B) Automatically ignores/removes duplicate messages based on MessageId
- C) Compression
- D) Security feature

**Answer: B**
Duplicate detection uses MessageId to identify and discard duplicate messages within a configurable time window.
---
## Question 7
What is message deferral?


- A) Delaying message send
- B) Message archiving
- C) Postponing message processing; message set aside and retrieved later by sequence number
- D) Message deletion

**Answer: C**
Deferral allows receivers to postpone processing specific messages, retrieving them later using their sequence number.
---
## Question 8
What is the dead-letter queue (DLQ)?


- A) Subqueue for messages that can't be processed or exceeded MaxDeliveryCount
- B) A logging queue
- C) A priority queue
- D) A backup queue

**Answer: A**
DLQ stores failed messages for investigation, preventing them from blocking queue processing.
---
## Question 9
What are transactions in Service Bus?


- A) Database transactions
- B) Not supported
- C) Atomic operations across multiple messages/queues ensuring all-or-nothing execution
- D) Payment processing

**Answer: C**
Transactions group multiple send/receive operations; all succeed or all roll back, ensuring consistency.
---
## Question 10
Can Service Bus integrate with Azure Event Grid?


- A) Requires third-party tools
- B) Only manually
- C) Yes, can trigger Event Grid events for message arrival
- D) No integration

**Answer: C**
Service Bus can publish events to Event Grid when messages arrive, enabling event-driven architectures.