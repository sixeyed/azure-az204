# AKS Apps with Secure Networking - Exercises Introduction

We've covered the concepts of securing AKS applications using Azure networking and managed identities. Now let's implement a production-ready security pattern with defense-in-depth protection.

## What You'll Do

You'll start by **creating a virtual network with a dedicated AKS subnet**. This subnet will be the foundation for implementing service endpoints that restrict access to Azure resources. You'll then **deploy an AKS cluster using Azure CNI networking**, which gives each pod its own IP address from the VNet - this is required for service endpoint integration.

Next, you'll **set up a Storage Account and Key Vault** for the application to use. The Asset Manager application stores data in Blob Storage, but the connection string is too sensitive to put directly in the deployment YAML. Instead, you'll store it in Key Vault.

The key security implementation involves **configuring service endpoints on the AKS subnet**, which creates a secure, private path between the subnet and Azure services. You'll then **add network rules to Key Vault** that restrict access to only requests coming from the AKS subnet. This means even if someone steals your credentials, they can't access Key Vault from outside Azure.

You'll **grant the AKS managed identity access to Key Vault** using access policies, enabling credential-free authentication. The application will use the **KeyVault Secrets Provider CSI driver** to mount secrets directly into the container filesystem - the application reads the connection string from a file, never needing to know about Key Vault or authentication.

Finally, you'll **deploy the application** and verify it can access both Key Vault and Storage Account. The **lab challenge** extends the network restrictions to the Storage Account as well, completing the security perimeter.

Let's build a production-ready, secure AKS application!
