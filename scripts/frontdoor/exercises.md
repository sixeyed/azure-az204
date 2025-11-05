# Azure Front Door - Exercises Narration Script

## Exercise 1: Exploring and Creating Front Door

Let's start by exploring Front Door in the Azure Portal. If you navigate to create a new resource and search for "front door", you'll see the option for Front Door and CDN profiles - Microsoft has unified these services under one interface.

When you click Create and choose Quick Create, you'll notice several important options. First, there are tier choices that prioritize either performance or security. The Standard tier focuses on content delivery and basic load balancing. The Premium tier adds comprehensive security features including Web Application Firewall integration, making it suitable for production scenarios with strict security requirements.

Front Door supports many origin types including Azure Container Instances, API Management, Application Gateway, and custom origins. You can enable caching on static resources simply by checking a box, which can dramatically improve performance and reduce costs for content that doesn't change frequently.

However, for this lab, we'll use the Azure CLI to create Front Door. This gives us more control over the configuration, better repeatability, and helps you understand exactly what's being created at each step.

## Exercise 2: Creating the Front Door Profile

Let's begin by creating a resource group and Front Door profile. We're creating a resource group named "labs-frontdoor" in the East US region with the courselabs tag for easy identification.

Now we'll create the Front Door profile using the Premium SKU to support WAF functionality. The profile name is "labs" and we're specifying the Premium_AzureFrontDoor SKU. This command creates the top-level container for all our Front Door configuration - endpoints, routes, origin groups, and security policies will all be configured under this profile.

The profile creation takes a couple of minutes because Azure is provisioning the global infrastructure needed to support Front Door's worldwide presence.

## Exercise 3: Deploying Backend Applications

Front Door needs backend services to route traffic to. We'll deploy two Azure Container Instances running the same application in different regions. This simulates a real-world scenario where you have regional deployments for redundancy and performance.

For the first container in East US, we're deploying a container named "simple-web-1" using the courselabs simple-web image version 6.0, exposing port 80, and setting a DNS name label. The --no-wait flag starts the deployment asynchronously so we don't have to wait for it to complete.

For the second container in West US, we're deploying "simple-web-2" with the same image but in a different region and with a different DNS name. The --no-wait flag lets both deployments proceed in parallel, saving time.

These two containers represent your multi-region application deployment. In production, you might have dozens or hundreds of origins across multiple regions, but the pattern is the same.

## Exercise 4: Understanding Front Door Components

While the containers are starting, let's explore the Front Door Profile in the Azure Portal. Understanding the component hierarchy and relationships is crucial for working with Front Door effectively.

Front Door Manager is where you create endpoints. These endpoints are subdomains under azurefd.net or your custom domains that serve as the entry point to your application. Clients connect to the endpoint URL, and Front Door handles routing the request to the appropriate backend.

Origin groups represent collections of your backend servers. Each endpoint refers to an origin group, and each origin group can contain multiple origins - the actual application hosts. Origins within a group can be weighted for traffic distribution and prioritized for failover scenarios.

Routes link a frontend endpoint to a backend origin group. This is where the connection happens - when a request comes to your endpoint, the route determines which origin group should handle it. Routes can include path patterns, protocols, caching rules, and more.

Finally, Rule sets allow you to customize request processing, Security policies integrate Web Application Firewall protection, and Optimizations let you tune performance characteristics for specific routes or content types.

## Exercise 5: Configuring Backend Origins

Now let's configure our ACI containers as origins. Each application host becomes an origin in Front Door. Origins belong to an origin group, which defines shared settings like health probes and load balancing configuration.

First, we'll create the origin group named "simple-web". The probe configuration is critical - we're specifying that health checks should use GET requests over HTTP, check the root path, probe every 30 seconds, require 3 successful probes out of 4 samples before marking an origin healthy, and allow up to 50 milliseconds of additional latency before preferring a different origin.

These health check parameters ensure that Front Door only routes traffic to healthy origins and can quickly detect when an origin becomes unhealthy.

Now let's add our first container as an origin. First, we need to get its fully qualified domain name from the container's IP address configuration.

Then we add it to the origin group with specific configuration. We're setting priority to 1, which means this origin is a primary - lower numbers are preferred. The weight is 300, which controls traffic distribution when multiple origins have the same priority. We're enabling the origin and specifying HTTP on port 80. The origin-host-header parameter sets the Host header sent to the backend - this is important if your backend checks the Host header.

Now let's add the second container. After getting its FQDN, we create the origin with priority 1 but weight 1000 - much higher than the first container.

The weight configuration means that when both containers are healthy, approximately three-quarters of the traffic will go to container 2 (with weight 1000) and one-quarter will go to container 1 (with weight 300). This weighted distribution is useful for scenarios like blue-green deployments or gradually ramping up traffic to new infrastructure.

If you check the Portal now, you'll see the origin group with both containers listed. However, they're not yet serving traffic because we haven't created an endpoint and route to connect clients to the origins.

