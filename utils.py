import json
import os
from typing import Any, Dict


def load_json(file_path: str) -> Dict[str, Any]:
    """Loads a JSON file and returns its content as a dictionary."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(file_path: str, data: Dict[str, Any]) -> None:
    """Saves a dictionary as a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merges two dictionaries recursively."""
    result = dict1.copy()  
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def extract_keys(data: Dict[str, Any], keys: list) -> Dict[str, Any]:
    """Extracts specified keys from a dictionary, returning a new dictionary."""
    return {key: data[key] for key in keys if key in data} 
