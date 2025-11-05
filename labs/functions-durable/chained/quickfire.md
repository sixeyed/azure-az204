# Durable Functions - Chained Pattern - Quickfire Questions

## Question 1
What are Azure Durable Functions?

- A) Functions that run for a long time
- B) An extension that enables stateful workflows and orchestrations in serverless environments
- C) Functions with high availability
- D) Functions that cost more

**Answer: B**
Durable Functions add stateful orchestration, durable timers, and reliable execution patterns to serverless Azure Functions.

---

## Question 2
What is the function chaining pattern?

- A) Linking function apps together
- B) Executing a sequence of functions in a specific order, passing output of one as input to the next
- C) Running functions in parallel
- D) Connecting to blockchain

**Answer: B**
Function chaining executes functions sequentially where the output of one function becomes the input of the next.

---

## Question 3
What are the three function types in Durable Functions?

- A) Small, Medium, Large
- B) Orchestrator, Activity, Client
- C) Input, Output, Process
- D) Trigger, Binding, Execute

**Answer: B**
Orchestrator functions define the workflow, Activity functions do the work, and Client functions start orchestrations.

---

## Question 4
What is the role of an orchestrator function?

- A) Performs computational work
- B) Defines and coordinates the workflow logic
- C) Handles HTTP requests only
- D) Monitors function execution

**Answer: B**
Orchestrator functions define the workflow, calling activity functions and managing state and execution flow.

---

## Question 5
What is the role of an activity function?

- A) Starts the orchestration
- B) Performs the actual work/business logic in the workflow
- C) Only logs information
- D) Manages state

**Answer: B**
Activity functions contain the actual work logic. They're called by orchestrators and can perform any operations.

---

## Question 6
What is a key constraint of orchestrator functions?

- A) They can't call activity functions
- B) They must be deterministic (same inputs always produce same outputs/actions)
- C) They can only run once
- D) They can't use variables

**Answer: B**
Orchestrator functions must be deterministic because they may be replayed multiple times to rebuild state from history.

---

## Question 7
What should you NOT do in an orchestrator function?

- A) Call activity functions
- B) Perform non-deterministic operations (random numbers, DateTime.Now, HTTP calls)
- C) Use context objects
- D) Return values

**Answer: B**
Orchestrators must avoid non-deterministic operations. Use context.CurrentUtcDateTime, context.NewGuid(), or activity functions for such operations.

---

## Question 8
How does Durable Functions maintain state?

- A) In memory only
- B) Using Event Sourcing pattern with Azure Storage (or other providers)
- C) In configuration files
- D) Using databases

**Answer: B**
Durable Functions use Event Sourcing, storing execution history in Azure Storage Tables and rebuilding state through replay.

---

## Question 9
What happens if an activity function in a chain fails?

- A) The entire orchestration is immediately cancelled
- B) The orchestrator can retry, handle errors, or compensate based on your logic
- C) All previous activities are rolled back automatically
- D) Nothing, errors are ignored

**Answer: B**
Orchestrators can implement error handling, automatic retries, compensation logic, or fallback paths when activities fail.

---

## Question 10
Can you pass data between chained activity functions?

- A) No, each function is isolated
- B) Yes, the orchestrator passes the output of one activity as input to the next
- C) Only using global variables
- D) Only through database

**Answer: B**
In function chaining, the orchestrator receives output from one activity and passes it as input to the next, creating a data flow.
