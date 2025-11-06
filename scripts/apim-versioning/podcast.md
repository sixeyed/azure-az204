# API Management: API Changes & Versioning - Podcast Script

## Welcome and Introduction

Welcome to this episode on API versioning and revisions in Azure API Management. Today we're exploring one of the most critical aspects of professional API design: managing changes while maintaining backward compatibility with existing clients.

Whether you're preparing for the Azure AZ-204 certification or working with APIs in production, understanding how to evolve APIs safely is an essential skill. This episode will teach you how Azure API Management supports both non-breaking revisions and breaking version changes.

## The Challenge of API Changes

Let's start with a fundamental question: What happens when you need to change a published API?

APIs represent explicit contracts between your service and its consumers. When you publish an API, developers build their applications against that contract. They depend on specific endpoints, parameter structures, and response formats. Their code makes assumptions based on your API's behavior.

But requirements change. You discover bugs that need fixing. Users request new features. Security vulnerabilities require updates. Your data model evolves. The question isn't whether your API will change, but how you manage those changes without breaking existing client applications.

This is where API versioning becomes critical. Without a proper versioning strategy, you face an impossible choice: either freeze your API forever, never improving it, or make changes that break client applications. Neither option is acceptable in professional software development.

A well-designed versioning scheme allows you to make necessary changes under a new version while continuing to support older versions. This gives your clients time to migrate at their own pace, on their own schedules. You can innovate without disrupting existing users.

## Revisions vs Versions: A Critical Distinction

Azure API Management supports two types of changes, and understanding the difference is crucial both for the AZ-204 exam and for real-world API design.

**Revisions** are for non-breaking changes. These are modifications that existing clients can handle without any code updates. A classic example is adding optional parameters to an operation. When you add optional parameters, clients that don't send them simply get default behavior. Their code continues working exactly as before because the change is backward compatible.

Think about it: if your API returns random numbers between 1 and 100, and you add optional "min" and "max" parameters to let clients specify the range, existing clients that don't send those parameters still get numbers between 1 and 100. Nothing breaks. They just don't benefit from the new feature until they choose to update their code.

Other examples of revision-level changes include adding new optional response fields, improving error messages, optimizing performance, or fixing bugs that don't affect the API contract. The key characteristic is that existing clients continue working without modification.

**Versions**, on the other hand, are for breaking changes. These are modifications that would cause existing client code to fail if applied to the current API. Breaking changes include making optional parameters required, changing the structure of responses, removing fields that clients depend on, or changing the data types of parameters or responses.

For example, if you decide that the min and max parameters should be mandatory and you want to validate them properly, that's a breaking change. Existing clients that don't send those parameters will start receiving 400 Bad Request errors. Their code isn't prepared to handle those errors, so they break.

When you publish a breaking change, you create a new version of the API. Both versions run simultaneously. Existing clients continue using version 1.0, while new clients can adopt version 2.0. You give your consumers time to migrate when it's convenient for them, rather than forcing immediate updates.

## Versioning Schemes in API Management

API Management supports three versioning schemes, each with different trade-offs. For the AZ-204 exam, you need to understand when to use each one.

**Header-based versioning** requires clients to specify the API version in an HTTP header, commonly named something like "x-api-version". With header versioning, the URL path stays clean and consistent across versions. The same URL path can serve different versions based on the header value.

The advantage is that URLs remain stable and readable. The disadvantage is that versioning isn't visible in URLs, which can make debugging more complex. You need to inspect headers to understand which version a request is using. Web browsers don't make it easy to send custom headers, so header versioning works better for API-to-API communication than for browser-based access.

**Query string versioning** includes the version as a query parameter, like "?api-version=2.0". This makes versioning explicit in every URL, which helps with debugging and logging. URLs are self-documenting because you can see the version at a glance.

However, query string versioning can complicate caching because URLs differ between versions. It also makes URLs longer and slightly less clean. But the explicitness is often worth these trade-offs, especially for debugging and troubleshooting.

**Path-based versioning** embeds the version in the URL path itself, like "/v1/api/resource" versus "/v2/api/resource". This is extremely visible and explicit. Different versions have completely different URL structures.

The advantage is absolute clarity. Every URL screams which version it belongs to. The disadvantage is that it requires more configuration in your API gateway and can lead to more complex routing rules. It also makes version identifiers part of your permanent URL structure, which some designers consider inelegant.

In our scenario, we use header-based versioning with the "x-api-version" header. This keeps URLs clean while still providing clear version identification.

