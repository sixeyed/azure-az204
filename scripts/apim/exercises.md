# API Management - Exercises Narration Script

## Exercise Overview

Welcome to the hands-on exercises for Azure API Management. In this session, we'll work through creating an APIM instance, deploying a backend API, configuring policies, publishing through the Developer Portal, and testing as an API consumer. Let's dive in!

## Exercise 1: Create APIM Resource

First, we need to create our API Management resource. As I mentioned earlier, this takes time, so we'll do it through the CLI with the no-wait flag so we can continue working while it provisions.

Let's start by creating a resource group:

```bash
az group create -n labs-apim --tags courselabs=azure -l westus
```

Now, let's create the APIM instance. You'll need to provide three things: a unique name for your APIM instance, a publisher name which is typically your company name, and a real email address:

```bash
az apim create --no-wait --sku-name Developer \
  -g labs-apim \
  -n <your-apim-name> \
  --publisher-name <your-company-name> \
  --publisher-email <your-email-address>
```

Notice we're using the Developer tier, which is perfect for labs and development work. The no-wait flag means this command will return immediately, and Azure will provision the instance in the background.

You'll receive an email when your APIM instance is ready to use. This typically takes 30 to 45 minutes, so this is a great time to grab a coffee or work on something else.

## Exercise 2: Deploy Backend API

While we're waiting for APIM to provision, let's deploy our backend API. We'll use a random number generator API as our example. This is a simple .NET Core API that we'll deploy as an Azure Web App.

Navigate to the API source code directory:

```bash
cd src/rng/Numbers.Api
```

Now deploy it as a Web App:

```bash
az webapp up -g labs-apim \
  --os-type Linux \
  --sku B1 \
  --runtime dotnetcore:6.0 \
  -l westus \
  -n <your-webapp-name>
```

Make sure you choose a unique name for your Web App. Once this completes, you'll have a running API hosted in Azure.

## Exploring the Backend API

Let's explore the backend API before we import it into APIM. This API hosts its own documentation using Swagger. Open your browser and navigate to:

```
http://<your-webapp-name>.azurewebsites.net/swagger
```

You'll see the Swagger UI showing all the API operations. Our random number generator API has three endpoints: /rng which returns a random number, /reset which resets the generator, and /healthz which is a health check endpoint.

Now, here's the really useful part. The API also publishes its documentation in JSON format using the OpenAPI specification. You can view this at:

```
https://<your-webapp-name>.azurewebsites.net/swagger/v1/swagger.json
```

This JSON document describes the entire API - all the operations, parameters, response types, everything. And APIM can import this directly, which is what we'll do next.

## Importing the API into APIM

By now, your APIM instance should be provisioned. Open the Azure Portal and navigate to your APIM resource. If it's still provisioning, you'll see a notification - be patient!

Once it's ready, let's import our API:

1. In the APIM resource, open the APIs blade from the left navigation
2. Click "Add API"
3. Select "OpenAPI" as the import source
4. Enter the URL for your Web App's swagger.json file
5. Give your API a name and display name - let's call it "Random Number Generator"
6. Leave the API URL suffix as suggested or customize it

Click Create, and APIM will import all the operations from your OpenAPI spec. Pretty neat, right? In just a few clicks, you've got a fully defined API in APIM without manually creating each operation.

## Exercise 3: Configure API Policies

Now comes the fun part - configuring policies. This is where APIM really shines. We're going to configure three different policies on our three different endpoints.

Let's start with the /rng endpoint. We want to cache the response for 30 seconds to reduce the load on our backend API. In the API designer:

1. Select the /rng operation
2. In the inbound processing section, click "Add policy"
3. Select "Cache responses"
4. Set the duration to 30 seconds
5. Save the policy

What this means is that when someone calls /rng, APIM will call the backend once and cache the response. For the next 30 seconds, any subsequent calls will get the cached response without hitting the backend at all.

Next, let's configure the /reset endpoint. This is an administrative operation - we don't want just anyone calling it. We'll restrict it to your IP address only:

1. Select the /reset operation
2. Add an inbound policy
3. Select "Filter IP addresses"
4. Set action to "allow"
5. Add your public IP address (you can find this at ifconfig.me)
6. Save the policy

Now only requests from your IP address can call this endpoint. Anyone else will get a 403 Forbidden response.

Finally, let's handle the /healthz endpoint. This is an internal health check endpoint that shouldn't be exposed publicly at all. We want APIM to return a 404 Not Found without ever calling the backend:

1. Select the /healthz operation
2. Switch to the policy code editor (there should be a code view option)
3. In the inbound section, add a return-response policy
4. Set the status code to 404
5. Make sure this policy comes before the base tag so the backend is never called
6. Save the policy

The XML should look something like this:

```xml
<inbound>
    <return-response>
        <set-status code="404" reason="Not Found" />
    </return-response>
    <base />
</inbound>
```

## Testing the Policies

Now let's test each endpoint through the designer to validate our policies are working correctly.

Test the /rng endpoint:
1. Click on the /rng operation
2. Go to the Test tab
3. Click Send
4. Note the random number in the response
5. Click Send again immediately
6. You should get the same random number - that's the cache working!
7. Wait 30 seconds and try again
8. Now you should get a different number

