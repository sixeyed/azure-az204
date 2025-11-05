# APIM Versioning - Quickfire Questions

## Question 1
Why is API versioning important?

- A) Not important
- B) Allows API evolution while maintaining backward compatibility for existing consumers
- C) Only for documentation
- D) Marketing purposes

**Answer: B**
Versioning enables adding features or breaking changes without disrupting existing API consumers.

---

## Question 2
What versioning schemes does APIM support?

- A) Only one scheme
- B) Path, Query string, Header
- C) Only path-based
- D) No versioning

**Answer: B**
Path (/v1/api), Query (?api-version=1), or Header (api-version: 1) versioning schemes.

---

## Question 3
What is path-based versioning?

- A) File path versioning
- B) Version identifier in URL path (e.g., /v1/products)
- C) Query parameter
- D) Header-based

**Answer: B**
Path versioning includes version in URL: `/v1/products`, `/v2/products` - most visible and cacheable.

---

## Question 4
What is query string versioning?

- A) Database queries
- B) Version specified as query parameter (e.g., ?api-version=1)
- C) Path-based
- D) Header-based

**Answer: B**
Version passed as query parameter: `/products?api-version=2` - less visible than path.

---

## Question 5
What is header-based versioning?

- A) HTTP status codes
- B) Version specified in custom HTTP header (e.g., api-version: 1)
- C) Query parameter
- D) URL path

**Answer: B**
Version in header: `api-version: 2` - keeps URLs clean but less visible for caching.

---

## Question 6
What is the difference between version and revision?

- A) Same thing
- B) Versions are breaking changes (separate entries); revisions are non-breaking iterations
- C) Revisions are major changes
- D) No difference

**Answer: B**
Versions (v1, v2) for breaking changes with separate catalog entries. Revisions for non-breaking updates to same version.

---

## Question 7
Can you have multiple versions active simultaneously?

- A) No, only one
- B) Yes, multiple versions can coexist for different consumers
- C) Maximum 2
- D) Requires downtime

**Answer: B**
Multiple API versions run simultaneously, allowing gradual migration from old to new versions.

---

## Question 8
What is a version set?

- A) A backup copy
- B) Logical grouping of related API versions sharing common configuration
- C) Security setting
- D) Deployment package

**Answer: B**
Version set groups related API versions, specifying versioning scheme and other shared settings.

---

## Question 9
How can you deprecate an API version?

- A) Immediate deletion
- B) Mark as deprecated and communicate sunset timeline to consumers
- C) Cannot deprecate
- D) Automatic removal

**Answer: B**
Set deprecation flag, update documentation, notify consumers, provide migration path and sunset date.

---

## Question 10
What is semantic versioning?

- A) APIM-specific versioning
- B) Versioning scheme using MAJOR.MINOR.PATCH (e.g., 2.1.3)
- C) Random versioning
- D) Date-based versioning

**Answer: B**
Semantic versioning (semver) uses MAJOR (breaking), MINOR (features), PATCH (fixes) - commonly adopted convention.
