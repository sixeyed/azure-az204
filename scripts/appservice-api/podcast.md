# App Service for Distributed Apps - Podcast Script

## Welcome and Introduction

Welcome to this episode on using Azure App Service for distributed applications. Today we're exploring how to deploy and manage multiple interconnected applications within App Service, demonstrating patterns you'll encounter in microservices architectures and distributed systems.

Whether you're preparing for the Azure AZ-204 certification or building multi-tier applications in production, understanding how to deploy and configure distributed components on App Service is essential. This episode covers deployment automation, application configuration, scaling strategies, and cross-origin security.

## Understanding Distributed Applications on App Service

Let's start by clarifying what we mean by a distributed application in the context of App Service.

A distributed application consists of multiple components that work together but deploy and run independently. In a typical modern web architecture, you might have a REST API backend providing business logic and data access, a web frontend that consumes the API and renders the user interface, and perhaps additional components like background workers or specialized services.

Each component is its own application with its own codebase, deployment lifecycle, and configuration. But they need to communicate and work together as a cohesive system. The challenge is deploying these components to Azure in a way that's cost-effective, manageable, and properly configured.

App Service provides an elegant solution: you can run multiple applications on a single App Service Plan, sharing the underlying compute resources while maintaining logical separation between applications.

## Sharing an App Service Plan

One of App Service's most powerful features for cost optimization is the ability to run multiple web apps on a single App Service Plan.

Remember, an App Service Plan is the actual compute resource - one or more virtual machines that host your applications. When you create a plan with the B1 SKU and two workers, you're provisioning two virtual machine instances with specific CPU and memory allocations.

You can then create multiple web apps that all run on that same plan. If you have a REST API, a web frontend, and an admin interface, you could run all three on one App Service Plan. They share the CPU, memory, and storage of that plan.

This sharing dramatically reduces costs for development, testing, or low-traffic scenarios. Instead of paying for three separate App Service Plans, you pay for one. Instead of managing three separate infrastructure allocations, you manage one.

The applications remain logically separate with their own URLs, configuration, and deployment pipelines. But they share the underlying infrastructure. This is perfect for related components of the same system that don't need isolated resources.

In production, you might separate components onto different plans for performance isolation or independent scaling, but for many scenarios, sharing a plan is both practical and cost-effective.

## Automated Deployment with az webapp up

Let's walk through deploying a distributed application using one of App Service's most convenient deployment commands.

We start by creating an App Service Plan with the B1 SKU, Linux operating system, and two worker instances. This plan will host all our application components.

To deploy an application, we use the "az webapp up" command. This is a powerful shortcut that combines multiple operations into one command. You point it at a directory containing source code, specify the target resource group and App Service Plan, and it handles everything else: creating the web app resource, packaging your source code, uploading it to Azure, building the application on Azure using the appropriate build system, and starting the application.

For a .NET 6.0 API, we navigate to the source directory and run webapp up, specifying Linux as the operating system, dotnetcore:6.0 as the runtime, and a globally unique name for the web app.

Behind the scenes, Azure's Oryx build system detects that this is a .NET project, restores NuGet packages, compiles the code, and configures the web server. All of this happens automatically without configuring build pipelines or build scripts.

Within a few minutes, the API is live and accessible. When we test the /rng endpoint, it returns random numbers as expected. The Swagger documentation is automatically available, providing an interactive interface for exploring the API.

Next, we deploy the web frontend using the same process. We navigate to the web application's source directory and run webapp up again, specifying the same resource group and App Service Plan but a different web app name. Now we have two applications running on the same App Service Plan, sharing resources but with independent URLs.

## Application Configuration and Service Discovery

When we first test the web frontend, it fails to retrieve random numbers from the API. The web page shows an error indicating the API is unavailable and displays that it's trying to connect to localhost.

This reveals an important concept about App Service configuration. The application has default configuration in its source code that points to localhost, which is appropriate for local development. But in Azure, the web app can't access localhost - it needs the actual URL of the API app.

This is where App Service application settings come in. Application settings are environment variables that Azure injects into your application at runtime. They override configuration values in your application's files, allowing you to deploy the same code to different environments with different configurations.

In the Azure Portal, we navigate to the web app's Configuration section and add a new application setting. The key is "RngApi__Url" - notice the double underscore. In .NET Core, double underscores represent hierarchy in configuration. This setting maps to "RngApi:Url" in the application's configuration system.

The value is the full URL of our API app followed by the /rng path. When we save this configuration, Azure restarts the application to pick up the new setting.

