# Log Analytics - Introduction

## Opening

Welcome to this lab on Azure Log Analytics. In this session, we'll explore one of the most powerful monitoring and analytics tools in Azure, learning how to query and visualize application data using Kusto Query Language.

## What is Log Analytics?

Log Analytics is the centralized data store for all sorts of log collection in Azure. It serves as the backbone for Azure's monitoring infrastructure.

Application Insights sends its telemetry data to Log Analytics. Virtual Machines can send their logs there. You can even ingest logs that have been saved in Storage Accounts.

What makes Log Analytics particularly powerful is its query interface. The Azure Portal provides a rich UI for querying data using Kusto Query Language, or KQL for short.

## Why KQL Matters

KQL is not just for interactive queries. You'll use it to:
- Power dashboards with custom visualizations
- Create intelligent alerts based on complex conditions
- Test and refine queries before using them in production monitoring
- Analyze application performance and troubleshoot issues

Log Analytics becomes your testing ground for KQL queries that you'll use throughout Azure Monitor.

## What We'll Cover

In this lab, we'll focus on how Log Analytics gives you access to data collected by Application Insights. You'll get hands-on experience with:

1. Setting up Log Analytics with Application Insights
2. Writing and executing KQL queries to analyze application logs
3. Aggregating metrics and creating meaningful summaries
4. Building visualizations to understand application behavior
5. Creating a comprehensive Workbook for monitoring

## The Sample Application

We'll work with a Fulfilment Processor application that runs in Azure Container Instances. This application generates logs and metrics that flow through Application Insights into Log Analytics.

The beauty of this setup is that it represents a real-world scenario - multiple instances of an application generating telemetry data that you need to monitor and analyze.

## Prerequisites

For this lab, you'll need:
- An active Azure subscription
- Azure CLI installed and configured
- Basic understanding of Azure Monitor concepts
- Familiarity with the Azure Portal

If you've completed the Application Insights lab, you can reuse those resources. Otherwise, we'll create everything from scratch.

## Let's Get Started

By the end of this lab, you'll be comfortable writing KQL queries to extract insights from your application data. You'll understand how to navigate the Log Analytics interface, and you'll have created a practical Workbook for ongoing monitoring.

Let's dive in and start exploring the power of Azure Log Analytics.
