# Azure Container Registry - Exercise Walkthrough

## Exercise 1: Explore ACR in the Azure Portal

Let's start by getting familiar with Azure Container Registry options in the Portal.

**Navigate to the Portal**: We're opening the Azure Portal and searching for "Container Registry" to create a new resource. Before creating anything, let's explore the available options to understand what ACR offers.

**SKU Selection**: You'll see three SKU tiers available, and choosing the right one is important. The Basic tier is entry-level for development and testing, with limited storage and throughput - it's perfect for learning and small projects. The Standard tier is production-ready with more storage and higher throughput, suitable for most production workloads. The Premium tier unlocks advanced features including geo-replication, private endpoints, and customer-managed encryption - this is what you need for enterprise deployments with high security requirements.

**Key Configuration Points**: The registry name becomes your DNS name with the .azurecr.io suffix automatically appended, which is why it must be globally unique across all of Azure - no two registries anywhere can have the same name. The Premium SKU unlocks private networking through private endpoints and customer-managed encryption keys for additional security. You can choose the Azure region where your registry will be hosted, and it's generally best to choose a region close to where your containers will run.

After exploring the Portal, we'll switch to the command line to create our registry with the Azure CLI - this approach is much more suitable for automation and repeatability.

---

## Exercise 2: Create an ACR Instance with the CLI

**Create a Resource Group**: Every Azure resource needs a home, so we're starting by creating a resource group for this lab. We're calling it "labs-acr" and placing it in the East US region. The tags parameter helps you track resources created for this course - this is a best practice for organizing and managing resources, especially when you have multiple projects or labs running.

**Find the Create Command**: Let's explore what options are available for creating a registry by running az acr create with the help flag. The CLI offers many more configuration options than what you see in the Portal's initial creation screen - things like network rules, retention policies, and encryption settings. Some of these can be configured later in the management pages, but it's good to know they exist.

**Create Your Registry**: We're creating a Basic SKU registry for this lab. The command specifies our resource group, location, SKU tier, and most importantly, the registry name. Remember to choose a unique name - something like "acrlab" followed by your initials or a random number works well.

**Naming Rules**: If you see an error, check that your registry name contains only lowercase letters and numbers, is between 5 and 50 characters, and is globally unique across Azure. The name cannot include hyphens or special characters - this is different from most other Azure resources.

**Verify Creation**: When the command completes, you'll see JSON output containing all the registry details. Look for the loginServer field - this is your full registry domain name, something like your-acr-name.azurecr.io. This is what you'll use when tagging and pushing images.

---

## Exercise 3: Pull and Push Images to ACR

**Understanding Image Names**: Docker image names can include a registry domain, and understanding how this works is crucial. For example, the short name "nginx:alpine" is actually interpreted as "docker.io/nginx:alpine" - when no domain is specified, Docker defaults to Docker Hub at docker.io. You can see this full name when you pull images.

**Pull an Image from Docker Hub**: We're downloading the Nginx Alpine image from Docker Hub using docker image pull. This downloads the latest version of the nginx:alpine image, which is a lightweight web server based on Alpine Linux. The pull process downloads all the image layers that make up this container.

**Tag the Image for ACR**: To push an image to ACR, it needs to have your ACR domain in its name. We're using the tag command to create a new reference. The tag includes your registry name, a repository path like "labs-acr/nginx", and a tag like "alpine-2204". This doesn't copy the image - it just creates another tag pointing to the same image data, like creating a shortcut or alias.

**View Your Tagged Images**: We're listing both the original and ACR-tagged versions using filters to show only nginx images. You'll see both tags with the same image ID because tags are like aliases - one image can have many tags, and they all point to the same underlying layers.

**Attempt to Push (Will Fail)**: Let's try pushing the image without authentication to see what happens. The push fails with an authentication error because ACR requires authentication for all push operations - you cannot push images anonymously to a private registry.

**Authenticate to ACR**: We're using the Azure CLI to log in to your registry with az acr login. This command configures Docker to use your Azure credentials for this registry. Behind the scenes, it obtains an access token from Azure Active Directory and stores it in your Docker configuration. The token is valid for a few hours before needing renewal.

**Push the Image Successfully**: Now we're pushing the image to your ACR and you'll see the layers being pushed. If a layer already exists in the registry, Docker skips it - this is Docker's efficient layer caching at work. The push might be quick if you've pushed similar images before.

**Run a Container from ACR**: You can now run containers from your registry using docker run. We're running in detached mode, mapping port 8080 on your machine to container port 80, and specifying the full ACR image name. Anyone with access to your ACR can run this same application, making it a great way to distribute containerized applications within your organization.

