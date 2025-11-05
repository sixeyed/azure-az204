# IaaS Apps - AZ-204 Exam Introduction

Great work with IaaS deployment! While PaaS is preferred, understanding IaaS is important for legacy migration scenarios on the AZ-204.

## What We'll Cover

**VM provisioning with proper image selection** uses publisher:offer:SKU:version format. Example: MicrosoftWindowsServer:WindowsServer:2022-datacenter-core:latest. Knowing how to find available images with `az vm image list` and understanding the naming convention is important. The exam tests selecting appropriate images for different scenarios.

**VM sizing for different workloads** must match requirements. D-series for general purpose (balanced CPU/memory), F-series for compute-intensive, E-series for memory-intensive, N-series for GPU workloads. The exam tests choosing appropriate sizes based on application needs and understanding cost implications.

**NSG rules with priorities** control network access. Lower numbers have higher priority (processed first). Rules specify source/destination (IP ranges or service tags), port ranges, and action (allow/deny). The exam tests designing NSG rules for scenarios like allowing HTTP but blocking RDP from internet, or restricting database access to specific subnets.

**Service endpoints for secure Azure service connectivity** provide private paths between VNets and Azure services (SQL Database, Storage Account, Key Vault). Enable service endpoint on subnet, configure Azure service firewall to allow that subnet. No public internet exposure. The exam tests when to use service endpoints versus private endpoints (dedicated private IPs in your VNet).

**VNet rules for SQL Database access** restrict connections to specific VNets/subnets. More secure than IP-based firewall rules because IPs can change, but subnet association is stable. The exam tests configuring VNet rules and troubleshooting connectivity issues.

**Connection string formats** for SQL Database use server name, database name, authentication method (SQL auth or Azure AD). Exam tests constructing correct connection strings and troubleshooting authentication failures.

**When to choose IaaS versus App Service** is critical. IaaS for: legacy apps requiring specific OS versions, full control needed, existing virtualization infrastructure being migrated. App Service for: modern apps, managed platform benefits, automatic scaling, built-in CI/CD. The exam frequently tests this decision.

We'll cover **security best practices** (Key Vault for connection strings, least privilege access), **managed disks**, **availability sets and zones**, **backup and disaster recovery**, and **troubleshooting** connectivity, performance, and deployment issues.

Master IaaS deployments for the AZ-204!
