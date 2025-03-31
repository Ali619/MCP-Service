# Django MCP Integration

A Django integration for the Model Context Protocol (MCP) that enables AI-powered assistance for Django applications.

## Overview

This project integrates Django with the Model Context Protocol (MCP) and Claude AI to create an intelligent assistant that can answer questions about your Django application. The assistant can access model schemas, application documentation, and perform database queries.

## Features

- **AI-Powered Chat Interface**: Web interface for interacting with the assistant
- **REST API**: API endpoint for programmatic access to the assistant
- **Django Model Integration**: Access to Django model schemas and data
- **Documentation Access**: Retrieval of application documentation

## Architecture

The project consists of several components:

- **MCP Server**: Provides tools and resources for the AI assistant
- **MCP Client**: Connects to the MCP server and Claude API
- **Django Integration**: Bridges Django and the MCP service
- **Web Interface**: User interface for interacting with the assistant

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```
   ANTHROPIC_API_KEY=your_api_key
   ```
4. Add the URLs to your Django project's urls.py:
   ```python
   urlpatterns = [
       # ... your existing URLs
       path('', include('mcp_service.urls')),
   ]
   ```

## Usage

### Web Interface

Access the chat interface at `/chat/` to interact with the assistant through a web interface.

### API

Send POST requests to `/api/chat/` with the following JSON payload:

```json
{
  "query": "Your question here",
  "conversation_history": [] // Optional previous conversation
}
```

## Extending

### Adding New Tools

Add new tools to the MCP server in `mcp_server.py`:

```python
@mcp.tool()
def your_tool_function(param1: str, param2: int = 0) -> Dict[str, Any]:
    """
    Your tool description
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Result of the tool operation
    """
    # Your implementation here
    return {"result": "value"}
```

### Adding New Resources

Add new resources to the MCP server in `mcp_server.py`:

```python
@mcp.resource("resource://{param}")
def your_resource_function(param: str) -> Any:
    """
    Your resource description
    
    Args:
        param: Description of param
        
    Returns:
        Resource data
    """
    # Your implementation here
    return {"data": "value"}
```

## Documentation

For detailed documentation, see [docs.md](docs.md).

## License

MIT

## Requirements

- Python 3.8+
- Django 4.0+
- Anthropic API key
