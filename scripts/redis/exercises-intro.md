# Azure Cache for Redis - Exercises Introduction

We've covered Redis as an in-memory data store for caching and pub-sub messaging with sub-millisecond response times. Now let's implement caching and messaging patterns.

## What You'll Do

You'll start by **creating a Redis cache instance** using Azure CLI with Basic SKU (single node for dev/test), C0 size (smallest, 250MB), TLS 1.2 encryption, and Redis version 6. Then you'll **retrieve access keys** for connecting securely to the cache.

Next, you'll **use Redis as a cache with a Pi calculator application**. The app calculates Pi to many decimal places (computationally expensive). First request is slow (calculation happens). But subsequent requests? Lightning fast! The result is cached in Redis, so the app retrieves it from memory instead of recalculating. This is the **cache-aside pattern** - check cache first, calculate and store if missing.

You'll **verify cached data using Redis Console** in the Portal with `GET` commands, seeing the exact data stored. Then you'll **test cache deletion with `DEL`** and observe the performance difference when cache is empty (slow) versus populated (fast).

Next comes **pub-sub messaging**. You'll `SUBSCRIBE` to a channel, then `PUBLISH` messages to it. Subscribers receive messages instantly. This enables real-world patterns like cache invalidation notifications - when data changes, publish an event so all subscribers can refresh their caches.

The key learning: Redis serves two distinct roles. As a cache, it improves performance by storing frequently-accessed data in memory. As a message queue with pub-sub, it enables asynchronous communication between services. Both use the same simple Redis API.

Let's implement caching and messaging with Redis!
