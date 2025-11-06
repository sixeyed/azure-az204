---
theme: default
layout: cover
---

# Event Hubs Partitioned Consumers

<div class="abs-bottom-4">
  <iconify-icon icon="carbon:event" style="font-size: 4rem;" />
</div>

---

---
layout: center
---

# Event Hubs Partitioned Consumers - Introduction

<div class="text-xl mt-8" v-click>

Welcome to this lab on Event Hubs Partitioned Consumers. In this session, we'll explore how to process a partitioned stream of events reliably using Azure Event Hubs.

</div>

---

---
layout: center
---

# What You'll Learn

<div class="mt-8">

<div v-click>
<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> especially when dealing with partitioned data streams.
</div>

</div>

---

---
layout: center
---

# The Challenge

<div class="text-xl mt-8" v-click>

When processing streams of events, you need to solve several problems:

</div>

---

---
layout: center
---

# The Solution

<div class="text-xl mt-8" v-click>

Microsoft has built this logic into the Event Hubs client libraries. The library handles:

</div>

---

---
layout: center
---

# What We'll Build

<div class="text-xl mt-8" v-click>

In this lab, we'll work with a device logging scenario. We'll:

</div>

---

---
layout: center
---

# Key Concepts

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click>
<h3 class="text-xl font-bold">Partitions</h3>
<p class="text-sm">Event Hubs splits the event stream into multiple partitions. This allows parallel processing and inc</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Consumer Groups</h3>
<p class="text-sm">These are logical views of the event stream. Different consumer groups can process the same events a</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">Checkpoints</h3>
<p class="text-sm">Consumers periodically record their position in the event stream by storing the offset in blob stora</p>
</div>

<div v-click>
<h3 class="text-xl font-bold">At-Least-Once Delivery</h3>
<p class="text-sm">The Event Hubs consumer pattern guarantees that every event will be processed at least once. However</p>
</div>

</div>