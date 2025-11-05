# Azure API Management - AZ-204 Exam Introduction

Great job implementing API Management! This is a significant AZ-204 exam topic with questions appearing in multiple domains. Let's focus on what you need to know for the certification.

## Exam Coverage

APIM appears in questions about implementing API Management, integrating Azure services, and securing solutions. Expect both configuration questions and scenario-based questions about choosing the right policies and architectures.

## What We'll Cover

**Service tier selection** is critical for the exam. Developer tier is for dev/test (99.9% SLA, no auto-scale). Consumption tier is serverless with per-call pricing (no SLA, auto-scales to zero). Basic/Standard tiers are production-ready (99.9% SLA, manual scale). Premium tier is for enterprise (99.95% SLA, multi-region, VNet integration, auto-scale). Scenario questions test which tier to choose based on requirements like SLA, cost model, and scale needs.

**Policy structure** is heavily tested. Policies have four execution sections: inbound (before backend call), backend (during backend routing), outbound (before client response), and on-error (when errors occur). Know the order and what each section is for. Policy scope hierarchy goes Operation > API > Product > Global, and the `<base />` tag controls inheritance - without it, parent policies don't execute.

**Common policies** you must know include rate-limit (throttling), caching (requires BOTH cache-lookup in inbound AND cache-store in outbound), validate-jwt (token authentication), set-header (add/modify/delete headers), find-and-replace (transform response content), CORS (cross-origin resource sharing), and ip-filter (restrict by IP address). The exam tests when to use each and how to configure them.

**Authentication methods** appear frequently. Subscription keys via Ocp-Apim-Subscription-Key header (simplest), JWT validation for OAuth/OpenID Connect tokens, client certificates for mutual TLS, and Azure AD integration. Know that APIs must belong to at least one Product to be accessible, and Products require subscriptions (with keys) unless configured otherwise.

**Versions vs Revisions** is a key exam concept. Revisions are for non-breaking changes (optional parameters, bug fixes) - tested via ;rev=N syntax before making them current. Versions are for breaking changes (required parameters, removed endpoints) - create new URL paths requiring client migration. Know three versioning schemes: Header (custom header), Query string (parameter), and Path (URL segment).

We'll cover **OpenAPI integration**, **products and subscriptions**, **developer portal customization**, **monitoring and analytics**, **integration with App Service deployment slots**, and **common exam scenarios** about securing APIs, transforming responses, and troubleshooting access issues.

Master APIM for the AZ-204!
