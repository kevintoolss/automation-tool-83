import time
from typing import List, Callable

def timeit(func: Callable) -> Callable:
    """Decorator to measure execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

@timeit
def compute_factorial(n: int) -> int:
    """Compute factorial of a given number using an efficient iterative approach."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@timeit
def batch_process(items: List[int]) -> List[int]:
    """Process a batch of items and compute their factorials."""
    return [compute_factorial(item) for item in items if item >= 0]