Now when we test the web app, it successfully retrieves random numbers from the API. The two applications are communicating through the configuration we provided. This demonstrates the proper pattern for configuring distributed applications: use environment variables or application settings for environment-specific values like service URLs, connection strings, or API keys. Never hardcode these values in source code.

## Scaling Challenges and SKU Awareness

Let's discuss a subtle but important behavior when working with App Service Plans and automated deployment commands.

We initially created our App Service Plan with the B1 SKU and two workers. The B1 tier supports up to three instances, so we decide to scale to three workers for additional capacity.

When we run the command to update the worker count to three, it fails. The error message indicates that the SKU doesn't support three workers. But we created a B1 plan, which should support three workers. What happened?

When we query the App Service Plan details, we discover it's now on the Free F1 tier, not the B1 tier we created. The F1 tier only supports a single instance, which is why scaling failed.

Here's what happened: the webapp up command is convenient, but it has a side effect. It can modify existing App Service Plans, potentially downgrading them to the Free tier for cost efficiency. This behavior caught us by surprise because we expected our B1 plan to remain unchanged.

This teaches an important lesson about automated commands: understand what they do beyond their primary purpose. Commands that seem simple might have additional behaviors that affect your infrastructure.

To fix this, we update both the SKU and the worker count in a single command. First, we scale up to B1 again, which increases the maximum worker count to three. Then we scale out to three instances, distributing our applications across three virtual machine instances.

This incident demonstrates the distinction between scaling up and scaling out. Scaling up means changing the pricing tier to get different resources or features. Scaling out means adding more instances of the same tier.

## Observing Load Distribution

With three instances running, we can observe how Azure distributes traffic across them.

When we use the web application repeatedly, each request to the API might go to a different instance. Azure's built-in load balancer distributes incoming requests across all healthy instances in round-robin fashion or based on current load.

This automatic load distribution provides both scalability and availability. If one instance becomes unhealthy or slow, Azure automatically routes traffic to the other instances. Users experience consistent performance because multiple instances share the load.

Understanding load distribution is important for troubleshooting production issues. When you examine logs, requests might be handled by different instances, so you need to aggregate logs across all instances to see the complete picture.

## Cross-Origin Resource Sharing (CORS)

Now let's address a common security challenge when deploying distributed web applications: Cross-Origin Resource Sharing, or CORS.

Imagine we have a static single-page application - just HTML and JavaScript files - that calls our REST API. We deploy this static app to App Service as a separate web app. When users load the static app in their browser and click a button to fetch data from the API, they encounter an error.

The browser's developer console shows a CORS policy error: "Access to XMLHttpRequest has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource."

This is a security feature built into web browsers. By default, JavaScript code running on one domain cannot make requests to a different domain. This prevents malicious websites from making unauthorized requests to APIs on behalf of users.

In our case, the static web app runs on one domain, like static-app.azurewebsites.net, while the API runs on api-app.azurewebsites.net. These are different domains, so the browser blocks the request by default.

To allow legitimate cross-origin requests, we configure CORS settings on the API app. In the Azure Portal, the API app has a CORS configuration section where we can specify which origins are allowed to make requests.

We add the static app's URL to the allowed origins list. Now when the browser makes a preflight request to check if cross-origin calls are permitted, the API responds with headers indicating that requests from the static app's domain are allowed. The browser permits the actual request to proceed, and the application works correctly.

CORS configuration is critical for any API that will be called from browser-based applications hosted on different domains. It balances security - preventing unauthorized cross-origin requests - with functionality - allowing legitimate requests from trusted origins.

## App Service for Distributed Apps and the AZ-204 Exam

Let's connect these concepts to the Azure AZ-204 Developer Associate certification exam, where distributed App Service deployments appear frequently.

### Multi-App Deployments and Cost Optimization

The exam tests your understanding of cost optimization strategies. Running multiple applications on a single App Service Plan is a common scenario-based question.

For example, an exam question might describe a system with multiple related components and ask how to minimize infrastructure costs while maintaining separate deployments. The answer involves creating one App Service Plan and deploying multiple web apps to it.

Understanding when this strategy is appropriate versus when applications need separate plans for performance isolation or independent scaling is important for exam success.

### Application Configuration Best Practices

Configuration management is heavily tested on the AZ-204 exam. The exam emphasizes secure development practices, and proper configuration management is foundational.

Know that App Service application settings are injected as environment variables, overriding values in configuration files. This allows identical code to run in different environments with environment-specific configuration.

