# Azure Container Registry - Exercise Walkthrough

## Exercise 1: Explore ACR in the Azure Portal

Let's start by getting familiar with Azure Container Registry options in the Portal.

**Navigate to the Portal:**
Open the Azure Portal and search for "Container Registry" to create a new resource. Before creating anything, explore the available options.

**SKU Selection:**
You'll see three SKU tiers available:
- **Basic** - Entry-level for development and testing, with limited storage and throughput
- **Standard** - Production-ready with more storage and higher throughput
- **Premium** - Advanced features including geo-replication, private endpoints, and customer-managed encryption

**Key Configuration Points:**
- The registry name becomes your DNS name with the `.azurecr.io` suffix
- The name must be globally unique across all of Azure
- Premium SKU unlocks private networking and customer-managed encryption keys
- You can choose the Azure region where your registry will be hosted

After exploring the Portal, we'll switch to the command line to create our registry with the Azure CLI.

---

## Exercise 2: Create an ACR Instance with the CLI

**Create a Resource Group:**
First, create a dedicated resource group for this lab. We're using eastus as the region:

```bash
az group create -n labs-acr --tags courselabs=azure -l eastus
```

The `--tags` parameter helps you track resources created for this course.

**Find the Create Command:**
Let's explore what options are available for creating a registry:

```bash
az acr create --help
```

The CLI offers many more configuration options than what you see in the Portal's initial creation screen. Some of these can be configured later in the management pages.

**Create Your Registry:**
Create a Basic SKU registry. Remember to choose a unique name:

```bash
az acr create -g labs-acr -l eastus --sku 'Basic' -n <your-unique-acr-name>
```

**Naming Rules:**
If you see an error, check that your registry name:
- Contains only lowercase letters and numbers
- Is between 5 and 50 characters
- Is globally unique

**Verify Creation:**
When the command completes, you'll see JSON output. Look for the `loginServer` field - this is your full registry domain name: `<your-acr-name>.azurecr.io`

---

## Exercise 3: Pull and Push Images to ACR

**Understanding Image Names:**
Docker image names can include a registry domain. For example:
- Short name: `nginx:alpine`
- Full name: `docker.io/nginx:alpine`

When no domain is specified, Docker defaults to Docker Hub (`docker.io`).

**Pull an Image from Docker Hub:**
Download the Nginx Alpine image:

```bash
docker image pull docker.io/nginx:alpine
```

This downloads the latest version of the nginx:alpine image from Docker Hub.

**Tag the Image for ACR:**
To push an image to ACR, it needs to have your ACR domain in its name. Use the `tag` command to create a new reference:

```bash
docker image tag docker.io/nginx:alpine <your-acr-name>.azurecr.io/labs-acr/nginx:alpine-2204
```

This doesn't copy the image - it just creates another tag pointing to the same image data.

**View Your Tagged Images:**
List both the original and ACR-tagged versions:

```bash
docker image ls --filter reference=nginx --filter reference=*/labs-acr/nginx
```

You'll see both tags with the same image ID. Tags are like aliases - one image can have many tags.

**Attempt to Push (Will Fail):**
Try pushing the image without authentication:

```bash
docker image push <your-acr-name>.azurecr.io/labs-acr/nginx:alpine-2204
```

This fails because you haven't authenticated to your registry yet.

**Authenticate to ACR:**
Use the Azure CLI to log in to your registry:

```bash
az acr login -n <your-acr-name>
```

This command configures Docker to use your Azure credentials for this registry.

**Push the Image Successfully:**
Now push the image to your ACR:

```bash
docker image push <your-acr-name>.azurecr.io/labs-acr/nginx:alpine-2204
```

The image uploads to your private registry. You'll see the layers being pushed.

**Run a Container from ACR:**
You can now run containers from your registry:

```bash
docker run -d -p 8080:80 <your-acr-name>.azurecr.io/labs-acr/nginx:alpine-2204
```

