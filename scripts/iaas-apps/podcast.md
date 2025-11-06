# IaaS Apps - Podcast Script

## Welcome and Introduction

Welcome to this podcast episode on deploying applications using Azure Infrastructure-as-a-Service. If you're preparing for the Azure AZ-204 certification or working on migrating existing applications to the cloud, understanding IaaS deployments is essential knowledge.

Today we're going to explore how to deploy traditional applications to Azure using virtual machines and managed databases. While Platform-as-a-Service solutions are often the end goal for cloud-native applications, IaaS provides a straightforward and sometimes necessary migration path for existing workloads - particularly legacy applications that haven't been modernized yet.

## The IaaS Approach to Cloud Deployment

Infrastructure-as-a-Service gives you complete control over your virtual machines. You manage the operating system, the runtime environment, and application configuration. This level of control makes IaaS an excellent choice in several scenarios.

First, when migrating existing applications to the cloud. If you have an application running on-premises that works well but wasn't designed for cloud-native architectures, IaaS lets you move it to Azure with minimal changes. You're essentially recreating your on-premises environment in the cloud.

Second, when applications require specific operating system configurations. Maybe your application depends on specific Windows Server features, particular versions of system libraries, or custom kernel modules. IaaS gives you the flexibility to configure the OS exactly as needed.

Third, when you need full control over the infrastructure. Perhaps for compliance reasons, performance tuning, or integration with specialized software that requires low-level system access.

The trade-off, of course, is that you're responsible for more management. You patch the operating system, manage security updates, configure the web server, handle scaling, and monitor system health. It's more work than Platform-as-a-Service, but that extra work buys you complete control.

## Our Lab Scenario: A Legacy .NET Framework Application

For our example today, we're working with a legacy .NET Framework application - the kind of application many organizations still run in production. This application uses Windows Server and SQL Server, both of which are fully supported in Azure.

Specifically, this is a .NET Framework 4.8 application, not .NET Core or .NET 5 and later. This distinction is important. The newer .NET platforms are cross-platform and can run on Linux, but .NET Framework specifically requires Windows Server. This requirement alone often makes IaaS the most practical deployment option.

The application we're deploying is a simple user signup web application. Users enter their information through a web form, and that data gets saved to a SQL Server database. It's straightforward functionality, but it represents the type of line-of-business application that forms the backbone of many organizations.

## Architecture Overview

Our architecture is relatively straightforward but includes several important Azure components working together.

At the core, we have a Windows Server virtual machine running in a virtual network. This VM hosts Internet Information Services - IIS - which is Microsoft's web server platform. IIS serves our .NET Framework 4.8 application.

For data storage, we're using Azure SQL Database. This is important to understand: we're not installing SQL Server on the VM itself. Azure SQL Database is a managed platform service that handles database management tasks like backups, patching, and high availability automatically. Even in an IaaS deployment, you can leverage managed services for components where you don't need full control.

The VM and database communicate securely using Azure virtual network service endpoints. This keeps database traffic on the Azure backbone network rather than going over the public internet.

And finally, we expose the application to the internet through a public IP address and network security group rules that allow HTTP traffic to reach the VM.

## Creating the Foundation: Resource Group and SQL Database

Every Azure deployment starts with a resource group - a logical container for related resources. Think of it as a folder that holds everything for a particular application or project. Resource groups make management easier because you can apply permissions, policies, and tags at the group level, and you can delete everything at once when you're done.

For our lab, we create a resource group with a descriptive name like "labs-iaas-apps" in a specific region. The region choice affects where your resources physically run, which has implications for latency, compliance, and pricing.

Next, we create our database infrastructure. Azure SQL Database has a two-level hierarchy: first you create a logical SQL Server, then you create databases within that server. The logical server isn't actually a server you manage - it's an administrative boundary and connection endpoint.

When creating the SQL Server, you need to provide a globally unique name. This name becomes part of the fully qualified domain name - something like "myserver12345.database.windows.net". Because this has to be unique across all of Azure globally, you can't just use simple names like "server" or "database".

You also provide administrator credentials - a username and password. In our lab example, we use simple credentials for educational purposes, but in production, you'd use much stronger passwords and store them securely in Azure Key Vault rather than including them in scripts.

