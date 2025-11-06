# Securing AKS Apps with Key Vault and Virtual Networks - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on securing Azure Kubernetes Service applications with Key Vault and Virtual Networks. Today we're diving deep into production-grade security patterns for containerized applications running in Azure. If you've been deploying applications to AKS and wondering how to properly secure sensitive credentials and restrict access to resources, this episode will show you the defense-in-depth approach that Azure enables. This is essential knowledge for both the AZ-204 certification and real-world production deployments.

## The Security Challenge

When running applications in Kubernetes, security should be a primary concern. Your applications inevitably need to access sensitive resources - databases, storage accounts, external APIs - and they need credentials to authenticate to these services. The question is: how do you manage these credentials securely?

The naive approach stores connection strings in environment variables or configuration files deployed with your application. This is problematic because anyone with access to your Kubernetes cluster can read these values. They appear in Pod specifications, are visible through kubectl describe commands, and potentially get logged or exposed through various monitoring tools.

A better approach uses Azure Key Vault to store secrets centrally with proper access control. But even this raises questions: how does your application authenticate to Key Vault? How do you prevent unauthorized access to the vault itself? And how do you ensure that even if someone compromises your application, they can't access resources directly?

Today's episode addresses all these concerns through a comprehensive security pattern combining managed identities, Key Vault integration, and virtual network restrictions.

## Azure CNI Networking for AKS

Let's start with networking, because it's foundational to everything else we'll discuss. By default, AKS can use kubenet networking where Pods get IP addresses from a private address space managed by Kubernetes. This works, but Pods aren't directly addressable from your Azure virtual network.

Azure Container Network Interface, or Azure CNI, changes this model fundamentally. When you deploy an AKS cluster with Azure CNI, each Pod gets an IP address directly from your VNet subnet. They're first-class citizens in your Azure network infrastructure.

Why does this matter? Because now Azure services can identify where traffic is coming from. When a Pod connects to Key Vault or Storage, these services see the connection originating from your VNet subnet. This enables service endpoints and firewall rules that restrict access based on network location.

The trade-off is IP address consumption. If you plan to run hundreds of Pods, your subnet needs hundreds of available IP addresses. You need to plan your address space carefully when designing your VNet. A /24 subnet provides 256 addresses, /23 provides 512, and so on. Consider your maximum expected Pod count when sizing subnets.

For the AZ-204 exam, understand that Azure CNI is the network plugin that enables this VNet integration. Questions may present scenarios requiring Pod-level network access to Azure services or VNet restrictions - Azure CNI is the enabling technology.

## Service Endpoints

Service endpoints are a key Azure networking feature that enables our security pattern. Many Azure services - including Key Vault and Storage Accounts - support service endpoints. When you enable a service endpoint on a subnet for a particular service, you're doing two things.

First, you're optimizing the network path. Traffic from your subnet to that Azure service stays on the Microsoft backbone network instead of traversing the public internet. This improves performance and security.

Second, you're enabling the Azure service to identify traffic from your subnet. The service can now create firewall rules that allow connections from specific subnets while denying everything else. This is the key to our security pattern.

Think of it this way: your Key Vault is still technically accessible via a public endpoint on the internet. But with service endpoints and firewall rules configured, it rejects all connections except those coming from your authorized subnet. Even if someone has valid credentials, they can't access the vault from their laptop or a compromised server elsewhere - only from your AKS cluster.

The commands to enable service endpoints are straightforward. You update your subnet to enable endpoints for specific Azure services, like Microsoft.KeyVault and Microsoft.Storage. Then you configure the target services to allow your subnet and deny all other traffic.

For the exam, understand the difference between service endpoints and private endpoints. Service endpoints keep the public endpoint active but add subnet-based filtering. Private endpoints give you a private IP address for the service inside your VNet. Service endpoints are simpler and often sufficient; private endpoints provide deeper network isolation.

## Managed Identities for Authentication

Authentication is where managed identities shine. We've discussed managed identities in previous episodes, but their application in AKS deserves special attention.

When you enable the AKS KeyVault Secrets Provider add-on, it creates a user-assigned managed identity. This identity is what your Pods use to authenticate to Key Vault. The critical point is that your application code never handles credentials. The identity is managed by Azure, authentication tokens are obtained automatically, and credentials are rotated behind the scenes.

This solves a classic security problem: how do you secure the credentials used to retrieve other credentials? With managed identities, there are no credentials to secure at that level. Azure handles the entire authentication flow using cryptographic identities and certificates managed at the platform level.

The workflow is elegant: the CSI driver running in your cluster uses the managed identity to authenticate to Key Vault, retrieves secret values, and mounts them into your Pod's filesystem. Your application reads secrets from mounted files just like reading any other file. The application doesn't know or care that these values came from Key Vault - it's completely transparent.