## Building a Versioned API: The Random Number Generator

Let's walk through a practical example that demonstrates both revisions and versions. We'll build a Random Number Generator API that evolves through multiple changes.

We start with version 1.0, which has a simple contract: call the /rng endpoint, and you get back a random number between 1 and 100. The API is straightforward, with no parameters required.

To deploy this in Azure, we use an Azure App Service with the Standard SKU. The Standard tier is important because it provides deployment slots, which we'll need to run multiple versions simultaneously. We deploy our version 1.0 code to the main production slot of the App Service.

In API Management, we create the API from an OpenAPI specification that describes the contract. The crucial decision happens at creation time: we enable versioning immediately, even for version 1.0. This is a best practice. Don't wait to add versioning until you already have consumers depending on an unversioned API. Start with version 1.0, clearly marked as such.

We set the version identifier to "1.0", choose header-based versioning, and specify "x-api-version" as the header name. Now every request to this API must include the version header. This might seem like extra overhead for version 1.0, but it establishes the contract pattern from day one.

The API Management instance knows where to route requests: we configure the backend URL to point to our App Service's production slot URL. When a client sends a request with "x-api-version: 1.0", API Management forwards it to the App Service production slot.

## Adding Non-Breaking Changes with Revisions

After version 1.0 is live and clients are using it, we receive a feature request: users want to control the range of random numbers. Instead of always getting numbers between 1 and 100, they want to specify minimum and maximum values.

This is a perfect candidate for a revision because we can make it backward compatible. We'll add optional "min" and "max" query parameters. Clients that send these parameters get numbers in their specified range. Clients that don't send them continue getting numbers between 1 and 100, exactly as before.

First, we need somewhere to run the new code. We create an App Service deployment slot called "blue". Deployment slots are essentially separate instances of your App Service, each with its own URL. The blue slot runs independently of the production slot, allowing us to test the new code without affecting live traffic.

We deploy version 1.1 of our application code to the blue slot. This version includes the logic to accept min and max parameters and generate numbers within the specified range, or default to 1-100 if those parameters aren't provided.

Back in API Management, we create a revision of version 1.0. Revisions are tracked separately from versions. They represent iterative improvements to the same API contract. We add a description explaining what changed: "Now you can set the range of the random number using min and max parameters in the query string."

In the revision's settings, we point the backend URL to the blue deployment slot URL instead of the production slot URL. This is how we route different revisions to different backend implementations, all within the same API version.

We update the API definition to include the min and max query parameters, explicitly marked as optional. This is critical: they must be optional to maintain backward compatibility. Required parameters would be a breaking change.

When we test the revision, we can send requests with min and max parameters and get numbers in that range. We can also send requests without those parameters and get numbers between 1 and 100. Both patterns work, confirming backward compatibility.

API Management provides a special URL syntax for testing revisions before making them current. The URL includes a revision marker like ";rev=2", allowing you to test the new revision while the original revision continues serving live traffic.

Once we've validated the revision, we make it current. Now the standard version 1.0 URL routes to the new revision with optional parameters. The transition is seamless. Existing clients continue working exactly as before, while new clients can start using the min and max parameters immediately.

## Publishing Breaking Changes with Versions

The optional parameters work, but they're not ideal from a design perspective. We can't properly validate them. What if a client sends min=1000 and max=1? What if they send letters instead of numbers? Without validation, we might return nonsensical results or cause errors in the backend.

We want to add validation: verify that min is less than max, ensure both are integers, and return clear error messages when validation fails. But here's the problem: this is a breaking change.

Version 1.0 clients never expected to receive 400 Bad Request error responses from this endpoint. If we add validation that can return 400 errors, we're changing the contract. Their code might not handle these error responses properly. This violates the backward compatibility promise.

The professional solution is to create version 2.0 as a new API version with a breaking change. We'll make min and max required parameters with proper validation.

We deploy the version 2.0 code to a new deployment slot called "green". Now we have three active deployments: production running version 1.0 revision 1, blue running version 1.0 revision 2, and green running version 2.0.

In API Management, we create a new version of the API. We specify version 2.0, use the same header-based versioning scheme, and import an updated OpenAPI specification that reflects the new contract: min and max are required parameters, not optional.

The backend URL for version 2.0 points to the green deployment slot. Now API Management can route requests to different App Service deployments based on the version header value.

