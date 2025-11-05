# Service Bus Topics and Subscriptions - Quickfire Questions

## Question 1
What is a Service Bus topic?


- A) A conversation subject
- B) A database table
- C) A publish-subscribe messaging entity allowing multiple independent subscriptions
- D) A queue type

**Answer: C**
Topics enable pub-sub patterns: publishers send to topic, multiple subscribers receive copies via subscriptions.
---
## Question 2
What is a subscription in Service Bus?


- A) A billing plan
- B) A network connection
- C) An independent receiver endpoint that receives copies of messages from a topic
- D) A security group

**Answer: C**
Subscriptions are virtual queues that receive messages from topics, enabling multiple consumers with independent consumption.
---
## Question 3
How many subscriptions can a topic have?


- A) Only 1
- B) Up to 2,000 per topic
- C) Unlimited
- D) Maximum 10

**Answer: B**
Topics support up to 2,000 subscriptions, each acting as an independent receiver.
---
## Question 4
What are subscription filters?


- A) Spam filters
- B) Security filters
- C) Rules determining which messages a subscription receives from a topic
- D) Network filters

**Answer: C**
Filters (Boolean, SQL, Correlation) allow subscriptions to receive only messages matching specific criteria.
---
## Question 5
What filter types are available?


- A) Boolean (true/false), SQL (expression-based), Correlation (property matching)
- B) Only one type
- C) Regex only
- D) No filters

**Answer: A**
Boolean filters (TrueFilter/FalseFilter), SQL filters (WHERE-like expressions), Correlation filters (efficient property matching).
---
## Question 6
What is a TrueFilter?


- A) Security validation
- B) Default filter that accepts all messages from the topic
- C) Authentication filter
- D) Encryption filter

**Answer: B**
TrueFilter is the default - subscriptions receive all topic messages unless a different filter is applied.
---
## Question 7
What are subscription actions?


- A) Creating backups
- B) Message deletion
- C) Operations that modify message properties when filter matches
- D) Sending notifications

**Answer: C**
Actions can add, remove, or update message properties when a filter matches, useful for routing metadata.
---
## Question 8
When should you use topics vs. queues?


- A) Always use topics
- B) Use topics for pub-sub with multiple independent consumers; queues for point-to-point
- C) They're identical
- D) Always use queues

**Answer: B**
Topics for broadcasting to multiple subscribers (one-to-many). Queues for single consumer or competing consumers (one-to-one).
---
## Question 9
Do subscriptions have their own dead-letter queues?


- A) Shared DLQ for all subscriptions
- B) Only topics have DLQ
- C) Yes, each subscription has its own DLQ
- D) No DLQ for subscriptions

**Answer: C**
Each subscription maintains its own dead-letter queue for failed messages specific to that subscription.
---
## Question 10
Can the same message go to multiple subscriptions?


- A) Maximum 2 subscriptions
- B) Only with manual routing
- C) No, exclusive delivery
- D) Yes, each matching subscription receives a copy of the message

**Answer: D**
Messages are independently copied to all subscriptions whose filters match, enabling true pub-sub.