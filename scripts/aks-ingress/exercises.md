# AKS Ingress and Application Gateway - Exercise Walkthrough

## Reference

Ingress is a Kubernetes feature that lets you route HTTP traffic into your cluster using domain names rather than IP addresses. This means a single cluster can serve multiple applications through one public IP address. In Azure, the Application Gateway service integrates with Kubernetes Ingress objects to provide enterprise-grade HTTP load balancing with features like SSL termination and Web Application Firewall protection.

## Create an Application Gateway

Let's start by creating the Application Gateway. This is an unusual Azure resource - each configuration page must be completed before you can move on, unlike most resources where you can jump around. The setup includes several important sections: Basics where you choose between fixed scale or autoscaling, select a tier, and specify a VNet. Frontends where you configure the IP address that routes to the Application Gateway, usually a public IP. Backends where you define backend pools where traffic will be routed, similar to Azure Load Balancer. And Configuration where you set up routing rules for matching incoming requests to backends.

We're taking a different approach than the default. While you can create an AKS cluster with the AGIC add-on and let it create everything automatically, it's better to create the Application Gateway first. This gives you control over the configuration and lets you keep the Application Gateway running even if you remove your AKS cluster - useful for maintaining consistent public endpoints across cluster recreations.

**Create the Resource Group**: First, we're creating a new resource group named "labs-aks-ingress" with the courselabs=azure tag in the East US region. This will contain all our resources for this lab.

**Create the Public IP**: Since the Application Gateway will be the entry point for all your apps, it needs a public IP address. We're creating a public IP named "appgw-pip" with the Standard SKU, and setting a DNS name label. Remember to use your own unique DNS name - something like "appgw-demo-yourname" or similar. The Standard SKU is required because Application Gateway v2 only works with Standard SKU public IPs.

**Create the Virtual Network**: Now we're creating the virtual network named "vnet" with the address space 10.2.0.0/16. This provides plenty of addresses for our subnets. The Application Gateway needs to be deployed into the same VNet you'll use for your AKS cluster, which is why we're creating it now.

**Create the Subnets**: We need two subnets - one for AKS and one for the Application Gateway. First, we're creating the AKS subnet with the address space 10.2.8.0/21 - that's a larger subnet providing over 2000 IP addresses for Pods when using Azure CNI. Then we're creating the Application Gateway subnet with 10.2.3.0/24, which provides 256 addresses. The Application Gateway needs its own dedicated subnet, it cannot share with other resources.

**Create the Application Gateway**: Now we're creating the Application Gateway itself. Note that we need a v2 SKU to work with AKS - the older v1 SKU isn't compatible with the AGIC add-on. All networking components must be in the same region, which is why we specified eastus for everything. The command references our public IP, VNet, and Application Gateway subnet. The capacity is set to 1 for this lab, but in production you'd typically use autoscaling. The priority parameter is required for routing rules.

This creation process takes several minutes - Application Gateway is a complex resource with multiple backend components. You can check progress in the Portal by navigating to the resource group and watching the deployment status. While it's creating, we can move on to the AKS cluster.

## AKS add-ons

AKS has a concept of add-ons that you can use to add functionality to an existing cluster. We'll create the cluster now, and when both the cluster and the Application Gateway are ready, we can integrate them with an add-on.

**Understand the Requirements**: The cluster needs to use the Azure network plugin and be deployed into the AKS subnet we created earlier. This is essential for the Application Gateway integration to work properly.

**Get the Subnet ID**: First, we're getting the subnet ID using az network vnet subnet show with a query to extract just the id field. Copy that subnet ID - you'll need it for the next command. It's a long string that uniquely identifies the subnet within Azure.

**Create the AKS Cluster**: We're creating the AKS cluster named "aks04" with the network-plugin set to azure and the vnet-subnet-id pointing to our AKS subnet. When you integrate AKS with a VNet, the cluster needs permission to manage the network resources. You'll see a message "Waiting for AAD role to propagate" with its own progress bar - this is Azure setting up the necessary role assignments. Your account needs elevated permissions in the subscription to create this role, typically Contributor or Owner.

