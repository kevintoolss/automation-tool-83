import time


def timed_execution(func):
    """Decorator to time functions execution."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper


@timed_execution
def process_data(data):
    """Simulates data processing by sleeping."""
    time.sleep(1)  # Simulate long processing time
    return [x * 2 for x in data]


@timed_execution
def main():
    """Main function to run the process_data."""
    data = range(1000)
    processed_data = process_data(data)
    return processed_data


if __name__ == '__main__':
    main()