import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_attempts=3, wait_time=2):
    """
    Attempt to send a GET request to the specified URL with retry logic.
    :param url: The URL to send the request to.
    :param max_attempts: The maximum number of attempts (default is 3).
    :param wait_time: Time to wait between attempts in seconds (default is 2).
    :return: Response object if successful.
    """
    attempt = 0
    while attempt < max_attempts:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            attempt += 1
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                time.sleep(wait_time)
    raise Exception(f"Failed to retrieve data from {url} after {max_attempts} attempts")
