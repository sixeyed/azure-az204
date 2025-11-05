# Web Applications on VMs - Quickfire Questions

## Question 1
When should you host web apps on VMs vs App Service?

- A) Always use VMs
- B) VMs for full control, legacy compatibility, custom OS; App Service for managed PaaS
- C) Always use App Service
- D) No difference

**Answer: B**
VMs provide flexibility but require management. App Service simplifies deployment and scaling.

---

## Question 2
What web servers can run on Azure VMs?

- A) Only IIS
- B) IIS, Apache, Nginx, Tomcat, Node.js, etc.
- C) Only Apache
- D) None

**Answer: B**
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

- A) No benefits
- B) Distributes traffic across multiple VMs for scalability and availability
- C) Only monitoring
- D) Only backup

**Answer: B**
Load balancers provide high availability and horizontal scaling for web applications.

---

## Question 5
Can you use SSL/TLS certificates on VMs?

- A) No, not supported
- B) Yes, install certificates and configure web server
- C) Only App Service
- D) Automatic only

**Answer: B**
Install certificates from Key Vault, Let's Encrypt, or other CAs and configure in web server.

---

## Question 6
What is the difference between public and private load balancer?

- A) Same thing
- B) Public has internet-facing IP; private has internal VNet IP
- C) Public is free
- D) Private is faster

**Answer: B**
Public for internet traffic, private for internal tier communication (web → app → database).

---

## Question 7
How do you update web apps on VMs?

- A) Delete and recreate
- B) Deploy new code, update configuration, restart services (manually or automated)
- C) Automatic only
- D) Not possible

**Answer: B**
Use CI/CD pipelines, deployment tools, or manual processes to update applications.

---

## Question 8
Can you use VM Scale Sets for web apps?

- A) No
- B) Yes, VMSS ideal for scalable web applications with auto-scaling
- C) Only manual VMs
- D) Not recommended

**Answer: B**
VMSS automatically scales web tier based on demand, similar to App Service scaling.

---

## Question 9
What monitoring is available for web apps on VMs?

- A) No monitoring
- B) Azure Monitor, Application Insights, web server logs, custom monitoring
- C) Only basic metrics
- D) Manual monitoring only

**Answer: B**
Comprehensive monitoring through Azure Monitor, Log Analytics, and application-level telemetry.

---

## Question 10
Do you need to patch/maintain VMs running web apps?

- A) No, fully managed
- B) Yes, OS updates, security patches, web server updates are your responsibility
- C) Automatic always
- D) Not needed

**Answer: B**
IaaS model means you manage patching, backups, and maintenance (unlike App Service PaaS).
