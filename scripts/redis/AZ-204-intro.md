# Azure Cache for Redis - AZ-204 Exam Introduction

Excellent work with Redis! Caching is a critical performance optimization topic on the AZ-204.

## What We'll Cover

**When to use Redis versus alternatives** is frequently tested. Redis for: frequently-accessed data needing sub-millisecond response, session storage for stateless web apps, pub-sub messaging, leaderboards/counters. Table Storage for: simple key-value with longer durability. SQL/Cosmos for: complex queries and relationships. Service Bus for: enterprise messaging with guarantees. The exam tests choosing appropriate storage based on requirements.

**Service tiers** must be memorized. Basic: single node, no SLA, dev/test only. Standard: replication (master + replica), 99.9% SLA, production workloads. Premium: everything in Standard plus VNet support, persistence (RDB/AOF), geo-replication, clustering, up to 99.95% SLA. Enterprise: highest performance, Redis modules, active geo-replication. The exam tests which tier supports which features.

**Connection string format** includes host, port 6380 for TLS, SSL=True, password from access keys. Example: `{cachename}.redis.cache.windows.net:6380,ssl=True,password={accesskey}`. The exam may test constructing connection strings or troubleshooting connection failures.

**Common Redis commands** for the exam: `SET key value` (store), `GET key` (retrieve), `DEL key` (delete), `PUBLISH channel message` (publish), `SUBSCRIBE channel` (subscribe), `FLUSHDB` (clear all keys). Know basic operations even if you won't write Redis commands on the exam.

**Caching patterns** include cache-aside (check cache, load from DB if missing, populate cache), write-through (write to cache and DB simultaneously), write-behind (write to cache immediately, async to DB). The exam tests understanding of when to use each pattern.

**Data eviction policies** control what happens when cache is full. `allkeys-*` (evict from all keys) vs `volatile-*` (evict only keys with expiration). Common policies: LRU (least recently used), LFU (least frequently used), random. The exam tests choosing appropriate policies.

**High availability features** require specific tiers. Replication (Standard+), clustering for horizontal scale (Premium+), geo-replication for disaster recovery (Premium+). The exam tests understanding of availability features and their tier requirements.

We'll cover **monitoring metrics** (cache hits/misses ratio, memory usage, evicted keys), **security best practices** (TLS encryption, VNet integration, firewall rules), **cost optimization**, and **common scenarios** about implementing caching strategies, troubleshooting performance, and choosing appropriate tiers.

Master Redis caching for the AZ-204!
