# Securing Key Vault Access - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on securing Azure Key Vault access. If you're preparing for the Azure AZ-204 certification, this topic is crucial because it combines several key concepts: network security, identity-based access control, and managed identities.

Today we're going to explore how to properly lock down access to your Key Vaults to ensure only authorized resources can access your sensitive data. This isn't just about passing an exam - misconfigured Key Vault security is one of the most common cloud security vulnerabilities.

## Why Key Vault Security Matters

Key Vaults store your most sensitive data - passwords, connection strings, API keys, encryption keys, and certificates. If an attacker gains access to your Key Vault, they've potentially compromised your entire application infrastructure. They can access your databases, call your external APIs using your credentials, decrypt your data, impersonate your services.

Because of this, securing access to Key Vault is absolutely critical. A misconfigured Key Vault could expose your secrets to unauthorized users or services. The default configuration allows access from any network globally, which might be convenient for development but is far too permissive for production environments.

## Two Layers of Security

Azure Key Vault provides two distinct layers of security that work together to protect your secrets. Understanding both layers and how they interact is essential for the AZ-204 exam.

The first layer is network-level security. This controls whether a request can even reach the Key Vault service. Think of this as a firewall at the perimeter. Before a request can even attempt authentication, it must come from an allowed network. By default, Key Vaults are accessible from any network on the internet, but you can restrict access to specific Azure virtual networks or specific IP addresses.

The second layer is identity-based security. Even if a request can reach the Key Vault over the network - even if it passes through the network firewall - the caller still needs to authenticate as an authorized principal. Azure uses the term "principal" to refer to any identity, whether that's a user account, a group of users, a service principal representing an application, or a managed identity for an Azure resource.

These two layers are independent. Network restrictions can deny access before authentication happens. Identity-based permissions can deny access even if the network allows it. Both layers must allow the request for it to succeed. This is defense in depth - multiple layers of security protecting your sensitive data.

## The Default Configuration Problem

When you create a Key Vault, the default configuration allows public access from all networks. Any device anywhere on the internet can attempt to connect to your Key Vault. They'll still need proper authentication and authorization to actually read secrets, but they can reach the service.

This creates several risks. First, it exposes the Key Vault to potential attack from anywhere on the internet. Attackers can attempt to exploit vulnerabilities, try credential-based attacks, or probe for misconfigurations. Second, it makes it harder to audit access. When connections can come from anywhere, identifying anomalous access patterns is more difficult. Third, it violates the principle of least privilege. If your applications only run in Azure, why should the Key Vault be accessible from outside Azure?

For production environments, you should restrict Key Vault network access to only the networks that legitimately need to access it. This significantly reduces the attack surface.

## Service Endpoints: Secure Virtual Network Connectivity

Service endpoints are the mechanism for allowing Azure resources in a virtual network to securely access Azure platform services like Key Vault, Storage, and SQL Database.

Here's how they work. When you enable a service endpoint for Key Vault on a subnet, Azure adds special routes to the subnet's route table. Traffic from that subnet to Key Vault is routed through the Azure backbone network instead of going over the public internet. The traffic never leaves Microsoft's network infrastructure. This provides several benefits.

First, it's more secure. Traffic on the backbone network isn't exposed to internet-based attacks. Second, it's more reliable. Microsoft's backbone network has better performance and availability characteristics than the public internet. Third, it's faster. Lower latency and higher throughput because you're using Microsoft's private network. Fourth, it's transparent. Applications don't need any code changes - they still use the same public DNS names and endpoints.

Service endpoints are configured at the subnet level. You enable specific services - like Microsoft.KeyVault for Key Vault, or Microsoft.Storage for Storage. Once enabled, resources in that subnet can access the service through the backbone network.

On the Key Vault side, you configure network rules that allow access from specific virtual networks and subnets. The Key Vault checks incoming requests: is this request coming from an allowed network? If yes, allow it through to authentication. If no, reject it at the network layer before authentication even happens.

Important detail: service endpoints don't make the service private. The Key Vault still has its public DNS name and public IP address. Service endpoints just provide a secure path from your virtual network to that public endpoint, and you configure Key Vault to only accept traffic from that secure path.

