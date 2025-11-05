# Azure Front Door - Exercises Narration Script

## Exercise 1: Exploring and Creating Front Door

Let's start by exploring Front Door in the Azure Portal. If you navigate to create a new resource and search for "front door", you'll see the option for Front Door and CDN profiles.

When you click Create and choose Quick Create, you'll notice several important options. First, there are tier choices that prioritize either performance or security. For production scenarios with security requirements, you'll want the Premium tier, which requires a WAF policy.

Front Door supports many origin types, including Azure Container Instances, API Management, and Application Gateway. You can enable caching on static resources simply by checking a box.

However, for this lab, we'll use the Azure CLI to create Front Door, giving us more control and repeatability.

## Exercise 2: Creating the Front Door Profile

Let's begin by creating a resource group and Front Door profile. We'll create a resource group named "labs-frontdoor" in the East US region.

```
az group create -n labs-frontdoor --tags courselabs=azure -l eastus
```

Now we'll create the Front Door profile using the Premium SKU to support WAF functionality:

```
az afd profile create --profile-name labs --sku Premium_AzureFrontDoor -g labs-frontdoor
```

This command creates the Front Door profile, which is the top-level container for all our Front Door configuration.

## Exercise 3: Deploying Backend Applications

Front Door needs some backends to serve. We'll deploy two Azure Container Instances running the same application in different regions. This simulates a real-world scenario where you have regional deployments for redundancy and performance.

For the first container in East US:

```
az container create -g labs-frontdoor --name simple-web-1 --image courselabs/simple-web:6.0 --ports 80 --no-wait -l eastus --dns-name-label placeholder-app1-dns
```

And the second container in West US:

```
az container create -g labs-frontdoor --name simple-web-2 --image courselabs/simple-web:6.0 --ports 80 --no-wait -l westus --dns-name-label placeholder-app2-dns
```

Notice we're using the no-wait flag so both containers start deploying in parallel.

## Exercise 4: Understanding Front Door Components

While the containers are starting, let's explore the Front Door Profile in the Portal. Understanding the component structure is crucial.

Front Door Manager is where you create endpoints. These are subdomains or custom domains that serve as the entry point to your application.

Origin groups represent your backends. Each endpoint refers to an origin group, and each origin group can contain multiple origins, which are the actual application hosts.

Routes link a frontend endpoint to a backend origin group. This is where the magic happens - connecting your public endpoint to your backend services.

Finally, Rule sets, Security policies, and Optimizations allow you to customize the processing behavior for individual routes.

## Exercise 5: Configuring Backend Origins

Now let's configure our ACI containers as origins. Each application host becomes an origin in Front Door. Origins belong to an origin group, which defines shared settings.

First, we'll create the origin group:

```
az afd origin-group create -g labs-frontdoor --origin-group-name simple-web --profile-name labs --probe-request-type GET --probe-protocol Http --probe-interval-in-seconds 30 --probe-path / --sample-size 4 --successful-samples-required 3 --additional-latency-in-milliseconds 50
```

These parameters define the health check configuration. We're specifying how frequently to probe the origins, what constitutes a healthy response, and how much additional latency is acceptable.

Now let's add our first container as an origin. First, we'll get its FQDN:

```
az container show -g labs-frontdoor --name simple-web-1 --query 'ipAddress.fqdn'
```

Then add it to the origin group:

```
az afd origin create -g labs-frontdoor --profile-name labs --origin-group-name simple-web --origin-name container1 --priority 1 --weight 300 --enabled-state Enabled --http-port 80 --origin-host-header placeholder-container1-fqdn --host-name placeholder-container1-fqdn
```

And the second container:

```
az container show -g labs-frontdoor --name simple-web-2 --query 'ipAddress.fqdn'

az afd origin create -g labs-frontdoor --profile-name labs --origin-group-name simple-web --origin-name container2 --priority 1 --weight 1000 --enabled-state Enabled --http-port 80 --origin-host-header placeholder-container2-fqdn --host-name placeholder-container2-fqdn
```

