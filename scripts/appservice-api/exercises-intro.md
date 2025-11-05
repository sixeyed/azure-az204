# App Service for Distributed Apps (API) - Exercises Introduction

We've covered deploying multiple applications within a single App Service Plan to share compute resources cost-effectively. Now let's build a distributed system with an API backend and web frontend.

## What You'll Do

You'll start by **creating an App Service Plan** (B1 SKU with 2 workers on Linux). Then you'll deploy the REST API using **`az webapp up`** - this powerful command combines creating a web app, packaging code, and deploying in a single operation. Azure's Oryx build system automatically detects .NET 6.0, builds your application, and runs it. You'll **verify deployment** through logs and test the Swagger documentation.

Next, you'll **deploy the web frontend to the same plan**, sharing the infrastructure but isolated with its own URL. When you test it, you'll see "RNG service unavailable" - this is the key learning moment! The default localhost configuration doesn't work in Azure because the frontend and API are separate apps with different hostnames.

The solution: **configure application settings**. You'll set `RngApi__Url` (double underscore maps to nested .NET Core configuration) with the API's full URL. Now the frontend can communicate with the backend. This demonstrates centralized configuration management - change settings in Azure Portal without redeploying code.

You'll attempt to **scale to 3 workers** but discover that `az webapp up` downgraded your plan to F1 Free (a known side effect). This teaches an important lesson: some automation tools have unintended consequences. You'll need to **scale up (change SKU) and scale out (add instances) simultaneously**, then observe load balancing across multiple workers.

The **lab challenge** involves deploying a static HTML SPA. You'll encounter **CORS errors** when the SPA tries to call your API - the browser's security model blocks cross-origin requests by default. You'll configure CORS settings in the Portal to allow your SPA's origin, learning a critical real-world web development skill.

Let's build a distributed application in App Service!