Browse to http://localhost:8080 to see the Nginx welcome page. Anyone with access to your ACR can run this same application.

---

## Exercise 4: Build and Push a Custom Image

**Build with ACR Tag:**
When building images, you can include the registry domain directly in the tag. Build the simple ASP.NET web application:

```bash
docker build -t <your-acr-name>.azurecr.io/labs-acr/simple-web:6.0 src/simple-web
```

The build should be quick if you've built this image before, thanks to Docker's caching.

**Create an Additional Tag:**
Create a second tag for the same image using "latest" as the version:

```bash
docker tag <your-acr-name>.azurecr.io/labs-acr/simple-web:6.0 <your-acr-name>.azurecr.io/labs-acr/simple-web:latest
```

**List Your ACR Images:**
View all images tagged with your ACR domain:

```bash
docker image ls <your-acr-name>.azurecr.io/*/*
```

You'll see both the `6.0` and `latest` tags for your simple-web image, plus the nginx image from earlier.

**Push Multiple Tags:**
Push all versions of the simple-web image with one command:

```bash
docker push --all-tags <your-acr-name>.azurecr.io/labs-acr/simple-web
```

This pushes both the `6.0` and `latest` tags to your registry.

---

## Exercise 5: Browse ACR in the Portal

ACR provides a rich management experience in the Azure Portal.

**Navigate to Your Registry:**
Open the Azure Portal and find your Container Registry resource.

**Explore Repositories:**
Open the "Repositories" section. You'll see:
- `labs-acr/nginx` - One image with one tag
- `labs-acr/simple-web` - One image with two tags (6.0 and latest)

**Understanding Repository Views:**
- **Repositories** - Collections of related images (like "simple-web")
- **Tags** - Specific versions (like "6.0" or "latest")
- **Manifests** - The actual image content (layers and configuration)

Multiple tags can point to the same manifest when they represent the same image build.

**Explore Other Features:**
Take a look at other ACR capabilities:
- **Webhooks** - Trigger automation when images are pushed or deleted
- **Replications** - Geo-replicate your registry (Premium SKU only)
- **Networking** - Configure private endpoints and firewall rules
- **Encryption** - View customer-managed key settings (Premium SKU)

---

## Lab Challenge: Image Cleanup Script

**The Scenario:**
In a real CI/CD environment, you might push new images to ACR with every code change. Over time, this can result in hundreds or thousands of image versions, increasing your storage costs.

**Your Task:**
Look at the `az acr` commands for deleting images and repositories. If you're comfortable with scripting, try to write a script that:
1. Lists all tags for a specific repository
2. Sorts them by creation date
3. Keeps only the 5 most recent versions
4. Deletes all older versions

**Hints:**
- The `az acr repository` commands have options for listing and deleting tags
- You can output in JSON format with the `--output json` flag for easier parsing
- The `jq` command-line tool is helpful for parsing JSON in bash scripts
- Consider the `az acr repository show-tags` and `az acr repository delete` commands

**Note:** Be careful when testing deletion commands! Consider using the `--dry-run` flag if available, or test on repositories you don't need.

---

## Cleanup

**Delete Azure Resources:**
Remove the resource group and all its contents:

```bash
az group delete -y --no-wait -n labs-acr
```

The `--no-wait` flag returns immediately without waiting for the deletion to complete.

**Clean Up Local Containers:**
Remove all Docker containers from your local machine:

```bash
docker rm -f $(docker ps -aq)
```

This force-removes all containers, both running and stopped.

**Optional - Clean Up Local Images:**
If you want to free up disk space, you can also remove the images:

```bash
docker image rm <your-acr-name>.azurecr.io/labs-acr/nginx:alpine-2204
docker image rm <your-acr-name>.azurecr.io/labs-acr/simple-web:6.0
docker image rm <your-acr-name>.azurecr.io/labs-acr/simple-web:latest
docker image rm docker.io/nginx:alpine
```

Or remove all unused images at once:

```bash
docker image prune -a
```
