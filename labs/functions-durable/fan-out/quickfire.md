# Durable Functions - Fan-Out/Fan-In Pattern - Quickfire Questions

## Question 1
What is the fan-out/fan-in pattern?

- A) Sequential execution of functions
- B) Executing multiple functions in parallel, then aggregating results
- C) Duplicating functions
- D) Load balancing

**Answer: B**
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

- A) Reduced cost only
- B) Parallel processing for improved performance and throughput
- C) Simpler code
- D) Better security

**Answer: B**
Fan-out/fan-in enables parallel processing of independent tasks, significantly reducing total execution time.

---

## Question 4
How many activity functions can you fan-out to?

- A) Maximum 10
- B) Maximum 100
- C) Hundreds or thousands, limited by platform quotas and resources
- D) Only 2

**Answer: C**
Durable Functions can fan-out to many activity instances (hundreds or thousands), limited by platform quotas and app configuration.

---

## Question 5
What happens if one activity fails in a fan-out scenario?

- A) All activities are cancelled
- B) Task.WhenAll throws, and the orchestrator can handle the exception
- C) Failed activity is ignored
- D) Entire Function App crashes

**Answer: B**
If any activity fails, Task.WhenAll throws an exception. The orchestrator can catch and handle it (retry, compensate, etc.).

---

## Question 6
Can you process batches of items using fan-out/fan-in?

- A) No, only single items
- B) Yes, iterate over collection and fan-out an activity for each item
- C) Only in Premium plan
- D) Requires custom code

**Answer: B**
A common pattern is iterating over a collection and fanning-out an activity function for each item to process them in parallel.

---

## Question 7
How do you aggregate results in the fan-in phase?

- A) Results are lost
- B) Collect the Task results from Task.WhenAll and process them
- C) Use a database
- D) Results are automatically merged

**Answer: B**
After Task.WhenAll completes, you access the Result property of each task to collect and aggregate all results.

---

## Question 8
What is the difference between fan-out/fan-in and function chaining?

- A) No difference
- B) Fan-out/fan-in runs activities in parallel; chaining runs them sequentially
- C) Chaining is faster
- D) Fan-out is only for databases

**Answer: B**
Chaining executes functions one after another (sequential), while fan-out/fan-in executes multiple functions simultaneously (parallel).

---

## Question 9
Can you combine fan-out/fan-in with other patterns?

- A) No, mutually exclusive
- B) Yes, patterns can be combined (e.g., chain of fan-out operations)
- C) Only with custom code
- D) Only in Enterprise tier

**Answer: B**
Durable Function patterns can be combined. For example, you can chain multiple fan-out/fan-in operations or fan-out to other orchestrators.

---

## Question 10
What is sub-orchestration in Durable Functions?

- A) A billing tier
- B) An orchestrator calling other orchestrator functions for composition
- C) A monitoring feature
- D) A testing mode

**Answer: B**
Sub-orchestration allows orchestrator functions to call other orchestrators, enabling complex workflow composition and reuse.
