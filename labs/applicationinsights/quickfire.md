# Azure Application Insights - Quickfire Questions

## Question 1
What is Azure Application Insights?


- A) A database service
- B) A storage service
- C) Application Performance Management (APM) service for monitoring live applications
- D) A networking service

**Answer: C**
Application Insights provides telemetry collection, performance monitoring, error tracking, and usage analytics for applications.
---
## Question 2
What types of telemetry does Application Insights collect?


- A) Requests, dependencies, exceptions, traces, metrics, events, page views
- B) Only logs
- C) Only errors
- D) Only performance data

**Answer: A**
Comprehensive telemetry: HTTP requests, external dependencies, exceptions, custom events, performance counters, and more.
---
## Question 3
How do you instrument an application for Application Insights?


- A) Install SDK or enable auto-instrumentation (for supported platforms)
- B) Not possible
- C) Manual logging only
- D) Requires custom service

**Answer: A**
Add Application Insights SDK to code or use auto-instrumentation/agent for .NET, Java, Node.js on App Service.
---
## Question 4
What is the instrumentation key (connection string)?


- A) Unique identifier linking telemetry to specific Application Insights resource
- B) API key
- C) Encryption key
- D) Database connection

**Answer: A**
The connection string (or legacy instrumentation key) routes telemetry data to the correct Application Insights resource.
---
## Question 5
What is automatic dependency tracking?


- A) Manual logging
- B) SDK automatically captures calls to databases, HTTP APIs, Azure services without code
- C) Not supported
- D) Only for .NET

**Answer: B**
SDKs automatically track dependencies (SQL, HTTP, Redis, Cosmos DB) without manual instrumentation.
---
## Question 6
What is distributed tracing?


- A) Following requests across multiple services/components to understand end-to-end flow
- B) GPS tracking
- C) Tracing in one application
- D) Network tracing

**Answer: A**
Distributed tracing correlates telemetry across microservices, showing complete request path and bottlenecks.
---
## Question 7
What is Application Map?


- A) Geographic map
- B) Visual representation of application components and their dependencies
- C) Network map
- D) Deployment map

**Answer: B**
Application Map shows application topology: components, dependencies, and health status visually.
---
## Question 8
What are availability tests (ping tests)?


- A) Load tests
- B) Network tests only
- C) Synthetic tests probing application endpoints from global locations to verify uptime
- D) Security tests

**Answer: C**
Availability tests continuously monitor endpoints from Azure regions, alerting when unavailable.
---
## Question 9
What is the difference between metrics and logs?


- A) No difference
- B) Metrics are slower
- C) Metrics are numerical time-series data; logs are detailed event/message records
- D) Logs are numerical only

**Answer: C**
Metrics: aggregated numbers over time (response time, request rate). Logs: detailed records of events (exceptions, traces).
---
## Question 10
What query language does Application Insights use?


- A) Kusto Query Language (KQL)
- B) JavaScript
- C) Python
- D) SQL

**Answer: A**
KQL (Kusto Query Language) is used for querying telemetry in Application Insights and Log Analytics.