# Log Analytics - Exercise Walkthrough

## Setting Up the Environment

### Creating the Resource Groups

First, we need to set up our monitoring infrastructure. We'll create two resource groups - one for the monitoring resources and another for the sample applications.

Let's create the monitoring resource group using az group create with a name, location set to eastus, and the courselabs equals azure tag. This resource group will house our Log Analytics workspace and Application Insights component.

### Creating the Log Analytics Workspace

Now we'll create the Log Analytics Workspace. This is where all our log data will be stored. We're running az monitor log-analytics workspace create with our resource group name, workspace name, and location.

The workspace is the foundation of our monitoring setup. All logs and metrics will flow into this workspace, giving us a centralized location for querying and analyzing telemetry data.

### Creating the Application Insights Component

Next, we'll create an Application Insights component that's connected to our Log Analytics Workspace. We're using az monitor app-insights component create with the app name, kind set to web, resource group, workspace name, and location.

Notice how we're linking Application Insights to the Log Analytics Workspace. This integration is what allows us to query Application Insights data using KQL - Kusto Query Language - which is incredibly powerful for analyzing logs and metrics.

### Getting the Connection String

We need the Application Insights connection string to configure our applications. We're running az monitor app-insights component show with a query parameter to extract just the connectionString field and output format set to tsv.

Copy this connection string - we'll use it in the next step to configure our sample applications.

### Deploying the Sample Applications

Let's create a resource group for our sample applications using az group create with the apps resource group name, courselabs tag, and location.

Now we'll deploy multiple instances of the Fulfilment Processor application. This simulates a real-world scenario with multiple application instances. We're using az container create with the fulfilment-processor image tagged as appinsights-1.0, running in the background with the --no-wait flag, and passing the Application Insights connection string as a secure environment variable.

We'll deploy several instances using different versions. This will generate varied telemetry data that we can analyze - some instances might be running version 1.0, others might be on 1.1 or 1.2, giving us realistic diversity in our logs.

Give the containers a few minutes to start up and begin generating logs. You'll want plenty of data to work with for the queries we'll write.

---

## Exploring the Query Interface

### Navigating to Log Analytics

In the Azure Portal, we're navigating to the Log Analytics Workspace. Clicking on the Logs view opens the KQL query editor.

You'll see a pop-up with sample queries. These are generic templates, so let's close that and explore the actual data from our applications.

### Understanding the Tables View

On the left side, we're switching from the Queries view to the Tables view. This shows the actual data tables in your workspace.

Expanding the LogManagement section, you'll see many tables that are populated from Application Insights. AppEvents contains custom events tracked by your application. AppDependencies shows external calls made by your application - like database queries or HTTP requests to other services. AppTraces holds log entries written by your application code. And AppMetrics contains custom metrics reported by your application.

These tables represent the same data you see in Application Insights, but now you can query it directly with KQL, which gives you much more flexibility and power than the standard Application Insights interface.

### Your First KQL Queries

The simplest KQL query is just the table name. Let's try AppTraces. This returns all trace entries. You'll see columns like TimeGenerated, Message, SeverityLevel, and more - all the contextual information about each log entry.

Let's try a few more basic queries. Running AppTraces pipe limit 100 returns just the first 100 entries. The pipe character is how you chain operations in KQL - it's like the Unix pipe, passing results from one operation to the next.

Now let's try AppMetrics pipe order by TimeGenerated desc pipe limit 10. Here we're ordering by the most recent entries first, then limiting to 10 results. This shows you the latest metrics that were reported.

---

## Querying Application Logs

### Understanding Log Severity

Let's explore what severity levels exist in our logs. We're running AppTraces pipe distinct SeverityLevel. The distinct operator gives us the unique values. You might see severity levels 0 through 3, representing different log levels like Verbose, Information, Warning, and Error.

Now let's count how many logs we have for each severity using AppTraces pipe summarize LogsBySeverity equals count grouped by SeverityLevel.

The summarize operator is powerful - it aggregates data. Here we're counting rows and grouping by severity level, which gives us a breakdown of how many logs exist at each level. This helps you understand the overall health of your application - lots of errors might indicate problems.

### Filtering and Projecting Data

Let's find logs for a specific severity level and show only the fields we care about. We're running AppTraces pipe where SeverityLevel equals 3 pipe project Message, AppRoleName, AppRoleInstance.

The where clause filters rows - only severity level 3 logs pass through. The project clause selects which columns to display. This is similar to SELECT in SQL, but the syntax is different - you're projecting specific columns from the filtered results.

### Combining Filters

We can combine multiple conditions. Let's find error logs with a specific error code. Running AppTraces pipe where SeverityLevel equals 3 pipe where Message contains "302" pipe count.

This tells us how many severity 3 logs contain the error code 302. You're filtering first by severity, then by message content, then counting the results. This kind of drilling down is essential for troubleshooting specific issues.

### Analyzing Events by Instance

