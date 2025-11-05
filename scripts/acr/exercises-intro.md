# Azure Container Registry - Exercises Introduction

Now that we understand what Azure Container Registry is and why you need a private registry for production applications, let's get hands-on with creating and managing your own registry.

## What You'll Do

First, you'll **explore ACR in the Azure Portal** to understand the three SKU tiers - Basic for development, Standard for production, and Premium for enterprise deployments with geo-replication and private networking. You'll see how registry names become DNS hostnames and why they must be globally unique.

Then we'll **create an ACR instance using the Azure CLI**. You'll learn the proper naming rules - only lowercase letters and numbers, 5-50 characters, globally unique. The CLI offers many more configuration options than the Portal's initial creation screen, and you'll see how to explore these with the help flag.

Next comes the core skill: **pulling images from Docker Hub and pushing them to your private registry**. You'll pull the Nginx Alpine image, tag it with your ACR domain name, and attempt to push it. The first attempt will fail with an authentication error, teaching you an important security principle - ACR requires authentication for all push operations. You'll then use `az acr login` to authenticate Docker with your Azure credentials and successfully push the image. Finally, you'll run a container from your private registry, demonstrating the full cycle.

You'll also **build a custom application image**, tag it with both a version number and "latest", and push both tags to ACR. You'll see how Docker's layer caching makes this efficient - multiple tags can point to the same image data.

In the Portal, you'll **browse your ACR repositories** to see the visual organization of images, tags, and manifests. You'll explore webhooks for CI/CD automation, geo-replication settings, networking options, and encryption features.

The challenge exercise has you thinking about real-world scenarios: in a CI/CD environment where you push images frequently, how do you clean up old versions to manage storage costs? You'll explore the CLI commands for deleting images and potentially write a retention script.

Let's build and manage your private container registry!
