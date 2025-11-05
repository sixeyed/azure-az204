# Azure Functions Cosmos DB - Quickfire Questions

## Question 1
What triggers a Cosmos DB-triggered Azure Function?

- A) When documents are read
- B) When documents are inserted or updated (via Change Feed)
- C) When the database is scaled
- D) On a schedule

**Answer: B**
Cosmos DB triggers use the Change Feed to detect document inserts and updates, triggering the function for each change.

---

## Question 2
What is the Cosmos DB Change Feed?

- A) A pricing model
- B) A persistent log of changes to documents in order they occurred
- C) A backup feature
- D) A monitoring tool

**Answer: B**
The Change Feed is a persistent record of changes (inserts/updates) to a Cosmos DB container, processed in order.

---

## Question 3
Does the Cosmos DB trigger fire for document deletions?

- A) Yes, always
- B) No, Change Feed doesn't capture deletes
- C) Only in SQL API
- D) Only with special configuration

**Answer: B**
The Change Feed doesn't include deletes. You need to use soft-delete patterns (marking documents as deleted) to capture deletions.

---

## Question 4
What is a lease container in Cosmos DB triggers?

- A) A billing container
- B) A container that stores checkpoints to track Change Feed progress
- C) A backup container
- D) A temporary storage container

**Answer: B**
The lease container stores progress checkpoints, allowing the trigger to resume from where it left off and coordinate across instances.

---

## Question 5
How does the Cosmos DB trigger scale across multiple function instances?

- A) It doesn't scale
- B) Using partition-based distribution via the lease container
- C) Round-robin distribution
- D) Manual configuration required

**Answer: B**
The trigger uses leases to distribute partitions across function instances, allowing parallel processing.

---

## Question 6
What binding direction is used for Cosmos DB output bindings?

- A) In
- B) Out
- C) InOut
- D) Both In and Out

**Answer: B**
Output bindings use direction="out" to write documents to Cosmos DB after function execution.

---

## Question 7
Can you process changes from multiple containers with one function?

- A) Yes, specify multiple containers in the trigger
- B) No, one trigger per container
- C) Only in Premium plan
- D) Only with custom code

**Answer: B**
Each Cosmos DB trigger monitors a single container. Use multiple functions or custom code for multiple containers.

---

## Question 8
What happens if the Change Feed processing falls behind?

- A) Old changes are dropped
- B) The trigger queues changes and processes them as capacity allows
- C) The function stops
- D) Cosmos DB resets

**Answer: B**
Changes accumulate in the Change Feed and are processed as function instances scale to handle the load.

---

## Question 9
Which Cosmos DB APIs support the Change Feed?

- A) Only SQL API
- B) SQL API and MongoDB API
- C) All Cosmos DB APIs
- D) Only Table API

**Answer: B**
Change Feed is primarily supported in SQL API and MongoDB API (version 3.6+). Other APIs have limited or no support.

---

## Question 10
How can you initialize the Change Feed to process historical data?

- A) Not possible, only new changes
- B) Set StartFromBeginning to true in trigger configuration
- C) Manually read all documents
- D) Use a different trigger type

**Answer: B**
Setting StartFromBeginning=true processes all existing documents. By default, it only processes changes after the trigger starts.
