import json
import os

def read_json_file(filepath):
    """Read and parse a JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    with open(filepath, 'r') as file:
        return json.load(file)

def write_json_file(data, filepath):
    """Write a dictionary to a JSON file."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def merge_dicts(dict1, dict2):
    """Merge two dictionaries."""
    result = dict1.copy()  # Start with dict1's keys and values
    result.update(dict2)  # Modifies result with dict2's keys and values & returns None
    return result

def print_json(data):
    """Print a dictionary in JSON format."""
    print(json.dumps(data, indent=4))