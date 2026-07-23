import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, delay=2):
    """Perform a GET request with retry logic.

    Args:
        url (str): The URL to make the request to.
        max_retries (int): Maximum number of retry attempts.
        delay (int): Delay between retries in seconds.

    Returns:
        Response: The response object from the request.
    """
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            attempts += 1
            print(f'Attempt {attempts} failed: {e}')
            if attempts < max_retries:
                time.sleep(delay)  # Wait before retrying
    raise Exception(f'Max retries exceeded for URL: {url}')
