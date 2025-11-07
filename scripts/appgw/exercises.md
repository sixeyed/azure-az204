# Application Gateway with Web Application Firewall

## Reference

Application Gateway is a layer 7 load balancer that routes traffic based on incoming HTTP requests, using domain names and URL paths to match the right backend service. Backends are monitored to ensure they're healthy, and traffic is shared between healthy instances. Web Application Firewall is an optional feature that provides powerful security protection. WAF can inspect headers and bodies of HTTP calls looking for malicious payloads. Attacks can be prevented at the WAF layer so they never reach the backend service, protecting your applications from common web vulnerabilities without requiring code changes.

## Create Application Gateway

We explored App Gateway in the AKS Ingress lab, so we'll get straight to creating one with the CLI. Let's start by creating the Application Gateway infrastructure. We'll need several networking components before we can deploy the gateway itself.

First, we'll create a resource group to contain all our resources, naming it "labs-appgw" and deploying to the East US region. The courselabs tag helps us track these resources for the course.

Next, we need a public IP for the Application Gateway using the Standard SKU which is required for Application Gateway. We're also setting a DNS name - you'll need to replace the placeholder with a globally unique DNS name for your gateway.

Application Gateway must be deployed inside a virtual network, so let's create one with the address space 10.4.0.0/16, which gives us plenty of IP addresses for our deployment.

Application Gateway requires its own dedicated subnet that can't be shared with other resources. We're creating a subnet with the address prefix 10.4.10.0/24, providing 256 IP addresses specifically for the Application Gateway.

Now we'll create a Web Application Firewall policy using the latest OWASP ruleset version 3.2, which protects against the most common web vulnerabilities.

Let's enable the policy and set it to Prevention mode. We're updating the policy to use Prevention mode, which means the WAF will actively block suspicious requests rather than just detecting them. We're also enabling request body checking for thorough inspection and setting the state to Enabled. Prevention mode is important because it actively protects your applications - it doesn't just log threats, it blocks them before they reach your backend servers.

Now we can create the Application Gateway itself using the WAF version 2 SKU which supports the latest WAF features. This command will take several minutes to complete as Azure provisions all the components. While that's creating, let's move on to deploying our backend services.

---

## Create Backend ACI Containers

We'll use Azure Container Instances to quickly deploy some web applications that our Application Gateway will front. ACI doesn't scale horizontally, so we'll run two separate containers with the simple web app for load balancing demonstration.

We're creating containers that will deploy in the background using the no-wait flag. We're also deploying a different application, the Pi calculator web app, which demonstrates that Application Gateway can route to different types of applications.

Once the containers are running, we're testing each application by browsing to their public IP addresses. Make a note of these IP addresses as we'll need them for the Application Gateway configuration.

---

## Configure App Routing

Opening the Application Gateway in the Azure Portal and navigating to the Overview page, we're copying the public IP address and browsing to it. You'll see a 502 Bad Gateway error. This is expected because we haven't configured any routing rules yet - the gateway doesn't know where to send traffic.

For the simple web application, we need to create three components that work together to route traffic. First, we're creating a backend pool with both simple-web container IP addresses as targets. This pool represents the group of servers that can handle requests for this application.

Second, we're creating a multi-site listener with a specific host name. The listener waits for incoming requests that match this hostname.

Third, we're creating a routing rule that links the listener to the backend pool using the default HTTP settings. This rule tells the gateway "when you receive a request matching this listener, send it to this backend pool."

For the Pi application, we're following the same pattern to keep our routing organized - creating a backend pool, listener, and routing rule for complete separation.

The default rule that was created with the Application Gateway will interfere with our multi-site rules because routing rules are evaluated by priority. We're changing the default rule's priority to a lower value, ensuring our custom rules are evaluated first.

Since we're using fake domain names for this lab, we need to add them to your local hosts file so your computer knows to send requests for these domains to your Application Gateway's public IP address.

Now we're testing both applications by browsing to the configured domain names. Refreshing the simple web app several times, you should see the hostname alternating between the two containers. This demonstrates load balancing in action - the Application Gateway is distributing requests across both backend instances.

---

## Test the Web Application Firewall

Let's verify that the WAF is protecting our applications from common attacks. First, let's see what happens when we attack the container directly, bypassing WAF. We're using curl to send a request with a SQL injection payload in the query string. This is a classic SQL injection attack pattern.

You'll get a normal 200 response with HTML content. The application has no idea it's being attacked - it just processes the request normally.

Now we're trying the same attack through the Application Gateway. This time you'll receive a 403 Forbidden response. The WAF detected the SQL injection pattern and blocked the request before it reached the backend. Your application is protected without any code changes.

In the Azure Portal, you can view the WAF logs to see details about the blocked request, including which OWASP rule was triggered and why it was considered malicious.

If you want a thorough security test, you can use the GoTestWAF tool which runs hundreds of attack simulations against your gateway. The tool will take several minutes to run over 500 test cases covering all major OWASP vulnerabilities. You should see the WAF successfully blocking all attempted attacks.

---

## Lab

Application Gateway can route based on URL paths, not just domain names. This means different paths in the same domain can be sent to different backend pools. What part of the routing configuration would you use for that?

---

## Cleanup

When you're finished with the lab, we're deleting the resource group to remove all resources and stop incurring charges. The delete command uses flags to confirm without prompting and return immediately while deletion continues in the background.
