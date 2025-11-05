# API Management: Request and Response Policies - Introduction

Welcome to this lab on API Management policies for requests and responses.

## What Are APIM Policies?

Policies are the plug-in features in API Management that let you change the behavior of API operations without modifying the backend code.

There are two main types:
- **Input policies** - These fire before the backend gets called and can alter the request or even avoid calling the backend at all
- **Output policies** - These fire after the backend has been called and can alter the response before it gets sent to the client

## What We've Done So Far

In previous labs, we've already used a few policies - for caching and sending mocked responses. But there are other policies you should always look to add because they increase the security of your APIs.

## Today's Lab

In this lab, we'll present a public API through APIM, using policies to enhance security.

Specifically, we'll:
- Explore a backend API and identify security concerns
- Create an API in APIM to front the backend
- Apply header manipulation policies
- Implement caching policies
- Use find-and-replace policies to modify response bodies
- Test our secured API

## The Backend: SWAPI

We'll be working with SWAPI - the Star Wars API. This is a public REST API popular with developers that returns information about characters, places, and other data types from the Star Wars films.

You can read about it at swapi.dev.

An interesting aspect of this lab is that we're fronting a third-party API. Yes, you can do this with APIM, as long as the third-party's usage policy allows it.

Let's get started by exploring the backend API to see what security issues we need to address.
