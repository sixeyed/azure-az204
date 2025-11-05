# Application Gateway with WAF - Exercise Walkthrough

## Exercise 1: Create Application Gateway

Let's start by creating the Application Gateway infrastructure. We'll need several networking components before we can deploy the gateway itself.

### Step 1: Create Resource Group

First, we'll create a resource group to contain all our resources:

```
az group create -n labs-appgw --tags courselabs=azure -l eastus
```

We're using the name "labs-appgw" and deploying to the East US region. The courselabs tag helps us track these resources.

### Step 2: Create Public IP Address

Next, we need a public IP for the Application Gateway:

```
az network public-ip create -g labs-appgw -n appgw-pip --sku Standard -l eastus --dns-name your-unique-dns-name
```

Note that we're using the Standard SKU, which is required for Application Gateway. Replace "your-unique-dns-name" with a globally unique DNS name for your gateway.

### Step 3: Create Virtual Network

Application Gateway must be deployed inside a virtual network, so let's create one:

```
az network vnet create -g labs-appgw -n vnet --address-prefix 10.4.0.0/16 -l eastus
```

We're using the address space 10.4.0.0/16, which gives us plenty of IP addresses for our deployment.

### Step 4: Create Dedicated Subnet

Application Gateway requires its own dedicated subnet:

```
az network vnet subnet create -g labs-appgw --vnet-name vnet -n appgw --address-prefixes 10.4.10.0/24
```

This creates a subnet with 256 IP addresses specifically for the Application Gateway.

### Step 5: Create WAF Policy

Now we'll create a Web Application Firewall policy using the latest OWASP ruleset:

```
az network application-gateway waf-policy create -n appg-waf -g labs-appgw --type OWASP --version 3.2 -l eastus
```

This creates a WAF policy with OWASP version 3.2 rules, which protect against the most common web vulnerabilities.

### Step 6: Enable WAF in Prevention Mode

Let's enable the policy and set it to Prevention mode:

```
az network application-gateway waf-policy policy-setting update --mode Prevention --policy-name appg-waf -g labs-appgw --request-body-check true --state Enabled
```

Prevention mode means the WAF will actively block suspicious requests. We're also enabling request body checking for thorough inspection.

### Step 7: Create Application Gateway

Now we can create the Application Gateway itself:

```
az network application-gateway create -g labs-appgw -n appgw --public-ip-address appgw-pip --vnet-name vnet --subnet appgw --capacity 1 --sku WAF_v2 --priority "1" --waf-policy appg-waf -l eastus
```

We're using the WAF_v2 SKU, which supports the latest WAF features. Note that this command will take several minutes to complete as Azure provisions all the components.

While that's creating, let's move on to deploying our backend services.

## Exercise 2: Create Backend ACI Containers

We'll use Azure Container Instances to quickly deploy some web applications that our Application Gateway will front.

### Step 1: Create Simple Web Containers

Let's create two instances of a simple web application for load balancing demonstration:

```
az container create -g labs-appgw --name simple-web-1 --image courselabs/simple-web:6.0 --ports 80 --ip-address Public --no-wait
```

```
az container create -g labs-appgw --name simple-web-2 --image courselabs/simple-web:6.0 --ports 80 --ip-address Public --no-wait
```

The no-wait flag allows these to create in the background while we continue.

### Step 2: Create Pi Web Container

Let's also deploy a different application, the Pi calculator web app:

```
az container create -g labs-appgw --name pi-0 --image kiamol/ch05-pi --ports 80 --ip-address Public --command-line "dotnet Pi.Web.dll -m web" --no-wait
```

### Step 3: Verify Container Deployment

Once the containers are running, test each application by browsing to their public IP addresses. Make a note of these IP addresses as we'll need them for the Application Gateway configuration.

You should see the simple web app responding with a hostname, and the Pi app showing its calculator interface.

## Exercise 3: Configure Application Routing

Now let's configure the Application Gateway to route traffic to our backend containers.

### Step 1: Initial Test

Open the Application Gateway in the Azure Portal and navigate to the Overview page. Copy the public IP address and browse to it. You'll see a 502 Bad Gateway error. This is expected because we haven't configured any routing rules yet.

### Step 2: Configure Simple Web App Routing

For the simple web application, we need to create three components:

