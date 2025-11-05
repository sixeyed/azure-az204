# Azure Container Instances - Exercises Walkthrough

## Exercise 1: Explore Azure Container Instances in the Portal

Let's start by exploring what ACI offers through the Azure Portal interface.

**Navigate to the Portal**: Open portal.azure.com and search for "Container Instances" in the top search bar. Click "Create" to start the creation wizard.

**Review the Basics Tab**: Here you'll see the fundamental settings:
- **Subscription and Resource Group**: Where your container will be deployed
- **Container name**: A unique identifier for your instance
- **Region**: The Azure region where your container will run
- **Image source**: Notice you can pull from Azure Container Registry, Docker Hub, or other registries
- **Image**: The container image to run, like "nginx:latest" or your custom applications

**Check the Compute Tab**: This is where you control resources:
- **OS type**: Linux or Windows containers - both are supported
- **Size**: CPU cores and memory - you have granular control from 1 vCPU and 1GB RAM up to 4 vCPUs and 16GB
- This flexibility means you can right-size your container to your workload

**Explore the Networking Tab**: Network configuration options include:
- **Ports**: Which ports to expose - 80 for HTTP, 443 for HTTPS, or custom ports
- **DNS name label**: Set a friendly name prefix, and Azure creates the full DNS name for you
- **Networking type**: Public or private network access

**Review Advanced Options**: Additional configuration includes:
- **Restart policy**: Always, OnFailure, or Never - controls container restart behavior
- **Environment variables**: Pass configuration to your container
- **Command override**: Override the container's default startup command

Don't create the container yet - we'll do that with the Azure CLI for better repeatability and automation.

---

## Exercise 2: Create an ACI Container with the Azure CLI

Now let's deploy a real container using the command line. This approach is more suitable for automation and version control.

**Create a Resource Group**: Every Azure resource needs a home. Let's create a resource group for this lab:

```bash
az group create -n labs-aci --tags courselabs=azure -l eastus
```

This creates a resource group named "labs-aci" in the East US region. The tag helps us identify lab resources.

**Deploy Your First Container**: We'll use the `az container create` command. This single command provisions and starts a container in Azure:

```bash
az container create -g labs-aci --name simple-web --image courselabs/simple-web:6.0 --ports 80 --dns-name-label <your-unique-dns-name>
```

Replace `<your-unique-dns-name>` with something unique like "myapp-yourname-123". The DNS name must be globally unique within the Azure region.

**What's happening here?**
- `-g labs-aci`: Deploy to our resource group
- `--name simple-web`: Name the container instance
- `--image courselabs/simple-web:6.0`: Pull this image from Docker Hub
- `--ports 80`: Expose port 80 for HTTP traffic
- `--dns-name-label`: Create a public DNS name

**Wait for Deployment**: The command takes a minute or two. Azure is provisioning infrastructure, pulling the image, and starting your container. When it completes, you'll see JSON output with all the container details.

**Find Your Container URL**: Look for the "fqdn" field in the output. It will look something like:
```
<your-dns-name>.eastus.azurecontainer.io
```

**Test Your Application**: Open a browser and navigate to the FQDN. You should see the simple-web application running. If it's not immediately available, wait a minute - the container might still be initializing.

**View Container Logs**: Just like with Docker, you can view application logs:

```bash
az container logs -g labs-aci -n simple-web
```

You'll see the ASP.NET Core application startup logs and any HTTP requests. This is invaluable for debugging.

**Inspect Container Details**: Get comprehensive information about your running container:

```bash
az container show -g labs-aci -n simple-web
```

This shows CPU, memory, networking configuration, current state, and more.

---

## Exercise 3: Deploy to ACI from Docker CLI

If you're a Docker user, you'll love this integration. The Docker CLI can deploy directly to Azure Container Instances using contexts.

**Understand Docker Contexts**: A Docker context tells the Docker CLI where to send commands - your local machine, a remote Docker host, or Azure ACI. It's like switching between different Docker environments.

**Login to Azure from Docker**: The Docker CLI needs its own authentication:

```bash
docker login azure
```

This opens your browser for Azure authentication, just like `az login`. Complete the sign-in process.

**Create an ACI Context**: Link Docker to your Azure Resource Group:

```bash
docker context create aci labs-aci --resource-group labs-aci
```

The CLI will prompt you to select your subscription if you have multiple. Choose the one where you created the labs-aci resource group.

**Switch to the ACI Context**: Point Docker to use Azure instead of your local machine:

```bash
docker context use labs-aci
```

