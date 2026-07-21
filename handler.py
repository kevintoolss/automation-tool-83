import json
from typing import Any, Dict, List, Union

def load_json(file_path: str) -> Union[Dict[str, Any], List[Any]]:
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data: Union[Dict[str, Any], List[Any]], file_path: str) -> None:
    """Save data as JSON to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, with dict2 overwriting dict1 keys."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged

if __name__ == '__main__':
    sample_data = {'name': 'Automation Tool', 'version': 1.0}
    save_json(sample_data, 'data.json')
    loaded_data = load_json('data.json')
    print(loaded_data)
    additional_data = {'description': 'A tool for automation.'}
    combined_data = merge_dicts(loaded_data, additional_data)
    print(combined_data)