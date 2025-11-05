# Virtual Machines - AZ-204 Exam Introduction

Excellent work with VMs! Understanding virtual machines is important for the AZ-204 exam's compute and decision-making domains.

## What We'll Cover

**IaaS vs PaaS decision making** is critical. Use VMs when you need complete control over OS and software, need to run applications requiring specific OS configurations, are migrating legacy applications that can't be containerized, or need full administrative access. Prefer PaaS alternatives when you want to focus on application code rather than infrastructure, need automatic scaling and high availability, want built-in patching and maintenance, or are building cloud-native applications. The exam tests understanding of when VMs are appropriate.

**VM creation and configuration** using Azure CLI requires knowing `az vm create` with key parameters: resource group (-g), location (-l), VM name (-n), image (--image), size (--size), and authentication options. Portal workflow includes resource group selection, image and size selection, networking and disk configuration, and authentication setup. The exam tests understanding of creation processes.

**Resource dependencies** must be understood. Virtual Network (VNet) provides network isolation and connectivity. Network Interface (NIC) connects VM to virtual network. Network Security Group (NSG) provides firewall rules controlling traffic. Public IP Address enables optional internet connectivity. Managed Disks include OS disk and optional data disks. The exam tests understanding of dependencies and automatic vs manual creation.

**VM sizes and performance** require knowing different series: A-Series for entry-level development and test, B-Series burstable for variable CPU usage, D-Series general purpose with balanced CPU-to-memory, E-Series memory-optimized for databases, F-Series compute-optimized with higher CPU-to-memory ratio, N-Series GPU-enabled for machine learning. VM size affects CPU cores, memory, network bandwidth, disk throughput and IOPS, and cost. The exam tests choosing appropriate sizes.

**Storage and disks** have performance characteristics: Standard HDD lowest cost for backup, Standard SSD better performance for web servers, Premium SSD high performance for production databases, Ultra Disk highest performance with sub-millisecond latency. You can attach multiple data disks, resize disks (increase only), take snapshots for backup, and encrypt disks. The exam tests understanding of disk types and operations.

**Networking and security** concepts include: NSG rules configure traffic by port number, protocol, source/destination, and priority (lower numbers processed first); Port 22 for SSH, 3389 for RDP, 80 for HTTP, 443 for HTTPS; Public IPs enable internet connectivity while Private IPs are for internal VNet communication with static vs dynamic allocation; Connectivity options include SSH for Linux, RDP for Windows, Azure Bastion for secure browser-based access, and VPN/ExpressRoute for hybrid connectivity. The exam tests network security configuration.

**Managed Identities** enable VMs to authenticate to Azure services. System-Assigned Managed Identity is created with VM and deleted when VM is deleted. User-Assigned Managed Identity is created independently and assigned to multiple VMs. This eliminates credentials in code - a security best practice tested on the exam.

We'll cover **VM availability and scaling** (Availability Sets protect against hardware failures, Availability Zones protect against datacenter failures, VM Scale Sets auto-scale instances, Load Balancers distribute traffic), **cost management** (VM size affects cost, region pricing varies, Azure Hybrid Benefit reduces Windows costs, Reserved Instances save up to 72%, Spot VMs use spare capacity), and **common scenarios** about choosing between VM, App Service, Container Instances, AKS, Azure Functions, and Azure Batch.

Master Virtual Machines for the AZ-204!
