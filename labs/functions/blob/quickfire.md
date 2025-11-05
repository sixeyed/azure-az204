# Azure Functions Blob Trigger - Quickfire Questions

## Question 1
What triggers a blob-triggered Azure Function to execute?


- A) On a schedule
- B) When a database changes
- C) When a blob is deleted
- D) When a blob is created or updated in a specified container

**Answer: D**
Blob triggers execute when a new blob is created or an existing blob is updated in the monitored container.
---
## Question 2
Which storage account feature is required for blob triggers to work?


- A) Static website hosting
- B) Azure Files
- C) Queue Storage (for poison message handling)
- D) Table Storage

**Answer: C**
Blob triggers use Azure Queue Storage internally to ensure reliable triggering and tracking of processed blobs.
---
## Question 3
What is a poison blob in the context of blob triggers?


- A) A blob larger than 100MB
- B) An encrypted blob
- C) A corrupted storage account
- D) A blob that causes a function to fail repeatedly

**Answer: D**
A poison blob is one that causes the function to fail repeatedly. After max retries, it's moved to a poison queue for manual handling.
---
## Question 4
How can you access the blob content in a blob-triggered function?


- A) Via the BlobClient
- B) Via the Stream parameter
- C) Via byte array
- D) All of the above

**Answer: D**
You can bind to Stream, byte[], string, BlobClient, or other types depending on how you want to process the blob.
---
## Question 5
What is the blob path pattern syntax for triggering on specific blobs?


- A) container/{name}.{ext}
- B) container/{name}
- C) {container}/{name}.{extension}
- D) Both A and C

**Answer: D**
Common patterns: "container/{name}" (all blobs) or "container/{name}.{ext}" (specific extensions). You can extract parts to binding data.
---
## Question 6
What happens if your blob-triggered function fails?


- A) The trigger stops working
- B) The function is retried automatically (up to 5 times by default)
- C) Nothing, errors are ignored
- D) The blob is deleted

**Answer: B**
Functions runtime automatically retries failed executions. After max retries, the message goes to a poison queue.
---
## Question 7
How can blob triggers impact cost?


- A) No impact
- B) Polling storage can incur transaction costs
- C) Blob triggers are not metered
- D) Each trigger costs $1

**Answer: B**
Blob triggers poll storage accounts for changes, which incurs storage transaction costs. Event Grid triggers are an alternative for lower cost.
---
## Question 8
What is the alternative to blob triggers for event-driven blob processing?


- A) Queue triggers
- B) HTTP triggers
- C) Timer triggers
- D) Event Grid triggers

**Answer: D**
Event Grid triggers react to blob events with lower latency and cost compared to polling-based blob triggers.
---
## Question 9
Can blob triggers process multiple blobs in parallel?


- A) No, always sequential
- B) Only for small blobs
- C) Yes, Functions scales out to process multiple blobs concurrently
- D) Only in Premium plan

**Answer: C**
Azure Functions automatically scales out to process multiple blob events in parallel across multiple instances.
---
## Question 10
What metadata is available in a blob-triggered function?


- A) Size and content type
- B) All of the above
- C) Blob name and URI
- D) Last modified date

**Answer: B**
Blob metadata including name, URI, size, content type, and timestamps are available through binding expressions or BlobProperties.