When clients send requests with "x-api-version: 2.0", they must include min and max parameters. If they omit them, they receive a 400 error response. This is acceptable because version 2.0 is explicitly a new contract. Clients adopting version 2.0 know they need to provide these parameters.

The beauty of this architecture is that both versions run simultaneously. Clients using "x-api-version: 1.0" continue working exactly as before, with optional parameters. Clients using "x-api-version: 2.0" get required parameters with validation. Each version can evolve independently through its own revisions.

You can support both versions as long as necessary, giving clients months or even years to migrate if needed. Eventually, you might deprecate version 1.0, but you control that timeline based on actual client migration, not arbitrary deadlines.

## The Blue-Green Deployment Question

This architecture raises an interesting question about deployment strategies. App Service deployment slots support swapping, where you instantly switch the production and staging slots. This is the foundation of blue-green deployments: you deploy the new version to staging, test it thoroughly, then swap it to production instantly with zero downtime.

But in our architecture, API Management has backend URLs explicitly configured to point to specific slot URLs. Revision 2 points to the blue slot URL, and version 2.0 points to the green slot URL. If you swap slots at the App Service level, the blue slot becomes production and vice versa, but API Management is still pointing to the URL labeled "blue".

This means the traditional slot swap mechanism doesn't integrate seamlessly with explicit URL configuration in API Management. You'd need to either update the API Management backend URLs after swapping, use different naming conventions that don't depend on slot names, or avoid swapping altogether and just update which revision or version is current.

This is a real architectural consideration in production systems. There's no single right answer; it depends on your deployment processes, automation capabilities, and tolerance for manual configuration updates. But it's important to think through these integration points when combining Azure services.

## API Management Versioning and the AZ-204 Exam

Now let's connect this to the Azure AZ-204 Developer Associate certification. API versioning is a key topic under the "Implement API Management" exam objective.

### Understanding the Distinction for the Exam

The most important concept for the exam is understanding when to use revisions versus versions. This comes up repeatedly in scenario-based questions.

If the exam describes adding optional fields to a response, that's a revision. If it describes changing required parameters or modifying response schemas in incompatible ways, that's a version.

If the question says "existing clients should continue working without changes," you need a revision. If it says "clients will need to update their code," you need a version.

This distinction might seem subtle, but it's the foundation of professional API management. The exam tests whether you understand the difference and can apply it to realistic scenarios.

### Versioning Schemes

The exam may ask you to choose the appropriate versioning scheme for different scenarios. Understand the trade-offs:

Header-based versioning keeps URLs clean and stable, but makes versioning less visible. It works well for service-to-service communication where you control both sides.

Query string versioning makes versions explicit in URLs, which helps with debugging and logging. It's more visible but makes URLs longer.

Path-based versioning is extremely explicit and visible, but requires more routing configuration and makes versions part of your permanent URL structure.

For exam questions, look for clues about what's important in the scenario. If the question emphasizes URL stability, consider header-based. If it emphasizes debuggability or logging, consider query string. If it emphasizes clear separation between versions, consider path-based.

### Integration with Other Azure Services

The exam tests your understanding of how Azure services work together. This scenario demonstrates several integration points:

Deployment slots in App Service allow running multiple application versions simultaneously, each with its own URL.

API Management backend URLs can point to different deployment slots, enabling routing based on API versions or revisions.

OpenAPI specifications define API contracts that can be imported and updated in API Management.

Understanding these connections is crucial. The exam doesn't test services in isolation; it tests your ability to design complete solutions using multiple services together.

### Common Exam Scenarios

Based on actual exam questions, here are patterns you should be prepared for:

**Scenario: Adding Optional Features**
"A company needs to add new optional fields to their API response. Existing clients should continue to work without changes."

Solution: Create a new revision in API Management. Revisions maintain backward compatibility while allowing new clients to use additional features.

**Scenario: Breaking Changes**
"An API currently returns data as XML, but version 2.0 needs to return JSON instead. How should you implement this change?"

Solution: Create a new API version, not a revision. Changing response format is a breaking change that requires a new version and explicit client migration.

**Scenario: Testing in Production**
"You need to test a new API version in production without affecting existing users."

Solution: Deploy the new version to an App Service deployment slot, create a new API version in API Management pointing to that slot URL, and use versioning to route only test traffic to the new version.

**Scenario: Multiple Backend Environments**
"Route API requests to staging backend for test subscriptions and production backend for regular subscriptions."

Solution: Use API Management revisions or versions with different backend URLs, or use policies with conditional logic to route based on subscription properties.

### Practical Skills to Practice

