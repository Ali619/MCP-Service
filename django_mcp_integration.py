import asyncio
import os

from asgiref.sync import async_to_sync
from django.conf import settings

from mcp_client import DjangoMCPClient


class DjangoMCPService:
    """
    Django integration for MCP service
    """

    def __init__(self):
        # Path to the MCP server script
        server_script = os.path.join(settings.BASE_DIR, "mcp_server.py")

        # Command to run the server
        server_command = f"python {server_script}"

        # Initialize the client
        self.client = DjangoMCPClient(server_command)

    def ask(self, user_query: str, conversation_history=None) -> str:
        """
        Ask a question to the MCP-powered assistant

        Args:
            user_query: The user's question
            conversation_history: Optional previous conversation

        Returns:
            The assistant's response
        """
        # Initialize or use provided conversation history
        if conversation_history is None:
            messages = []
        else:
            messages = conversation_history.copy()

        # Add the new user query
        messages.append({"role": "user", "content": user_query})

        # Use async_to_sync to call the async chat method
        response = async_to_sync(self.client.chat)(messages)

        # Return the assistant's response
        return response
