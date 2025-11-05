# Virtual Machine Scale Sets - Linux: AZ-204 Exam Focus

Great work! This Linux VM Scale Set lab directly supports the "Implement IaaS solutions" domain of the AZ-204 exam. Understanding VMSS creation, configuration, and updates is essential for the certification.

## What We'll Cover

We'll examine how to create VMSS instances with custom initialization scripts using cloud-init. You'll master the custom-data parameter and the @ symbol syntax for passing script files during VM provisioning.

We'll explore load balancer configuration including health probes that monitor backend instance health, and load balancer rules that specify frontend ports, backend ports, and protocols. You'll understand why VMSS creates load balancers automatically but doesn't configure the rules.

The exam tests your understanding of the VMSS model and instance lifecycle - how model updates don't automatically affect running instances, the latestModelApplied flag for tracking state, and when to use update-instances versus reimage commands.

You'll learn about custom data processing at provisioning time versus update time, why cloud-init scripts only run during initial VM boot, and how to handle rolling updates when configurations change.

The exam expects you to know when VMSS is appropriate versus container-based solutions, and how to troubleshoot using run-command features for accessing logs and verifying deployments without SSH access.

Master cloud-init automation and VMSS model management for the AZ-204!
