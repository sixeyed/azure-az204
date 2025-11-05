# Azure Functions Service Bus - Quickfire Questions

## Question 1
What can trigger a Service Bus-triggered Azure Function?

- A) Messages in a Service Bus queue or topic subscription
- B) Only queues
- C) Only topics
- D) HTTP requests

**Answer: A**
Service Bus triggers can respond to messages from both queues and topic subscriptions.

---

## Question 2
What is the difference between a Service Bus queue and topic?

- A) No difference
- B) Queue is one-to-one, Topic is one-to-many (pub-sub)
- C) Queue is faster
- D) Topic is cheaper

**Answer: B**
Queues provide point-to-point communication. Topics support publish-subscribe patterns with multiple subscriptions.

---

## Question 3
What happens to a message if the function processing it fails?

- A) Message is deleted
- B) Message is automatically retried based on delivery count
- C) Function stops
- D) Message is sent to another queue

**Answer: B**
Service Bus automatically redelivers messages when processing fails. After max delivery attempts, it goes to the dead-letter queue.

---

## Question 4
What is the dead-letter queue (DLQ)?

- A) A backup queue
- B) A queue for messages that couldn't be processed after max retries
- C) A deleted message archive
- D) A monitoring queue

**Answer: B**
The DLQ stores messages that failed processing after exceeding MaxDeliveryCount, allowing for investigation and manual handling.

---

## Question 5
How can you ensure message processing is exactly-once?

- A) Use Sessions and implement idempotent operations
- B) Set a special flag
- C) Use Premium tier
- D) It's guaranteed automatically

**Answer: A**
While Service Bus provides at-least-once delivery, exact-once requires sessions (for ordering) and idempotent function logic.

---

## Question 6
What is the PeekLock mode in Service Bus?

- A) Messages are deleted immediately
- B) Messages are locked temporarily; deleted only after successful processing
- C) Messages cannot be read
- D) Messages are permanently locked

**Answer: B**
PeekLock locks messages during processing. They're only deleted upon successful completion; otherwise, they're released for retry.

---

## Question 7
What is a Service Bus session?

- A) A connection to Service Bus
- B) A way to guarantee FIFO processing of related messages
- C) A monitoring period
- D) A pricing tier

**Answer: B**
Sessions enable ordered, FIFO processing of related messages by grouping them with a session ID.

---

## Question 8
How does the Service Bus trigger scale in Azure Functions?

- A) It doesn't scale
- B) Automatically, with instances based on queue/subscription depth
- C) Manually only
- D) Based on time of day

**Answer: B**
The Functions runtime scales based on queue length and message processing throughput using target-based scaling.

---

## Question 9
Can you send a message to a Service Bus queue from an Azure Function?

- A) No
- B) Yes, using output bindings
- C) Only with custom code
- D) Only in Premium plan

**Answer: B**
Service Bus output bindings allow functions to send messages to queues or topics declaratively.

---

## Question 10
What is the maximum message size for Service Bus Standard tier?

- A) 64 KB
- B) 256 KB
- C) 1 MB
- D) 100 MB

**Answer: B**
Standard tier supports up to 256 KB per message. Premium tier supports up to 1 MB (or 100 MB with large message support).
