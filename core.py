import json
from typing import Any, Dict, List, Union

def convert_to_json(data: Union[Dict[str, Any], List[Any]]) -> str:
    """
    Convert a dictionary or a list to a JSON string.
    
    Args:
        data (Union[Dict[str, Any], List[Any]]): The data structure to convert.
    
    Returns:
        str: JSON formatted string.
    """
    return json.dumps(data, indent=4)


def read_json_file(file_path: str) -> Union[Dict[str, Any], List[Any]]:
    """
    Read JSON data from a file and return it as a dictionary or list.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        Union[Dict[str, Any], List[Any]]: Parsed JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Union[Dict[str, Any], List[Any]]) -> None:
    """
    Write data to a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
        data (Union[Dict[str, Any], List[Any]]): The data to write.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
