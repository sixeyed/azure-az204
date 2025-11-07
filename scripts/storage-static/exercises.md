# Static Websites with Azure Storage Blobs

## Reference

Static website hosting on Azure Storage lets you host entire websites directly from blob storage without managing web servers. You can upload HTML files and static assets as blobs, and configure the blob container for public web access. You get a fast, scalable website with no server infrastructure to maintain. The documentation covers static website configuration, CDN integration, and custom domain setup. The command line interface provides complete control through az storage blob service-properties commands for configuration and az cdn commands for global distribution.

## Deploy a Static Website

Let's begin by setting up the infrastructure and enabling static website hosting.

**Create Infrastructure**: We're creating a Resource Group called "labs-storage-static" with course tracking tags and a standard storage account with locally redundant storage. Remember that storage account names must be globally unique and can only contain lowercase letters and numbers - choose a name that's unique to you.

**Enable Static Website Hosting**: We're using the blob service-properties update command to configure the storage account for static website hosting. You need to use the static-website flag and pass the file names for the main index page and the 404 error page. We're specifying 404.html as the custom error document and index.html as the default landing page. You don't need any content uploaded before you enable these settings - the configuration prepares the storage account to serve web content.

**Explore the Portal Configuration**: Let's open the Storage Account in the Portal and browse to the Static website blade. You'll notice several important details. The base URL is different from the standard blob URL - it's optimized for web serving rather than blob access. There is a new container called dollar-web, which is where the web content will need to be uploaded. This container has special properties that make it suitable for web hosting.

**Test Empty Site**: Browse to the static website URL - what do you see? The site responds, but with a standard 404 not found error saying "Requested content does not exist". This is expected because we haven't uploaded any content yet. The website infrastructure is ready, but there's nothing to serve.

**Upload Web Content**: We're uploading the contents of the labs/storage-static/web directory to the dollar-web container. You can upload multiple files in the Portal, or use the batch upload in the CLI which is much faster for multiple files. We're using az storage blob upload-batch with destination dollar-web - note the single quotes around the dollar sign which is necessary for shell escaping - source pointing to your local web directory, and account name. This preserves the directory structure from your local files.

**Verify the Site**: Refresh the browser at the static website URL - you'll see the home page loading correctly with all styles and images. Browse to any other path like /missing and you'll get the customized 404 page instead of the default Azure error. This demonstrates that your static website is fully functional and serving content correctly.

**Understanding Access Restrictions**: The blobs themselves are not publicly available even though the website is accessible. Let's verify this by finding the blob URL of the index.html file in the portal and trying to download it with curl. You'll get an XML error file saying the blob is not accessible. The pages must be accessed via the static website domain, not the blob endpoint directly. This is a security feature that gives you control over how content is accessed.

**Access via Static Website Domain**: Try again with the static website URL instead of the blob URL. This time when you examine the downloaded file, you'll see the actual HTML content successfully. This distinction is important - the static website endpoint serves your content publicly, while the blob endpoint remains protected.

## Replication to a second region

Static websites are excellent candidates for geo-redundant storage because they need high availability but typically don't require low-latency writes.

**Upgrade to RA-GRS**: We're changing the Storage Account to use read-access globally redundant storage. This means the content is replicated to a secondary region hundreds of miles away, which can be used for reads even without a failover. We're using az storage account update with the SKU parameter set to Standard_RAGRS. With RA-GRS, your content is automatically replicated to a secondary region, and the secondary endpoint is read-only but provides an additional access point if the primary region becomes unavailable.

**Understand Secondary Endpoints**: In the output you'll see the secondary location and a list of secondary endpoints, including one for the static website. The secondary region is automatically paired with your primary region by Azure based on geographic location - for example, East US pairs with West US. You don't choose the secondary region; Azure selects optimal pairings for disaster recovery. You can access the site from the secondary endpoint too, and the storage cost is lower with RA than full GRS because you can't write to the secondary.

