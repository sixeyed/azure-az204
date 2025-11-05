# Azure Log Analytics - Quickfire Questions

## Question 1
What is Azure Log Analytics?


- A) A database service
- B) A networking service
- C) A storage service
- D) Service for collecting, analyzing, and querying log data from Azure and other sources

**Answer: D**
Log Analytics ingests logs and metrics from resources, providing querying and visualization via KQL.
---
## Question 2
What is a Log Analytics workspace?


- A) A virtual machine
- B) A database
- C) A physical office
- D) Container for log data with access control, retention, and query scope

**Answer: D**
Workspaces store log data, define retention policies, and control access to monitoring data.
---
## Question 3
What query language is used in Log Analytics?


- A) Python
- B) PowerShell
- C) Kusto Query Language (KQL)
- D) SQL

**Answer: C**
KQL provides powerful querying capabilities for filtering, aggregating, and analyzing log data.
---
## Question 4
What types of data can Log Analytics collect?


- A) Only performance data
- B) Azure resource logs, application telemetry, OS metrics, custom logs, security events
- C) Only application logs
- D) Only Azure resources

**Answer: B**
Log Analytics collects diverse data: Azure diagnostics, VM metrics, Application Insights data, custom sources.
---
## Question 5
What is a KQL query example for counting events?


- A) COUNT Events
- B) Events | count
- C) GET /count
- D) SELECT COUNT(*)

**Answer: B**
KQL uses pipe syntax: `TableName | operation`. Example: `AzureActivity | summarize count()`.
---
## Question 6
What is the `where` operator in KQL?


- A) Filters rows based on conditions
- B) Location query
- C) Sorting operator
- D) Aggregation function

**Answer: A**
`where` filters data: `SecurityEvent | where EventID == 4625` (failed login attempts).
---
## Question 7
What is the `summarize` operator?


- A) Filters data
- B) Text summary
- C) Aggregates data (count, avg, sum) grouped by dimensions
- D) Sorts data

**Answer: C**
`summarize` aggregates: `Heartbeat | summarize count() by Computer` counts heartbeats per computer.
---
## Question 8
How do you visualize Log Analytics data?


- A) No visualization
- B) Only text output
- C) Built-in charts, dashboards, Azure Workbooks, Power BI
- D) Only tables

**Answer: C**
Render charts in query results, pin to dashboards, create Azure Workbooks, or export to Power BI.
---
## Question 9
What is the retention period for Log Analytics?


- A) 24 hours only
- B) 7 days fixed
- C) 30-730 days configurable (per data type)
- D) Forever

**Answer: C**
Default is often 30-90 days, configurable up to 730 days (2 years) or longer with archive.
---
## Question 10
Can you create alerts from Log Analytics queries?


- A) No alerting
- B) Only email notifications
- C) Yes, using Azure Monitor alerts triggered by query results
- D) Only manual checking

**Answer: C**
Log-based alerts run queries on schedule and trigger actions when thresholds are met.