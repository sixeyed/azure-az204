# Azure Event Hubs - Quickfire Questions

## Question 1
What is Azure Event Hubs?

- A) A queue service
- B) A big data streaming platform and event ingestion service
- C) A database
- D) A monitoring service

**Answer: B**
Event Hubs is designed for high-throughput event streaming, ingesting millions of events per second for big data scenarios.

---

## Question 2
What is the difference between Event Hubs and Service Bus?

- A) No difference
- B) Event Hubs for high-volume streaming/telemetry; Service Bus for transactional messaging
- C) Event Hubs is slower
- D) Service Bus doesn't support messages

**Answer: B**
Event Hubs: massive scale, streaming, retain events. Service Bus: enterprise messaging, queues/topics, transactions.

---

## Question 3
What is a partition in Event Hubs?

- A) Storage division
- B) Ordered sequence of events; mechanism for parallel processing and scaling
- C) Security boundary
- D) Network segment

**Answer: B**
Partitions are ordered logs of events. Multiple partitions enable parallel consumption and horizontal scaling.

---

## Question 4
What is a partition key?

- A) Encryption key
- B) Value determining which partition an event is sent to for ordering
- C) Primary key
- D) Access key

**Answer: B**
Events with the same partition key go to the same partition, ensuring order. Without it, round-robin distribution occurs.

---

## Question 5
How many partitions can an Event Hub have?

- A) Only 1
- B) 1 to 32 (Standard), up to 100+ (Dedicated/Premium)
- C) Unlimited
- D) Fixed at 10

**Answer: B**
Standard tier: 1-32 partitions. Premium/Dedicated: more partitions available for higher throughput needs.

---

## Question 6
What is a consumer group?

- A) User group
- B) Independent view of the event stream allowing multiple applications to read independently
- C) Security group
- D) Billing group

**Answer: B**
Consumer groups enable multiple consumers to read the same stream independently, each maintaining their own offset/checkpoint.

---

## Question 7
How long does Event Hubs retain events?

- A) Forever
- B) 1-90 days (Standard), up to 90 days (Premium), indefinite with Capture to storage
- C) 1 hour only
- D) Until consumed

**Answer: B**
Standard: 1-7 days retention. Premium: up to 90 days. Event Hubs Capture can archive to storage indefinitely.

---

## Question 8
What is Event Hubs Capture?

- A) Screenshot feature
- B) Automatic archiving of streaming data to Blob Storage or Data Lake
- C) Manual backup
- D) Monitoring feature

**Answer: B**
Capture automatically streams events to Azure Blob Storage or Data Lake in Avro format without code.

---

## Question 9
What are Throughput Units (TUs)?

- A) Storage units
- B) Pre-purchased capacity units (1 TU = 1 MB/s ingress, 2 MB/s egress)
- C) CPU cores
- D) Network bandwidth

**Answer: B**
TUs control throughput capacity. Standard tier uses TUs; Premium uses Processing Units (PUs) with better isolation.

---

## Question 10
What protocol does Event Hubs use?

- A) HTTP only
- B) AMQP, Kafka, HTTPS
- C) FTP
- D) SMTP

**Answer: B**
Event Hubs supports AMQP 1.0, Apache Kafka protocol, and HTTPS, enabling diverse client ecosystems.
