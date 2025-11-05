# VNet Access Control - Quickfire Questions

## Question 1
What are NSG rules based on?


- A) Only protocols
- B) Random
- C) Only IP addresses
- D) Priority, source/destination IP/port, protocol, action (allow/deny)

**Answer: D**
NSG rules use 5-tuple: priority, source, destination, protocol, action to filter traffic.
---
## Question 2
What is the priority range for NSG rules?


- A) 100-4096
- B) 1-100
- C) 1-10
- D) Any number

**Answer: A**
Priorities range from 100-4096. Lower numbers processed first. Rules stop at first match.
---
## Question 3
What is an Application Security Group (ASG)?


- A) Logical grouping of VMs for simplified NSG rules
- B) Storage group
- C) Load balancer pool
- D) Application tier

**Answer: A**
ASGs group VMs by role (web, app, data), allowing NSG rules using group names instead of IP addresses.
---
## Question 4
Can you associate NSG to both subnet and NIC?


- A) Only subnet
- B) Only NIC
- C) Yes, both subnet and network interface (rules combined)
- D) No, only one

**Answer: C**
NSGs can be applied at subnet level, NIC level, or both. Both sets of rules apply (most restrictive wins).
---
## Question 5
What are default NSG rules?


- A) Allow everything
- B) No defaults
- C) Allow VNet traffic, allow outbound internet, deny all inbound from internet
- D) Deny everything

**Answer: C**
Defaults: allow within VNet, allow outbound internet, deny inbound from internet. Cannot be deleted but can override.
---
## Question 6
What is service tag in NSG rules?


- A) Resource tag
- B) Predefined label representing IP ranges for Azure services (e.g., Storage, SQL)
- C) Version tag
- D) Price tag

**Answer: B**
Service tags simplify rules: use "Storage", "AzureCloud", "Internet" instead of managing IP ranges.
---
## Question 7
What is DDoS protection in Azure?


- A) No protection
- B) Basic (free, automatic) or Standard (enhanced, paid) protection against DDoS attacks
- C) Requires third-party
- D) Only manual mitigation

**Answer: B**
DDoS Protection Basic is automatic and free. Standard adds advanced mitigation, monitoring, and SLA.
---
## Question 8
What is Azure Firewall?


- A) Physical firewall
- B) Managed, cloud-native firewall with advanced features (FQDN filtering, threat intelligence)
- C) Free service
- D) NSG replacement

**Answer: B**
Azure Firewall is stateful, managed network firewall with application and network rules, threat intelligence integration.
---
## Question 9
Can you log NSG traffic?


- A) Only manual logs
- B) No logging
- C) Yes, using NSG flow logs sent to Storage and Log Analytics
- D) Only to email

**Answer: C**
NSG flow logs capture allowed/denied traffic, sent to Storage Account, viewable in Log Analytics or Network Watcher.
---
## Question 10
What is the forced tunneling?


- A) VPN tunnel
- B) Encryption method
- C) Routing all internet-bound traffic through on-premises for inspection/compliance
- D) Load balancing

**Answer: C**
Forced tunneling redirects internet traffic through on-premises network for central monitoring/control.