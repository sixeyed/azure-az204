# Distributed Apps on Azure Container Instances

## Reference

ACI is the simplest container platform on Azure where you can run single containers or multiple containers in a group to host distributed applications. There are different options for modelling applications including Azure's YAML specification with the Azure CLI and the Docker Compose specification with the Docker CLI. The ACI container groups documentation covers the architectural patterns and integration capabilities. The command line interface gives you multiple deployment paths through both the az container commands and the docker compose commands, which we'll explore in these exercises.

## Deploy a distributed app with ACI YAML

Let's start by creating a Resource Group for this lab. We're calling it "labs-aci-compose" and deploying it to the East US region. The command includes a tag parameter set to "courselabs=azure" which helps us identify and track resources created for this course.

Now let's look at the ACI YAML model. The YAML format for ACI is a custom specification that looks somewhat like Bicep and somewhat like Compose, but it's neither - it's Azure's own format for defining container groups.

We're opening the file rng-aci-v1.yaml to examine it. This file defines a container group with two containers - a random number API and a website that calls that API. Notice some specific details required in this model: Container sizes for CPU and memory are mandatory because ACI needs to know this to provision the right compute resources. Since containers in a group share the same network space, the environment variables configure communication using localhost. Any services you want to expose publicly need ports specified at both the IP address level and the container level.

Let's deploy this app using the az container create command with the YAML file. We're pointing it to our resource group, giving the container group a name of "rng-app", and specifying the YAML file from the labs directory.

While the deployment is running, let's talk about what's happening. Azure is provisioning compute resources based on the specifications in your YAML file, pulling the container images from the registry, and starting both containers in the same container group. This process takes a minute or two to complete.

Once deployment completes, we're opening the ACI resource in the Azure Portal. Under the Containers section, you should see both the API and web containers running. You can view properties and logs for each container individually, and even connect to a shell session inside a container for debugging purposes.

The YAML specification didn't include a DNS name, but you'll see there's a public IP address assigned. Let's test the application by browsing to that IP address. When the page loads, click the button and you should see a random number appear. This demonstrates that the web container is successfully communicating with the API container through their shared network space.

**Updating Container Configuration**: Now let's look at the API container logs. You'll notice they don't give us much detail - we're only seeing basic startup information without detailed request logging. We can increase the logging level by modifying the container configuration.

We're opening rng-aci-v2.yaml to examine the changes. This version adds a new environment variable to each container called "Logging__LogLevel__Default" set to "Information" to enable more verbose logging. This gives us better visibility into what the containers are doing.

Let's deploy this updated specification using the same az container create command but pointing to the v2 YAML file. Watch what happens - the command shows "Running..." for a while and stays in that state for several minutes. What's actually happening is that ACI is recreating the containers with the new configuration.

We're checking the Events table for the containers in the Portal. You'll see multiple "Started" events and "Killing" events for the old containers. This illustrates an important principle: you cannot change properties of the compute environment for a running container. If you need to update environment variables, resource requests, or ports, the only way is to remove the old container and create a replacement. This behavior is actually true for all container runtimes - Docker, ACI, and Kubernetes all work this way. It's the container paradigm at work.

## Deploy a Compose App to ACI

The ACI YAML specification gives you access to all ACI features, but if you don't need ACI-specific configuration, you can use a standard Docker Compose file instead and deploy with the Docker CLI.

Let's look at rng-compose-v1.yml. This Compose model is much simpler than the ACI YAML we just used. It still uses the same container images, but the Docker ACI integration handles many of the ACI-specific details automatically - things like CPU and memory defaults, networking configuration, and port exposure are all managed for you.

Before we can deploy with Docker Compose, we need to set up a Docker Context so our local Docker CLI can communicate with Azure. If you've completed the basic ACI lab, you may already have this configured, but let's go through the steps to make sure everything is set up correctly.

First, we're authenticating with Azure using docker login azure. This opens your browser for Azure authentication, just like az login does. Complete the sign-in process and the Docker CLI will be authenticated to work with your Azure subscription.

Next, we're creating a context for ACI targeting our lab resource group. We're using docker context create with the aci type, naming it "labs-aci-compose", and associating it with our labs-aci-compose resource group. If you have multiple subscriptions, the CLI will prompt you to select which one to use - make sure to choose the subscription where you created the resource group.

Then we're switching to that context using docker context use. This is where it gets interesting - we're telling Docker to use Azure instead of your local machine. From this point forward, when you run Docker and Compose commands, they're actually operating on Azure Container Instances, not your local Docker Desktop. The commands look the same, but they're doing something completely different under the hood.

We're running docker ps to list running containers. You'll see the containers you deployed earlier with the az command, but now you're viewing them through the Docker CLI. Notice the format is slightly different from local Docker - it shows the domain name and exposed ports in an ACI-specific format, but it's still recognizable as a container list.

Let's deploy the application using Docker Compose. We're using docker compose with the file flag pointing to our v1 compose file, setting the project name to "rng-app-2", and using the up command with detached mode. You'll see output about the container group being created first, then the individual containers are created in parallel.

You can view your new containers in the Portal, or use the docker ps command to see details. When listing ACI containers through Docker, the output includes the IP address assigned to the container group.

