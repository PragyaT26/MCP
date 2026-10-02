from fastmcp import FastMCP

mcp = FastMCP()
@mcp.tool()
def fetch():
    '''Use this tool to fetch data from source''' #doc string for description specially in mcp
    return {"data": "Hello MCP!"}
@mcp.tool()

def process():
    '''use this tool to process the fetched data'''
    return{'proceed_data':"data has been processed! "}

if __name__ == "__main__":
    mcp.run(transport="stdio")