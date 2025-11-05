# Azure API Management - Exercises Introduction

We've covered what API Management is and its four core features: API designer, gateway, developer portal, and integrated security. Now let's build a complete API management solution.

## What You'll Do

You'll start by **creating an APIM instance** - note that Developer tier provisioning takes 60+ minutes, so this is a good time to grab coffee! While you wait, you'll **deploy a random number generator backend API** to Azure Web App. This backend provides the actual functionality that APIM will front.

Once APIM is ready, you'll **import the API using its OpenAPI/Swagger specification**. This automated import saves you from manually defining endpoints - APIM reads the spec and creates all operations automatically. You'll see the API designer with all your endpoints ready to configure.

The power of APIM comes from **policies**. You'll configure three distinct policies to add production-grade features without changing any backend code: **response caching** on the /rng endpoint (30 seconds) to improve performance and reduce backend load, **IP filtering** on the /reset endpoint to restrict admin-only access (only your IP can call this sensitive operation), and **mock 404 responses** on the /healthz endpoint, effectively blocking it from external access.

Next, you'll **publish through the Developer Portal**. You'll sign up as an API consumer yourself, obtaining a subscription key - this is the authentication token clients need to call your API. You'll **test with curl**, including subscription key validation (try without the key and get rejected!), and explore **rate limiting** by hitting the 5 calls/minute limit for the Starter product.

Finally, you'll explore the **analytics dashboard** to observe usage patterns, performance metrics, and which operations are being called. This monitoring capability is built into APIM without any backend instrumentation.

Let's build a complete API management solution!