## Configuring Network Restrictions

Let me walk through the process of locking down a Key Vault to only allow access from a specific virtual network.

First, you create a virtual network with subnets where your applications will run. This might be where your virtual machines, container instances, or other Azure resources are deployed.

Next, you enable the Key Vault service endpoint on the subnet. This is done with a command that updates the subnet configuration to add Microsoft.KeyVault to its service endpoints. This tells Azure to route Key Vault traffic from this subnet through the backbone network.

Then, you add a network rule to your Key Vault that allows access from that specific virtual network and subnet. This tells the Key Vault "allow connections that come through this subnet's service endpoint."

Finally, and this is the critical step that people often miss, you change the Key Vault's default action from "Allow" to "Deny". By default, adding network rules doesn't block other access - it just adds exceptions. The default behavior is still to allow access from everywhere. You must explicitly change the default to deny.

After these steps, the Key Vault is locked down. Requests from outside the allowed network are rejected at the network layer. You'll get a "Forbidden" error immediately, before authentication even occurs. The error message won't reveal information about what secrets exist or who has access - it just says network access is denied.

This means your local development machine can't access the Key Vault anymore. Your CI/CD pipelines running outside Azure can't access it. Nothing can access it except resources in the allowed networks. This is exactly what you want for production security, but it requires planning for deployment and administration scenarios.

## Managed Identities: The Missing Piece

Network restrictions ensure only resources in your virtual network can reach the Key Vault. But those resources still need to authenticate and have appropriate permissions. This is where managed identities become critical.

A managed identity is an identity in Azure Active Directory that Azure manages for you. When you enable a managed identity for an Azure resource - a virtual machine, an App Service, an Azure Function, a container instance - Azure automatically creates an identity in Azure AD and associates it with that resource.

The key benefit is that there are no credentials you need to manage. No passwords, no certificates, no secret keys. Azure handles authentication automatically through its instance metadata service. Your application code requests a token, Azure provides one using the managed identity, and that token is used to authenticate with Key Vault.

There are two types of managed identities. System-assigned identities are tied to a single Azure resource. When you create a VM with a system-assigned identity, that identity exists only for that VM. When you delete the VM, the identity is automatically deleted too. This tight coupling is appropriate when an identity is used by just one resource.

User-assigned identities have an independent lifecycle. You create them as standalone resources, then assign them to one or more Azure resources. You can assign the same identity to multiple VMs, App Services, or Functions. When you delete one of those resources, the identity persists because others might still use it. This is appropriate when multiple resources need the same permissions.

For the AZ-204 exam, you need to understand when to use each type. If the scenario mentions a single resource or ties the identity to one resource's lifecycle, use system-assigned. If it mentions multiple resources sharing identity or persistence beyond resource deletion, use user-assigned.

## The Complete Security Flow

Let me walk through what happens when an Azure resource with a managed identity accesses Key Vault with network restrictions.

Your application running in a virtual machine needs to read a secret from Key Vault. The VM has a managed identity, and that identity has been granted "get secrets" permission through an access policy or RBAC role.

The application code uses the Azure SDK to request the secret. The SDK first contacts the Azure Instance Metadata Service, which is a special endpoint available to all Azure VMs at IP address 169.254.169.254. This endpoint is not routable from outside the VM - only the VM itself can reach it.

The metadata service authenticates the VM and returns an access token for the managed identity. This token is a JSON Web Token signed by Azure AD that asserts the identity of the VM.

The SDK then makes a request to Key Vault with this token in the authorization header. The request travels through the subnet's service endpoint, staying on the Azure backbone network.

Key Vault receives the request and first checks network-level access: is this request coming from an allowed network? Yes, it's coming through the service endpoint from an allowed subnet. Network check passes.

Next, Key Vault validates the token: is this token valid, not expired, signed by Azure AD? Yes, it's a valid token. Authentication succeeds.

Then Key Vault checks authorization: does this identity have permission to read secrets? The access policy grants this identity "get secrets" permission. Authorization succeeds.

Finally, Key Vault returns the secret value to the application.

If any step fails - wrong network, invalid token, no permission - the request is denied. All steps must succeed. This is defense in depth in practice.

