import time
import requests
from functools import wraps


def retry_request(max_retries=3, delay=2):
    """
    Decorator to add retry logic to network requests.
    """  
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    attempts += 1
                    if attempts == max_retries:
                        raise
                    print(f'Retry {attempts}/{max_retries} for {func.__name__} due to {e}')
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_request(max_retries=5, delay=3)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# Example usage
if __name__ == '__main__':
    try:
        data = fetch_data('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(f'Failed to fetch data: {e}')