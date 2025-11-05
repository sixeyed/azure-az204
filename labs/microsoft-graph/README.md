# Microsoft Graph

Microsoft Graph is the gateway to data and intelligence in Microsoft 365, providing a unified programmability model to access data in Office 365, Windows 10, and Enterprise Mobility + Security.

In this lab you will learn how to:

- Understand Microsoft Graph API structure
- Authenticate applications using Microsoft Identity platform
- Query user data, groups, mail, and calendar
- Work with delegated and application permissions
- Use Graph Explorer for testing

## Learning Objectives

- Understand the Microsoft Graph API endpoint structure
- Register an application in Azure AD for Graph access
- Implement authentication with Microsoft Identity platform
- Make basic Graph API calls for common scenarios
- Work with delegated and application permissions

## What is Microsoft Graph?

Microsoft Graph is a RESTful web API that enables you to access Microsoft Cloud service resources. After you register your app and get authentication tokens for a user or service, you can make requests to the Microsoft Graph API.

### Key Benefits

- **Unified endpoint**: Single endpoint (https://graph.microsoft.com) for all Microsoft 365 services
- **Rich data model**: Access to users, groups, mail, calendar, files, devices, and more
- **Consistent API**: Standardized REST API with OData query capabilities
- **Extensive SDKs**: Available for .NET, Java, JavaScript, Python, and more

### Graph API Structure

All Microsoft Graph requests follow this pattern:

```
https://graph.microsoft.com/{version}/{resource}?{query-parameters}
```

- **version**: `v1.0` (production) or `beta` (preview features)
- **resource**: The resource you're accessing (users, groups, me, etc.)
- **query-parameters**: Optional OData parameters ($filter, $select, $top, etc.)

Examples:
```
GET https://graph.microsoft.com/v1.0/me
GET https://graph.microsoft.com/v1.0/users
GET https://graph.microsoft.com/v1.0/me/messages
GET https://graph.microsoft.com/v1.0/groups
```

## Prerequisites

- Azure subscription
- Azure CLI installed
- Basic understanding of REST APIs
- Basic understanding of OAuth 2.0

## Exercise 1: Register an Application

To access Microsoft Graph, you need to register an application in Azure Active Directory.

### Create App Registration

```bash
# Create resource group
az group create -n labs-graph --tags courselabs=azure -l eastus

# Register application
az ad app create \
  --display-name "GraphLabApp" \
  --sign-in-audience AzureADMyOrg

# Get the Application (client) ID
APP_ID=$(az ad app list --display-name "GraphLabApp" --query '[0].appId' -o tsv)
echo "Application ID: $APP_ID"

# Get the Directory (tenant) ID
TENANT_ID=$(az account show --query tenantId -o tsv)
echo "Tenant ID: $TENANT_ID"
```

### Create Client Secret

```bash
# Create client secret
az ad app credential reset \
  --id $APP_ID \
  --append \
  --query password -o tsv

# Save this secret securely - you won't be able to retrieve it again!
```

📋 Navigate to the Azure Portal and find your app registration under Azure Active Directory > App registrations.

## Exercise 2: Configure API Permissions

Your application needs permissions to access Microsoft Graph resources.

### Add Microsoft Graph Permissions

In the Azure Portal:

1. Navigate to **Azure Active Directory** > **App registrations**
2. Select your **GraphLabApp** application
3. Click **API permissions** in the left menu
4. Click **Add a permission**
5. Select **Microsoft Graph**
6. Choose permission type:
   - **Delegated permissions**: Act on behalf of a signed-in user
   - **Application permissions**: Act as the application itself (no user)

### Common Permissions

**Delegated permissions** (requires user sign-in):
- `User.Read` - Read signed-in user's profile
- `User.ReadBasic.All` - Read all users' basic profiles
- `Mail.Read` - Read user's mail
- `Calendars.Read` - Read user's calendar
- `Files.Read` - Read user's files

**Application permissions** (no user required):
- `User.Read.All` - Read all users' profiles
- `Group.Read.All` - Read all groups
- `Mail.Read` - Read mail in all mailboxes
- `Calendars.Read` - Read calendars in all mailboxes

> **Important**: Application permissions require admin consent!

### Grant Admin Consent

For application permissions, an admin must grant consent:

```bash
# Grant admin consent (requires admin privileges)
az ad app permission grant \
  --id $APP_ID \
  --api 00000003-0000-0000-c000-000000000000 \
  --scope User.Read
```

Or in the Portal:
1. Go to **API permissions**
2. Click **Grant admin consent for [Your Organization]**

## Exercise 3: Graph Explorer

Graph Explorer is a web-based tool for testing Microsoft Graph APIs without writing code.

### Access Graph Explorer

Navigate to: https://developer.microsoft.com/en-us/graph/graph-explorer

### Try Sample Queries

1. **Sign in** with your Microsoft 365 account
2. Grant permissions when prompted
3. Try these sample queries:

**Get your profile:**
```
GET https://graph.microsoft.com/v1.0/me
```

**Get your emails:**
```
GET https://graph.microsoft.com/v1.0/me/messages
```

**Get your calendar events:**
```
GET https://graph.microsoft.com/v1.0/me/events
```

**Get users in your organization:**
```
GET https://graph.microsoft.com/v1.0/users
```

📋 Use Graph Explorer to retrieve the top 5 messages from your mailbox with only the subject and from fields.

<details>
  <summary>Not sure how?</summary>

```
GET https://graph.microsoft.com/v1.0/me/messages?$top=5&$select=subject,from
```

</details><br/>

### Query Parameters

Microsoft Graph supports OData query parameters:

- **$select**: Choose which properties to return
  ```
  /me?$select=displayName,mail
  ```

- **$filter**: Filter results
  ```
  /users?$filter=startsWith(displayName,'A')
  ```

- **$orderby**: Sort results
  ```
  /users?$orderby=displayName
  ```

- **$top**: Limit number of results
  ```
  /users?$top=10
  ```

- **$expand**: Include related resources
  ```
  /me?$expand=manager
  ```

## Exercise 4: Authentication Flows

Microsoft Graph uses OAuth 2.0 for authentication. Different scenarios use different flows.

### Authentication Flow Types

1. **Authorization Code Flow** (web apps, delegated permissions)
   - User signs in and grants consent
   - App receives authorization code
   - App exchanges code for access token
   - Best for: Web applications with server-side code

2. **Implicit Flow** (single-page apps)
   - Tokens returned directly in URL fragment
   - No server-side code required
   - Less secure than authorization code
   - Best for: Client-side JavaScript apps (use PKCE instead if possible)

3. **Client Credentials Flow** (daemon apps, application permissions)
   - App authenticates with client ID and secret
   - No user interaction
   - Requires application permissions
   - Best for: Background services, scheduled jobs

4. **Device Code Flow** (devices with limited input)
   - User signs in on separate device
   - Best for: CLI tools, IoT devices

### Authentication Endpoints

**Authorization endpoint:**
```
https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize
```

**Token endpoint:**
```
https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
```

## Exercise 5: Basic Graph Queries

### Get Current User Profile

Using Azure CLI (behind the scenes uses Graph API):

```bash
az ad signed-in-user show
```

Using curl with access token:

```bash
# Get access token (for testing only)
TOKEN=$(az account get-access-token --resource https://graph.microsoft.com --query accessToken -o tsv)

# Get user profile
curl -H "Authorization: Bearer $TOKEN" \
  https://graph.microsoft.com/v1.0/me
```

### Query Users

```bash
# Get all users
curl -H "Authorization: Bearer $TOKEN" \
  https://graph.microsoft.com/v1.0/users

# Get specific user
curl -H "Authorization: Bearer $TOKEN" \
  https://graph.microsoft.com/v1.0/users/{user-id}

# Filter users
curl -H "Authorization: Bearer $TOKEN" \
  "https://graph.microsoft.com/v1.0/users?\$filter=startsWith(displayName,'John')"
```

### Query Groups

```bash
# Get all groups
curl -H "Authorization: Bearer $TOKEN" \
  https://graph.microsoft.com/v1.0/groups

# Get groups user is member of
curl -H "Authorization: Bearer $TOKEN" \
  https://graph.microsoft.com/v1.0/me/memberOf
```

📋 Try to get all members of a specific group.

<details>
  <summary>Not sure how?</summary>

```bash
# First, get a group ID
GROUP_ID=$(curl -s -H "Authorization: Bearer $TOKEN" \
  "https://graph.microsoft.com/v1.0/groups" | jq -r '.value[0].id')

# Get group members
curl -H "Authorization: Bearer $TOKEN" \
  "https://graph.microsoft.com/v1.0/groups/$GROUP_ID/members"
```

</details><br/>

### Query Mail

```bash
# Get messages
curl -H "Authorization: Bearer $TOKEN" \
  https://graph.microsoft.com/v1.0/me/messages

# Get unread messages
curl -H "Authorization: Bearer $TOKEN" \
  "https://graph.microsoft.com/v1.0/me/messages?\$filter=isRead eq false"

# Send email
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": {
      "subject": "Test from Graph API",
      "body": {
        "contentType": "Text",
        "content": "Hello from Microsoft Graph!"
      },
      "toRecipients": [
        {
          "emailAddress": {
            "address": "user@example.com"
          }
        }
      ]
    }
  }' \
  https://graph.microsoft.com/v1.0/me/sendMail
```

### Query Calendar

```bash
# Get calendar events
curl -H "Authorization: Bearer $TOKEN" \
  https://graph.microsoft.com/v1.0/me/events

# Get events for next 7 days
START=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
END=$(date -u -d "+7 days" +"%Y-%m-%dT%H:%M:%SZ")

curl -H "Authorization: Bearer $TOKEN" \
  "https://graph.microsoft.com/v1.0/me/calendarView?\$startDateTime=$START&\$endDateTime=$END"
```

## Exercise 6: Permissions Deep Dive

### Delegated Permissions

**How it works:**
1. User signs in to your application
2. User consents to permissions
3. Application receives token with user's identity
4. Application acts on behalf of the user

**Use cases:**
- Mobile apps
- Web apps with user sign-in
- Single-page applications

**Example:** Read signed-in user's email

### Application Permissions

**How it works:**
1. Admin grants consent to application
2. Application authenticates with client credentials
3. Application receives token with app identity
4. Application acts as itself (no user context)

**Use cases:**
- Background services
- Daemon applications
- Scheduled jobs
- Admin tools

**Example:** Read all users' email in organization

### Permission Scopes

When requesting tokens, specify scopes:

**Delegated:**
```
https://graph.microsoft.com/User.Read
https://graph.microsoft.com/Mail.Read
https://graph.microsoft.com/Calendars.Read
```

**Application:**
```
https://graph.microsoft.com/.default
```

### Least Privilege Principle

Always request the minimum permissions needed:

- ❌ `Mail.ReadWrite.All` when you only need to read
- ✅ `Mail.Read` for read-only access

- ❌ `User.ReadWrite.All` when you only need basic profile
- ✅ `User.Read` for current user profile

## Common Patterns

### Pagination

Graph API returns results in pages. Use `@odata.nextLink` for pagination:

```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users",
  "@odata.nextLink": "https://graph.microsoft.com/v1.0/users?$skip=100",
  "value": [...]
}
```

### Error Handling

Graph API returns errors in this format:

```json
{
  "error": {
    "code": "InvalidAuthenticationToken",
    "message": "Access token is empty.",
    "innerError": {
      "request-id": "...",
      "date": "..."
    }
  }
}
```

Common error codes:
- `401 Unauthorized`: Invalid or expired token
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource doesn't exist
- `429 Too Many Requests`: Rate limit exceeded
- `503 Service Unavailable`: Service temporarily unavailable

## Best Practices

1. **Use v1.0 for production**: Beta endpoint may change
2. **Cache tokens**: Don't request new token for every call
3. **Implement retry logic**: Handle transient failures
4. **Use batch requests**: Combine multiple requests
5. **Request only needed properties**: Use $select
6. **Handle pagination**: Always check for @odata.nextLink
7. **Follow rate limits**: Implement backoff strategy
8. **Use least privilege**: Request minimum required permissions

## Cleanup

```bash
# Delete app registration
az ad app delete --id $APP_ID

# Delete resource group
az group delete -y -n labs-graph --no-wait
```

## Additional Resources

- [Microsoft Graph documentation](https://docs.microsoft.com/en-us/graph/)
- [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
- [Microsoft Graph REST API v1.0 reference](https://docs.microsoft.com/en-us/graph/api/overview)
- [Graph SDK documentation](https://docs.microsoft.com/en-us/graph/sdks/sdks-overview)
- [Permissions reference](https://docs.microsoft.com/en-us/graph/permissions-reference)

## Next Steps

Complete the [AZ-204 exam exercises](AZ-204.md) which cover advanced scenarios and SDK usage required for the certification exam.
