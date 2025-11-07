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

<!--
METADATA:
sentence: In this session, we'll explore one of Azure's most powerful services for managing and publishing HTTP APIs.
search_anchor: this session, we'll explore one
-->
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

<!--
METADATA:
sentence: Think of it as a full-service solution for delivering HTTP APIs to your consumers - whether that's a public API available to everyone, or an external API for your business partners.
search_anchor: Think of it as a
-->
<v-click>

<div class="mt-8 text-xl text-center">
Full-service solution for delivering HTTP APIs
</div>

</v-click>

<!--
METADATA:
sentence: It provides a self-service experience for your API consumers.
search_anchor: It provides a self-service experience
-->
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

<!--
METADATA:
sentence: APIM gives you four core features that make it incredibly valuable: First, there's an API designer where you can describe and version your API's operations.
search_anchor: APIM gives you four core
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-4xl text-blue-400 mt-1">1</div>
  <div>
    <carbon-api class="text-3xl inline-block" />
    <span class="ml-3 text-lg">API Designer - Describe and version operations</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Second, you have a gateway that routes incoming traffic to your backend API hosts.
search_anchor: Second, you have a gateway
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-4xl text-green-400 mt-1">2</div>
  <div>
    <carbon-network-4 class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Gateway - Route and modify traffic</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Developer Portal The Developer Portal is another standout feature.
search_anchor: Developer Portal The Developer Portal
-->
<v-click>

<div class="mt-6 flex items-start gap-4">
  <div class="text-4xl text-purple-400 mt-1">3</div>
  <div>
    <carbon-portal class="text-3xl inline-block" />
    <span class="ml-3 text-lg">Developer Portal - Self-service onboarding</span>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: So, what exactly is API Management?
search_anchor: So, what exactly is API
-->
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

<!--
METADATA:
sentence: This gives you a centralized place to manage all your API definitions.
search_anchor: This gives you a centralized
-->
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

<!--
METADATA:
sentence: Subscription key management with automatic generation and rotation?
search_anchor: Subscription key management with automatic
-->
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

<!--
METADATA:
sentence: Second, you have a gateway that routes incoming traffic to your backend API hosts.
search_anchor: Second, you have a gateway
-->
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

<!--
METADATA:
sentence: You can transform request and response payloads.
search_anchor: You can transform request and
-->
<v-click>

<div class="mt-8 text-center text-lg">
Can modify requests and responses
</div>

</v-click>

<!--
METADATA:
sentence: The gateway can also modify both requests and responses, giving you incredible flexibility in how you handle API traffic.
search_anchor: gateway can also modify both
-->
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

<!--
METADATA:
sentence: It provides a self-service experience for your API consumers.
search_anchor: It provides a self-service experience
-->
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

<!--
METADATA:
sentence: This self-service approach dramatically reduces the administrative overhead of managing API consumers.
search_anchor: This self-service approach dramatically reduces
-->
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

<!--
METADATA:
sentence: And fourth, you get integrated security features to restrict API access, ensuring that only authorized users can call your APIs.
search_anchor: fourth, you get integrated security
-->
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

<!--
METADATA:
sentence: And fourth, you get integrated security features to restrict API access, ensuring that only authorized users can call your APIs.
search_anchor: fourth, you get integrated security
-->
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

<!--
METADATA:
sentence: But before we dive deep, there's something important you need to know: creating an instance of the API Management service can take 60 minutes or more.
search_anchor: But before we dive deep
-->
<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
Creating an APIM instance can take<br/>60 minutes or more
</div>

</v-click>

<!--
METADATA:
sentence: So you might want to kick off that creation process in advance if you're planning to work through these labs.
search_anchor: So you might want to
-->
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

<!--
METADATA:
sentence: When you create an APIM instance, you get several key URLs: The gateway URL is the endpoint that your API consumers will call.
search_anchor: When you create an APIM
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-network-4 class="text-4xl text-green-400" />
  <div>
    <div class="text-lg font-bold">Gateway URL</div>
    <div class="text-sm opacity-70">Where API consumers call</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: The management URL is for programmatic configuration of your APIM instance using the REST API.
