class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConnectionError(CustomError):
    """Exception raised for connection-related errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Exception raised when an item is not found."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AuthenticationError(CustomError):
    """Exception raised for authentication failures."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)