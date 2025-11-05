# Azure Container Apps

Azure Container Apps is a fully managed serverless container platform that enables you to run containerized applications without managing complex infrastructure. It's built on top of Kubernetes but abstracts away the complexity, providing a simple developer experience similar to Azure Functions but with full container flexibility.

Container Apps sits between Azure Container Instances (simple, single containers) and Azure Kubernetes Service (full Kubernetes control), offering the best balance of simplicity and features for most modern cloud-native applications.

## Reference

- [Container Apps overview](https://docs.microsoft.com/en-us/azure/container-apps/overview)

- [Container Apps concepts](https://docs.microsoft.com/en-us/azure/container-apps/concepts)

- [`az containerapp` commands](https://docs.microsoft.com/en-us/cli/azure/containerapp?view=azure-cli-latest)

## Container Apps vs ACI vs AKS

| Feature | Container Apps | Container Instances | Kubernetes Service |
|---------|----------------|---------------------|-------------------|
| **Complexity** | Low | Very Low | High |
| **Serverless** | Yes | Yes | No |
| **Auto-scaling** | Yes (HTTP, CPU, custom) | No | Manual setup |
| **Multiple containers** | Yes (in app) | Yes (container group) | Yes (pods) |
| **Ingress/Load Balancing** | Built-in | Manual | Manual setup |
| **Dapr integration** | Built-in | No | Manual |
| **Revisions** | Built-in | No | Manual |
| **Use Case** | Microservices, APIs, web apps | Batch jobs, simple containers | Complex orchestration |

## Create a Container Apps Environment

Container Apps run in a Container Apps Environment, which is a secure boundary around a group of container apps that share the same virtual network and write logs to the same Log Analytics workspace.

```bash
az group create -n labs-container-apps --tags courselabs=azure -l eastus

# Create Container Apps environment
az containerapp env create \
  -g labs-container-apps \
  -n my-container-env \
  -l eastus
```

> Creating an environment takes a few minutes as it provisions the underlying infrastructure.

## Deploy Your First Container App

Let's deploy a simple web application from a public container image:

```bash
az containerapp create \
  -g labs-container-apps \
  -n simple-web-app \
  --environment my-container-env \
  --image mcr.microsoft.com/azuredocs/containerapps-helloworld:latest \
  --target-port 80 \
  --ingress external \
  --query properties.configuration.ingress.fqdn
```

The output shows the FQDN (fully qualified domain name) for your app. Browse to that URL and you'll see the hello world application running!

## Scaling Configuration

Container Apps automatically scale based on HTTP traffic, CPU, memory, or custom metrics:

```bash
# Configure HTTP scaling (scale based on concurrent requests)
az containerapp update \
  -g labs-container-apps \
  -n simple-web-app \
  --min-replicas 1 \
  --max-replicas 10 \
  --scale-rule-name http-rule \
  --scale-rule-type http \
  --scale-rule-http-concurrency 50
```

This configuration means:
- Minimum 1 replica always running
- Maximum 10 replicas
- Scale up when concurrent requests exceed 50 per replica

📋 Test the scaling by generating load to your application and observing the replica count.

<details>
  <summary>Not sure how?</summary>

```bash
# Get the app URL
APP_URL=$(az containerapp show \
  -g labs-container-apps \
  -n simple-web-app \
  --query properties.configuration.ingress.fqdn -o tsv)

# Generate load using Apache Bench (if installed) or curl in a loop
for i in {1..1000}; do
  curl -s "https://$APP_URL" > /dev/null &
done

# Check replica count
az containerapp replica list \
  -g labs-container-apps \
  -n simple-web-app \
  -o table
```

</details><br/>

## Using Custom Container Images

You can deploy your own containerized applications. First, build and push a container image to a registry:

```bash
# Create Azure Container Registry
az acr create \
  -g labs-container-apps \
  -n <acr-name> \
  --sku Basic \
  --admin-enabled true

# Get ACR credentials
ACR_USERNAME=$(az acr credential show -n <acr-name> --query username -o tsv)
ACR_PASSWORD=$(az acr credential show -n <acr-name> --query passwords[0].value -o tsv)

# Build and push an image (if you have a Dockerfile)
az acr build \
  -r <acr-name> \
  -t myapp:v1 \
  .

# Create Container App with ACR image
az containerapp create \
  -g labs-container-apps \
  -n my-custom-app \
  --environment my-container-env \
  --image <acr-name>.azurecr.io/myapp:v1 \
  --registry-server <acr-name>.azurecr.io \
  --registry-username $ACR_USERNAME \
  --registry-password $ACR_PASSWORD \
  --target-port 80 \
  --ingress external
```

## Revisions and Traffic Splitting

One of the most powerful features of Container Apps is built-in revisions and traffic splitting:

```bash
# Create a new revision with updated image
az containerapp update \
  -g labs-container-apps \
  -n my-custom-app \
  --image <acr-name>.azurecr.io/myapp:v2 \
  --revision-suffix v2

# List all revisions
az containerapp revision list \
  -g labs-container-apps \
  -n my-custom-app \
  -o table

# Split traffic: 80% to v1, 20% to v2
az containerapp ingress traffic set \
  -g labs-container-apps \
  -n my-custom-app \
  --revision-weight my-custom-app--v1=80 my-custom-app--v2=20
```

This enables:
- **Blue-green deployments**: Switch traffic between versions instantly
- **Canary releases**: Gradually increase traffic to new version
- **A/B testing**: Split traffic to test different versions

## Environment Variables and Secrets

```bash
# Set environment variables
az containerapp update \
  -g labs-container-apps \
  -n my-custom-app \
  --set-env-vars \
    "API_URL=https://api.example.com" \
    "LOG_LEVEL=info"

# Add secrets
az containerapp secret set \
  -g labs-container-apps \
  -n my-custom-app \
  --secrets "api-key=super-secret-key-12345"

# Reference secret in environment variable
az containerapp update \
  -g labs-container-apps \
  -n my-custom-app \
  --set-env-vars "API_KEY=secretref:api-key"
```

## Lab

Container Apps can scale to zero replicas when there's no traffic, reducing costs. Configure your app to:

- Scale to 0 minimum replicas
- Scale up based on HTTP requests
- Set a maximum of 5 replicas

After configuring, wait for the app to scale to zero (no traffic), then send a request and observe the cold start behavior. How does this compare to Azure Functions consumption plan?

> Stuck? Try [hints](hints.md) or check the [solution](solution.md).

___

## Cleanup

Delete the lab resources:

```bash
az group delete -y --no-wait -n labs-container-apps
```