Then we create the actual database within that logical server. Database creation can take several minutes, so Azure CLI offers a helpful "no-wait" flag that lets the operation run in the background while you continue with other tasks. This parallelism can significantly speed up overall deployment time.

## Provisioning the Windows Server Virtual Machine

Now let's talk about creating the virtual machine that will host our application.

Azure offers numerous virtual machine images for different operating systems and configurations. We're using Windows Server 2022 Datacenter Core, which is worth discussing because it's different from what many people expect when they think "Windows Server".

Windows Server Core is a minimal installation without the full graphical user interface. When you connect to a Server Core VM, you don't see the familiar Windows desktop with Start menu and taskbar. Instead, you get a command prompt window. This can be surprising at first, but Server Core has significant advantages: it's lighter on resources, boots faster, requires fewer patches, and has a smaller attack surface for security because there are fewer components installed.

For web server workloads, you don't actually need the full GUI. Everything you need can be done through PowerShell or command-line tools.

When creating the VM, you specify several important parameters. The image is identified by a URN - a uniform resource name - in the format publisher:offer:SKU:version. For Windows Server 2022 Datacenter Core second-generation VMs, this looks like "MicrosoftWindowsServer:WindowsServer:2022-datacenter-core-g2:latest". The "g2" designation means it's a second-generation VM, which uses newer Azure hypervisor features for better performance.

The VM size determines the compute resources - CPU cores, memory, disk throughput, and network bandwidth. For our example, we use Standard_D2s_v5, which provides 2 virtual CPUs and 8 gigabytes of memory. The "D" series is general-purpose, suitable for most workloads. The "v5" indicates the fifth generation of this series, with the latest improvements in performance and efficiency.

You also configure authentication by providing an administrator username and password. In production, you'd use more secure methods like Azure AD integration, but for lab purposes, a local admin account works fine.

One particularly useful feature is the ability to assign a DNS name to the public IP address. Instead of remembering an IP address like "52.137.45.123", you get a friendly name like "myapp-vm-12345.westeurope.cloudapp.azure.com". This makes connecting to the VM much easier.

When you execute the VM creation command, Azure automatically provisions several resources: the VM itself, a network interface, a virtual network with a subnet, a public IP address, and a network security group with default rules. Azure handles all this infrastructure orchestration for you, even though you're running IaaS. You're not manually creating virtual networks and wiring up network interfaces - the platform handles that complexity.

## Installing and Configuring the Application

Once the VM is running, you connect using Remote Desktop Protocol. When you connect to a Server Core VM, that command prompt window is what you get instead of a desktop. Everything you need to do is accomplished through PowerShell commands.

The first thing to verify is that .NET Framework 4.8 is installed. Windows Server 2022 includes this by default, but it's good practice to verify. You can query the Windows registry where .NET Framework installations are recorded. The registry key stores version numbers and release identifiers for each installed framework version.

When you check, you'll find that .NET Framework 4.8 Full is indeed installed and ready to use. This is exactly what our application requires.

Next, you need to install IIS and the ASP.NET components. Windows Server has a feature called "Windows Features" - optional components you can install. PowerShell provides commands to manage these features. You can list available features to confirm IIS isn't already installed, then use the Install-WindowsFeature command to add what you need.

Specifically, you install three components: Web-Server for IIS itself, NET-Framework-45-ASPNET for the ASP.NET runtime integration, and Web-Asp-Net45 for the ASP.NET IIS modules. The installation completes quickly - usually within a minute or two - and typically doesn't require a restart.

Our application is packaged as an MSI installer file hosted on GitHub. You download it using curl, saving it to a local file. Then you install it using the Windows Installer service through the msiexec command. The installation runs silently without user interface, and you prevent automatic reboots that would disconnect your remote session.

After installation, the application files exist in a specific directory, and IIS has been configured to serve the application at a particular URL path - in this case "/signup". You can verify this through PowerShell commands that query IIS configuration.

## The Database Connection Challenge

At this point, the application is installed and IIS is configured, but if you try to access it, you'll get an error. The application can't connect to its database.

When you examine the application's configuration file - specifically the connectionStrings.config file - you'll see it's configured with a default connection string pointing to "localhost", expecting a local SQL Server installation. But we don't have SQL Server installed on this VM. Our database is in Azure SQL Database, running as a separate service.

