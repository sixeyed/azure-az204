# App Service for Distributed Apps

## Reference

One App Service Plan can run multiple App Services, which is a great way to share compute resources. You pay for one set of infrastructure and use it to run multiple components of a distributed application. Connecting components together is where things get interesting, because the addresses to use will change for each environment. App Service gives you a nice way to manage that by setting configuration values in the App Service which get pushed into the application.

## Deploy API

Let's begin by setting up our foundational resources. We'll create a resource group to contain all our resources, and an App Service Plan that will host our applications.

First, we're creating the resource group with a unique name, adding our standard courselabs tag for tracking, and selecting a region close to you.

Now, let's create the App Service Plan. We're using the B1 SKU with Linux and configuring it with 2 workers for high availability. The B1 tier is cost-effective for development and testing, and having 2 workers means if one instance has issues, the other can continue serving requests.

Important note: Not all Azure regions support all App Service Plan SKUs. If you see an error about the plan not being supported in your region, try a different region like West US or East US - these major regions typically support all SKU types.

Now we'll deploy our REST API using the webapp up command. This is a convenient shortcut that handles both the App Service creation and code deployment in a single operation.

First, we're navigating to the API source code directory at "src/rng/Numbers.Api".

Before deploying, let's verify the available runtimes since this is a .NET 6.0 application. We're listing the Linux runtimes to confirm dotnetcore:6.0 is available in our chosen region.

Now we're deploying the API using webapp up. We're specifying the resource group, the App Service Plan we created, Linux as the operating system, .NET Core 6.0 as the runtime, the region, and a globally unique name for the web app.

During deployment, the command creates a ZIP file of your source code and uploads it to Azure. The platform then builds and runs your application using the Oryx build system - this all happens automatically without you needing to configure build tools.

Let's check the deployment logs to ensure everything built successfully. We're viewing the deployment logs which show the build process and any warnings or errors that occurred.

In the Azure Portal, navigating to your API App Service and opening the Deployment Center, we can review the detailed build logs, including the Oryx build output showing how the .NET application was compiled and configured.

Now let's test the API. Browsing to your app's URL with "/swagger" appended shows the Swagger documentation for your random number generator API. This auto-generated documentation is incredibly useful for understanding what endpoints are available.

Testing the API endpoint directly using curl to call the "/rng" path, you should see a random number returned. Trying it multiple times, you'll get a different number each time, confirming the API is working correctly.

## Deploy Website

Now let's deploy the web frontend that will consume our API. We're navigating to the web application directory at "Numbers.Web".

We're deploying the web application to the same App Service Plan using webapp up. This is efficient - both applications share the same underlying infrastructure, but they're isolated from each other and have separate URLs. We're specifying the same resource group and plan name, with Linux and .NET Core 6.0, in the same region, but with a different unique name for the web app.

While the web deployment is in progress, let's check if we can see our API calls in the logs. In the Azure Portal, navigating to your API App Service and examining the logs, you should see records of the curl requests you made earlier. This demonstrates the built-in logging that App Service provides automatically.

Once deployment completes, we're browsing to your web application. You'll see the random number generator web interface with a simple form.

Clicking the "Go!" button to fetch a random number, you'll notice an error: "RNG service unavailable". The page also shows the API URL it's trying to use - it's pointing to a localhost address because we're using the default development configuration. This won't work in Azure because the web app can't access localhost - it needs the actual API URL.

In the Azure Portal, opening your web App Service and navigating to Configuration settings, you'll see some existing settings used for deployment, but we need to add an application-specific setting to tell the web app where to find the API.

We're adding a new Application Setting with the key "RngApi__Url" and the value set to your API's full URL followed by "/rng". The double underscore in the key name is how .NET Core hierarchical configuration works - this maps to "RngApi:Url" in the application's configuration system.

Clicking Save, Azure warns you that the application will restart to pick up the new configuration. This is necessary because applications cache their configuration at startup.

Browsing to your web application again and clicking the "Go!" button, now you should see a random number successfully retrieved from your API. The two applications are now communicating through the configuration you just set. This demonstrates the proper pattern for configuring distributed applications in App Service.

If you're familiar with .NET, look at the default configuration in the application's appsettings.json file. How does the App Service configuration override these values? Understanding this pattern is crucial for managing applications across different environments - you can have development settings in the file and production settings in App Service configuration.

## Scale the App Service Plan

Let's try to scale our App Service Plan to 3 workers. We initially created it with 2 workers on the B1 SKU, which supports up to 3 instances. We're using the appservice plan update command to set the worker count to 3.

Interesting - this command fails! Let's investigate why this is happening.

Checking the current state of your App Service Plan using the show command, we're examining the SKU details in the output. You'll notice it's showing the Free F1 tier, not the B1 tier we created. The F1 tier only supports 1 worker, which is why our scale operation failed.

What happened? The webapp up command can modify your App Service Plan, potentially downgrading it to the Free tier. This is a side effect of using webapp up - it's convenient, but it can make unexpected changes to existing resources.

Let's fix this by updating both the SKU and the worker count in a single command. We're setting the SKU back to B1 and the worker count to 3.

The SKU update happens first, which increases the maximum worker count from 1 to 3, then the plan scales to 3 instances. This demonstrates the difference between scaling up (changing the SKU tier) and scaling out (adding more instances).

Now let's see how requests are distributed across our API instances. Opening your web application and clicking the "Go!" button several times, we can observe the behavior.

Checking the API logs - are you seeing requests handled by different instances? This helps you understand how App Service distributes traffic.

Try these experiments: Opening the web app in a private or incognito browser window with no history, do you see responses from different API servers? Using curl to call the API directly, does each request go to a different instance?

This demonstrates how Azure App Service distributes traffic across your scaled instances using its built-in load balancer.

---

## Lab

We have an alternative frontend - a static HTML single-page application located in "labs/appservice-api/spa/index.html".

Your challenge has three parts: First, edit the index.html file to set your API URL. Second, deploy it as a static web app. Third, when you test it, you'll encounter a CORS error in the browser console - you need to figure out how to fix this.

When you click the button in your static web app, checking the browser's developer tools console, you'll see an error about CORS policy. The message says something like "Access to XMLHttpRequest at your API URL from origin your static web app URL has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource."

This is a security feature built into browsers. The API won't allow calls from external domains by default - it's protecting against cross-site request forgery attacks. But in our case, we want to allow our static web app to call the API.

Find and configure the CORS settings on your API App Service to allow requests from your static web app's domain.

Hint: Looking in the API App Service settings in the Azure Portal, there's a dedicated section for CORS configuration where you can specify which origins are allowed to make requests to your API.

---

## Cleanup

When you're finished with the lab, we're deleting the resource group to remove all resources. The command uses the -y flag to confirm the deletion without prompting, and the --no-wait flag to return immediately while the deletion continues in the background.
