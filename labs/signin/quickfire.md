# Azure Sign-in and Authentication - Quickfire Questions

## Question 1
What is Azure Active Directory (Azure AD / Microsoft Entra ID)?


- A) A virtual network
- B) Cloud-based identity and access management service
- C) A storage service
- D) A database

**Answer: B**
Azure AD provides identity services for authentication, authorization, SSO, and application access management.
---
## Question 2
What is the Azure CLI used for?


- A) Only monitoring
- B) Only billing
- C) Command-line tool for managing Azure resources
- D) Only networking

**Answer: C**
Azure CLI provides cross-platform commands for creating, managing, and automating Azure resources.
---
## Question 3
How do you sign in to Azure CLI?


- A) az connect
- B) az login
- C) az auth
- D) az signin

**Answer: B**
`az login` initiates browser-based or device code authentication to Azure AD.
---
## Question 4
What is a subscription in Azure?


- A) Newsletter subscription
- B) Resource group
- C) Logical container for resources with billing and access control boundary
- D) User account

**Answer: C**
Subscriptions are billing and access containers. Resources belong to subscriptions for cost tracking and management.
---
## Question 5
Can you have multiple subscriptions?


- A) Maximum 2
- B) No, only one per account
- C) Yes, for separating environments, departments, or billing
- D) Requires special permission

**Answer: C**
Organizations typically use multiple subscriptions for dev/test/prod separation, cost management, or organizational boundaries.
---
## Question 6
What is a service principal?


- A) A resource group
- B) The main Azure administrator
- C) An identity for applications to authenticate and access Azure resources
- D) A user account

**Answer: C**
Service principals are application identities for programmatic access, used in automation and CI/CD.
---
## Question 7
How do you set the default subscription in Azure CLI?


- A) az account set --subscription <id>
- B) az subscription set
- C) az config subscription
- D) az default subscription

**Answer: A**
`az account set --subscription <subscription-id>` sets the default subscription for subsequent commands.
---
## Question 8
What is the difference between authentication and authorization?


- A) No difference
- B) Authorization is first
- C) Authentication verifies identity; authorization determines permissions
- D) Same thing

**Answer: C**
Authentication proves "who you are." Authorization determines "what you can do."
---
## Question 9
What is multi-factor authentication (MFA)?


- A) Using multiple accounts
- B) Complex passwords only
- C) Multiple passwords
- D) Additional verification beyond password (SMS, app, biometric)

**Answer: D**
MFA requires 2+ verification factors (something you know + have/are) for enhanced security.
---
## Question 10
Can you use Azure CLI without a browser?


- A) Yes, using device code flow for headless/SSH scenarios
- B) Not possible
- C) No, browser required
- D) Only with GUI

**Answer: A**
Device code flow (`az login --use-device-code`) allows authentication on another device, useful for servers/containers.