# Azure Kubernetes Service

## Reference

Azure Kubernetes Service is Microsoft's managed Kubernetes offering that simplifies deploying and managing containerized applications in the cloud. AKS handles the complexity of provisioning VMs for cluster nodes, installing and configuring Kubernetes, and managing tasks like scaling, upgrading, and integrating with other Azure services. The documentation covers everything from basic cluster creation to advanced features like autoscaling and integration with Azure services. The command line interface provides complete control through the az aks commands.

## Explore in portal

Let's start by exploring what AKS offers in the Azure Portal.

**Navigate to the Portal**: We're opening the Azure Portal and searching for "Kubernetes Service" to create a new resource. Before creating anything, let's explore the available options to understand what AKS offers.

**Configuration Options**: You'll see there's a lot you can configure. The number of nodes and the VM size determine your cluster's capacity and cost. The Presets give you some good starting configurations for different scenarios - development, production, or cost-optimized.

**Node Pools**: AKS has Node Pools which are groups of nodes that share the same setup. You may have ten Linux nodes in one pool, five Linux servers with GPU in another pool, and two Windows servers in a third pool, all in the same cluster. This flexibility lets you run different types of workloads efficiently.

**Security and Integration**: Clusters can be secured with standard Kubernetes Role-Based Access Control linked to Azure accounts. AKS can be integrated with ACR so you can run containers from private ACR images without extra configuration. These integrations make AKS much easier to work with than managing Kubernetes yourself.

After exploring the Portal, we'll switch to the command line to create our cluster - this approach is much more suitable for automation and repeatability.

---

## Create an AKS cluster with the CLI

Let's start by creating our first AKS cluster. We'll begin with a new resource group.

**Create the Resource Group**: First, we're creating a resource group named "labs-aks" in the East US region. We're also adding a tag to help organize our resources - this is a best practice for tracking costs and managing resources across different projects and environments.

**Create the AKS Cluster**: Now, let's create the AKS cluster itself using az aks create. The command has many options, but we'll focus on the essentials for getting started.

We're creating a cluster named "aks01" in our resource group, starting with two nodes, which is a good minimum for high availability. We're using Standard D2s v5 VMs, which provide a good balance of compute and memory for general workloads. Note that VM sizes vary by region, so you might need to choose a different size depending on where you're deploying - the CLI will tell you if your chosen size isn't available.

This process will take several minutes. Azure is provisioning virtual machines, configuring networking, installing Kubernetes components, and setting up all the management infrastructure. While we wait, let's explore something interesting in the Azure Portal.

**Understanding Resource Groups**: While the cluster is being created, we're opening the Azure Portal and navigating to your resource groups. You'll notice something interesting - there are now two resource groups.

First, there's "labs-aks", which we created. This contains your AKS resource - the management object that represents your cluster.

Second, there's another resource group with a name that begins with "MC_" followed by your resource group name, cluster name, and region. This is the managed resource group that AKS creates automatically, and it's important to understand what this means.

The MC resource group contains all the underlying Azure resources that make your cluster work - virtual machines for the nodes, network interfaces, load balancers, network security groups, and more. This is important to understand: you shouldn't directly modify resources in this managed resource group. Think of it as a black box that Azure manages for you. All your interactions should go through the AKS resource itself - use kubectl for workloads and the az aks commands for cluster management.

---

## Using the cluster

Once your cluster is ready, let's connect to it. To work with Kubernetes, we use the kubectl command-line tool. Kubectl uses the concept of contexts - similar to how Docker CLI manages different environments.

**Download Credentials**: We're downloading the credentials for your AKS cluster using az aks get-credentials. This command does several things: it retrieves the cluster connection information from Azure, it adds a new context to your kubectl configuration file, and it sets this new context as your current context so kubectl commands immediately target this cluster.

**View Contexts**: You can verify which clusters you can connect to by running kubectl config get-contexts. You'll see an asterisk next to your AKS cluster, indicating it's your current context. If you have multiple clusters - perhaps a local Docker Desktop cluster and several AKS clusters - you can see them all listed here.

