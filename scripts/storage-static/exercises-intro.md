# Static Websites with Azure Storage - Exercises Introduction

We've covered Azure Storage static website hosting as a cost-effective, scalable solution for hosting static web content without managing traditional web servers - uploading HTML, JavaScript, CSS, and images as blobs with public web access. Now let's deploy and distribute a static website globally.

## What You'll Do

You'll start by **deploying a static website** by enabling static website hosting on a storage account using `az storage blob service-properties update`. This creates the special $web container with unique properties: blobs inside aren't directly accessible via standard blob endpoint but are served through the static website endpoint instead. You'll specify index.html as the default landing page and 404.html as the custom error page.

Then you'll **upload web content** using `az storage blob upload-batch` to the $web container, preserving directory structure from local files. Once uploaded, your site loads correctly with all styles and images. You'll understand the dual access model: blob endpoint access is NOT publicly accessible even when static website is enabled, but static website endpoint access provides public access through the dedicated static website domain.

You'll **implement geo-replication for high availability** by upgrading to RA-GRS (Read-Access Geo-Redundant Storage). Your content is automatically replicated to a secondary region hundreds of miles away. The secondary endpoint is read-only but provides additional access if the primary region becomes unavailable. Geo-replication isn't instantaneous - you'll monitor replication status checking lastSyncTime to verify synchronization completion.

Next comes **global distribution with Azure CDN** by creating a CDN profile and endpoint pointing to your static website. The CDN caches content at edge locations worldwide, serving users from the nearest point of presence rather than your storage account directly. This reduces latency, improves performance, reduces load on origin, and provides better scalability. The origin-host-header parameter ensures the CDN sends correct host headers when requesting content.

You'll **understand CDN caching behavior** by uploading new content and observing that the origin shows updates immediately but the CDN continues showing cached content. This aggressive caching is intentional for performance but requires purge operations with `az cdn endpoint purge` to force CDN cache refresh and push new content immediately to all edge locations.

The key learning: Static websites on Azure Storage are serverless and cost-effective, requiring no server management. Combined with CDN, they provide excellent performance globally with automatic scaling. Geo-replication adds high availability and disaster recovery built-in.

Let's build scalable static websites!
