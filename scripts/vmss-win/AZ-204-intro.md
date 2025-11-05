# Virtual Machine Scale Sets - Windows: AZ-204 Exam Focus

Great work! This Windows VMSS lab is crucial for the "Implement IaaS solutions" objective in the AZ-204 exam. Understanding when and how to use scale sets is a key competency tested in the certification.

## What We'll Cover

We'll examine VMSS orchestration modes - uniform mode where all instances are identical versus flexible mode for heterogeneous workloads. The exam focuses on uniform orchestration as the standard pattern for web applications.

We'll explore manual scaling with the az vmss scale command and autoscaling based on CPU metrics. You'll master scale-out and scale-in rules including metric thresholds, time windows, cool-down periods, and minimum/maximum instance counts.

The exam tests your knowledge of load balancer integration - how backend pools automatically contain healthy VMSS instances, the difference between load balancing rules for traffic distribution and NAT rules for direct instance access, and why health probes are essential.

You'll understand custom images with VMSS including creating images from generalized VMs, the requirement that images must be in the same region, and how all instances are created from the same image for consistency.

We'll cover high availability concepts including availability zones for datacenter-level protection, update domains and fault domains for resilience, and overprovisioning to reduce scale-out time.

The exam expects you to know when to choose VMSS versus other options, cost optimization through autoscaling, and monitoring with Azure Monitor.

Master VMSS creation, scaling, and load balancing for the AZ-204!
