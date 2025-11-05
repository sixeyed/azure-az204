# Distributed Apps on Azure Container Instances - Exercise Narration

## Exercise 1: Deploy a Distributed App with ACI YAML

Let's start by creating a Resource Group for this lab. We'll call it "labs-aci-compose" and deploy it to the East US region:

```bash
az group create -n labs-aci-compose --tags courselabs=azure -l eastus
```

Now let's look at the ACI YAML model. The YAML format for ACI is a custom specification that looks somewhat like Bicep and somewhat like Compose, but it's neither. It's Azure's own format for defining container groups.

Open the file `rng-aci-v1.yaml`. This file defines a container group with two containers - a random number API and a website that calls that API. Notice some specific details required in this model:

- Container sizes for CPU and memory are mandatory. ACI needs to know this to provision the right compute resources.
- Since containers in a group share the same network space, the environment variables configure communication using `localhost`.
- Any services you want to expose publicly need ports specified at both the IP address level and the container level.

Let's deploy this app. Use the `az container create` command with the YAML file:

```bash
az container create -g labs-aci-compose -n rng-app --file labs/aci-compose/rng-aci-v1.yaml
```

While the deployment is running, let's talk about what's happening. Azure is provisioning compute resources based on the specifications in your YAML file, pulling the container images, and starting both containers in the same container group.

Once deployment completes, open the ACI resource in the Azure Portal. Under the Containers section, you should see both the API and web containers running. You can view properties and logs for each container individually, and even connect to a shell session inside a container for debugging purposes.

The YAML specification didn't include a DNS name, but you'll see there's a public IP address. Let's test the application. Browse to that IP address and click the button - you should see a random number appear.

### Updating Container Configuration

Now let's look at the API container logs. You'll notice they don't give us much detail. We can increase the logging level by modifying the container configuration.

Open `rng-aci-v2.yaml`. This version adds a new environment variable to each container to enable more verbose logging.

Let's deploy this updated specification:

```bash
az container create -g labs-aci-compose -n rng-app --file labs/aci-compose/rng-aci-v2.yaml
```

Watch what happens. The command shows "Running..." for a while. What's actually happening is that ACI is recreating the containers with the new configuration.

Check the Events table for the containers in the Portal. You'll see multiple "Started" events and "Killing" events for the old containers. This illustrates an important principle: you cannot change properties of the compute environment for a running container. If you need to update environment variables, resource requests, or ports, the only way is to remove the old container and create a replacement. This behavior is actually true for all container runtimes - Docker, ACI, and Kubernetes all work this way.

## Exercise 2: Deploy a Compose App to ACI

The ACI YAML specification gives you access to all ACI features, but if you don't need ACI-specific configuration, you can use a standard Docker Compose file instead and deploy with the Docker CLI.

Let's look at `rng-compose-v1.yml`. This Compose model is much simpler than the ACI YAML. It still uses the same container images, but the Docker ACI integration handles many of the ACI-specific details automatically.

Before we can deploy with Docker Compose, we need to set up a Docker Context so our local Docker CLI can communicate with Azure. If you've completed the basic ACI lab, you may already have this configured, but let's go through the steps:

First, authenticate with Azure:

```bash
docker login azure
```

Next, create a context for ACI targeting our lab resource group:

```bash
docker context create aci labs-aci-compose --resource-group labs-aci-compose
```

Then switch to that context:

```bash
docker context use labs-aci-compose
```

Now when you run Docker and Compose commands, you're working in the context of ACI in your lab resource group. Try running `docker ps` - you'll see the containers you deployed earlier with the `az` command.

Let's deploy the application using Docker Compose:

```bash
docker compose -f labs/aci-compose/rng-compose-v1.yml --project-name rng-app-2 up -d
```

You'll see output about the container group being created, then the individual containers are created in parallel.

You can view your new containers in the Portal, or use the Docker command to see details. When listing ACI containers, the output includes the IP address:

```bash
docker ps
```

