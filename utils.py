import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, delay=2):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status
            return response.json()  # Return JSON response if successful
        except requests.exceptions.RequestException as e:
            retries += 1
            if retries == max_retries:
                raise NetworkError(f'Failed to retrieve data after {max_retries} attempts: {str(e)}')
            time.sleep(delay)  # Wait before retrying

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as ne:
        print(ne)