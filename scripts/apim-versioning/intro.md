# API Management: API Changes & Versioning - Introduction

Welcome to this lab on API Management versioning and revisions. In this session, we'll explore how Azure API Management helps you manage API changes while maintaining backward compatibility with existing clients.

## Why API Versioning Matters

APIs are meant to be explicitly defined contracts between your service and its consumers. When you publish an API, clients build their applications against that contract. But what happens when you need to make changes?

This is where versioning becomes critical. By including a versioning scheme in your API specification from the beginning, you can make breaking changes under a new version while still supporting older versions. This gives your clients time to migrate at their own pace.

## Understanding Revisions vs Versions

Azure API Management supports two types of changes:

**Revisions** are for non-breaking changes. Think of adding optional parameters to an existing operation. Consumers don't need to update their code because the changes are backward compatible. They use defaults if the new parameters aren't provided.

**Versions** are for breaking changes. These require a new API version because existing clients would break if you changed the original. For example, making optional parameters mandatory, or changing response structures.

## The Power of Deployment Slots

In this lab, we'll see how API Management versioning works beautifully with deployment slots in Azure App Services. You can run multiple versions of your application code simultaneously, and APIM routes requests to the correct backend based on your versioning scheme.

This gives you tremendous flexibility. You can test new versions in isolation, perform blue-green deployments, and gradually migrate traffic between versions.

## What We'll Build

We're going to work with a Random Number Generator API. We'll start with version 1.0, then:

- Add a revision for version 1.1 with optional parameters
- Publish version 2.0 as a breaking change with mandatory parameters
- Use deployment slots to run all versions simultaneously

By the end of this lab, you'll understand how to evolve your APIs safely and professionally using Azure API Management.

Let's get started!
