import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=5, delay=2):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            # Check for HTTP errors
            response.raise_for_status()
            return response.json()  # Return JSON data on success
        except requests.exceptions.RequestException as e:
            print(f"Attempt {retries + 1} failed: {e}")
            retries += 1
            time.sleep(delay)  # Wait before retrying
            
    raise NetworkError(f"Failed to retrieve data from {url} after {max_retries} attempts")
