# API Management: Request and Response Policies - Podcast Script

## Welcome and Introduction

Welcome to this episode on API Management request and response policies. Today we're exploring one of the most powerful features of Azure API Management: policies that let you modify the behavior of your APIs without touching any backend code.

Whether you're preparing for the Azure AZ-204 certification or working with API Management in production environments, understanding policies is essential. These policies act as plug-in features that can transform requests, modify responses, enforce security, and optimize performance.

## Understanding APIM Policies

Let's start with the fundamental concept: what exactly are API Management policies?

Policies are configuration elements that execute in sequence on API requests and responses. Think of them as middleware that sits between your clients and your backend services, intercepting traffic and applying transformations or rules.

There are two main categories of policies that you'll work with most often:

**Input policies** execute before the request reaches your backend service. These are powerful because they can alter the incoming request, add authentication, enforce rate limits, or even short-circuit the entire call and return a cached or mocked response without ever hitting the backend.

**Output policies** execute after the backend has responded but before the response goes back to the client. These let you transform the response, add or remove headers, modify the response body, or store responses in cache.

Beyond these, there are also backend policies that execute when forwarding to the backend service, and on-error policies that handle exceptions and errors. But the inbound and outbound policies are where you'll spend most of your time.

## Policy Scope and Inheritance

One critical concept to understand is policy scope. Policies can be applied at multiple levels, and they work together through inheritance.

At the broadest level, you have **global policies** that apply to every API in your API Management instance. These are great for organization-wide rules like logging or common security headers.

**Product-level policies** apply to all APIs within a specific product. Remember, products in API Management are how you package APIs together for different audiences or subscription tiers.

**API-level policies** apply to all operations within a single API, while **operation-level policies** apply only to specific endpoints.

What makes this system flexible is the base tag. When you include the base tag in a policy section, you're explicitly calling the parent scope's policies. The position of the base tag matters: policies you define before the base tag execute before the parent's policies, and policies after the base tag execute afterward. This gives you precise control over the execution order.

## Real-World Example: Securing a Public API

Let's walk through a practical scenario that demonstrates how policies solve real security and performance problems. We'll work with SWAPI, the Star Wars API, which is a popular public REST API that returns information about Star Wars characters, planets, films, and more.

Now, this is interesting because we're fronting a third-party API with API Management. Yes, this is absolutely allowed, as long as you respect the third party's usage terms. This pattern is common when you want to add your own security, caching, or transformation layer on top of external services.

## Identifying Security Issues

When you examine the raw backend API by making a direct request to SWAPI, you'll discover several security and operational issues that need addressing.

**The Server Header Problem**: The response includes a Server header that reveals the backend is running nginx. This might seem harmless, but it's actually a security risk. When attackers know what server software you're running, they can search for known vulnerabilities specific to that software version. If they discover you're running nginx version X, they can look up every security flaw ever found in that version and attempt to exploit them. It's better to hide this implementation detail entirely.

**URL Leakage**: The response body contains numerous URLs pointing directly back to swapi.dev. For example, character data includes URLs like https://swapi.dev/api/planets/8/ and https://swapi.dev/api/species/2/. This is problematic for two reasons.

First, if clients have these direct backend URLs, they can bypass your API Management instance completely. Every security policy, rate limit, and authentication check you've configured becomes worthless because attackers can just go around your gateway.

Second, from a branding and control perspective, you want all API interactions to go through your gateway. If someone's using your API service, they should be hitting your endpoints, not discovering the backend service you're proxying.

**Performance and Respect**: There's also a performance consideration. SWAPI is a free public service provided for the developer community. It has rate limiting based on IP address to prevent abuse. When you use API Management, all requests appear to come from your APIM instance's IP address. This means you could hit the rate limit much faster than individual users would. Plus, it's simply respectful to reduce load on free services by implementing caching.

## Building the Solution with Policies

Let's walk through how we solve these problems using API Management policies.

First, we create an API in API Management that proxies to SWAPI. The backend URL is set to https://swapi.dev/api, and we configure our API to be accessible through our API Management gateway URL with a suffix like "swapi". We define operations matching the backend API structure, such as a GET operation for /people/{personId} that retrieves information about specific Star Wars characters.

Now comes the interesting part: applying policies to secure and optimize this API.

## Response Caching Policy

The first policy we apply is response caching. This is an inbound policy because cache lookup happens before we consider calling the backend.

We configure the cache-lookup policy with a duration of 86,400 seconds, which is 24 hours. Why such a long cache duration? Because Star Wars character data never changes! Luke Skywalker's height isn't going to be different tomorrow than it is today.

