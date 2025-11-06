---
theme: default
layout: cover
---

# Kubernetes Services

<div class="abs-bottom-4">
  <iconify-icon icon="logos:kubernetes" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Kubernetes Services - Introduction Script

<div class="text-xl mt-8" v-click>

**Duration:** 2-3 minutes
**Target:** AZ-204 candidates learning Kubernetes networking

</div>

---

---
layout: center
---

# SLIDE 1: Title Slide

<div class="text-xl mt-8" v-click>

[On screen: "Kubernetes Services - Networking Made Simple"]

</div>

---

---
layout: center
---

# SLIDE 2: The Problem - Pod IP Addresses

<div class="text-xl mt-8" v-click>

[On screen: Diagram showing Pods with dynamic IP addresses being created and destroyed]

</div>

---

---
layout: center
---

# SLIDE 3: What is a Kubernetes Service?

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

[On screen: Service icon with stable IP and DNS name connected to multiple Pods]...

</div>

---

---
layout: center
---

# SLIDE 4: Service Type - ClusterIP

<div class="text-xl mt-8" v-click>

[On screen: Diagram showing ClusterIP Service with internal cluster communication]

</div>

---

---
layout: center
---

# SLIDE 5: Service Type - NodePort

<div class="text-xl mt-8" v-click>

[On screen: Diagram showing NodePort Service exposing port on all nodes]

</div>

---

---
layout: center
---

# SLIDE 6: Service Type - LoadBalancer

<div class="text-xl mt-8" v-click>

[On screen: Diagram showing LoadBalancer Service with cloud provider integration]

</div>

---

---
layout: center
---

# SLIDE 7: Service Discovery with DNS

<div class="text-xl mt-8" v-click>

[On screen: Diagram showing DNS resolution flow from Pod to Service]

</div>

---

---
layout: center
---

# SLIDE 8: AZ-204 Exam Relevance

<div class="text-xl mt-8" v-click>

[On screen: List of AZ-204 topics related to Kubernetes Services]

</div>

---

---
layout: center
---

# SLIDE 9: What's Next

<div class="text-xl mt-8" v-click>

[On screen: "Hands-On Lab - Let's Build Services Together"]

</div>

---

---
layout: center
---

# SLIDE 10: Summary

<div class="text-xl mt-8" v-click>

[On screen: Key takeaways bullet points]

</div>