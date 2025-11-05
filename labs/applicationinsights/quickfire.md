# Azure Application Insights - Quickfire Questions

## Question 1
What is Azure Application Insights?

- A) A database service
- B) Application Performance Management (APM) service for monitoring live applications
- C) A storage service
- D) A networking service

**Answer: B**
Application Insights provides telemetry collection, performance monitoring, error tracking, and usage analytics for applications.

---

## Question 2
What types of telemetry does Application Insights collect?

- A) Only errors
- B) Requests, dependencies, exceptions, traces, metrics, events, page views
- C) Only performance data
- D) Only logs

**Answer: B**
Comprehensive telemetry: HTTP requests, external dependencies, exceptions, custom events, performance counters, and more.

---

## Question 3
How do you instrument an application for Application Insights?

- A) Manual logging only
- B) Install SDK or enable auto-instrumentation (for supported platforms)
- C) Not possible
- D) Requires custom service

**Answer: B**
Add Application Insights SDK to code or use auto-instrumentation/agent for .NET, Java, Node.js on App Service.

---

## Question 4
What is the instrumentation key (connection string)?

- A) Encryption key
- B) Unique identifier linking telemetry to specific Application Insights resource
- C) Database connection
- D) API key

**Answer: B**
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

- A) Tracing in one application
- B) Following requests across multiple services/components to understand end-to-end flow
- C) GPS tracking
- D) Network tracing

**Answer: B**
Distributed tracing correlates telemetry across microservices, showing complete request path and bottlenecks.

---

## Question 7
What is Application Map?

- A) Geographic map
- B) Visual representation of application components and their dependencies
- C) Deployment map
- D) Network map

**Answer: B**
Application Map shows application topology: components, dependencies, and health status visually.

---

## Question 8
What are availability tests (ping tests)?

- A) Network tests only
- B) Synthetic tests probing application endpoints from global locations to verify uptime
- C) Load tests
- D) Security tests

**Answer: B**
Availability tests continuously monitor endpoints from Azure regions, alerting when unavailable.

---

## Question 9
What is the difference between metrics and logs?

- A) No difference
- B) Metrics are numerical time-series data; logs are detailed event/message records
- C) Metrics are slower
- D) Logs are numerical only

**Answer: B**
Metrics: aggregated numbers over time (response time, request rate). Logs: detailed records of events (exceptions, traces).

---

## Question 10
What query language does Application Insights use?

- A) SQL
- B) Kusto Query Language (KQL)
- C) JavaScript
- D) Python

**Answer: B**
KQL (Kusto Query Language) is used for querying telemetry in Application Insights and Log Analytics.
