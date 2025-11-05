# Azure Cache for Redis - Exercise Walkthrough

## Exercise 1: Creating a Redis Cache

Let's start by creating our Redis cache instance. We'll use the Azure CLI for this.

### Create Resource Group

First, we'll create a resource group to hold our Redis instance:

```bash
az group create -n <resource-group-name> --tags courselabs=azure -l <location>
```

This creates our resource group in the specified location. The tag helps us track resources created during our labs.

### Explore Creation Options

Before creating the Redis instance, let's look at the available options:

```bash
az redis create --help
```

Notice the various configuration parameters available. For this lab, we'll use basic settings, but more advanced scenarios can use JSON configuration files.

### Create Redis Instance

Now let's create a basic Redis instance. We'll specify:
- Basic SKU for cost-effective testing
- C0 size (the smallest available)
- Minimum TLS version 1.2 for security
- Redis version 6

```bash
az redis create --sku Basic --vm-size c0 --minimum-tls-version 1.2 --redis-version 6 -g <resource-group-name> -n <redis-name>
```

This will take several minutes to complete. While it's creating, let's look at what we get.

### Portal Exploration

Open the Azure Portal and navigate to your Redis instance. Even while it's still creating, you can see the blade and explore the available features.

Notice:
- **Access keys**: Where you'll find connection details
- **Geo-replication**: Not available in Basic SKU
- **Cluster size**: Not available in Basic SKU
- **Data persistence**: Not available in Basic SKU

Even with these limitations, a basic Redis cache is powerful for many scenarios.

## Exercise 2: Using Redis as a Cache

Now let's see Redis in action as a cache. We have a Pi calculator application that computes Pi to a specified number of decimal places.

### Run Without Cache

First, let's run the application without caching:

```bash
dotnet run --project ./src/pi -dp 1000
```

This calculates Pi to 1000 decimal places. Notice it takes a few seconds. This is a compute-intensive operation, but the result never changes - it will always be the same for the same input.

Run it again, and you'll see it takes the same amount of time because it's computing from scratch each time.

### Get Redis Connection Details

To use Redis, we need the access key:

```bash
az redis list-keys -g <resource-group-name> -n <redis-name>
```

This key acts as the password for Redis client connections.

### Run With Cache

Now let's enable caching:

```bash
dotnet run --project src/pi -dp 1000 -usecache -cs '<redis-name>.redis.cache.windows.net:6380,password=<redis-key>,ssl=True,abortConnect=False'
```

The first run still takes time because the cache is empty. But the application stores the result in Redis after computing it.

### Verify Cached Data

Let's check the data in Redis. In the Portal, open the Console from your Redis blade.

This is the Redis CLI, embedded in the Portal and already connected to your instance.

Query the cached value:

```
GET pi-1000
```

You'll see the same Pi value that was computed. Now run the application again, and watch how much faster it returns - it's reading from the cache instead of recalculating.

### Test Cache Deletion

Redis data is read-write from any connected process. In the console, delete the cached value:

```
DEL pi-1000
```

Redis responses are concise - you'll see `1` if the value was deleted, or `0` if the key wasn't found.

Run the application again, and it needs to recalculate because the cache is empty.

### Understanding Cache Characteristics

This demonstrates an important principle: the cache is not critical. The application works correctly without it, but responses are slower.

This is perfect for the Basic Redis tier, where data isn't replicated or persisted. It's effectively in-memory on a single server. If Redis restarted, the data would be lost - but that's acceptable for a cache.

## Exercise 3: Using Redis for Pub-Sub Messaging

Redis also supports publish-subscribe messaging in the same instance used for data storage. It's not reliable like Service Bus, but it's fast and simple.

### Subscribe to Events

In the Redis Console in the Portal, subscribe to the Pi application's event channel:

```
SUBSCRIBE events.pi.computed
```

You'll see confirmation messages that the console is subscribed. Now it's listening for messages.

### Publish Events

In your terminal, run the Pi application with event publishing enabled:

```bash
dotnet run --project ./src/pi -dp 100 -usecache -publishevents -cs '<redis-name>.redis.cache.windows.net:6380,password=<redis-key>,ssl=True,abortConnect=False'

dotnet run --project ./src/pi -dp 200 -usecache -publishevents -cs '<redis-name>.redis.cache.windows.net:6380,password=<redis-key>,ssl=True,abortConnect=False'

dotnet run --project ./src/pi -dp 300 -usecache -publishevents -cs '<redis-name>.redis.cache.windows.net:6380,password=<redis-key>,ssl=True,abortConnect=False'
```

### View Published Events

Check the Azure Portal console. You'll see events being received, each displaying three lines:

```
1) "message"
2) "events.pi.computed"
3) "Calculated Pi to: <value>dp"
```

### Real-World Pattern

This demonstrates a common pattern: an intensive operation gets cached, and an event gets published to notify subscribers that fresh data is available. Consumers subscribe to these events to know when to reload data from the cache.

## Lab Challenge

Now it's your turn to explore. Consider these questions:

1. What happens with multiple subscribers to the same channel?
2. What if no subscribers are running when events are published?
3. Can you find metrics in the Portal showing cache eviction?
4. Can you use the CLI to delete all cache entries at once?

These are important considerations for understanding Redis behavior in production scenarios.

## Cleanup

When you're finished exploring, clean up your resources:

```bash
az group delete -y --no-wait -n <resource-group-name>
```

This removes all resources and stops any charges.
