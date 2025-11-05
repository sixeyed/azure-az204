# Log Analytics - Exercises Introduction

We've covered Log Analytics as Azure's centralized log data store providing rich query capabilities with Kusto Query Language (KQL). Now let's explore application telemetry and create monitoring dashboards.

## What You'll Do

You'll start by **setting up a Log Analytics workspace** - the central repository for all your telemetry data. Then you'll **link Application Insights to the workspace**, enabling all your application telemetry to flow into Log Analytics for querying.

You'll **deploy a sample application** (Fulfilment Processor) that generates rich telemetry - custom events, metrics, traces, and dependencies. This gives you real data to query and analyze.

Now comes the fun part: **writing KQL queries**. You'll use operators like `where` (filtering rows), `project` (selecting columns), `summarize` (aggregating data), `distinct` (unique values), `count` (counting rows), and `limit` (limiting results). KQL uses pipe operators (|) to chain transformations, making queries readable and composable.

You'll practice **filtering and aggregating data** - finding logs by severity level, investigating custom events, analyzing metrics over time. The `bin()` function enables time-based aggregation (group by hour, day, etc.) for trend analysis.

Then you'll **create visualizations** - line charts showing metrics over time, bar charts comparing values, and tables displaying detailed data. Finally, you'll **build comprehensive Workbooks** combining multiple queries, markdown text, and interactive visualizations into monitoring dashboards that update in real-time.

The key learning: KQL is the query language you'll use throughout Azure Monitor, whether querying Application Insights, Log Analytics, or Azure Sentinel. Mastering KQL unlocks powerful monitoring and troubleshooting capabilities.

Let's query and visualize application telemetry!
