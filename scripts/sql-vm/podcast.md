# SQL Server on Azure Virtual Machines - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on SQL Server Virtual Machines in Azure. Today we're exploring when and why you might choose SQL Server VMs over managed database options like Azure SQL Database and SQL Managed Instance.

While managed SQL Server databases should be your preferred choice for most scenarios, they don't support 100% of the features you get with SQL Server in the datacenter. There will be occasions where you need a feature that isn't available in the managed options. That's where Azure SQL Server VMs come in. The SQL VM service lets you set up the underlying operating system and SQL Server deployment exactly how you need to, giving you complete control and access to all SQL Server features.

## Understanding Azure SQL VM Options

When exploring Azure SQL options in the Portal, you'll see SQL Virtual Machines as one of the three main ways to run SQL Server in Azure - the other two being Azure SQL Database and SQL Managed Instance. The variety of choices available includes Linux and Windows variants, since SQL Server runs on both operating systems now. Different SQL Server versions are available including 2019, 2017, and others. Multiple SKUs are offered for different performance requirements - you'll see options like Standard, Enterprise, Web, and Express editions.

## Creating a SQL Server VM

The process of creating a SQL Server VM starts with identifying the right VM image. You're looking for a specific combination like SQL Server 2019 Standard on Windows Server 2022 - this gives you a recent SQL Server version on the latest Windows Server.

When you query for available images, you first find the offers from the Microsoft SQL Server publisher, showing all the different SQL Server versions and Windows Server combinations available. Then you find specific SKUs within your chosen offer, showing the different editions like Standard, Enterprise, Web, and Express. Finally, you list all available images for your chosen configuration with their version numbers and URNs.

The URN uniquely identifies a specific image and is what you'll use to create your VM. It looks something like MicrosoftSQLServer:sql2019-ws2022:standard:15.0.220913.

When creating the SQL Server VM using the standard VM create command, this is just like creating any other VM, but the image you're using has SQL Server pre-installed and configured. You specify parameters like location, resource group, VM name, the image URN, VM size for compute capacity, admin credentials for the Windows account, and a unique DNS name for remote access.

After creation, the VM appears as a standard VM with the usual options - compute, networking, storage. You won't see any special SQL Server management options visible yet because you haven't registered it for SQL Server management.

## The SQL Server IaaS Extension

To add enhanced management options and configure SQL authentication, you need to register the VM with the SQL Server IaaS extension. This transforms your VM from a generic virtual machine into a managed SQL Server resource with Azure-integrated management capabilities.

When you register the VM, you can configure it for public access and set up SQL Authentication. The registration installs the SQL IaaS extension on the VM, configures SQL Server for SQL authentication in addition to Windows authentication, sets up the firewall to allow SQL Server traffic, and creates the SQL authentication login you specified.

After registration, a new SQL Virtual Machine resource appears in your resource group. This is a separate Azure resource that provides SQL-specific management capabilities. The Security Configuration shows that connectivity is set to Public, allowing connections from the internet, and the Network Security Group has a new rule allowing incoming traffic on port 1433. This is one of the conveniences of the extension - it handles common configuration tasks automatically.

## Advanced SQL Server Features

One of the key advantages of SQL Server VMs is access to features unavailable in managed services. For example, you can create custom User-Defined Functions that call .NET code. This demonstrates the flexibility you get with full control over SQL Server.

The process involves uploading a DLL file to the VM's file system, enabling CLR integration in SQL Server, and creating a function that calls into the .NET code. You couldn't perform these operations with Azure SQL Database or SQL Managed Instance for several reasons. You don't have access to upload files to disk since those are fully managed services. Some configuration commands are restricted because they affect server-level settings. The managed services prioritize security and consistency, so they don't allow arbitrary .NET code execution.

This demonstrates why you might choose a VM - you get complete control at the cost of managing the infrastructure yourself. You can create custom logins with whatever access levels you need, own authentication without using standard Azure auth mechanisms, and have complete control over security policies and configurations.

## SQL Server VMs and the AZ-204 Exam

Now let's connect this to the Azure AZ-204 Developer Associate certification. SQL Server VMs fall under the broader Azure compute solutions domain, specifically Infrastructure as a Service concepts.

