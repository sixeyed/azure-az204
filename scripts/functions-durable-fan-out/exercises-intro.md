# Durable Functions - Fan-Out/Fan-In Pattern - Exercises Introduction

We've covered the fan-out/fan-in pattern for executing multiple activities in parallel and aggregating results. Now let's build a quote engine that dramatically reduces processing time.

## What You'll Do

You'll **explore the code structure** - an HTTP trigger that starts the orchestration, a quote orchestrator that coordinates parallel work using `Task.WhenAll`, and three supplier activity functions that simulate getting price quotes. Each supplier takes 10 seconds to respond, so sequential execution would take 30 seconds. But with fan-out, all three run simultaneously and complete in about 10 seconds!

You'll **run locally using Azurite emulator** for durable state storage. Then you'll **trigger orchestrations via HTTP** and observe parallel execution in the logs. You'll see all three suppliers called at the same time, their results collected, and the best price selected.

The orchestrator returns **HTTP management URLs** for tracking long-running operations. You'll use the **statusQueryGetUri** to check orchestration status, seeing it progress from "Running" to "Completed" with the final result. This is the standard pattern for async HTTP APIs - start an operation, return immediately with status URLs, client polls for completion.

After **deployment to Azure**, you'll **monitor through the portal**, seeing the orchestration timeline that shows parallel execution visually. The **challenge** asks you to compare fan-out to event-driven pub-sub patterns - when should you use orchestrated parallel execution versus independent event processing?

The key insight: fan-out/fan-in is perfect when you need to **aggregate results from parallel operations**. If operations are independent and don't need aggregation, event-driven pub-sub (Event Grid, Service Bus) is simpler.

Let's implement parallel aggregation!
