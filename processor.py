import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    """Attempts to make a network request with retry logic."""
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response on success
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(delay)  # Wait before retrying
            else:
                raise NetworkError(f'Failed to connect to {url} after {retries} attempts') from e

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(e)