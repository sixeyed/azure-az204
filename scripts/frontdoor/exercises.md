# Azure Front Door

## Reference

Front Door acts like Application Gateway but it also has a global CDN. It can be integrated with the same WAF functionality and provides DDOS protection. It's the evolution of various load balancing and CDN services and is the preferred option now for the front end to your HTTP services, which can include Web Apps and API Management domains. Understanding Front Door's global presence, intelligent routing, and security capabilities is essential for building globally distributed applications on Azure.

## Explore & create Front Door

Create a new resource in the Portal and search for "front door" - select Front Door and CDN profiles, click Create and choose Quick Create. The tier choices prioritize performance or security - selecting the Premium tier gives you access to WAF policy configuration. Front Door supports lots of origins including ACI, APIM and AppGW. You can get caching on static resources just by ticking a box. We'll create Front Door using the CLI for better control and repeatability.

Start with a resource group and a Front Door profile. We're creating a resource group named "labs-frontdoor" in the East US region with the courselabs tag. Now we'll create the Front Door profile using the Premium SKU to support WAF functionality. The profile name is "labs" and we're specifying the Premium_AzureFrontDoor SKU. This command creates the top-level container for all our Front Door configuration. The profile creation takes a couple of minutes because Azure is provisioning the global infrastructure needed to support Front Door's worldwide presence.

---

## Deploying Backend Applications

Front Door needs backend services to route traffic to. We'll deploy two Azure Container Instances running the same application in different regions. This simulates a real-world scenario where you have regional deployments for redundancy and performance.

For the first container in East US, we're deploying using the simple-web image, exposing port 80, and setting a DNS name label. The --no-wait flag starts the deployment asynchronously so we don't have to wait for it to complete.

For the second container in West US, we're deploying with the same image but in a different region and with a different DNS name. The --no-wait flag lets both deployments proceed in parallel, saving time. These two containers represent your multi-region application deployment.

---

## Understanding Front Door Components

While the containers are starting, let's explore the Front Door Profile in the Azure Portal. Understanding the component hierarchy and relationships is crucial for working with Front Door effectively.

Front Door Manager is where you create endpoints - subdomains under azurefd.net or your custom domains that serve as the entry point to your application. Clients connect to the endpoint URL, and Front Door handles routing to the appropriate backend.

Origin groups represent collections of your backend servers. Each endpoint refers to an origin group, and each origin group can contain multiple origins - the actual application hosts. Origins within a group can be weighted for traffic distribution and prioritized for failover scenarios.

Routes link a frontend endpoint to a backend origin group. This is where the connection happens - when a request comes to your endpoint, the route determines which origin group should handle it. Routes can include path patterns, protocols, caching rules, and more.

Finally, Rule sets allow you to customize request processing, Security policies integrate Web Application Firewall protection, and Optimizations let you tune performance characteristics for specific routes or content types.

---

## Configuring Backend Origins

Now let's configure our ACI containers as origins. Each application host becomes an origin in Front Door. Origins belong to an origin group, which defines shared settings like health probes and load balancing configuration.

First, we'll create the origin group. The probe configuration is critical - we're specifying that health checks should use GET requests over HTTP, check the root path, probe every 30 seconds, require 3 successful probes out of 4 samples before marking an origin healthy, and allow up to 50 milliseconds of additional latency before preferring a different origin. These health check parameters ensure that Front Door only routes traffic to healthy origins.

Now let's add our first container as an origin. We need to get its fully qualified domain name from the container's IP address configuration, then add it to the origin group with specific settings. We're setting priority to 1, which means this origin is a primary. The weight is 300, which controls traffic distribution when multiple origins have the same priority. We're enabling the origin and specifying HTTP on port 80. The origin-host-header parameter sets the Host header sent to the backend.

Now let's add the second container with priority 1 but weight 1000 - much higher than the first container. The weight configuration means that when both containers are healthy, approximately three-quarters of the traffic will go to container 2 and one-quarter will go to container 1. This weighted distribution is useful for scenarios like blue-green deployments or gradually ramping up traffic to new infrastructure.

---

## Configuring the Frontend

Front Door endpoints are the public domain names for your application. Let's create an endpoint under our profile. This endpoint will be accessible at a globally unique URL under azurefd.net.

Now we have a public endpoint URL, but it's not connected to our backend yet. The final piece is creating a route that connects the endpoint to the origin group.

We're creating a route with several important configuration options. The forwarding-protocol is set to HttpOnly because our ACI containers don't support HTTPS. We're naming the route and connecting it to our origin group. The supported-protocols parameter is set to Http, and we're disabling HTTPS redirect. We're linking to the default domain that Front Door provides, and we're enabling compression so browsers that support it will receive compressed responses, improving performance especially for text-based content.

After the route provisions, check the Portal. You should see green checkmarks with "Provision succeeded" for your endpoint, route, and origin group. The entire Front Door configuration is now active and ready to serve traffic.

Browse to the endpoint URL and refresh several times. You should see traffic being load balanced between the two containers, with most requests going to the container with the higher weight.

---

## Applying WAF Security Rules

The Premium SKU of Front Door supports the same Web Application Firewall functionality as Application Gateway. This provides protection against common web exploits and vulnerabilities.

Let's create a WAF policy in Prevention mode. We're naming it and using the Premium_AzureFrontDoor SKU to match our Front Door profile. The WAF policy is a separate resource in your resource group, not directly attached to the Front Door profile. This separation allows you to reuse WAF policies across multiple endpoints.

The policy starts without any rules configured. We need to select managed rulesets for protection. Let's see what's available. The two most useful rulesets are the Microsoft Default Rule Set, which provides comprehensive OWASP Top 10 protection, and the Bot Manager Rule Set, which blocks known bad bots while allowing legitimate bots like search engine crawlers.

Let's add both rulesets to our policy. You can view all the individual rules within these rulesets in the Portal - you'll see hundreds of rules covering various attack patterns, each with configurable actions.

Now let's apply the WAF to our endpoint by creating a security policy. This command requires resource IDs rather than names, so we need to query for them first. We're getting the endpoint ID and the WAF policy ID, then creating a security policy that links them together.

Once provisioned, the WAF is actively protecting your application. Let's test it with a simulated SQL injection attack. You'll receive a 403 Forbidden response with a message saying the request is blocked. The WAF detected the attack pattern and rejected the request before it ever reached your backend. Your application is now protected.

---

## Lab

Deploy a new ACI container with the Pi application and publish this Pi application through Front Door with its own endpoint URL. You'll need to create an origin group for the Pi application, add the container as an origin, create a new endpoint with a different name, and configure a route connecting the endpoint to the origin group.

---

## Cleanup

When you're finished experimenting with Front Door, clean up the resources to avoid ongoing charges. Resource group deletion is asynchronous and can take several minutes, but you don't need to wait for it to complete.
