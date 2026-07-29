import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file, level=logging.INFO):
    # Create a logger object
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    # Create a file handler for rotating logs
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
    handler.setLevel(level)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Example usage:
if __name__ == '__main__':
    logger = setup_logger('app.log')
    logger.info('Logger setup complete')