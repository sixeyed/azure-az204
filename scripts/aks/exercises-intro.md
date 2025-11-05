# Azure Kubernetes Service - Exercises Introduction

We've covered what AKS is and why it's valuable for container orchestration. Now let's get hands-on and create your first Kubernetes cluster in Azure.

## What You'll Do

You'll start by **creating an AKS cluster** using the Azure CLI with `az aks create`. You'll specify the node count (starting with two for high availability) and VM size for your cluster nodes. This process takes several minutes as Azure provisions virtual machines, configures networking, installs Kubernetes components, and sets up the management infrastructure.

While the cluster is being created, you'll discover something interesting in the Portal: **two resource groups appear**. The one you created ("labs-aks") contains the AKS management object. But Azure also creates a second resource group starting with "MC_" that contains all the underlying infrastructure - VMs, network interfaces, load balancers, and network security groups. This is the managed resource group, and understanding this separation is crucial: you shouldn't directly modify resources in the MC group. All interactions should go through the AKS resource using kubectl or `az aks` commands.

Next, you'll **connect to your cluster** using `az aks get-credentials`, which downloads cluster credentials and configures kubectl. You'll verify the connection by listing the nodes with `kubectl get nodes`, seeing your two Azure-hosted nodes in the Ready state.

Then comes the exciting part: **deploying an application**. You'll use three YAML files - a ConfigMap for configuration data, a Deployment defining how the app runs, and a Service exposing it to external traffic. You'll deploy all three with `kubectl apply`, then watch as Kubernetes pulls the container image and starts your pods. You'll see the Service's external IP initially show as "pending" while Azure provisions a public IP address and configures the load balancer - within minutes, your app will be accessible from anywhere on the internet!

The **lab challenge** has you exploring scaling by modifying the deployment to run four pods instead of one. You'll watch the pods being created, explore how the load balancer distributes requests, and discover that ConfigMap changes don't automatically update running pods - they're loaded at startup, so you need to restart pods to see new configuration.

Let's create and explore your first Kubernetes cluster in Azure!
