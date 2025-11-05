# Application Insights - Exercises Introduction

We've covered Application Insights as Azure's comprehensive monitoring solution that acts as your application's flight recorder. Now let's implement monitoring for a distributed application.

## What You'll Do

You'll start by **creating a workspace-based Application Insights instance** linked to Log Analytics. This modern architecture stores all telemetry in Log Analytics, enabling queries across Azure Dashboards, Log Analytics, and the Application Insights interface from the same dataset.

Then you'll **deploy a fulfillment processor container** with custom Application Insights SDK integration. This demonstrates manual instrumentation where your code explicitly tracks operations, events, and dependencies. You'll see custom telemetry appear in real-time as the application processes requests.

Next comes **deploying a .NET web app** using App Service's built-in auto-instrumentation. Here's the magic: you enable monitoring through the Portal with one click - no code changes required! App Service automatically injects the Application Insights SDK and starts collecting telemetry.

You'll also **deploy a REST API** and configure both components to use the same Application Insights instance. By enabling **client-side telemetry** with `APPINSIGHTS_JAVASCRIPT_ENABLED`, you'll capture browser-side page views and user interactions, giving you the complete picture from browser to backend.

Now the exploration begins: **Live Metrics** shows real-time requests, dependencies, and exceptions as they happen. **Application Map** visualizes your distributed system with components and their dependencies. **Performance views** identify bottlenecks showing operation duration. **User Flows** reveal how users navigate through your application. And **End-to-end transaction details** let you trace a single request across all components, seeing exactly where time was spent.

Let's implement comprehensive monitoring for distributed applications!
