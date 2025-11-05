# Application Gateway with Web Application Firewall - Introduction

## Opening

Welcome to this lab on Azure Application Gateway with Web Application Firewall. In this session, we'll explore one of Azure's most powerful traffic management and security tools.

## What is Application Gateway?

Application Gateway is Azure's layer 7 load balancer. Unlike traditional load balancers that work at the network layer, Application Gateway operates at the application layer, routing traffic based on HTTP request attributes. This means it can make intelligent routing decisions based on the domain name and URL path in incoming requests.

Application Gateway continuously monitors backend services to ensure they're healthy, distributing traffic only to healthy instances. This provides both high availability and optimal performance for your web applications.

## Web Application Firewall Overview

Web Application Firewall, or WAF, is an optional but powerful security feature of Application Gateway. WAF inspects both the headers and body of HTTP requests, looking for malicious payloads that could indicate an attack.

The key benefit here is that attacks can be prevented at the WAF layer, so they never reach your backend services. This provides a critical security boundary for your applications.

## Lab Objectives

In this lab, we'll accomplish three main objectives:

First, we'll deploy an Application Gateway with Web Application Firewall enabled, using the latest OWASP security ruleset.

Second, we'll configure Application Gateway to front multiple web applications running in Azure Container Instances, demonstrating multi-site routing capabilities.

Third, we'll test the WAF functionality by simulating common attack patterns like SQL injection, and observe how WAF blocks these malicious requests.

## Key Concepts

Before we begin, let's clarify some important concepts:

Layer 7 load balancing means routing decisions are made based on application-level data like HTTP headers, cookies, and URL paths. This is much more flexible than traditional network-level load balancing.

The OWASP ruleset we'll be using comes from the Open Web Application Security Project, the organization behind the famous OWASP Top 10 security risks. These rules protect against common web vulnerabilities.

WAF operates in two modes: Detection mode logs suspicious requests but allows them through, while Prevention mode actively blocks attacks. We'll use Prevention mode to stop threats before they reach our applications.

## Architecture Overview

Let's visualize what we're building:

At the front, we'll have a public IP address with a DNS name that clients will connect to.

This connects to our Application Gateway, deployed in a dedicated subnet within a virtual network. The Application Gateway includes the WAF component for security inspection.

Behind the gateway, we'll have multiple Azure Container Instances running web applications. The Application Gateway will route requests to the appropriate container based on the domain name in the request.

All traffic flows through the WAF first, providing a security checkpoint before reaching any backend service.

## Prerequisites

For this lab, you'll need:

An active Azure subscription with permissions to create resources.

The Azure CLI installed and authenticated to your subscription.

Basic familiarity with networking concepts like IP addresses and DNS.

Docker Desktop if you want to run the optional GoTestWAF security testing tool.

## What You'll Learn

By the end of this lab, you'll understand how to create and configure Azure Application Gateway with WAF, how to set up multi-site routing to different backend pools, how to test and validate WAF security rules, and how to troubleshoot common issues like 502 Bad Gateway errors.

Let's get started with creating our Application Gateway infrastructure.
