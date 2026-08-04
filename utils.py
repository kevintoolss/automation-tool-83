import json


def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON: {e}")
        return None


def save_json(file_path, data):
    """Save data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving JSON: {e}")


def flatten_dict(nested_dict, parent_key='', sep='_'):
    """Flatten a nested dictionary."""
    items = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def filter_dict(input_dict, keys):
    """Filter a dictionary by a list of keys."""
    return {key: input_dict[key] for key in keys if key in input_dict}
