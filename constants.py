import os

# Define global constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# API constants
API_TIMEOUT = 30  # seconds
API_RETRIES = 3  # number of retry attempts

# File processing constants
MAX_FILE_SIZE = 10485760  # 10 MB in bytes
SUPPORTED_FILE_TYPES = ['.txt', '.csv', '.json']

# Logging constants
LOGGING_LEVEL = 'DEBUG'
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Database constants
DB_CONNECTION_STRING = 'sqlite:///mydatabase.db'
DB_TIMEOUT = 5  # seconds

# Miscellaneous constants
DEFAULT_LANGUAGE = 'en'
ITEMS_PER_PAGE = 10