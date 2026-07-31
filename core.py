import requests
import time
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=2):
    """
    Perform a GET request and retry on failure.
    
    :param url: The URL to send the request to.
    :param max_retries: Max number of retries for the request.
    :param delay: Delay in seconds between retries.
    :return: Response object on success or None on failure.
    """
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response
        except RequestException as e:
            attempt += 1
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                time.sleep(delay)
    return None  

# Example usage of retry_request
if __name__ == "__main__":
    result = retry_request('https://example.com/api/data')
    if result is not None:
        print("Request succeeded:", result.json())
    else:
        print("Request failed after retries."),
