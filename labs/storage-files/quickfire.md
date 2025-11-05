# Azure Files - Quickfire Questions

## Question 1
What is Azure Files?

- A) A blob storage service
- B) Fully managed cloud file shares accessible via SMB or NFS protocols
- C) A database
- D) A backup service

**Answer: B**
Azure Files provides cloud-based file shares that can be mounted like traditional network shares.

---

## Question 2
What protocols does Azure Files support?

- A) Only HTTP
- B) SMB 3.0 (all tiers) and NFS 4.1 (premium tier only)
- C) Only FTP
- D) Only SFTP

**Answer: B**
Azure Files supports SMB 3.0 for standard and premium tiers, plus NFS 4.1 for premium tier.

---

## Question 3
What is a common use case for Azure Files?

- A) Running virtual machines
- B) Lift-and-shift applications requiring shared file storage
- C) Object storage
- D) Real-time analytics

**Answer: B**
Azure Files is ideal for migrating on-premises apps that use file shares to the cloud without code changes.

---

## Question 4
Can Azure Files shares be mounted on-premises?

- A) No, cloud-only
- B) Yes, via SMB over port 445 or VPN/ExpressRoute
- C) Only on Windows
- D) Requires special hardware

**Answer: B**
Azure Files can be mounted on-premises (Windows, Linux, macOS) if port 445 is open or via VPN/ExpressRoute.

---

## Question 5
What is Azure File Sync?

- A) A backup service
- B) A service that syncs on-premises file servers with Azure Files for cloud tiering and caching
- C) A replication tool
- D) A monitoring service

**Answer: B**
File Sync enables cloud tiering (frequently accessed files on-prem, others in cloud) and multi-site sync.

---

## Question 6
What authentication methods does Azure Files SMB support?

- A) Only access keys
- B) Storage account keys, Active Directory (AD DS, Azure AD DS), or Azure AD Kerberos
- C) Only anonymous
- D) Only SAS tokens

**Answer: B**
Azure Files supports identity-based authentication using on-premises AD DS, Azure AD DS, or Azure AD Kerberos.

---

## Question 7
What is the maximum size of a single file in Azure Files (standard tier)?

- A) 1 GB
- B) 1 TiB
- C) 4 TiB
- D) Unlimited

**Answer: B**
Standard tier supports files up to 1 TiB each. Premium tier also supports 4 TiB files.

---

## Question 8
What is the maximum size of an Azure Files share?

- A) 100 GB
- B) 5 TiB (standard) or 100 TiB (large file shares/premium)
- C) 1 PB
- D) Unlimited

**Answer: B**
Standard shares: 5 TiB default, up to 100 TiB with large file shares enabled. Premium: up to 100 TiB.

---

## Question 9
How can you secure data in transit for Azure Files?

- A) No encryption available
- B) SMB 3.0 encryption or HTTPS (REST API)
- C) Only physical security
- D) Only VPN

**Answer: B**
Azure Files uses SMB 3.0 encryption for in-transit data protection, and HTTPS for REST API access.

---

## Question 10
What is cloud tiering in Azure File Sync?

- A) Pricing tiers
- B) Frequently accessed files cached locally; infrequently accessed files moved to Azure Files
- C) Access control tiers
- D) Performance levels

**Answer: B**
Cloud tiering optimizes on-premises storage by keeping hot files local and tiering cold files to Azure Files.
