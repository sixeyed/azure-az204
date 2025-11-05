# Azure API Management (APIM) - Quickfire Questions

## Question 1
What is Azure API Management?

- A) A database service
- B) A fully managed service for publishing, securing, transforming, and monitoring APIs
- C) A storage service
- D) A compute service

**Answer: B**
APIM acts as a gateway between API consumers and backend services, providing management, security, and analytics.

---

## Question 2
What are the main components of APIM?

- A) Only gateway
- B) Gateway, Developer Portal, Management Plane
- C) Only portal
- D) Only policies

**Answer: B**
APIM consists of API Gateway (handles requests), Developer Portal (documentation), and Management Plane (configuration).

---

## Question 3
What are APIM service tiers?

- A) Free only
- B) Consumption, Developer, Basic, Standard, Premium
- C) Small and Large
- D) One tier only

**Answer: B**
Consumption (serverless), Developer (non-production), Basic/Standard (production), Premium (multi-region, VNet).

---

## Question 4
What is the purpose of the Developer Portal?

- A) Code editor
- B) Self-service portal for API consumers to discover, learn, and subscribe to APIs
- C) Admin dashboard only
- D) Monitoring tool

**Answer: B**
Developer Portal provides API documentation, interactive console, subscription management for developers.

---

## Question 5
What are products in APIM?

- A) Physical goods
- B) Groupings of APIs with access control, quotas, and terms of use
- C) Database products
- D) Server products

**Answer: B**
Products bundle APIs together with policies, visibility settings, and subscription requirements.

---

## Question 6
What is a subscription key?

- A) Newsletter subscription
- B) Authentication credential for accessing APIs published through APIM
- C) Encryption key
- D) Database connection

**Answer: B**
Subscription keys authenticate API requests. Required unless explicitly bypassed in product/API settings.

---

## Question 7
What is the difference between subscription scopes?

- A) No scopes
- B) All APIs, Product, or Single API scope controls access breadth
- C) Only global scope
- D) Only API scope

**Answer: B**
Subscriptions can grant access to all APIs, a specific product, or a single API depending on requirements.

---

## Question 8
Can APIM transform requests and responses?

- A) No transformation
- B) Yes, using policies to modify headers, body, query parameters
- C) Only routing
- D) Only logging

**Answer: B**
APIM policies can transform requests/responses, including XML/JSON conversion, header manipulation, and content rewriting.

---

## Question 9
What backends can APIM proxy?

- A) Only Azure services
- B) Any HTTP/HTTPS endpoint (Azure, on-premises, other clouds)
- C) Only App Service
- D) Only Functions

**Answer: B**
APIM can front any HTTP/HTTPS backend regardless of location: Azure services, on-premises APIs, third-party APIs.

---

## Question 10
What is self-hosted gateway?

- A) On-premises APIM instance
- B) Containerized gateway component deployable to on-premises or other clouds
- C) A separate service
- D) Not available

**Answer: B**
Self-hosted gateway extends APIM to on-premises and multi-cloud environments while managing centrally in Azure.
