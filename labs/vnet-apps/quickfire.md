# VNet Integration with Apps - Quickfire Questions

## Question 1
What is VNet integration for App Service?

- A) Connecting VMs
- B) Enabling App Service to access resources in a virtual network
- C) Public internet only
- D) DNS configuration

**Answer: B**
VNet integration allows App Service apps to make outbound calls to resources within a VNet (databases, internal APIs).

---

## Question 2
What are the VNet integration types?

- A) Only one type
- B) Regional VNet Integration and Gateway-required VNet Integration
- C) Public and Private
- D) Basic and Premium

**Answer: B**
Regional integration (same region, preferred) and Gateway-required integration (cross-region/classic VNets).

---

## Question 3
What App Service plans support VNet integration?

- A) All plans
- B) Standard, Premium, PremiumV2, PremiumV3, Elastic Premium
- C) Only Premium
- D) Only Free

**Answer: B**
VNet integration requires Standard or higher. Not available in Free, Shared, or Basic tiers.

---

## Question 4
Can App Service access on-premises resources through VNet integration?

- A) No, Azure only
- B) Yes, if VNet connects to on-premises via VPN or ExpressRoute
- C) Only with public IPs
- D) Requires separate service

**Answer: B**
VNet integration + VPN/ExpressRoute allows App Service to reach on-premises resources.

---

## Question 5
What is the purpose of using Private Endpoints with App Service?

- A) Faster performance only
- B) Enables private inbound access to App Service from VNet
- C) Cost reduction
- D) No purpose

**Answer: B**
Private Endpoints provide private IPs for inbound connectivity, removing public internet exposure.

---

## Question 6
Can you use Key Vault with VNet service endpoints from App Service?

- A) No integration
- B) Yes, App Service with VNet integration can access Key Vault via service endpoint
- C) Only public access
- D) Requires custom code

**Answer: B**
VNet integration allows App Service to securely access Key Vault over service endpoints or private endpoints.

---

## Question 7
What is the difference between VNet integration and Private Endpoints?

- A) Same thing
- B) VNet integration is for outbound; Private Endpoints are for inbound
- C) Private Endpoints are deprecated
- D) VNet integration is inbound only

**Answer: B**
VNet integration: app makes outbound calls into VNet. Private Endpoint: external clients connect to app via VNet.

---

## Question 8
Do you need to modify application code for VNet integration?

- A) Complete rewrite required
- B) No code changes needed; works transparently
- C) Only for .NET apps
- D) Major refactoring needed

**Answer: B**
VNet integration is infrastructure-level; applications make normal outbound calls without code changes.

---

## Question 9
What is the subnet requirement for regional VNet integration?

- A) Any subnet
- B) Dedicated subnet for integration (Microsoft.Web/serverFarms delegation)
- C) Shared with VMs
- D) No subnet needed

**Answer: B**
Regional VNet integration requires a dedicated subnet delegated to Microsoft.Web/serverFarms.

---

## Question 10
Can multiple apps share the same integration subnet?

- A) No, one app per subnet
- B) Yes, multiple apps from the same App Service Plan can share integration subnet
- C) Maximum 2 apps
- D) Requires separate VNets

**Answer: B**
Apps in the same App Service Plan can share the integration subnet; different plans need separate subnets.
