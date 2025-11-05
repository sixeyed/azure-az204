# Azure Functions Service Bus - Quickfire Questions

## Question 1
What can trigger a Service Bus-triggered Azure Function?


- A) HTTP requests
- B) Only topics
- C) Only queues
- D) Messages in a Service Bus queue or topic subscription

**Answer: D**
Service Bus triggers can respond to messages from both queues and topic subscriptions.
---
## Question 2
What is the difference between a Service Bus queue and topic?


- A) Queue is faster
- B) Topic is cheaper
- C) Queue is one-to-one, Topic is one-to-many (pub-sub)
- D) No difference

**Answer: C**
Queues provide point-to-point communication. Topics support publish-subscribe patterns with multiple subscriptions.
---
## Question 3
What happens to a message if the function processing it fails?


- A) Message is deleted
- B) Function stops
- C) Message is sent to another queue
- D) Message is automatically retried based on delivery count

**Answer: D**
Service Bus automatically redelivers messages when processing fails. After max delivery attempts, it goes to the dead-letter queue.
---
## Question 4
What is the dead-letter queue (DLQ)?


- A) A deleted message archive
- B) A backup queue
- C) A monitoring queue
- D) A queue for messages that couldn't be processed after max retries

**Answer: D**
The DLQ stores messages that failed processing after exceeding MaxDeliveryCount, allowing for investigation and manual handling.
---
## Question 5
How can you ensure message processing is exactly-once?


- A) Set a special flag
- B) Use Sessions and implement idempotent operations
- C) Use Premium tier
- D) It's guaranteed automatically

**Answer: B**
While Service Bus provides at-least-once delivery, exact-once requires sessions (for ordering) and idempotent function logic.
---
## Question 6
What is the PeekLock mode in Service Bus?


- A) Messages are deleted immediately
- B) Messages are locked temporarily; deleted only after successful processing
- C) Messages are permanently locked
- D) Messages cannot be read

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
- B) Based on time of day
- C) Automatically, with instances based on queue/subscription depth
- D) Manually only

**Answer: C**
The Functions runtime scales based on queue length and message processing throughput using target-based scaling.
---
## Question 9
Can you send a message to a Service Bus queue from an Azure Function?


- A) Only in Premium plan
- B) Yes, using output bindings
- C) No
- D) Only with custom code

**Answer: B**
Service Bus output bindings allow functions to send messages to queues or topics declaratively.
---
## Question 10
What is the maximum message size for Service Bus Standard tier?


- A) 100 MB
- B) 64 KB
- C) 256 KB
- D) 1 MB

**Answer: C**
Standard tier supports up to 256 KB per message. Premium tier supports up to 1 MB (or 100 MB with large message support).