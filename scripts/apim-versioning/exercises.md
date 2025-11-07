# API Management Versioning - Exercise Walkthrough

## Deploy Version 1.0 of the API

Let's start by deploying the first version of our Random Number Generator API. We'll deploy this to an Azure App Service in the same Resource Group as our API Management instance.

**Deploy to App Service**: First, we need to navigate to the API source code folder at src/rng/Numbers.Api and deploy it. We're using the Standard SKU for our App Service because it gives us 5 deployment slots, which we'll need for running multiple versions simultaneously. We're deploying to the labs-apim resource group with Linux OS, S1 SKU, .NET Core 6.0 runtime, and placing it in West US. Remember to use a globally unique name for your web app.

While that's deploying, let's talk about what we're going to do in API Management. We're going to create a new API from an OpenAPI specification, but we're going to enable versioning right from the start. This is a best practice - don't wait to add versioning later when you already have consumers, add it from day one.

**Create the API with Versioning**: Now, we're creating the API in APIM. In the Azure Portal, we're navigating to your API Management instance and creating a new API from the OpenAPI specification. Make sure to select the Full UI option to see all the versioning options.

Here's where versioning comes in. We're checking the "Version this API?" checkbox. We're setting the version identifier to "1.0", choosing "Header" as the versioning scheme, and setting the version header name to "x-api-version". This means consumers will specify which version they want by sending a header.

We're uploading the OpenAPI spec from the file at labs/apim-versioning/rng-v1.0.json. This spec defines the API contract - the endpoints, parameters, and response formats.

Once your web app is running, you'll need to set its URL as the Web Service URL in the API settings. This will look something like https://your-webapp-name.azurewebsites.net, telling APIM where to proxy requests.

**Test Version 1.0**: Now let's test it. We're going to the Test tab in APIM and trying the rng operation. Notice something important: the HTTP request includes the API version in the header with x-api-version: 1.0. This is now a requirement for all consumers - versioned APIs need to know which version you're calling.

## Add a Revision to Version 1.1

Now we're going to add some new functionality, but we want to do it in a backward-compatible way. We're adding optional min and max parameters to control the range of random numbers. Since this is a non-breaking change - existing clients can continue working without changes - we'll use a revision instead of a new version.

**Create Deployment Slot**: First, let's create a deployment slot for the 1.1 release. We'll use blue-green deployment naming conventions. We're creating a slot called "blue" for our web app. Deployment slots are separate instances of your app with their own URLs, perfect for testing new versions.

**Deploy Version 1.1**: Now we're deploying the new version of the API to the blue slot using az webapp deployment source config-zip. We're pointing to the pre-packaged zip file for version 1.1 and targeting the blue slot specifically.

This is important: the deployment slot has its own URL, something like https://your-webapp-name-blue.azurewebsites.net. You can see it in the Portal under Deployment Slots. This separate URL is how we can test the new feature before making it live.

**Create a Revision**: Back in API Management, we're opening the Revisions tab for the RNG API. You'll see one existing revision. We're clicking "Add revision" and adding a description like "Now you can set the range of the random number you want, using min and max parameters in the query string!" This description helps track what changed in each revision.

Notice that the UI now shows "REVISION 2" above the Design tab, indicating you're working on the new revision.

**Update Backend URL**: In the Settings tab, we're changing the Web service URL to point to your blue slot URL. Now revision 1 points to Production, and revision 2 points to the blue slot. Remember, end users never see this backend URL, so it's fine that it has an unusual name - it's purely internal configuration.

**Add Parameters**: In the Design tab, we're opening the rng operation and editing the Frontend to add two query parameters: "min" and "max". We're leaving "Required" unticked for both, because these are optional parameters - clients can omit them and the API still works.

**Test the Revision**: Let's test it. In the Test tab, we're setting min to 15 and max to 45, then testing. You should get a random number in that range. Now we're deleting those parameters and testing again. It should still work, just with the default range of 1 to 100. That's what makes this a revision and not a version - it's backward compatible.

Notice that APIM adds the revision to the URL to distinguish this from the live revision. It looks something like https://your-apim-name.azure-api.net/rand;rev=2/rng. This special URL syntax lets you test revisions before making them current.

**Make Revision Current**: Now, let's make revision 2 the current revision. We're going back to the Revisions tab and making Revision 2 current. The normal URL now points to the 1.1 release, and all consumers automatically get the new optional parameters.

You can test with curl and you'll see that you can add the min and max parameters to the original URL. If you don't include them, the app still works, so existing consumers don't need to change anything - they just keep working.

## Publish Version 2.0 of the API

The optional parameters work, but they're not ideal. We can't properly validate them - what if someone sends min=1000 and max=1? What if they send letters instead of numbers? Version 1.0 clients never expected they might get a 400 Bad Request response, so if we add that validation to a revision, we could break their code. This would violate the backward compatibility promise.

To clean up the API with proper validation and an updated spec, we need a new version. This is a breaking change because clients will need to update their code to handle potential error responses.

**Deploy Version 2.0**: Let's deploy the version 2.0 code to a new deployment slot. We're creating a "green" slot, then deploying the version 2.0 zip file to it.

**Create Version 2.0**: Now in API Management, we're creating a new version of the API. We're setting the version to "2.0", using "Header" as the versioning scheme, setting the version header to "x-api-version", and using "rng-api-v2" as the full API version name for clarity.

We're importing the OpenAPI spec from labs/apim-versioning/rng-v2.0.json using the Update method. This spec reflects that min and max are now required parameters with validation.

**Update Backend URL**: In the Settings tab for version 2.0, we're using the URL for your green deployment slot as the Web service URL. Now you have both versions running simultaneously, each pointing to its own backend slot.

**Test Version 2.0**: Now we're testing the version 2.0 rng operation. Notice that min and max are now mandatory parameters - the spec requires them. If you try to call it without them, you'll get a 400 Bad Request response. This is a breaking change, which is why it needed to be a new version rather than a revision.

**Multiple Versions Live**: The beautiful thing is that we can have both versions live simultaneously. Consumers using version 1.1 continue to work with optional parameters, while new consumers can use version 2.0 with required parameters and proper validation. You can support both, and we can continue to support them with revisions and deployment slots as needed. Each version can evolve independently.

## Reference

- [Azure documentation](https://docs.microsoft.com/azure/)

## Challenge Lab

Here's something to think about: Is this really a blue-green deployment? App Service deployment slots can be swapped using az webapp deployment slot swap, which does give you the traditional blue-green experience - you swap production and staging instantly. But is that possible with APIM in front directing traffic to specific slot URLs?

**Think About**: APIM has revision 2 hard-coded to point to the blue slot URL. If you swap slots at the App Service level, the blue slot becomes production and vice versa, but APIM is still pointing to the URL labeled "blue". How would you handle a blue-green swap in this architecture? Would you update the APIM backend URL after swapping? Use different naming? Avoid swapping altogether?

Take some time to explore this question and see if you can find a solution that works for your deployment strategy.
