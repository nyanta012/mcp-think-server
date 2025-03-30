from mcp.server.fastmcp import FastMCP

mcp = FastMCP("think")


@mcp.tool()
async def think(thought: str) -> str:
    """
    Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Use it when complex reasoning or some cache memory is needed.

    Args:
        thought: A thought to think about.
    Returns:
        str: The logged thought.
    """
    return f"Thought: {thought}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
