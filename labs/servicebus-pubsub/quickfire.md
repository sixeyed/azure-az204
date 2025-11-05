# Service Bus Topics and Subscriptions - Quickfire Questions

## Question 1
What is a Service Bus topic?

- A) A conversation subject
- B) A publish-subscribe messaging entity allowing multiple independent subscriptions
- C) A queue type
- D) A database table

**Answer: B**
Topics enable pub-sub patterns: publishers send to topic, multiple subscribers receive copies via subscriptions.

---

## Question 2
What is a subscription in Service Bus?

- A) A billing plan
- B) An independent receiver endpoint that receives copies of messages from a topic
- C) A security group
- D) A network connection

**Answer: B**
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
- B) Rules determining which messages a subscription receives from a topic
- C) Security filters
- D) Network filters

**Answer: B**
Filters (Boolean, SQL, Correlation) allow subscriptions to receive only messages matching specific criteria.

---

## Question 5
What filter types are available?

- A) Only one type
- B) Boolean (true/false), SQL (expression-based), Correlation (property matching)
- C) Regex only
- D) No filters

**Answer: B**
Boolean filters (TrueFilter/FalseFilter), SQL filters (WHERE-like expressions), Correlation filters (efficient property matching).

---

## Question 6
What is a TrueFilter?

- A) Security validation
- B) Default filter that accepts all messages from the topic
- C) Encryption filter
- D) Authentication filter

**Answer: B**
TrueFilter is the default - subscriptions receive all topic messages unless a different filter is applied.

---

## Question 7
What are subscription actions?

- A) Message deletion
- B) Operations that modify message properties when filter matches
- C) Sending notifications
- D) Creating backups

**Answer: B**
Actions can add, remove, or update message properties when a filter matches, useful for routing metadata.

---

## Question 8
When should you use topics vs. queues?

- A) Always use queues
- B) Use topics for pub-sub with multiple independent consumers; queues for point-to-point
- C) Always use topics
- D) They're identical

**Answer: B**
Topics for broadcasting to multiple subscribers (one-to-many). Queues for single consumer or competing consumers (one-to-one).

---

## Question 9
Do subscriptions have their own dead-letter queues?

- A) No DLQ for subscriptions
- B) Yes, each subscription has its own DLQ
- C) Only topics have DLQ
- D) Shared DLQ for all subscriptions

**Answer: B**
Each subscription maintains its own dead-letter queue for failed messages specific to that subscription.

---

## Question 10
Can the same message go to multiple subscriptions?

- A) No, exclusive delivery
- B) Yes, each matching subscription receives a copy of the message
- C) Only with manual routing
- D) Maximum 2 subscriptions

**Answer: B**
Messages are independently copied to all subscriptions whose filters match, enabling true pub-sub.
