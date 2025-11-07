---
theme: default
background: https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Azure API Management
  Full-service API platform for AZ-204
drawings:
  persist: false
transition: slide-left
title: Azure API Management
mdc: true
---

# Azure API Management

Full-Service Platform for HTTP APIs

<div class="abs-bottom-10 left-10">
  <carbon-api class="text-8xl text-blue-400 opacity-80" />
</div>

---
layout: center
---

# Welcome to APIM

<v-click>

<div class="text-xl mt-8">
Explore Azure's most powerful service<br/>for managing and publishing HTTP APIs
</div>

</v-click>

---
layout: section
---

# What is API Management?

---

# APIM Overview

<v-click>

<div class="mt-4">
  <carbon-api class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Full-service solution for delivering HTTP APIs
</div>

</v-click>

<v-click>

<div class="mt-12 flex justify-center gap-12">
  <div class="text-center">
    <carbon-globe class="text-5xl text-green-400" />
    <div class="text-sm mt-3">Public APIs</div>
  </div>
  <div class="text-center">
    <carbon-enterprise class="text-5xl text-blue-400" />
    <div class="text-sm mt-3">Partner APIs</div>
  </div>
</div>

</v-click>

---

# Four Core Features

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-4xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-api class="text-3xl inline-block" />
    <span class="ml-3 text-lg">API Designer - Describe and version operations</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-4xl text-green-400 mt-1">2</div>
  <div>
    <carbon-network-4 class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Gateway - Route and modify traffic</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-4xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-portal class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Developer Portal - Self-service onboarding</span>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-4xl text-red-400 mt-1">4</div>
  <div>
    <carbon-security class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Security - Restrict API access</span>
  </div>
</div>

</v-click>

---

# Feature 1: API Designer

<v-click>

<div class="mt-4">
  <carbon-api class="text-6xl text-blue-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Centralized place to manage API definitions
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Designer[API Designer] --> API1[API v1.0]
    Designer --> API2[API v2.0]
    Designer --> API3[API v3.0]
    style Designer fill:#0078d4
    style API1 fill:#51cf66
    style API2 fill:#51cf66
    style API3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Describe operations and manage versions
</div>

</v-click>

---

# Feature 2: Gateway

<v-click>

<div class="mt-4">
  <carbon-network-4 class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Routes incoming traffic to backend hosts
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Client[API Client] --> Gateway[APIM Gateway]
    Gateway -->|Route| Backend1[Backend API 1]
    Gateway -->|Route| Backend2[Backend API 2]
    style Gateway fill:#51cf66
    style Backend1 fill:#0078d4
    style Backend2 fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Can modify requests and responses
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-sm opacity-70">
Incredible flexibility in handling API traffic
</div>

</v-click>

---

# Feature 3: Developer Portal

<v-click>

<div class="mt-4">
  <carbon-portal class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Self-service for API consumers
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Portal[Developer Portal] --> Discover[Discover APIs]
    Portal --> Signup[Sign Up]
    Portal --> Keys[Get Keys]
    style Portal fill:#ff6b6b
    style Discover fill:#51cf66
    style Signup fill:#51cf66
    style Keys fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg text-green-400">
Dramatically reduces administrative overhead
</div>

</v-click>

---

# Feature 4: Security

<v-click>

<div class="mt-4">
  <carbon-security class="text-6xl text-red-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Integrated security features
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Request[API Request] --> Auth{Authenticate}
    Auth -->|✓ Authorized| Backend[Backend API]
    Auth -->|❌ Denied| Block[403 Forbidden]
    style Auth fill:#ff6b6b
    style Backend fill:#51cf66
    style Block fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg">
Restrict access to authorized users only
</div>

</v-click>

---

# Important Note

<v-click>

<div class="mt-8">
  <carbon-time class="text-8xl text-orange-400" />
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
Creating an APIM instance can take<br/>60 minutes or more
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
💡 Kick off creation process in advance!
</div>

</v-click>

---
layout: section
---

# APIM Architecture

---

# Key URLs

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-4 class="text-4xl text-green-400" />
  <div>
    <div class="text-lg font-bold">Gateway URL</div>
    <div class="text-sm opacity-70">Where API consumers call</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings-adjust class="text-4xl text-blue-400" />
  <div>
    <div class="text-lg font-bold">Management URL</div>
    <div class="text-sm opacity-70">Programmatic configuration via REST</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-portal class="text-4xl text-purple-400" />
  <div>
    <div class="text-lg font-bold">Developer Portal URL</div>
    <div class="text-sm opacity-70">Where consumers discover and sign up</div>
  </div>
