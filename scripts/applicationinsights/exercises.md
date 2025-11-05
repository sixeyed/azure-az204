# Application Insights - Exercises Walkthrough

## Exercise 1: Creating Application Insights

Let's start by creating our Application Insights resource. We'll do this using the Azure CLI.

First, we'll create a resource group to hold our monitoring infrastructure in the East US region with our standard courselabs tag for tracking purposes.

Now, when you create Application Insights, you have a choice between two modes: Classic and Workspace-based. The Classic mode uses Application Insights' own storage, while Workspace mode stores data in a Log Analytics Workspace. Workspace mode is the modern approach because it allows you to store data from multiple sources in one place and query across all of them - this is incredibly powerful for correlation and troubleshooting.

Let's create a Log Analytics Workspace first. We're creating the workspace in our resource group, giving it a unique name, and deploying to East US.

Now we can create the Application Insights instance linked to this workspace. We're specifying the application name, setting the kind to "web" since we'll be monitoring web applications, associating it with our resource group and the Log Analytics Workspace we just created, and deploying to East US.

Great! Now if you browse to Application Insights in the Portal, you'll see lots of interesting features like Application Map, Live Metrics, and Failures. But they won't show anything yet because we don't have any applications sending data. Let's fix that.

## Exercise 2: Deploy App with Custom Application Insights

Now we're going to deploy an application that uses the Application Insights SDK directly. This is a fulfillment processor application that explicitly tracks operations, events, and dependencies using custom code.

First, we need to get the connection string for our Application Insights instance. We're using the az monitor app-insights component show command with a query parameter to extract just the connection string, outputting it as plain text.

This will output a connection string that contains an instrumentation key and an ingestion endpoint URL. This is what the application uses to send telemetry data to Application Insights.

We'll use this to configure our applications. Let's create a separate resource group for the applications to keep our infrastructure organized - one group for monitoring, another for the apps being monitored.

Now we'll deploy multiple container instances. We're deploying different versions to simulate a real-world scenario where you might have multiple versions running during a rollout. We're creating container instances with the fulfilment-processor image, using the no-wait flag to deploy in the background, giving each a unique name, and passing the Application Insights connection string as a secure environment variable so it's not visible in the resource properties.

We're repeating this command for additional containers, including one running a different version of the application. This demonstrates how Application Insights can track multiple instances and versions simultaneously.

These containers will start publishing telemetry to Application Insights within a few minutes. Let's explore what we can see.

Heading back to Application Insights in the Portal and opening the Live Metrics view, you can see real-time data flowing from your applications - requests per second, response times, failures, and custom metrics. It's incredibly useful for monitoring deployments or troubleshooting issues in real-time. You're watching your application's heartbeat.

Next, checking out the Application Map view, this shows you all the components of your application and their dependencies. You can see how the fulfillment processor calls external services and the success rates for those calls. This visual representation makes it easy to spot problem areas.

In the Performance view, you can analyze how long different operations take. For example, you can see the average time to process a batch and identify performance bottlenecks. This helps you understand where to focus your optimization efforts.

This approach gives you complete control over what telemetry is collected, but it requires writing custom code. For standard web applications, there's an easier way.

## Exercise 3: Add Application Insights to a Web App

Now we're going to deploy a web application and enable Application Insights using auto-instrumentation. This is a .NET web application called the Random Number Generator. The code has standard logging but no Application Insights integration.

Let's deploy it to App Service using the webapp up command. We're specifying the resource group, the App Service Plan name, Linux operating system, .NET Core 6.0 runtime, West US location, and a unique web app name.

Once deployed, you can browse to the application. It has a home page, but if you try to get a random number, it will fail because the backend API isn't running yet. That's okay - we'll fix that in a moment.

Now here's where the magic happens. Opening your Web App in the Portal and browsing to the Application Insights section, we're clicking "Turn on Application Insights". We're selecting "Select existing resource" and choosing your Application Insights instance, then under "Instrument your application", selecting .NET Core as the runtime, and clicking Apply.

That's it! No code changes required. Azure will automatically start collecting telemetry from your web application - HTTP requests, dependencies, exceptions, performance counters, everything.

Browsing the application and refreshing a few times, try to get a random number - remember, it will fail because we haven't deployed the API yet. Now going back to Application Insights and opening the Failures view, filtering by your web app's role name, you'll see the failed dependency call to the API.

Clicking on a failure to open the End-to-end transaction details, this is incredibly powerful. You can see what happened before and after the failure, the complete timeline for this user, and drill down into error logs. All of this without writing a single line of monitoring code.

## Exercise 4: Add the REST API to Application Insights

To fix our application, we need to deploy the backend API. Let's deploy it to the same App Service Plan using webapp up, specifying the same plan name to share infrastructure, with the same runtime and region, but a different unique name for the API.

Just like we did for the web app, we're opening the API in the Portal and enabling Application Insights using the same Application Insights instance. This ensures all components report to the same monitoring destination.

Now we need to configure the web app to use the API. Opening the web app in the Portal and adding application settings in the Configuration section, we're setting "RngApi__Url" to the full URL of the API's rng endpoint. The double underscore syntax maps to nested configuration in .NET Core.

We're also adding a second setting, "APPINSIGHTS_JAVASCRIPT_ENABLED" set to "true". This setting is particularly interesting - it enables client-side telemetry collection from the browser, giving you insights into the user's experience, not just the server's perspective.

Saving the settings triggers a web app restart to pick up the new configuration.

Now trying the application again, getting a few random numbers, and then exploring Application Insights, you'll see a complete picture of your distributed application.

Opening User Flows and searching for the GET /rng event, you can see the complete user journey through your application - from the initial page load, through the button click, to the API call, and back to the response.

In the Metrics section, you'll find browser metrics showing client-side performance like page load times and AJAX call durations, server metrics showing response times and request rates, and custom metrics from the fulfillment processor showing application-specific data like queue sizes.

If you open developer tools in your browser and look at the network traffic, you'll see that the page is now making track calls to Application Insights. These send client-side performance data including page load times and user interactions - data you wouldn't normally have access to from the server side.

## Lab Exercise

Here's a challenge for you. Azure Functions also has automatic instrumentation. By default, when you create a Functions App, Azure creates a separate Application Insights instance for each one. In this lab, we created a single Application Insights instance and used it for multiple components.

Think about the tradeoffs: What are the benefits of having separate Application Insights instances per component? When would you want to use a shared instance like we did?

Consider aspects like cost and resource management - more instances mean more billing entities to manage. Think about cross-component correlation and analysis - with a shared instance, you can trace requests across all your services in one place. Consider access control and separation of concerns - separate instances might be better when different teams own different components. And think about query complexity - is it easier to filter one large dataset or query multiple smaller ones?

Take some time to think through these scenarios and experiment with the setup.

## Cleanup

When you're finished, you can delete the resource group containing the applications using the group delete command with the -y flag to skip confirmation and the --no-wait flag to return immediately.

If you're moving on to the Log Analytics lab next, keep the Application Insights resource group since it includes the Log Analytics Workspace. Otherwise, you can delete that too using the same approach.

That wraps up our Application Insights exercises. You've learned how to integrate monitoring both with custom code and auto-instrumentation, and explored the powerful analysis tools available in Application Insights.
