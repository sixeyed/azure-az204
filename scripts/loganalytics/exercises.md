# Log Analytics - Exercise Walkthrough

## Exercise 1: Setting Up the Environment

### Creating the Resource Groups

First, we need to set up our monitoring infrastructure. We'll create two resource groups - one for the monitoring resources and another for the sample applications.

Let's create the monitoring resource group:

```
az group create -n resource-group-name -l eastus --tags courselabs=azure
```

### Creating the Log Analytics Workspace

Now we'll create the Log Analytics Workspace. This is where all our log data will be stored:

```
az monitor log-analytics workspace create -g resource-group-name -n workspace-name -l eastus
```

The workspace is the foundation of our monitoring setup. All logs and metrics will flow into this workspace.

### Creating the Application Insights Component

Next, we'll create an Application Insights component that's connected to our Log Analytics Workspace:

```
az monitor app-insights component create --app app-name --kind web -g resource-group-name --workspace workspace-name -l eastus
```

Notice how we're linking Application Insights to the Log Analytics Workspace. This integration is what allows us to query Application Insights data using KQL.

### Getting the Connection String

We need the Application Insights connection string to configure our applications:

```
az monitor app-insights component show --app app-name -g resource-group-name --query connectionString -o tsv
```

Copy this connection string - we'll use it in the next step.

### Deploying the Sample Applications

Let's create a resource group for our sample applications:

```
az group create -n apps-resource-group-name --tags courselabs=azure -l eastus
```

Now we'll deploy multiple instances of the Fulfilment Processor application. This simulates a real-world scenario with multiple application instances:

```
az container create -g apps-resource-group-name --image courselabs/fulfilment-processor:appinsights-1.0 --no-wait --name container-name-1 --secure-environment-variables "ApplicationInsights__ConnectionString=connection-string-value"
```

We'll deploy several instances using different versions. This will generate varied telemetry data that we can analyze.

Give the containers a few minutes to start up and begin generating logs. You'll want plenty of data to work with for the queries we'll write.

## Exercise 2: Exploring the Query Interface

### Navigating to Log Analytics

In the Azure Portal, navigate to your Log Analytics Workspace. Click on the Logs view to open the KQL query editor.

You'll see a pop-up with sample queries. These are generic templates, so let's close that and explore the actual data.

### Understanding the Tables View

On the left side, switch from the Queries view to the Tables view. This shows the actual data tables in your workspace.

Expand the LogManagement section. You'll see many tables that are populated from Application Insights:
- AppEvents - Custom events tracked by your application
- AppDependencies - External calls made by your application
- AppTraces - Log entries written by your application
- AppMetrics - Custom metrics reported by your application

These tables represent the same data you see in Application Insights, but now you can query it directly with KQL.

### Your First KQL Queries

The simplest KQL query is just the table name. Try this:

```
AppTraces
```

This returns all trace entries. You'll see columns like TimeGenerated, Message, SeverityLevel, and more.

Let's try a few more basic queries:

```
AppTraces
| limit 100
```

This returns just the first 100 entries. The pipe character is how you chain operations in KQL.

```
AppMetrics
| order by TimeGenerated desc
| limit 10
```

Here we're ordering by the most recent entries first, then limiting to 10 results.

## Exercise 3: Querying Application Logs

### Understanding Log Severity

Let's explore what severity levels exist in our logs:

```
AppTraces
| distinct SeverityLevel
```

The distinct operator gives us the unique values. You might see severity levels 0 through 3.

Now let's count how many logs we have for each severity:

```
AppTraces
| summarize LogsBySeverity = count() by(SeverityLevel)
```

The summarize operator is powerful - it aggregates data. Here we're counting rows and grouping by severity level.

### Filtering and Projecting Data

Let's find logs for a specific severity level and show only the fields we care about:

```
AppTraces
| where SeverityLevel == 3
| project Message, AppRoleName, AppRoleInstance
```

The where clause filters rows. The project clause selects which columns to display. This is similar to SELECT in SQL, but the syntax is different.

### Combining Filters

We can combine multiple conditions. Let's find error logs with a specific error code:

```
AppTraces
| where SeverityLevel == 3
| where Message contains "302"
| count
```