Here's what happens when caching is enabled: The first time someone requests information about character number 3, API Management checks its cache, doesn't find it, forwards the request to SWAPI, receives the response, and stores it in cache before returning it to the client. Every subsequent request for character 3 within the next 24 hours comes directly from cache. The backend never gets called, which reduces latency dramatically and eliminates load on the SWAPI service.

This is a powerful optimization pattern. Not only does it improve response times for your users, but it protects the backend from traffic spikes and reduces costs if the backend service charges per call.

## Header Manipulation Policies

Next, we address the security issue with the Server header. This requires an outbound policy because we're modifying the response after the backend returns it.

We use the set-header policy configured to delete the Server header entirely. The action is "delete", and the header name is "Server". When this policy executes, API Management strips out the nginx server header from the response, preventing that information from reaching the client.

But we don't just remove headers; we can add them too. For identification and troubleshooting purposes, we add our own custom header called "x-server" with the value "swapi-apim". This makes it clear that responses are coming through our API Management instance. It helps with debugging and provides a way to verify that our policies are actually executing.

Header manipulation policies have several actions available: delete removes a header, override replaces a header's value, append adds a value to an existing header, and skip means only set the header if it doesn't already exist. Understanding these actions is important for the AZ-204 exam.

## Response Body Transformation

The most sophisticated policy we implement is URL rewriting in the response body. This addresses the problem of backend URLs appearing in the response.

For this, we use the find-and-replace policy, which performs string substitution on the response body. We configure it to find every occurrence of "swapi.dev/api" and replace it with our API Management URL, something like "your-apim-name.azure-api.net/swapi".

This is an outbound policy because it processes the response body after the backend returns it. When SWAPI returns JSON containing URLs like https://swapi.dev/api/species/2/, our policy transforms them to https://your-apim-name.azure-api.net/swapi/species/2/.

Now clients only see your API gateway URLs. They can't bypass your security policies by calling the backend directly, because they don't even know the backend exists.

This policy is particularly useful when proxying third-party APIs or when you want to hide implementation details about your backend services.

## Testing the Policies

When you test the API after applying these policies, the behavior changes completely compared to calling the backend directly.

First, without a valid subscription key, requests to your API Management endpoint return a 401 Unauthorized response. This is because the API is published through a product that requires subscription key authentication. The subscription key must be passed in the Ocp-Apim-Subscription-Key header.

When you provide a valid subscription key, the request succeeds, and you can verify that all policies are working correctly. The Server header is gone from the response, your custom x-server header appears with the value "swapi-apim", and every URL in the JSON response points to your API Management domain instead of swapi.dev.

If you make the same request again, the second response is even faster because it's served from cache. API Management doesn't even contact the backend; it returns the cached response immediately.

## The Challenge of Complete API Coverage

Here's an interesting challenge that arises from our URL rewriting: The response contains URLs to related resources. For example, character data includes references to their home planet, species, and films they appeared in. We've rewritten all these URLs to point to our API Management instance.

But what happens when someone tries to follow those links? If we only defined the /people/{personId} operation in our API, requests to /planets/8 or /species/2 will fail. API Management doesn't have those operations configured, so it returns a 404 not found error.

This raises an important architectural consideration: When you proxy an API through API Management, you need to think about the complete API surface. You have several options. You could define all the backend operations in your APIM, giving you full control over policies for each operation. You could use a wildcard operation that forwards everything to the backend. Or you could be selective and only expose certain operations, intentionally restricting what clients can access.

In production scenarios, this requires careful planning. You're not just configuring one endpoint; you're thinking about the entire API contract and user experience.

## API Management Policies and the AZ-204 Exam

Now let's connect all of this to the Azure AZ-204 Developer Associate certification. API Management policies are a key topic in the exam, specifically under the "Implement API Management" objective.

### Policy Execution Flow

For the exam, you need to understand the complete policy execution flow. Requests progress through four policy sections in order:

**Inbound policies** execute first, before the backend is called. These can modify the request, perform authentication checks, look up cached responses, or enforce rate limits. Inbound policies can completely short-circuit the call and prevent the backend from being contacted at all, such as when serving cached responses or returning errors for rate-limited requests.

**Backend policies** execute when forwarding to the backend service. These are less commonly used but can modify the backend URL or request properties. A common use case is routing to different backend servers based on conditions like environment or request properties.