Now let's look at custom events. We want to see if one application instance is having more failures than others. We're running AppEvents pipe where Name equals "Fulfilment.Failed" pipe summarize FailureCount equals count grouped by AppRoleInstance pipe order by FailureCount desc.

This query filters to the specific event type "Fulfilment.Failed", counts occurrences per instance, and sorts by count descending. You can quickly identify if one instance is problematic - maybe it's running a buggy version or has bad configuration.

---

## Aggregating Application Metrics

### Exploring the Metrics Table

Let's see how many metric entries we have by running AppMetrics pipe count. This gives you an idea of the volume of metrics data.

Now let's look at a sample of the data with AppMetrics pipe limit 10. You'll see columns like Name, Sum, Count, Min, Max. These represent the metric values reported by the application - Sum is the total value, Count is how many times it was recorded, Min and Max show the range.

### Calculating Averages

Let's calculate the average queue size across all time. We're running AppMetrics pipe where Name equals "QueueSize" pipe summarize AvgQueueLength equals avg of Sum.

This gives us a single number, but it's not very useful without context. An average across all time doesn't show you trends or variations.

### Time-Based Aggregation

What we really want is to see how the queue size changes over time. We can use the bin function to group by time intervals. Running AppMetrics pipe where Name equals "QueueSize" pipe summarize AvgQueueSize equals avg of Sum by bin of TimeGenerated, 10 minutes pipe order by TimeGenerated ascending.

The bin function groups timestamps into 10-minute intervals. Now we can see trends over time - is the queue growing? Shrinking? Staying stable? This time-series view is much more actionable than a single average.

### Visualizing the Data

KQL queries aren't just for tables. We're clicking the Chart button above the results. Try different visualization types - line charts are great for showing trends over time, bar charts are good for comparing values across categories, and pie charts are useful for showing proportions.

The line chart works particularly well for our time-series queue size data. You can see spikes, trends, and patterns much more easily than in a table. This visual feedback makes it obvious when something unusual is happening.

---

## Lab Challenge - Building a Workbook

### Understanding Workbooks

Workbooks in Azure are like interactive dashboards. They combine multiple KQL queries, text, and visualizations into a cohesive monitoring view.

The Workbook editor takes some getting used to, but it's powerful once you understand it. You can create rich monitoring experiences that bring together different data sources and perspectives.

### Creating the Workbook

We're navigating to Workbooks in the Log Analytics Workspace and creating a new workbook.

### Adding the Instances Table

First, let's add a query that shows all running instances. We're adding AppTraces pipe where TimeGenerated greater than ago of 5 minutes pipe distinct AppRoleName, AppRoleInstance pipe order by AppRoleName, AppRoleInstance.

This shows instances that have logged something in the last 5 minutes, effectively showing active instances. We're adding this as a query block in the workbook and formatting it as a table.

### Adding the Failure Breakdown

Next, we want to see failures by instance. We're adding AppEvents pipe where Name equals "Fulfilment.Failed" pipe where TimeGenerated greater than ago of 1 hour pipe summarize FailureCount equals count by AppRoleInstance pipe order by FailureCount desc.

We're adding this query and visualizing it as a bar chart. This makes it easy to spot problematic instances at a glance - the tallest bar is the instance with the most failures.

### Adding the Queue Size Graph

Finally, let's add the queue size trend. We're adding AppMetrics pipe where Name equals "QueueSize" pipe where TimeGenerated greater than ago of 1 hour pipe summarize AvgQueueSize equals avg of Sum by bin of TimeGenerated, 10 minutes pipe order by TimeGenerated ascending.

We're visualizing this as a line chart. This shows you how the queue is trending - growing, shrinking, or staying stable. If the queue is growing continuously, that might indicate your workers can't keep up with the incoming workload.

### Organizing the Workbook

We're adding text blocks to label each section. You can add parameters to make the workbook interactive - for example, a time range picker that lets users adjust the time window for all queries at once.

We're saving the workbook with a descriptive name. You can pin it to your dashboard for quick access.

### Using the Workbook

Now you have a single pane of glass for monitoring your Fulfilment Processor application. You can see which instances are running, identify instances with high failure rates, and monitor queue size trends.

This is the kind of monitoring that's valuable in production environments - actionable insights at a glance.

---

## Cleanup

When you're done with the lab, remember to clean up your resources. We're running az group delete with the -y flag to skip confirmation and --no-wait to return immediately, for both the apps resource group and the monitoring resource group.

This deletes the resource groups and all contained resources. The --no-wait flag returns immediately without waiting for completion - the deletion continues in the background.

---

## Reference

- [Azure documentation](https://docs.microsoft.com/azure/)

## Summary

In this lab, you've learned how to set up Log Analytics with Application Insights, the basics of KQL syntax and common operations, how to query logs, events, and metrics, how to aggregate data and create visualizations, and how to build a practical monitoring Workbook.

These skills are fundamental for monitoring Azure applications and troubleshooting issues in production.
