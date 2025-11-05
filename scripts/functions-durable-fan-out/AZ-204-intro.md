# Durable Functions - Fan-Out/Fan-In Pattern - AZ-204 Exam Introduction

Excellent work with parallel orchestration! The fan-out/fan-in pattern is heavily tested on the AZ-204 for scenarios requiring parallel aggregation.

## What We'll Cover

**Distinguishing between all five patterns** with specific focus on fan-out/fan-in. This pattern uses `Task.WhenAll` to call multiple activities in parallel, waits for all to complete, then aggregates results. Key difference from chained pattern: operations execute simultaneously, not sequentially. The exam tests recognizing when parallel execution with aggregation is needed.

**Task.WhenAll for parallel execution** is the core technique. Create multiple tasks by calling activities, pass the array to `Task.WhenAll`, await completion. All activities execute in parallel, total time equals the slowest operation. The exam tests understanding that `Task.WhenAll` doesn't execute sequentially like multiple awaits would.

**HTTP management APIs** return status URLs for tracking orchestrations. statusQueryGetUri for checking status, sendEventPostUri for sending events, terminatePostUri for cancellation, purgeHistoryDeleteUri for cleanup. The exam tests which URL to use for different operations and understanding the HTTP-based management pattern.

**Performance benefits** are dramatic. 10 parallel operations that each take 10 seconds complete in 10 seconds total (not 100 seconds). This pattern is essential for scenarios like calling multiple external APIs, processing multiple files, or aggregating data from multiple sources. The exam tests calculating execution time and recognizing performance optimization opportunities.

**Retry policies for resilience** in parallel operations need independent configuration. Each activity can have its own retry policy. The exam tests configuring retries for fan-out scenarios where some operations may fail but others should continue.

**Comparing to Logic Apps** helps understand when to use each. Durable Functions: code-first approach, better for complex logic, runs in Azure Functions (consumption or premium). Logic Apps: visual designer, better for simple workflows, many connectors. The exam tests choosing the right tool.

We'll cover **scaling considerations** (fan-out creates many simultaneous executions), **cost implications**, **common anti-patterns** (fanning out to thousands of activities), and **scenarios** about parallel data processing, aggregating external API calls, and implementing map-reduce patterns.

Master parallel orchestration for the AZ-204!
