# Durable Functions - Human Interaction Pattern - AZ-204 Exam Introduction

Great work with human interaction! This pattern appears frequently in AZ-204 scenarios requiring approvals, verifications, or external input.

## What We'll Cover

**External events sent via raiseEvent HTTP endpoint** enable sending data into running orchestrations. The endpoint URL is provided in HTTP management APIs (sendEventPostUri). Event names must match exactly what the orchestrator is waiting for (case-sensitive). Events can carry data payloads. The exam tests understanding of the external event mechanism and endpoint usage.

**WaitForExternalEvent** makes orchestrators pause until an event with a matching name arrives. The orchestration checkpoints state and stops consuming resources. When the event arrives (via HTTP POST to raiseEvent endpoint), the orchestration wakes up and continues. Multiple events can be sent - only those being waited for are consumed. The exam tests understanding of the pause/resume mechanism.

**Durable timers with CreateTimer** implement timeouts without blocking threads or consuming resources. Timers checkpoint their state - if the function app restarts, timers resume correctly. When combined with `Task.WhenAny`, timers enable racing against events for timeout scenarios. The exam tests configuring timeouts and understanding their behavior during failures.

**Task.WhenAny for racing timers against events** is the core pattern for human interaction with timeouts. Create timer task, create WaitForExternalEvent task, await `Task.WhenAny(timerTask, eventTask)`, check which completed first. The exam tests implementing timeout logic correctly.

**HTTP management API URLs** for human interaction scenarios must be understood. sendEventPostUri for raising external events, statusQueryGetUri for checking completion, terminatePostUri if user cancels. The exam tests which endpoint to use for different operations.

**Security with secure parameters** (@secure decorator in Bicep, SecureString in ARM) protects sensitive data like Twilio credentials. Timeouts should be configurable parameters, not hardcoded. The exam tests security best practices for credentials and configuration.

**Distinguishing external events from HTTP triggers** is important. HTTP triggers start new orchestrations, external events send data to running orchestrations. The exam may present confusion scenarios requiring clarification.

We'll cover **approval workflows**, **verification patterns**, **notification mechanisms**, **timeout strategies**, and **scenarios** about implementing multi-step approvals, two-factor authentication, and long-running processes requiring human input.

Master human interaction patterns for the AZ-204!
