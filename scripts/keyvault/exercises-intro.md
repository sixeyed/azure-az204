# Azure Key Vault - Exercises Introduction

We've covered Key Vault as Azure's specialized security service for storing secrets, keys, and certificates with encryption, access control, and audit logging. Now let's work with Key Vault hands-on.

## What You'll Do

You'll start by **creating Key Vaults via both Portal and CLI** to understand the options available. You'll choose between Standard tier (software encryption) and Premium tier (HSM-backed keys), and see how both pricing tiers include automatic versioning and recovery features like soft delete.

Then you'll **store and retrieve secrets with versioning**. Each time you update a secret, Key Vault creates a new version while keeping old versions accessible. You can reference secrets by name (always gets latest) or by specific version (gets that exact version). You'll practice both approaches and understand why referencing by name is better for automatic rotation.

Next comes **managing secret attributes** - expiration dates (secrets that automatically become invalid after a date), content types (hints about what the secret contains), tags (key-value metadata for organization), and enabled/disabled status (soft delete without removing the secret). These attributes provide lifecycle management without writing custom code.

You'll **create self-signed certificates using policy files** that define certificate properties like subject name, validity period, and key properties. Then you'll **download certificates in different formats** - PEM for Linux systems, DER for Windows systems, demonstrating Key Vault's role in certificate lifecycle management.

The key learning: Portal is great for exploration and one-off tasks, but CLI is essential for automation and production workflows. Everything you do in Portal has a CLI equivalent for scripting.

Let's secure sensitive data with Key Vault!