While this is creating, take a moment to check the Application Gateway in the Portal. The user interface is very similar to the Load Balancer resource, and that's because Application Gateway is essentially an enhanced load balancer with extra features. In particular, the Web Application Firewall feature is something you definitely want to explore for production deployments - it provides protection against common web exploits like SQL injection and cross-site scripting.

Once both resources are ready, we can deploy the Application Gateway Ingress Controller add-on.

**Get the Application Gateway ID**: First, we're getting the Application Gateway resource ID using az network application-gateway show with a query to extract the id field. Copy that ID - it's what we need to link the Application Gateway to AKS.

**Enable the Add-on**: Now we're enabling the add-on using az aks enable-addons with the addon type set to ingress-appgw and the appgw-id parameter pointing to our Application Gateway. This setup takes a while to complete - Azure is installing the AGIC controller into your cluster, configuring permissions, and establishing the connection between AKS and the Application Gateway.

What you're creating here is a production-grade deployment that's ready for scalable, reliable, public-facing applications. The AGIC controller will automatically configure the Application Gateway based on Kubernetes Ingress resources you create, eliminating manual configuration.

## Deploy with Application Gateway on AKS

Now everything is ready. Let's deploy a simple application and make it accessible via a public URL.

**Get Cluster Credentials**: First, we're downloading the connection credentials for kubectl using az aks get-credentials. This creates the kubectl context and sets it as the current one, so all subsequent kubectl commands will target this AKS cluster.

**Verify Connection**: Let's verify the connection by listing the nodes with kubectl get nodes. You should see your AKS nodes listed with their status, typically showing Ready.

**Deploy the Application**: Now we're deploying the whoami application using kubectl apply. This creates a ClusterIP Service and a Deployment with multiple replicas. The ClusterIP Service means it's only accessible from within the cluster - it doesn't get a public IP on its own.

**Get the Public IP DNS Name**: For the Ingress object, we need to use the DNS name of our public IP address. We're getting the fully-qualified domain name using az network public-ip show with a query to extract the dnsSettings.fqdn field. Take note of this FQDN - something like appgw-demo-yourname.eastus.cloudapp.azure.com.

**Edit the Ingress Spec**: You need to edit the ingress specification file at labs/aks-ingress/specs/ingress-aks.yaml and replace the placeholder with your actual FQDN. This tells Kubernetes which hostname this Ingress should respond to.

**Create the Ingress**: Now we're creating the Ingress object using kubectl apply. The AGIC controller sees this Ingress resource and automatically configures the Application Gateway with the appropriate rules, backend pools, and health probes.

**Check Ingress Status**: We're checking the Ingress status using kubectl get ingress. You should see your Ingress object with the DNS name and public IP address assigned. It might take a minute for the address to appear as the controller configures the Application Gateway.

**Test the Application**: We're browsing to the hostname in a web browser. You should see the whoami application, routed via Application Gateway. The application shows information about which Pod handled the request. Refresh the page several times - the load balancing should distribute requests nicely between all the Pods, and you'll see different Pod names appearing.

## Lab

For the lab challenge, navigate through the Application Gateway setup in the Azure Portal. Explore the configuration to understand how the routing actually works.

**What to Explore**: Look at the backend pools section - you'll see that AGIC has automatically created a backend pool pointing to your AKS nodes. Check the backend health to see if the health probes are successfully reaching your Pods. Examine the HTTP settings to see how the Application Gateway communicates with the backends. Review the routing rules to understand how incoming requests are matched to backend pools. Look at the listeners to see which ports and protocols are configured.

Take your time exploring these settings. Understanding the integration between Application Gateway and AKS will help you troubleshoot issues and optimize your deployments. You'll see how AGIC translates Kubernetes Ingress resources into Application Gateway configuration automatically, which is the real power of this integration.

## Cleanup

When you're finished, we're deleting the resource group to remove all resources using az group delete with the yes flag to skip confirmation and the no-wait flag to return immediately. This removes everything - the Application Gateway, AKS cluster, public IP, virtual network, and all associated resources.

We're also switching your Kubernetes context back to your local Docker Desktop using kubectl config use-context. This ensures that future kubectl commands target your local environment, not the deleted cluster.

Great job completing this lab on AKS Ingress and Application Gateway! You now understand how to create production-grade ingress configuration for Kubernetes applications in Azure.