We need to edit this configuration file to use the correct connection string for Azure SQL Database. Even in Server Core, you have access to basic GUI applications like Notepad, so you can open the configuration file and modify it.

The Azure SQL Database connection string has a specific format. The Server parameter is the fully qualified domain name of your logical SQL Server - that "myserver12345.database.windows.net" name. The Database parameter is your database name. User Id and Password are the credentials you set when creating the SQL Server. It's also good practice to include a Connect Timeout parameter to avoid hanging indefinitely if there's a connectivity problem.

After saving the updated configuration and restarting the application, you test again. Now you get a different error - the database exists and the connection string is correct, but the VM can't reach the database due to firewall rules.

This is actually good security. Azure SQL databases aren't publicly accessible by default. You must explicitly grant network access to specific IP addresses or virtual networks.

## Configuring Secure Network Access

Azure SQL Database has robust network security features. You can configure firewall rules based on IP addresses, or you can use virtual network rules that allow access from specific Azure virtual networks.

Virtual network rules are more secure than IP-based rules because they keep traffic on the Azure backbone network. Instead of database connections going over the public internet, they stay within Azure's infrastructure. This is faster, more secure, and doesn't count against your internet bandwidth limits.

To enable virtual network rules for SQL Database, you first need to configure a service endpoint on the VM's subnet. Service endpoints are a virtual network feature that extends your VNet's identity to Azure services. When you enable the Microsoft.Sql service endpoint on a subnet, you're telling Azure "resources in this subnet should have direct access to SQL Database services through the Azure backbone network".

You configure this in the virtual network settings, selecting the appropriate subnet and adding Microsoft.Sql as a service endpoint.

Once the service endpoint is configured, you can add a virtual network rule to your SQL Server. This rule says "allow connections from this specific virtual network and subnet". Now any resource in that subnet - including our VM - can connect to the database.

When you test the application again after configuring the service endpoint and virtual network rule, it works. The application successfully connects to Azure SQL Database, processes requests, and returns web pages. The error is gone, and the internal connectivity is functioning properly.

## Exposing the Application to the Internet

At this point, the application works if you access it from within the VM, but it's not yet accessible from the outside world. This is because of the Network Security Group - Azure's firewall for virtual machines.

Network Security Groups contain security rules that allow or deny traffic based on source, destination, port, and protocol. By default, Azure creates rules that allow outbound internet access but restrict inbound access to only management ports like RDP.

To make the web application publicly accessible, you need to add an inbound security rule that allows HTTP traffic on port 80.

The rule specifies several parameters. The source is "Any", meaning any IP address on the internet. The destination is also "Any", meaning any IP in the virtual network. The destination port is 80 for HTTP. The protocol is TCP. The action is Allow. You assign it a priority - lower numbers are evaluated first, so if you have conflicting rules, the priority determines which one wins.

Once this rule is active, you can access the application from any web browser on the internet using the VM's DNS name. The full end-to-end architecture is now working: requests come from the internet, pass through the Network Security Group firewall, reach IIS on the VM, which runs the application that connects to Azure SQL Database.

You can test it fully by accessing the signup form and creating a test user. When you submit the form, the application processes the data and saves it to the database. You get a confirmation message, indicating success.

## Verifying Data Flow

To completely verify everything is working, you can check that the data actually made it into the database.

Azure Portal provides a Query Editor for Azure SQL Database - a browser-based tool for running SQL queries without needing to install SQL Server Management Studio. You authenticate with your SQL admin credentials and can run queries directly.

A simple SELECT query against the Prospects table shows all the user signups. You'll see the test data you just entered through the web form - the name, email, role selection, and a timestamp showing when the record was created.

This confirms the complete data flow: from web form in the browser, through the internet, into the VM, through the application code, into Azure SQL Database. Every component of the architecture is working together correctly.

## IaaS and the AZ-204 Exam

Now let's connect this practical experience to the Azure AZ-204 Developer Associate certification. Understanding IaaS deployments is crucial for several exam objectives.

### Provisioning Virtual Machines

