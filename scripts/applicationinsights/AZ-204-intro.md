
Excellent work implementing Application Insights! Monitoring and diagnostics are critical AZ-204 exam topics appearing across multiple domains.

When to use Application Insights versus other monitoring solutions is fundamental. Use Application Insights for application-specific telemetry (request/dependency tracking, custom events, performance), Azure Monitor for infrastructure metrics (CPU, memory, disk), Log Analytics for querying across data sources, and Azure Service Health for platform status. The exam tests choosing the right tool for different monitoring scenarios.

Auto-instrumentation vs SDK integration is a key distinction. Auto-instrumentation is perfect for standard web apps - enable it through the Portal without code changes, automatically tracks requests/dependencies/exceptions, works with App Service and Azure Functions. SDK integration provides custom telemetry and fine-grained control - track specific events/operations, add custom properties, control sampling, but requires code changes and NuGet packages. Know when to use each approach.

Workspace-based versus Classic mode needs to be understood. Workspace-based (newer, recommended) stores data in Log Analytics workspaces enabling cross-resource queries, retention policies, and Azure RBAC. Classic mode uses separate Application Insights storage with limited query capabilities. The exam expects you to recommend workspace-based for new deployments.

Telemetry types are heavily tested. Requests (HTTP requests with duration and result code), Dependencies (external service calls like databases, REST APIs), Exceptions (application errors with stack traces), Traces (log messages from logging frameworks), Custom Events (business-specific events you define), Page Views (browser-side navigation), and Custom Metrics (numeric measurements you track). Know what each telemetry type captures and when to use it.

Correlation using operation IDs enables end-to-end tracing across distributed systems. Application Insights assigns an operation ID to each request and propagates it to all dependencies, allowing you to trace a single transaction across multiple services. The exam tests understanding of how correlation works and how to view end-to-end transactions.

Sampling strategies control how much telemetry is collected. Adaptive sampling (default) adjusts automatically based on traffic volume. Fixed-rate sampling collects a fixed percentage. Ingestion sampling occurs after data reaches Azure, reducing costs but losing data. Know the tradeoffs and when to use each strategy.

We'll cover configuration via Portal, ARM templates, and CLI commands, integration with Log Analytics, Azure Monitor, and Azure Functions, querying with Kusto Query Language (KQL), and common exam scenarios about troubleshooting performance issues, setting up alerts, and implementing custom telemetry.

Master Application Insights for the AZ-204!
