# App Service Configuration and Administration

## Reference

App Service is a PaaS which gives you features that would take a lot of effort to implement with an IaaS deployment. Your applications will need different configuration settings and App Service lets you set them without manually logging in and editing files. App Service is also able to monitor your application health, restarting instances which are unhealthy.

## Deploy an Application which Fails

Let's start by deploying our application. We're using a .NET 6.0 REST API that generates random numbers.

First, we'll create a resource group for this lab with our standard courselabs tag for tracking.

Now we'll use the webapp up command to deploy our application. This is a convenient shortcut that creates both the App Service Plan and the Web App in one step.

We need to navigate to the source code directory first at "src/rng/Numbers.Api".

Then we're deploying the application using webapp up. We're specifying the resource group name, the App Service Plan name, Linux as the operating system, the B1 SKU for the plan, .NET Core 6.0 as the runtime, and a unique DNS name for the app.

We're using the B1 SKU, which is a Basic tier plan suitable for development and testing. Let's verify the App Service Plan details using the show command to examine its configuration.

You'll see the current worker count is 1, which is the default, and the maximum worker count is 3 for the B1 tier.

Let's test our API using curl to call the "/rng" endpoint. The first response may take a minute while the app warms up - this is normal as the application initializes - but subsequent calls should be fast. You should get a random number back.

Now, let's look at the application's configuration. The app has a setting called "FailAfter__CallCount" in the appsettings.json file. By default, this is set high enough that the app won't fail during normal use. But we're going to override this to make it fail after just 3 calls so we can demonstrate health monitoring.

Let's set an app setting that will cause our API to fail after 3 requests. We're using the config appsettings set command with a setting named "Rng__FailAfter__CallCount" set to the value "3".

Notice the syntax here. The double underscore represents a nested configuration value in .NET - it maps to Rng:FailAfter:CallCount in the application's configuration hierarchy. This overrides the default configuration without changing the source code, which is exactly what you want for environment-specific settings.

Now let's test the API again. We're making several requests using curl to call the "/rng" endpoint.

After the third call, you'll get an error message. The app is now in a failed state because we configured it to fail after 3 calls.

The API includes a health endpoint at "/healthz". Let's check it with the verbose flag to see the HTTP status code. We're using curl with the -v flag to see the full HTTP response headers.

You'll see a 500 status code - Internal Server Error. This indicates the app is unhealthy. The health endpoint is reporting that something is wrong with the application.

## Add an App Service Healthcheck

Now we'll configure App Service to monitor this health endpoint automatically. Opening the Azure Portal and navigating to your App Service, we're finding the Health check blade under the Monitoring section.

We're enabling the health check and configuring it by setting the path to "/healthz" and reducing the load balancing threshold to the minimum value, which is 2 minutes. This threshold determines how long an unhealthy instance stays in rotation before being replaced.

Saving the changes triggers an app restart to apply the new configuration.

After the restart, you have a fresh, healthy instance. Let's verify using curl with the verbose flag to check the health endpoint.

This time you should see a 200 status code - the app is healthy again.

Let's open the Metrics tab in the Portal. Here we're creating charts for HTTP response codes and health check status. This gives you visibility into your application's health over time - you can see trends and patterns that help you understand application behavior.

Now we're making some requests to get random numbers again using curl. After three calls, the app fails again. Checking the metrics in the Portal, you'll see a spike in HTTP Server Errors - the 500 responses show up clearly in the chart.

In the Overview tab, you'll see a warning that the app is unhealthy. But notice that Azure won't restart it automatically. That's because there's only one instance. Azure takes a cautious approach - it won't replace a single instance even if it's unhealthy, because that would cause downtime while the new instance starts. Better to have an unhealthy instance than no instance at all.

## Exercise 4: Scale Out and Auto-Heal

To enable automatic healing, we need multiple instances. Let's scale out to two instances using the appservice plan update command. We're setting the SKU to B1 and the worker count to 2.

It takes a few minutes for the new instance to come online and become ready to serve traffic. When it does, it will be healthy while the old instance remains unhealthy. App Service automatically routes all traffic to the healthy instance - this is the load balancer doing its job.

Checking the health endpoint using curl, you should get a 200 response from the healthy instance. The load balancer is smart enough to only send requests to instances that are passing their health checks.

Now we're making some calls to get random numbers using curl. After three calls, this instance fails too. Now both instances are unhealthy, but the most recently failed one still receives all the traffic because it's the "least unhealthy" option.

App Service will eventually restart these failed instances, but by default it waits one hour. That's not ideal for production applications where you want quick recovery.

## Lab Challenge: Configure Auto-Heal

Your challenge is to configure auto-heal to restart instances immediately when they start returning 500 errors.

The goal is to set up a rule that triggers a restart if there are any 500 errors within a 30-second period. This way, failed instances are replaced quickly rather than waiting an hour.

You can find the auto-heal configuration in the Portal under the App Service's Diagnose and solve problems blade, or by searching for "Auto-heal" in the Configuration section.

We're configuring the trigger to watch for status codes in the 500 range, with a 30-second time window. We're setting the action to restart the instance.

Once configured, testing it by making requests until the instance fails, then watching as it automatically restarts and becomes healthy again within minutes rather than an hour.

This demonstrates how App Service can maintain high availability even when your application encounters issues - the platform actively monitors and recovers from failures.
