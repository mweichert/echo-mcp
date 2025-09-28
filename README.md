# echo-mcp

A simple FastMCP server that provides an echo tool which repeats input with the prefix "I hear you: ".

## Features

- Single `echo` tool that outputs "I hear you: [input]"
- Built with [FastMCP](https://github.com/jlowin/fastmcp)
- Supports MCP (Model Context Protocol) communication

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mweichert/echo-mcp.git
cd echo-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

To start the MCP server:

```bash
python server.py
```

The server will start and wait for MCP connections via stdio.

### Tool Documentation

The server provides one tool:

- **echo**: Takes a string input and returns it prefixed with "I hear you: "
  - Input: `input` (string) - The text to echo
  - Output: String in the format "I hear you: [input]"

### Testing

Run the test suite to verify functionality:

```bash
python test_echo.py
```

## Example

When called with input "Hello, World!", the echo tool returns:
```
I hear you: Hello, World!
```

## Deployment

### Docker Deployment

The server can be deployed using Docker:

```bash
# Build the Docker image
docker build -t echo-mcp .

# Run the container
docker run -it echo-mcp
```

### Render Deployment

This server is designed for MCP (Model Context Protocol) communication via stdio, which is different from traditional web services. For Render deployment:

1. **Using Docker**: The included `Dockerfile` and `render.yaml` can be used to deploy as a background worker service on Render.

2. **Important Note**: This is an MCP server that communicates via stdio (standard input/output), not HTTP. It's designed to be used by MCP clients that can communicate through stdin/stdout pipes, not web browsers or HTTP clients.

3. **Alternative**: If you need HTTP access, you might want to create a web wrapper around the MCP server or use it in an environment that supports MCP protocol directly.

### Local Development

For local development and testing with MCP clients:

```bash
python server.py
```

## Requirements

- Python 3.8+
- FastMCP 0.4.0+
