# App Service Configuration and Administration

## Reference

App Service is Azure's platform-as-a-service offering that provides enterprise-grade features without the operational overhead of infrastructure management. The service handles all the underlying infrastructure while giving you granular control over application behavior through configuration. The documentation covers everything from basic application settings and environment variables to advanced features like health monitoring and auto-heal capabilities. The command line interface provides complete control through the az webapp config commands, which we'll be using throughout these exercises to configure monitoring and healing behaviors.

## Deploy an Application which Fails

We're starting with a practical scenario that demonstrates why monitoring matters. We have a .NET 6.0 REST API that generates random numbers, and we're going to configure it in a way that causes failures so we can see how App Service handles unhealthy applications.

**Create the Resource Group**: We're starting by creating a resource group called "labs-appservice-config" with our standard courselabs tag for tracking resources.

**Deploy with webapp up**: We're navigating to the source code directory at "src/rng/Numbers.Api" and using the webapp up command to deploy. This convenient shortcut creates both the App Service Plan and the Web App in a single operation. We're specifying a Basic B1 SKU with Linux as the operating system, .NET Core 6.0 as the runtime, and a unique DNS name for your API.

**Verify the App Service Plan**: We're checking the plan details with the show command to see its configuration. You'll see the current worker count is 1, which is the default, and the maximum worker count is 3 for this SKU tier.

**Test the Initial Deployment**: We're testing the API with curl to call the "/rng" endpoint. The first response may take a minute while the app warms up and initializes, but subsequent calls should be fast. You should see random numbers being generated successfully.

**Examine the Configuration**: The application includes configuration settings in "appsettings.json" that control its behavior. There's a setting that causes the API to fail after a certain number of calls - by default this is set high enough that you won't hit it during normal use, but we're going to override it.

**Configure Failure Behavior**: We're overriding the default configuration by setting an app setting called "Rng__FailAfter__CallCount" with the value "3". Notice the double underscore syntax - this represents a nested configuration value in .NET applications, mapping to the hierarchy Rng:FailAfter:CallCount. This override happens at the platform level without changing any source code, which is exactly what you want for environment-specific configuration.

**Trigger the Failure**: We're making repeated curl requests to the API until it fails. After the third successful call, you'll get an error message. The application is now in a failed state and won't recover on its own - it's permanently broken until something restarts it.

**Check the Health Endpoint**: The API includes a health endpoint at "/healthz" that reports whether the application is functioning correctly. We're using curl with the verbose flag to see the HTTP status code. You'll see a 500 status code indicating Internal Server Error - the health endpoint is correctly reporting that the application is unhealthy.

---

## Add an App Service Healthcheck

Now we'll configure App Service to automatically monitor this health endpoint and take action when the application becomes unhealthy.

**Navigate to Health Check**: We're opening the App Service in the Azure Portal and finding the Health check blade under the Monitoring section. This is where you configure automated health monitoring for your application.

**Enable Health Monitoring**: We're enabling the health check feature and configuring it with the path "/healthz" - this is the endpoint the platform will call periodically to verify application health. We're also reducing the load balancing threshold to the minimum value of 2 minutes, which determines how quickly unhealthy instances are removed from rotation.

**Apply Configuration**: Saving these changes triggers an automatic restart of the application to apply the new configuration. This gives us a fresh, healthy instance to work with.

**View Metrics**: We're opening the Metrics tab to create charts for HTTP response codes and health check status. These metrics give you visibility into application health over time, showing trends and patterns that help you understand behavior and detect issues early.

**Verify Healthy State**: After the restart, we're testing the health endpoint again with curl. This time you should see a 200 status code - the application is healthy and the health check is passing.

**Trigger Failure Again**: We're making several requests to generate random numbers. After three calls, the application fails again just like before. Checking the metrics in the Portal, you'll see a spike in HTTP Server Errors showing up clearly in the chart.

**Observe Single Instance Limitation**: Looking at the Overview tab, you'll see a warning that the app is unhealthy. Notice that Azure doesn't automatically restart it - this is because there's only one instance running. Azure takes a cautious approach and won't replace a single instance even when it's unhealthy, because doing so would cause downtime while the replacement instance starts. It's better to have an unhealthy instance serving some traffic than no instance at all.

---

## Scale Up the App

To enable automatic healing and high availability, we need multiple instances. With multiple instances, Azure can route traffic away from unhealthy instances while keeping healthy ones in service.

**Scale Out to Multiple Instances**: We're scaling the App Service Plan to two instances using the appservice plan update command. We're keeping the B1 SKU but changing the worker count to 2. This gives us multiple instances of the application running in parallel.

**Wait for New Instance**: It takes a few minutes for the new instance to come online and become ready. When it does, it will be healthy while the previous instance remains unhealthy from our earlier testing. App Service automatically routes all traffic to the healthy instance - the load balancer is smart enough to only send requests to instances passing their health checks.

**Verify Healthy Instance**: We're checking the health endpoint with curl. You should consistently get 200 responses from the healthy instance. The unhealthy instance is still running but receives no traffic.

**Trigger Second Failure**: We're making calls to generate random numbers again. After three calls, this instance fails too. Now both instances are unhealthy, but the most recently failed one still receives all the traffic because it's the "least unhealthy" option.

**Understand Default Behavior**: App Service will eventually restart these failed instances automatically, but by default it waits one hour before doing so. For production applications where you need quick recovery, this delay isn't acceptable.

---

## Lab

Your challenge is to configure auto-heal to restart instances immediately when they start returning errors, rather than waiting an hour.

**The Task**: Configure an auto-heal rule that triggers a restart if there are any 500-series status codes within a 30-second period. This way, failed instances are replaced quickly and your application recovers automatically from transient failures.

**Where to Configure**: You can find the auto-heal configuration in the Portal under the App Service's "Diagnose and solve problems" blade, or by searching for "Auto-heal" in the Configuration section.

**The Configuration**: You need to set up a trigger that watches for HTTP status codes in the 500 range, with a 30-second time window. The action should be to recycle the worker process - this restarts the instance cleanly.

**Test Your Configuration**: After configuring auto-heal, make requests to trigger another failure. This time, watch as the instance automatically restarts within minutes rather than waiting an hour. You'll see the application recover and become healthy again automatically.

This demonstrates how App Service can maintain high availability even when your application encounters issues - the platform actively monitors health and takes corrective action based on rules you define.

---

## Cleanup

**Delete Azure Resources**: We're removing the resource group and all its contents using az group delete. The yes flag confirms the deletion without prompting. This cleanup is important because Azure resources continue to incur charges until they're deleted, even if they're not actively serving traffic.
