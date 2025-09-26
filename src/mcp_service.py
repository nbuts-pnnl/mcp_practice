from fastmcp import FastMCP
import logging
import os

LOG_FORMAT = os.getenv("LOG_FORMAT")
LOG_DIR = os.getenv("LOG_DIR")
LOG_NAME = os.getenv("LOG_NAME")
LOG_LEVEL = os.getenv("LOG_LEVEL").upper()
SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT = int(os.getenv("SERVER_PORT"))

LOG_LEVELS = {
    "CRITICAL": logging.CRITICAL,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "NOTSET": logging.NOTSET
}

logging.basicConfig(level=LOG_LEVELS.get(LOG_LEVEL),
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
    mcp.run(transport="streamable-http", host=SERVER_HOST, port=SERVER_PORT)