## Access Policies versus RBAC

Key Vault supports two models for authorization, and understanding both is important for the exam.

Access policies are the traditional model. You configure them directly on the Key Vault. They grant specific permissions on secrets, keys, and certificates to specific principals. Permissions are granular: get, list, set, delete, backup, restore, recover, purge for secrets. Similar permissions exist for keys and certificates.

Access policies are configured per Key Vault. If you have multiple Key Vaults, you configure access policies on each one independently. This can become tedious at scale but provides fine-grained control.

Azure RBAC is the newer model. Instead of Key Vault-specific access policies, you use standard Azure role assignments. Azure provides built-in roles like "Key Vault Secrets User" for reading secrets, "Key Vault Secrets Officer" for managing secrets, and "Key Vault Administrator" for full access.

RBAC integrates with Azure's broader security model. Roles can be assigned at different scopes - management group, subscription, resource group, or individual Key Vault. Permissions inherit through the hierarchy. This provides consistency with other Azure resources and centralized permission management.

You choose one model when you create the Key Vault. If you enable RBAC authorization, access policies are ignored. You can't use both models on the same Key Vault. For new Key Vaults, Microsoft recommends RBAC for its consistency and integration with Azure's overall security model.

The exam may test your understanding of both models and when each is appropriate. Know the built-in RBAC roles and what permissions they grant.

## Soft Delete and Purge Protection

One more security feature worth discussing is soft delete, which protects against accidental deletion of secrets.

Soft delete is enabled by default on all new Key Vaults. When you delete a secret, key, or certificate, it doesn't disappear immediately. Instead, it enters a "deleted" state where it's retained for a recovery period - typically 90 days.

During this period, you can recover the deleted object. You use a "recover" command that restores it exactly as it was. If you try to create a new secret with the same name, it fails because the name is still in use by the deleted secret. You must either recover the deleted secret or permanently delete it - "purge" it - before the name can be reused.

Purge protection adds another layer. When enabled, it prevents anyone from purging deleted objects during the retention period. Even if someone explicitly tries to permanently delete a secret, the operation fails. They must wait for the retention period to expire.

Together, soft delete and purge protection provide comprehensive protection against accidental and malicious deletion. For production Key Vaults, both features should be enabled. Purge protection can't be disabled once enabled - this is by design to prevent attackers from disabling it.

## Common Exam Scenarios

Let me walk through some typical AZ-204 exam scenarios related to Key Vault security.

**Scenario one**: "An application running in Azure App Service needs to read database connection strings from Key Vault. What is the most secure approach?"

The answer involves several steps. Enable a system-assigned managed identity on the App Service. Grant that identity "get secrets" permission on the Key Vault through an access policy or RBAC role. Configure the application to use DefaultAzureCredential, which automatically uses the managed identity. Optionally, restrict Key Vault network access to only the App Service's outbound IP addresses or integrate with a virtual network. This approach has no credentials in code or configuration.

**Scenario two**: "A development team needs to list what secrets exist in a Key Vault but should not be able to read secret values. How do you configure this?"

Grant the team "list secrets" permission but not "get secrets" permission. With access policies, you explicitly select only "list" when configuring the policy. With RBAC, you could use the "Key Vault Reader" role, which allows reading metadata but not secret values. This follows the principle of least privilege - grant only the permissions actually needed.

**Scenario three**: "An application needs to access Key Vault but must use private connectivity only, with no traffic over the public internet."

Use Private Link and private endpoints instead of service endpoints. Create a private endpoint for the Key Vault in your virtual network. This gives the Key Vault a private IP address from your virtual network's address space. Configure the Key Vault to deny all public network access. All traffic stays within your virtual network. This is more isolated than service endpoints but has associated costs.

**Scenario four**: "Multiple VMs in different subnets need to access the same Key Vault using network restrictions."

Enable the Key Vault service endpoint on each subnet where VMs are located. Add network rules to the Key Vault allowing each of those subnets. Set the Key Vault's default action to deny. Each VM needs appropriate authentication - either managed identities or other credentials - but the network rules allow all the subnets.

**Scenario five**: "After restricting Key Vault network access, deployment pipelines outside Azure fail to update secrets. How do you fix this?"

