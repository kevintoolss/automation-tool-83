import os

# Define constant file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configuration of default settings
DEFAULT_CONFIG = {
    'timeout': 30,
    'max_retries': 5,
    'api_base_url': 'https://api.example.com/',
}

# Error messages
ERROR_MESSAGES = {
    'not_found': 'Requested resource was not found.',
    'unauthorized': 'Access denied due to invalid credentials.',
    'timeout': 'The operation timed out.',
}

# Commonly used data formats
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'
DATETIME_FORMAT = f'{DATE_FORMAT} {TIME_FORMAT}'

# API response status codes
HTTP_STATUS = {
    'OK': 200,
    'CREATED': 201,
    'NO_CONTENT': 204,
    'BAD_REQUEST': 400,
    'UNAUTHORIZED': 401,
    'FORBIDDEN': 403,
    'NOT_FOUND': 404,
    'INTERNAL_SERVER_ERROR': 500,
}
