---
theme: default
layout: cover
---

# Static Websites with Azure Storage Blobs

<div class="abs-bottom-4">
  <iconify-icon icon="vscode-icons:file-type-azure" style="font-size: 4rem;" />
</div>

---

---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

Welcome to this lab on hosting static websites with Azure Storage Blobs

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>

---

---
layout: center
---

# What are Static Websites on Azure Storage?

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

Azure Storage Blobs provide a cost-effective and scalable solution for hosting static web content. You can upload HTML files, JavaScript, CSS, images,...

</div>

---

---
layout: two-cols
---

# Key Benefits

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Serverless Architecture: - No web server to manage, update, or scale
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Cost Effective: - Pay only for the storage you use
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> High Availability: - Built-in redundancy options keep your site accessible
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Scalability: - Handle traffic spikes automatically
</div>

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-green-500" /> Global Reach: - Combine with CDN for worldwide content delivery
</div>

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>

---

---
layout: center
---

# What We'll Cover

<div v-click>

```mermaid
graph LR
    A[Deploy a static website]
    B[Upload web content]
    C[Configure geo-replication]
    D[Set up Azure CDN]
    E[Manage content updates]
    A --> B
    B --> C
    C --> D
    D --> E

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
    style E fill:#fce4ec,stroke:#e91e63
```

</div>

---

---
layout: center
---

# Use Cases

<div class="grid grid-cols-1 gap-4 mt-8">

<div v-click>
<iconify-icon icon="mdi:web" /> Marketing and promotional sites
</div>

<div v-click>
<iconify-icon icon="mdi:cog" /> Documentation portals
</div>

<div v-click>
<iconify-icon icon="mdi:code-braces" /> Single Page Applications (SPAs)
</div>

<div v-click>
<iconify-icon icon="mdi:test-tube" /> Personal blogs and portfolios
</div>

<div v-click>
<iconify-icon icon="mdi:lightning-bolt" /> Event landing pages
</div>

</div>

---

---
layout: center
---

# What You'll Need

<div class="text-xl mt-8" v-click>

To complete this lab, you'll need:

</div>