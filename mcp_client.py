import asyncio
import os
from contextlib import AsyncExitStack
from typing import Any, Dict, List, Optional

from anthropic import Anthropic
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()


class DjangoMCPClient:
    def __init__(self, server_command: str):
        """
        Initialize the MCP client

        Args:
            server_command: The command to start the MCP server
        """
        self.server_command = server_command
        self.anthropic = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    async def chat(self, messages: List[Dict[str, str]]) -> str:
        """
        Run a chat session with Claude using MCP context

        Args:
            messages: List of message objects (role and content)

        Returns:
            The assistant's response
        """
        async with AsyncExitStack() as stack:
            # Start the MCP server process and connect to it
            server_params = StdioServerParameters(
                command=self.server_command.split(),
            )

            client_session = await stack.enter_async_context(
                stdio_client(server_params)
            )

            # Get the manifest to understand server capabilities
            manifest = await client_session.manifest()
            print(f"Connected to server: {manifest.name}")

            # Create a context with available resources
            ctx = await client_session.create_context()

            # Add useful resources to context (could be dynamic based on user query)
            await ctx.add_resource("schema://User")
            await ctx.add_resource("docs://users")

            # Use the Claude API with the context
            client_messages = messages.copy()

            # Get the formatted context from MCP
            context_message = await ctx.format_for_claude()

            # Insert the context at the beginning of the conversation
            if context_message:
                client_messages.insert(0, {
                    "role": "user",
                    "content": context_message
                })
                client_messages.insert(1, {
                    "role": "assistant",
                    "content": "I'll help you with your Django application questions."
                })

            # Send the entire conversation to Claude
            response = await self.anthropic.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                messages=client_messages,
                tools=[tool.to_dict() for tool in ctx.tools]
            )

            return response.content[0].text
