
We've covered the distinction between revisions (non-breaking changes) and versions (breaking changes), and how APIM integrates with App Service deployment slots. Now let's evolve an API through its lifecycle.

You'll start by deploying version 1.0 to Azure App Service (Standard S1 SKU, which provides 5 deployment slots). Then you'll create the API in APIM from the OpenAPI specification with header-based versioning (clients specify x-api-version header).

Next, you'll create a "blue" deployment slot for version 1.1 development. This slot runs independently with its own URL. You'll add revision 2 to your APIM API with optional min/max query parameters, pointing the backend URL to the blue slot. You'll test using ;rev=2 URL syntax - this special syntax lets you test revisions before making them current. Once validated, you'll make revision 2 the current version.

Then comes the big change: deploying version 2.0 to a "green" slot with required parameters and validation. This is a breaking change - clients that don't provide min/max parameters will get errors. You'll configure this as a new APIM version (not revision) so clients can specify x-api-version: 2.0 in their requests.

The key learning moment: running multiple versions simultaneously. Version 1.1 accepts optional parameters (backward compatible), while version 2.0 requires them (breaking change). Each points to a different deployment slot with different backend code. Clients can migrate to v2.0 on their own schedule.

You'll also explore the challenge: APIM backend URLs are hard-coded to specific slot names (blue or green). This affects true blue-green deployment where you swap slots - the APIM backend URL doesn't automatically update to follow the swap.

Let's evolve an API through revisions and versions!
