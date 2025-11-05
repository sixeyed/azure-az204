# Azure Sign-in and Authentication - Quickfire Questions

## Question 1
What is Azure Active Directory (Azure AD / Microsoft Entra ID)?

- A) A storage service
- B) Cloud-based identity and access management service
- C) A database
- D) A virtual network

**Answer: B**
Azure AD provides identity services for authentication, authorization, SSO, and application access management.

---

## Question 2
What is the Azure CLI used for?

- A) Only monitoring
- B) Command-line tool for managing Azure resources
- C) Only billing
- D) Only networking

**Answer: B**
Azure CLI provides cross-platform commands for creating, managing, and automating Azure resources.

---

## Question 3
How do you sign in to Azure CLI?

- A) az login
- B) az signin
- C) az auth
- D) az connect

**Answer: A**
`az login` initiates browser-based or device code authentication to Azure AD.

---

## Question 4
What is a subscription in Azure?

- A) Newsletter subscription
- B) Logical container for resources with billing and access control boundary
- C) User account
- D) Resource group

**Answer: B**
Subscriptions are billing and access containers. Resources belong to subscriptions for cost tracking and management.

---

## Question 5
Can you have multiple subscriptions?

- A) No, only one per account
- B) Yes, for separating environments, departments, or billing
- C) Maximum 2
- D) Requires special permission

**Answer: B**
Organizations typically use multiple subscriptions for dev/test/prod separation, cost management, or organizational boundaries.

---

## Question 6
What is a service principal?

- A) The main Azure administrator
- B) An identity for applications to authenticate and access Azure resources
- C) A user account
- D) A resource group

**Answer: B**
Service principals are application identities for programmatic access, used in automation and CI/CD.

---

## Question 7
How do you set the default subscription in Azure CLI?

- A) az subscription set
- B) az account set --subscription <id>
- C) az default subscription
- D) az config subscription

**Answer: B**
`az account set --subscription <subscription-id>` sets the default subscription for subsequent commands.

---

## Question 8
What is the difference between authentication and authorization?

- A) Same thing
- B) Authentication verifies identity; authorization determines permissions
- C) Authorization is first
- D) No difference

**Answer: B**
Authentication proves "who you are." Authorization determines "what you can do."

---

## Question 9
What is multi-factor authentication (MFA)?

- A) Multiple passwords
- B) Additional verification beyond password (SMS, app, biometric)
- C) Using multiple accounts
- D) Complex passwords only

**Answer: B**
MFA requires 2+ verification factors (something you know + have/are) for enhanced security.

---

## Question 10
Can you use Azure CLI without a browser?

- A) No, browser required
- B) Yes, using device code flow for headless/SSH scenarios
- C) Only with GUI
- D) Not possible

**Answer: B**
Device code flow (`az login --use-device-code`) allows authentication on another device, useful for servers/containers.
