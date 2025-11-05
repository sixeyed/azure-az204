# Virtual Machine Scale Sets - Windows: Exercises Introduction

We've covered what Virtual Machine Scale Sets are and why managing multiple instances as a single resource simplifies operations at scale. Now let's build a Windows VMSS from a custom image and explore scaling capabilities.

## What You'll Do

You'll start by verifying prerequisites from the VM images lab - the custom Windows image with IIS pre-installed. Then you'll create a VMSS with three instances from that image using the CLI.

You'll explore the resources Azure creates automatically including the scale set itself, load balancer, public IP, and networking components. You'll notice that instances aren't individual VM resources but are managed through the VMSS.

Next, you'll configure load balancing by creating health probes and load balancer rules in the Portal. Without these configurations, the load balancer doesn't know how to route traffic even though the backend pool is correctly populated.

You'll test the application to see different instances responding, then manually scale up to five instances with a single command. You'll observe overprovisioning - Azure creates extra instances temporarily to ensure the desired count reaches healthy status quickly.

Then you'll configure autoscaling based on CPU metrics with scale-out and scale-in rules. You'll watch as Azure automatically adjusts capacity based on load, removing instances when they exceed the maximum or fall below minimum thresholds.

The key learning: VMSS provides centralized management with automatic load balancing and flexible scaling - both manual control and metric-based autoscaling to handle varying workloads efficiently.
