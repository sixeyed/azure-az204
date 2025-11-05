# Azure Log Analytics - Quickfire Questions

## Question 1
What is Azure Log Analytics?

- A) A database service
- B) Service for collecting, analyzing, and querying log data from Azure and other sources
- C) A storage service
- D) A networking service

**Answer: B**
Log Analytics ingests logs and metrics from resources, providing querying and visualization via KQL.

---

## Question 2
What is a Log Analytics workspace?

- A) A physical office
- B) Container for log data with access control, retention, and query scope
- C) A virtual machine
- D) A database

**Answer: B**
Workspaces store log data, define retention policies, and control access to monitoring data.

---

## Question 3
What query language is used in Log Analytics?

- A) SQL
- B) Kusto Query Language (KQL)
- C) Python
- D) PowerShell

**Answer: B**
KQL provides powerful querying capabilities for filtering, aggregating, and analyzing log data.

---

## Question 4
What types of data can Log Analytics collect?

- A) Only application logs
- B) Azure resource logs, application telemetry, OS metrics, custom logs, security events
- C) Only Azure resources
- D) Only performance data

**Answer: B**
Log Analytics collects diverse data: Azure diagnostics, VM metrics, Application Insights data, custom sources.

---

## Question 5
What is a KQL query example for counting events?

- A) SELECT COUNT(*)
- B) Events | count
- C) COUNT Events
- D) GET /count

**Answer: B**
KQL uses pipe syntax: `TableName | operation`. Example: `AzureActivity | summarize count()`.

---

## Question 6
What is the `where` operator in KQL?

- A) Location query
- B) Filters rows based on conditions
- C) Sorting operator
- D) Aggregation function

**Answer: B**
`where` filters data: `SecurityEvent | where EventID == 4625` (failed login attempts).

---

## Question 7
What is the `summarize` operator?

- A) Text summary
- B) Aggregates data (count, avg, sum) grouped by dimensions
- C) Sorts data
- D) Filters data

**Answer: B**
`summarize` aggregates: `Heartbeat | summarize count() by Computer` counts heartbeats per computer.

---

## Question 8
How do you visualize Log Analytics data?

- A) Only text output
- B) Built-in charts, dashboards, Azure Workbooks, Power BI
- C) No visualization
- D) Only tables

**Answer: B**
Render charts in query results, pin to dashboards, create Azure Workbooks, or export to Power BI.

---

## Question 9
What is the retention period for Log Analytics?

- A) 7 days fixed
- B) 30-730 days configurable (per data type)
- C) Forever
- D) 24 hours only

**Answer: B**
Default is often 30-90 days, configurable up to 730 days (2 years) or longer with archive.

---

## Question 10
Can you create alerts from Log Analytics queries?

- A) No alerting
- B) Yes, using Azure Monitor alerts triggered by query results
- C) Only manual checking
- D) Only email notifications

**Answer: B**
Log-based alerts run queries on schedule and trigger actions when thresholds are met.
