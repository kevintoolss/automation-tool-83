import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    """
    Sets up a logger with rotation.
    :param log_file: Path to the log file.
    :param max_bytes: Maximum file size in bytes before rotation.
    :param backup_count: Number of backup files to keep.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger
