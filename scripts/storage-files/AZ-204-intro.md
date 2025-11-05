# Azure Files Storage - AZ-204 Exam Introduction

Excellent work with Azure Files! This is an important storage option for the AZ-204 exam's "Develop for Azure storage" domain.

## What We'll Cover

**Storage account fundamentals for file shares** must be understood. Azure Files is a feature of Azure Storage Accounts requiring Standard or Premium tier selection. Standard tier uses HDD storage offering locally redundant or geo-redundant options. Premium tier uses SSD storage for low-latency scenarios with different redundancy options and higher costs, requiring FileStorage account kind (not general-purpose v2). You cannot convert between Standard and Premium after creation. The exam tests understanding of tier selection at creation time.

**File share configuration parameters** are testable. Share name must be lowercase and unique within storage account. Quota defines maximum size in gigabytes - Standard default is 5120 GB, Premium requires specifying provisioned size upfront. Tier options for Standard shares: hot, cool, or transaction-optimized. Premium shares don't have sub-tiers. The exam may test configuring shares with appropriate parameters.

**SMB protocol versions** need to be known. Azure Files uses SMB protocol versions 2.1 and 3.0. SMB 3.0 includes encryption in transit which is important for security. Windows, Linux, and macOS all support SMB but specific version support varies by OS version. The exam tests protocol compatibility understanding.

**Authentication methods** are critical. Storage account keys provide full access to storage account, should be protected and rotated regularly. Shared Access Signatures (SAS) provide limited access with specific permissions and time constraints at account or share level. Azure AD Domain Services (Azure AD DS) enables identity-based authentication for domain-joined machines - more secure than storage account keys. The exam tests security implications and when to use each method.

**Access patterns** differ by protocol. SMB access is used when mounting file share as network drive - most common for VMs and on-premises systems. REST API access allows programmatic access using Azure Storage SDK or direct HTTP calls requiring SAS token for authentication. The exam tests understanding of when each access method is appropriate.

**Comparison with other storage services** is frequently tested. Use Azure Files when you need file system semantics with directories and file shares, or shared access from multiple VMs. Use Blob Storage for unstructured object storage like images, videos, or backups. Use Azure Disks when only one VM needs storage and you need maximum performance. Use Azure NetApp Files for high-performance computing or specialized enterprise storage requirements. The exam tests choosing appropriate service based on requirements.

**Integration with Azure services** must be understood. Azure Virtual Machines can mount file shares for shared storage. Azure Container Instances can mount Azure Files as persistent volumes. Azure App Service can mount Azure Files for shared content across instances. Azure File Sync can replicate Azure Files to on-premises Windows Servers for hybrid scenarios. The exam tests understanding of use cases and configuration.

We'll cover **CLI commands** (`az storage share create`, `az storage share update` for quota changes, `az storage file upload`, `az storage share generate-sas`, `az storage account keys list`, `az storage account keys renew`), **security best practices** (use SMB 3.0+ for encryption, store keys in Azure Key Vault, use Azure AD DS for domain scenarios, plan for key rotation), **mounting commands** (platform-specific SMB mount syntax for Windows/Linux/macOS), **monitoring and troubleshooting** (Azure Monitor metrics, Storage Analytics logging, common issues like authentication failures after key rotation), and **common scenarios** about shared storage, lift-and-shift migrations, configuration files across instances, and development/debugging scenarios.

Master Azure Files for the AZ-204!