search_anchor: management URL is for programmatic
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-settings-adjust class="text-4xl text-blue-400" />
  <div>
    <div class="text-lg font-bold">Management URL</div>
    <div class="text-sm opacity-70">Programmatic configuration via REST</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: And the developer portal URL is where your API consumers go to discover your APIs, sign up for access, and get their subscription keys.
search_anchor: developer portal URL is where
-->
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

<!--
METADATA:
sentence: This is where all the magic happens - rate limiting, authentication, policy enforcement, and routing to backends.
search_anchor: This is where all the
-->
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

<!--
METADATA:
sentence: Each API represents a collection of operations that work together.
search_anchor: Each API represents a collection
-->
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

<!--
METADATA:
sentence: Think of products as your pricing tiers or access levels.
search_anchor: Think of products as your
-->
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

<!--
METADATA:
sentence: Third, Subscriptions - these show you the users who have signed up for your products.
search_anchor: Third, Subscriptions - these show
-->
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

<!--
METADATA:
sentence: Core Concepts There are three core concepts you need to understand in APIM: First, APIs - you can host multiple APIs in one APIM resource.
search_anchor: Core Concepts There are three
-->
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

<!--
METADATA:
sentence: Think of products as your pricing tiers or access levels.
search_anchor: Think of products as your
-->
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

<!--
METADATA:
sentence: Each subscription gets a unique key that identifies the consumer and controls their access.
search_anchor: Each subscription gets a unique
-->
<v-click>

<div class="mt-8 text-center text-xl">
Each subscription gets unique key
</div>

</v-click>

<!--
METADATA:
sentence: Each subscription gets a unique key that identifies the consumer and controls their access.
search_anchor: Each subscription gets a unique
-->
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

<!--
METADATA:
sentence: However, there's no SLA, so you absolutely cannot use it for production environments.
search_anchor: However, there's no SLA, so
-->
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

<!--
METADATA:
sentence: It's cheap to run - currently about seven cents per hour - and is fine for exploration and development.
search_anchor: It's cheap to run -
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Perfect for exploration and development
</div>

</v-click>

<!--
METADATA:
sentence: For production, you have several options.
search_anchor: production, you have several options
-->
<v-click>

<div class="mt-6 text-center text-xl text-red-400">
Never use for production!
</div>

</v-click>

---

# Production Tiers

<!--
METADATA:
sentence: The Consumption tier is serverless and you pay per call, with auto-scaling built in.
search_anchor: Consumption tier is serverless and
-->
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

<!--
METADATA:
sentence: And the Premium tier is for enterprise scenarios with multi-region deployment, VNet integration, and high capacity.
search_anchor: Premium tier is for enterprise
-->
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

<!--
METADATA:
sentence: This is why API Management is such a powerful service.
search_anchor: This is why API Management
-->
<v-click>

<div class="mt-12 text-center text-2xl text-red-400">
APIM is NOT a hosting service
</div>

</v-click>

<!--
METADATA:
sentence: You still need to deploy your actual API logic to another service inside or outside of Azure.
search_anchor: You still need to deploy
-->
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

<!--
METADATA:
sentence: APIM works as a facade or proxy in front of your backend APIs.
search_anchor: APIM works as a facade
-->
<v-click>

<div class="mt-12 text-center text-xl">
APIM works as a facade or proxy
</div>

</v-click>

<!--
METADATA:
sentence: You add your backend as a backend service in APIM, so the gateway knows where to route incoming calls.
search_anchor: You add your backend as
-->
<v-click>

<div class="mt-6 text-center text-lg opacity-70">
Add backend as backend service in APIM
</div>

</v-click>

---

# Backend Options

<!--
METADATA:
sentence: What is API Management?
search_anchor: What is API Management
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-application-web class="text-4xl text-blue-400" />
  <span class="text-lg">Azure Web App</span>
</div>

</v-click>