</div>

</v-click>

---

# Gateway: Where the Magic Happens

<v-click>

<div class="mt-8">

```mermaid
graph TB
    Client[API Client] --> Gateway[APIM Gateway]
    Gateway --> Rate[Rate Limiting]
    Gateway --> Auth[Authentication]
    Gateway --> Policy[Policy Enforcement]
    Gateway --> Route[Routing]
    Route --> Backend[Backend API]
    style Gateway fill:#0078d4
    style Backend fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
All the magic happens at the gateway
</div>

</v-click>

---
layout: section
---

# Core Concepts

---

# Three Core Concepts

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-4xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-api class="text-3xl inline-block" />
    <div class="ml-3 mt-2">
      <div class="text-lg font-bold">APIs</div>
      <div class="text-sm opacity-70">Collection of operations - can host multiple</div>
    </div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-4xl text-green-400 mt-1">2</div>
  <div>
    <carbon-product class="text-3xl inline-block" />
    <div class="ml-3 mt-2">
      <div class="text-lg font-bold">Products</div>
      <div class="text-sm opacity-70">Business units - pricing tiers, access levels</div>
    </div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8 flex items-start gap-4">
  <div class="text-4xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-user-multiple class="text-3xl inline-block" />
    <div class="ml-3 mt-2">
      <div class="text-lg font-bold">Subscriptions</div>
      <div class="text-sm opacity-70">Users signed up - unique keys for access</div>
    </div>
  </div>
</div>

</v-click>

---

# APIs

<v-click>

<div class="mt-8">

```mermaid
graph TB
    APIM[APIM Resource] --> API1[Products API]
    APIM --> API2[Orders API]
    APIM --> API3[Customers API]
    API1 --> Op1[GET /products]
    API1 --> Op2[POST /products]
    style APIM fill:#0078d4
    style API1 fill:#51cf66
    style API2 fill:#51cf66
    style API3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Host multiple APIs in one APIM resource
</div>

</v-click>

---

# Products

<v-click>

<div class="mt-8">

```mermaid
graph LR
    Products[Products] --> Free[Free Tier]
    Products --> Basic[Basic Tier]
    Products --> Premium[Premium Tier]
    Free -->|Access to| API1[Public APIs]
    Basic -->|Access to| API2[API1 + API2]
    Premium -->|Access to| API3[All APIs]
    style Products fill:#0078d4
    style Free fill:#51cf66
    style Basic fill:#ffd43b
    style Premium fill:#ff6b6b
```

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Products = Pricing tiers or access levels
</div>

</v-click>

---

# Subscriptions

<v-click>

<div class="mt-8">

```mermaid
graph TB
    User1[User 1] -->|Subscribes| Product[Product]
    User2[User 2] -->|Subscribes| Product
    User3[User 3] -->|Subscribes| Product
    Product --> Key1[Subscription Key 1]
    Product --> Key2[Subscription Key 2]
    Product --> Key3[Subscription Key 3]
    style Product fill:#0078d4
    style User1 fill:#51cf66
    style User2 fill:#51cf66
    style User3 fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Each subscription gets unique key
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
Identifies consumer and controls access
</div>

</v-click>

---
layout: section
---

# APIM Service Tiers

---

# Developer Tier

<v-click>

<div class="mt-4">
  <carbon-code class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 flex justify-center gap-16">
  <div class="text-center">
    <carbon-currency-dollar class="text-5xl text-green-400" />
    <div class="text-sm mt-3">~$0.07/hour</div>
  </div>
  <div class="text-center">
    <carbon-warning class="text-5xl text-red-400" />
    <div class="text-sm mt-3">No SLA</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Perfect for exploration and development
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-xl text-red-400">
Never use for production!
</div>

</v-click>

---

# Production Tiers

<v-click>

<div class="mt-6 grid grid-cols-2 gap-8">
  <div>
    <carbon-cloud class="text-5xl text-blue-400" />
    <div class="text-lg mt-3 font-bold">Consumption</div>
    <div class="text-sm mt-2">✓ Serverless</div>
    <div class="text-sm">✓ Pay per call</div>
    <div class="text-sm">✓ Auto-scaling</div>
  </div>
  <div>
    <carbon-enterprise class="text-5xl text-green-400" />
    <div class="text-lg mt-3 font-bold">Basic & Standard</div>
    <div class="text-sm mt-2">✓ SLA included</div>
    <div class="text-sm">✓ More capacity</div>
    <div class="text-sm">✓ Production-ready</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-8">
  <carbon-data-center class="text-5xl text-purple-400" />
  <div class="text-lg mt-3 font-bold">Premium</div>
  <div class="text-sm mt-2">✓ Multi-region deployment</div>
  <div class="text-sm">✓ VNet integration</div>
  <div class="text-sm">✓ High capacity</div>
  <div class="text-sm">✓ Enterprise scenarios</div>
</div>

</v-click>

---
layout: section
---

# Backend API Deployment

---

# Important Understanding

<v-click>

<div class="mt-8">
  <carbon-warning class="text-8xl text-orange-400" />
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
APIM is NOT a hosting service
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
You still need to deploy your API logic<br/>to another service
</div>

</v-click>

---

# APIM as Facade

<v-click>

<div class="mt-8">

```mermaid
graph LR
    Client[API Clients] --> APIM[APIM<br/>Facade/Proxy]
    APIM --> Backend[Backend API<br/>Actual Logic]
    style Client fill:#51cf66
    style APIM fill:#ff6b6b
    style Backend fill:#0078d4