Notice the weight configuration. Both containers have priority 1, but container 1 has a weight of 300 while container 2 has a weight of 1000. This means when both origins are healthy, we should see approximately three times more traffic going to container 2 than container 1.

If you check the Portal now, you'll see the origin group with both containers listed. However, they're not yet serving traffic because we haven't created an endpoint and route.

## Exercise 6: Configuring the Frontend

Front Door endpoints are the public domain names for your application. Let's create an endpoint:

```
az afd endpoint create -g labs-frontdoor --profile-name labs --endpoint-name simple-web --enabled-state Enabled
```

Now we have a public endpoint URL, but it's not connected to our backend yet. The final step is creating a route:

```
az afd route create -g labs-frontdoor --profile-name labs --endpoint-name simple-web --forwarding-protocol HttpOnly --route-name simple-web-route --origin-group simple-web --supported-protocols Http --https-redirect Disabled --link-to-default-domain Enabled --enable-compression true
```

This route configuration includes several important settings. Since our ACI containers don't support HTTPS, we're restricting traffic to HTTP only. We've also enabled compression, so browsers that support it will receive compressed responses, improving performance.

In the Portal, you should now see green checkmarks with Provision succeeded for your endpoint, route, and origin group. Browse to the endpoint URL and refresh several times. You should see traffic being load balanced, with more requests going to the container with the higher weight.

## Exercise 7: Applying WAF Security Rules

The Premium SKU of Front Door supports the same Web Application Firewall functionality as Application Gateway. You can create different WAF security policies for each endpoint, tailoring the ruleset for each frontend.

Let's create a WAF policy in Prevention mode:

```
az network front-door waf-policy create -g labs-frontdoor --name simplewebwaf --sku Premium_AzureFrontDoor --disabled false --mode Prevention
```

Note that the WAF policy is a separate resource in the resource group, not directly attached to the Front Door profile.

The policy starts without any rules. We need to select rulesets for protection. Let's see what's available:

```
az network front-door waf-policy managed-rule-definition list -o table
```

The two most useful rulesets are the Microsoft Defaults, which cover OWASP threats, and the Bot Manager, which blocks bot access.

Let's add both rulesets:

```
az network front-door waf-policy managed-rules add -g labs-frontdoor --policy-name simplewebwaf --type Microsoft_DefaultRuleSet --version 1.1

az network front-door waf-policy managed-rules add -g labs-frontdoor --policy-name simplewebwaf --type Microsoft_BotManagerRuleSet --version 1.0
```

You can view all the rules in the Portal by opening the WAF policy and selecting Managed rules.

Now let's apply the WAF by creating a security policy. This command needs resource IDs:

```
az afd endpoint show -g labs-frontdoor --profile-name labs --endpoint-name simple-web --query id

az network front-door waf-policy show -g labs-frontdoor -n simplewebwaf --query id

az afd security-policy create -g labs-frontdoor --profile-name labs --security-policy-name simplewebsec --domains placeholder-endpoint-id --waf-policy placeholder-policy-id
```

Once provisioned, attacks like SQL injection will be blocked. Let's test it:

```
curl -v "http://placeholder-endpoint-url/?id=1;select+1,2,3+from+users+where+id=1--"
```

You'll receive a 403 Forbidden response with a message that the request is blocked. The WAF is working.

## Lab Challenge

Now it's your turn. Deploy a new ACI container with the Pi application:

```
az container create -g labs-frontdoor --name pi --image kiamol/ch05-pi --ports 80 --ip-address Public --command-line "dotnet Pi.Web.dll -m web" --no-wait --dns-name-label placeholder-pi-dns
```

Follow similar steps to publish this app through Front Door with its own endpoint URL. Create an origin group, add the origin, create an endpoint, and configure a route.

This exercise will reinforce what you've learned and ensure you can set up Front Door independently.

## Cleanup

When you're finished, clean up the resources:

```
az group delete -y --no-wait -n labs-frontdoor
```

This concludes our Azure Front Door exercises. You've learned how to create and configure a global load balancing solution with CDN capabilities and web application firewall protection.
