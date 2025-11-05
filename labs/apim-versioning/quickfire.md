# APIM Versioning - Quickfire Questions

## Question 1
Why is API versioning important?


- A) Only for documentation
- B) Not important
- C) Marketing purposes
- D) Allows API evolution while maintaining backward compatibility for existing consumers

**Answer: D**
Versioning enables adding features or breaking changes without disrupting existing API consumers.
---
## Question 2
What versioning schemes does APIM support?


- A) No versioning
- B) Path, Query string, Header
- C) Only one scheme
- D) Only path-based

**Answer: B**
Path (/v1/api), Query (?api-version=1), or Header (api-version: 1) versioning schemes.
---
## Question 3
What is path-based versioning?


- A) Version identifier in URL path (e.g., /v1/products)
- B) Query parameter
- C) Header-based
- D) File path versioning

**Answer: A**
Path versioning includes version in URL: `/v1/products`, `/v2/products` - most visible and cacheable.
---
## Question 4
What is query string versioning?


- A) Path-based
- B) Version specified as query parameter (e.g., ?api-version=1)
- C) Database queries
- D) Header-based

**Answer: B**
Version passed as query parameter: `/products?api-version=2` - less visible than path.
---
## Question 5
What is header-based versioning?


- A) HTTP status codes
- B) URL path
- C) Query parameter
- D) Version specified in custom HTTP header (e.g., api-version: 1)

**Answer: D**
Version in header: `api-version: 2` - keeps URLs clean but less visible for caching.
---
## Question 6
What is the difference between version and revision?


- A) No difference
- B) Versions are breaking changes (separate entries); revisions are non-breaking iterations
- C) Revisions are major changes
- D) Same thing

**Answer: B**
Versions (v1, v2) for breaking changes with separate catalog entries. Revisions for non-breaking updates to same version.
---
## Question 7
Can you have multiple versions active simultaneously?


- A) Maximum 2
- B) Requires downtime
- C) No, only one
- D) Yes, multiple versions can coexist for different consumers

**Answer: D**
Multiple API versions run simultaneously, allowing gradual migration from old to new versions.
---
## Question 8
What is a version set?


- A) Logical grouping of related API versions sharing common configuration
- B) Deployment package
- C) A backup copy
- D) Security setting

**Answer: A**
Version set groups related API versions, specifying versioning scheme and other shared settings.
---
## Question 9
How can you deprecate an API version?


- A) Cannot deprecate
- B) Immediate deletion
- C) Automatic removal
- D) Mark as deprecated and communicate sunset timeline to consumers

**Answer: D**
Set deprecation flag, update documentation, notify consumers, provide migration path and sunset date.
---
## Question 10
What is semantic versioning?


- A) Random versioning
- B) APIM-specific versioning
- C) Versioning scheme using MAJOR.MINOR.PATCH (e.g., 2.1.3)
- D) Date-based versioning

**Answer: C**
Semantic versioning (semver) uses MAJOR (breaking), MINOR (features), PATCH (fixes) - commonly adopted convention.