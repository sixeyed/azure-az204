# Docker Multi-Stage Builds - Quickfire Questions

## Question 1
What is a multi-stage Docker build?

- A) Building multiple images
- B) Using multiple FROM statements in a Dockerfile to create intermediate stages and optimize final image
- C) Running builds in parallel
- D) Building in multiple regions

**Answer: B**
Multi-stage builds use multiple FROM statements, allowing you to build in one stage and copy artifacts to a smaller final stage.

---

## Question 2
What are the benefits of multi-stage builds?

- A) Faster builds only
- B) Smaller final images by excluding build tools and intermediate artifacts
- C) Better colors
- D) Automatic testing

**Answer: B**
Multi-stage builds reduce final image size by separating build-time dependencies from runtime dependencies.

---

## Question 3
What instruction copies files from one stage to another?

- A) COPY --from=stage
- B) MOVE --from=stage
- C) TRANSFER --from=stage
- D) GET --from=stage

**Answer: A**
`COPY --from=stagename /source /destination` copies files from a named or numbered build stage.

---

## Question 4
How do you name a build stage in a Dockerfile?

- A) STAGE name
- B) FROM image AS name
- C) NAME stage
- D) LABEL stage=name

**Answer: B**
`FROM node:18 AS build` creates a named stage called "build" that can be referenced later.

---

## Question 5
What is a common pattern for multi-stage builds with compiled languages?

- A) Single stage with all tools
- B) Build stage (with compiler/SDK) → Runtime stage (with minimal runtime only)
- C) Test stage only
- D) Documentation stage

**Answer: B**
Typical pattern: Build stage with full SDK compiles the app, runtime stage copies only the compiled output with minimal runtime.

---

## Question 6
Which base image is commonly used for minimal final stages?

- A) ubuntu:latest
- B) alpine, distroless, or scratch
- C) windows:latest
- D) centos:latest

**Answer: B**
Alpine Linux, Google's distroless images, or scratch (empty image) are used for minimal final images.

---

## Question 7
Can you build only a specific stage?

- A) No, always builds all stages
- B) Yes, using `docker build --target stagename`
- C) Only in Enterprise edition
- D) Only with special tools

**Answer: B**
`docker build --target build` builds only up to and including the specified stage, useful for testing build stages.

---

## Question 8
What is the scratch image?

- A) A damaged image
- B) An empty base image with no OS files, for ultra-minimal containers
- C) A test image
- D) A cache image

**Answer: B**
`FROM scratch` creates an empty image. Useful for compiled binaries that don't need an OS (like Go static binaries).

---

## Question 9
Do earlier stages affect the final image size if not referenced?

- A) Yes, they're included in final image
- B) No, only the final stage and referenced artifacts are in the final image
- C) Sometimes
- D) Only on Windows

**Answer: B**
Intermediate stages and their layers are not included in the final image unless explicitly copied.

---

## Question 10
What is layer caching in Docker builds?

- A) A pricing tier
- B) Docker reuses unchanged layers from previous builds to speed up builds
- C) RAM allocation
- D) Network caching

**Answer: B**
Docker caches each layer. If a layer hasn't changed, it's reused, significantly speeding up subsequent builds.