For the exam, know that managed identities come in two flavors: system-assigned and user-assigned. System-assigned identities are tied to the lifecycle of a resource - when you delete the resource, the identity is deleted. User-assigned identities exist independently and can be assigned to multiple resources. The AKS KeyVault add-on uses a user-assigned identity because it needs to exist across Pod lifecycles.

## Storing Secrets in Key Vault

The actual secret storage process is straightforward but worth understanding in detail. You create a Key Vault instance, and you store secrets using the Azure CLI or SDK. Secrets can be simple strings or entire files - when you use the file parameter, the file contents become the secret value.

For structured data like JSON configuration files, this is perfect. Your application can retrieve the secret value and parse it as JSON. The structure is preserved, and you can store complex configurations as single secrets.

Key Vault provides several important features beyond simple storage. Version history tracks changes to secrets over time. Access policies control who can read, write, or manage secrets. Activity logs track all access for audit purposes. And Key Vault integrates with Azure Monitor for alerts and compliance reporting.

For the exam, know the difference between access policies and RBAC for Key Vault. Access policies are Key Vault's traditional authorization model, granting permissions to specific identities for operations on secrets, keys, and certificates. RBAC is the newer, more consistent authorization model that aligns with Azure's overall permissions system. Both work; RBAC is generally preferred for new deployments but access policies remain widely used.

## Network Restrictions on Key Vault

Here's where our security model comes together. After creating and populating Key Vault, we apply network restrictions. The process involves three steps.

First, enable service endpoints for Key Vault on your AKS subnet. This was already done when we created the networking infrastructure.

Second, add a network rule to Key Vault allowing your subnet. This creates an allow-list entry saying "accept connections from this specific subnet."

Third - and this is crucial - change the Key Vault's default action from Allow to Deny. This flips the security model. Instead of "allow everything except blocked sources," it becomes "deny everything except allowed sources." Only traffic from your explicitly permitted subnet can access the vault.

The practical effect is dramatic. You can no longer access Key Vault from the Azure Portal, from your local machine, or from Azure CLI commands running outside the subnet. Attempts to read secrets return access denied errors. The only way to access secrets is through the AKS managed identity from Pods running in your cluster.

This is defense in depth. Even if someone compromises your subscription credentials, they can't access Key Vault secrets without also gaining access to your AKS cluster. And even if they access the cluster, they need the managed identity's permissions. Multiple security layers protect your secrets.

For the exam, understand this pattern thoroughly. Questions often present scenarios like "prevent internet access to Key Vault" or "restrict Key Vault to specific resources." The solution involves service endpoints, network rules, and changing the default action to Deny.

## The KeyVault Secrets Provider

The KeyVault Secrets Provider is a Kubernetes component that integrates Key Vault with Pods. It's implemented as a Container Storage Interface driver, which is Kubernetes' standard plugin architecture for storage systems.

When you deploy a Pod that references a SecretProviderClass, the CSI driver springs into action. It uses the specified managed identity to authenticate to the specified Key Vault, retrieves the requested secrets, and mounts them as files in your container's filesystem.

From your application's perspective, secrets appear as regular files in a directory you specify. You read them like any other file. The application doesn't need Azure SDK dependencies or Key Vault-specific code - just standard file I/O.

This is better than environment variables for several reasons. Secrets aren't visible in Pod specifications or kubectl describe output. They don't appear in process listings. And they can be larger than environment variables typically allow, enabling complex configuration files.

The SecretProviderClass resource is where you configure this integration. You specify the Key Vault name, the tenant ID, the managed identity client ID, and which secrets to retrieve. You can map secrets to specific files and control permissions.

For the exam, understand that the SecretProviderClass is the Kubernetes resource that configures Key Vault integration. Questions may show YAML and ask what values need to be filled in, or present scenarios requiring secret access and ask how to configure it.

## Extending Protection to Storage

The same network restriction pattern applies to Azure Storage. Your application uses a storage connection string to access Blob Storage. That connection string contains credentials that grant full access to the storage account.

Storing the connection string in Key Vault protects it from casual exposure, but someone with the connection string could still access storage directly from anywhere. To prevent this, you apply storage account firewall rules.

The process mirrors what we did with Key Vault. Service endpoints for Storage were already enabled on the subnet. You add network rules to the storage account allowing your subnet. You change the default action to Deny. Now only traffic from your AKS Pods can access the storage account.

This completes the security perimeter. Key Vault is restricted to the subnet. Storage is restricted to the subnet. Application access flows through your AKS cluster, which sits inside the secured subnet. Even if credentials leak, they can't be used from outside the authorized network.

