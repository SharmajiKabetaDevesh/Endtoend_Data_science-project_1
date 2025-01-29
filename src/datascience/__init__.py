# src/datascience/__init__.py
import logging
import os
from pathlib import Path

# Logging configuration
log_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = Path("logs")
log_file = log_dir / "app.log"

# Ensure the log directory exists
log_dir.mkdir(parents=True, exist_ok=True)

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()  
    ]
)

# Create a logger instance
logger = logging.getLogger("datasciencelogger")
logger.info("Logger initialized.")
