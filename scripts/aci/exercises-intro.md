# Azure Container Instances - Exercises Introduction

Now that we've covered what Azure Container Instances is and when to use it, let's put that knowledge into practice with hands-on exercises.

## What's Coming Up

In the exercises ahead, you'll get practical experience deploying and managing containers in Azure. We'll start by exploring the Azure Portal to see all the configuration options available for ACI - the basics like resource groups and container images, compute settings for CPU and memory allocation, networking configuration including DNS names and port exposure, and advanced options like restart policies and environment variables.

Then we'll move to the command line where you'll deploy real containers using the Azure CLI. You'll see how a single `az container create` command provisions infrastructure, pulls your image, and gets your application running in the cloud. We'll work with a simple web application, make it publicly accessible with a DNS name, and explore the container logs to see what's happening inside.

Next comes something really interesting - Docker CLI integration. If you're already comfortable with Docker commands, you'll love this. We'll authenticate the Docker CLI to Azure, create an ACI context, and then use standard `docker run` and `docker ps` commands - but instead of running locally, they'll be creating and managing containers in Azure. It's the same familiar Docker workflow, just running in the cloud.

You'll also tackle a challenge exercise exploring Windows containers versus Linux containers, comparing startup times, resource usage, and compatibility. And we'll cover practical resource management - checking container state, viewing logs, and the important concept that ACI containers are ephemeral resources you recreate rather than modify.

Let's get hands-on with Azure Container Instances!
