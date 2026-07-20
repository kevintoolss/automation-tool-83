class CustomException(Exception):
    """Base class for custom exceptions in this module."""
    pass

class ValidationError(CustomException):
    """Exception raised for validation errors."""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class DatabaseError(CustomException):
    """Exception raised for database related errors."""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomException):
    """Exception raised when a resource is not found."""
    def __init__(self, resource_name: str) -> None:
        self.message = f'{resource_name} not found.'
        super().__init__(self.message)

# Example usage of exceptions
if __name__ == '__main__':
    try:
        raise ValidationError('Invalid input!')
    except ValidationError as e:
        print(e)
    
    try:
        raise NotFoundError('User')
    except NotFoundError as e:
        print(e)
    
    try:
        raise DatabaseError('Database connection failed.')
    except DatabaseError as e:
        print(e)