Test the /reset endpoint:
1. Click on the /reset operation
2. If you're testing from the Azure Portal, this might fail because the Portal's requests come from Azure's IP addresses, not yours
3. You can modify the policy to add the Azure Portal IP ranges, or test from your local machine with curl

Test the /healthz endpoint:
1. Click on the /healthz operation
2. Click Send
3. You should get a 404 response
4. This confirms that APIM is blocking this endpoint without calling the backend

## Exercise 4: Configure API Settings

Before we can publish our API, we need to configure a few settings. In the API Settings tab:

1. Set the Web service URL to your backend Web App URL: `https://<your-webapp-name>.azurewebsites.net`
2. Add the API to a Product - you can use one of the default products like "Starter" or "Unlimited", or create your own
3. Save the settings

Products are important - they're how you control access to your APIs. An API must be in at least one product to be accessible through the Developer Portal.

## Exercise 5: Publish the Developer Portal

Now let's set up the Developer Portal. This is the self-service portal where your API consumers will sign up and get access to your APIs.

Click on the Developer Portal link from the overview page. This opens the designer view where you can customize the portal:

1. Update the company name to your own
2. Customize the colors and styling if you like
3. Add or modify content pages
4. Preview your changes

When you're happy with the design, go to Portal overview and:

1. Enable CORS so the portal can call your API gateway
2. Configure authentication options - enable Azure AD if you want
3. Click Publish to make the portal live

The portal is now published and accessible to the public at your Developer Portal URL.

## Exercise 6: Sign Up as a Consumer

Now let's experience APIM from the consumer's perspective. Open a private or incognito browser window and navigate to your Developer Portal URL.

Click on Sign Up and create a new account. You'll need to provide:
- A username
- A real email address
- A strong password

You'll receive a verification email with a link to confirm your account. Click the link to verify, then log in to the portal.

Take a moment to explore the Developer Portal. You'll see the products available, and if you navigate to the products, you'll see the APIs included in each.

## Subscribing to a Product

Find the Random Number Generator API and try to test it using the portal's test page. It will fail! That's because you need a subscription key.

To get a subscription key:
1. Navigate to Products
2. Choose a product that includes your API (like Starter or Unlimited)
3. Click Subscribe
4. Confirm the subscription

Now you'll see your subscription keys. There are two keys - a primary and a secondary. This allows you to rotate keys without downtime.

## Testing the API with curl

Let's test the API from the command line using curl. The Developer Portal shows you example curl commands. The format is:

```bash
curl "https://<your-apim-name>.azure-api.net/<api-path>/rng" \
  -H "Ocp-Apim-Subscription-Key: <your-subscription-key>"
```

Replace the placeholders with your actual values. Make sure to copy your full subscription key from the portal.

Run this command and you should get a random number back. Now run it again immediately - you should get the same number. This confirms that the caching policy is working correctly. Wait 30 seconds and try again - you'll get a different number.

## Rate Limiting in Action

If you chose the Starter product, there's a rate limit of 5 calls per minute. Let's test this. Run your curl command rapidly six times in a row:

```bash
for i in {1..6}; do curl "https://<your-apim-name>.azure-api.net/<api-path>/rng" \
  -H "Ocp-Apim-Subscription-Key: <your-subscription-key>"; echo ""; done
```

On the sixth call, you should get an error response:

```json
{ "statusCode": 429, "message": "Rate limit is exceeded. Try again in XX seconds." }
```

This is production-grade rate limiting that you got without writing a single line of code. APIM is enforcing these limits automatically based on the product configuration.

## Monitoring in the Portal

Back in the Azure Portal, navigate to your APIM resource and check the Analytics blade. You'll see:
- Request volume over time
- Response times
- Success and error rates
- Top operations

This gives you valuable insights into how your API is being used and how it's performing.

## Lab Challenge

Now that you've completed the core exercises, here are some questions to think about:

1. Can you customize the text of the emails that get sent to users signing up? Look in the Notifications section of your APIM resource.

2. All the clicking and pointing we did in the Portal is error-prone and doesn't scale. How would you automate APIM configuration? Think about Infrastructure as Code - you could use ARM templates, Bicep, or Terraform to define your entire APIM configuration as code.

3. The endpoint policies are all applied by APIM, but is your backend Web App still publicly available? Try accessing it directly. How would you secure it so only APIM can reach it? Think about network security groups, VNets, and IP restrictions.

## Important Note

Don't clean up this resource group yet! APIM takes so long to provision that we'll reuse the same instance in the next few labs. One APIM instance can host multiple APIs, so we'll add more APIs to this instance as we progress through the course.

## Conclusion

Congratulations! You've successfully:
- Created an API Management instance
- Deployed a backend API
- Imported the API using OpenAPI specification
- Configured caching, IP filtering, and custom response policies
- Published the Developer Portal
- Signed up as a consumer and tested the API with subscription keys
- Experienced rate limiting and monitoring

You've seen how APIM gives you production-grade features - caching, rate limiting, security, monitoring, and a self-service developer portal - all without writing code. This is the power of Azure API Management.

In the next lab, we'll explore more advanced APIM features. Great work!
