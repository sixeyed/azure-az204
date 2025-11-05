# AKS Ingress and Application Gateway - Exercise Walkthrough

## Exercise 1: Creating the Application Gateway

Let's start by creating the Application Gateway. This is an unusual Azure resource - each configuration page must be completed before you can move on. The setup includes:

- Basics - where you choose between fixed scale or autoscaling, select a tier, and specify a VNet
- Frontends - the IP address that routes to the Application Gateway, usually a public IP
- Backends - backend pools where traffic will be routed, similar to Azure Load Balancer
- Configuration - routing rules for matching incoming requests to backends

We're taking a different approach than the default. While you can create an AKS cluster with the AGIC add-on and let it create everything automatically, it's better to create the Application Gateway first. This gives you control over the configuration and lets you keep the Application Gateway running even if you remove your AKS cluster.

First, create a new resource group:

```
az group create -n labs-aks-ingress --tags courselabs=azure -l eastus
```

Since the Application Gateway will be the entry point for all your apps, it needs a public IP address. It also needs to be deployed into the same VNet you'll use for your AKS cluster.

Create the public IP address:

```
az network public-ip create -g labs-aks-ingress -n appgw-pip --sku Standard -l eastus --dns-name <your-unique-dns-name>
```

Remember to use your own unique DNS name - something like appgw-demo-yourname.

Now create the virtual network:

```
az network vnet create -g labs-aks-ingress -n vnet --address-prefix 10.2.0.0/16 -l eastus
```

We need two subnets - one for AKS and one for the Application Gateway:

```
az network vnet subnet create -g labs-aks-ingress --vnet-name vnet -n aks --address-prefixes 10.2.8.0/21

az network vnet subnet create -g labs-aks-ingress --vnet-name vnet -n appgw --address-prefixes 10.2.3.0/24
```

Now create the Application Gateway. Note that we need a v2 SKU to work with AKS, and all networking components must be in the same region:

```
az network application-gateway create -g labs-aks-ingress -n appgw --public-ip-address appgw-pip --vnet-name vnet --subnet appgw --capacity 1 --sku Standard_v2 --priority "1" -l eastus
```

This will take several minutes to create. You can check progress in the Portal. While it's creating, we can move on to the AKS cluster.

## Exercise 2: Creating the AKS Cluster

AKS has a concept of add-ons that you can use to add functionality to an existing cluster. We'll create the cluster now, and when both the cluster and the Application Gateway are ready, we can integrate them with an add-on.

The cluster needs to use the Azure network plugin and be deployed into the AKS subnet we created earlier.

First, get the subnet ID:

```
az network vnet subnet show -g labs-aks-ingress -n aks --vnet-name vnet --query id -o tsv
```

Copy that subnet ID - you'll need it for the next command.

Create the AKS cluster:

```
az aks create -g labs-aks-ingress -n aks04 --network-plugin azure --vnet-subnet-id '<your-subnet-id>' -l eastus
```

When you integrate AKS with a VNet, the cluster needs permission to manage the network. You'll see a message "Waiting for AAD role to propagate" with its own progress bar. Your account needs elevated permissions in the subscription to create this role.

While this is creating, take a moment to check the Application Gateway in the Portal. The user interface is very similar to the Load Balancer resource. Application Gateway is essentially an enhanced load balancer with extra features. In particular, the Web Application Firewall feature is something you definitely want to explore for production deployments.

## Exercise 3: Integrating Application Gateway with AKS

Once both resources are ready, we can deploy the Application Gateway Ingress Controller add-on.

First, get the Application Gateway ID:

```
az network application-gateway show -n appgw -g labs-aks-ingress --query id -o tsv
```

Copy that ID, then enable the add-on:

```
az aks enable-addons -n aks04 -g labs-aks-ingress -a ingress-appgw --appgw-id '<your-appgw-id>'
```

This setup takes a while to complete, but what you're creating is a production-grade deployment that's ready for scalable, reliable, public-facing applications.

## Exercise 4: Deploying an Application

Now everything is ready. Let's deploy a simple application and make it accessible via a public URL.

First, download the connection credentials for kubectl:

```
az aks get-credentials -g labs-aks-ingress -n aks04 --overwrite
```

This creates the kubectl context and sets it as the current one. Let's verify the connection by listing the nodes:

```
kubectl get nodes
```

You should see your AKS nodes listed.

Now deploy the whoami application. This creates a ClusterIP Service and a Deployment with multiple replicas:

```
kubectl apply -f labs/aks-ingress/specs/whoami.yaml
```

For the Ingress object, we need to use the DNS name of our public IP address. Get the fully-qualified domain name:

```
az network public-ip show -g labs-aks-ingress -n appgw-pip --query 'dnsSettings.fqdn' -o tsv
```

Take note of this FQDN. You'll need to edit the ingress specification file and replace the placeholder with your actual FQDN.

Open the file at labs/aks-ingress/specs/ingress-aks.yaml and replace <pip-fqdn> with your actual domain name.

Now create the Ingress object:

```
kubectl apply -f labs/aks-ingress/specs/ingress-aks.yaml
```

Check the Ingress status:

```
kubectl get ingress
```

You should see your Ingress object with the DNS name and public IP address.

Browse to the hostname in your web browser. You should see the whoami application, routed via Application Gateway. Refresh the page several times - the load balancing should distribute requests nicely between all the Pods.

## Lab Challenge

For the lab challenge, navigate through the Application Gateway setup in the Portal. Explore the configuration to understand:

- How the routing actually works
- How backend pools are configured
- How health checks ensure traffic only goes to healthy Pods
- What happens when you look at the HTTP settings

Take your time exploring these settings. Understanding the integration between Application Gateway and AKS will help you troubleshoot issues and optimize your deployments.

## Cleanup

When you're finished, delete the resource group to remove all resources:

```
az group delete -y --no-wait -n labs-aks-ingress
```

And switch your Kubernetes context back to your local Docker Desktop:

```
kubectl config use-context docker-desktop
```

Great job completing this lab on AKS Ingress and Application Gateway!