Now when you run Docker commands, they operate on ACI, not your local Docker Desktop.

**List Running Containers**: Use the familiar Docker command:

```bash
docker ps
```

You'll see your ACI containers listed, including the one created with `az container create`. Notice the format is slightly different - it shows the domain name and exposed ports.

**View Container Logs**: Just like locally:

```bash
docker logs <container-id>
```

Replace `<container-id>` with one from the `docker ps` output.

**Deploy a New Container with Docker**: Now use standard Docker commands to create an ACI container:

```bash
docker run -d -p 80:80 --domainname <another-unique-dns-name> courselabs/simple-web:6.0
```

This feels like running Docker locally, but it's creating a real Azure Container Instance! The `--domainname` parameter is ACI-specific for setting the DNS label.

**Verify Both Containers**: List containers using both CLIs:

```bash
docker ps
az container list -o table
```

Both commands show the same containers. The Docker-created container has a random name, while the CLI-created one has the name we specified.

**Browse Both Applications**: Both containers are running the same image on different domain names. Test them both to verify they're working.

---

## Exercise 4: Lab Challenge - Windows Containers

Here's your challenge: The simple-web image has both Windows and Linux variants. Explore the differences.

**The Challenge**:
1. Run an ACI container using the Windows version of the image
2. Compare the behavior and startup time to the Linux version
3. Try running the ARM64 Linux variant - what happens?

**Hints to Get Started**:

Docker images can have multiple tags for different architectures. Check the [Docker Hub tags](https://hub.docker.com/r/courselabs/simple-web/tags) for the simple-web image.

To specify a Windows container in ACI, use the `--os-type` parameter:
```bash
az container create -g labs-aci --name simple-web-windows --image courselabs/simple-web:6.0-windows --os-type Windows --ports 80 --dns-name-label <unique-dns-name>
```

For ARM64 images, Azure's x86 infrastructure might not support them directly.

**What to Observe**:
- **Startup time**: Windows containers typically take longer to start than Linux
- **Resource usage**: Windows containers generally use more memory
- **Compatibility**: Not all container images work on all platforms
- **Image size**: Windows base images are significantly larger

**Questions to Explore**:
- How does the Windows container startup time compare?
- What happens when you try to run an ARM-based image on Azure's x86 infrastructure?
- Can you successfully access both Windows and Linux versions of the application?

---

## Exercise 5: Resource Management and Monitoring

Let's explore how to manage and monitor your running containers.

**Check Container State**: View the current state of a container:

```bash
az container show -g labs-aci -n simple-web --query "containers[0].instanceView.currentState"
```

This shows whether the container is running, terminated, or in another state.

**Monitor Resource Usage**: While ACI doesn't provide real-time metrics via the CLI, you can see configured limits:

```bash
az container show -g labs-aci -n simple-web --query "containers[0].resources.requests"
```

**Restart a Container**: Sometimes you need to restart:

```bash
az container restart -g labs-aci -n simple-web
```

**Stop and Start**: You can't stop/start ACI containers like VMs. You delete and recreate them. This is the container paradigm - containers are ephemeral.

**Update a Container**: To change CPU, memory, or image version:
1. Delete the existing container
2. Create a new one with updated parameters
3. This ensures clean state and updated configuration

---

## Cleanup

**Important**: ACI containers continue running and incurring charges until you delete them.

**Delete with Docker Context**: If you're still in the labs-aci context:

```bash
docker rm -f <container-id>
```

**Switch Back to Local Context**: Don't forget to switch back:

```bash
docker context use default
```

**Delete Everything**: Remove the entire resource group and all containers:

```bash
az group delete -y --no-wait -n labs-aci
```

The `--no-wait` flag returns immediately without waiting for deletion to complete.

**Remove Docker Context**: Clean up the ACI context:

```bash
docker context rm labs-aci
```

**Verify Cleanup**: Check that containers are gone:

```bash
az container list -g labs-aci
```

Should return an error or empty list since the resource group is deleted.

---

## Key Takeaways

- **ACI is the simplest way** to run containers in Azure - no infrastructure management
- **Multiple deployment methods**: Azure CLI, Portal, Docker CLI, ARM templates, and more
- **Docker integration** lets you use familiar commands while deploying to Azure
- **Flexibility**: Support for Linux and Windows, custom compute sizes, and networking options
- **Container paradigm**: Treat containers as ephemeral - recreate rather than modify
- **Cost awareness**: Remember to delete containers when done to avoid charges

Excellent work! You now understand how to deploy and manage containers in Azure Container Instances.
