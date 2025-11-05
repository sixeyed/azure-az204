# Azure Container Instances - Exercises Walkthrough

## Exercise 1: Explore Azure Container Instances in the Portal

Let's start by exploring what ACI offers through the Azure Portal interface.

**Navigate to the Portal**: We're opening the Azure Portal and searching for "Container Instances" in the top search bar, then clicking "Create" to start the creation wizard. This gives us a good overview of all the configuration options available.

**Review the Basics Tab**: Here we see the fundamental settings for deploying a container. First up is the subscription and resource group - this determines where your container will be deployed and how it's organized with your other Azure resources. You'll specify a unique container name to identify this instance, and choose the Azure region where your container will physically run. The image source setting is particularly interesting - you can pull from Azure Container Registry for private images, Docker Hub for public images, or any other container registry you have access to. The image field is where you specify which container image to run, whether that's something standard like nginx:latest or your own custom applications.

**Check the Compute Tab**: This is where you control the compute resources allocated to your container. The OS type setting lets you choose between Linux and Windows containers - both are fully supported in ACI. The size configuration is where you see the real flexibility of ACI - you have granular control over CPU cores and memory, ranging from 1 vCPU and 1GB RAM all the way up to 4 vCPUs and 16GB. This means you can right-size your container to match your workload exactly, paying only for the resources you actually need.

**Explore the Networking Tab**: The networking options let you configure how your container communicates with the outside world. You'll specify which ports to expose - typically port 80 for HTTP, 443 for HTTPS, or any custom ports your application needs. The DNS name label setting is particularly convenient - you provide a friendly name prefix, and Azure automatically creates the full DNS name for you. You can also control whether your container has public internet access or is restricted to private network access.

**Review Advanced Options**: The advanced section includes several important configuration options. The restart policy controls what happens when your container stops - you can set it to always restart, only restart on failure, or never restart automatically. Environment variables let you pass configuration into your container without baking it into the image. And the command override option lets you override the container's default startup command if you need to run it differently from how it was built.

We're not going to create the container through the portal - instead, we'll use the Azure CLI for better repeatability and automation.

---

## Exercise 2: Create an ACI Container with the Azure CLI

Now let's deploy a real container using the command line. This approach is much more suitable for automation and version control than clicking through the portal.

**Create a Resource Group**: Every Azure resource needs a home, so we're starting by creating a resource group for this lab. We're calling it "labs-aci" and placing it in the East US region. The command also includes a tag parameter set to "courselabs=azure" which helps us identify and track resources created for this course - this is a best practice for organizing resources.

**Deploy Your First Container**: Now we're using the az container create command to actually provision and start a container in Azure. This is where the real magic happens - a single command that takes care of everything. We're deploying to our labs-aci resource group, naming the container "simple-web", and pulling the image courselabs/simple-web:6.0 from Docker Hub. We're exposing port 80 for HTTP traffic, and setting a DNS name label that must be globally unique within the Azure region - something like "myapp-yourname-123" works well.

**What's happening here?**: Let's break down what each parameter does. The -g flag specifies our resource group where everything will be deployed. The --name parameter gives our container instance a friendly name we can use to reference it later. The --image parameter tells Azure which container image to pull and run - in this case, it's pulling from Docker Hub since we didn't specify a registry. The --ports parameter opens port 80 so we can access the web application, and the --dns-name-label creates a public DNS name that will make our container accessible on the internet.

**Wait for Deployment**: The command takes a minute or two to complete. Behind the scenes, Azure is provisioning the infrastructure, pulling the container image from Docker Hub, and starting your container. When it finishes, you'll see JSON output containing all the container details - things like the fully qualified domain name, IP address, provisioning state, and resource configuration.

**Find Your Container URL**: In the JSON output, we're looking for the "fqdn" field - that's the fully qualified domain name. It will look something like your-dns-name.eastus.azurecontainer.io. This is the public URL where your application is now accessible.

