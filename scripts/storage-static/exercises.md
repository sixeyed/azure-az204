# Static Websites with Azure Storage Blobs - Exercises

## Exercise 1: Deploy a Static Website

### Creating the Storage Account

Let's begin by creating a resource group and storage account. We'll use the Azure CLI to create our resources.

First, create a resource group in your preferred region:

```
az group create -n [RESOURCE_GROUP_NAME] --tags courselabs=azure -l [REGION]
```

Next, create a storage account with locally redundant storage:

```
az storage account create -g [RESOURCE_GROUP_NAME] --sku Standard_LRS -n [STORAGE_ACCOUNT_NAME]
```

Remember that storage account names must be globally unique and between 3 and 24 characters.

### Enabling Static Website Hosting

Now we need to enable static website hosting on our storage account. We'll use the blob service-properties update command and specify the index and 404 documents:

```
az storage blob service-properties update --static-website --404-document 404.html --index-document index.html --account-name [STORAGE_ACCOUNT_NAME]
```

Notice that we're specifying two important files:
- **index.html** - The default page that loads when users visit the root URL
- **404.html** - The custom error page for missing content

### Understanding the Static Website Container

After enabling static website hosting, Azure automatically creates a special container called dollar-web. This container has a unique property - while the blobs inside aren't directly accessible via the blob endpoint, they're served through the static website endpoint.

Open the Storage Account in the Azure Portal and navigate to the Static website blade. You'll notice:
- A unique primary endpoint URL for your static website
- The dollar-web container has been created automatically
- The endpoint domain is different from the standard blob storage domain

If you browse to the URL now, you'll see a 404 error stating "Requested content does not exist". This is expected - we haven't uploaded any content yet.

### Uploading Web Content

Now let's upload our website files. We have HTML, CSS, and image files in our web directory that we need to upload to the dollar-web container.

Using the Azure CLI, we can upload multiple files at once with the upload-batch command:

```
az storage blob upload-batch -d '$web' -s [LOCAL_PATH_TO_WEB_FILES] --account-name [STORAGE_ACCOUNT_NAME]
```

After the upload completes, refresh your browser at the static website URL. You should now see the home page of your site. Try navigating to a non-existent path, like slash-missing, and you'll see your custom 404 page instead of the default Azure error.

### Understanding Public Access

Here's an important security consideration. Even though the website is publicly accessible via the static website endpoint, the blobs themselves aren't publicly accessible via the standard blob endpoint.

Let's demonstrate this. Find the blob URL for index.html in the portal - it will look like:

```
https://[STORAGE_ACCOUNT_NAME].blob.core.windows.net/$web/index.html
```

Try downloading it with curl:

```
curl -o download.html 'https://[STORAGE_ACCOUNT_NAME].blob.core.windows.net/$web/index.html'
cat download.html
```

You'll get an XML error file. The pages must be accessed via the static website domain, not the blob endpoint. Try again with the public URL:

```
curl -o download2.html https://[STATIC_WEB_DOMAIN]/index.html
cat download2.html
```

This time you'll get the actual HTML content. This distinction is important for security and access control.

## Exercise 2: Geo-Replication for High Availability

### Upgrading to RA-GRS

Static websites are excellent candidates for geo-redundant storage because they need to be highly available but typically don't require low-latency writes. Let's upgrade our storage account to read-access geo-redundant storage, or RA-GRS.

```
az storage account update -g [RESOURCE_GROUP_NAME] --sku Standard_RAGRS -n [STORAGE_ACCOUNT_NAME]
```

With RA-GRS, your content is automatically replicated to a secondary region hundreds of miles away. The secondary endpoint is read-only, but provides an additional access point if the primary region becomes unavailable.

### Understanding Secondary Endpoints

After the update completes, examine the output. You'll see secondary endpoints including one for the static website. The secondary region is automatically paired with your primary region by Azure.

Try accessing the site from the secondary endpoint:

```
curl -v https://[SECONDARY_WEB_ENDPOINT]/
```

You might get an error initially. Geo-replication isn't instantaneous - it takes time for data to synchronize to the secondary region.

### Monitoring Replication Status

You can check the replication status in the Azure Portal by navigating to the Redundancy tab of your storage account. You'll see metrics showing when the last synchronization occurred.

You can also query the last sync time programmatically:

```
az storage account show -g [RESOURCE_GROUP_NAME] --expand geoReplicationStats --query geoReplicationStats.lastSyncTime -o tsv -n [STORAGE_ACCOUNT_NAME]
```

If you see "Last sync time is unavailable", the account is still performing its initial sync. This can take several minutes to hours depending on the amount of data.

Once replication is complete, you'll have two geographically distributed endpoints serving your static website, providing better availability and disaster recovery capabilities.

## Exercise 3: Global Distribution with Azure CDN

### Understanding Azure CDN

Azure Content Delivery Network is a globally distributed network of servers that can cache your static content at edge locations around the world. When users access your site, they're served from the nearest CDN point of presence, reducing latency and improving performance.

### Creating a CDN Profile and Endpoint

Let's create a CDN profile using the Microsoft CDN SKU:

```
az cdn profile create --sku Standard_Microsoft -g [RESOURCE_GROUP_NAME] -n [CDN_PROFILE_NAME]
```

Now create an endpoint that points to your static website:

```
az cdn endpoint create -g [RESOURCE_GROUP_NAME] --profile-name [CDN_PROFILE_NAME] --origin [STATIC_WEBSITE_DOMAIN] --origin-host-header [STATIC_WEBSITE_DOMAIN] -n [CDN_ENDPOINT_NAME]
```

The origin-host-header parameter is important - it ensures the CDN sends the correct host header when requesting content from your storage account.

### Waiting for CDN Propagation

After creating the endpoint, navigate to the CDN URL in your browser:

```
https://[CDN_ENDPOINT_NAME].azureedge.net
```

You might see an error message initially. The CDN needs time to replicate your content across its global network. This process is called propagation and can take several minutes.

Keep refreshing the page. Once you can see your website, it means the CDN is fully provisioned and your content is being served from an edge location close to your geographic location.

### Understanding CDN Caching

The CDN caches content aggressively to improve performance. Let's see this in action by updating our website content.

Upload new content to the storage account:

```
az storage blob upload-batch -d '$web' -s [PATH_TO_UPDATED_WEB_FILES] --overwrite --account-name [STORAGE_ACCOUNT_NAME]
```

Now check your various URLs:

- The primary static website URL shows the updated content immediately
- The secondary endpoint might update quickly, assuming the initial geo-replication has completed
- The CDN endpoint continues showing the old content because it's cached

The CDN caching behavior is intentional - it reduces load on the origin and improves performance. However, when you need to force an update, you'll need to purge the CDN cache, which we'll explore in the lab exercise.

## Summary

In these exercises, we've covered:
- Enabling static website hosting on Azure Storage
- Understanding the dollar-web container and access patterns
- Implementing geo-replication for high availability
- Setting up Azure CDN for global content delivery
- Understanding caching behavior and content propagation

These skills are essential for building scalable, highly available web applications on Azure.
