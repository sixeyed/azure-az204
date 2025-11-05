# Azure Service Bus Queues - Quickfire Questions

## Question 1
What is Azure Service Bus?

- A) A virtual network service
- B) A fully managed enterprise message broker with queues and topics
- C) A database service
- D) A monitoring service

**Answer: B**
Service Bus provides reliable cloud messaging as a service with advanced features like transactions, ordering, and duplicate detection.

---

## Question 2
What is the difference between Service Bus and Storage Queues?

- A) No difference
- B) Service Bus offers advanced features (FIFO, transactions, duplicate detection, larger messages)
- C) Storage Queues are always better
- D) Service Bus doesn't support messaging

**Answer: B**
Service Bus is enterprise messaging with 256KB messages, FIFO, sessions, transactions. Storage Queues are simpler, 64KB messages.

---

## Question 3
What are the Service Bus tiers?

- A) Free and Paid
- B) Basic, Standard, Premium
- C) Small and Large
- D) Developer and Production

**Answer: B**
Basic (queues only), Standard (queues + topics), Premium (high throughput, VNet, geo-disaster recovery).

---

## Question 4
What is the maximum message size in Standard tier?

- A) 64 KB
- B) 256 KB
- C) 1 MB
- D) 100 MB

**Answer: B**
Standard tier supports up to 256 KB per message. Premium supports up to 1 MB (or 100 MB with large message support).

---

## Question 5
What is FIFO ordering in Service Bus?

- A) Random order
- B) First-In-First-Out message ordering using sessions
- C) Newest first
- D) Priority-based only

**Answer: B**
Sessions enable strict FIFO ordering for related messages grouped by SessionId.

---

## Question 6
What is duplicate detection?

- A) Security feature
- B) Automatically ignores/removes duplicate messages based on MessageId
- C) Compression
- D) Encryption

**Answer: B**
Duplicate detection uses MessageId to identify and discard duplicate messages within a configurable time window.

---

## Question 7
What is message deferral?

- A) Delaying message send
- B) Postponing message processing; message set aside and retrieved later by sequence number
- C) Message deletion
- D) Message archiving

**Answer: B**
Deferral allows receivers to postpone processing specific messages, retrieving them later using their sequence number.

---

## Question 8
What is the dead-letter queue (DLQ)?

- A) A backup queue
- B) Subqueue for messages that can't be processed or exceeded MaxDeliveryCount
- C) A logging queue
- D) A priority queue

**Answer: B**
DLQ stores failed messages for investigation, preventing them from blocking queue processing.

---

## Question 9
What are transactions in Service Bus?

- A) Payment processing
- B) Atomic operations across multiple messages/queues ensuring all-or-nothing execution
- C) Database transactions
- D) Not supported

**Answer: B**
Transactions group multiple send/receive operations; all succeed or all roll back, ensuring consistency.

---

## Question 10
Can Service Bus integrate with Azure Event Grid?

- A) No integration
- B) Yes, can trigger Event Grid events for message arrival
- C) Only manually
- D) Requires third-party tools

**Answer: B**
Service Bus can publish events to Event Grid when messages arrive, enabling event-driven architectures.
