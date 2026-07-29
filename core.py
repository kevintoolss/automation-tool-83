from typing import List, Dict


def process_data(data: List[Dict[str, int]]) -> List[int]:
    """Processes a list of dictionaries and returns a list of result integers.

    Each dictionary is expected to contain numeric values, and the function computes their sum.

    Args:
        data (List[Dict[str, int]]): A list of dictionaries containing numeric values.

    Returns:
        List[int]: A list of integers representing the sums of the values in each dictionary.
    """
    results = []
    
    for item in data:
        if not isinstance(item, dict):
            raise ValueError('Each item must be a dictionary.')
        results.append(sum(item.values()))
    return results


def main() -> None:
    """Main function to demonstrate the processing of data.

    This function serves as an entry point for the script and can be modified to process
    real input data.
    """
    sample_data = [
        {'a': 1, 'b': 2},
        {'x': 10, 'y': 20, 'z': 5},
        {'m': 0, 'n': -1},
    ]
    processed_results = process_data(sample_data)
    print(processed_results)  # Output the processed results before returning.


if __name__ == '__main__':
    main()