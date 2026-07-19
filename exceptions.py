class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass

class NotFoundError(CustomError):
    """Exception raised for not found errors."""
    def __init__(self, resource):
        self.message = f"Resource '{resource}' not found"
        super().__init__(self.message)

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, field, errors):
        self.message = f"Validation failed for '{field}': {', '.join(errors)}"
        super().__init__(self.message)

class PermissionError(CustomError):
    """Exception raised for permission errors."""
    def __init__(self, action):
        self.message = f"Permission denied for action: '{action}'"
        super().__init__(self.message)