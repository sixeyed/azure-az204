# Azure Virtual Networks (VNet) - Quickfire Questions

## Question 1
What is an Azure Virtual Network (VNet)?


- A) Public internet
- B) Isolated private network in Azure for resources to communicate securely
- C) Physical network
- D) VPN only

**Answer: B**
VNets provide network isolation, allowing Azure resources to securely communicate with each other, internet, and on-premises.
---
## Question 2
What is an address space in VNet?


- A) Storage space
- B) Public IP range
- C) Physical location
- D) Private IP address range (CIDR) for the virtual network

**Answer: D**
Address space defines private IP range (e.g., 10.0.0.0/16) used within the VNet.
---
## Question 3
What is a subnet?


- A) Underwater network
- B) Public network
- C) Storage account
- D) Subdivision of VNet address space for organizing resources

**Answer: D**
Subnets divide VNet into smaller segments for resource organization and network security.
---
## Question 4
Can resources in different VNets communicate by default?


- A) Only with load balancer
- B) No, requires VNet peering or VPN gateway
- C) Only in same region
- D) Yes, automatically

**Answer: B**
VNets are isolated. Communication requires VNet peering, VPN gateway, or routing through internet.
---
## Question 5
What is VNet peering?


- A) Connecting two VNets for direct, low-latency communication
- B) Social networking
- C) Monitoring
- D) Load balancing

**Answer: A**
VNet peering connects VNets within same or different regions, enabling seamless communication via Azure backbone.
---
## Question 6
What is a Network Security Group (NSG)?


- A) Application group
- B) Firewall rules filtering inbound/outbound traffic based on source/destination, port, protocol
- C) Storage security
- D) User group

**Answer: B**
NSGs contain security rules allowing or denying traffic, applied to subnets or individual network interfaces.
---
## Question 7
Can you connect VNet to on-premises network?


- A) Only with public IPs
- B) Not supported
- C) Yes, using VPN Gateway or ExpressRoute
- D) No, cloud-only

**Answer: C**
Site-to-Site VPN, Point-to-Site VPN, or ExpressRoute connects VNet to on-premises infrastructure.
---
## Question 8
What is a service endpoint?


- A) Web endpoint
- B) Extends VNet to Azure services over Azure backbone without public IPs
- C) API endpoint
- D) Monitoring endpoint

**Answer: B**
Service endpoints provide secure, direct access to Azure services (Storage, SQL) from VNet without internet.
---
## Question 9
What is the difference between service endpoint and private endpoint?


- A) Same thing
- B) Service endpoint extends VNet to service; private endpoint brings service into VNet with private IP
- C) Private is public
- D) Service endpoint is deprecated

**Answer: B**
Service endpoint: VNet traffic to service. Private endpoint: service gets private IP in your VNet (more isolated).
---
## Question 10
What is the default outbound internet access for VNet resources?


- A) Requires configuration
- B) Not possible
- C) Allowed by default (using dynamic public IPs)
- D) Blocked

**Answer: C**
VNet resources have outbound internet access by default. Inbound requires public IP, load balancer, or Application Gateway.