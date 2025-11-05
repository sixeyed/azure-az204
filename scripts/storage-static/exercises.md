# Static Websites with Azure Storage Blobs - Exercises

## Exercise 1: Deploy a Static Website

### Creating the Storage Account

Let's begin by creating a resource group and storage account. We'll use the Azure CLI to create our resources with infrastructure-as-code principles.

First, create a resource group in your preferred region. We're using az group create with -n for your resource group name, --tags courselabs=azure for tracking our course resources, and -l for your chosen region like eastus or westeurope.

Next, create a storage account with locally redundant storage. We're using az storage account create with -g for your resource group name, --sku Standard_LRS for locally redundant storage which is cost-effective for static websites, and -n for your storage account name. Remember that storage account names must be globally unique across all of Azure and between 3 and 24 characters - only lowercase letters and numbers are allowed, no special characters or uppercase letters.

### Enabling Static Website Hosting

Now we need to enable static website hosting on our storage account. This is a special feature that turns blob storage into a web server. We'll use the blob service-properties update command and specify the index and 404 documents. We're running az storage blob service-properties update with --static-website to enable the feature, --404-document 404.html for the custom error page, --index-document index.html as the default landing page, and --account-name for your storage account.

Notice that we're specifying two important files. The index.html file is the default page that loads when users visit the root URL or any directory without specifying a file - this is standard web server behavior. The 404.html file is the custom error page for missing content, giving you control over what users see when they request a file that doesn't exist.

### Understanding the Static Website Container

After enabling static website hosting, Azure automatically creates a special container called dollar-web. This container has a unique property - while the blobs inside aren't directly accessible via the standard blob endpoint, they're served through the static website endpoint instead. This separation provides better security and cleaner URLs.

Open the Storage Account in the Azure Portal and navigate to the Static website blade under Data management. You'll notice a unique primary endpoint URL for your static website displayed at the top. The dollar-web container has been created automatically under Containers. And the endpoint domain is different from the standard blob storage domain - it's optimized for web serving rather than blob access.

If you browse to the static website URL now, you'll see a 404 error stating "Requested content does not exist". This is expected - we haven't uploaded any content yet, so there's nothing to serve.

### Uploading Web Content

Now let's upload our website files. We have HTML, CSS, and image files in our web directory that we need to upload to the dollar-web container to make them accessible.

Using the Azure CLI, we can upload multiple files at once with the upload-batch command. We're using az storage blob upload-batch with -d '$web' as the destination container - note the single quotes around the dollar sign which is necessary for shell escaping, -s for your local path to web files, and --account-name for your storage account. This preserves the directory structure from your local files.

After the upload completes, refresh your browser at the static website URL. You should now see the home page of your site loading correctly with all styles and images. Try navigating to a non-existent path, like /missing or /test, and you'll see your custom 404 page instead of the default Azure error. This demonstrates that your static website is fully functional and serving content correctly.

### Understanding Public Access

Here's an important security consideration to understand. Even though the website is publicly accessible via the static website endpoint, the blobs themselves aren't publicly accessible via the standard blob endpoint. This is a security feature that gives you control.

Let's demonstrate this. Find the blob URL for index.html in the portal by navigating to Containers, clicking on $web, finding index.html, and viewing its properties. The blob URL will look like: https://your-storage-account-name.blob.core.windows.net/$web/index.html - this is the blob storage endpoint, not the static website endpoint.

Try downloading it with curl. We're using curl with -o download.html to save output, followed by the blob URL in single quotes. Then cat download.html to view what we got. You'll get an XML error file indicating the blob is not accessible. The pages must be accessed via the static website domain, not the blob endpoint directly. This provides a security boundary.

Try again with the static website URL instead. Use curl with -o download2.html and your static website URL path like https://your-static-website-domain/index.html, then cat download2.html. This time you'll get the actual HTML content successfully. This distinction is important for security and access control - you choose which endpoint serves your content.

## Exercise 2: Geo-Replication for High Availability

### Upgrading to RA-GRS

Static websites are excellent candidates for geo-redundant storage because they need to be highly available but typically don't require low-latency writes. The content is usually updated infrequently, but read access needs to be fast and reliable. Let's upgrade our storage account to read-access geo-redundant storage, or RA-GRS.

We're using az storage account update with -g for your resource group, --sku Standard_RAGRS for read-access geo-redundant storage, and -n for your storage account name. With RA-GRS, your content is automatically replicated to a secondary region hundreds of miles away from your primary region. The secondary endpoint is read-only, but provides an additional access point if the primary region becomes unavailable due to outages or disasters.

### Understanding Secondary Endpoints

