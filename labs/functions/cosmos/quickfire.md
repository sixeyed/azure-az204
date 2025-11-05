# Azure Functions Cosmos DB - Quickfire Questions

## Question 1
What triggers a Cosmos DB-triggered Azure Function?


- A) When documents are inserted or updated (via Change Feed)
- B) When the database is scaled
- C) On a schedule
- D) When documents are read

**Answer: A**
Cosmos DB triggers use the Change Feed to detect document inserts and updates, triggering the function for each change.
---
## Question 2
What is the Cosmos DB Change Feed?


- A) A monitoring tool
- B) A pricing model
- C) A persistent log of changes to documents in order they occurred
- D) A backup feature

**Answer: C**
The Change Feed is a persistent record of changes (inserts/updates) to a Cosmos DB container, processed in order.
---
## Question 3
Does the Cosmos DB trigger fire for document deletions?


- A) No, Change Feed doesn't capture deletes
- B) Only in SQL API
- C) Only with special configuration
- D) Yes, always

**Answer: A**
The Change Feed doesn't include deletes. You need to use soft-delete patterns (marking documents as deleted) to capture deletions.
---
## Question 4
What is a lease container in Cosmos DB triggers?


- A) A temporary storage container
- B) A backup container
- C) A billing container
- D) A container that stores checkpoints to track Change Feed progress

**Answer: D**
The lease container stores progress checkpoints, allowing the trigger to resume from where it left off and coordinate across instances.
---
## Question 5
How does the Cosmos DB trigger scale across multiple function instances?


- A) Using partition-based distribution via the lease container
- B) Manual configuration required
- C) It doesn't scale
- D) Round-robin distribution

**Answer: A**
The trigger uses leases to distribute partitions across function instances, allowing parallel processing.
---
## Question 6
What binding direction is used for Cosmos DB output bindings?


- A) Out
- B) In
- C) Both In and Out
- D) InOut

**Answer: A**
Output bindings use direction="out" to write documents to Cosmos DB after function execution.
---
## Question 7
Can you process changes from multiple containers with one function?


- A) Only in Premium plan
- B) Yes, specify multiple containers in the trigger
- C) Only with custom code
- D) No, one trigger per container

**Answer: D**
Each Cosmos DB trigger monitors a single container. Use multiple functions or custom code for multiple containers.
---
## Question 8
What happens if the Change Feed processing falls behind?


- A) Cosmos DB resets
- B) The trigger queues changes and processes them as capacity allows
- C) The function stops
- D) Old changes are dropped

**Answer: B**
Changes accumulate in the Change Feed and are processed as function instances scale to handle the load.
---
## Question 9
Which Cosmos DB APIs support the Change Feed?


- A) Only Table API
- B) Only SQL API
- C) All Cosmos DB APIs
- D) SQL API and MongoDB API

**Answer: D**
Change Feed is primarily supported in SQL API and MongoDB API (version 3.6+). Other APIs have limited or no support.
---
## Question 10
How can you initialize the Change Feed to process historical data?


- A) Not possible, only new changes
- B) Set StartFromBeginning to true in trigger configuration
- C) Use a different trigger type
- D) Manually read all documents

**Answer: B**
Setting StartFromBeginning=true processes all existing documents. By default, it only processes changes after the trigger starts.