import time
import random

class RetryConfig:
    def __init__(self, max_attempts=5, backoff_factor=1, jitter=True):
        self.max_attempts = max_attempts
        self.backoff_factor = backoff_factor
        self.jitter = jitter

    def backoff_time(self, attempt):
        # Calculate backoff time with optional jitter
        backoff = self.backoff_factor * (2 ** (attempt - 1))
        if self.jitter:
            backoff += random.uniform(0, 1)
        return backoff

def retry_operation(operation, *args, **kwargs):
    retries = RetryConfig()
    for attempt in range(1, retries.max_attempts + 1):
        try:
            return operation(*args, **kwargs)
        except Exception as e:
            if attempt == retries.max_attempts:
                raise e  # Raise final exception
            time.sleep(retries.backoff_time(attempt))