**Outbound policies** execute after the backend responds but before the response reaches the client. This is where you transform responses, manipulate headers, store responses in cache, or modify the response body. In our example, all our security policies were outbound policies.

**On-error policies** execute when an error occurs at any stage. These handle exceptions, format error responses consistently, and log errors for troubleshooting.

Understanding this flow is critical. The exam may present scenarios where you need to choose which section to place a policy in, or you may need to understand why a policy isn't working because it's in the wrong section.

### Important Policies for the Exam

Several specific policies appear frequently on the AZ-204 exam:

**Caching policies** include cache-lookup and cache-store. These reduce backend load and improve performance. You can configure caching to vary by query parameters, headers, or other request properties. In our example, we cached for 24 hours, but the duration should be based on how frequently the data changes.

**Rate limiting policies** prevent API abuse. The rate-limit policy restricts calls per time period, like 100 calls per minute. The quota policy limits total calls over longer periods, like 10,000 calls per month. These policies can be keyed by subscription, IP address, or custom values. Rate limiting is especially important for the exam because Microsoft emphasizes API protection and fair usage.

**Authentication policies** include validate-jwt for JWT token validation, which is crucial when integrating with Azure AD or other identity providers. The validate-jwt policy can verify token signatures, check claims, ensure tokens haven't expired, and enforce that specific audiences or issuers are present.

**Transformation policies** include set-header for header manipulation, set-body for body transformation, find-and-replace for string substitution, and json-to-xml or xml-to-json for format conversion. These let you adapt legacy APIs to modern standards or vice versa.

**Security policies** include ip-filter for allowing or denying requests from specific IP ranges, cors for managing cross-origin requests, and check-header for validating required headers.

### Policy XML Structure

For the exam, you should be comfortable reading and writing basic policy XML. The structure follows this pattern:

```xml
<policies>
    <inbound>
        <base />
        <!-- Inbound policies -->
    </inbound>
    <backend>
        <base />
        <!-- Backend policies -->
    </backend>
    <outbound>
        <base />
        <!-- Outbound policies -->
    </outbound>
    <on-error>
        <base />
        <!-- Error policies -->
    </on-error>
</policies>
```

The base tag is crucial. It explicitly calls parent scope policies. Policies before the base tag execute before parent policies, and policies after it execute after. If you omit the base tag entirely, parent policies don't execute at all, which is occasionally useful but usually not what you want.

### Common Exam Scenarios

Let me walk you through some typical exam question patterns:

**Scenario: Rate Limiting by Subscription**
"You need to configure API Management to limit each subscription to 100 calls per minute."

The solution uses the rate-limit-by-key policy in the inbound section. You configure calls to 100, renewal period to 60 seconds, and counter-key to the subscription ID. The policy expression looks like: counter-key="@(context.Subscription.Id)". Policy expressions use C# syntax and are denoted by the @ symbol.

**Scenario: JWT Validation with Azure AD**
"Ensure all API calls include a valid JWT token issued by Azure AD."

The solution uses the validate-jwt policy in the inbound section. You configure it with your Azure AD tenant's OpenID configuration URL, specify the audience claim to match your API application ID, and optionally check required claims like roles or scopes.

**Scenario: Conditional Backend Routing**
"Route API requests to a staging backend for test subscriptions and production backend for regular subscriptions."

The solution uses the set-backend-service policy with a choose/when condition checking the subscription ID or product. Different conditions set different backend URLs, allowing you to use one API configuration for multiple environments.

**Scenario: Response Transformation**
"Remove sensitive headers from backend responses before returning to clients."

The solution uses set-header policies in the outbound section with the delete action. You can remove multiple headers by applying multiple set-header policies. Common headers to remove include Server, X-Powered-By, X-AspNet-Version, and any proprietary headers that reveal implementation details.

### Security Best Practices

The exam emphasizes security best practices, and several patterns come up repeatedly:

**Hide Backend Implementation Details**: Never expose server software, framework versions, or technology stacks in responses. Use header manipulation policies to remove revealing headers. Return consistent error messages that don't leak stack traces or file paths. In our lab, we removed the nginx Server header to hide the backend server software.

**Prevent Backend Bypass**: If clients can call your backend directly, they circumvent all your API Management policies. Use URL rewriting to hide backend URLs from responses. Implement network security rules that only allow traffic from your API Management instance's IP to reach the backend. In our lab, the find-and-replace policy ensured clients only saw API Management URLs.

