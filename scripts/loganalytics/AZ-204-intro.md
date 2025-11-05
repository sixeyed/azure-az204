# Log Analytics - AZ-204 Exam Introduction

Great work with Log Analytics! This is essential knowledge for the AZ-204's monitoring and troubleshooting objectives.

## What We'll Cover

**Application Insights integration with Log Analytics** is the modern architecture. Workspace-based Application Insights stores all telemetry in Log Analytics, enabling cross-resource queries, longer retention, and consistent querying. The exam tests understanding of this integration and benefits over classic Application Insights.

**Basic KQL queries with pipe operators** must be understood. The pipe (|) sends output of one operator as input to the next. Example: `AppTraces | where severityLevel > 2 | count` gets traces, filters by severity, counts results. The exam tests reading and writing simple KQL queries.

**Log Analytics tables** for Application Insights need to be memorized. `AppTraces` for logging statements (ILogger, console.log), `AppEvents` for custom tracked events, `AppMetrics` for custom metrics, `AppDependencies` for external service calls (HTTP, SQL, Redis), `AppRequests` for incoming HTTP requests, `AppExceptions` for errors with stack traces. The exam tests knowing which table to query for different telemetry types.

**Configuring workspaces for multiple data sources** enables centralized monitoring. One workspace can receive telemetry from multiple Application Insights instances, VMs with monitoring agents, Azure resources with diagnostic settings. The exam tests understanding of workspace architecture and benefits.

**Troubleshooting scenarios** require KQL skills. Finding slow dependencies (`AppDependencies | where duration > 1000`), monitoring health (`AppRequests | summarize SuccessRate = sum(success)/count()`), analyzing custom metrics, identifying error patterns. The exam presents troubleshooting scenarios requiring appropriate queries.

**Workspace-based benefits** include cross-application correlation, longer retention options (up to 730 days), Azure RBAC integration, cost optimization with commitment tiers, and support for Azure Monitor features like alerts and dashboards. The exam tests understanding of why workspace-based is preferred.

**Query performance optimization** with techniques like filtering early in the query pipeline, using `summarize` instead of `distinct` for counts, limiting result sets, and avoiding expensive operations on large datasets. The exam may test query optimization understanding.

We'll cover **KQL operators in depth**, **creating alerts from queries**, **building dashboards**, **monitoring costs**, **retention policies**, and **common scenarios** about troubleshooting application issues, analyzing performance, and creating actionable monitoring.

Master Log Analytics querying for the AZ-204!
