# API Management Policies - Exercise Walkthrough

## Explore the Backend API

Let's start by exploring the backend API directly to understand what security issues we need to address.

**Test the Backend**: We're opening Postman or your preferred API testing tool and making a GET request to https://swapi.dev/api/people/3. This returns information about a Star Wars character - in this case, character number 3.

**Identifying Security Issues**: Looking at the response carefully, you'll notice two potential security issues that we want to fix with APIM policies.

**Issue 1: Server Header Exposure**: The Server header has the value "nginx". This reveals what server software is being used on the backend. Attackers like to know this information because they can search for known exploits in specific versions of server software. For example, if they know you're running nginx version X, they can look for security vulnerabilities specific to that version. It's better to hide this information.

**Issue 2: URL Leakage**: The response body contains lots of links back to the original API at swapi.dev. You'll see URLs like https://swapi.dev/api/planets/8/ and https://swapi.dev/api/films/1/. If we want all traffic to go through APIM so our policies are applied, we don't want people to see these direct links. Otherwise, attackers can bypass APIM and go straight to the source, circumventing all our security measures.

**Respecting the Backend**: There's also a performance consideration. SWAPI is a public service provided for free, and we should respect its bandwidth. The API has its own rate limiting, restricting calls by IP address. Normally this is fine - one end-user is unlikely to max out the limit. But when we use APIM, all calls will come from one APIM IP address, so we could hit the limit much faster. We'll use caching to reduce the load on SWAPI and improve response times.

## Create the API in API Management

Now let's create our API in APIM to front the SWAPI backend.

**Navigate to APIM**: We're navigating to your API Management instance in the Azure Portal.

**Create the API**: We're going to the APIs section and adding a new manually defined HTTP API. For the Web service URL, we're setting it to https://swapi.dev/api - this is the backend that APIM will proxy to. We're giving it a name like "Star Wars API" and a URL suffix like "swapi" so it will be accessible at your-apim-name.azure-api.net/swapi.

**Add the Operation**: We'll add just one operation to start. We're clicking to add a new operation with Method set to GET, URL path set to /people/{personId} with a template parameter for personId, and Display name set to "Get person by ID".

In the Responses section, we're adding a response with Status code 200 OK and adding a representation with content type application/json. For the sample, we're using a JSON structure showing what the response looks like - a person object with properties like name, height, mass, and various URLs to related entities.

Notice all those URLs in the sample response - we'll need to replace those with our APIM URLs using policies.

## Configure Header and Cache Policies

Now for the important part - let's add policies to secure and optimize our API.

**Open the Policy Editor**: We're clicking on our "Get person by ID" operation and going to the Policy editor.

**Policy 1: Response Caching**: First, we'll add caching to reduce load on the backend and improve response times. In the Inbound processing section, we're adding a Cache responses policy. We're setting the cache duration to 86400 seconds - that's a full day. Since Star Wars character data doesn't change, we can cache it for a long time. This means the first request fetches from SWAPI, but subsequent requests for the same character come from the APIM cache, reducing latency and backend load.

**Policy 2: Remove Server Header**: In the Outbound processing section, we're adding a policy to remove the Server header. We're looking for the Set headers policy and configuring it with Header name set to "Server" and Action set to "delete". This removes the nginx server header that we identified as a security risk, preventing attackers from knowing what software the backend is running.

**Policy 3: Add Custom Header**: While we're here, let's add our own custom header to identify responses from our APIM. We're adding another Set headers policy with Header name set to "x-server", Value set to "swapi-apim", and Action set to "append". This helps with troubleshooting and makes it clear that responses are coming through your APIM instance.

**Policy 4: URL Replacement**: This is the most interesting policy. We need to replace all occurrences of "swapi.dev" in the response body with our APIM URL. For this, we need to go to the Code editor view to work with the policy XML directly.

In the outbound section, we're adding a find-and-replace policy with the from attribute set to "swapi.dev/api" and the to attribute set to "YOUR-APIM-NAME.azure-api.net/swapi". Make sure to replace YOUR-APIM-NAME with your actual APIM instance name. This policy searches through the response body and replaces all instances of the backend URL with your APIM URL, ensuring clients only see your API gateway.

We're placing this in the outbound section, before the base tag, so it processes after the backend returns the response but before APIM sends it to the client.

**Test in the Designer**: We're saving your policies and testing the operation right there in the Azure Portal. We're clicking the Test tab, entering a personId like 3, and sending the request.

Looking at the response, we're verifying: The Server header should be gone - you shouldn't see nginx anymore. The x-server header should show "swapi-apim", confirming our custom header was added. All URLs in the response body should point to your APIM domain, not swapi.dev - every reference should now go through your gateway.

## Publish and Test the API

Now let's publish this API through a Product so it's available with subscription key authentication.

**Add to Product**: We're going to Products in your APIM instance and selecting one of your existing products, or creating a new one. We're adding your SWAPI API to the product.

**Test Without Subscription Key**: Now we're testing the API externally using Postman or curl. We're trying a request without the subscription key to your APIM URL at /swapi/people/14. You should get a 401 Unauthorized response. This is good - it means subscription key authentication is working, blocking unauthenticated access.

**Test With Subscription Key**: Now we're trying with the subscription key, passing it in the Ocp-Apim-Subscription-Key header. This should return a successful response with the character data.

**Verify the Policies**: Let's look at the response carefully. We're checking the headers - you should see your custom x-server header set to "swapi-apim". The Server header should be absent, not showing nginx. In the JSON body, all URLs should point to your APIM domain like your-apim-name.azure-api.net/swapi, not swapi.dev.

**Test Caching**: We're making the same request again. The second request should be even faster because it's served from cache - you're not even hitting the SWAPI backend, it's coming directly from APIM's cache. You can verify this by checking the response times.

## Lab Challenge

Here's a challenge to think about: The SWAPI response contains URLs linking to related entities. For example, people/3 has a species field that refers to species/2. Since we've rewritten the URLs to point to our APIM, can you follow those links? What happens when you try?

**Think About**: Do we have those other operations defined in our APIM? We only created a /people/{personId} operation, so what happens if someone tries to access /species/2 or /planets/8? What would users experience if they try to follow those links? How might you handle this in a production scenario - would you add all the SWAPI operations to your APIM, or use a different approach?

This is a real consideration when proxying APIs - you need to think about the entire API surface, not just individual operations.

## Reference

- [APIM policies reference](https://docs.microsoft.com/azure/api-management/api-management-policies)
- [Policy expressions](https://docs.microsoft.com/azure/api-management/api-management-policy-expressions)
- [Transformation policies](https://docs.microsoft.com/azure/api-management/api-management-transformation-policies)

Great work! You've successfully secured an API using APIM policies to remove sensitive information from headers, add custom headers for identification, rewrite response content to hide backend URLs, and implement caching to improve performance and reduce backend load.
