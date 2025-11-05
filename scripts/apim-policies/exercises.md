# API Management Policies - Exercise Walkthrough

## Exercise 1: Explore the Backend API

Let's start by exploring the backend API directly to understand what security issues we need to address.

Open Postman or your preferred API testing tool, and make a GET request to:

```
https://swapi.dev/api/people/3
```

This returns information about a Star Wars character - in this case, character number 3.

### Identifying Security Issues

Look at the response carefully. You'll notice two potential security issues:

**Issue 1: Server Header Exposure**
The `Server` header has the value `nginx`. This reveals what server software is being used. Attackers like to know this information because they can search for known exploits in specific versions of server software.

**Issue 2: URL Leakage**
The response body contains lots of links back to the original API at swapi.dev. If we want all traffic to go through APIM so our policies are applied, we don't want people to see these direct links. Otherwise, attackers can bypass APIM and go straight to the source.

### Respecting the Backend

There's also a performance consideration. SWAPI is a public service, and we should respect its bandwidth. The API has its own rate limiting, restricting calls by IP address.

Normally this is fine - one end-user is unlikely to max out the limit. But when we use APIM, all calls will come from one APIM IP address, so we could hit the limit. We'll use caching to reduce the load on SWAPI.

## Exercise 2: Create the API in API Management

Now let's create our API in APIM to front the SWAPI backend.

Navigate to your API Management instance in the Azure Portal.

Go to the APIs section and add a new **manually defined HTTP API**.

Set the Web service URL to:
```
https://swapi.dev/api
```

Give it a name like "Star Wars API" and a URL suffix like "swapi".

### Add the Operation

We'll add just one operation to start. Click to add a new operation:

- Method: **GET**
- URL path: **/people/{personId}**
- Display name: "Get person by ID"

In the Responses section, add a response:
- Status code: **200 OK**
- Add a representation with content type **application/json**

For the sample, you can use this JSON structure showing what the response looks like:

```json
{
  "name": "R2-D2",
  "height": "96",
  "mass": "32",
  "hair_color": "n/a",
  "skin_color": "white, blue",
  "eye_color": "red",
  "birth_year": "33BBY",
  "gender": "n/a",
  "homeworld": "https://swapi.dev/api/planets/8/",
  "films": [
    "https://swapi.dev/api/films/1/",
    "https://swapi.dev/api/films/2/"
  ],
  "species": [
    "https://swapi.dev/api/species/2/"
  ],
  "vehicles": [],
  "starships": [],
  "created": "2014-12-10T15:11:50.376000Z",
  "edited": "2014-12-20T21:17:50.311000Z",
  "url": "https://swapi.dev/api/people/3/"
}
```

Notice all those URLs in the response - we'll need to replace those with our APIM URLs.

## Exercise 3: Configure Header and Cache Policies

Now for the important part - let's add policies to secure and optimize our API.

Click on your "Get person by ID" operation and go to the Policy editor.

### Policy 1: Response Caching

First, we'll add caching to reduce load on the backend and improve response times.

In the **Inbound processing** section, add a **Cache responses** policy.

Set the cache duration to **86400** seconds - that's a full day. Since Star Wars character data doesn't change, we can cache it for a long time.

### Policy 2: Remove Server Header

In the **Outbound processing** section, add a policy to remove the Server header.

Look for **Set headers** policy and configure it to:
- Header name: **Server**
- Action: **delete**

This removes the nginx server header that we identified as a security risk.

### Policy 3: Add Custom Header

While we're here, let's add our own custom header to identify responses from our APIM.

Add another **Set headers** policy:
- Header name: **x-server**
- Value: **swapi-apim**
- Action: **append**

### Policy 4: URL Replacement

This is the most interesting policy. We need to replace all occurrences of `swapi.dev` in the response body with our APIM URL.

For this, we need to go to the **Code editor** view to work with the policy XML directly.

In the **outbound** section, add a **find-and-replace** policy:

```xml
<find-and-replace from="swapi.dev/api" to="<YOUR-APIM-NAME>.azure-api.net/swapi" />
```

Make sure to place this in the `<outbound>` section, before the `<base />` tag.

Replace `<YOUR-APIM-NAME>` with your actual APIM instance name.

### Test in the Designer

Save your policies and test the operation right there in the Azure Portal.

Click the **Test** tab, enter a personId like **3**, and send the request.

Look at the response:
- The Server header should be gone
- The x-server header should show "swapi-apim"
- All URLs in the response body should point to your APIM domain, not swapi.dev

## Exercise 4: Publish and Test the API

Now let's publish this API through a Product so it's available with subscription key authentication.

Go to **Products** in your APIM instance and select one of your existing products, or create a new one.

Add your SWAPI API to the product.

### Test with Postman

Now test the API externally using Postman or curl.

First, get your subscription key from the product's subscription page.

Try a request **without** the subscription key:

```
curl -v "https://<YOUR-APIM-NAME>.azure-api.net/swapi/people/14"
```

You should get a **401 Unauthorized** response. This is good - it means subscription key authentication is working.

Now try with the subscription key:

```
curl -v "https://<YOUR-APIM-NAME>.azure-api.net/swapi/people/14" -H "Ocp-Apim-Subscription-Key: <YOUR-SUBSCRIPTION-KEY>"
```

This should return a successful response.

### Verify the Policies

Look at the response carefully:
- Check the headers - you should see your custom **x-server** header
- The **Server** header should be absent
- All URLs in the JSON body should point to your APIM domain, not swapi.dev

Try making the same request again. The second request should be even faster because it's served from cache.

## Lab Challenge

Here's a challenge to think about:

The SWAPI response contains URLs linking to related entities. For example, `people/3` has a species field that refers to `species/2`.

Since we've rewritten the URLs to point to our APIM, can you follow those links? What happens when you try?

Is this a good thing or a bad thing?

Think about:
- Do we have those other operations defined in our APIM?
- What would users experience if they try to follow those links?
- How might you handle this in a production scenario?

Great work! You've successfully secured an API using APIM policies to remove sensitive information, add custom headers, and rewrite response content.
