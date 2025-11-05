# Azure Event Grid

Azure Event Grid is an event routing service that enables event-driven, reactive programming. It uses a publish-subscribe model where publishers send events without knowing who will consume them, and subscribers choose which events they want to handle. Event Grid is ideal for building serverless architectures and integrating services in a loosely coupled way.

## Reference

- [Event Grid overview](https://docs.microsoft.com/en-us/azure/event-grid/overview)

- [Event Grid concepts](https://docs.microsoft.com/en-us/azure/event-grid/concepts)

- [`az eventgrid` commands](https://docs.microsoft.com/en-us/cli/azure/eventgrid?view=azure-cli-latest)

## Event Grid Basics

Event Grid is built around these concepts:

- **Events**: What happened (e.g., "blob created", "VM started")
- **Event sources**: Where the event happened (e.g., Storage Account, Azure subscription)
- **Topics**: The endpoint where events are sent
- **Event subscriptions**: Filter and route events to handlers
- **Event handlers**: Where events are processed (Functions, Logic Apps, webhooks)

## Create a Custom Topic

Event Grid has two types of topics:

- **System topics**: Built-in events from Azure services (Blob Storage, Resource Groups, etc.)
- **Custom topics**: Events from your own applications

Let's start by creating a custom topic:

```bash
az group create -n labs-eventgrid --tags courselabs=azure -l eastus

# Create Event Grid topic
az eventgrid topic create \
  -g labs-eventgrid \
  -n orders-topic \
  -l eastus
```

Get the topic endpoint and access key:

```bash
# Get endpoint
TOPIC_ENDPOINT=$(az eventgrid topic show \
  -g labs-eventgrid \
  -n orders-topic \
  --query endpoint -o tsv)

echo "Topic endpoint: $TOPIC_ENDPOINT"

# Get access key
TOPIC_KEY=$(az eventgrid topic key list \
  -g labs-eventgrid \
  -n orders-topic \
  --query key1 -o tsv)

echo "Access key: $TOPIC_KEY"
```

## Publish Events to Custom Topic

You can publish events to the topic using the REST API or Azure SDKs. Let's use curl to publish an event:

```bash
# Create event data
cat > event.json << 'EOF'
[
  {
    "id": "1",
    "eventType": "OrderCreated",
    "subject": "orders/order-12345",
    "eventTime": "2024-01-15T10:30:00Z",
    "data": {
      "orderId": "12345",
      "customer": "Alice",
      "amount": 99.99,
      "status": "pending"
    },
    "dataVersion": "1.0"
  }
]
EOF

# Publish event
curl -X POST "$TOPIC_ENDPOINT/api/events" \
  -H "aeg-sas-key: $TOPIC_KEY" \
  -H "Content-Type: application/json" \
  -d @event.json
```

The event is now published, but we don't have any subscribers yet, so it goes nowhere.

## Create an Event Subscription with Webhook

For testing, we'll use a webhook endpoint. You can use a service like webhook.site or RequestBin to get a temporary webhook URL.

Browse to https://webhook.site and copy your unique URL.

```bash
# Create event subscription with webhook handler
az eventgrid event-subscription create \
  --source-resource-id "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/labs-eventgrid/providers/Microsoft.EventGrid/topics/orders-topic" \
  --name orders-webhook-sub \
  --endpoint <your-webhook-url>
```

📋 Publish another event and check your webhook site to see if it was received.

<details>
  <summary>Not sure how?</summary>

```bash
# Update event with new ID
cat > event2.json << 'EOF'
[
  {
    "id": "2",
    "eventType": "OrderCreated",
    "subject": "orders/order-67890",
    "eventTime": "2024-01-15T11:00:00Z",
    "data": {
      "orderId": "67890",
      "customer": "Bob",
      "amount": 149.99,
      "status": "pending"
    },
    "dataVersion": "1.0"
  }
]
EOF

curl -X POST "$TOPIC_ENDPOINT/api/events" \
  -H "aeg-sas-key: $TOPIC_KEY" \
  -H "Content-Type: application/json" \
  -d @event2.json
```

Check your webhook site - you should see the event payload!

</details><br/>

## Event Filtering

You can filter events based on event type or subject patterns:

```bash
# Create subscription that only receives "OrderShipped" events
az eventgrid event-subscription create \
  --source-resource-id "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/labs-eventgrid/providers/Microsoft.EventGrid/topics/orders-topic" \
  --name orders-shipped-sub \
  --endpoint <webhook-url> \
  --included-event-types OrderShipped

# Create subscription with subject filtering (begins with)
az eventgrid event-subscription create \
  --source-resource-id "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/labs-eventgrid/providers/Microsoft.EventGrid/topics/orders-topic" \
  --name high-value-orders-sub \
  --endpoint <webhook-url> \
  --subject-begins-with "orders/high-value/"
```

## System Topics - Blob Storage Events

Event Grid can automatically capture events from Azure services. Let's set up blob storage events:

```bash
# Create storage account
az storage account create \
  -g labs-eventgrid \
  -n <storage-account-name> \
  --sku Standard_LRS

# Get storage account resource ID
STORAGE_ID=$(az storage account show \
  -g labs-eventgrid \
  -n <storage-account-name> \
  --query id -o tsv)

# Create event subscription for blob created events
az eventgrid event-subscription create \
  --source-resource-id $STORAGE_ID \
  --name blob-created-sub \
  --endpoint <webhook-url> \
  --included-event-types Microsoft.Storage.BlobCreated
```

Now upload a file to trigger an event:

```bash
# Create container
az storage container create \
  -n uploads \
  --account-name <storage-account-name>

# Upload a file
echo "Test content" > test.txt
az storage blob upload \
  -c uploads \
  -f test.txt \
  -n test.txt \
  --account-name <storage-account-name>
```

Check your webhook - you should see the `Microsoft.Storage.BlobCreated` event!

## Event Grid with Azure Functions

A more practical handler is Azure Functions. The function is automatically triggered when events arrive:

```bash
# Create function app
az functionapp create \
  -g labs-eventgrid \
  -n <function-app-name> \
  --storage-account <storage-account-name> \
  --consumption-plan-location eastus \
  --runtime dotnet \
  --functions-version 4
```

Create a simple function with Event Grid trigger (you would deploy this code):

```csharp
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.EventGrid;
using Azure.Messaging.EventGrid;
using Microsoft.Extensions.Logging;

public static class OrderProcessor
{
    [FunctionName("ProcessOrder")]
    public static void Run(
        [EventGridTrigger] EventGridEvent eventGridEvent,
        ILogger log)
    {
        log.LogInformation($"Event type: {eventGridEvent.EventType}");
        log.LogInformation($"Subject: {eventGridEvent.Subject}");
        log.LogInformation($"Data: {eventGridEvent.Data}");
    }
}
```

## Lab

Event Grid supports retry policies and dead-letter queues for failed deliveries. Configure a subscription with:

- Maximum of 5 retry attempts
- Event time-to-live of 1 hour
- Dead-letter destination to a blob container

Can you test the dead-letter behavior by creating a subscription with an invalid webhook endpoint?

> Stuck? Try [hints](hints.md) or check the [solution](solution.md).

___

## Cleanup

Delete the lab resources:

```bash
az group delete -y --no-wait -n labs-eventgrid
```
