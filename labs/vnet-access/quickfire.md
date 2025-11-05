# VNet Access Control - Quickfire Questions

## Question 1
What are NSG rules based on?

- A) Only IP addresses
- B) Priority, source/destination IP/port, protocol, action (allow/deny)
- C) Only protocols
- D) Random

**Answer: B**
NSG rules use 5-tuple: priority, source, destination, protocol, action to filter traffic.

---

## Question 2
What is the priority range for NSG rules?

- A) 1-10
- B) 100-4096
- C) Any number
- D) 1-100

**Answer: B**
Priorities range from 100-4096. Lower numbers processed first. Rules stop at first match.

---

## Question 3
What is an Application Security Group (ASG)?

- A) Application tier
- B) Logical grouping of VMs for simplified NSG rules
- C) Storage group
- D) Load balancer pool

**Answer: B**
ASGs group VMs by role (web, app, data), allowing NSG rules using group names instead of IP addresses.

---

## Question 4
Can you associate NSG to both subnet and NIC?

- A) No, only one
- B) Yes, both subnet and network interface (rules combined)
- C) Only subnet
- D) Only NIC

**Answer: B**
NSGs can be applied at subnet level, NIC level, or both. Both sets of rules apply (most restrictive wins).

---

## Question 5
What are default NSG rules?

- A) No defaults
- B) Allow VNet traffic, allow outbound internet, deny all inbound from internet
- C) Allow everything
- D) Deny everything

**Answer: B**
Defaults: allow within VNet, allow outbound internet, deny inbound from internet. Cannot be deleted but can override.

---

## Question 6
What is service tag in NSG rules?

- A) Price tag
- B) Predefined label representing IP ranges for Azure services (e.g., Storage, SQL)
- C) Version tag
- D) Resource tag

**Answer: B**
Service tags simplify rules: use "Storage", "AzureCloud", "Internet" instead of managing IP ranges.

---

## Question 7
What is DDoS protection in Azure?

- A) No protection
- B) Basic (free, automatic) or Standard (enhanced, paid) protection against DDoS attacks
- C) Only manual mitigation
- D) Requires third-party

**Answer: B**
DDoS Protection Basic is automatic and free. Standard adds advanced mitigation, monitoring, and SLA.

---

## Question 8
What is Azure Firewall?

- A) NSG replacement
- B) Managed, cloud-native firewall with advanced features (FQDN filtering, threat intelligence)
- C) Free service
- D) Physical firewall

**Answer: B**
Azure Firewall is stateful, managed network firewall with application and network rules, threat intelligence integration.

---

## Question 9
Can you log NSG traffic?

- A) No logging
- B) Yes, using NSG flow logs sent to Storage and Log Analytics
- C) Only manual logs
- D) Only to email

**Answer: B**
NSG flow logs capture allowed/denied traffic, sent to Storage Account, viewable in Log Analytics or Network Watcher.

---

## Question 10
What is the forced tunneling?

- A) VPN tunnel
- B) Routing all internet-bound traffic through on-premises for inspection/compliance
- C) Load balancing
- D) Encryption method

**Answer: B**
Forced tunneling redirects internet traffic through on-premises network for central monitoring/control.
