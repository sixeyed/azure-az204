# App Service - Quickfire Questions

## Question 1
What is the primary difference between IaaS and PaaS offerings in Azure?


- A) IaaS is more expensive than PaaS
- B) PaaS only supports Windows applications
- C) PaaS provides automatic platform management, while IaaS requires you to manage the underlying infrastructure
- D) IaaS cannot scale automatically

**Answer: C**
PaaS (Platform-as-a-Service) abstracts away infrastructure management, while IaaS (Infrastructure-as-a-Service) gives you control but requires you to manage VMs, OS, etc.
---
## Question 2
What is an Azure App Service Plan?


- A) A deployment script for your application
- B) A backup strategy for web apps
- C) An abstraction of the infrastructure resources needed to run App Service applications
- D) A monitoring dashboard for applications

**Answer: C**
The App Service Plan defines the compute resources (region, VM size, instance count) that your web apps will run on.
---
## Question 3
Which SKU would you choose for a production App Service that requires auto-scaling?


- A) Basic (B1)
- B) Free (F1)
- C) Shared (D1)
- D) Standard (S1) or higher

**Answer: D**
Auto-scaling is only available in Standard (S1) and Premium (P1) tiers. Basic and below do not support auto-scaling.
---

## Question 4
What deployment methods are supported by Azure App Service? (Choose all that apply)

- A) Local Git repository
- B) Docker containers
- C) GitHub Actions
- D) FTP

**Answer: All of the above (A, B, C, D)**
App Service supports multiple deployment methods including Git, Docker, CI/CD pipelines, FTP, and ZIP deploy.

---
## Question 5
When you create an App Service web app, what protocol is automatically enabled?


- A) HTTP only
- B) Both HTTP and HTTPS
- C) Neither, you must configure manually
- D) HTTPS only

**Answer: B**
Azure App Service automatically provides both HTTP and HTTPS endpoints with a platform-managed SSL certificate.
---
## Question 6
How many web apps can run on a single App Service Plan?


- A) Only one
- B) Up to 100
- C) Up to 10
- D) Multiple apps, limited only by the plan's resources

**Answer: D**
You can host multiple web apps on a single App Service Plan, sharing the compute resources of that plan.
---
## Question 7
What happens when you push code to an App Service configured for Git deployment?


- A) The code is only uploaded, you must manually build it
- B) Azure automatically builds and deploys the application
- C) The previous version is permanently deleted
- D) The app goes offline until you restart it

**Answer: B**
Azure App Service uses Kudu to automatically detect the project type, build the application, and deploy it when you push to the Git remote.
---
## Question 8
Which file system location persists across app restarts in App Service?


- A) /tmp directory
- B) Memory-based storage
- C) Application directory (wwwroot)
- D) None, all storage is ephemeral

**Answer: C**
The application directory (typically D:\home on Windows, /home on Linux) persists across restarts. Temporary directories do not.
---
## Question 9
What is the SCM URI used for in App Service?


- A) Configuring SSL certificates
- B) Accessing the Kudu console and deployment endpoints
- C) Setting up custom domains
- D) Monitoring application metrics

**Answer: B**
The SCM (Source Control Management) URI is used to access the Kudu service, which handles deployments, console access, and diagnostic tools.
---
## Question 10
How can you scale OUT an App Service?


- A) Add more instances to run your app (horizontal scaling)
- B) Compress the application code
- C) Deploy to multiple regions
- D) Increase the CPU and RAM of existing instances (vertical scaling)

**Answer: A**
Scaling OUT means horizontal scaling - adding more instances of your app. Scaling UP (A) would be increasing the size of instances (vertical scaling).