Understand the double underscore syntax for hierarchical configuration in .NET Core. This appears in exam questions about configuring applications correctly.

Know that sensitive values like connection strings should be stored in application settings or Azure Key Vault, never hardcoded in source code or committed to repositories.

### Scaling Concepts

Scaling questions are common on the exam. You need to understand both types of scaling and their constraints.

Scaling up means changing the pricing tier to get more resources per instance or access to additional features. This requires restarting applications and might have cost implications.

Scaling out means adding more instances of the same tier. This can be done without downtime and is ideal for handling increased traffic.

Know which pricing tiers support which scaling options. Free and Shared tiers have limited scaling. Basic supports manual scale-out. Standard and Premium support auto-scaling.

Understand that different tiers have different maximum instance counts. The B1 tier supports up to 3 instances, while higher tiers support many more.

### CORS Configuration

CORS appears on the exam in scenarios involving single-page applications, mobile app backends, or APIs called from JavaScript.

Understand why CORS exists: it's a browser security feature preventing unauthorized cross-origin requests.

Know how to configure CORS in App Service through the Portal or using Azure CLI commands.

Understand the security implications: allowing "*" as an origin is convenient but insecure because it permits requests from any domain. Production APIs should specify exact allowed origins.

### Deployment Automation

The exam tests your knowledge of different deployment methods and their appropriate uses.

Commands like "az webapp up" automate multiple steps, which is convenient but requires understanding what they do. The exam may present scenarios where automation commands have unexpected side effects, similar to how webapp up modified our App Service Plan SKU.

Know when to use different deployment methods: local Git for simple scenarios, external repositories for continuous deployment, containers for consistent runtime environments, and Azure DevOps for complex CI/CD pipelines.

### Common Exam Scenarios

Based on exam patterns, expect questions like:

"You have a web application and REST API that need to communicate. The API URL differs between development and production environments. How should you configure the web application?"

Solution: Use App Service application settings to inject the API URL as an environment variable, allowing the same code to run in both environments with different configurations.

"A single-page application cannot call your API in App Service. The browser console shows a CORS error. What configuration is needed?"

Solution: Configure CORS settings on the API App Service to allow requests from the single-page application's domain.

"Your App Service Plan is on the Free tier. You need to scale to three instances. What must you do first?"

Solution: Scale up to at least the Basic tier, which supports multiple instances. The Free tier only supports one instance.

"You need to deploy multiple microservices to Azure App Service while minimizing costs for a development environment. What approach should you use?"

Solution: Create a single App Service Plan and deploy all microservices as separate web apps on that plan, sharing compute resources.

## Key Takeaways

Let me summarize the critical points about distributed applications on App Service:

First, multiple web apps can run on a single App Service Plan, sharing compute resources for cost optimization while maintaining logical separation.

Second, application settings override configuration files, enabling environment-specific configuration without code changes.

Third, the "az webapp up" command automates deployment but can have side effects on existing resources that require awareness.

Fourth, scaling up changes the pricing tier and features available, while scaling out adds more instances of the same tier.

Fifth, CORS configuration is necessary for APIs called from browser-based applications on different domains, balancing security with functionality.

Finally, proper configuration management separates environment-specific values from code, using application settings for URLs, connection strings, and other environment-dependent values.

## Final Thoughts

Deploying distributed applications to Azure App Service demonstrates several important cloud development patterns: sharing infrastructure for cost efficiency, externalizing configuration for environment portability, understanding platform automation behaviors, and configuring security policies for cross-origin access.

For the AZ-204 exam, this topic is significant because it combines multiple exam domains: creating and configuring App Service, implementing proper configuration management, understanding scaling strategies, and addressing security concerns like CORS.

The hands-on experience with these patterns is essential. Actually deploying applications, troubleshooting configuration issues, experiencing scaling limitations, and resolving CORS errors provides practical knowledge that documentation alone cannot deliver.

As you continue your AZ-204 preparation, think about distributed applications in context: How do you design resilient multi-tier systems? How do you balance cost efficiency with performance isolation? How do you implement secure service-to-service communication? How do you troubleshoot issues in distributed systems?

These broader questions demonstrate the systems thinking that the AZ-204 certification validates. It's not just about deploying individual applications; it's about architecting complete, maintainable, secure, and cost-effective solutions.

Thanks for listening to this episode on App Service for distributed applications. I hope this gives you both the conceptual understanding and practical knowledge for the AZ-204 exam and for building distributed systems in Azure confidently. Good luck with your studies!
