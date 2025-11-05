# App Service for Distributed Apps - Exercise Narration

## Exercise 1: Deploy the REST API

### Step 1.1: Create Resource Group and App Service Plan

Let's begin by setting up our foundational resources. We'll create a resource group to contain all our resources, and an App Service Plan that will host our applications.

First, create the resource group:
```bash
az group create -n [RESOURCE-GROUP-NAME] --tags courselabs=azure -l [REGION]
```

Now, let's create the App Service Plan. We'll use the B1 SKU with Linux and configure it with 2 workers for high availability:
```bash
az appservice plan create -g [RESOURCE-GROUP-NAME] -n [APP-PLAN-NAME] --is-linux --sku B1 --number-of-workers 2 -l [REGION]
```

**Important note**: Not all Azure regions support all App Service Plan SKUs. If you see an error about the plan not being supported in your region, try a different region like westus or eastus.

### Step 1.2: Deploy the API Application

Now we'll deploy our REST API using the `az webapp up` command. This is a convenient shortcut that handles both the App Service creation and code deployment.

First, navigate to the API source code directory:
```bash
cd src/rng/Numbers.Api
```

Before deploying, let's verify the available runtimes since this is a .NET 6.0 application:
```bash
az webapp list-runtimes --os-type=linux
```

Now deploy the API:
```bash
az webapp up -g [RESOURCE-GROUP-NAME] --plan [APP-PLAN-NAME] --os-type Linux --runtime dotnetcore:6.0 -l [REGION] -n [API-DNS-NAME]
```

During deployment, the command creates a ZIP file of your source code and uploads it to Azure. The platform then builds and runs your application.

### Step 1.3: Verify API Deployment

Let's check the deployment logs to ensure everything built successfully:
```bash
az webapp log deployment show -g [RESOURCE-GROUP-NAME] -n [API-DNS-NAME]
```

In the Azure Portal, navigate to your API App Service and open the Deployment Center to review the detailed build logs, including the Oryx build output.

Now let's test the API. Browse to `https://[API-FQDN]/swagger` to see the Swagger documentation for your random number generator API.

Test the API endpoint directly:
```bash
curl https://[API-FQDN]/rng
```

You should see a random number returned. Try calling it multiple times - you'll get a different number each time.

## Exercise 2: Deploy the Web Frontend

### Step 2.1: Deploy the Web Application

Now let's deploy the web frontend that will consume our API. Navigate to the web application directory:
```bash
cd ../Numbers.Web
```

Deploy the web application to the same App Service Plan:
```bash
az webapp up -g [RESOURCE-GROUP-NAME] --plan [APP-PLAN-NAME] --os-type Linux --runtime dotnetcore:6.0 -l [REGION] -n [WEB-DNS-NAME]
```

### Step 2.2: Check API Logs

While the web deployment is in progress, let's check if we can see our API calls in the logs. In the Azure Portal, navigate to your API App Service and examine the logs. You should see records of the curl requests you made earlier.

### Step 2.3: Test Initial Web Deployment

Once deployment completes, browse to your web application at `https://[WEB-FQDN]`. You'll see the random number generator web interface.

Click the "Go!" button to fetch a random number. You'll notice an error: "RNG service unavailable". The page also shows the API URL it's trying to use - it's pointing to a localhost address because we're using the default development configuration.

## Exercise 3: Configure Application Communication

### Step 3.1: Add Application Configuration

In the Azure Portal, open your web App Service and navigate to Configuration settings. You'll see some existing settings used for deployment, but we need to add an application-specific setting.

Add a new Application Setting:
- Key: `RngApi__Url`
- Value: `https://[API-FQDN]/rng`

The double underscore in the key name is how .NET Core hierarchical configuration works - this maps to `RngApi:Url` in the application.

Click Save. Azure will warn you that the application will restart to pick up the new configuration.

### Step 3.2: Verify the Configuration

Browse to your web application again and click the "Go!" button. Now you should see a random number successfully retrieved from your API. The two applications are now communicating through the configuration you just set.

**Question to consider**: If you're familiar with .NET, look at the default configuration in the application's appsettings.json file. How does the App Service configuration override these values? Understanding this pattern is crucial for managing applications across different environments.

## Exercise 4: Scale the App Service Plan

### Step 4.1: Attempt to Scale

Let's try to scale our App Service Plan to 3 workers. We initially created it with 2 workers on the B1 SKU, which supports up to 3 instances:
```bash
az appservice plan update -g [RESOURCE-GROUP-NAME] -n [APP-PLAN-NAME] --number-of-workers 3
```

Interesting - this command fails! Let's investigate why.

### Step 4.2: Investigate the Issue

Check the current state of your App Service Plan:
```bash
az appservice plan show -g [RESOURCE-GROUP-NAME] -n [APP-PLAN-NAME]
```

Look at the SKU details in the output. You'll notice it's showing the Free F1 tier, not the B1 tier we created. The F1 tier only supports 1 worker, which is why our scale operation failed.

**What happened?** The `az webapp up` command can modify your App Service Plan, potentially downgrading it to the Free tier.

### Step 4.3: Scale Up and Out

Let's fix this by updating both the SKU and the worker count:
```bash
az appservice plan update -g [RESOURCE-GROUP-NAME] -n [APP-PLAN-NAME] --sku B1 --number-of-workers 3
```

The SKU update happens first, which increases the maximum worker count, then the plan scales to 3 instances.

### Step 4.4: Observe Load Distribution

Now let's see how requests are distributed across our API instances. Open your web application and click the "Go!" button several times.

Check the API logs - are you seeing requests handled by different instances?

Try these experiments:
- Open the web app in a private/incognito browser window with no history. Do you see responses from different API servers?
- Use curl to call the API directly. Does each request go to a different instance?

This demonstrates how Azure App Service distributes traffic across your scaled instances.

## Lab Challenge: Static Web App with CORS

### Challenge Setup

We have an alternative frontend - a static HTML single-page application located in `labs/appservice-api/spa/index.html`.

Your challenge:
1. Edit the index.html file to set your API URL
2. Deploy it as a static web app
3. When you test it, you'll encounter a CORS error in the browser console

### Understanding the Problem

When you click the button in your static web app, check the browser's developer tools console. You'll see an error similar to:

"Access to XMLHttpRequest at '[API-URL]' from origin '[STATIC-WEB-APP-URL]' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource."

This is a security feature. The API won't allow calls from external domains by default.

### Your Task

Find and configure the CORS settings on your API App Service to allow requests from your static web app's domain.

**Hint**: Look in the API App Service settings in the Azure Portal. There's a dedicated section for CORS configuration.

## Cleanup

When you're finished with the lab, delete the resource group to remove all resources:
```bash
az group delete -y -n [RESOURCE-GROUP-NAME] --no-wait
```

The `--no-wait` flag allows the command to return immediately while the deletion continues in the background.