**Test Your Application**: Opening a browser and navigating to that FQDN shows the simple-web application running. If it's not immediately available, give it a minute - the container might still be initializing and starting up the web server.

**View Container Logs**: Just like with Docker running locally, you can view the application logs using the az container logs command. You'll see the ASP.NET Core application startup messages and any HTTP requests that have come in. This is invaluable for debugging and understanding what's happening inside your container.

**Inspect Container Details**: The az container show command gives you comprehensive information about your running container - CPU and memory allocation, networking configuration, the current state, environment variables, and much more. This is your window into understanding the container's complete configuration and status.

---

## Exercise 3: Deploy to ACI from Docker CLI

If you're a Docker user, you'll love this integration. The Docker CLI can deploy directly to Azure Container Instances using a feature called contexts.

**Understand Docker Contexts**: A Docker context tells the Docker CLI where to send commands - whether that's your local machine, a remote Docker host, or Azure ACI. It's essentially like switching between different Docker environments, but from the same command line interface.

**Login to Azure from Docker**: The Docker CLI needs its own authentication separate from the Azure CLI. Running docker login azure opens your browser for Azure authentication, just like az login does. Complete the sign-in process and the Docker CLI will be authenticated to work with your Azure subscription.

**Create an ACI Context**: Now we're linking Docker to our Azure Resource Group by creating a context specifically for ACI. We're naming the context "labs-aci" and associating it with our labs-aci resource group. If you have multiple subscriptions, the CLI will prompt you to select which one to use - make sure to choose the subscription where you created the labs-aci resource group.

**Switch to the ACI Context**: This is where it gets interesting - we're telling Docker to use Azure instead of your local machine. The docker context use command switches the active context. From this point forward, when you run Docker commands, they're actually operating on Azure Container Instances, not your local Docker Desktop. The commands look the same, but they're doing something completely different under the hood.

**List Running Containers**: Using the familiar docker ps command now shows your ACI containers, including the one we created earlier with az container create. Notice the format is slightly different from local Docker - it shows the domain name and exposed ports in an ACI-specific format, but it's still recognizable as a container list.

**View Container Logs**: Just like working with local containers, you can use docker logs with a container ID from the docker ps output. This retrieves the logs from your ACI container in Azure, even though you're using the exact same command you'd use for local containers.

**Deploy a New Container with Docker**: Here's where it really comes together - we're using the standard docker run command to create an ACI container. We're running it in detached mode, mapping port 80, setting a unique domain name, and specifying the courselabs/simple-web:6.0 image. This feels exactly like running Docker locally, but it's actually creating a real Azure Container Instance in the cloud. The --domainname parameter is ACI-specific for setting the DNS label.

**Verify Both Containers**: We can list containers using both the Docker CLI and the Azure CLI, and both commands show the same containers. The Docker-created container has a randomly generated name, while the one we created with az container create has the specific name we gave it. But they're all managed ACI containers visible through either interface.

**Browse Both Applications**: Both containers are running the same image on different domain names. We can test them both in a browser to verify they're working - two separate container instances, both accessible on the internet, managed through either the Docker CLI or Azure CLI.

---

## Exercise 4: Lab Challenge - Windows Containers

Here's your challenge: The simple-web image has both Windows and Linux variants, and we want to explore the differences between them.

**The Challenge**: First, run an ACI container using the Windows version of the image. Then, compare the behavior and startup time to the Linux version we've already deployed. Finally, try running the ARM64 Linux variant and see what happens.

**Hints to Get Started**: Docker images can have multiple tags for different architectures. Checking the Docker Hub page for the courselabs/simple-web image shows all the available tags, including the Windows and ARM64 variants.

To specify a Windows container in ACI, you'll need to add the --os-type parameter with a value of "Windows". You'll also want to use the appropriate Windows-tagged image, like simple-web:6.0-windows, and give it a unique DNS name. Keep in mind that for ARM64 images, Azure's x86 infrastructure might not support them directly - that's actually part of what you're exploring here.