One consideration: this makes troubleshooting more complex. You can't browse storage in the Azure Portal or upload test files from your local machine. You need to either temporarily modify firewall rules or work through the cluster for all storage operations. For production systems, this added security is worth the operational complexity.

For the exam, expect scenarios asking how to secure storage accounts or prevent unauthorized access. The answer involves the same service endpoint and network rule pattern we've discussed.

## Real-World Application Design

Let's connect these security measures to application architecture. In production systems, you typically have multiple environments - development, staging, production. Each environment has its own Key Vault, storage account, and AKS cluster.

Development environments might have relaxed security for convenience. Key Vaults might be internet-accessible for local development. Storage accounts might allow public access. This enables developers to work efficiently.

As you promote code toward production, security tightens. Staging environments enforce network restrictions but might allow access from specific office IP addresses. Production environments have the strictest controls - service endpoints, network rules, default deny actions, and comprehensive audit logging.

The code remains the same across environments. Configuration injected through Key Vault changes - connection strings point to different storage accounts, API endpoints reference different services, feature flags enable or disable functionality. But the application logic is consistent.

This separation of code and configuration is a cloud-native best practice. It enables the same container image to run in multiple environments securely. For the exam, this pattern appears in questions about deploying applications across environments or managing configuration.

## Common Exam Scenarios

Let me walk through exam question patterns related to this topic.

**Scenario: Key Vault access from AKS** - An application needs to retrieve database connection strings from Key Vault. What's the most secure authentication method? The answer is: use a managed identity granted Key Vault access policies or RBAC permissions. This avoids storing any credentials.

**Scenario: Preventing internet access** - Compliance requires that Key Vault not be accessible from the internet. What should you configure? The answer is: enable service endpoints on the subnet, add network rules allowing the subnet, and set the default action to Deny. This restricts access to specific network locations.

**Scenario: Mounting secrets into containers** - How should containers running in AKS access Key Vault secrets? The answer is: use the KeyVault Secrets Provider with a SecretProviderClass that mounts secrets as volumes. This provides transparent access without SDK dependencies.

**Scenario: Storage account security** - Your application uses Blob Storage with connection string authentication. How do you prevent unauthorized access even if the connection string leaks? The answer is: configure storage account firewall rules allowing only your AKS subnet, preventing connections from other locations.

## Integration with Application Code

While this episode focuses on configuration and infrastructure, it's worth mentioning how application code interacts with this setup. With secrets mounted as files, code typically reads them at startup.

For ASP.NET Core applications, you can use the configuration system to load JSON files from specific paths. The mounted Key Vault secret becomes a configuration source. For Node.js applications, you read the file synchronously at startup and parse the JSON. For Python applications, you use the json module to load the file.

The key point is simplicity. No Azure SDK dependencies for Key Vault. No authentication code. Just file I/O that works the same in all environments. This makes testing easier - in local development, you can mount a file with test configuration, and the code behaves identically.

For the exam, you might encounter code samples that access secrets. Look for the Azure SDK approach with managed identity authentication, or the file-based approach we've discussed. Both are valid; the file-based approach through mounted secrets is simpler for containerized applications.

## Study Recommendations

To prepare for exam questions on this topic, practice the complete workflow hands-on. Create AKS clusters with Azure CNI. Configure service endpoints and network rules. Grant managed identity access to Key Vault. Deploy applications that consume mounted secrets.

Understand the YAML structure for SecretProviderClass. Know what fields are required and where to find the values you need - Key Vault name, tenant ID, identity client ID, secret names.

Practice with the Azure CLI commands for network configuration. Know how to enable service endpoints, add network rules, and change default actions. These commands appear in exam scenarios.

Study managed identity concepts deeply. Understand system-assigned versus user-assigned, how to grant permissions, and how different Azure services implement managed identity support.

Most importantly, understand the security rationale. Why is this pattern more secure than alternatives? What threats does it mitigate? How does defense in depth work? These conceptual questions appear alongside technical implementation questions.

## Final Thoughts

Securing applications in Azure requires layered defenses. Managed identities eliminate credential management. Key Vault centralizes secret storage with access control. Virtual network integration and service endpoints restrict network access. Together, these create a robust security posture for production applications.

For the AZ-204 exam, this topic bridges several domains: compute through containerized solutions, security through identities and Key Vault, networking through VNet integration, and storage through secure connectivity. Questions often combine these areas, presenting scenarios that require holistic solutions.

The practical skills you develop securing AKS applications transfer to other Azure services. App Service, Functions, Container Apps, and even Virtual Machines use similar patterns. Master this approach, and you'll be well-prepared for the security portions of the exam and for building production Azure solutions.

Thanks for listening to this episode on securing AKS applications with Key Vault and Virtual Networks. I hope this deepens your understanding of Azure security patterns and prepares you for the relevant AZ-204 exam questions. Good luck with your studies!
