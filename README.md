# echo-mcp

A simple FastMCP server that provides an echo tool which repeats input with the prefix "I hear you: ". Configured as a remote MCP server with HTTP transport and no authentication required.

## Features

- Single `echo` tool that outputs "I hear you: [input]"
- Built with [FastMCP](https://github.com/jlowin/fastmcp)
- Remote MCP server with SSE (Server-Sent Events) transport
- No authentication required
- Ready for cloud deployment

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

To start the remote MCP server:

```bash
python server.py
```

The server will start on `http://0.0.0.0:8000` and serve MCP requests via HTTP/SSE transport.

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
docker run -p 8000:8000 echo-mcp
```

### Render Deployment

This server is configured as a remote MCP server with HTTP transport for easy deployment:

1. **Using Docker**: The included `Dockerfile` and `render.yaml` deploy as a web service on Render.

2. **Configuration**: The server runs on port 8000 with SSE transport, making it accessible to MCP clients over HTTP.

3. **No Authentication**: The server requires no authentication as requested.

4. **Deployment Steps**:
   - Connect your GitHub repo to Render
   - Use the included `render.yaml` configuration
   - Deploy as a web service (not background worker)

### Local Development

For local development and testing:

```bash
python server.py
```

The server will be available at `http://localhost:8000` for MCP client connections.

## Requirements

- Python 3.8+
- FastMCP 0.4.0+