## Exercise 6: Configuring the Frontend

Front Door endpoints are the public domain names for your application. Let's create an endpoint named "simple-web" under our profile. This endpoint will be accessible at simple-web.some-hash.azurefd.net where the hash makes it globally unique.

Now we have a public endpoint URL, but it's not connected to our backend yet. The final piece is creating a route that connects the endpoint to the origin group.

We're creating a route with several important configuration options. The forwarding-protocol is set to HttpOnly because our ACI containers don't support HTTPS - in production, you'd typically use HTTPS for security. We're naming the route "simple-web-route" and connecting it to our "simple-web" origin group. The supported-protocols parameter is set to Http, and we're disabling HTTPS redirect since we're not using HTTPS. We're linking to the default domain that Front Door provides. And we're enabling compression so browsers that support it will receive compressed responses, improving performance especially for text-based content.

After the route provisions, check the Portal. You should see green checkmarks with "Provision succeeded" for your endpoint, route, and origin group. The entire Front Door configuration is now active and ready to serve traffic.

Browse to the endpoint URL and refresh several times. You should see traffic being load balanced between the two containers, with most requests going to the container with the higher weight. You might see the container name or region information in the response, confirming which backend served each request.

## Exercise 7: Applying WAF Security Rules

The Premium SKU of Front Door supports the same Web Application Firewall functionality as Application Gateway. This provides protection against common web exploits and vulnerabilities.

Let's create a WAF policy in Prevention mode. Prevention mode actively blocks malicious requests, as opposed to Detection mode which just logs them. We're naming it "simplewebwaf" and using the Premium_AzureFrontDoor SKU to match our Front Door profile.

The WAF policy is a separate resource in your resource group, not directly attached to the Front Door profile. This separation allows you to reuse WAF policies across multiple endpoints or even multiple Front Door profiles.

The policy starts without any rules configured. We need to select managed rulesets for protection. Let's see what's available using the CLI to list managed rule definitions.

The two most useful rulesets are the Microsoft Default Rule Set, which provides comprehensive OWASP Top 10 protection covering SQL injection, cross-site scripting, and other common attacks, and the Bot Manager Rule Set, which blocks known bad bots while allowing legitimate bots like search engine crawlers.

Let's add both rulesets to our policy. We're adding the Microsoft Default Rule Set version 1.1 and the Microsoft Bot Manager Rule Set version 1.0.

You can view all the individual rules within these rulesets in the Portal by opening the WAF policy and selecting Managed rules. You'll see hundreds of rules covering various attack patterns, each with configurable actions.

Now let's apply the WAF to our endpoint by creating a security policy. This command requires resource IDs rather than names, so we need to query for them first.

We're getting the endpoint ID and the WAF policy ID, then creating a security policy that links them together. This associates the WAF rules with the specific endpoint.

Once provisioned, the WAF is actively protecting your application. Let's test it with a simulated SQL injection attack. We're using curl with a malicious-looking query string that includes SQL injection patterns.

You'll receive a 403 Forbidden response with a message saying the request is blocked. The WAF detected the attack pattern and rejected the request before it ever reached your backend. Your application is now protected.

## Lab Challenge

Now it's your turn to apply what you've learned. Deploy a new ACI container with the Pi application - this is a compute-intensive application that calculates digits of pi. Use the command to create a container in your resource group with the kiamol/ch05-pi image, exposing port 80 with public IP, and running a specific command line.

Your challenge is to publish this Pi application through Front Door with its own endpoint URL. You'll need to follow similar steps: create an origin group for the Pi application, add the container as an origin, create a new endpoint with a different name, and configure a route connecting the endpoint to the origin group.

This exercise will reinforce what you've learned and ensure you can set up Front Door independently without step-by-step instructions. Take your time and refer back to the previous exercises if needed.

## Cleanup

When you're finished experimenting with Front Door, clean up the resources to avoid ongoing charges. We're using the az group delete command with the -y flag to skip confirmation and --no-wait to return immediately.

Resource group deletion is asynchronous and can take several minutes, but you don't need to wait for it to complete.

## Key Takeaways

Azure Front Door provides global load balancing and content delivery with sophisticated routing capabilities. You can distribute traffic across origins using weighted routing, priority-based failover, and health probe monitoring.

The origin group concept allows you to manage collections of backend servers as a unit, with shared health check and load balancing configuration. Routes connect public endpoints to origin groups with configurable protocols, caching, and compression.

Web Application Firewall integration in the Premium tier provides enterprise-grade security with managed rulesets covering OWASP Top 10 and bot protection. The WAF operates at the edge before traffic reaches your backends, providing defense in depth.

Front Door's global presence means users connect to the nearest edge location, reducing latency. Backend selection is intelligent, considering health status, priority, weight, and latency to choose the optimal origin.

Understanding Front Door's architecture and capabilities is essential for the AZ-204 exam and for building globally distributed applications on Azure.
