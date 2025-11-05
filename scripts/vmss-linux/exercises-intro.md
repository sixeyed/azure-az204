# Virtual Machine Scale Sets - Linux: Exercises Introduction

We've covered the power of cloud-init for automated deployment and why it's a flexible approach for VM Scale Sets. Now let's use cloud-init scripts to deploy and configure applications automatically across multiple Linux instances.

## What You'll Do

You'll start by creating a single VM with a cloud-init script to understand the automation system. The script installs Nginx automatically during provisioning, and you'll verify execution by examining the cloud-init logs.

Then you'll create a full VM Scale Set with three instances, each running Nginx configured by an advanced cloud-init script that embeds the VM hostname into the web page. This lets you see load balancing in action as different instances respond to your requests.

You'll configure the load balancer by creating health probes for port 80 and load balancer rules to distribute HTTP traffic. Then you'll test the deployment with curl to see responses from all three instances.

Next, you'll update the VMSS model with new cloud-init content and learn the critical difference between updating the model and updating instances. You'll scale up to see how new instances use the updated configuration while old instances keep their original setup.

The key learning: The VMSS model is the desired state, but changes don't automatically apply to running instances - you control when updates roll out, which is crucial for managing service availability during deployments.
