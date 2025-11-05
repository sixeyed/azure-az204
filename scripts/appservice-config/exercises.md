# App Service Configuration and Administration - Exercises

## Exercise 1: Deploy an Application with Configuration

Let's start by deploying our application. We're using a .NET 6.0 REST API that generates random numbers.

First, we'll create a resource group for this lab:

```bash
az group create -n [RESOURCE-GROUP-NAME] --tags courselabs=azure
```

Now we'll use the `webapp up` command to deploy our application. This is a convenient shortcut that creates both the App Service Plan and the Web App in one step.

We need to navigate to the source code directory first:

```bash
cd src/rng/Numbers.Api
```

Then deploy the application:

```bash
az webapp up -g [RESOURCE-GROUP-NAME] --plan [APP-PLAN-NAME] --os-type Linux --sku B1 --runtime dotnetcore:6.0 -n [APP-DNS-NAME]
```

We're using the B1 SKU, which is a Basic tier plan. Let's verify the App Service Plan details:

```bash
az appservice plan show -g [RESOURCE-GROUP-NAME] -n [APP-PLAN-NAME]
```

You'll see the current worker count is 1, which is the default, and the maximum worker count is 3.

Let's test our API:

```bash
curl https://[APP-FQDN]/rng
```

The first response may take a minute while the app warms up, but subsequent calls should be fast. You should get a random number back.

Now, let's look at the application's configuration. The app has a setting called `FailAfter__CallCount` in the appsettings.json file. By default, this is set high enough that the app won't fail during normal use. But we're going to override this to make it fail after just 3 calls.

## Exercise 2: Configure App Settings

Let's set an app setting that will cause our API to fail after 3 requests:

```bash
az webapp config appsettings set --settings Rng__FailAfter__CallCount='3' -g [RESOURCE-GROUP-NAME] -n [APP-DNS-NAME]
```

Notice the syntax here. The double underscore represents a nested configuration value in .NET. This overrides the default configuration without changing the source code.

Now let's test the API again. Make several requests:

```bash
curl https://[APP-FQDN]/rng
```

After the third call, you'll get an error message. The app is now in a failed state.

The API includes a health endpoint at `/healthz`. Let's check it with the verbose flag to see the HTTP status code:

```bash
curl -v https://[APP-FQDN]/healthz
```

You'll see a 500 status code - Internal Server Error. This indicates the app is unhealthy.

## Exercise 3: Configure Health Checks

Now we'll configure App Service to monitor this health endpoint. Open the Azure Portal and navigate to your App Service.

Find the Health check blade under the Monitoring section. Enable the health check and configure it:

- Set the path to `/healthz`
- Reduce the load balancing threshold to the minimum value, which is 2

Save the changes. Azure will restart your app to apply the new configuration.

After the restart, you have a fresh, healthy instance. Let's verify:

```bash
curl -v https://[APP-FQDN]/healthz
```

This time you should see a 200 status code - the app is healthy.

Let's open the Metrics tab in the Portal. Here you can create charts for HTTP response codes and health check status. This gives you visibility into your application's health over time.

Now make some requests to get random numbers again:

```bash
curl https://[APP-FQDN]/rng
```

After three calls, the app fails again. Check the metrics in the Portal - you'll see a spike in HTTP Server Errors.

In the Overview tab, you'll see a warning that the app is unhealthy. But notice that Azure won't restart it. That's because there's only one instance. Azure takes a cautious approach - it won't replace a single instance even if it's unhealthy, because that would cause downtime while the new instance starts.

## Exercise 4: Scale Out and Auto-Heal

To enable automatic healing, we need multiple instances. Let's scale out to two instances:

```bash
az appservice plan update -g [RESOURCE-GROUP-NAME] -n [APP-PLAN-NAME] --sku B1 --number-of-workers 2
```

It takes a few minutes for the new instance to come online. When it does, it will be healthy while the old instance remains unhealthy. App Service automatically routes all traffic to the healthy instance.

Check the health endpoint:

```bash
curl https://[APP-FQDN]/healthz
```

You should get a 200 response from the healthy instance.

Now make some calls to get random numbers:

```bash
curl https://[APP-FQDN]/rng
```

After three calls, this instance fails too. Now both instances are unhealthy, but the most recently failed one still receives all the traffic.

App Service will eventually restart these failed instances, but by default it waits one hour. That's not ideal for production applications.

## Lab Challenge: Configure Auto-Heal

Your challenge is to configure auto-heal to restart instances immediately when they start returning 500 errors.

The goal is to set up a rule that triggers a restart if there are any 500 errors within a 30-second period. This way, failed instances are replaced quickly rather than waiting an hour.

You can find the auto-heal configuration in the Portal under the App Service's Diagnose and solve problems blade, or by searching for "Auto-heal" in the Configuration section.

Configure the trigger to watch for status codes in the 500 range, with a 30-second time window. Set the action to restart the instance.

Once configured, test it by making requests until the instance fails, then watch as it automatically restarts and becomes healthy again.

This demonstrates how App Service can maintain high availability even when your application encounters issues.
