# Azure API Management (APIM) - Quickfire Questions

## Question 1
What is Azure API Management?


- A) A storage service
- B) A fully managed service for publishing, securing, transforming, and monitoring APIs
- C) A compute service
- D) A database service

**Answer: B**
APIM acts as a gateway between API consumers and backend services, providing management, security, and analytics.
---
## Question 2
What are the main components of APIM?


- A) Only portal
- B) Gateway, Developer Portal, Management Plane
- C) Only gateway
- D) Only policies

**Answer: B**
APIM consists of API Gateway (handles requests), Developer Portal (documentation), and Management Plane (configuration).
---
## Question 3
What are APIM service tiers?


- A) One tier only
- B) Small and Large
- C) Consumption, Developer, Basic, Standard, Premium
- D) Free only

**Answer: C**
Consumption (serverless), Developer (non-production), Basic/Standard (production), Premium (multi-region, VNet).
---
## Question 4
What is the purpose of the Developer Portal?


- A) Admin dashboard only
- B) Monitoring tool
- C) Code editor
- D) Self-service portal for API consumers to discover, learn, and subscribe to APIs

**Answer: D**
Developer Portal provides API documentation, interactive console, subscription management for developers.
---
## Question 5
What are products in APIM?


- A) Server products
- B) Physical goods
- C) Database products
- D) Groupings of APIs with access control, quotas, and terms of use

**Answer: D**
Products bundle APIs together with policies, visibility settings, and subscription requirements.
---
## Question 6
What is a subscription key?


- A) Encryption key
- B) Newsletter subscription
- C) Database connection
- D) Authentication credential for accessing APIs published through APIM

**Answer: D**
Subscription keys authenticate API requests. Required unless explicitly bypassed in product/API settings.
---
## Question 7
What is the difference between subscription scopes?


- A) No scopes
- B) All APIs, Product, or Single API scope controls access breadth
- C) Only API scope
- D) Only global scope

**Answer: B**
Subscriptions can grant access to all APIs, a specific product, or a single API depending on requirements.
---
## Question 8
Can APIM transform requests and responses?


- A) No transformation
- B) Only routing
- C) Yes, using policies to modify headers, body, query parameters
- D) Only logging

**Answer: C**
APIM policies can transform requests/responses, including XML/JSON conversion, header manipulation, and content rewriting.
---
## Question 9
What backends can APIM proxy?


- A) Only App Service
- B) Only Azure services
- C) Only Functions
- D) Any HTTP/HTTPS endpoint (Azure, on-premises, other clouds)

**Answer: D**
APIM can front any HTTP/HTTPS backend regardless of location: Azure services, on-premises APIs, third-party APIs.
---
## Question 10
What is self-hosted gateway?


- A) On-premises APIM instance
- B) A separate service
- C) Not available
- D) Containerized gateway component deployable to on-premises or other clouds

**Answer: D**
Self-hosted gateway extends APIM to on-premises and multi-cloud environments while managing centrally in Azure.