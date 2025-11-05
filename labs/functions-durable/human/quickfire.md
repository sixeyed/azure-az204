# Durable Functions - Human Interaction Pattern - Quickfire Questions

## Question 1
What is the human interaction pattern in Durable Functions?

- A) Functions that talk to users
- B) Workflows that wait for external human approval or input before proceeding
- C) User interface generation
- D) Speech recognition

**Answer: B**
The human interaction pattern enables workflows to pause and wait for external events (like approvals) before continuing execution.

---

## Question 2
What Durable Functions API is used to wait for external events?

- A) context.WaitForEvent
- B) context.WaitForExternalEvent
- C) context.Pause
- D) Task.Delay

**Answer: B**
The context.WaitForExternalEvent method pauses orchestration until an external event with the specified name is raised.

---

## Question 3
How do you raise an external event to a waiting orchestration?

- A) Using the DurableOrchestrationClient.RaiseEventAsync method
- B) Through email
- C) Automatically after timeout
- D) Not possible

**Answer: A**
External events are raised using the client binding's RaiseEventAsync method, passing the instance ID, event name, and event data.

---

## Question 4
What happens if an external event never arrives?

- A) Orchestration completes anyway
- B) Orchestration waits indefinitely (or until timeout if implemented)
- C) Orchestration fails automatically after 1 hour
- D) Function App crashes

**Answer: B**
Without a timeout, orchestration waits indefinitely. Best practice is to use Task.WhenAny with a durable timer for timeout logic.

---

## Question 5
How do you implement a timeout for human interaction?

- A) Not possible
- B) Use Task.WhenAny with WaitForExternalEvent and CreateTimer
- C) Set a configuration value
- D) Use Thread.Sleep

**Answer: B**
Create a timer with CreateTimer and use Task.WhenAny to race between the external event and timer, handling timeout if timer wins.

---

## Question 6
What is an approval workflow use case?

- A) Automatic processing only
- B) Waiting for manager/admin approval before proceeding with an action
- C) User registration
- D) Data validation

**Answer: B**
Approval workflows pause for human decision (approve/reject) before continuing, common in expense approvals, content moderation, etc.

---

## Question 7
Can multiple external events be sent to the same orchestration?

- A) No, only one event allowed
- B) Yes, orchestration can wait for multiple different events
- C) Only in Premium plan
- D) Only sequentially

**Answer: B**
Orchestrations can wait for multiple events sequentially or use Task.WhenAll/WhenAny to wait for multiple events concurrently.

---

## Question 8
How can you notify users that their input is needed?

- A) Not possible
- B) Activity function sends notification (email, SMS, etc.) before waiting for event
- C) Automatic notifications
- D) Only through portal

**Answer: B**
Before waiting for external event, call an activity function that sends notifications (email, SMS, push) to inform users action is needed.

---

## Question 9
What data can be passed with an external event?

- A) No data, event name only
- B) Any JSON-serializable data relevant to the event
- C) Only strings
- D) Only numbers

**Answer: B**
External events can carry JSON-serializable payloads (objects, arrays, primitives) that are received by the waiting orchestrator.

---

## Question 10
What is escalation in the context of human interaction workflows?

- A) Increasing server resources
- B) Automatically notifying higher authority or taking alternative action after timeout
- C) Making functions run faster
- D) Scaling out instances

**Answer: B**
Escalation handles timeout scenarios by notifying supervisors, auto-approving, or taking alternative paths when human response isn't received in time.
