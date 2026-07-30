import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=5, delay=2):
    """Makes a GET request to the specified URL with retry logic.
    Retries the request if a network error occurs.
    """
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON content if the request is successful
        except requests.exceptions.RequestException as e:
            attempt += 1
            if attempt == retries:
                raise NetworkError(f'Failed to retrieve data from {url} after {retries} attempts') from e
            time.sleep(delay)  # Wait before the next attempt

# Example usage (commented out)
# if __name__ == '__main__':
#     try:
#         data = retry_request('https://api.example.com/data')
#         print(data)
#     except NetworkError as ne:
#         print(str(ne))