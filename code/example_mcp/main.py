import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ls")

@mcp.tool()
def list_files(path: str = ".") -> str:
    files = os.listdir(path)
    return "\n".join(files)

if __name__ == "__main__":
    mcp.run(transport='stdio')
