# Virtual Network Applications: AZ-204 Exam Focus

Great work! This VNet integration lab is essential for the "Implement Azure Security" and "Implement Azure infrastructure" objectives in the AZ-204 exam. Understanding network integration is crucial for secure Azure applications.

## What We'll Cover

We'll examine App Service VNet Integration that the exam tests extensively. Regional VNet Integration connects apps to subnets in the same region enabling access to VNet resources, on-premises via VPN, and Azure services via service endpoints. Gateway-required VNet Integration for cross-region scenarios requires VPN Gateway. Know that VNet Integration affects outbound traffic only while inbound requires private endpoints or service endpoints.

We'll explore private endpoints as the preferred security approach where private IP addresses in VNet provide access to PaaS services, traffic never uses public internet, private DNS zones resolve service names to private IPs, and network security groups control access. The exam tests when to use private endpoints versus service endpoints.

You'll master Container Instances with VNet Integration deploying containers into VNet subnets with private IPs, enabling communication with VNet resources without public exposure, and using network security groups for traffic control. This is ideal for batch jobs and backend processing.

The exam tests Azure Kubernetes Service networking with two models. Azure CNI assigns VNet IPs to pods enabling direct VNet integration but consuming more IP addresses. Kubenet uses pod CIDR separate from VNet conserving IPs but requiring route tables for VNet communication. Know the tradeoffs for exam scenarios.

We'll cover service endpoints versus private endpoints where service endpoints use Microsoft backbone without private IPs, provide subnet-level access control, and work with storage accounts and SQL databases. Private endpoints provide private IPs, enable granular access control, and work with most PaaS services as the more secure option.

You'll understand hybrid connectivity that appears in exam scenarios including VPN Gateway connecting VNets to on-premises, ExpressRoute for dedicated private connections, VNet peering for connecting Azure VNets, and VNet Integration enabling App Service and Functions to access all connected networks.

The exam includes security best practices: never expose databases with public endpoints, use private endpoints for all PaaS services in production, implement network security groups for traffic control, use Azure Firewall for centralized egress filtering, enable DDoS protection for public-facing applications, and monitor with Network Watcher and Azure Monitor.

Master VNet integration patterns, private connectivity options, and security configurations for the AZ-204!
