#!/usr/bin/env python3
"""
Echo MCP Server

A FastMCP server that provides a single echo tool which outputs "I hear you: [input]".
Configured as a remote MCP server with HTTP transport and no authentication.
"""

import asyncio
from fastmcp import FastMCP

# Create the FastMCP server instance
mcp = FastMCP("Echo Server")


@mcp.tool()
def echo(input: str) -> str:
    """
    Echo tool that repeats the input with a prefix.
    
    Args:
        input: The text to echo
        
    Returns:
        The input text prefixed with "I hear you: "
    """
    return f"I hear you: {input}"


def main():
    """Main entry point for the server."""
    # Configure as remote MCP server with HTTP transport, no auth
    mcp.run(transport="sse", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # Run the server
    main()