After the update completes, examine the output JSON. You'll see secondary endpoints including one for the static website labeled as secondaryEndpoints with a web field. The secondary region is automatically paired with your primary region by Azure based on geographic location - for example, East US pairs with West US. You don't choose the secondary region; Azure selects optimal pairings for disaster recovery.

Try accessing the site from the secondary endpoint to see if replication has completed. Use curl with -v for verbose output and your secondary web endpoint URL. You might get an error initially indicating the content isn't available yet. Geo-replication isn't instantaneous - it takes time for data to synchronize to the secondary region, especially for the initial replication.

### Monitoring Replication Status

You can check the replication status in the Azure Portal by navigating to the Redundancy tab of your storage account. You'll see metrics showing when the last synchronization occurred and whether replication is current or behind. There's also a map showing your primary and secondary regions visually.

You can also query the last sync time programmatically using az storage account show with -g for resource group, --expand geoReplicationStats to include replication information, --query geoReplicationStats.lastSyncTime to extract just the timestamp, -o tsv for clean output, and -n for storage account name. If you see "Last sync time is unavailable", the account is still performing its initial sync. This can take several minutes to hours depending on the amount of data and current Azure load.

Once replication is complete and the lastSyncTime shows a recent timestamp, you'll have two geographically distributed endpoints serving your static website. This provides better availability with automatic failover if one region has issues, and disaster recovery capabilities protecting against regional outages. Users can access your site from either endpoint, giving you flexibility in routing and load distribution.

## Exercise 3: Global Distribution with Azure CDN

### Understanding Azure CDN

Azure Content Delivery Network is a globally distributed network of servers that can cache your static content at edge locations around the world. When users access your site, they're served from the nearest CDN point of presence rather than your storage account directly. This reduces latency significantly and improves performance, especially for users far from your storage account's region. It also reduces load on your origin storage account and provides better scalability.

### Creating a CDN Profile and Endpoint

Let's create a CDN profile using the Microsoft CDN SKU. We're using az cdn profile create with --sku Standard_Microsoft for the CDN tier - this is Microsoft's own CDN network, -g for your resource group, and -n for your CDN profile name.

Now create an endpoint that points to your static website. We're using az cdn endpoint create with -g for resource group, --profile-name for the CDN profile we just created, --origin with your static website domain without https:// prefix, --origin-host-header with the same domain to ensure the CDN sends the correct host header when requesting content from your storage account, and -n for a unique endpoint name. The origin-host-header parameter is important - it ensures the CDN sends the correct host header when requesting content from your storage account, which is required for static websites to work properly.

### Waiting for CDN Propagation

After creating the endpoint, navigate to the CDN URL in your browser. The URL will be: https://your-cdn-endpoint-name.azureedge.net - this is your CDN-accelerated URL. You might see an error message initially about the endpoint not being available yet. The CDN needs time to replicate your content configuration across its global network. This process is called propagation and can take several minutes, sometimes up to 15 minutes for full global distribution.

Keep refreshing the page periodically. Once you can see your website loading successfully, it means the CDN is fully provisioned and your content is being served from an edge location close to your geographic location. The CDN has cached your content and is now serving it with lower latency than accessing the storage account directly.

### Understanding CDN Caching

The CDN caches content aggressively to improve performance and reduce origin load. Let's see this in action by updating our website content and observing caching behavior.

Upload new content to the storage account, replacing your existing files. We're using az storage blob upload-batch with -d '$web', -s for your path to updated web files, --overwrite to replace existing files, and --account-name. This updates the files in your storage account.

Now check your various URLs and observe the differences. The primary static website URL shows the updated content immediately because you're accessing the origin directly. The secondary endpoint might update quickly as well, assuming the initial geo-replication has completed and changes replicate quickly. But the CDN endpoint continues showing the old content because it's cached at the edge locations.

The CDN caching behavior is intentional and beneficial - it reduces load on the origin storage and improves performance by serving cached content. However, when you need to force an update and push new content immediately, you'll need to purge the CDN cache. This is done using az cdn endpoint purge, specifying the profile, endpoint, and paths to purge. The purge operation tells all CDN edge locations to discard their cached copies and fetch fresh content from the origin on the next request.

## Summary

In these exercises, we've covered essential static website hosting concepts and techniques. We enabled static website hosting on Azure Storage, understanding how the dollar-web container works and how static website endpoints differ from blob endpoints. We implemented geo-replication for high availability using RA-GRS, providing disaster recovery and redundancy across regions. We set up Azure CDN for global content delivery, reducing latency for users worldwide. And we learned about caching behavior and content propagation, understanding how CDN edge locations serve content.

These skills are essential for building scalable, highly available web applications on Azure. Static websites hosted on Azure Storage are cost-effective, performant, and require no server management. Combined with CDN, they provide excellent performance globally. And with geo-replication, you get high availability and disaster recovery built in.