**What to Observe**: Pay close attention to several key differences. Windows containers typically take significantly longer to start than Linux containers - sometimes several minutes compared to seconds. You'll also notice that Windows containers generally use more memory, often requiring at least 2GB to run comfortably. Compatibility is another interesting factor - not all container images work on all platforms, and you'll see this firsthand. And image size is dramatically different - Windows base images are significantly larger than their Linux counterparts, sometimes by several gigabytes.

**Questions to Explore**: As you work through this challenge, think about these questions: How does the Windows container startup time compare to Linux - is it seconds, minutes, or somewhere in between? What error message do you see when you try to run an ARM-based image on Azure's x86 infrastructure? Can you successfully access both Windows and Linux versions of the application in your browser? These real-world observations help you understand the tradeoffs between different container platforms.

---

## Exercise 5: Resource Management and Monitoring

Let's explore how to manage and monitor your running containers once they're deployed.

**Check Container State**: Using az container show with a query parameter, we can view the current state of a container - whether it's running, terminated, or in another state like waiting or transitioning. This gives you a quick snapshot of what your container is doing right now.

**Monitor Resource Usage**: While ACI doesn't provide real-time performance metrics via the CLI like you'd get with virtual machines, you can see the configured resource limits. Querying the resources.requests section shows you the CPU and memory allocation that was set when the container was created. This helps you understand the capacity you're paying for.

**Restart a Container**: Sometimes you need to restart a container - maybe it's stuck or you want to pick up environment variable changes. The az container restart command handles this for you, stopping and starting the container in place.

**Stop and Start**: Here's an important characteristic of ACI - you can't stop and start containers like you can with virtual machines. Instead, you delete and recreate them. This is the container paradigm at work - containers are ephemeral, designed to be thrown away and recreated rather than maintained as long-running resources.

**Update a Container**: To change configuration like CPU allocation, memory limits, or the image version, the process is straightforward: delete the existing container and create a new one with updated parameters. This might seem wasteful compared to modifying a VM in place, but it actually ensures you get a clean state and updated configuration without any residual issues from the previous deployment.

---

## Cleanup

This is important - ACI containers continue running and incurring charges until you explicitly delete them, so proper cleanup is essential.

**Delete with Docker Context**: If you're still in the labs-aci context, you can use docker rm with the force flag to remove containers by their container ID. This works just like local Docker cleanup.

**Switch Back to Local Context**: Don't forget to switch your Docker context back to default, otherwise your local docker commands will continue trying to talk to Azure instead of your local Docker Desktop.

**Delete Everything**: The cleanest approach is to remove the entire resource group using az group delete. The -y flag confirms the deletion without prompting, and the --no-wait flag returns immediately without waiting for the deletion to complete in the background. This removes the resource group and all containers within it at once.

**Remove Docker Context**: Clean up the ACI context from your Docker configuration using docker context rm. This removes the context definition so it doesn't clutter your context list.

**Verify Cleanup**: You can check that containers are gone by listing containers in the labs-aci resource group. This should return an error or empty list since the resource group has been deleted.

---

## Key Takeaways

Looking back at what we've covered - ACI is the simplest way to run containers in Azure with no infrastructure management required. You get multiple deployment methods including the Azure CLI, Portal, Docker CLI, and ARM templates, giving you flexibility in how you work. The Docker integration is particularly powerful, letting you use familiar commands while actually deploying to Azure in the cloud.

You have flexibility in what you run - both Linux and Windows containers are supported, with custom compute sizes ranging from small to large configurations. The networking options let you expose containers publicly or keep them private.

Understanding the container paradigm is crucial - treat containers as ephemeral resources that you recreate rather than modify in place. This is different from virtual machines, but it leads to cleaner, more reliable deployments.

And finally, cost awareness - remember to delete containers when you're done to avoid ongoing charges. Unlike some services that only charge when actively used, ACI charges for running time.

Excellent work! You now understand how to deploy and manage containers in Azure Container Instances.