We're browsing to localhost:8080 to see the Nginx welcome page. The container is running from your private registry, demonstrating the full cycle of tagging, pushing, and running.

---

## Exercise 4: Build and Push a Custom Image

**Build with ACR Tag**: When building images, you can include the registry domain directly in the tag to save a step later. We're building the simple ASP.NET web application with docker build, tagging it with your ACR domain, repository path "labs-acr/simple-web", and version "6.0". The build should be quick if you've built this image before, thanks to Docker's layer caching that reuses unchanged layers.

**Create an Additional Tag**: We're creating a second tag for the same image using "latest" as the version. The "latest" tag is a convention in Docker - it's not automatically updated, it's just another tag that you can assign to whatever version you consider current. Many teams tag each build with both a specific version and "latest" for convenience.

**List Your ACR Images**: We're viewing all images tagged with your ACR domain using a wildcard pattern. You'll see both the 6.0 and latest tags for your simple-web image, plus the nginx image from earlier. Notice they appear as separate entries but the simple-web tags share the same image ID.

**Push Multiple Tags**: We're pushing all versions of the simple-web image with one command using the all-tags flag. This pushes both the 6.0 and latest tags to your registry efficiently. Docker is smart about this - it only uploads the layers once even though you're pushing two tags.

---

## Exercise 5: Browse ACR in the Portal

ACR provides a rich management experience in the Azure Portal that goes beyond what the CLI offers.

**Navigate to Your Registry**: We're opening the Azure Portal and finding your Container Registry resource in the labs-acr resource group.

**Explore Repositories**: Opening the Repositories section shows your container images organized by name. You'll see labs-acr/nginx with one image and one tag, and labs-acr/simple-web with one image but two tags - 6.0 and latest. This demonstrates how the repository view organizes images.

**Understanding Repository Views**: It's important to understand the hierarchy here. Repositories are collections of related images, like "simple-web" representing all versions of that application. Tags are specific versions within a repository, like "6.0" or "latest" representing different releases. Manifests are the actual image content, containing the configuration and layer information. Multiple tags can point to the same manifest when they represent the same image build - this is exactly what we did with 6.0 and latest.

**Explore Other Features**: Take a look at other ACR capabilities in the Portal. Webhooks let you trigger automation when images are pushed or deleted - useful for CI/CD pipelines that need to deploy when new images arrive. Replications allow you to geo-replicate your registry to multiple regions, but this requires the Premium SKU. Networking options let you configure private endpoints and firewall rules to restrict access to your registry. Encryption settings show customer-managed key configuration, also a Premium SKU feature.

---

## Lab Challenge: Image Cleanup Script

**The Scenario**: In a real CI/CD environment, you might push new images to ACR with every code change, every pull request, or every commit to certain branches. Over time, this can result in hundreds or thousands of image versions accumulating in your registry. Each version consumes storage, and Azure charges you for that storage, so keeping old versions indefinitely increases your costs unnecessarily.

**Your Task**: Look at the az acr commands for deleting images and repositories - you can find these by running az acr repository delete with the help flag. If you're comfortable with scripting in bash or PowerShell, try to write a script that lists all tags for a specific repository, sorts them by creation date, keeps only the 5 most recent versions, and deletes all older versions.

**Hints**: The az acr repository commands have options for listing and deleting tags - explore az acr repository show-tags and az acr repository delete. You can output results in JSON format with the output json flag for easier parsing in scripts. The jq command-line tool is helpful for parsing JSON in bash scripts - it lets you filter, sort, and extract values. Consider using query parameters to extract just the data you need, like creation dates and tag names.

**Note**: Be careful when testing deletion commands! Test your logic on repositories you don't need first, or use a test registry. There's no undo for deletions - once an image is deleted from ACR, it's gone permanently.

---

## Cleanup

**Delete Azure Resources**: We're removing the resource group and all its contents using az group delete. The yes flag confirms the deletion without prompting, and the no-wait flag returns immediately without waiting for the deletion to complete. The deletion happens in the background, which is useful when cleaning up large resource groups.

**Clean Up Local Containers**: We're removing all Docker containers from your local machine using docker rm with the force flag to stop and remove running containers. The dollar-parentheses syntax runs docker ps with the all-quiet flags to get all container IDs, which are then passed to the remove command.

**Optional - Clean Up Local Images**: If you want to free up disk space, you can also remove the images we created. You can delete them individually by specifying each image name, or remove all unused images at once using docker image prune with the all flag. The prune command removes all images that aren't currently being used by any container, which is a quick way to reclaim disk space.

This cleanup is important - while the local containers and images don't cost money, the ACR instance does continue to incur charges until the resource group is deleted.
