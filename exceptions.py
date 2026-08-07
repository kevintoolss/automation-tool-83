class DataHandlingError(Exception):
    """
    Custom exception for data handling errors.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidDataFormatError(DataHandlingError):
    """
    Exception raised for invalid data format.
    """
    def __init__(self, format_type):
        message = f"Invalid data format: {format_type}"
        super().__init__(message)

class MissingDataError(DataHandlingError):
    """
    Exception raised when required data is missing.
    """
    def __init__(self, field_name):
        message = f"Missing required field: {field_name}"
        super().__init__(message)

class DataProcessingError(DataHandlingError):
    """
    Exception raised for general data processing errors.
    """
    def __init__(self, details):
        message = f"Data processing error: {details}"
        super().__init__(message)