**Test Secondary Access**: Let's try accessing the site from the secondary endpoint using curl with verbose output. You'll probably get an error because it takes a while for data to be synchronized to the secondary region. Geo-replication isn't instantaneous - the initial sync especially can take time depending on the amount of data and current Azure load.

**Check Replication Status**: Open the Storage Account in the Portal and check the Redundancy tab to see the status of the replication. You'll see metrics showing when the last synchronization occurred and whether replication is current or behind. It can take a long time for the sync to complete initially. You can check the status by querying the last sync time with az storage account show using the expand geoReplicationStats parameter and query for lastSyncTime. You'll see "Last sync time is unavailable" if the account is still performing its initial sync.

**Benefits of Replication**: Once replication is complete and the lastSyncTime shows a recent timestamp, you'll have two geographically distributed endpoints serving your static website. This provides better availability with automatic failover capabilities if one region has issues, and disaster recovery protecting against regional outages. Users can access your site from either endpoint, giving you flexibility in routing and load distribution.

## Global replication with CDN

Azure Content Delivery Network is a globally distributed network of servers that can cache your static content at edge locations around the world.

**Understanding CDN Benefits**: When users access your site, they're served from the nearest CDN point of presence rather than your storage account directly. This reduces latency significantly, especially for users far from your storage account's region, and it also reduces load on your origin storage account while providing better scalability for global traffic.

**Create CDN Profile**: Let's create a CDN profile using the Microsoft CDN SKU. We're using az cdn profile create with SKU Standard_Microsoft for the CDN tier - this is Microsoft's own CDN network with global coverage - resource group, and profile name.

**Create CDN Endpoint**: Now we're creating an endpoint that points to your static website. We're using az cdn endpoint create with the resource group, profile name from the CDN profile we just created, origin parameter set to your static website domain without the https:// prefix, and origin-host-header with the same domain. The origin-host-header parameter is important - it ensures the CDN sends the correct host header when requesting content from your storage account, which is required for static websites to work properly. Choose a unique endpoint name that will become your CDN domain.

**Wait for Propagation**: After creating the endpoint, navigate to the CDN URL in your browser - it will be https://your-cdn-endpoint-name.azureedge.net. You might see an error message initially about the endpoint not being available yet. The CDN needs time to replicate your content configuration across its global network. This process is called propagation and can take several minutes, sometimes up to fifteen minutes for full global distribution.

**Verify CDN Serving**: Keep refreshing the page periodically. Once you can see your website loading successfully, it means the CDN is fully provisioned and your content is being served from an edge location close to your geographic location. The CDN has cached your content and is now serving it with lower latency than accessing the storage account directly.

**Update Content**: Let's see CDN caching in action by updating our website content. Upload new content to the storage account by replacing your existing files with az storage blob upload-batch using the overwrite flag. This updates the files in your storage account.

**Observe Caching Behavior**: Now check your various URLs and observe the differences. The primary static website URL shows the updated content immediately because you're accessing the origin directly. The secondary endpoint might update quickly as well, assuming the initial geo-replication has completed and changes replicate quickly. But the CDN endpoint continues showing the old content because it's cached at the edge locations. The CDN caching behavior is intentional and beneficial - it reduces load on the origin storage and improves performance by serving cached content. However, when you need to force an update and push new content immediately, you'll need to purge the CDN cache.

## Lab

The purpose of the CDN is to cache content which has a heavy read profile but is not updated so regularly. The caching is quite aggressive, and sometimes you might need to force a page to be refreshed in the CDN.

**Your Challenge**: How would you force the index.html page to be refreshed in the CDN? The content has been updated in storage, but the CDN is still serving the old cached version. You need to find the command to purge specific content from the CDN cache.

**Hint**: Look at the az cdn endpoint purge command to see how to invalidate cached content. You'll need to specify which paths to purge.

## Cleanup

When you're finished with the lab, remember to clean up your resources.

**Delete Resource Group**: We're using az group delete with -y to confirm without prompting and --no-wait to return immediately without waiting for completion. This removes the entire resource group and all its contents including the storage account, CDN profile, CDN endpoint, and all website content. The deletion happens asynchronously in the background.
