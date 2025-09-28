#!/usr/bin/env python3
"""
Echo MCP Server

A FastMCP server that provides a single echo tool which outputs "I hear you: [input]".
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
    mcp.run()


if __name__ == "__main__":
    # Run the server
    main()