import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

# Create a logger instance
logger = logging.getLogger(__name__)

def log_info(message):
    """Log an info message."""
    logger.info(message)


def log_warning(message):
    """Log a warning message."""
    logger.warning(message)


def log_error(message):
    """Log an error message."""
    logger.error(message)


def log_debug(message):
    """Log a debug message."""
    logger.debug(message)


def log_exception(exception):
    """Log an exception with traceback."""
    logger.exception(exception)