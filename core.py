import time

def optimized_function(data):
    start_time = time.time()
    results = []
    results_dict = {}
    for item in data:
        if item not in results_dict:
            results_dict[item] = heavy_computation(item)
        results.append(results_dict[item])
    end_time = time.time()
    print(f"Function executed in {end_time - start_time} seconds")
    return results


def heavy_computation(item):
    time.sleep(1)  # Simulates a heavy computation
    return item * 2  # Example computation