<!--
METADATA:
sentence: For production, you have several options.
search_anchor: production, you have several options
-->
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

<!--
METADATA:
sentence: Your backend could be an Azure Web App, a Function App, a Logic App, or even a custom URL pointing to infrastructure running anywhere - in Azure, on-premises, or in another cloud.
search_anchor: Your backend could be an
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-url class="text-4xl text-orange-400" />
  <span class="text-lg">Custom URL (Azure, on-prem, other cloud)</span>
</div>

</v-click>

<!--
METADATA:
sentence: APIM works as a facade or proxy in front of your backend APIs.
search_anchor: APIM works as a facade
-->
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

<!--
METADATA:
sentence: Policies allow you to add inbound and outbound processing to wrap the actual logic of your API.
search_anchor: Policies allow you to add
-->
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

<!--
METADATA:
sentence: Policies allow you to add inbound and outbound processing to wrap the actual logic of your API.
search_anchor: Policies allow you to add
-->
<v-click>

<div class="mt-8 text-center text-lg opacity-70">
Wrap actual API logic with processing
</div>

</v-click>

---

# Policy Examples

<!--
METADATA:
sentence: For example, you can cache responses to reduce load on your backend.
search_anchor: example, you can cache responses
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-data-storage class="text-3xl text-green-400" />
  <span>Cache responses to reduce backend load</span>
</div>

</v-click>

<!--
METADATA:
sentence: You can filter requests based on IP address to implement geographical restrictions or admin-only endpoints.
search_anchor: You can filter requests based
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-location class="text-3xl text-blue-400" />
  <span>Filter requests based on IP address</span>
</div>

</v-click>

<!--
METADATA:
sentence: You can transform request and response payloads.
search_anchor: You can transform request and
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-data-enrichment class="text-3xl text-purple-400" />
  <span>Transform request and response payloads</span>
</div>

</v-click>

<!--
METADATA:
sentence: You can add headers, validate tokens, enforce rate limits - the list goes on.
search_anchor: You can add headers, validate
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-data-1 class="text-3xl text-orange-400" />
  <span>Add headers, validate tokens</span>
</div>

</v-click>

<!--
METADATA:
sentence: You can add headers, validate tokens, enforce rate limits - the list goes on.
search_anchor: You can add headers, validate
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-meter-alt class="text-3xl text-red-400" />
  <span>Enforce rate limits</span>
</div>

</v-click>

---

# The Best Part

<!--
METADATA:
sentence: For production, you have several options.
search_anchor: production, you have several options
-->
<v-click>

<div class="mt-12 text-center text-2xl text-green-400">
Production-grade features
</div>

</v-click>

<!--
METADATA:
sentence: And here's the best part: you get all of these production-grade features without having to write any code in your backend API.
search_anchor: here's the best part: you
-->
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

<!--
METADATA:
sentence: A product gives them access to one or more APIs.
search_anchor: product gives them access to
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-search class="text-4xl text-blue-400" />
  <span class="text-lg">Browse APIs</span>
</div>

</v-click>

<!--
METADATA:
sentence: They can browse your APIs, read documentation, sign up for access, get subscription keys, and even test APIs directly in the browser.
search_anchor: They can browse your APIs
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-document class="text-4xl text-green-400" />
  <span class="text-lg">Read documentation</span>
</div>

</v-click>

<!--
METADATA:
sentence: Think of products as your pricing tiers or access levels.
search_anchor: Think of products as your
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-user-follow class="text-4xl text-purple-400" />
  <span class="text-lg">Sign up for access</span>
</div>

</v-click>

<!--
METADATA:
sentence: Subscription key management with automatic generation and rotation?
search_anchor: Subscription key management with automatic
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-password class="text-4xl text-orange-400" />
  <span class="text-lg">Get subscription keys</span>
</div>

</v-click>

<!--
METADATA:
sentence: They can browse your APIs, read documentation, sign up for access, get subscription keys, and even test APIs directly in the browser.
search_anchor: They can browse your APIs
-->
<v-click>