For the exam, you should be comfortable with:

Creating APIs in API Management from OpenAPI specifications, enabling versioning at creation time, configuring backend URLs, creating revisions for non-breaking changes, creating versions for breaking changes, making revisions current, and testing APIs with different version identifiers.

You don't need to memorize exact Azure CLI commands, but you should understand what commands like "az webapp deployment slot create" and "az webapp deployment source config-zip" do and when you'd use them.

Understand the Azure Portal workflows as well. The exam sometimes includes screenshots or asks you to identify correct configuration steps in the portal interface.

### Best Practices for the Exam

Based on this scenario, remember these best practices:

**Version from the start**: Include versioning in your initial API design. Don't add it later when you already have unversioned clients. Start with version 1.0 explicitly marked as such.

**Use semantic versioning**: Major.Minor version numbers like 1.0, 1.1, 2.0 clearly communicate the scope of changes. Major version changes indicate breaking changes, minor version changes indicate new features with backward compatibility.

**Document changes**: Both revisions and versions should have clear descriptions explaining what changed. This helps teams understand API evolution and assists with troubleshooting.

**Test before promoting**: Use deployment slots and revisions to test changes before making them current. Don't push untested code directly to production through the primary API version.

**Support multiple versions**: Don't force immediate client migration. Support older versions during transition periods, giving clients time to update on their schedules.

### Policy Integration

While this scenario focuses on versioning mechanics, remember that in production systems, you'd typically combine versioning with policies. Different API versions might have:

Different rate limits, with more generous limits for newer versions that are more efficient.

Different authentication requirements, such as supporting legacy API keys for version 1.0 while requiring JWT tokens for version 2.0.

Different response transformations, such as converting between data formats or adding headers specific to each version.

Different caching strategies based on how frequently data changes in each version.

The exam may test your understanding of how policies and versioning work together.

## Key Takeaways

Let me summarize the critical points about API versioning in Azure API Management:

First, understand the fundamental distinction between revisions and versions. Revisions are for non-breaking changes that maintain backward compatibility. Versions are for breaking changes that require client updates. This distinction appears repeatedly on the exam and is crucial for real-world API design.

Second, enable versioning from the beginning. Start with version 1.0 explicitly, establishing the versioning pattern before you have clients dependent on unversioned APIs. This makes future changes much easier.

Third, understand the three versioning schemes: header-based, query string, and path-based. Each has trade-offs regarding URL stability, visibility, and debuggability. Choose based on your specific requirements.

Fourth, deployment slots enable running multiple versions simultaneously. Each slot has its own URL and can run different application code. This is how you support multiple versions without separate infrastructure.

Fifth, API Management backend URLs route to different deployments based on versions and revisions. This provides flexible traffic routing without changing client-facing URLs.

Sixth, OpenAPI specifications define API contracts that can be imported and updated. These specifications document your API structure and enable tooling and validation.

Finally, test thoroughly before making changes current. Use revision URLs and deployment slots to validate changes in production-like environments before exposing them to all clients.

## Final Thoughts

API versioning is one of those topics that seems simple in theory but has significant implications for real-world systems. The difference between doing versioning well and doing it poorly can determine whether your API is reliable and professional or constantly breaks client applications.

Azure API Management provides powerful tools for managing API evolution, but tools alone aren't enough. You need to understand the principles: what constitutes a breaking change, how to maintain backward compatibility, when to create new versions versus revisions, and how to give clients time to migrate.

For the AZ-204 exam, versioning is a significant topic because it demonstrates systems thinking. It's not just about configuring a service; it's about understanding API contracts, backward compatibility, and how different Azure services integrate to solve complete problems.

The hands-on practice is invaluable. Actually creating revisions, seeing how they behave differently from versions, routing traffic to different deployment slots, and testing with version headers cements your understanding in ways that reading documentation cannot.

As you continue your AZ-204 preparation, think about versioning in the context of complete Azure solutions. How does API versioning integrate with CI/CD pipelines? How do you automate version deployments? How do monitoring and logging work across multiple versions? How do you eventually deprecate old versions when clients have migrated?

These broader questions demonstrate the holistic thinking that the AZ-204 certification validates. It's about understanding not just individual services but complete patterns for building, deploying, and managing cloud applications professionally.

Thanks for listening to this episode on API versioning and revisions. I hope this gives you both the conceptual understanding and practical knowledge you need for the AZ-204 exam and for working with Azure API Management in production. Good luck with your studies!
