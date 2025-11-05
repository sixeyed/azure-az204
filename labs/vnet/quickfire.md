# Azure Virtual Networks (VNet) - Quickfire Questions

## Question 1
What is an Azure Virtual Network (VNet)?

- A) Physical network
- B) Isolated private network in Azure for resources to communicate securely
- C) Public internet
- D) VPN only

**Answer: B**
VNets provide network isolation, allowing Azure resources to securely communicate with each other, internet, and on-premises.

---

## Question 2
What is an address space in VNet?

- A) Physical location
- B) Private IP address range (CIDR) for the virtual network
- C) Public IP range
- D) Storage space

**Answer: B**
Address space defines private IP range (e.g., 10.0.0.0/16) used within the VNet.

---

## Question 3
What is a subnet?

- A) Underwater network
- B) Subdivision of VNet address space for organizing resources
- C) Public network
- D) Storage account

**Answer: B**
Subnets divide VNet into smaller segments for resource organization and network security.

---

## Question 4
Can resources in different VNets communicate by default?

- A) Yes, automatically
- B) No, requires VNet peering or VPN gateway
- C) Only in same region
- D) Only with load balancer

**Answer: B**
VNets are isolated. Communication requires VNet peering, VPN gateway, or routing through internet.

---

## Question 5
What is VNet peering?

- A) Social networking
- B) Connecting two VNets for direct, low-latency communication
- C) Load balancing
- D) Monitoring

**Answer: B**
VNet peering connects VNets within same or different regions, enabling seamless communication via Azure backbone.

---

## Question 6
What is a Network Security Group (NSG)?

- A) User group
- B) Firewall rules filtering inbound/outbound traffic based on source/destination, port, protocol
- C) Storage security
- D) Application group

**Answer: B**
NSGs contain security rules allowing or denying traffic, applied to subnets or individual network interfaces.

---

## Question 7
Can you connect VNet to on-premises network?

- A) No, cloud-only
- B) Yes, using VPN Gateway or ExpressRoute
- C) Only with public IPs
- D) Not supported

**Answer: B**
Site-to-Site VPN, Point-to-Site VPN, or ExpressRoute connects VNet to on-premises infrastructure.

---

## Question 8
What is a service endpoint?

- A) API endpoint
- B) Extends VNet to Azure services over Azure backbone without public IPs
- C) Web endpoint
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

- A) Blocked
- B) Allowed by default (using dynamic public IPs)
- C) Requires configuration
- D) Not possible

**Answer: B**
VNet resources have outbound internet access by default. Inbound requires public IP, load balancer, or Application Gateway.
