# App Service Configuration - Exercises Introduction

We've covered enterprise-grade PaaS features for configuration management and health monitoring. Now let's see how App Service handles application failures gracefully.

## What You'll Do

You'll **deploy a .NET 6.0 REST API** using `webapp up` with B1 SKU. The app initially works perfectly. Then comes the interesting part: you'll **configure it to fail** after a certain number of requests by setting the app setting `Rng__FailAfter__CallCount` to "3". This simulates real-world scenarios where applications enter unhealthy states. After the third API call, you'll get a 500 error, and the `/healthz` health check endpoint also returns 500.

Now you'll implement **health checks** in the Portal. You set the health check path to `/healthz` and configure the load balancing threshold to 2 minutes. This triggers Azure to periodically check your health endpoint. When it detects the failure, Azure **automatically restarts the instance**, creating a fresh healthy application. Your app is healthy again!

Make requests until it fails again, and you'll observe an important limitation: **Azure won't automatically restart a single instance** to avoid downtime (restarting your only instance would make the app temporarily unavailable). The solution is **scaling out to 2 instances**. Now when one instance fails, Azure's load balancer sends requests only to the healthy instance while the unhealthy one either recovers or gets restarted. Your application stays available even when individual instances fail!

The **lab challenge** introduces **auto-heal** - configuring automatic restarts when specific conditions occur, like receiving 500 errors within a time window. You'll set it to restart immediately (within 30 seconds) rather than waiting the default one hour, demonstrating more aggressive failure recovery.

Let's implement production-grade health monitoring!
