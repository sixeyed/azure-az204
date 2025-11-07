# Azure Cache for Redis - Exercise Walkthrough

## Creating a Redis Cache

Let's start by creating our Redis cache instance. We'll use the Azure CLI for this.

### Create Resource Group

First, we'll create a resource group to hold our Redis instance using az group create with a name, the courselabs equals azure tag, and a location.

This creates our resource group in the specified location. The tag helps us track resources created during our labs - it's a best practice for organizing and managing Azure resources.

### Explore Creation Options

Before creating the Redis instance, let's look at the available options using az redis create --help. Notice the various configuration parameters available. For this lab, we'll use basic settings, but more advanced scenarios can use JSON configuration files for complex setups.

### Create Redis Instance

Now let's create a basic Redis instance. We're specifying the Basic SKU for cost-effective testing, C0 size which is the smallest available, minimum TLS version 1.2 for security, and Redis version 6.

We're running az redis create with these parameters. This will take several minutes to complete - creating a Redis instance involves provisioning virtual machines and configuring the Redis server. While it's creating, let's look at what we get.

### Portal Exploration

Opening the Azure Portal and navigating to the Redis instance, even while it's still creating, you can see the blade and explore the available features.

Notice several things. The Access keys section is where you'll find connection details - the hostname and the access keys that act as passwords. Geo-replication is not available in Basic SKU - you'd need Standard or Premium tier for that. Cluster size isn't available either - Basic tier gives you a single node. And data persistence is also not available in Basic SKU - there's no backup to storage.

Even with these limitations, a basic Redis cache is powerful for many scenarios - especially for caching and temporary data storage.

---

## Using Redis as a Cache

Now let's see Redis in action as a cache. We have a Pi calculator application that computes Pi to a specified number of decimal places.

### Run Without Cache

First, let's run the application without caching. We're using dotnet run pointing to the pi project with the dp parameter set to 1000 decimal places.

This calculates Pi to 1000 decimal places. Notice it takes a few seconds. This is a compute-intensive operation, but the result never changes - it will always be the same for the same input. This makes it a perfect candidate for caching.

Running it again, you'll see it takes the same amount of time because it's computing from scratch each time. There's no caching happening yet.

### Get Redis Connection Details

To use Redis, we need the access key. We're running az redis list-keys with the resource group and Redis instance name. This key acts as the password for Redis client connections - it's how your application authenticates to the Redis server.

### Run With Cache

Now let's enable caching. We're running dotnet run with the same parameters, but adding the usecache flag and the cs parameter for connection string. The connection string includes the Redis hostname, port 6380 for SSL connections, the password which is the access key, SSL set to True for encrypted connections, and abortConnect set to False so temporary connection issues don't crash the application.

The first run still takes time because the cache is empty. But the application stores the result in Redis after computing it, using the key "pi-1000".

### Verify Cached Data

Let's check the data in Redis. In the Portal, we're opening the Console from the Redis blade. This is the Redis CLI, embedded in the Portal and already connected to your instance - no need to provide credentials.

We're querying the cached value using the GET command with the key pi-1000. You'll see the same Pi value that was computed. Now when we run the application again, watch how much faster it returns - it's reading from the cache instead of recalculating. The response is nearly instantaneous.

### Test Cache Deletion

Redis data is read-write from any connected process. In the console, we're deleting the cached value using the DEL command with the key pi-1000.

Redis responses are concise - you'll see 1 if the value was deleted, or 0 if the key wasn't found. This confirmation tells you the operation succeeded.

Running the application again, it needs to recalculate because the cache is empty. The computation time is back to several seconds.

### Understanding Cache Characteristics

This demonstrates an important principle: the cache is not critical. The application works correctly without it, but responses are slower. The application degrades gracefully when the cache is unavailable or empty.

This is perfect for the Basic Redis tier, where data isn't replicated or persisted. It's effectively in-memory on a single server. If Redis restarted, the data would be lost - but that's acceptable for a cache. The application would just recalculate and repopulate the cache.

---

## Using Redis for Pub-Sub Messaging

Redis also supports publish-subscribe messaging in the same instance used for data storage. It's not reliable like Service Bus - there's no guaranteed delivery or message persistence - but it's fast and simple.

### Subscribe to Events

In the Redis Console in the Portal, we're subscribing to the Pi application's event channel using SUBSCRIBE events.pi.computed.

You'll see confirmation messages that the console is subscribed. Now it's listening for messages on that channel. Any message published to this channel will appear here.

### Publish Events

In the terminal, we're running the Pi application with event publishing enabled. We're running it multiple times with different decimal place values - 100, 200, and 300 - each time with the usecache and publishevents flags enabled.

### View Published Events

Checking the Azure Portal console, you'll see events being received. Each event displays three lines - the first line says "message", the second shows the channel name "events.pi.computed", and the third shows the actual message content like "Calculated Pi to: 100dp".

These events appear in real-time as the Pi calculations complete. Any subscriber to this channel receives every message published while they're subscribed.

### Real-World Pattern

This demonstrates a common pattern: an intensive operation gets cached, and an event gets published to notify subscribers that fresh data is available. Consumers subscribe to these events to know when to reload data from the cache.

For example, you might have multiple web servers subscribing to events. When one server recalculates something and updates the cache, it publishes an event. All other servers receive that event and know they can now fetch the updated data from the cache. This keeps all servers synchronized without each one having to recalculate independently.

---

## Lab Challenge

Now it's your turn to explore. Consider these questions:

What happens with multiple subscribers to the same channel? Try opening the Redis console in multiple browser tabs and subscribing to the same channel. When you publish an event, do all subscribers receive it?

What if no subscribers are running when events are published? Publish some events, then subscribe. Do you see the old events? This is an important characteristic of pub-sub - messages are not persisted.

Can you find metrics in the Portal showing cache eviction? Navigate to the Metrics blade and explore what telemetry is available. Can you see cache hits, misses, and evicted keys?

Can you use the CLI to delete all cache entries at once? Look at the FLUSHDB or FLUSHALL commands. What's the difference between them?

These are important considerations for understanding Redis behavior in production scenarios.

---

## Reference

- [Azure documentation](https://docs.microsoft.com/azure/)

## Cleanup

When you're finished exploring, clean up your resources using az group delete with the -y flag to skip confirmation and --no-wait to return immediately.

This removes all resources and stops any charges. The --no-wait flag means the command returns immediately while deletion continues in the background.
