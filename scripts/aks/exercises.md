# Azure Kubernetes Service - Exercises Script

## Exercise 1: Creating an AKS Cluster

Let's start by creating our first AKS cluster. We'll begin with a new resource group.

First, we'll create a resource group named "labs-aks" in the East US region. We're also adding a tag to help organize our resources:

```
az group create -n labs-aks --tags courselabs=azure -l eastus
```

Now, let's create the AKS cluster itself. We'll use the `az aks create` command. The command has many options, but we'll focus on the essentials:

```
az aks create -g labs-aks -n aks01 --node-count 2 --node-vm-size Standard_D2s_v5 --location eastus
```

Let's break down what we're doing here:
- We're creating a cluster named "aks01" in our resource group
- We're starting with two nodes, which is a good minimum for high availability
- We're using Standard_D2s_v5 VMs, which provide a good balance of compute and memory
- Note that VM sizes vary by region, so you might need to choose a different size depending on where you're deploying

This process will take several minutes. While we wait, let's explore something interesting in the Azure Portal.

## Understanding Resource Groups

While the cluster is being created, open the Azure Portal and navigate to your resource groups. You'll notice something interesting - there are now two resource groups:

First, there's "labs-aks", which we created. This contains your AKS resource.

Second, there's another resource group with a name that begins with "MC_" followed by your resource group name, cluster name, and region. This is the managed resource group that AKS creates automatically.

The MC resource group contains all the underlying Azure resources that make your cluster work - virtual machines, network interfaces, load balancers, and more. This is important to understand: you shouldn't directly modify resources in this managed resource group. Think of it as a black box that Azure manages for you. All your interactions should go through the AKS resource itself.

## Exercise 2: Connecting to the Cluster

Once your cluster is ready, let's connect to it. To work with Kubernetes, we use the kubectl command-line tool. Kubectl uses the concept of contexts - similar to how Docker CLI manages different environments.

To download the credentials for your AKS cluster, run:

```
az aks get-credentials -g labs-aks -n aks01 --overwrite-existing
```

This command does several things:
- It retrieves the cluster connection information
- It adds a new context to your kubectl configuration
- It sets this new context as your current context

You can verify which clusters you can connect to by running:

```
kubectl config get-contexts
```

You'll see an asterisk next to your AKS cluster, indicating it's your current context. Now, all kubectl commands will communicate with your Azure-hosted Kubernetes cluster.

Let's verify the connection by listing the nodes:

```
kubectl get nodes
```

You should see your two cluster nodes listed, both in the Ready state.

## Exercise 3: Deploying an Application

Now for the exciting part - deploying an application. One of the great things about Kubernetes is portability. The same YAML specifications that work on Docker Desktop or any other Kubernetes cluster will work on AKS.

In the labs folder, we have three YAML files:

First, **configmap.yaml** - This contains configuration data. In our case, it sets an environment name to "PROD".

Second, **deployment.yaml** - This defines how our application should run, including which container image to use, how many replicas to create, and environment variables to inject.

Third, **service.yaml** - This exposes our application to external traffic by routing incoming requests on port 80 to our application pods.

Let's deploy all three files at once. Kubectl can process an entire directory:

```
kubectl apply -f labs/aks/specs
```

Now let's check what was created:

```
kubectl get pods,services
```

You should see a pod for the simple-web application, and it should move to the Running state fairly quickly. You'll also see a service with the same name.

## Understanding External IP Assignment

Pay attention to the external IP address field in the service output. Initially, it might show as "pending". This is normal - Azure needs a moment to provision a public IP address and configure the load balancer.

If you see pending, you can watch for updates with:

```
kubectl get service simple-web --watch
```

Within a minute or two, you'll see an actual IP address appear. This is your application's public IP address.

## Accessing the Application

Once you have the IP address, open a web browser and navigate to it. You should see your application running. Take a moment to appreciate what just happened - you deployed a containerized application to a Kubernetes cluster in Azure, and it's now accessible from anywhere on the internet.

If you're curious, head back to the Azure Portal and explore the managed resource group. Can you find the public IP address resource? What about the load balancer that routes traffic to your cluster nodes?

## Exercise 4: Lab Challenge - Scaling the Application

For the lab challenge, let's explore scaling. Currently, we have one pod running our application. With spare capacity in our cluster, we can run multiple pods to serve more users.

Your challenge is to modify the deployment to run four pods instead of one. Here's what you need to do:

Open the deployment.yaml file and look for the replicas field. Change it from 1 to 4, then reapply the configuration:

```
kubectl apply -f labs/aks/specs/deployment.yaml
```

Watch the pods being created:

```
kubectl get pods --watch
```

You should see four pods running after a few moments.

Now, here's an interesting question to explore: With multiple pods running, what happens when you repeatedly refresh the website in your browser? Do you notice anything different? Think about how the load balancer might be distributing requests.

Also, try modifying the ConfigMap to change the environment name from "PROD" to something else, like "STAGING". After you reapply the ConfigMap, does the website update immediately? Or do you need to do something else? This will help you understand how Kubernetes handles configuration updates.

## Cleanup

When you're finished exploring, let's clean up the resources to avoid unnecessary charges. We can delete the entire resource group:

```
az group delete -y --no-wait -n labs-aks
```

The --no-wait flag means the command returns immediately without waiting for the deletion to complete. When the AKS cluster gets deleted, Azure automatically removes the managed MC resource group as well.

Finally, switch your kubectl context back to your local environment:

```
kubectl config use-context docker-desktop
```

This ensures that future kubectl commands won't accidentally try to connect to the deleted cluster.

## Summary

In this exercise, you've accomplished quite a bit:
- Created an AKS cluster using the Azure CLI
- Connected to the cluster using kubectl
- Deployed a multi-component application using Kubernetes YAML
- Explored scaling and configuration management
- Cleaned up resources properly

These are fundamental skills you'll use in every AKS project. Well done!
