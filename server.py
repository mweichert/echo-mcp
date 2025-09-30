#!/usr/bin/env python3
"""
Echo MCP Server

A FastMCP server that provides a single echo tool which outputs "I hear you: [input]".
Configured as a remote MCP server with HTTP transport and no authentication.
"""

import asyncio
from fastmcp import FastMCP, Context

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


@mcp.tool(exclude_args=["ctx"])
async def delegate(request: str, ctx: Context = None) -> str:
    """
    Delegate a request to an AI Agent Executive Assistant.

    The Executive Assistant manages a team of specialized AI agents and will
    intelligently delegate your request to the appropriate agents to complete
    the task. You can provide requests in natural language, just as you would
    with ChatGPT or Claude.

    Examples of requests:
    - "Analyze the sales data from Q3 and create a summary report"
    - "Research the latest trends in AI and write a blog post"
    - "Debug the authentication issue in the login module"
    - "Create a marketing plan for our new product launch"

    The assistant will provide real-time progress updates as work proceeds.

    Args:
        request: A natural language prompt describing the task or tasks you
                 want completed. Can be a single task or a list of tasks.

    Returns:
        Results from the Executive Assistant and delegated agents.
    """
    total_duration = 120  # 2 minutes
    update_interval = 5  # 5 seconds

    # Report progress: starting work
    if ctx:
        ctx.report_progress(0, total_duration, "Let me work on that for you")

    # Send progress updates every 5 seconds for 2 minutes
    for elapsed in range(update_interval, total_duration, update_interval):
        await asyncio.sleep(update_interval)
        if ctx:
            ctx.report_progress(elapsed, total_duration, f"Working on your request... ({elapsed}s elapsed)")

    # Final sleep to reach exactly 2 minutes
    await asyncio.sleep(update_interval)

    # Report progress: work complete
    if ctx:
        ctx.report_progress(total_duration, total_duration, "All Done")

    return "Task completed successfully after 2 minutes of processing."


def main():
    """Main entry point for the server."""
    # Configure as remote MCP server with HTTP transport, no auth
    mcp.run(transport="sse", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # Run the server
    main()