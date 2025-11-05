# Azure Functions CI/CD - Quickfire Questions

## Question 1
Which deployment methods are supported for Azure Functions?

- A) ZIP deploy, Git, Docker, Azure DevOps
- B) Only manual upload
- C) Only Visual Studio
- D) FTP only

**Answer: A**
Functions support multiple deployment methods: ZIP deploy, Git, Docker containers, Azure DevOps, GitHub Actions, and more.

---

## Question 2
What is the recommended deployment method for production Functions?

- A) FTP
- B) ZIP deploy via CI/CD pipeline
- C) Manual file copy
- D) Edit in portal

**Answer: B**
ZIP deploy through automated CI/CD pipelines (Azure DevOps, GitHub Actions) is the recommended production deployment method.

---

## Question 3
What is Run-From-Package mode?

- A) Running functions from source code
- B) Running functions directly from a ZIP package without extracting
- C) A debugging mode
- D) A testing feature

**Answer: B**
Run-From-Package (WEBSITE_RUN_FROM_PACKAGE=1) mounts the ZIP file as read-only, improving cold start performance.

---

## Question 4
What are deployment slots used for in Azure Functions?

- A) Organizing code files
- B) Testing new versions before swapping to production
- C) Storing backups
- D) Monitoring functions

**Answer: B**
Deployment slots allow you to deploy and test new versions in a staging slot before swapping with production (Premium/Dedicated plans only).

---

## Question 5
Which Functions plan supports deployment slots?

- A) Consumption plan
- B) All plans
- C) Premium and Dedicated (App Service) plans only
- D) Free plan

**Answer: C**
Deployment slots are only available in Premium and Dedicated (App Service) plans, not Consumption plan.

---

## Question 6
What is the purpose of the FUNCTIONS_EXTENSION_VERSION setting?

- A) Specifies storage version
- B) Specifies the Functions runtime version (e.g., ~4 for v4)
- C) Sets API version
- D) Controls scaling

**Answer: B**
FUNCTIONS_EXTENSION_VERSION determines which Functions runtime version the app uses (~4, ~3, ~2, etc.).

---

## Question 7
How can you deploy Functions as containers?

- A) Not supported
- B) Deploy Docker images to Premium or Dedicated plans, or container platforms like ACI/AKS
- C) Only on virtual machines
- D) Only in Consumption plan

**Answer: B**
Functions can run in containers on Premium/Dedicated plans, Azure Container Instances, AKS, or any Docker-compatible platform.

---

## Question 8
What is the difference between in-process and isolated worker process models?

- A) No difference
- B) In-process runs in same process as host; isolated runs in separate process with more flexibility
- C) Isolated is slower
- D) In-process is deprecated

**Answer: B**
Isolated worker process runs functions in a separate process, supporting different .NET versions and middleware. In-process shares the host process.

---

## Question 9
Which file contains Function App settings that override local development settings?

- A) function.json
- B) host.json
- C) Application Settings in Azure Portal (or CI/CD variables)
- D) web.config

**Answer: C**
Application Settings in the portal (or set via CI/CD) override local.settings.json values from development.

---

## Question 10
What is blue-green deployment in Functions?

- A) A color scheme
- B) Deploying new version to a slot (green), testing, then swapping with production (blue)
- C) A monitoring feature
- D) A security feature

**Answer: B**
Blue-green deployment uses slots: production (blue) continues serving traffic while new version (green) is tested, then swapped.
