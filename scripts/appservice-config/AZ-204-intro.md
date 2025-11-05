# App Service Configuration - AZ-204 Exam Introduction

Great work implementing health checks and auto-heal! These production features are important AZ-204 exam topics testing your understanding of application reliability.

## What We'll Cover

**Application settings as environment variables** override configuration files - this is heavily tested. Settings take priority over appsettings.json or web.config. The **double underscore pattern** for nested configuration (Rng__FailAfter__CallCount becomes Rng:FailAfter:CallCount in .NET Core's hierarchical configuration) is important. The exam tests configuration precedence and how to set environment-specific values without code changes.

**Health checks** require an endpoint that returns HTTP 200 when healthy and 500-series when unhealthy. App Service periodically probes this endpoint (every minute). Failed health checks trigger actions based on configuration. **Load balancing thresholds** (minimum 2 minutes, maximum 10 minutes) determine how long failed instances stay in rotation before being marked unhealthy. The exam tests when health checks are triggered and what actions occur.

**Health check results in Azure Monitor** provide metrics for monitoring. You can set alerts based on unhealthy instances, track availability over time, and correlate health issues with application logs. The exam may test how to monitor application health using these metrics.

**Scale up versus scale out** is a critical distinction. Scale up changes SKU for more CPU/memory per instance (requires restart, improves per-instance performance). Scale out adds more instances for higher total throughput and availability (no restart, distributes load). The exam frequently tests when to use each strategy and their effects on applications.

**Worker instance benefits** include throughput (more instances handle more concurrent requests), availability (application stays online when individual instances fail), and automatic traffic routing (load balancer sends requests only to healthy instances). The exam tests understanding of multi-instance architectures and their reliability benefits.

**SKU tier scaling limitations** must be memorized. Free/Shared: no scale-out. Basic: up to 3 instances, manual scaling only. Standard: up to 10 instances, auto-scale available. Premium: up to 30 instances, enhanced performance. The exam tests which tiers support what scaling capabilities.

**Auto-heal configuration** with trigger types (request count, slow requests, status codes, memory thresholds) and actions (recycle process, log event, custom executable) enables automatic recovery from specific failure patterns. The exam tests understanding of when to use auto-heal versus health checks: **health checks remove instances from load balancer**, **auto-heal restarts them**. Know the key limitation: single instances won't be automatically replaced to avoid downtime.

We'll cover **monitoring and alerting**, **scaling best practices**, **common failure scenarios**, and **troubleshooting unhealthy instances**.

Master App Service reliability patterns for the AZ-204!
