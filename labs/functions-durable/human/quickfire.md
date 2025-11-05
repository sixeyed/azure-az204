# Durable Functions - Human Interaction Pattern - Quickfire Questions

## Question 1
What is the human interaction pattern in Durable Functions?


- A) User interface generation
- B) Speech recognition
- C) Workflows that wait for external human approval or input before proceeding
- D) Functions that talk to users

**Answer: C**
The human interaction pattern enables workflows to pause and wait for external events (like approvals) before continuing execution.
---
## Question 2
What Durable Functions API is used to wait for external events?


- A) context.Pause
- B) Task.Delay
- C) context.WaitForExternalEvent
- D) context.WaitForEvent

**Answer: C**
The context.WaitForExternalEvent method pauses orchestration until an external event with the specified name is raised.
---
## Question 3
How do you raise an external event to a waiting orchestration?


- A) Automatically after timeout
- B) Using the DurableOrchestrationClient.RaiseEventAsync method
- C) Not possible
- D) Through email

**Answer: B**
External events are raised using the client binding's RaiseEventAsync method, passing the instance ID, event name, and event data.
---
## Question 4
What happens if an external event never arrives?


- A) Orchestration fails automatically after 1 hour
- B) Function App crashes
- C) Orchestration waits indefinitely (or until timeout if implemented)
- D) Orchestration completes anyway

**Answer: C**
Without a timeout, orchestration waits indefinitely. Best practice is to use Task.WhenAny with a durable timer for timeout logic.
---
## Question 5
How do you implement a timeout for human interaction?


- A) Set a configuration value
- B) Use Thread.Sleep
- C) Not possible
- D) Use Task.WhenAny with WaitForExternalEvent and CreateTimer

**Answer: D**
Create a timer with CreateTimer and use Task.WhenAny to race between the external event and timer, handling timeout if timer wins.
---
## Question 6
What is an approval workflow use case?


- A) Data validation
- B) Waiting for manager/admin approval before proceeding with an action
- C) User registration
- D) Automatic processing only

**Answer: B**
Approval workflows pause for human decision (approve/reject) before continuing, common in expense approvals, content moderation, etc.
---
## Question 7
Can multiple external events be sent to the same orchestration?


- A) Only in Premium plan
- B) Only sequentially
- C) Yes, orchestration can wait for multiple different events
- D) No, only one event allowed

**Answer: C**
Orchestrations can wait for multiple events sequentially or use Task.WhenAll/WhenAny to wait for multiple events concurrently.
---
## Question 8
How can you notify users that their input is needed?


- A) Activity function sends notification (email, SMS, etc.) before waiting for event
- B) Only through portal
- C) Automatic notifications
- D) Not possible

**Answer: A**
Before waiting for external event, call an activity function that sends notifications (email, SMS, push) to inform users action is needed.
---
## Question 9
What data can be passed with an external event?


- A) Any JSON-serializable data relevant to the event
- B) No data, event name only
- C) Only numbers
- D) Only strings

**Answer: A**
External events can carry JSON-serializable payloads (objects, arrays, primitives) that are received by the waiting orchestrator.
---
## Question 10
What is escalation in the context of human interaction workflows?


- A) Making functions run faster
- B) Increasing server resources
- C) Automatically notifying higher authority or taking alternative action after timeout
- D) Scaling out instances

**Answer: C**
Escalation handles timeout scenarios by notifying supervisors, auto-approving, or taking alternative paths when human response isn't received in time.