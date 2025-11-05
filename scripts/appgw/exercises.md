# Application Gateway with WAF - Exercise Walkthrough

## Exercise 1: Create Application Gateway

Let's start by creating the Application Gateway infrastructure. We'll need several networking components before we can deploy the gateway itself.

### Step 1: Create Resource Group

First, we'll create a resource group to contain all our resources. We're using the name "labs-appgw" and deploying to the East US region. The courselabs tag helps us track these resources for the course.

### Step 2: Create Public IP Address

Next, we need a public IP for the Application Gateway. We're creating a public IP address in the labs-appgw resource group, naming it "appgw-pip", and using the Standard SKU which is required for Application Gateway. We're also setting a DNS name - you'll need to replace the placeholder with a globally unique DNS name for your gateway.

### Step 3: Create Virtual Network

Application Gateway must be deployed inside a virtual network, so let's create one. We're creating a virtual network in the labs-appgw resource group, naming it "vnet", and using the address space 10.4.0.0/16, which gives us plenty of IP addresses for our deployment.

### Step 4: Create Dedicated Subnet

Application Gateway requires its own dedicated subnet that can't be shared with other resources. We're creating a subnet within the vnet, naming it "appgw", and using the address prefix 10.4.10.0/24. This subnet provides 256 IP addresses specifically for the Application Gateway.

### Step 5: Create WAF Policy

Now we'll create a Web Application Firewall policy using the latest OWASP ruleset. We're creating a WAF policy named "appg-waf" in the labs-appgw resource group, specifying the OWASP type with version 3.2, which protects against the most common web vulnerabilities.

### Step 6: Enable WAF in Prevention Mode

Let's enable the policy and set it to Prevention mode. We're updating the policy settings to use Prevention mode, which means the WAF will actively block suspicious requests rather than just detecting them. We're also enabling request body checking for thorough inspection, and setting the state to Enabled.

Prevention mode is important because it actively protects your applications - it doesn't just log threats, it blocks them before they reach your backend servers.

### Step 7: Create Application Gateway

Now we can create the Application Gateway itself. We're deploying to the labs-appgw resource group, naming it "appgw", associating it with the public IP we created, placing it in our virtual network within the dedicated appgw subnet, setting the capacity to 1 instance, using the WAF version 2 SKU which supports the latest WAF features, setting a priority value of 1, and linking it to the WAF policy we created.

Note that this command will take several minutes to complete as Azure provisions all the components - the load balancer, the WAF engine, and all the networking infrastructure.

While that's creating, let's move on to deploying our backend services.

## Exercise 2: Create Backend ACI Containers

We'll use Azure Container Instances to quickly deploy some web applications that our Application Gateway will front.

### Step 1: Create Simple Web Containers

Let's create two instances of a simple web application for load balancing demonstration. We're creating the first container in the labs-appgw resource group, naming it "simple-web-1", using the courselabs simple-web image version 6.0, exposing port 80, setting the IP address type to Public, and using the no-wait flag to let it create in the background.

We're repeating this for a second container named "simple-web-2" with the same configuration. The no-wait flag allows these to create in the background while we continue with other tasks.

### Step 2: Create Pi Web Container

Let's also deploy a different application, the Pi calculator web app. We're creating a container named "pi-0", using the kiamol Pi image, exposing port 80, setting a public IP address, and providing a custom command line to start the application with specific parameters. This demonstrates that Application Gateway can route to different types of applications.

### Step 3: Verify Container Deployment

Once the containers are running, we're testing each application by browsing to their public IP addresses. Make a note of these IP addresses as we'll need them for the Application Gateway configuration.

You should see the simple web app responding with a hostname, and the Pi app showing its calculator interface.

## Exercise 3: Configure Application Routing

Now let's configure the Application Gateway to route traffic to our backend containers.

### Step 1: Initial Test

Opening the Application Gateway in the Azure Portal and navigating to the Overview page, we're copying the public IP address and browsing to it. You'll see a 502 Bad Gateway error. This is expected because we haven't configured any routing rules yet - the gateway doesn't know where to send traffic.

### Step 2: Configure Simple Web App Routing

For the simple web application, we need to create three components that work together to route traffic.

First, we're creating a backend pool. Navigating to Backend pools in the portal, we're adding a new pool named "simple-web-pool" and adding both simple-web container IP addresses as targets. This pool represents the group of servers that can handle requests for this application.

