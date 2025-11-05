# API Management - Versioning - AZ-204 Exam Introduction

Excellent work with API versioning! This topic combines APIM versioning concepts with App Service deployment slots - both are important AZ-204 exam areas.

## What We'll Cover

**Three versioning schemes** are fundamental: Header (clients send custom header like x-api-version: 2.0), Query string (clients send parameter like ?api-version=2.0), and Path (URL includes version like /v2/endpoint). Each has tradeoffs. Header is cleanest but requires header manipulation. Query is simple but clutters URLs. Path is most visible but requires more URL management. The exam tests when to choose each scheme.

**Revisions vs Versions** is the critical distinction. Revisions are for non-breaking changes (optional parameters, bug fixes, performance improvements) - clients don't need to change anything. Revisions are tested using ;rev=N URL syntax before making them current. Versions are for breaking changes (required parameters, removed endpoints, changed response formats) - clients must update their code. Versions create new URL paths/identifiers requiring explicit client migration. The exam tests whether you recognize breaking vs non-breaking changes and choose revision or version appropriately.

**Integration with App Service deployment slots** enables running multiple code versions. Each slot has an independent URL (production: myapp.azurewebsites.net, blue: myapp-blue.azurewebsites.net). In APIM, you configure backend URLs to point to specific slots, allowing version 1.1 to call the blue slot while version 2.0 calls the green slot. The exam may test understanding of slot URLs and how APIM backend configuration integrates with them.

**Semantic versioning practices** should be understood: Major.Minor format (1.0, 1.1, 2.0). Major version changes for breaking changes, minor version changes for non-breaking additions. The exam doesn't test semantic versioning deeply, but questions may reference it in scenarios.

**OpenAPI specification imports** create APIs with all operations defined automatically. The exam tests that you know APIs can be created from OpenAPI/Swagger files, and that the specification defines endpoints, parameters, request/response schemas, and security requirements. You should recognize when to use automated import versus manual API creation.

**Best practices** the exam expects you to know: version from day one (don't add versioning later), document all changes comprehensively, test revisions before making them current (;rev=N syntax), support multiple versions simultaneously during migration periods, deprecate old versions gracefully with clear timelines, and use descriptive version identifiers (v1, v2 or 1.0, 2.0).

We'll cover **revision promotion workflow**, **version migration strategies**, **backend URL management with slots**, **common exam scenarios** about API evolution, and **troubleshooting version routing issues**.

Master API versioning for the AZ-204!
