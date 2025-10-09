import os
import logging
from dotenv import load_dotenv

load_dotenv()

LOG_FORMAT = os.getenv("LOG_FORMAT")
LOG_DIR = os.getenv("LOG_DIR")
LOG_NAME = os.getenv("LOG_NAME")
LOG_LEVEL = os.getenv("LOG_LEVEL")
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