# Python Logging Module Cheat Sheet

# Importing the logging module
import logging

# Basic Logging
logging.debug("Debugging information")
logging.info("Informational message")
logging.warning("Warning:Config file %s not found", "server.conf")
logging.error("Error occurred")
logging.critical("Critical error -- shutting down")

# Basic Configuration
logging.basicConfig(level=logging.INFO)

# Logging Levels
logging.DEBUG  # Detailed information, typically of interest only when diagnosing problems.
logging.INFO  # Confirmation that things are working as expected.
logging.WARNING  # An indication that something unexpected happened, or indicative of some problem. But the software is still working as expected.
logging.ERROR  # Due to a more serious problem, the software has not been able to perform some function.
logging.CRITICAL  # A serious error, indicating that the program itself may be unable to continue running.

# Creating a Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Creating Handlers
c_handler = logging.StreamHandler()  # Console handler
f_handler = logging.FileHandler("file.log")  # File handler
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Creating Formatters and adding to handlers
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Adding Handlers to the Logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Logging Messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

# Logging Exception Information
try:
    1 / 0
except ZeroDivisionError:
    logger.error("ZeroDivisionError occurred", exc_info=True)

# Log Record Attributes
# Examples include %(name)s, %(levelname)s, %(message)s, %(asctime)s, etc.

# Rotating File Handler
from logging.handlers import RotatingFileHandler

r_handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
r_handler.setFormatter(f_format)
logger.addHandler(r_handler)

# Conditional Logging
if logger.isEnabledFor(logging.DEBUG):
    logger.debug("This message is logged because the debug level is set")
