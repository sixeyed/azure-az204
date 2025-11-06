---
theme: default
layout: cover
---

# API Management: Request and Response Policies

<div class="abs-bottom-4">
  <iconify-icon icon="carbon:api" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# API Management: Request and Response Policies - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this lab on API Management policies for requests and responses.

</div>

---

---
layout: center
---

# What Are APIM Policies?

<div v-click>

```mermaid
graph LR
    A[Your Application] --> B[Package as Container]
    B --> C[Deploy to Azure]
    C --> D[Running in Cloud]

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
```

</div>

<div class="mt-8 text-center" v-click>

Policies are the plug-in features in API Management that let you change the behavior of API operations without modifying the backend code....

</div>

---

---
layout: center
---

# What We've Done So Far

<div class="text-xl mt-8" v-click>

In previous labs, we've already used a few policies - for caching and sending mocked responses. But there are other policies you should always look to add because they increase the security of your AP

</div>

---

---
layout: center
---

# Today's Lab

<div class="text-xl mt-8" v-click>

In this lab, we'll present a public API through APIM, using policies to enhance security.

</div>

---

---
layout: center
---

# The Backend: SWAPI

<div class="text-xl mt-8" v-click>

We'll be working with SWAPI - the Star Wars API. This is a public REST API popular with developers that returns information about characters, places, and other data types from the Star Wars films.

</div>