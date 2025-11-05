# Azure Functions CI/CD - Quickfire Questions

## Question 1
Which deployment methods are supported for Azure Functions?


- A) FTP only
- B) Only manual upload
- C) Only Visual Studio
- D) ZIP deploy, Git, Docker, Azure DevOps

**Answer: D**
Functions support multiple deployment methods: ZIP deploy, Git, Docker containers, Azure DevOps, GitHub Actions, and more.
---
## Question 2
What is the recommended deployment method for production Functions?


- A) Edit in portal
- B) FTP
- C) ZIP deploy via CI/CD pipeline
- D) Manual file copy

**Answer: C**
ZIP deploy through automated CI/CD pipelines (Azure DevOps, GitHub Actions) is the recommended production deployment method.
---
## Question 3
What is Run-From-Package mode?


- A) Running functions from source code
- B) A debugging mode
- C) A testing feature
- D) Running functions directly from a ZIP package without extracting

**Answer: D**
Run-From-Package (WEBSITE_RUN_FROM_PACKAGE=1) mounts the ZIP file as read-only, improving cold start performance.
---
## Question 4
What are deployment slots used for in Azure Functions?


- A) Testing new versions before swapping to production
- B) Organizing code files
- C) Monitoring functions
- D) Storing backups

**Answer: A**
Deployment slots allow you to deploy and test new versions in a staging slot before swapping with production (Premium/Dedicated plans only).
---
## Question 5
Which Functions plan supports deployment slots?


- A) Free plan
- B) Premium and Dedicated (App Service) plans only
- C) All plans
- D) Consumption plan

**Answer: B**
Deployment slots are only available in Premium and Dedicated (App Service) plans, not Consumption plan.
---
## Question 6
What is the purpose of the FUNCTIONS_EXTENSION_VERSION setting?


- A) Sets API version
- B) Specifies storage version
- C) Controls scaling
- D) Specifies the Functions runtime version (e.g., ~4 for v4)

**Answer: D**
FUNCTIONS_EXTENSION_VERSION determines which Functions runtime version the app uses (~4, ~3, ~2, etc.).
---
## Question 7
How can you deploy Functions as containers?


- A) Only on virtual machines
- B) Only in Consumption plan
- C) Not supported
- D) Deploy Docker images to Premium or Dedicated plans, or container platforms like ACI/AKS

**Answer: D**
Functions can run in containers on Premium/Dedicated plans, Azure Container Instances, AKS, or any Docker-compatible platform.
---
## Question 8
What is the difference between in-process and isolated worker process models?


- A) In-process is deprecated
- B) In-process runs in same process as host; isolated runs in separate process with more flexibility
- C) No difference
- D) Isolated is slower

**Answer: B**
Isolated worker process runs functions in a separate process, supporting different .NET versions and middleware. In-process shares the host process.
---
## Question 9
Which file contains Function App settings that override local development settings?


- A) web.config
- B) Application Settings in Azure Portal (or CI/CD variables)
- C) function.json
- D) host.json

**Answer: B**
Application Settings in the portal (or set via CI/CD) override local.settings.json values from development.
---
## Question 10
What is blue-green deployment in Functions?


- A) Deploying new version to a slot (green), testing, then swapping with production (blue)
- B) A security feature
- C) A monitoring feature
- D) A color scheme

**Answer: A**
Blue-green deployment uses slots: production (blue) continues serving traffic while new version (green) is tested, then swapped.