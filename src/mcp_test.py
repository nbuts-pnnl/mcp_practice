from fastmcp import FastMCP
import logging

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DIR = "logs//mcp.log"
LOG_NAME = "mathtool"

logging.basicConfig(level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_DIR),
        logging.StreamHandler()
    ]
)

mcp = FastMCP(name="Math")


@mcp.tool()
async def add(a: int, b: int) -> dict:
    """Add two numbers"""
    logger = logging.getLogger(LOG_NAME)
    logger.info(f"Adding {a} and {b}")
    c = a + b
    logger.info(f"Result of addition: {c}")
    return {"result": c}

@mcp.tool()
async def multiply(a: int, b: int) -> dict:
    """Multiply two numbers"""
    logger = logging.getLogger(LOG_NAME)
    logger.info(f"Multiplying {a} and {b}")
    c = a * b
    logger.info(f"Result of multiplication: {c}")
    return {"result": c}

if __name__ == "__main__":
    mcp.run(transport="stdio")