The exam expects you to understand how to create VMs using Azure CLI or PowerShell. You need to know the parameters for the "az vm create" command: specifying the image using publisher, offer, SKU, and version format; selecting appropriate VM sizes for different workloads; configuring authentication; and attaching network resources like public IPs and DNS names.

The command structure we used demonstrates all these concepts. Understanding the publisher-offer-SKU hierarchy is particularly important. You should be able to find the right image for different scenarios, whether it's Windows Server, Ubuntu, Red Hat, or other distributions.

### VM Sizing and Series

We used the Standard_D2s_v5 size, which is from the general-purpose D-series. For the exam, you need to know the different VM series and their use cases.

The D-series is general-purpose, balanced compute and memory. The F-series is compute-optimized with higher CPU-to-memory ratio. The E-series is memory-optimized for applications like databases and caching. The N-series includes GPUs for graphics and AI workloads. The L-series has fast local storage for databases and data warehousing.

You should be able to select appropriate sizes based on application requirements. The exam might give you a scenario and ask which VM series is most suitable.

### Networking Configuration

We configured several networking components that are testable on the exam.

When you create a VM, Azure automatically creates a virtual network, subnet, network interface, and network security group. Understanding these components and how they interconnect is crucial. The virtual network provides isolated network space. Subnets segment the network into smaller blocks. Network interfaces attach VMs to subnets. Network security groups control traffic to and from those interfaces.

Service endpoints are an important concept. We configured a service endpoint for Microsoft.Sql to enable secure access from the VM to Azure SQL Database. Service endpoints extend your VNet identity to Azure services, improve security by keeping traffic on the Azure backbone, and are required for virtual network rules on services like SQL Database and Storage.

For the exam, know how to configure service endpoints, understand the difference between service endpoints and private endpoints - private endpoints give the Azure service a private IP in your VNet, whereas service endpoints keep the service's public endpoint but add a secure path from your VNet.

Know which Azure services support service endpoints: SQL Database, Storage, Key Vault, Service Bus, Cosmos DB, and others.

### Network Security Groups

We configured NSG rules to allow HTTP traffic. For the exam, understand how to create and modify NSG rules, how source and destination specifications work - these can be IP addresses, ranges, service tags, or application security groups.

Understand port ranges and protocols - you can specify single ports like 80, ranges like 8000-9000, or asterisk for all ports. Protocols can be TCP, UDP, ICMP, or Any.

Rule priorities determine evaluation order. Lower numbers are evaluated first. If multiple rules match, the first matching rule's action is taken. Understanding this priority system is essential for troubleshooting connectivity issues.

### Azure SQL Database

We created and configured Azure SQL Database, which is a significant exam topic.

Understanding the hierarchy is important: you create a logical SQL Server first, then databases within that server. The logical server is an administrative boundary and connection endpoint, not a server you manage directly.

For the exam, know the different pricing tiers and service objectives. Basic tier for development and small workloads, Standard for most production workloads, Premium for high transaction volumes, and Hyperscale for very large databases. There's also the serverless compute tier that automatically scales and pauses.

Understand backup and restore options - Azure SQL Database automatically backs up databases with point-in-time restore capabilities. Know the retention periods and how to perform restores.

We configured virtual network rules for database access. The exam may test firewall rules based on IP addresses versus virtual network rules versus private endpoints. Understand when each approach is appropriate. IP rules are simple but less secure. VNet rules keep traffic on Azure backbone. Private endpoints give the database a private IP in your VNet for maximum security.

### Connection Strings and Security

We modified the application's connection string to connect to Azure SQL Database. For the exam, know connection string formats for different scenarios - SQL authentication versus Azure AD authentication, different driver types, special parameters.

Understand that connection strings should never be hard-coded in application code. They should be stored in configuration systems like Azure App Configuration or Azure Key Vault. In our lab, we edited a configuration file directly, but the exam will expect you to know more secure approaches.

Managed identities are particularly important. Instead of using usernames and passwords, your application can authenticate using its managed identity. This eliminates the need to handle credentials at all.

## Choosing Between IaaS and PaaS

A key exam skill is understanding when to choose IaaS versus Platform-as-a-Service options like Azure App Service.

We deployed this application to IaaS because it uses .NET Framework, which requires Windows Server and isn't supported by App Service on Linux. It might also need specific IIS configuration or have dependencies on Windows Server features.

