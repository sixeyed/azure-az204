# Web Applications on VMs - Quickfire Questions

## Question 1
When should you host web apps on VMs vs App Service?


- A) Always use VMs
- B) No difference
- C) Always use App Service
- D) VMs for full control, legacy compatibility, custom OS; App Service for managed PaaS

**Answer: D**
VMs provide flexibility but require management. App Service simplifies deployment and scaling.
---
## Question 2
What web servers can run on Azure VMs?


- A) IIS, Apache, Nginx, Tomcat, Node.js, etc.
- B) Only Apache
- C) Only IIS
- D) None

**Answer: A**
Any web server compatible with Windows or Linux can run on Azure VMs.
---
## Question 3
How do you expose web apps on VMs to the internet?


- A) Automatic
- B) Assign public IP, configure NSG to allow HTTP/HTTPS, optionally use load balancer
- C) Not possible
- D) Only VPN

**Answer: B**
Public IP for direct access, or use Load Balancer/Application Gateway for production scenarios.
---
## Question 4
What is the benefit of using load balancer with web VMs?


- A) Distributes traffic across multiple VMs for scalability and availability
- B) Only monitoring
- C) Only backup
- D) No benefits

**Answer: A**
Load balancers provide high availability and horizontal scaling for web applications.
---
## Question 5
Can you use SSL/TLS certificates on VMs?


- A) Only App Service
- B) Yes, install certificates and configure web server
- C) Automatic only
- D) No, not supported

**Answer: B**
Install certificates from Key Vault, Let's Encrypt, or other CAs and configure in web server.
---
## Question 6
What is the difference between public and private load balancer?


- A) Public has internet-facing IP; private has internal VNet IP
- B) Same thing
- C) Public is free
- D) Private is faster

**Answer: A**
Public for internet traffic, private for internal tier communication (web → app → database).
---
## Question 7
How do you update web apps on VMs?


- A) Delete and recreate
- B) Deploy new code, update configuration, restart services (manually or automated)
- C) Not possible
- D) Automatic only

**Answer: B**
Use CI/CD pipelines, deployment tools, or manual processes to update applications.
---
## Question 8
Can you use VM Scale Sets for web apps?


- A) Only manual VMs
- B) No
- C) Not recommended
- D) Yes, VMSS ideal for scalable web applications with auto-scaling

**Answer: D**
VMSS automatically scales web tier based on demand, similar to App Service scaling.
---
## Question 9
What monitoring is available for web apps on VMs?


- A) Manual monitoring only
- B) No monitoring
- C) Azure Monitor, Application Insights, web server logs, custom monitoring
- D) Only basic metrics

**Answer: C**
Comprehensive monitoring through Azure Monitor, Log Analytics, and application-level telemetry.
---
## Question 10
Do you need to patch/maintain VMs running web apps?


- A) Yes, OS updates, security patches, web server updates are your responsibility
- B) No, fully managed
- C) Not needed
- D) Automatic always

**Answer: A**
IaaS model means you manage patching, backups, and maintenance (unlike App Service PaaS).