### Service Selection Criteria

A critical skill for the exam is knowing when to choose different Azure services. Use SQL Server VMs when you need features not available in PaaS options, require full control over SQL Server configuration, need to upload files to the file system for database operations, have specific OS-level requirements, or are migrating legacy applications that require specific SQL Server features.

Don't use SQL Server VMs when PaaS options can meet your requirements, you want Azure to handle patching, backups, and high availability, you want to minimize operational overhead, or you don't need OS-level access.

### Comparing SQL Services

Be prepared to compare Azure SQL Database, which is fully managed PaaS and the most common choice; Azure SQL Managed Instance, which is PaaS with better compatibility with on-premises SQL; and SQL Server on Azure VMs, which is IaaS with full control and all features available.

### Security Concepts

The exam tests security implementation including configuring Network Security Groups to control traffic, understanding port requirements like 1433 for SQL Server and 3389 for RDP, managing public versus private connectivity options, and implementing least-privilege access through NSG rules.

For authentication and authorization, understand configuring SQL Server authentication separate from Azure AD, creating custom logins with specific permissions, the difference between Windows authentication and SQL authentication, and managing credentials securely.

### Azure CLI Proficiency

The exam expects proficiency with Azure CLI commands including az vm commands for virtual machine operations, az sql vm commands for SQL-specific operations, az network nsg commands for security configuration, querying and filtering Azure resources, and understanding command structure and common parameters.

### Cost Management

Understand cost implications including VM sizing and cost, SQL Server licensing models with Pay As You Go versus Bring Your Own License, storage costs, network egress costs, and the importance of cleaning up resources.

### Resource Management

The lab teaches creating and organizing resources in Resource Groups, using tags for resource organization and cost tracking, understanding the relationship between VM resources and SQL Virtual Machine resources, and cleaning up resources to manage costs.

## Real-World Applications

While the AZ-204 exam is developer-focused, understanding SQL Server VMs is important for application architecture when designing data tier solutions, understanding when IaaS versus PaaS is appropriate, and planning for application-specific database requirements.

For migration scenarios, SQL Server VMs are useful for lifting and shifting legacy applications, handling database migrations from on-premises, and dealing with unsupported features in managed services.

For custom requirements, VMs enable implementing specialized database features, using CLR integration for .NET code in SQL Server, creating User-Defined Functions and other custom objects, and managing file-based operations.

## Best Practices and Study Tips

For the AZ-204 exam, practice with Azure CLI to be comfortable creating and managing resources through command-line tools. Understand the "why" - don't just memorize commands but understand why you would choose one service over another. Know the limitations - understand what you can't do with each service option, as this helps with architectural decisions. Always consider security first in your solutions. Factor cost optimization into your architectural decisions. And get hands-on practice - actually perform these operations in Azure, as reading alone isn't sufficient.

## Common Exam Scenarios

You might see exam questions about choosing between SQL Database, SQL Managed Instance, and SQL VMs for given requirements, configuring network access to database resources, managing SQL Server credentials and authentication, understanding the trade-offs between IaaS and PaaS options, implementing security controls for database access, and selecting appropriate VM sizes and configurations.

## Final Thoughts

SQL Server on Azure Virtual Machines provides full control and access to all SQL Server features, making it the right choice when managed services can't meet your requirements. Understanding when to choose VMs versus managed database services is crucial for both the AZ-204 exam and real-world Azure development.

For the exam, focus on understanding service selection criteria, security configuration including NSGs and authentication, Azure CLI proficiency, and cost considerations. Remember that the exam tests not just your ability to perform tasks, but your understanding of when and why to use different Azure services.

SQL Server VMs represent the IaaS option in the Azure SQL family, providing maximum flexibility at the cost of increased operational responsibility. Knowing when they're the right choice is crucial for exam success and for designing effective Azure solutions.

Thanks for listening to this episode on SQL Server Virtual Machines. I hope this gives you a clear understanding of when and how to use SQL VMs in Azure and how this knowledge applies to the AZ-204 certification. Good luck with your studies!
