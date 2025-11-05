# Key Vault Access Security - Exercises Introduction

We've covered securing Key Vault with two distinct security layers: network-level and identity-based security. Now let's implement defense-in-depth protection.

## What You'll Do

You'll start by **creating a Key Vault and storing secrets**. Then you'll implement **network-level security by configuring virtual network service endpoints**. Service endpoints provide a secure, private path between your VNet and Azure services without going over the public internet.

Next, you'll **add network rules to restrict Key Vault access** to specific subnets only. Then you'll **change the default action to Deny**, enforcing that only requests from allowed networks can even reach the vault. Try accessing Key Vault from your local machine - it's blocked! This is network-level security in action.

Now you'll **create a VM within the allowed subnet**. From this VM, network access works. But you still can't access secrets without authentication! This demonstrates the two-layer security model.

You'll **assign a system-assigned managed identity** to the VM. This identity authenticates to Azure AD automatically using the Azure Instance Metadata Service - no passwords or certificates needed. Then you'll **grant Key Vault access policies** to this managed identity, giving it permission to Get and List secrets.

Finally, you'll **verify passwordless secret retrieval** from the VM. The application uses the managed identity to authenticate (automatically, no credentials in code), passes network security (VM is in allowed subnet), and retrieves secrets successfully. This is production-ready security!

The **lab challenge** explores soft delete behavior when recreating deleted secrets with the same name - understanding recovery workflows.

Let's implement defense-in-depth Key Vault security!