IaaS is appropriate when you have legacy applications not designed for PaaS, when you need specific OS configurations, when you require full control over the infrastructure, or when you're migrating from on-premises and want to minimize application changes.

App Service is better when you have modern applications built with PaaS in mind, when you want less management overhead, when you want built-in features like auto-scaling and deployment slots, or when you're building new cloud-native applications.

The exam will present scenarios and ask you to choose the appropriate hosting option. Understanding the trade-offs is essential.

## Automation and Infrastructure as Code

In our lab, we performed many steps manually - connecting to the VM, installing IIS, configuring the application. This is fine for learning, but the exam expects you to understand automated approaches.

Custom Script Extension for Azure VMs lets you run scripts automatically during or after VM provisioning. You could automate the entire application installation - installing IIS, downloading the application, configuring settings - all through a script that runs without human intervention.

For Linux VMs, cloud-init provides similar capabilities for initialization and configuration.

PowerShell Desired State Configuration - DSC - is a declarative configuration management platform for Windows. You define the desired state of a system, and DSC ensures it stays in that state.

And of course, ARM templates and Bicep let you define entire infrastructures as code. You could create a template that provisions the resource group, SQL Server, database, virtual network, VM, and runs configuration scripts - all in one deployment.

The exam will likely include questions about automating VM configuration and deployment. Know these tools and when to use each.

## Common Exam Scenarios

Let me walk through some typical exam scenarios related to IaaS deployments.

Scenario one: "Your organization needs to migrate a legacy ASP.NET application from on-premises to Azure. The application uses Windows Server, IIS, and SQL Server. What's your approach?"

The answer would involve Azure VMs running Windows Server for the application tier, migrating the database to Azure SQL Database or SQL Server on Azure VMs depending on compatibility requirements, configuring virtual network connectivity, possibly using ExpressRoute or site-to-site VPN for hybrid connectivity during migration, and implementing network security groups and service endpoints for security.

Scenario two: "An application running on an Azure VM needs to access Azure SQL Database. How do you secure this connection to avoid sending database traffic over the public internet?"

The answer involves configuring a service endpoint for Microsoft.Sql on the VM's subnet, then adding a virtual network rule to the SQL Server firewall. Alternatively, for maximum security, deploy a private endpoint that gives the database a private IP address within your virtual network.

Scenario three: "How should connection strings and sensitive credentials be managed for applications on VMs?"

The answer is Azure Key Vault with Managed Identity. The VM has a system-assigned or user-assigned managed identity that authenticates to Key Vault without credentials. The application retrieves connection strings from Key Vault at runtime. Credentials are never hard-coded in configuration files or application code.

Scenario four: "You need to deploy the same VM configuration across multiple regions. What's the best approach?"

Use ARM templates or Bicep to define the infrastructure as code. Parameterize region-specific values. Deploy the template to each region. This ensures consistency and makes updates easier - change the template, redeploy.

## Security Best Practices

Security is a major component of the AZ-204 exam. Several security best practices apply to IaaS deployments.

First, use Managed Identities instead of credentials whenever possible. VMs can have system-assigned identities that automatically authenticate to Azure services. No credentials to manage, rotate, or accidentally expose.

Second, store secrets in Azure Key Vault, not in code or configuration files. Key Vault provides centralized secret management, access auditing, and automatic secret rotation capabilities.

Third, apply least-privilege access using role-based access control - RBAC. Grant users and applications only the permissions they actually need, nothing more.

Fourth, use private endpoints for sensitive workloads. Private endpoints bring Azure services into your virtual network address space, eliminating public internet exposure entirely.

Fifth, keep systems patched. Enable automatic updates where possible. Use Azure Update Management to centrally manage patching across VMs.

And finally, implement defense in depth. Don't rely on a single security control. Use network security groups, Azure Firewall, service endpoints or private endpoints, managed identities, Key Vault, Azure AD authentication, and monitoring together to create multiple layers of protection.

## Monitoring and Troubleshooting

While not extensively covered in our deployment, the exam will test monitoring and troubleshooting knowledge.

Azure Monitor provides comprehensive monitoring for VMs. VM Insights collects performance data, discovers application dependencies, and tracks processes. You can see CPU, memory, disk, and network metrics over time.

