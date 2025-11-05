# Azure Functions Blob Trigger - Quickfire Questions

## Question 1
What triggers a blob-triggered Azure Function to execute?

- A) When a blob is deleted
- B) When a blob is created or updated in a specified container
- C) On a schedule
- D) When a database changes

**Answer: B**
Blob triggers execute when a new blob is created or an existing blob is updated in the monitored container.

---

## Question 2
Which storage account feature is required for blob triggers to work?

- A) Azure Files
- B) Table Storage
- C) Queue Storage (for poison message handling)
- D) Static website hosting

**Answer: C**
Blob triggers use Azure Queue Storage internally to ensure reliable triggering and tracking of processed blobs.

---

## Question 3
What is a poison blob in the context of blob triggers?

- A) A corrupted storage account
- B) A blob that causes a function to fail repeatedly
- C) A blob larger than 100MB
- D) An encrypted blob

**Answer: B**
A poison blob is one that causes the function to fail repeatedly. After max retries, it's moved to a poison queue for manual handling.

---

## Question 4
How can you access the blob content in a blob-triggered function?

- A) Via the Stream parameter
- B) Via the BlobClient
- C) Via byte array
- D) All of the above

**Answer: D**
You can bind to Stream, byte[], string, BlobClient, or other types depending on how you want to process the blob.

---

## Question 5
What is the blob path pattern syntax for triggering on specific blobs?

- A) container/{name}
- B) {container}/{name}.{extension}
- C) container/{name}.{ext}
- D) Both A and C

**Answer: D**
Common patterns: "container/{name}" (all blobs) or "container/{name}.{ext}" (specific extensions). You can extract parts to binding data.

---

## Question 6
What happens if your blob-triggered function fails?

- A) The blob is deleted
- B) The function is retried automatically (up to 5 times by default)
- C) The trigger stops working
- D) Nothing, errors are ignored

**Answer: B**
Functions runtime automatically retries failed executions. After max retries, the message goes to a poison queue.

---

## Question 7
How can blob triggers impact cost?

- A) No impact
- B) Polling storage can incur transaction costs
- C) Each trigger costs $1
- D) Blob triggers are not metered

**Answer: B**
Blob triggers poll storage accounts for changes, which incurs storage transaction costs. Event Grid triggers are an alternative for lower cost.

---

## Question 8
What is the alternative to blob triggers for event-driven blob processing?

- A) Timer triggers
- B) Event Grid triggers
- C) HTTP triggers
- D) Queue triggers

**Answer: B**
Event Grid triggers react to blob events with lower latency and cost compared to polling-based blob triggers.

---

## Question 9
Can blob triggers process multiple blobs in parallel?

- A) No, always sequential
- B) Yes, Functions scales out to process multiple blobs concurrently
- C) Only in Premium plan
- D) Only for small blobs

**Answer: B**
Azure Functions automatically scales out to process multiple blob events in parallel across multiple instances.

---

## Question 10
What metadata is available in a blob-triggered function?

- A) Blob name and URI
- B) Size and content type
- C) Last modified date
- D) All of the above

**Answer: D**
Blob metadata including name, URI, size, content type, and timestamps are available through binding expressions or BlobProperties.