We're browsing to the new deployment's IP address to verify the app is working. Click the button and you should see random numbers appearing, confirming that both containers are running and communicating properly.

Now let's open the container list in the Portal. You'll notice there are three containers even though we only defined two in the Compose model. The additional container is a sidecar that the Docker ACI integration adds automatically - it helps with networking and communication between containers in the group.

## ACI containers and Storage Accounts

Now let's explore how ACI containers can integrate with Azure Storage services. We'll use both Blob Storage and Azure Files to demonstrate different storage integration patterns.

First, we're creating a Storage Account. Remember to use a globally unique name - something like "saacilabs" followed by your initials or a random number. We're using the Standard ZRS SKU for zone-redundant storage, deploying to the same resource group, and placing it in West Europe to demonstrate that storage and compute can be in different regions.

We're getting the connection string for this Storage Account using az storage account show-connection-string. The query parameter extracts just the connection string value, and the output format is set to tsv for plain text. Copy this connection string value - we'll need it in a moment.

Let's test this locally first to understand how the application works. We're switching back to your local Docker engine using docker context use default. This ensures we're running containers locally, not in ACI.

Now we're running a container that uses Blob Storage as its database. The container is named "local", running in detached mode, mapping port 8013 to container port 80, and using an environment variable called ConnectionStrings__AssetsDb with your storage account connection string. Be careful with the quotes - they need to wrap the entire connection string to handle special characters. We're using the courselabs/asset-manager:22.11 image.

We're browsing to localhost:8013 and you'll see data on the screen - asset information that the application is storing and retrieving. Opening your Blob Storage container in the Azure Portal shows the raw data. There's the actual blob data, uploaded from your local container. The application is treating Azure Blob Storage as its database.

This container also writes a file to local storage using the container name as the filename. We're executing a command inside the container to list the contents of /app/lockfiles. You'll see a file named "local" - that's the lockfile the container created.

**Using Azure Files with ACI**: ACI containers can access Blob Storage using connection strings just like we did locally. But ACI also supports mounting Azure Files shares directly as volumes. When mounted, the share appears as part of the container filesystem, but data written there is actually stored in Azure Files. This is particularly useful for sharing data between containers or persisting data that needs to survive container restarts.

Let's create a file share called "assetmanager" in your Storage Account using az storage share create with the share name and account name parameters.

Now we're getting your Storage Account key using az storage account keys list. The query parameter extracts the first key's value. This key will look like a long base64-encoded string - copy this value as well.

We're opening the file assetmanager-aci.yaml to edit it. This YAML file has three placeholders that need to be replaced: Replace the sa-name placeholder with your Storage Account name, the sa-key placeholder with your Storage Account key, and the connection-string placeholder with your Storage Account connection string.

Looking at this YAML file, notice how it configures the container to use Blob Storage through the connection string environment variable, and it also defines a volume that mounts an Azure Files share at /app/lockfiles inside the container. This demonstrates both storage integration methods in a single container.

We're deploying the ACI group using az container create with the YAML file. The deployment process provisions the container, pulls the image, connects to the storage account, and mounts the file share.

Once it's running, we're browsing to the app's IP address. The app is reading and writing to Blob Storage for its main data - you'll see the same asset information we saw earlier. Now, let's check your Azure Files share in the Portal under your Storage Account. We're navigating to File shares and opening the "assetmanager" share. You should see a file there written by the container. The container thinks it's writing to local storage at /app/lockfiles, but it's actually writing to Azure Files. The file persists beyond the container lifecycle and can be accessed directly through the Azure Portal or via SMB.

This demonstrates the power of ACI's storage integration - you can persist data beyond the container lifecycle without changing your application code. The application doesn't know it's writing to cloud storage; it just writes to a path that happens to be a mounted Azure Files share.

---

## Lab

ACI is designed to be a quick and easy solution for running containers in the cloud. It provides reliability through automatic container restarts if they fail, but it doesn't have built-in horizontal scaling features like load balancing across multiple instances.

Here's your challenge: Run another copy of the Asset Manager app in ACI. Do both instances write to the same file share? How would you load-balance traffic between multiple instances?

Think about: How to deploy a second instance with a different name but the same configuration. Whether multiple containers can mount the same Azure Files share simultaneously and if they interfere with each other. What Azure service you might use for load balancing traffic between multiple ACI instances. The limitations of ACI for production workloads requiring scale, and when you might need to move to a more sophisticated orchestration platform like AKS.

Take some time to work through this challenge. If you get stuck, check the hints file or look at the solution to see one possible approach.

---

## Cleanup

When you're finished with the lab, you can delete the Resource Group to remove all resources, including containers created with the Docker CLI. We're using az group delete with the yes flag to skip confirmation prompts and the no-wait flag so the command returns immediately without waiting for the deletion to complete in the background.

Don't forget to change your Docker context back to local using docker context use default. This ensures your Docker CLI is back to working with your local Docker Desktop. We're also removing the lab context using docker context rm to clean up the context definition from your Docker configuration.

This cleanup is important - ACI containers continue running and incurring charges until you explicitly delete them, so proper cleanup ensures you're not paying for resources you're no longer using.