<div class="mt-4 flex items-center gap-4">
  <carbon-play class="text-4xl text-red-400" />
  <span class="text-lg">Test APIs in browser</span>
</div>

</v-click>

---

# Fully Customizable

<!--
METADATA:
sentence: The portal is fully customizable - you can add your company branding, customize the look and feel, and configure authentication options.
search_anchor: portal is fully customizable -
-->
<v-click>

<div class="mt-8 flex items-center gap-4">
  <carbon-paint-brush class="text-4xl text-blue-400" />
  <span class="text-lg">Add company branding</span>
</div>

</v-click>

<!--
METADATA:
sentence: The portal is fully customizable - you can add your company branding, customize the look and feel, and configure authentication options.
search_anchor: portal is fully customizable -
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-color-palette class="text-4xl text-green-400" />
  <span class="text-lg">Customize look and feel</span>
</div>

</v-click>

<!--
METADATA:
sentence: The portal is fully customizable - you can add your company branding, customize the look and feel, and configure authentication options.
search_anchor: portal is fully customizable -
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-user-identification class="text-4xl text-purple-400" />
  <span class="text-lg">Configure authentication options</span>
</div>

</v-click>

<!--
METADATA:
sentence: And all of this is hosted and managed by the APIM service itself, so there's no additional infrastructure for you to maintain.
search_anchor: all of this is hosted
-->
<v-click>

<div class="mt-12 text-center text-xl text-green-400">
Hosted and managed by APIM service
</div>

</v-click>

<!--
METADATA:
sentence: And all of this is hosted and managed by the APIM service itself, so there's no additional infrastructure for you to maintain.
search_anchor: all of this is hosted
-->
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

<!--
METADATA:
sentence: OpenAPI Integration APIM has excellent support for the OpenAPI specification, formerly known as Swagger.
search_anchor: OpenAPI Integration APIM has excellent
-->
<v-click>

<div class="mt-8 text-xl text-center">
Excellent support for OpenAPI specification
</div>

</v-click>

<!--
METADATA:
sentence: OpenAPI Integration APIM has excellent support for the OpenAPI specification, formerly known as Swagger.
search_anchor: OpenAPI Integration APIM has excellent
-->
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

<!--
METADATA:
sentence: If your backend API already publishes an OpenAPI spec, you can import it directly into APIM.
search_anchor: If your backend API already
-->
<v-click>

<div class="mt-8 text-center text-xl">
If backend publishes OpenAPI spec...
</div>

</v-click>

<!--
METADATA:
sentence: If your backend API already publishes an OpenAPI spec, you can import it directly into APIM.
search_anchor: If your backend API already
-->
<v-click>

<div class="mt-12 flex items-center gap-4">
  <carbon-download class="text-4xl text-blue-400" />
  <span class="text-lg">Import directly into APIM</span>
</div>

</v-click>

<!--
METADATA:
sentence: This automatically creates all the operations, parameters, and documentation in APIM, saving you a ton of manual work.
search_anchor: This automatically creates all the
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-magic-wand class="text-4xl text-purple-400" />
  <span class="text-lg">Automatically creates operations</span>
</div>

</v-click>

<!--
METADATA:
sentence: This automatically creates all the operations, parameters, and documentation in APIM, saving you a ton of manual work.
search_anchor: This automatically creates all the
-->
<v-click>

<div class="mt-6 flex items-center gap-4">
  <carbon-document class="text-4xl text-green-400" />
  <span class="text-lg">Imports parameters and documentation</span>
</div>

</v-click>

<!--
METADATA:
sentence: Each API represents a collection of operations that work together.
search_anchor: Each API represents a collection
-->
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

<!--
METADATA:
sentence: Rate limiting and quotas to protect your backends from overload?
search_anchor: Rate limiting and quotas to
-->
<v-click>

<div class="mt-6 flex items-start gap-3">
  <carbon-meter-alt class="text-3xl text-blue-400 mt-1" />
  <div>
    <div class="font-bold">Rate limiting and quotas</div>
    <div class="text-sm opacity-70">Protect backends from overload</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Response caching to improve performance and reduce backend load?