You have several options. Add the pipeline's public IP address to the Key Vault firewall rules - this is simple but less secure. Use a self-hosted agent running in the allowed virtual network - more secure but requires infrastructure. Use temporary firewall rules that are enabled only during deployments - complex but flexible. Or use Key Vault's "Azure services" exception, which allows trusted Microsoft services to bypass the firewall - works for Azure DevOps.

## Best Practices for Production

Let me highlight best practices for securing Key Vault in production environments, which are also important for the exam.

One: Always restrict network access. Don't leave Key Vaults with public access from all networks. Use service endpoints or private endpoints to limit access to your virtual networks.

Two: Always use managed identities when Azure resources access Key Vault. Never store credentials for Key Vault access in code or configuration files.

Three: Apply the principle of least privilege. Grant only the permissions actually needed. If an application only reads secrets, grant "get secrets" but not "list", "set", or "delete".

Four: Enable soft delete and purge protection on production Key Vaults. Protect against accidental and malicious deletion.

Five: Separate Key Vaults by environment. Use different vaults for development, testing, and production. This limits blast radius if a vault is compromised and prevents accidentally using production secrets in non-production environments.

Six: Monitor and alert on Key Vault access. Use Azure Monitor to track who accesses what and when. Alert on suspicious patterns like access from unexpected locations or principals.

Seven: Use RBAC for new Key Vaults. It provides better integration with Azure's overall security model and is the recommended approach going forward.

Eight: Plan for administrative access. If you lock down network access, ensure administrators can still manage the Key Vault. Either grant access from specific IP addresses or use Azure Bastion or VPN to access from within allowed networks.

## Key Takeaways for the AZ-204 Exam

Let me summarize the critical concepts you must understand for exam success.

**Two layers of security**: Network restrictions and identity-based permissions are independent layers. Both must allow access for requests to succeed.

**Service endpoints**: Allow virtual network resources to access Azure services through the backbone network. Configured at the subnet level. Key Vault still has public endpoint but only accepts traffic from allowed networks.

**Private endpoints**: Create a private IP address for Key Vault in your virtual network. More isolated than service endpoints but have associated costs. Traffic never leaves your virtual network.

**Managed identities**: Azure-managed identities with no credentials to manage. System-assigned for single resources, user-assigned for multiple resources. Always preferred over service principals for Azure-to-Azure authentication.

**Access policies vs RBAC**: Access policies are the traditional model with fine-grained permissions. RBAC is the modern model using standard Azure roles. Choose one model per Key Vault, not both.

**Soft delete and purge protection**: Soft delete enables recovery during retention period. Purge protection prevents permanent deletion during retention. Both should be enabled for production.

**DefaultAzureCredential**: The credential type that works everywhere - production with managed identity, development with Azure CLI credentials. Use this in all application code.

**Network configuration steps**: Enable service endpoint on subnet, add network rule to Key Vault, change default action to Deny. All three steps are required.

## Final Thoughts

Securing Azure Key Vault access combines multiple Azure security concepts: network isolation, identity and access management, managed identities, and defense in depth. These concepts appear throughout the AZ-204 exam in various contexts.

For the exam, you need to understand not just how to configure security, but why each layer matters and when to apply specific security controls. You'll see scenario-based questions that require you to choose appropriate security approaches or troubleshoot security configurations.

The concepts we've covered today - network restrictions using service endpoints, identity-based access control through access policies or RBAC, managed identities for passwordless authentication, and protection features like soft delete - form a comprehensive security model for Key Vault.

Practice these configurations hands-on. Create a Key Vault, lock it down to a virtual network, create a VM with a managed identity, grant permissions, and verify access works. Experience the "Forbidden" error when accessing from outside the network. This practical experience makes the concepts concrete and gives you confidence on exam day.

Remember that security is not optional. The exam tests not just your knowledge of Azure features, but your understanding of security best practices. Always think about least privilege, defense in depth, and elimination of credentials from code and configuration.

Thanks for listening to this episode on securing Azure Key Vault access. I hope this gives you both the practical security skills and the exam preparation insights you need. Good luck with your AZ-204 certification journey!
