# App Service - Quickfire Questions

## Question 1
What is the primary difference between IaaS and PaaS offerings in Azure?

- A) IaaS is more expensive than PaaS
- B) PaaS provides automatic platform management, while IaaS requires you to manage the underlying infrastructure
- C) PaaS only supports Windows applications
- D) IaaS cannot scale automatically

**Answer: B**
PaaS (Platform-as-a-Service) abstracts away infrastructure management, while IaaS (Infrastructure-as-a-Service) gives you control but requires you to manage VMs, OS, etc.

---

## Question 2
What is an Azure App Service Plan?

- A) A deployment script for your application
- B) An abstraction of the infrastructure resources needed to run App Service applications
- C) A backup strategy for web apps
- D) A monitoring dashboard for applications

**Answer: B**
The App Service Plan defines the compute resources (region, VM size, instance count) that your web apps will run on.

---

## Question 3
Which SKU would you choose for a production App Service that requires auto-scaling?

- A) Free (F1)
- B) Shared (D1)
- C) Basic (B1)
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
- B) HTTPS only
- C) Both HTTP and HTTPS
- D) Neither, you must configure manually

**Answer: C**
Azure App Service automatically provides both HTTP and HTTPS endpoints with a platform-managed SSL certificate.

---

## Question 6
How many web apps can run on a single App Service Plan?

- A) Only one
- B) Up to 10
- C) Up to 100
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
- B) Application directory (wwwroot)
- C) Memory-based storage
- D) None, all storage is ephemeral

**Answer: B**
The application directory (typically D:\home on Windows, /home on Linux) persists across restarts. Temporary directories do not.

---

## Question 9
What is the SCM URI used for in App Service?

- A) Monitoring application metrics
- B) Accessing the Kudu console and deployment endpoints
- C) Configuring SSL certificates
- D) Setting up custom domains

**Answer: B**
The SCM (Source Control Management) URI is used to access the Kudu service, which handles deployments, console access, and diagnostic tools.

---

## Question 10
How can you scale OUT an App Service?

- A) Increase the CPU and RAM of existing instances (vertical scaling)
- B) Add more instances to run your app (horizontal scaling)
- C) Deploy to multiple regions
- D) Compress the application code

**Answer: B**
Scaling OUT means horizontal scaling - adding more instances of your app. Scaling UP (A) would be increasing the size of instances (vertical scaling).