First, create a backend pool. Navigate to Backend pools in the portal and add a new pool named "simple-web-pool". Add both simple-web container IP addresses as targets.

Second, create a listener. Go to Listeners and add a multi-site listener named "simple-web-listener" with the host name "simple.appgw.azure.courselabs.co".

Third, create a routing rule. Navigate to Rules and create a new rule named "simple-web-rule". Link the simple-web-listener to the simple-web-pool, using the default HTTP settings.

### Step 3: Configure Pi App Routing

For the Pi application, follow the same pattern:

Create a backend pool named "pi-pool" with the Pi container IP address.

Create a multi-site listener named "pi-listener" with the host name "pi.appgw.azure.courselabs.co".

Create a routing rule named "pi-rule" linking the listener to the pool.

### Step 4: Fix Rule Priority

The default rule that was created with the Application Gateway will interfere with our multi-site rules. Navigate to Rules and change rule1's priority to 20000, making it lower priority than your custom rules.

### Step 5: Configure Local DNS

Since we're using fake domain names, we need to add them to your local hosts file. These entries should point to your Application Gateway's public IP address.

On Windows using PowerShell as Administrator:

```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process -Force
./scripts/add-to-hosts.ps1 pi.appgw.azure.courselabs.co your-appgw-ip
./scripts/add-to-hosts.ps1 simple.appgw.azure.courselabs.co your-appgw-ip
```

On macOS or Linux:

```
sudo chmod +x ./scripts/add-to-hosts.sh
./scripts/add-to-hosts.sh pi.appgw.azure.courselabs.co your-appgw-ip
./scripts/add-to-hosts.sh simple.appgw.azure.courselabs.co your-appgw-ip
```

### Step 6: Test Routing

Now test both applications by browsing to:

http://simple.appgw.azure.courselabs.co
http://pi.appgw.azure.courselabs.co

Refresh the simple web app several times. You should see the hostname alternating between the two containers, demonstrating load balancing in action.

## Exercise 4: Test Web Application Firewall

Let's verify that the WAF is protecting our applications from common attacks.

### Step 1: Test SQL Injection Against Container

First, let's see what happens when we attack the container directly, bypassing WAF:

```
curl "http://your-container-ip/?id=1;select+1,2,3+from+users+where+id=1--"
```

Replace "your-container-ip" with one of your simple-web container IP addresses. You'll get a normal 200 response with HTML content. The application has no idea it's being attacked.

### Step 2: Test SQL Injection Against WAF

Now try the same attack through the Application Gateway:

```
curl "http://simple.appgw.azure.courselabs.co/?id=1;select+1,2,3+from+users+where+id=1--"
```

This time you'll receive a 403 Forbidden response. The WAF detected the SQL injection pattern and blocked the request before it reached the backend.

### Step 3: View WAF Logs

In the Azure Portal, navigate to your Application Gateway and view the Logs section. You can query the WAF logs to see details about the blocked request, including which OWASP rule was triggered.

### Step 4: Optional - Comprehensive WAF Testing

If you want a thorough security test, you can use the GoTestWAF tool. This runs hundreds of attack simulations against your gateway.

Start Docker Desktop, then run:

```
docker run --add-host simple.appgw.azure.courselabs.co:your-app-gw-ip sixeyed/gotestwaf:2211 --noEmailReport --url http://simple.appgw.azure.courselabs.co --skipWAFIdentification --skipWAFBlockCheck --testSet owasp
```

Replace "your-app-gw-ip" with your Application Gateway IP address. The tool will take several minutes to run over 500 test cases. You should see the WAF successfully blocking all attempted attacks.

## Lab Challenge: Path-Based Routing

Application Gateway can route based on URL paths, not just domain names. This means different paths in the same domain can be sent to different backend pools.

Your challenge is to figure out how to configure path-based routing. Where in the Application Gateway configuration would you set this up? What changes would you need to make to your existing routing rules?

Take some time to explore the Portal and CLI documentation to find the solution.

## Cleanup

When you're finished with the lab, delete the resource group to remove all resources and stop incurring charges:

```
az group delete -y --no-wait -n labs-appgw
```

This completes our Application Gateway with WAF lab. You've learned how to deploy and configure a production-ready application delivery and security solution in Azure.
