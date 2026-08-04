import logging

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, message):
        try:
            self.logger.debug(message)
        except Exception as e:
            self.logger.error('Error logging debug message: %s', e)

    def info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.logger.error('Error logging info message: %s', e)

    def warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.logger.error('Error logging warning message: %s', e)

    def error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.logger.error('Error logging error message: %s', e)

    def critical(self, message):
        try:
            self.logger.critical(message)
        except Exception as e:
            self.logger.error('Error logging critical message: %s', e)