def is_valid_email(email):
    """Check if the provided email is valid."""
    import re
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


def is_non_empty_string(value):
    """Check if the provided value is a non-empty string."""
    return isinstance(value, str) and bool(value.strip())


def is_positive_integer(value):
    """Check if the provided value is a positive integer."""
    return isinstance(value, int) and value > 0


def is_valid_url(url):
    """Check if the provided URL is valid."""
    import re
    regex = r'^(http|https)://[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})?$'
    return re.match(regex, url) is not None


def is_in_range(value, min_value, max_value):
    """Check if the provided value is within a given range."""
    return isinstance(value, (int, float)) and min_value <= value <= max_value

