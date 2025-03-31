import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from django_mcp_integration import DjangoMCPService

# Initialize the MCP service
mcp_service = DjangoMCPService()


@require_http_methods(["POST"])
def chat_with_assistant(request):
    """
    API endpoint to chat with the MCP-powered assistant
    """
    try:
        data = json.loads(request.body)
        user_query = data.get('query', '')
        conversation_history = data.get('conversation_history', [])

        # Get response from MCP service
        response = mcp_service.ask(user_query, conversation_history)

        # Update conversation history
        conversation_history.append({"role": "user", "content": user_query})
        conversation_history.append({"role": "assistant", "content": response})

        return JsonResponse({
            'response': response,
            'conversation_history': conversation_history
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def chat_interface(request):
    """
    Render the chat interface
    """
    return render(request, 'chat.html')
