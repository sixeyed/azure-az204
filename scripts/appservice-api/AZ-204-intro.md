
Excellent work building a distributed application! This lab covers several important AZ-204 exam topics about multi-app deployments and configuration.

Multiple apps sharing an App Service Plan is a cost optimization pattern the exam tests frequently. Apps in the same plan share CPU, memory, and instances. Benefits include cost savings (pay for one plan, run multiple apps) and easy cross-component correlation. Drawbacks include resource contention and shared scaling (all apps scale together). The exam presents scenarios asking when to share plans versus separate them.

Configuration management with application settings is heavily tested. Settings act as environment variables that override application defaults, enabling environment-specific configuration without code changes. The double underscore pattern for .NET Core (RngApi__Url becomes RngApi:Url in configuration hierarchy) is important to understand. The exam tests how to configure apps for different environments using settings.

The `az webapp up` command combines multiple operations: creates web app if it doesn't exist, packages code into ZIP file, uploads and deploys, configures runtime stack automatically. Know its benefits (simplicity, rapid deployment) and limitations (may change plan settings, limited configuration control compared to separate commands). The exam may test when to use `webapp up` versus `az webapp create` + `az webapp deployment source`.

Scaling differences across SKUs is critical. Basic tier supports manual scale out up to 3 instances. Standard and above support auto-scale up to 10-30 instances depending on tier. Free/Shared tiers don't support scale out at all. When you need to change SKU and instance count, you must scale up (SKU) and scale out (instances) - these are separate operations. The exam tests understanding of SKU limitations and scaling capabilities.

Load balancing across instances happens automatically. App Service uses Azure Load Balancer to distribute requests across all healthy instances. Requests may go to any instance, so applications must be stateless or use external session storage (Redis, SQL, Storage). The exam tests understanding of stateless design and session management in scaled environments.

CORS configuration for APIs appears frequently. Browsers enforce same-origin policy - JavaScript from app1.com can't call APIs on app2.com without CORS headers. App Service has built-in CORS support - configure allowed origins in Portal, and Azure adds required headers automatically. The exam tests when CORS errors occur (cross-origin requests from browsers) and how to fix them (configure allowed origins).

Deployment automation side effects like `webapp up` changing plan configurations teach important lessons about checking what automation tools do. The exam may present troubleshooting scenarios where settings were unexpectedly changed by deployment tools.

We'll cover resource optimization strategies, configuration patterns for microservices, CORS troubleshooting, stateless application design, and common scenarios about multi-app deployments and service-to-service communication.

Master distributed App Service deployments for the AZ-204!
