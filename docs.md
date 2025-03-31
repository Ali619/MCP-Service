# MCP-Service Project Documentation

## Project Overview

This project integrates the Model Context Protocol (MCP) with Django to create an AI-powered assistant that can answer questions about Django applications. The integration allows the assistant to access Django model schemas, application documentation, and perform database queries.

## File Structure

- **mcp_server.py**: Defines the MCP server with tools and resources
- **mcp_client.py**: Implements the client that communicates with the MCP server and Claude API
- **django_mcp_integration.py**: Provides Django integration for the MCP service
- **views.py**: Contains Django views for the chat interface and API
- **urls.py**: Defines URL routing for the Django application
- **requirements.txt**: Lists project dependencies

## Components and Relationships

### MCP Server (mcp_server.py)

The MCP server is built using FastMCP and provides tools and resources that can be used by the AI assistant.

#### Classes and Functions:

- **FastMCP instance (mcp)**: The main MCP server instance
- **query_database()**: A tool for querying the Django database
- **get_model_schema()**: A resource for retrieving schema information for Django models
- **get_app_docs()**: A resource for retrieving documentation for Django apps

The server exposes these capabilities through the MCP protocol, allowing the AI assistant to access Django-specific information and functionality.

### MCP Client (mcp_client.py)

The MCP client connects to the MCP server and integrates with the Claude API to provide AI assistant capabilities.

#### Classes and Functions:

- **DjangoMCPClient**: Main client class that connects to the MCP server and Claude API
  - **__init__()**: Initializes the client with the server command
  - **chat()**: Runs a chat session with Claude using MCP context

The client starts the MCP server as a subprocess, connects to it, retrieves resources based on the user's query, and then sends the conversation with the context to Claude for processing.

### Django MCP Integration (django_mcp_integration.py)

This file provides the integration between Django and the MCP service.

#### Classes and Functions:

- **DjangoMCPService**: Main service class for Django integration
  - **__init__()**: Initializes the service with the path to the MCP server script
  - **ask()**: Sends a user query to the MCP-powered assistant and returns the response

The service uses Django's async_to_sync to call the async chat method of the MCP client, making it compatible with Django's synchronous views.

### Django Views (views.py)

This file contains the Django views for the chat interface and API.

#### Functions:

- **chat_with_assistant()**: API endpoint for chatting with the MCP-powered assistant
- **chat_interface()**: Renders the chat interface template

The views initialize the DjangoMCPService and use it to process user queries and return responses.

### URL Configuration (urls.py)

This file defines the URL routing for the Django application.

#### URL Patterns:

- **/chat/**: Renders the chat interface
- **/api/chat/**: API endpoint for chatting with the assistant

## Data Flow

1. A user submits a query through the chat interface or API
2. The Django view receives the request and passes it to the DjangoMCPService
3. The DjangoMCPService uses the DjangoMCPClient to:
   - Start the MCP server process
   - Connect to the server and retrieve the manifest
   - Create a context with relevant resources
   - Format the context for Claude
   - Send the conversation with context to Claude
   - Return Claude's response
4. The Django view returns the response to the user

## Dependencies

The project relies on several key dependencies:

- **Django**: Web framework
- **MCP**: Model Context Protocol library
- **Anthropic**: Claude API client
- **python-dotenv**: Environment variable management
- **asgiref**: ASGI utilities for Django

## Configuration

The project requires the following configuration:

- **ANTHROPIC_API_KEY**: API key for the Anthropic Claude API
- **Django settings**: Standard Django settings including BASE_DIR

## Extension Points

The project can be extended in several ways:

1. **Additional MCP Tools**: New tools can be added to the MCP server to provide more functionality
2. **Additional MCP Resources**: New resources can be added to provide more context to the assistant
3. **Enhanced Django Integration**: The integration can be extended to support more Django features
4. **Improved Chat Interface**: The chat interface can be enhanced with additional features

## Security Considerations

- API keys are loaded from environment variables using dotenv
- User input should be validated and sanitized to prevent injection attacks
- Access to the MCP server should be restricted to prevent unauthorized use