```

</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl">
APIM works as a facade or proxy
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg opacity-70">
Add backend as backend service in APIM
</div>

</v-click>

---

# Backend Options

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-application-web class="text-4xl text-blue-400" />
  <span class="text-lg">Azure Web App</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-function class="text-4xl text-green-400" />
  <span class="text-lg">Function App</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-flow class="text-4xl text-purple-400" />
  <span class="text-lg">Logic App</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-url class="text-4xl text-orange-400" />
  <span class="text-lg">Custom URL (Azure, on-prem, other cloud)</span>
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg text-green-400">
Deploy anywhere, proxy through APIM
</div>

</v-click>

---
layout: section
---

# The Power of Policies

---

# APIM Policies

<v-click>

<div class="mt-4">
  <carbon-settings-adjust class="text-6xl text-purple-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Add inbound and outbound processing
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Request[Request] --> Inbound[Inbound<br/>Policies]
    Inbound --> Backend[Backend API]
    Backend --> Outbound[Outbound<br/>Policies]
    Outbound --> Response[Response]
    style Inbound fill:#51cf66
    style Backend fill:#0078d4
    style Outbound fill:#ff6b6b
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Wrap actual API logic with processing
</div>

</v-click>

---

# Policy Examples

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-data-storage class="text-3xl text-green-400" />
  <span>Cache responses to reduce backend load</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-location class="text-3xl text-blue-400" />
  <span>Filter requests based on IP address</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-data-enrichment class="text-3xl text-purple-400" />
  <span>Transform request and response payloads</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-data-1 class="text-3xl text-orange-400" />
  <span>Add headers, validate tokens</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-meter-alt class="text-3xl text-red-400" />
  <span>Enforce rate limits</span>
</div>

</v-click>

---

# The Best Part

<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Production-grade features
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Without writing any code in your backend API
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph TB
    Backend[Backend API] -->|Focus on| Logic[Business Logic]
    APIM[APIM Policies] -->|Handle| Infra[Infrastructure Concerns]
    style Backend fill:#51cf66
    style Logic fill:#51cf66
    style APIM fill:#0078d4
    style Infra fill:#0078d4
```

</div>

</v-click>

---
layout: section
---

# Developer Portal

---

# Self-Service Experience

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-search class="text-4xl text-blue-400" />
  <span class="text-lg">Browse APIs</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-document class="text-4xl text-green-400" />
  <span class="text-lg">Read documentation</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-user-follow class="text-4xl text-purple-400" />
  <span class="text-lg">Sign up for access</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-password class="text-4xl text-orange-400" />
  <span class="text-lg">Get subscription keys</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-play class="text-4xl text-red-400" />
  <span class="text-lg">Test APIs in browser</span>
</div>

</v-click>

---

# Fully Customizable

<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-paint-brush class="text-4xl text-blue-400" />
  <span class="text-lg">Add company branding</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-color-palette class="text-4xl text-green-400" />
  <span class="text-lg">Customize look and feel</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-identification class="text-4xl text-purple-400" />
  <span class="text-lg">Configure authentication options</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Hosted and managed by APIM service
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg opacity-70">
No additional infrastructure to maintain
</div>

