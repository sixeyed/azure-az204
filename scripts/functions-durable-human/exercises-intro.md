# Durable Functions - Human Interaction Pattern - Exercises Introduction

We've covered the human interaction pattern where orchestrations pause to wait for external human input with timeouts. Now let's build a two-factor authentication system using SMS.

## What You'll Do

You'll **set up a Twilio account and phone number** for sending SMS messages. Twilio provides a simple API for programmable communications. Then you'll **examine the code structure** - an HTTP trigger to start authentication, an SMS verify orchestrator that coordinates the process, and an SMS challenge activity that sends the verification code.

The orchestrator uses two key durable functions features: **WaitForExternalEvent** to pause until receiving the verification code from the user, and **CreateTimer** to implement a timeout (30 seconds in this case). The orchestrator races these two tasks using `Task.WhenAny` - whichever completes first determines the outcome.

You'll **configure local settings with Twilio credentials** (account SID and auth token) to enable SMS sending. Then you'll **test the workflow** - trigger authentication via HTTP, receive an SMS with a verification code on your phone, and **respond via curl** to the raiseEvent endpoint with the code. If you respond within 30 seconds, verification succeeds. Wait too long, and the timer fires first, causing verification to fail.

After **deployment to Azure**, you'll test the production workflow. The **challenge** asks about replacing polling (client repeatedly checking status) with queue-based notifications (server pushes completion events to a queue). This teaches you about different patterns for notifying clients of long-running operation completion.

The key learning: external events enable orchestrations to pause indefinitely (or until timeout) without consuming resources. The orchestration checkpoints its state and goes to sleep. When the event arrives, it wakes up and continues exactly where it left off.

Let's implement human interaction workflows!