search_anchor: Response caching to improve performance
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-data-storage class="text-3xl text-green-400 mt-1" />
  <div>
    <div class="font-bold">Response caching</div>
    <div class="text-sm opacity-70">Improve performance, reduce load</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: Subscription key management with automatic generation and rotation?
search_anchor: Subscription key management with automatic
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-password class="text-3xl text-purple-400 mt-1" />
  <div>
    <div class="font-bold">Subscription key management</div>
    <div class="text-sm opacity-70">Automatic generation and rotation</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: IP filtering, CORS support, request transformation?
search_anchor: IP filtering, CORS support, request
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-location class="text-3xl text-orange-400 mt-1" />
  <div>
    <div class="font-bold">IP filtering</div>
    <div class="text-sm opacity-70">Geographic restrictions</div>
  </div>
</div>

</v-click>

<!--
METADATA:
sentence: IP filtering, CORS support, request transformation?
search_anchor: IP filtering, CORS support, request
-->
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

<!--
METADATA:
sentence: Production-Grade Features Out of the Box Let me emphasize something important: APIM gives you production-grade features that would take weeks or months to build yourself.
search_anchor: Production-Grade Features Out of the
-->
<v-click>

<div class="mt-12 text-center text-2xl">
Features that would take<br/>weeks or months to build yourself
</div>

</v-click>

<!--
METADATA:
sentence: This gives you a centralized place to manage all your API definitions.
search_anchor: This gives you a centralized
-->
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

<!--
METADATA:
sentence: You can take a simple backend API and transform it into a production-ready, secure, scalable API service with just configuration - no code required.
search_anchor: You can take a simple
-->
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

<!--
METADATA:
sentence: The management URL is for programmatic configuration of your APIM instance using the REST API.
search_anchor: management URL is for programmatic
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-add class="text-3xl text-blue-400 mt-1" />
  <span>Creating an APIM instance</span>
</div>

</v-click>

<!--
METADATA:
sentence: APIM works as a facade or proxy in front of your backend APIs.
search_anchor: APIM works as a facade
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-deploy class="text-3xl text-green-400 mt-1" />
  <span>Deploying a backend API</span>
</div>

</v-click>

<!--
METADATA:
sentence: What is API Management?
search_anchor: What is API Management
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-download class="text-3xl text-purple-400 mt-1" />
  <span>Importing API into APIM</span>
</div>

</v-click>

<!--
METADATA:
sentence: IP filtering, CORS support, request transformation?
search_anchor: IP filtering, CORS support, request
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-settings-adjust class="text-3xl text-orange-400 mt-1" />
  <span>Configuring policies</span>
</div>

</v-click>

<!--
METADATA:
sentence: Developer Portal The Developer Portal is another standout feature.
search_anchor: Developer Portal The Developer Portal
-->
<v-click>

<div class="mt-4 flex items-start gap-3">
  <carbon-portal class="text-3xl text-red-400 mt-1" />
  <span>Publishing through Developer Portal</span>
</div>

</v-click>

<!--
METADATA:
sentence: What is API Management?
search_anchor: What is API Management
-->
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

<!--
METADATA:
sentence: Remember to start that APIM creation process early - grab a coffee while you wait for it to provision, and then we'll dive into the hands-on work.
search_anchor: Remember to start that APIM
-->
<v-click>

<div class="text-3xl mt-8">
Remember: Start APIM creation early!
</div>

</v-click>

<!--
METADATA:
sentence: Remember to start that APIM creation process early - grab a coffee while you wait for it to provision, and then we'll dive into the hands-on work.
search_anchor: Remember to start that APIM
-->
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

<!--
METADATA:
sentence: Remember to start that APIM creation process early - grab a coffee while you wait for it to provision, and then we'll dive into the hands-on work.
search_anchor: Remember to start that APIM
-->
<v-click>

<div class="text-2xl mt-4 font-bold">
Then let's dive into hands-on work!
</div>

</v-click>

</div>
