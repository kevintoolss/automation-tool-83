from typing import Final

# Define constants used throughout the automation tool

# Base URL for the automation service
SERVICE_BASE_URL: Final[str] = 'https://api.automationtool.com/'

# HTTP status codes
HTTP_OK: Final[int] = 200
HTTP_NOT_FOUND: Final[int] = 404
HTTP_INTERNAL_ERROR: Final[int] = 500

# Timeouts in seconds
DEFAULT_TIMEOUT: Final[int] = 30

# Default configuration values
DEFAULT_RETRY_ATTEMPTS: Final[int] = 5
DEFAULT_RETRY_DELAY: Final[int] = 2  # in seconds

# Supported file types for processing
SUPPORTED_FILE_TYPES: Final[list[str]] = ['.csv', '.json', '.xml']

# Error messages
ERROR_MESSAGES: Final[dict[str, str]] = {
    'file_not_supported': 'The file type is not supported.',
    'service_unavailable': 'The automation service is currently unavailable.',
}