</v-click>

---
layout: section
---

# OpenAPI Integration

---

# OpenAPI Support

<v-click>

<div class="mt-4">
  <carbon-api class="text-6xl text-green-400" />
</div>

</v-click>

<v-click>

<div class="mt-8 text-xl text-center">
Excellent support for OpenAPI specification
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-lg opacity-70">
(Formerly known as Swagger)
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Backend[Backend API] -->|Publishes| OpenAPI[OpenAPI Spec]
    OpenAPI -->|Import| APIM[APIM]
    APIM -->|Auto-Creates| Everything[Operations + Docs]
    style OpenAPI fill:#51cf66
    style APIM fill:#0078d4
    style Everything fill:#ffd43b
```

</div>

</v-click>

---

# Import Benefits

<v-click>

<div class="mt-8 text-center text-xl">
If backend publishes OpenAPI spec...
</div>

</v-click>

<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-download class="text-4xl text-blue-400" />
  <span class="text-lg">Import directly into APIM</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-magic-wand class="text-4xl text-purple-400" />
  <span class="text-lg">Automatically creates operations</span>
</div>

</v-click>

<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document class="text-4xl text-green-400" />
  <span class="text-lg">Imports parameters and documentation</span>
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Saves tons of manual work!
</div>

</v-click>

---
layout: section
---

# Production-Grade Features

---

# Out of the Box

<v-click>

<div class="mt-6 flex items-start gap-3">
  <carbon-meter-alt class="text-3xl text-blue-400 mt-1" />
  <div>
    <div class="font-bold">Rate limiting and quotas</div>
    <div class="text-sm opacity-70">Protect backends from overload</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-data-storage class="text-3xl text-green-400 mt-1" />
  <div>
    <div class="font-bold">Response caching</div>
    <div class="text-sm opacity-70">Improve performance, reduce load</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-password class="text-3xl text-purple-400 mt-1" />
  <div>
    <div class="font-bold">Subscription key management</div>
    <div class="text-sm opacity-70">Automatic generation and rotation</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-location class="text-3xl text-orange-400 mt-1" />
  <div>
    <div class="font-bold">IP filtering</div>
    <div class="text-sm opacity-70">Geographic restrictions</div>
  </div>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-data-enrichment class="text-3xl text-red-400 mt-1" />
  <div>
    <div class="font-bold">CORS, request transformation</div>
    <div class="text-sm opacity-70">All configuration, no code</div>
  </div>
</div>

</v-click>

---

# The Power

<v-click>

<div class="mt-12 text-center text-2xl">
Features that would take<br/>weeks or months to build yourself
</div>

</v-click>

<v-click>

<div class="mt-12 text-center text-3xl text-green-400">
All built-in
</div>

</v-click>

<v-click>

<div class="mt-12">

```mermaid
graph LR
    Simple[Simple Backend API] -->|APIM| Production[Production-Ready<br/>Secure, Scalable API]
    style Simple fill:#ffd43b
    style Production fill:#51cf66
```

</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
Just configuration - no code required
</div>

</v-click>

---
layout: section
---

# What's Next

---

# Lab Exercises

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-add class="text-3xl text-blue-400 mt-1" />
  <span>Creating an APIM instance</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-deploy class="text-3xl text-green-400 mt-1" />
  <span>Deploying a backend API</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-download class="text-3xl text-purple-400 mt-1" />
  <span>Importing API into APIM</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-settings-adjust class="text-3xl text-orange-400 mt-1" />
  <span>Configuring policies</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-portal class="text-3xl text-red-400 mt-1" />
  <span>Publishing through Developer Portal</span>
</div>

</v-click>

<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-play class="text-3xl text-blue-500 mt-1" />
  <span>Testing as API consumer</span>
</div>

</v-click>

---
layout: center
class: text-center
---

<div>

<v-click>

<carbon-coffee class="text-8xl text-brown-400 inline-block" />

</v-click>

<v-click>

<div class="text-3xl mt-8">
Remember: Start APIM creation early!
</div>

</v-click>

<v-click>

<div class="text-xl mt-6 opacity-70">
Grab a coffee while it provisions (60+ minutes)
</div>

</v-click>

<v-click>

<div class="mt-12">
<carbon-play-outline class="text-6xl text-green-400 inline-block" />
</div>

</v-click>

<v-click>

<div class="text-2xl mt-4 font-bold">
Then let's dive into hands-on work!
</div>

</v-click>

</div>
