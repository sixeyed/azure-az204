---
theme: default
layout: cover
---

# Kubernetes ConfigMaps

<div class="abs-bottom-4">
  <iconify-icon icon="logos:kubernetes" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Kubernetes ConfigMaps - Introduction Script

<div class="text-xl mt-8" v-click>

**Duration:** 2-3 minutes
**Format:** Presentation with slides

</div>

---

---
layout: center
---

# Slide 1: Title Slide

<div class="text-xl mt-8" v-click>

*[SHOW ON SCREEN: "Kubernetes ConfigMaps - Externalizing Application Configuration"]*

</div>

---

---
layout: center
---

# Slide 2: What Are ConfigMaps?

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

*[SHOW ON SCREEN: ConfigMap icon and definition]*...

</div>

---

---
layout: center
---

# Slide 3: Why ConfigMaps Matter

<div class="text-xl mt-8" v-click>

*[SHOW ON SCREEN: Diagram showing container image + ConfigMap = Configured application]*

</div>

---

---
layout: center
---

# Slide 4: ConfigMaps in Azure Kubernetes Service

<div class="text-xl mt-8" v-click>

*[SHOW ON SCREEN: Azure Kubernetes Service logo with ConfigMap integration]*

</div>

---

---
layout: center
---

# Slide 5: Two Methods of Using ConfigMaps

<div class="text-xl mt-8" v-click>

*[SHOW ON SCREEN: Split screen showing Environment Variables vs. Volume Mounts]*

</div>

---

---
layout: center
---

# Slide 6: AZ-204 Exam Connection

<div class="text-xl mt-8" v-click>

*[SHOW ON SCREEN: AZ-204 exam topics checklist]*

</div>

---

---
layout: center
---

# Slide 7: What You'll Learn Today

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> on lab, you'll work with a real application that reads configuration from multiple sources. You'll create ConfigMaps using YAML manifests, inject them as environment variables, mount them as files, and see how configuration hierarchy affects which settings take precedence.
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> --
</div>

</div>