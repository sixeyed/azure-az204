# App Service Configuration - Quickfire Questions

## Question 1
What is the purpose of health check endpoints in App Service?

- A) To monitor database connections
- B) To detect unhealthy instances and route traffic away from them
- C) To check application version
- D) To validate SSL certificates

**Answer: B**
Health checks allow App Service to ping a specific path in your app. If an instance fails health checks, it's removed from the load balancer rotation.

---

## Question 2
Which auto-heal action can you configure for App Service?

- A) Recycle the worker process
- B) Run a custom executable
- C) Log an event
- D) All of the above

**Answer: D**
Auto-heal can recycle processes, run custom executables, or log events based on triggers like request count, slow requests, memory limits, or status codes.

---

## Question 3
What is the minimum App Service Plan tier required for auto-scaling?

- A) Free (F1)
- B) Basic (B1)
- C) Standard (S1)
- D) Premium (P1)

**Answer: C**
Auto-scaling (scale out) is only available starting with Standard (S1) tier and above.

---

## Question 4
Which metric would you use to scale out when CPU usage is high?

- A) Memory Percentage
- B) CPU Percentage
- C) Disk Queue Length
- D) HTTP Queue Length

**Answer: B**
CPU Percentage is a common metric for auto-scaling. When CPU exceeds a threshold (e.g., 70%), you can scale out by adding instances.

---

## Question 5
What is the difference between scale up and scale out?

- A) Scale up adds instances, scale out increases instance size
- B) Scale up increases instance size (vertical), scale out adds instances (horizontal)
- C) They are the same thing
- D) Scale up is for databases, scale out is for web apps

**Answer: B**
Scale up = vertical scaling (bigger instances), Scale out = horizontal scaling (more instances).

---

## Question 6
What happens to existing connections when an unhealthy instance is detected?

- A) They are immediately terminated
- B) New requests are not routed to it, but existing connections may continue
- C) All connections are migrated to healthy instances
- D) The entire app is restarted

**Answer: B**
By default, new requests stop being routed to unhealthy instances, but existing connections may continue until they complete or time out.

---

## Question 7
Which setting controls how long App Service waits before removing an unhealthy instance?

- A) Health check interval
- B) Health check path
- C) Unhealthy threshold
- D) Load balancing timeout

**Answer: C**
The unhealthy threshold specifies how many consecutive failed health checks are required before an instance is considered unhealthy.

---

## Question 8
What is the recommended health check path for a web application?

- A) The home page (/)
- B) A dedicated lightweight endpoint (e.g., /health)
- C) The database connection page
- D) A page that performs complex calculations

**Answer: B**
A dedicated /health endpoint that performs lightweight checks (not heavy operations) is recommended to avoid false positives.

---

## Question 9
Which auto-scaling mode distributes traffic based on a schedule?

- A) Metric-based scaling
- B) Schedule-based scaling
- C) Manual scaling
- D) Automatic scaling

**Answer: B**
Schedule-based scaling allows you to set different instance counts based on time of day, day of week, or specific date ranges.

---

## Question 10
What is the maximum number of instances you can scale to in the Standard (S1) tier?

- A) 3
- B) 10
- C) 20
- D) 100

**Answer: B**
Standard tier allows scaling up to 10 instances. Premium tiers allow up to 20 (P1v2) or 30 (P1v3/P2v3/P3v3) instances.