Second, we're creating a listener. Going to Listeners, we're adding a multi-site listener named "simple-web-listener" with the host name "simple.appgw.azure.courselabs.co". The listener waits for incoming requests that match this specific hostname.

Third, we're creating a routing rule. Navigating to Rules, we're creating a new rule named "simple-web-rule" that links the simple-web-listener to the simple-web-pool, using the default HTTP settings. This rule tells the gateway "when you receive a request matching this listener, send it to this backend pool."

### Step 3: Configure Pi App Routing

For the Pi application, we're following the same pattern to keep our routing organized.

We're creating a backend pool named "pi-pool" with the Pi container IP address as the target.

We're creating a multi-site listener named "pi-listener" with the host name "pi.appgw.azure.courselabs.co".

And we're creating a routing rule named "pi-rule" linking the listener to the pool. Now we have two completely separate routing paths through the same Application Gateway.

### Step 4: Fix Rule Priority

The default rule that was created with the Application Gateway will interfere with our multi-site rules because routing rules are evaluated by priority. Navigating to Rules, we're changing rule1's priority to 20000, making it lower priority than your custom rules which typically start at priority 100. This ensures our custom rules are evaluated first.

### Step 5: Configure Local DNS

Since we're using fake domain names for this lab, we need to add them to your local hosts file so your computer knows to send requests for these domains to your Application Gateway's public IP address.

On Windows, we're using PowerShell as Administrator to set the execution policy and run the add-to-hosts script for both the Pi and simple web domains, pointing them to your Application Gateway IP.

On macOS or Linux, we're making the script executable with chmod and running it for both domains with the Application Gateway IP.

### Step 6: Test Routing

Now we're testing both applications by browsing to the configured domain names. You should see the simple web application at its domain and the Pi calculator at its domain.

Refreshing the simple web app several times, you should see the hostname alternating between the two containers. This demonstrates load balancing in action - the Application Gateway is distributing requests across both backend instances.

## Exercise 4: Test Web Application Firewall

Let's verify that the WAF is protecting our applications from common attacks.

### Step 1: Test SQL Injection Against Container

First, let's see what happens when we attack the container directly, bypassing WAF. We're using curl to send a request with a SQL injection payload in the query string - selecting from a users table with specific parameters. This is a classic SQL injection attack pattern.

Replacing the placeholder with one of your simple-web container IP addresses, you'll get a normal 200 response with HTML content. The application has no idea it's being attacked - it just processes the request normally.

### Step 2: Test SQL Injection Against WAF

Now we're trying the same attack through the Application Gateway using the simple.appgw.azure.courselabs.co domain.

This time you'll receive a 403 Forbidden response. The WAF detected the SQL injection pattern and blocked the request before it reached the backend. Your application is protected without any code changes.

### Step 3: View WAF Logs

In the Azure Portal, navigating to your Application Gateway and viewing the Logs section, you can query the WAF logs to see details about the blocked request, including which OWASP rule was triggered and why it was considered malicious.

### Step 4: Optional - Comprehensive WAF Testing

If you want a thorough security test, you can use the GoTestWAF tool. This runs hundreds of attack simulations against your gateway to test how well the WAF is protecting you.

Starting Docker Desktop, we're running the GoTestWAF container with parameters to add the domain to the container's hosts file, skip email reporting, target your application URL, skip certain checks, and use the OWASP test set.

The tool will take several minutes to run over 500 test cases covering all major OWASP vulnerabilities. You should see the WAF successfully blocking all attempted attacks - SQL injection, cross-site scripting, path traversal, and many others.

## Lab Challenge: Path-Based Routing

Application Gateway can route based on URL paths, not just domain names. This means different paths in the same domain can be sent to different backend pools.

Your challenge is to figure out how to configure path-based routing. Where in the Application Gateway configuration would you set this up? What changes would you need to make to your existing routing rules?

Think about scenarios like sending requests for "/api" to one backend pool and "/admin" to a different pool, all on the same domain. Take some time to explore the Portal and CLI documentation to find the solution.

## Cleanup

When you're finished with the lab, we're deleting the resource group to remove all resources and stop incurring charges. The delete command uses the -y flag to confirm without prompting, and the --no-wait flag to return immediately while the deletion continues in the background.

This completes our Application Gateway with WAF lab. You've learned how to deploy and configure a production-ready application delivery and security solution in Azure.
