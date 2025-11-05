# API Management - Policies - AZ-204 Exam Introduction

Great work implementing security and performance policies! Policy configuration is one of the most heavily tested APIM topics on the AZ-204. Let's focus on what you need to master.

## What We'll Cover

**The four policy execution sections** and their specific order is fundamental: inbound (executes before backend call, can modify request or bypass backend), backend (executes during backend routing, can change backend URL), outbound (executes before client response, can modify response), and on-error (executes when errors occur). Know what types of policies go in each section and the execution order. The exam tests this constantly.

**Policy scope hierarchy** determines which policies execute: Operation > API > Product > Global (most specific to least specific). The `<base />` tag controls inheritance - it's a placeholder where parent-level policies execute. Without `<base />` in your inbound section, API/Product/Global inbound policies won't run. The exam tests whether you understand policy inheritance and how to use `<base />` correctly.

**Caching policies** are tricky and heavily tested. You need BOTH cache-lookup-value (in inbound section, before backend) AND cache-store-value (in outbound section, after backend). Just having one doesn't work. The cache-lookup checks for cached responses and short-circuits the backend call if found. The cache-store saves responses for future requests. Know the duration parameter, vary-by-query-parameter options, and cache key concepts.

**Header manipulation with set-header** has four actions: delete (remove header entirely), override (replace value), append (add to existing values), and skip-when-exists (only set if not already present). The exam tests which action to use for different scenarios like removing security-sensitive headers, adding custom tracking headers, or ensuring required headers exist.

**Response transformation with find-and-replace** is important for security. You can rewrite URLs, remove sensitive data, or modify response content without changing backend code. Know it goes in the outbound section and supports regex patterns. Common use case: preventing backend URL exposure.

**CORS policy** enables cross-origin requests from browsers. Know the difference between allowing specific origins versus * (all origins), which HTTP methods to allow, whether to include credentials, and which headers to expose. This appears in web app integration scenarios.

**Subscription key authentication** via Ocp-Apim-Subscription-Key header returns 401 Unauthorized without valid keys. Know that keys can be passed as header or query parameter, products can require or not require subscriptions, and keys can be regenerated without downtime using primary/secondary key rotation.

We'll cover **security best practices** (hiding implementation details, preventing backend bypass), **performance optimization patterns**, **common exam scenarios** about policy troubleshooting, and **policy execution flow debugging**.

Master APIM policies for the AZ-204!
