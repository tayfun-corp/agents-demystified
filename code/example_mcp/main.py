import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ls")


@mcp.tool()
def list_files(path: str = ".") -> str:
    path = os.path.expanduser(path)
    files = os.listdir(path)
    return "\n".join(files)


@mcp.tool()
def create_file(path: str, content: str) -> str:
    path = os.path.expanduser(path)
    with open(path, "w") as f:
        f.write(content)
    os.chmod(path, 0o777)
    return f"File {path} created with permissions {oct(os.stat(path).st_mode)}"


@mcp.tool()
def edit_file(path: str, str_to_replace: str, str_to_replace_with: str) -> str:
    path = os.path.expanduser(path)
    with open(path, "r") as f:
        content = f.read()
    with open(path, "w") as f:
        f.write(content.replace(str_to_replace, str_to_replace_with))
    os.chmod(path, 0o777)
    return f"File {path} edited"


@mcp.tool()
def read_file(path: str) -> str:
    path = os.path.expanduser(path)
    with open(path, "r") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    mcp.run(transport="stdio")
