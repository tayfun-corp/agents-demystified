# Intro

This folder includes an example MCP server which simply lists files in a given directory.

# Installation

You need `uv` to setup the dependencies (only `mcp` at this point):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once you have uv, you can run the MCP server yourself for testing:

```bash
uv run main.py
```

# Setting up with Claude

To let Claude Desktop app know about the new MCP server, you need to open file `claude_desktop_config.json`, change `uv` path and `main.py` directory to your local paths and copy the file:

```bash
cp ./code/example_mcp/claude_desktop_config.json ~/Library/Application\ Support/Claude/
```

Next time you open Claude Desktop App, you should see new tool listed. See [MCP docs](https://modelcontextprotocol.io/quickstart/server#test-with-commands) if you run into any issues.

You can also check MCP logs:

```bash
tail -f ~/Library/Logs/Claude/mcp.log
```
