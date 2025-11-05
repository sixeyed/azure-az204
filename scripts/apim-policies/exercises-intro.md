# API Management - Policies - Exercises Introduction

We've covered how APIM policies are plug-in features that modify API behavior without backend code changes. Now let's use policies to secure and optimize a third-party API.

## What You'll Do

You'll start by **exploring the SWAPI backend** (Star Wars API) directly to identify security issues. You'll discover the Server header reveals the nginx version (valuable information for attackers), and response bodies contain direct backend URLs (allowing clients to bypass APIM entirely and hit the backend directly).

Then you'll **create a manual HTTP API in APIM** pointing to https://swapi.dev/api as the backend. Unlike importing from OpenAPI, this gives you more control over policy configuration. Now comes the interesting part: **configuring four security and performance policies**.

**Response caching** (86400 seconds - 24 hours) improves performance dramatically for this static Star Wars data and respects the free service's bandwidth limitations. You'll see subsequent requests return instantly from cache.

**Server header removal** uses set-header with delete action to eliminate the security issue where clients can see the backend technology stack. **Custom x-server header addition** adds your own header identifying responses came through APIM, helping you verify policies are working.

**Find-and-replace in the outbound section** is the most powerful policy here - it rewrites all backend URLs in response bodies to point to your APIM gateway instead. This prevents clients from discovering and bypassing APIM to hit the backend directly.

You'll **publish through a product requiring subscription keys**, then **test authentication** (401 without key, 200 with valid key). You'll **verify all policies are functioning** - headers modified correctly, URLs rewritten to your gateway domain, and observe the dramatic caching performance improvement on subsequent requests.

Let's secure a third-party API with policies!
