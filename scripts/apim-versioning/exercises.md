# API Management Versioning - Exercise Walkthrough

## Exercise 1: Deploy Version 1.0 of the API

Let's start by deploying the first version of our Random Number Generator API. We'll deploy this to an Azure App Service in the same Resource Group as our API Management instance.

First, we need to navigate to the API source code folder and deploy it. We're using the Standard SKU for our App Service because it gives us 5 deployment slots, which we'll need for running multiple versions simultaneously.

```bash
cd src/rng/Numbers.Api
az webapp up -g labs-apim --os-type Linux --sku S1 --runtime dotnetcore:6.0 -l westus -n your-webapp-name
```

While that's deploying, let's talk about what we're going to do in API Management. We're going to create a new API from an OpenAPI specification, but we're going to enable versioning right from the start. This is a best practice - don't wait to add versioning later.

Now, let's create the API in APIM. In the Azure Portal, navigate to your API Management instance and create a new API from the OpenAPI specification. Make sure to select the Full UI option.

Here's where versioning comes in. Check the "Version this API?" checkbox. Set the version identifier to "1.0", choose "Header" as the versioning scheme, and set the version header name to "x-api-version".

Upload the OpenAPI spec from the file at labs/apim-versioning/rng-v1.0.json.

Once your web app is running, you'll need to set its URL as the Web Service URL in the API settings. This will look something like https://your-webapp-name.azurewebsites.net.

Now let's test it. Go to the Test tab in APIM and try the rng operation. Notice something important: the HTTP request includes the API version in the header. This is now a requirement for all consumers. Versioned APIs need to know which version you're calling.

## Exercise 2: Add a Revision to Version 1.1

Now we're going to add some new functionality, but we want to do it in a backward-compatible way. We're adding optional min and max parameters to control the range of random numbers.

Since this is a non-breaking change, we'll use a revision instead of a new version.

First, let's create a deployment slot for the 1.1 release. We'll use blue-green deployment naming conventions:

```bash
az webapp deployment slot create -g labs-apim --slot blue -n your-webapp-name
```

Now deploy the new version of the API to the blue slot:

```bash
az webapp deployment source config-zip -g labs-apim --src src/rng/Numbers.Api-v1.1/rng-api-v1-1.zip --slot blue -n your-webapp-name
```

This is important: the deployment slot has its own URL. You can see it in the Portal under Deployment Slots. This separate URL is how we can test the new feature before making it live.

Back in API Management, open the Revisions tab for the RNG API. You'll see one existing revision. Click "Add revision" and add a description: "Now you can set the range of the random number you want, using min and max parameters in the query string!"

Notice that the UI now shows "REVISION 2" above the Design tab.

In the Settings tab, change the Web service URL to point to your blue slot URL. Now revision 1 points to Production, and revision 2 points to the blue slot. Remember, end users never see this backend URL, so it's fine that it has an unusual name.

In the Design tab, open the rng operation and edit the Frontend to add two query parameters: min and max. Leave "Required" unticked for both, because these are optional parameters.

Let's test it. In the Test tab, set min to 15 and max to 45, then test. You should get a random number in that range. Now delete those parameters and test again. It should still work, just with the default range. That's what makes this a revision and not a version - it's backward compatible.

Notice that APIM adds the revision to the URL to distinguish this from the live revision. It looks something like https://your-apim-name.azure-api.net/rand;rev=2/rng.

Now, let's make revision 2 the current revision. Go back to the Revisions tab and make Revision 2 current. The normal URL now points to the 1.1 release.

You can test with curl, and you'll see that you can add the min and max parameters to the original URL. If you don't include them, the app still works, so existing consumers don't need to change anything.

## Exercise 3: Publish Version 2.0 of the API

The optional parameters work, but they're not ideal. We can't properly validate them. Version 1.0 clients never expected they might get a 400 response, so if we add that validation to a revision, we could break their code.

To clean up the API with proper validation and an updated spec, we need a new version. This is a breaking change.

Let's deploy the version 2.0 code to a new deployment slot:

```bash
az webapp deployment slot create -g labs-apim --slot green -n your-webapp-name
az webapp deployment source config-zip -g labs-apim --src src/rng/Numbers.Api-v2/rng-api-v2-0.zip --slot green -n your-webapp-name
```

Now in API Management, create a new version of the API. Set the version to "2.0", use "Header" as the versioning scheme, set the version header to "x-api-version", and use "rng-api-v2" as the full API version name.

Import the OpenAPI spec from labs/apim-versioning/rng-v2.0.json using the Update method.

In the Settings tab for version 2.0, use the URL for your green deployment slot as the Web service URL.

Now test the version 2.0 rng operation. Notice that min and max are now mandatory parameters. If you try to call it without them, you'll get a 400 response. This is a breaking change, which is why it needed to be a new version.

The beautiful thing is that we can have both versions live simultaneously. Version 1.1 and version 2.0 can both run, and we can continue to support them with revisions and deployment slots as needed.

## Challenge Lab

Here's something to think about: Is this really a blue-green deployment? App Service deployment slots can be swapped, which does give you the traditional blue-green experience. But is that possible with APIM in front directing traffic to specific slot URLs? How would you handle a blue-green swap in this architecture?

Take some time to explore this question and see if you can find a solution.
