# Azure Cache for Redis - Quickfire Questions

## Question 1
What is Azure Cache for Redis?


- A) A managed in-memory data store based on Redis, used for caching and high-performance scenarios
- B) A blob storage service
- C) A message queue
- D) A relational database

**Answer: A**
Azure Cache for Redis is a fully managed, in-memory data structure store used for caching, session storage, and pub/sub.
---
## Question 2
What are the pricing tiers for Azure Cache for Redis?


- A) Free and Paid
- B) Basic, Standard, Premium, Enterprise, Enterprise Flash
- C) Small, Medium, Large
- D) Developer and Production

**Answer: B**
Tiers: Basic (single node, dev/test), Standard (replicated), Premium (clustering, persistence), Enterprise (Redis Enterprise features).
---
## Question 3
What is the primary benefit of using Redis as a cache?


- A) Automatic backups
- B) Extremely fast in-memory access (microsecond latency) reducing database load
- C) Cheaper storage
- D) Better encryption

**Answer: B**
Redis stores data in memory, providing sub-millisecond response times and reducing load on backend databases.
---
## Question 4
What is the difference between Basic and Standard tiers?


- A) Standard provides replication (primary + replica) for high availability; Basic is single node
- B) Standard is cheaper
- C) Basic is faster
- D) No difference

**Answer: A**
Standard tier adds a replica for high availability and automatic failover. Basic is single-node with no SLA.
---
## Question 5
What data structures does Redis support?


- A) Only tables
- B) Only JSON
- C) Only key-value strings
- D) Strings, Lists, Sets, Sorted Sets, Hashes, Bitmaps, HyperLogLogs, Streams

**Answer: D**
Redis supports multiple data structures beyond strings, enabling diverse use cases like leaderboards, queues, and counters.
---
## Question 6
What is cache-aside pattern?


- A) Database-first always
- B) Cache-only pattern
- C) Application checks cache first; on miss, loads from database and populates cache
- D) No caching

**Answer: C**
Cache-aside (lazy loading) pattern: check cache, if miss load from DB and cache it. Application manages cache population.
---
## Question 7
What is the purpose of TTL (Time to Live) in Redis?


- A) Network timeout
- B) Automatically expires keys after a specified duration to prevent stale data
- C) Transaction timeout
- D) Cache size limit

**Answer: B**
TTL sets expiration time on keys, ensuring cached data doesn't become stale and memory is freed automatically.
---
## Question 8
What is Redis persistence?


- A) Optional feature (RDB snapshots or AOF logs) to persist data to disk
- B) Always in-memory only
- C) Automatic archiving
- D) Backup to Blob Storage

**Answer: A**
Premium tier supports RDB (snapshots) and AOF (append-only file) persistence for data durability across restarts.
---
## Question 9
What is Redis clustering?


- A) Database clustering
- B) Load balancing
- C) Clustering servers physically
- D) Distributing data across multiple Redis nodes (sharding) for scalability beyond single-node limits

**Answer: D**
Clustering (Premium tier) shards data across multiple nodes, enabling horizontal scaling beyond a single node's memory capacity.
---
## Question 10
What is pub/sub in Redis?


- A) Security feature
- B) Messaging pattern where publishers send messages to channels; subscribers receive them
- C) Subscription billing
- D) Publishing articles

**Answer: B**
Redis pub/sub enables real-time messaging where applications publish to channels and others subscribe to receive messages.