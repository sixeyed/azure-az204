# Application Insights - Exercises Walkthrough

## Exercise 1: Creating Application Insights

Let's start by creating our Application Insights resource. We'll do this using the Azure CLI.

First, we'll create a resource group to hold our monitoring infrastructure:

```
az group create -n [YOUR-RESOURCE-GROUP] -l eastus --tags courselabs=azure
```

Now, when you create Application Insights, you have a choice between two modes: Classic and Workspace-based. The Classic mode uses Application Insights' own storage, while Workspace mode stores data in a Log Analytics Workspace. Workspace mode is the modern approach because it allows you to store data from multiple sources in one place and query across all of them.

Let's create a Log Analytics Workspace first:

```
az monitor log-analytics workspace create -g [YOUR-RESOURCE-GROUP] -n [YOUR-WORKSPACE-NAME] -l eastus
```

Now we can create the Application Insights instance linked to this workspace:

```
az monitor app-insights component create --app [YOUR-APP-INSIGHTS-NAME] --kind web -g [YOUR-RESOURCE-GROUP] --workspace [YOUR-WORKSPACE-NAME] -l eastus
```

Great! Now if you browse to Application Insights in the Portal, you'll see lots of interesting features like Application Map, Live Metrics, and Failures. But they won't show anything yet because we don't have any applications sending data. Let's fix that.

## Exercise 2: Deploy App with Custom Application Insights

Now we're going to deploy an application that uses the Application Insights SDK directly. This is a fulfillment processor application that explicitly tracks operations, events, and dependencies using custom code.

First, we need to get the connection string for our Application Insights instance:

```
az monitor app-insights component show --app [YOUR-APP-INSIGHTS-NAME] -g [YOUR-RESOURCE-GROUP] --query connectionString -o tsv
```

This will output a connection string that looks like: `InstrumentationKey=[GUID];IngestionEndpoint=https://[REGION].in.applicationinsights.azure.com/`

We'll use this to configure our applications. Let's create a separate resource group for the applications:

```
az group create -n [YOUR-APPS-RESOURCE-GROUP] --tags courselabs=azure -l eastus
```

Now we'll deploy multiple container instances. We're deploying different versions to simulate a real-world scenario where you might have multiple versions running:

```
az container create -g [YOUR-APPS-RESOURCE-GROUP] --image courselabs/fulfilment-processor:appinsights-1.0 --no-wait --name [CONTAINER-1] --secure-environment-variables "ApplicationInsights__ConnectionString=[YOUR-CONNECTION-STRING]"
```

We'll repeat this command for additional containers, including one running a different version of the application.

These containers will start publishing telemetry to Application Insights within a few minutes. Let's explore what we can see.

Head back to Application Insights in the Portal and open the Live Metrics view. Here you can see real-time data flowing from your applications - requests per second, response times, failures, and custom metrics. It's incredibly useful for monitoring deployments or troubleshooting issues in real-time.

Next, check out the Application Map view. This shows you all the components of your application and their dependencies. You can see how the fulfillment processor calls external services and the success rates for those calls.

In the Performance view, you can analyze how long different operations take. For example, you can see the average time to process a batch and identify performance bottlenecks.

This approach gives you complete control over what telemetry is collected, but it requires writing custom code. For standard web applications, there's an easier way.

## Exercise 3: Add Application Insights to a Web App

Now we're going to deploy a web application and enable Application Insights using auto-instrumentation. This is a .NET web application called the Random Number Generator. The code has standard logging but no Application Insights integration.

Let's deploy it to App Service:

```
az webapp up -g [YOUR-APPS-RESOURCE-GROUP] --plan [YOUR-APP-SERVICE-PLAN] --os-type Linux --runtime dotnetcore:6.0 -l westus -n [YOUR-WEB-APP-NAME]
```

Once deployed, you can browse to the application. It has a home page, but if you try to get a random number, it will fail because the backend API isn't running yet.

Now here's where the magic happens. Open your Web App in the Portal and browse to the Application Insights section. Click "Turn on Application Insights":

- Select "Select existing resource" and choose your Application Insights instance
- Under "Instrument your application", select .NET Core as the runtime
- Click Apply

That's it! No code changes required. Azure will automatically start collecting telemetry from your web application.

Browse the application and refresh a few times. Try to get a random number - remember, it will fail because we haven't deployed the API yet. Now go back to Application Insights.

Open the Failures view and filter by your web app's role name. You'll see the failed dependency call to the API. Click on a failure to open the End-to-end transaction details. This is incredibly powerful - you can see:

- What happened before and after the failure
- The complete timeline for this user
- Drill down into error logs

All of this without writing a single line of monitoring code.

## Exercise 4: Add the REST API to Application Insights

To fix our application, we need to deploy the backend API. Let's deploy it to the same App Service Plan:

```
az webapp up -g [YOUR-APPS-RESOURCE-GROUP] --plan [YOUR-APP-SERVICE-PLAN] --os-type Linux --runtime dotnetcore:6.0 -l westus -n [YOUR-API-NAME]
```

Just like we did for the web app, open the API in the Portal and enable Application Insights using the same Application Insights instance.

Now we need to configure the web app to use the API. Open the web app in the Portal and add these application settings in the Configuration section:

- Key: `RngApi__Url` Value: `https://[YOUR-API-NAME].azurewebsites.net/rng`
- Key: `APPINSIGHTS_JAVASCRIPT_ENABLED` Value: `true`

Save the settings and the web app will restart. That second setting is particularly interesting - it enables client-side telemetry collection from the browser.

Now try the application again. Get a few random numbers and then explore Application Insights:

Open User Flows and search for the GET /rng event. You can see the complete user journey through your application.

In the Metrics section, you'll find:
- Browser metrics showing client-side performance
- Server metrics showing response times and request rates
- Custom metrics from the fulfillment processor showing queue sizes

If you open developer tools in your browser and look at the network traffic, you'll see that the page is now making track calls to Application Insights. These send client-side performance data including page load times and user interactions.

## Lab Exercise

Here's a challenge for you. Azure Functions also has automatic instrumentation. By default, when you create a Functions App, Azure creates a separate Application Insights instance for each one. In this lab, we created a single Application Insights instance and used it for multiple components.

Think about the tradeoffs: What are the benefits of having separate Application Insights instances per component? When would you want to use a shared instance like we did? Consider aspects like:

- Cost and resource management
- Cross-component correlation and analysis
- Access control and separation of concerns
- Query complexity

Take some time to think through these scenarios and experiment with the setup.

## Cleanup

When you're finished, you can delete the resource group containing the applications:

```
az group delete -y --no-wait -n [YOUR-APPS-RESOURCE-GROUP]
```

If you're moving on to the Log Analytics lab next, keep the Application Insights resource group. Otherwise, you can delete that too:

```
az group delete -y --no-wait -n [YOUR-RESOURCE-GROUP]
```

That wraps up our Application Insights exercises. You've learned how to integrate monitoring both with custom code and auto-instrumentation, and explored the powerful analysis tools available in Application Insights.
