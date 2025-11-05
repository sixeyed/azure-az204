# Azure Event Hubs - Quickfire Questions

## Question 1
What is Azure Event Hubs?


- A) A big data streaming platform and event ingestion service
- B) A monitoring service
- C) A queue service
- D) A database

**Answer: A**
Event Hubs is designed for high-throughput event streaming, ingesting millions of events per second for big data scenarios.
---
## Question 2
What is the difference between Event Hubs and Service Bus?


- A) Event Hubs is slower
- B) Service Bus doesn't support messages
- C) Event Hubs for high-volume streaming/telemetry; Service Bus for transactional messaging
- D) No difference

**Answer: C**
Event Hubs: massive scale, streaming, retain events. Service Bus: enterprise messaging, queues/topics, transactions.
---
## Question 3
What is a partition in Event Hubs?


- A) Storage division
- B) Security boundary
- C) Ordered sequence of events; mechanism for parallel processing and scaling
- D) Network segment

**Answer: C**
Partitions are ordered logs of events. Multiple partitions enable parallel consumption and horizontal scaling.
---
## Question 4
What is a partition key?


- A) Access key
- B) Primary key
- C) Value determining which partition an event is sent to for ordering
- D) Encryption key

**Answer: C**
Events with the same partition key go to the same partition, ensuring order. Without it, round-robin distribution occurs.
---
## Question 5
How many partitions can an Event Hub have?


- A) Unlimited
- B) Fixed at 10
- C) Only 1
- D) 1 to 32 (Standard), up to 100+ (Dedicated/Premium)

**Answer: D**
Standard tier: 1-32 partitions. Premium/Dedicated: more partitions available for higher throughput needs.
---
## Question 6
What is a consumer group?


- A) Billing group
- B) User group
- C) Independent view of the event stream allowing multiple applications to read independently
- D) Security group

**Answer: C**
Consumer groups enable multiple consumers to read the same stream independently, each maintaining their own offset/checkpoint.
---
## Question 7
How long does Event Hubs retain events?


- A) Forever
- B) Until consumed
- C) 1-90 days (Standard), up to 90 days (Premium), indefinite with Capture to storage
- D) 1 hour only

**Answer: C**
Standard: 1-7 days retention. Premium: up to 90 days. Event Hubs Capture can archive to storage indefinitely.
---
## Question 8
What is Event Hubs Capture?


- A) Monitoring feature
- B) Automatic archiving of streaming data to Blob Storage or Data Lake
- C) Screenshot feature
- D) Manual backup

**Answer: B**
Capture automatically streams events to Azure Blob Storage or Data Lake in Avro format without code.
---
## Question 9
What are Throughput Units (TUs)?


- A) Network bandwidth
- B) CPU cores
- C) Storage units
- D) Pre-purchased capacity units (1 TU = 1 MB/s ingress, 2 MB/s egress)

**Answer: D**
TUs control throughput capacity. Standard tier uses TUs; Premium uses Processing Units (PUs) with better isolation.
---
## Question 10
What protocol does Event Hubs use?


- A) FTP
- B) SMTP
- C) HTTP only
- D) AMQP, Kafka, HTTPS

**Answer: D**
Event Hubs supports AMQP 1.0, Apache Kafka protocol, and HTTPS, enabling diverse client ecosystems.