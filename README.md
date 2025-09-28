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

## Requirements

- Python 3.8+
- FastMCP 0.4.0+
