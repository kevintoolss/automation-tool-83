import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=5, backoff_factor=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON if successful
        except requests.exceptions.RequestException as e:
            retries += 1
            if retries == max_retries:
                raise NetworkError(f'Failed to fetch {url} after {max_retries} attempts') from e
            wait_time = backoff_factor * (2 ** (retries - 1))
            time.sleep(wait_time)  # Exponential backoff

if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(e)