Boot diagnostics capture serial console output and screenshots during VM boot. This is invaluable when a VM won't start or you can't connect. You can see exactly where the boot process is failing.

Network Watcher provides network diagnostics. Connection troubleshoot tests connectivity between resources. IP flow verify checks if traffic is allowed or denied by network security group rules. Next hop shows routing paths.

Application Insights can monitor applications running on VMs, collecting telemetry about requests, exceptions, dependencies, and custom events. This provides application-level monitoring beyond just infrastructure metrics.

For the exam, know which tool to use for different troubleshooting scenarios. VM won't boot? Check boot diagnostics. Network connectivity issue? Use Network Watcher. Application performance problem? Application Insights.

## Cost Optimization

Cost management is another exam topic. Several strategies apply to IaaS deployments.

First, shut down VMs when not needed. A stopped VM still incurs storage costs for its disks, but compute charges stop. Deallocating goes further - it releases the compute allocation entirely, reducing costs even more. Know the difference between stopped and deallocated states.

Second, right-size VM instances. Don't over-provision. Azure Advisor provides right-sizing recommendations based on actual usage patterns. If a VM consistently runs at 10% CPU utilization, you're paying for capacity you don't need.

Third, use appropriate SQL Database tiers. Don't run production workloads on Premium tier if Standard meets your needs. Consider serverless compute for intermittent workloads that can tolerate cold-start latency.

Fourth, use reserved instances for predictable workloads. Reservations provide significant discounts - up to 72% compared to pay-as-you-go - in exchange for one or three year commitments.

Fifth, implement auto-shutdown schedules for development and test VMs. They don't need to run nights and weekends when nobody is using them.

The exam might present scenarios asking how to optimize costs for different workload patterns. Understand these strategies and when each applies.

## Key Takeaways for the Exam

Let me summarize the critical points for AZ-204 exam success regarding IaaS deployments.

One: Know how to create and configure VMs using Azure CLI and PowerShell. Understand the parameter syntax, image URN format, sizing options, and authentication configuration.

Two: Understand networking components - virtual networks, subnets, network interfaces, network security groups, service endpoints, and private endpoints. Know how they interconnect and when to use each security feature.

Three: Know Azure SQL Database creation, configuration, and networking. Understand the logical server and database hierarchy, firewall rules, virtual network rules, and connection string formats.

Four: Understand when to choose IaaS versus PaaS. Know the decision criteria and trade-offs.

Five: Know automation approaches - Custom Script Extension, cloud-init, PowerShell DSC, ARM templates, Bicep. Understand that manual configuration doesn't scale and isn't repeatable.

Six: Apply security best practices - managed identities, Key Vault, RBAC, private endpoints, defense in depth.

Seven: Understand monitoring and troubleshooting tools - Azure Monitor, boot diagnostics, Network Watcher, Application Insights. Know which tool addresses which scenario.

Eight: Know cost optimization strategies - shutting down VMs, right-sizing, appropriate service tiers, reserved instances, auto-shutdown schedules.

## Final Thoughts

IaaS deployments represent a fundamental skill for Azure developers. While Platform-as-a-Service solutions are often preferable for new applications, IaaS remains essential for migrating existing workloads, supporting legacy applications, and scenarios requiring full infrastructure control.

For the AZ-204 exam, you need both theoretical understanding and practical experience. The exam includes scenario-based questions that test your ability to choose appropriate solutions, troubleshoot problems, and apply best practices. Hands-on experience deploying applications to VMs, configuring networking, and working with Azure SQL Database will help you answer these questions confidently.

The concepts we've covered today - VM provisioning, networking configuration, service endpoints, security practices, and the decision criteria for IaaS versus PaaS - form a core part of the exam's "Implement IaaS solutions" objective domain.

As you continue your AZ-204 preparation, practice these deployments repeatedly. Try different VM sizes and images. Experiment with networking configurations. Work with both SQL Database and SQL Server on VMs. Automate deployments using scripts and templates. The hands-on experience will make you a better developer and help you pass the exam.

Thanks for listening to this episode on IaaS application deployments. I hope this gives you both practical skills and exam preparation insights. Good luck with your AZ-204 studies!
