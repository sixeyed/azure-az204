# Event Hubs Consumers - Quickfire Questions

## Question 1
What is a checkpoint in Event Hubs?

- A) Security validation
- B) Marker indicating the last successfully processed event position in a partition
- C) Network checkpoint
- D) Billing checkpoint

**Answer: B**
Checkpoints track consumer progress, enabling resume from last processed position after restarts or failures.

---

## Question 2
Where are checkpoints typically stored?

- A) In memory only
- B) Azure Blob Storage or Table Storage
- C) Event Hub itself
- D) Consumer application only

**Answer: B**
Checkpoints are typically persisted to Azure Blob Storage, allowing recovery and coordination across instances.

---

## Question 3
What is the Event Processor Client?

- A) A monitoring tool
- B) High-level client that manages partition distribution, checkpointing, and load balancing
- C) A database client
- D) A security client

**Answer: B**
Event Processor Client (formerly Event Processor Host) simplifies consumption with automatic partition distribution and checkpoint management.

---

## Question 4
How does Event Processor Client distribute partitions?

- A) Manually configured
- B) Automatically balances partition ownership across available consumer instances
- C) Random assignment
- D) Fixed assignment

**Answer: B**
Event Processor Client uses blob leases to coordinate partition ownership, distributing partitions evenly across instances.

---

## Question 5
What happens when a new consumer instance starts?

- A) Nothing
- B) Event Processor Client rebalances partitions across all instances
- C) All consumers restart
- D) Events are lost

**Answer: B**
The partition manager detects new instances and rebalances partition assignments for even distribution.

---

## Question 6
What is the offset in Event Hubs?

- A) Time zone difference
- B) Position/sequence number of an event within a partition
- C) Price discount
- D) Network latency

**Answer: B**
Each event has a sequence number (offset) indicating its position in the partition's ordered stream.

---

## Question 7
Can you start reading from a specific point in time?

- A) No, always from beginning
- B) Yes, using enqueuedTime to start from a specific timestamp
- C) Only from latest
- D) Random access only

**Answer: B**
Consumers can start from beginning, latest, specific offset, or specific enqueued time.

---

## Question 8
What is the lease in partition management?

- A) Contract document
- B) Blob-based lock indicating which consumer instance owns a partition
- C) Storage rental
- D) Network lease

**Answer: B**
Leases are blob locks that coordinate partition ownership, preventing multiple instances from processing the same partition.

---

## Question 9
How often should checkpoints be created?

- A) After every event
- B) Periodically (e.g., every N events or time interval) balancing durability and performance
- C) Never
- D) Only on shutdown

**Answer: B**
Frequent checkpointing ensures durability but impacts performance. Balance based on acceptable reprocessing window.

---

## Question 10
What is epoch in Event Hubs consumers?

- A) Time period
- B) Value determining receiver priority; higher epoch receivers supersede lower ones
- C) Version number
- D) Partition count

**Answer: B**
Epoch enables exclusive receivers: higher epoch value disconnects lower epoch receivers on the same partition.
