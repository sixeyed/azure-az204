# Event Hubs Consumers - Quickfire Questions

## Question 1
What is a checkpoint in Event Hubs?


- A) Network checkpoint
- B) Billing checkpoint
- C) Marker indicating the last successfully processed event position in a partition
- D) Security validation

**Answer: C**
Checkpoints track consumer progress, enabling resume from last processed position after restarts or failures.
---
## Question 2
Where are checkpoints typically stored?


- A) Event Hub itself
- B) Consumer application only
- C) In memory only
- D) Azure Blob Storage or Table Storage

**Answer: D**
Checkpoints are typically persisted to Azure Blob Storage, allowing recovery and coordination across instances.
---
## Question 3
What is the Event Processor Client?


- A) A database client
- B) A monitoring tool
- C) A security client
- D) High-level client that manages partition distribution, checkpointing, and load balancing

**Answer: D**
Event Processor Client (formerly Event Processor Host) simplifies consumption with automatic partition distribution and checkpoint management.
---
## Question 4
How does Event Processor Client distribute partitions?


- A) Random assignment
- B) Manually configured
- C) Automatically balances partition ownership across available consumer instances
- D) Fixed assignment

**Answer: C**
Event Processor Client uses blob leases to coordinate partition ownership, distributing partitions evenly across instances.
---
## Question 5
What happens when a new consumer instance starts?


- A) All consumers restart
- B) Event Processor Client rebalances partitions across all instances
- C) Events are lost
- D) Nothing

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


- A) Only from latest
- B) Random access only
- C) No, always from beginning
- D) Yes, using enqueuedTime to start from a specific timestamp

**Answer: D**
Consumers can start from beginning, latest, specific offset, or specific enqueued time.
---
## Question 8
What is the lease in partition management?


- A) Storage rental
- B) Network lease
- C) Contract document
- D) Blob-based lock indicating which consumer instance owns a partition

**Answer: D**
Leases are blob locks that coordinate partition ownership, preventing multiple instances from processing the same partition.
---
## Question 9
How often should checkpoints be created?


- A) After every event
- B) Periodically (e.g., every N events or time interval) balancing durability and performance
- C) Only on shutdown
- D) Never

**Answer: B**
Frequent checkpointing ensures durability but impacts performance. Balance based on acceptable reprocessing window.
---
## Question 10
What is epoch in Event Hubs consumers?


- A) Partition count
- B) Time period
- C) Version number
- D) Value determining receiver priority; higher epoch receivers supersede lower ones

**Answer: D**
Epoch enables exclusive receivers: higher epoch value disconnects lower epoch receivers on the same partition.