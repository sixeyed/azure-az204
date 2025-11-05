# Durable Functions - Chained Pattern - AZ-204 Exam Introduction

Great work with the chained pattern! Durable Functions is an important AZ-204 topic testing your understanding of serverless orchestration.

## What We'll Cover

**The five durable function patterns** must be memorized. Chained (sequential steps with output passing), Fan-out/fan-in (parallel execution with aggregation), Async HTTP APIs (long-running operations with status polling), Monitoring (periodic checks with alerting), Human interaction (waiting for external input with timeouts). The exam heavily tests pattern recognition - given a scenario, which pattern should you use?

**Orchestrator constraints** are critical. Orchestrators must be deterministic (same inputs produce same outputs), cannot use DateTime.Now (use CurrentUtcDateTime instead), cannot make direct HTTP calls (use activity functions), cannot do I/O directly (use activities), and must not create random numbers (use activity functions for randomness). The exam tests understanding of why these constraints exist and how to work within them.

**The three binding types** need to be understood. DurableClient triggers start orchestrations and query status (HTTP triggers or queue triggers use this), OrchestrationTrigger marks orchestrator functions that coordinate activities, ActivityTrigger marks activity functions that do actual work. The exam tests which binding to use for different function types.

**State persistence in Azure Storage** enables orchestrations to survive failures. Durable Functions uses tables, queues, and blobs to track execution state. Orchestrations can run for days or months because state is externalized. The exam tests understanding of how durability works and its implications for scaling and reliability.

**Error handling with retry policies** allows activities to automatically retry on failure with exponential backoff. Know the RetryOptions configuration (MaxNumberOfAttempts, FirstRetryInterval, BackoffCoefficient, MaxRetryInterval). The exam tests designing resilient orchestrations.

We'll cover **orchestration lifecycle**, **activity function patterns**, **monitoring and diagnostics**, **performance considerations**, **when to use durable functions vs Logic Apps**, and **common scenarios** about implementing long-running workflows, coordinating microservices, and handling failures gracefully.

Master durable functions patterns for the AZ-204!
