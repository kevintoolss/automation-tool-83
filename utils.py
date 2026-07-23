import time
from functools import wraps


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@execution_time
def optimize_data_processing(data):
    optimized_data = []
    for item in data:
        # Simulate a processing step
        processed_item = item * 2  # Example operation
        optimized_data.append(processed_item)
    return optimized_data


def filter_data(data, threshold):
    return [item for item in data if item > threshold]


def main():
    data = list(range(10000))
    optimized_data = optimize_data_processing(data)
    filtered_data = filter_data(optimized_data, 5000)
    print(filtered_data)


if __name__ == "__main__":
    main()