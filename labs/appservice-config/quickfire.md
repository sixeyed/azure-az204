# App Service Configuration - Quickfire Questions

## Question 1
What is the purpose of health check endpoints in App Service?


- A) To validate SSL certificates
- B) To monitor database connections
- C) To detect unhealthy instances and route traffic away from them
- D) To check application version

**Answer: C**
Health checks allow App Service to ping a specific path in your app. If an instance fails health checks, it's removed from the load balancer rotation.
---
## Question 2
Which auto-heal action can you configure for App Service?


- A) Log an event
- B) Run a custom executable
- C) All of the above
- D) Recycle the worker process

**Answer: C**
Auto-heal can recycle processes, run custom executables, or log events based on triggers like request count, slow requests, memory limits, or status codes.
---
## Question 3
What is the minimum App Service Plan tier required for auto-scaling?


- A) Standard (S1)
- B) Free (F1)
- C) Premium (P1)
- D) Basic (B1)

**Answer: A**
Auto-scaling (scale out) is only available starting with Standard (S1) tier and above.
---
## Question 4
Which metric would you use to scale out when CPU usage is high?


- A) HTTP Queue Length
- B) Memory Percentage
- C) CPU Percentage
- D) Disk Queue Length

**Answer: C**
CPU Percentage is a common metric for auto-scaling. When CPU exceeds a threshold (e.g., 70%), you can scale out by adding instances.
---
## Question 5
What is the difference between scale up and scale out?


- A) They are the same thing
- B) Scale up increases instance size (vertical), scale out adds instances (horizontal)
- C) Scale up is for databases, scale out is for web apps
- D) Scale up adds instances, scale out increases instance size

**Answer: B**
Scale up = vertical scaling (bigger instances), Scale out = horizontal scaling (more instances).
---
## Question 6
What happens to existing connections when an unhealthy instance is detected?


- A) They are immediately terminated
- B) All connections are migrated to healthy instances
- C) The entire app is restarted
- D) New requests are not routed to it, but existing connections may continue

**Answer: D**
By default, new requests stop being routed to unhealthy instances, but existing connections may continue until they complete or time out.
---
## Question 7
Which setting controls how long App Service waits before removing an unhealthy instance?


- A) Load balancing timeout
- B) Health check interval
- C) Health check path
- D) Unhealthy threshold

**Answer: D**
The unhealthy threshold specifies how many consecutive failed health checks are required before an instance is considered unhealthy.
---
## Question 8
What is the recommended health check path for a web application?


- A) A page that performs complex calculations
- B) The database connection page
- C) A dedicated lightweight endpoint (e.g., /health)
- D) The home page (/)

**Answer: C**
A dedicated /health endpoint that performs lightweight checks (not heavy operations) is recommended to avoid false positives.
---
## Question 9
Which auto-scaling mode distributes traffic based on a schedule?


- A) Schedule-based scaling
- B) Automatic scaling
- C) Manual scaling
- D) Metric-based scaling

**Answer: A**
Schedule-based scaling allows you to set different instance counts based on time of day, day of week, or specific date ranges.
---
## Question 10
What is the maximum number of instances you can scale to in the Standard (S1) tier?


- A) 20
- B) 100
- C) 3
- D) 10

**Answer: D**
Standard tier allows scaling up to 10 instances. Premium tiers allow up to 20 (P1v2) or 30 (P1v3/P2v3/P3v3) instances.