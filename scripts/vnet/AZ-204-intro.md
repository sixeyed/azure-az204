# Virtual Networks: AZ-204 Exam Focus

Great work! This Virtual Networks lab is essential for the "Implement Azure Infrastructure as a Service Solutions" domain of the AZ-204 exam. Understanding VNets is crucial because they impact application security, performance, and architecture.

## What We'll Cover

We'll examine why VNets matter for developers - enabling security isolation so components communicate privately, service integration with Azure SQL Database, Storage, and Container Instances, and multi-tier architectures with frontend and backend separation.

We'll explore CIDR notation and IP address planning that the exam expects you to understand. When you see 10.10.0.0/16, you'll know the /16 means 16 bits are fixed giving 65,536 addresses, /24 subnets provide 256 addresses, and subnet ranges must not overlap and must fall within the parent VNet.

The exam tests your knowledge of how VMs and compute services integrate with VNets - specifying VNet and subnet during creation, the automatic networking resources Azure creates (NICs, NSGs, public IPs), and how VMs communicate using private addresses.

You'll understand VNet integration for Container Instances, App Service VNet integration for accessing private resources, and Private Endpoints versus Service Endpoints for securing PaaS services.

We'll cover Network Security Groups at the subnet and NIC level, and when VNet integration is required versus optional for different Azure services.

The exam includes infrastructure as code with ARM templates - understanding when to use declarative templates versus imperative CLI commands, template parameters and variables, and DevOps integration.

Master VNet planning, configuration, and service integration for the AZ-204!