This tells us how many severity 3 logs contain the error code 302.

### Analyzing Events by Instance

Now let's look at custom events. We want to see if one application instance is having more failures than others:

```
AppEvents
| where Name == "Fulfilment.Failed"
| summarize FailureCount = count() by AppRoleInstance
| order by FailureCount desc
```

This query filters to the specific event type, counts occurrences per instance, and sorts by count. You can quickly identify if one instance is problematic.

## Exercise 4: Aggregating Application Metrics

### Exploring the Metrics Table

Let's see how many metric entries we have:

```
AppMetrics
| count
```

Now let's look at a sample of the data:

```
AppMetrics
| limit 10
```

You'll see columns like Name, Sum, Count, Min, Max. These represent the metric values reported by the application.

### Calculating Averages

Let's calculate the average queue size across all time:

```
AppMetrics
| where Name == "QueueSize"
| summarize AvgQueueLength = avg(Sum)
```

This gives us a single number, but it's not very useful without context.

### Time-Based Aggregation

What we really want is to see how the queue size changes over time. We can use the bin function to group by time intervals:

```
AppMetrics
| where Name == "QueueSize"
| summarize AvgQueueSize = avg(Sum) by bin(TimeGenerated, 10m)
| order by TimeGenerated asc
```

The bin function groups timestamps into 10-minute intervals. Now we can see trends over time.

### Visualizing the Data

KQL queries aren't just for tables. Click the Chart button above the results. Try different visualization types:
- Line chart - Great for showing trends over time
- Bar chart - Good for comparing values across categories
- Pie chart - Useful for showing proportions

The line chart works particularly well for our time-series queue size data. You can see spikes, trends, and patterns much more easily than in a table.

## Exercise 5: Lab Challenge - Building a Workbook

### Understanding Workbooks

Workbooks in Azure are like interactive dashboards. They combine multiple KQL queries, text, and visualizations into a cohesive monitoring view.

The Workbook editor takes some getting used to, but it's powerful once you understand it.

### Creating the Workbook

Navigate to Workbooks in your Log Analytics Workspace and create a new workbook.

### Adding the Instances Table

First, let's add a query that shows all running instances:

```
AppTraces
| where TimeGenerated > ago(5m)
| distinct AppRoleName, AppRoleInstance
| order by AppRoleName, AppRoleInstance
```

This shows instances that have logged something in the last 5 minutes, effectively showing active instances.

Add this as a query block in your workbook and format it as a table.

### Adding the Failure Breakdown

Next, we want to see failures by instance:

```
AppEvents
| where Name == "Fulfilment.Failed"
| where TimeGenerated > ago(1h)
| summarize FailureCount = count() by AppRoleInstance
| order by FailureCount desc
```

Add this query and visualize it as a bar chart. This makes it easy to spot problematic instances at a glance.

### Adding the Queue Size Graph

Finally, let's add the queue size trend:

```
AppMetrics
| where Name == "QueueSize"
| where TimeGenerated > ago(1h)
| summarize AvgQueueSize = avg(Sum) by bin(TimeGenerated, 10m)
| order by TimeGenerated asc
```

Visualize this as a line chart. This shows you how the queue is trending - growing, shrinking, or staying stable.

### Organizing the Workbook

Add text blocks to label each section. You can add parameters to make the workbook interactive - for example, a time range picker.

Save your workbook with a descriptive name. You can pin it to your dashboard for quick access.

### Using the Workbook

Now you have a single pane of glass for monitoring your Fulfilment Processor application. You can:
- See which instances are running
- Identify instances with high failure rates
- Monitor queue size trends

This is the kind of monitoring that's valuable in production environments.

## Cleanup

When you're done with the lab, remember to clean up your resources:

```
az group delete -y --no-wait -n apps-resource-group-name

az group delete -y --no-wait -n resource-group-name
```

This deletes the resource groups and all contained resources. The --no-wait flag returns immediately without waiting for completion.

## Summary

In this lab, you've learned:
- How to set up Log Analytics with Application Insights
- The basics of KQL syntax and common operations
- How to query logs, events, and metrics
- How to aggregate data and create visualizations
- How to build a practical monitoring Workbook

These skills are fundamental for monitoring Azure applications and troubleshooting issues in production.
