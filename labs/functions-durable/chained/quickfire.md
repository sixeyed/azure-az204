# Durable Functions - Chained Pattern - Quickfire Questions

## Question 1
What are Azure Durable Functions?


- A) Functions that run for a long time
- B) Functions that cost more
- C) An extension that enables stateful workflows and orchestrations in serverless environments
- D) Functions with high availability

**Answer: C**
Durable Functions add stateful orchestration, durable timers, and reliable execution patterns to serverless Azure Functions.
---
## Question 2
What is the function chaining pattern?


- A) Executing a sequence of functions in a specific order, passing output of one as input to the next
- B) Running functions in parallel
- C) Connecting to blockchain
- D) Linking function apps together

**Answer: A**
Function chaining executes functions sequentially where the output of one function becomes the input of the next.
---
## Question 3
What are the three function types in Durable Functions?


- A) Input, Output, Process
- B) Orchestrator, Activity, Client
- C) Trigger, Binding, Execute
- D) Small, Medium, Large

**Answer: B**
Orchestrator functions define the workflow, Activity functions do the work, and Client functions start orchestrations.
---
## Question 4
What is the role of an orchestrator function?


- A) Defines and coordinates the workflow logic
- B) Performs computational work
- C) Monitors function execution
- D) Handles HTTP requests only

**Answer: A**
Orchestrator functions define the workflow, calling activity functions and managing state and execution flow.
---
## Question 5
What is the role of an activity function?


- A) Only logs information
- B) Performs the actual work/business logic in the workflow
- C) Starts the orchestration
- D) Manages state

**Answer: B**
Activity functions contain the actual work logic. They're called by orchestrators and can perform any operations.
---
## Question 6
What is a key constraint of orchestrator functions?


- A) They can't call activity functions
- B) They must be deterministic (same inputs always produce same outputs/actions)
- C) They can't use variables
- D) They can only run once

**Answer: B**
Orchestrator functions must be deterministic because they may be replayed multiple times to rebuild state from history.
---
## Question 7
What should you NOT do in an orchestrator function?


- A) Call activity functions
- B) Perform non-deterministic operations (random numbers, DateTime.Now, HTTP calls)
- C) Return values
- D) Use context objects

**Answer: B**
Orchestrators must avoid non-deterministic operations. Use context.CurrentUtcDateTime, context.NewGuid(), or activity functions for such operations.
---
## Question 8
How does Durable Functions maintain state?


- A) Using Event Sourcing pattern with Azure Storage (or other providers)
- B) Using databases
- C) In configuration files
- D) In memory only

**Answer: A**
Durable Functions use Event Sourcing, storing execution history in Azure Storage Tables and rebuilding state through replay.
---
## Question 9
What happens if an activity function in a chain fails?


- A) Nothing, errors are ignored
- B) The orchestrator can retry, handle errors, or compensate based on your logic
- C) All previous activities are rolled back automatically
- D) The entire orchestration is immediately cancelled

**Answer: B**
Orchestrators can implement error handling, automatic retries, compensation logic, or fallback paths when activities fail.
---
## Question 10
Can you pass data between chained activity functions?


- A) Yes, the orchestrator passes the output of one activity as input to the next
- B) Only using global variables
- C) No, each function is isolated
- D) Only through database

**Answer: A**
In function chaining, the orchestrator receives output from one activity and passes it as input to the next, creating a data flow.