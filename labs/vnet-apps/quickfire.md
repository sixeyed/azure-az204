# VNet Integration with Apps - Quickfire Questions

## Question 1
What is VNet integration for App Service?


- A) Enabling App Service to access resources in a virtual network
- B) Public internet only
- C) Connecting VMs
- D) DNS configuration

**Answer: A**
VNet integration allows App Service apps to make outbound calls to resources within a VNet (databases, internal APIs).
---
## Question 2
What are the VNet integration types?


- A) Only one type
- B) Basic and Premium
- C) Regional VNet Integration and Gateway-required VNet Integration
- D) Public and Private

**Answer: C**
Regional integration (same region, preferred) and Gateway-required integration (cross-region/classic VNets).
---
## Question 3
What App Service plans support VNet integration?


- A) Only Free
- B) Only Premium
- C) Standard, Premium, PremiumV2, PremiumV3, Elastic Premium
- D) All plans

**Answer: C**
VNet integration requires Standard or higher. Not available in Free, Shared, or Basic tiers.
---
## Question 4
Can App Service access on-premises resources through VNet integration?


- A) Yes, if VNet connects to on-premises via VPN or ExpressRoute
- B) Requires separate service
- C) Only with public IPs
- D) No, Azure only

**Answer: A**
VNet integration + VPN/ExpressRoute allows App Service to reach on-premises resources.
---
## Question 5
What is the purpose of using Private Endpoints with App Service?


- A) Enables private inbound access to App Service from VNet
- B) No purpose
- C) Faster performance only
- D) Cost reduction

**Answer: A**
Private Endpoints provide private IPs for inbound connectivity, removing public internet exposure.
---
## Question 6
Can you use Key Vault with VNet service endpoints from App Service?


- A) No integration
- B) Only public access
- C) Requires custom code
- D) Yes, App Service with VNet integration can access Key Vault via service endpoint

**Answer: D**
VNet integration allows App Service to securely access Key Vault over service endpoints or private endpoints.
---
## Question 7
What is the difference between VNet integration and Private Endpoints?


- A) Private Endpoints are deprecated
- B) VNet integration is inbound only
- C) Same thing
- D) VNet integration is for outbound; Private Endpoints are for inbound

**Answer: D**
VNet integration: app makes outbound calls into VNet. Private Endpoint: external clients connect to app via VNet.
---
## Question 8
Do you need to modify application code for VNet integration?


- A) Only for .NET apps
- B) Complete rewrite required
- C) Major refactoring needed
- D) No code changes needed; works transparently

**Answer: D**
VNet integration is infrastructure-level; applications make normal outbound calls without code changes.
---
## Question 9
What is the subnet requirement for regional VNet integration?


- A) No subnet needed
- B) Shared with VMs
- C) Any subnet
- D) Dedicated subnet for integration (Microsoft.Web/serverFarms delegation)

**Answer: D**
Regional VNet integration requires a dedicated subnet delegated to Microsoft.Web/serverFarms.
---
## Question 10
Can multiple apps share the same integration subnet?


- A) Maximum 2 apps
- B) No, one app per subnet
- C) Yes, multiple apps from the same App Service Plan can share integration subnet
- D) Requires separate VNets

**Answer: C**
Apps in the same App Service Plan can share the integration subnet; different plans need separate subnets.