Browse to the new deployment's IP address and verify the app is working. Then open the container list in the Portal. You'll notice there are three containers even though we only defined two in the Compose model. The additional container is a sidecar that the Docker ACI integration adds automatically - it helps with networking and communication between containers.

## Exercise 3: ACI Containers and Storage Accounts

Now let's explore how ACI containers can integrate with Azure Storage services. We'll use both Blob Storage and Azure Files.

First, create a Storage Account. Remember to use a globally unique name:

```bash
az storage account create --sku Standard_ZRS -g labs-aci-compose -l westeurope -n <sa-name>
```

Get the connection string for this Storage Account:

```bash
az storage account show-connection-string -g labs-aci-compose --query connectionString -o tsv -n <sa-name>
```

*[SHOW ON SCREEN: The connection string from the command output]*

Copy the connection string value. Let's test this locally first. Switch back to your local Docker engine:

```bash
docker context use default
```

Now run a container that uses Blob Storage as its database. Be careful with the quotes - they need to wrap the entire connection string:

```bash
docker run --name local -d -p 8013:80 -e 'ConnectionStrings__AssetsDb=<connection-string>' courselabs/asset-manager:22.11
```

Browse to `http://localhost:8013` and you'll see data on the screen. Open your Blob Storage container in the Azure Portal - there's the raw data, uploaded from your local container.

This container also writes a file to local storage using the container name as the filename. List the contents to see:

```bash
docker exec local ls /app/lockfiles
```

### Using Azure Files with ACI

ACI containers can access Blob Storage using connection strings just like we did locally. But ACI also supports mounting Azure Files shares directly. When mounted, the share appears as part of the container filesystem, but data written there is actually stored in Azure Files.

Let's create a file share called "assetmanager" in your Storage Account:

```bash
az storage share create -n assetmanager --account-name <sa-name>
```

Now get your Storage Account key:

```bash
az storage account keys list -g labs-aci-compose --query "[0].value" -o tsv --account-name <sa-name>
```

The key will look something like: `abc123def456...` (a long base64-encoded string)

Open the file `assetmanager-aci.yaml` and edit it to replace these placeholders:
- Replace `<sa-name>` with your Storage Account name
- Replace `<sa-key>` with your Storage Account key
- Replace `<connection-string>` with your Storage Account connection string

This YAML file configures the container to:
- Use Blob Storage through the connection string environment variable
- Mount an Azure Files share at `/app/lockfiles` inside the container

Deploy the ACI group:

```bash
az container create -g labs-aci-compose --file labs/aci-compose/assetmanager-aci.yaml
```

Once it's running, browse to the app's IP address. The app is reading and writing to Blob Storage for its main data. Now, check your Azure Files share in the Portal under your Storage Account. Can you find the lock file? Look in the "assetmanager" share - you should see a file there written by the container. The container thinks it's writing to local storage, but it's actually writing to Azure Files.

This demonstrates the power of ACI's storage integration - you can persist data beyond the container lifecycle without changing your application code.

## Lab Challenge

ACI is designed to be a quick and easy solution for running containers in the cloud. It provides reliability through automatic container restarts if they fail, but it doesn't have built-in horizontal scaling features.

Here's your challenge: Run another copy of the Asset Manager app in ACI. Do both instances write to the same file share? How would you load-balance traffic between multiple instances?

Think about:
- How to deploy a second instance with a different name
- Whether multiple containers can mount the same Azure Files share
- What Azure service you might use for load balancing
- The limitations of ACI for production workloads requiring scale

Take some time to work through this challenge. If you get stuck, check the hints file or look at the solution.

## Cleanup

When you're finished with the lab, you can delete the Resource Group to remove all resources, including containers created with the Docker CLI:

```bash
az group delete -y --no-wait -n labs-aci-compose
```

Don't forget to change your Docker context back to local and remove the lab context:

```bash
docker context use default
docker context rm labs-aci-compose
```

This ensures your Docker CLI is back to working with your local Docker Desktop.
