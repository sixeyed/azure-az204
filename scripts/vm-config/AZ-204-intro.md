# VM Configuration Automation - AZ-204 Exam Introduction

Great work with VM automation! This topic supports AZ-204 exam objectives around compute solutions and VM management.

## What We'll Cover

**Infrastructure as Code** demonstrates automation principles. Custom Script Extensions are a common pattern across Azure services appearing in VM Scale Sets, Azure DevTest Labs, and ARM template deployments - the post-deployment configuration concept is universal. Declarative vs Imperative Configuration: JSON specification for custom script extensions is declarative (describe what you want) while run-command feature is imperative (tell Azure exactly what to do step by step). The exam tests understanding of automation approaches.

**Security and networking** with NSGs is critical. Default Deny: Azure follows security-first approach with VMs denying all inbound traffic from Internet by default - you explicitly allow only what's needed. Priority Rules: NSG rules have priority 100 to 4096 with lower numbers evaluated first, default rules start at 65000 so custom rules use lower numbers to take precedence. Source and Destination: rules filter by IP ranges, service tags, or application security groups. The exam tests NSG configuration and security principles.

**Automation patterns** must be understood. VM Extensions run after VM is created asynchronously - VM is running while extension executes so you can't assume completion just because VM is running. Cloud-init runs during VM provisioning on Linux synchronously with boot process - VM isn't fully available until cloud-init completes. Run Commands are on-demand operations that don't persist - they execute once with immediate output. The exam tests understanding of when to use each approach.

**Integration scenarios** show VMs in context. Web Applications: could deploy to Azure App Service or use VMs with custom script extensions installing web servers - understand tradeoffs of control vs management. Development Environments: Windows VM with dev tools installation creates consistent environments, though production might use Azure DevTest Labs or Virtual Desktop. Hybrid Solutions: VMs are common in hybrid scenarios needing on-premises compatibility with NSGs, private IPs, and VNets essential for hybrid connectivity. The exam tests architectural decision-making.

**Common exam questions** include: "You need to ensure a script runs after a Linux VM is created and completes before VM is ready" (Answer: Cloud-init runs during provisioning); "You need to install monitoring agents on 100 VMs efficiently" (Answer: VM extensions deployed at scale via ARM templates); "You need to debug connectivity issue without logging in" (Answer: Use run-command to execute diagnostic scripts). The exam tests choosing appropriate automation approaches.

We'll cover **key takeaways** (automation is essential, extensions vs run-commands understanding, security defaults to deny, NSG rules use priority, multiple automation options), **security best practices** (least privilege, explicit allow rules, monitoring access logs), and **exam preparation** focusing on automation principles that apply across all Azure compute services.

Master VM configuration automation for the AZ-204!
