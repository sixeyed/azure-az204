# Durable Functions - Fan-Out/Fan-In Pattern - Quickfire Questions

## Question 1
What is the fan-out/fan-in pattern?


- A) Sequential execution of functions
- B) Load balancing
- C) Executing multiple functions in parallel, then aggregating results
- D) Duplicating functions

**Answer: C**
Fan-out executes multiple activity functions in parallel; fan-in waits for all to complete and aggregates their results.
---
## Question 2
What Durable Functions API is used to execute activities in parallel?


- A) context.CallActivityAsync called multiple times
- B) Task.WhenAll with multiple CallActivityAsync calls
- C) Parallel.ForEach
- D) context.Parallel

**Answer: B**
You create multiple Task objects using CallActivityAsync and use Task.WhenAll to wait for all parallel executions to complete.
---
## Question 3
What are the benefits of the fan-out/fan-in pattern?


- A) Parallel processing for improved performance and throughput
- B) Reduced cost only
- C) Simpler code
- D) Better security

**Answer: A**
Fan-out/fan-in enables parallel processing of independent tasks, significantly reducing total execution time.
---
## Question 4
How many activity functions can you fan-out to?


- A) Only 2
- B) Maximum 100
- C) Hundreds or thousands, limited by platform quotas and resources
- D) Maximum 10

**Answer: C**
Durable Functions can fan-out to many activity instances (hundreds or thousands), limited by platform quotas and app configuration.
---
## Question 5
What happens if one activity fails in a fan-out scenario?


- A) Failed activity is ignored
- B) Entire Function App crashes
- C) All activities are cancelled
- D) Task.WhenAll throws, and the orchestrator can handle the exception

**Answer: D**
If any activity fails, Task.WhenAll throws an exception. The orchestrator can catch and handle it (retry, compensate, etc.).
---
## Question 6
Can you process batches of items using fan-out/fan-in?


- A) No, only single items
- B) Only in Premium plan
- C) Yes, iterate over collection and fan-out an activity for each item
- D) Requires custom code

**Answer: C**
A common pattern is iterating over a collection and fanning-out an activity function for each item to process them in parallel.
---
## Question 7
How do you aggregate results in the fan-in phase?


- A) Results are automatically merged
- B) Collect the Task results from Task.WhenAll and process them
- C) Results are lost
- D) Use a database

**Answer: B**
After Task.WhenAll completes, you access the Result property of each task to collect and aggregate all results.
---
## Question 8
What is the difference between fan-out/fan-in and function chaining?


- A) Fan-out is only for databases
- B) No difference
- C) Chaining is faster
- D) Fan-out/fan-in runs activities in parallel; chaining runs them sequentially

**Answer: D**
Chaining executes functions one after another (sequential), while fan-out/fan-in executes multiple functions simultaneously (parallel).
---
## Question 9
Can you combine fan-out/fan-in with other patterns?


- A) Yes, patterns can be combined (e.g., chain of fan-out operations)
- B) Only with custom code
- C) Only in Enterprise tier
- D) No, mutually exclusive

**Answer: A**
Durable Function patterns can be combined. For example, you can chain multiple fan-out/fan-in operations or fan-out to other orchestrators.
---
## Question 10
What is sub-orchestration in Durable Functions?


- A) A testing mode
- B) A billing tier
- C) An orchestrator calling other orchestrator functions for composition
- D) A monitoring feature

**Answer: C**
Sub-orchestration allows orchestrator functions to call other orchestrators, enabling complex workflow composition and reuse.