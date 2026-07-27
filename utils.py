import time
import requests
from requests.exceptions import RequestException

def retry_request(url, retries=3, backoff_factor=0.3):
    """
    Attempts to send a GET request to a specified URL with retry logic.
    
    :param url: The URL to send the request to.
    :param retries: The number of retries before giving up.
    :param backoff_factor: A factor for backoff time between retries.
    :return: Response object or None if failed.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            wait = backoff_factor * (2 ** attempt)
            print(f'Attempt {attempt + 1} failed: {e}. Retrying in {wait:.1f} seconds...')
            time.sleep(wait)
    print('All retry attempts failed.')
    return None