**Respect Backend Rate Limits**: Use caching to reduce backend load, implement your own rate limiting at the API Management level, and cache responses for appropriate durations based on data volatility. In our lab, we cached for 24 hours because Star Wars data never changes, but for dynamic data, you'd use much shorter cache durations.

### Products and Subscriptions

Remember that policies work in conjunction with products and subscriptions. APIs are added to products, products require subscriptions for access, and subscription keys are passed in the Ocp-Apim-Subscription-Key header. Without a valid subscription key, requests return 401 Unauthorized.

This product/subscription model is how you implement different service tiers, like free, standard, and premium. Each product can have different policies, particularly around rate limiting and quotas. The free product might limit calls to 100 per day, while the premium product allows unlimited calls.

### Integration with Other Azure Services

API Management doesn't exist in isolation. For the exam, understand how it integrates with other Azure services:

**Azure AD** provides authentication via JWT tokens. The validate-jwt policy integrates with Azure AD to authenticate users and service principals.

**Azure Key Vault** stores secrets like backend credentials or API keys. API Management can retrieve secrets from Key Vault using named values with Key Vault references, preventing secrets from being stored in policies or configuration.

**Azure Monitor and Application Insights** collect logs and metrics from API Management. You can send request/response data, performance metrics, and custom events to Application Insights for monitoring and troubleshooting.

**Azure Functions** can serve as backends for APIs. API Management can front Azure Functions, adding authentication, rate limiting, and caching to serverless functions.

## Practical Skills for the Exam

To succeed on the AZ-204 exam's API Management questions, you should practice several hands-on skills:

Navigate the Azure Portal's API Management interface confidently. Know where to find the policy editor, how to switch between visual designer and XML editor, and how to access the test console.

Apply common policies like caching, rate limiting, header manipulation, and JWT validation. Understand not just what they do but when to use each one.

Test policies using the built-in test console in the Azure Portal. This is invaluable for verifying policy behavior without external tools.

Understand policy scope and inheritance. Practice applying policies at different levels and using the base tag to control execution order.

Configure products and subscriptions. Know how to add APIs to products, generate subscription keys, and test with and without authentication.

Troubleshoot policy errors. The policy editor provides validation, but runtime errors require analyzing logs and understanding the policy execution flow.

## Key Takeaways

Let me summarize the critical points about API Management policies:

First, policies modify API behavior without changing backend code. This is the fundamental value proposition. You can add security, caching, transformation, and more without touching your backend services.

Second, understand the four policy sections: inbound, backend, outbound, and on-error. Know what each section is for and when policies execute.

Third, policies can be applied at multiple scopes: global, product, API, and operation. More specific scopes can override broader scopes, and the base tag controls inheritance.

Fourth, common policies you must know include caching, rate limiting, header manipulation, JWT validation, and response transformation. These appear frequently on the exam.

Fifth, security policies help hide implementation details, prevent backend bypass, and enforce authentication and authorization.

Sixth, the base tag controls policy inheritance. Its position determines when parent policies execute relative to your policies.

Seventh, subscription keys enforce authentication at the product level. The Ocp-Apim-Subscription-Key header carries the subscription key.

Finally, policy expressions use C# syntax for dynamic values. The context object provides access to request, response, user, subscription, and other runtime information.

## Final Thoughts

API Management policies are powerful tools for creating a secure, performant, and flexible API gateway layer. They embody the principle of separation of concerns: your backend services focus on business logic, while API Management handles cross-cutting concerns like security, rate limiting, caching, and transformation.

For the AZ-204 exam, policies represent a significant portion of the API Management objective. The exam tests both conceptual understanding and practical knowledge. You need to know when to use which policy, how to configure them correctly, and how to troubleshoot when things don't work as expected.

The hands-on practice is essential. Reading about policies helps, but actually configuring them in the Azure Portal, testing them, and seeing how they affect API behavior cements your understanding. Try creating APIs that use multiple policies at different scopes, experiment with policy expressions, and intentionally create problematic configurations so you learn to recognize and fix them.

As you continue your AZ-204 preparation, think about how policies integrate with other Azure services. API Management doesn't stand alone; it's part of a broader Azure ecosystem. How do policies work with Azure AD for authentication? How does caching interact with Azure Cache for Redis? How do policies support microservices architectures running on Azure Kubernetes Service?

These connections demonstrate the holistic thinking that the AZ-204 certification validates. It's not just about knowing individual services; it's about understanding how they work together to build complete cloud solutions.

Thanks for listening to this episode on API Management policies. I hope this gives you a solid foundation for working with policies and preparing for the AZ-204 certification. Good luck with your studies!
