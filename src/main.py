from fastapi import FastAPI
from fastmcp import FastMCP
import logging

import config as config

logging.basicConfig(level=config.LOG_LEVELS.get(config.LOG_LEVEL),
    format=config.LOG_FORMAT,
    handlers=[
        logging.FileHandler(config.LOG_DIR),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(config.LOG_NAME)

app = FastAPI(title="Math MCP Service")

#TODO: Root endpoint currently not accessible, when run as an MCP service.
#      MCP endpoints not accessible when run as FastAPI service.
#      Need to consolodate them properly.
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Math MCP Service!"}

mcp = FastMCP("Math")

@mcp.tool()
async def add(a: int, b: int) -> dict:
    """Add two numbers"""
    logger.info(f"Adding {a} and {b}")
    c = a + b
    logger.info(f"Result of addition: {c}")
    return {"result": c}

@mcp.tool()
async def multiply(a: int, b: int) -> dict:
    """Multiply two numbers"""
    logger.info(f"Multiplying {a} and {b}")
    c = a * b
    logger.info(f"Result of multiplication: {c}")
    return {"result": c}

mcp_app = mcp.http_app(path ='/mcp')
app = FastAPI(title="Math MCP Service", lifespan=mcp_app.lifespan)
app.mount("/mcp", mcp_app)

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host=config.SERVER_HOST, port=config.SERVER_PORT)