**Verify Connection**: Now, all kubectl commands will communicate with your Azure-hosted Kubernetes cluster. Let's verify the connection by listing the nodes using kubectl get nodes. You should see your two cluster nodes listed, both in the Ready state. These are the virtual machines running in Azure that will host your containerized workloads.

---

## Deploying applications

Now for the exciting part - deploying an application. One of the great things about Kubernetes is portability. The same YAML specifications that work on Docker Desktop or any other Kubernetes cluster will work on AKS. This is the power of standardization.

**Understanding the Manifests**: In the labs folder, we have three YAML files. First, configmap.yaml - this contains configuration data, in our case setting an environment name to "PROD". Second, deployment.yaml - this defines how our application should run, including which container image to use, how many replicas to create, and environment variables to inject. Third, service.yaml - this exposes our application to external traffic by routing incoming requests on port 80 to our application pods.

**Deploy the Application**: Let's deploy all three files at once. Kubectl can process an entire directory, so we're using kubectl apply pointing to the specs directory.

**Check What Was Created**: Now we're checking what was created using kubectl get pods and services. You should see a pod for the simple-web application, and it should move to the Running state fairly quickly as Kubernetes pulls the container image and starts it. You'll also see a service with the same name.

**Watch for IP Assignment**: Pay attention to the external IP address field in the service output. Initially, it might show as "pending". This is normal - Azure needs a moment to provision a public IP address and configure the load balancer. Behind the scenes, Azure is creating a real Azure Load Balancer resource in the managed resource group and assigning it a public IP.

If you see pending, you can watch for updates using kubectl get service with the watch flag. Within a minute or two, you'll see an actual IP address appear. This is your application's public IP address, accessible from anywhere on the internet.

**Test the Application**: Once you have the IP address, we're opening a web browser and navigating to it. You should see your application running, displaying the hostname and environment information. Take a moment to appreciate what just happened - you deployed a containerized application to a Kubernetes cluster in Azure, and it's now accessible from anywhere on the internet with automatic load balancing and health monitoring.

**Explore the Portal**: If you're curious, head back to the Azure Portal and explore the managed resource group. Can you find the public IP address resource? What about the load balancer that routes traffic to your cluster nodes? You'll see all the infrastructure Azure created automatically to support your application.

---

## Lab

For the lab challenge, let's explore scaling. Currently, we have one pod running our application. With spare capacity in our cluster, we can run multiple pods to serve more users and provide redundancy.

**Your Challenge**: Modify the deployment to run four pods instead of one. Open the deployment.yaml file and look for the replicas field. Change it from 1 to 4, then reapply the configuration using kubectl apply.

**Watch the Scaling**: We're watching the pods being created using kubectl get pods with the watch flag. You should see four pods running after a few moments. Kubernetes is distributing these pods across your available nodes for better resilience.

**Explore Load Balancing**: Now, here's an interesting question to explore: With multiple pods running, what happens when you repeatedly refresh the website in your browser? Do you notice anything different in the hostname displayed? Think about how the load balancer might be distributing requests across the pods.

**Configuration Updates**: Also, try modifying the ConfigMap to change the environment name from "PROD" to something else, like "STAGING". After you reapply the ConfigMap using kubectl apply, does the website update immediately when you refresh? Or do you need to do something else? This will help you understand how Kubernetes handles configuration updates - ConfigMaps are loaded when pods start, so existing pods don't automatically pick up changes. You'd need to restart the pods to see the new configuration.

---

## Cleanup

When you're finished exploring, let's clean up the resources to avoid unnecessary charges.

**Delete the Resource Group**: We're deleting the entire resource group using az group delete with the yes flag to skip confirmation and the no-wait flag to return immediately without waiting for the deletion to complete. When the AKS cluster gets deleted, Azure automatically removes the managed MC resource group as well, cleaning up all the underlying infrastructure.

**Switch Kubectl Context**: Finally, we're switching your kubectl context back to your local environment using kubectl config use-context docker-desktop. This ensures that future kubectl commands won't accidentally try to connect to the deleted cluster.
