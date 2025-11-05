# Durable Functions - Chained Pattern - Exercises Introduction

We've covered the chained pattern where orchestrators coordinate multiple activity functions to execute sequentially with outputs passed between steps. Now let's build a health monitoring system demonstrating this pattern.

## What You'll Do

You'll start by **examining the code structure** - a trigger that starts the orchestration, an orchestrator function that coordinates the sequence, and three activity functions that execute in order. The orchestrator calls each activity and passes the output of one as input to the next, creating a chain of processing.

Then you'll **set up local development** with Azure Storage Emulator (for durable state persistence) and Service Bus (for notifications). You'll **test locally using func start**, triggering the health check orchestration and watching as it executes three sequential steps: writing health data to blob storage, sending a notification to Service Bus queue, and logging the event to table storage.

After deployment to Azure, you'll **verify the orchestration** through monitoring logs showing the exact sequence of execution. You'll **inspect the created artifacts** - the blob with health data, the Service Bus message with notification details, and the table entry with the log record. Each step waited for the previous one to complete before executing.

The key learning: durable functions handle all the state management automatically. The orchestrator looks like simple sequential code (`var blob = await WriteBlob(); var message = await SendMessage(blob); await LogEvent(message);`), but behind the scenes, Durable Functions is persisting state, handling retries, and coordinating execution across potentially multiple servers.

Let's implement the chained pattern!
