import json
from typing import Any, Dict

class CustomError(Exception):
    pass

def process_data(data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise CustomError('Input is not a dictionary')
    try:
        processed = {key: value for key, value in data.items() if value is not None}
        if not processed:
            raise CustomError('No valid data to process')
    except Exception as e:
        raise CustomError(f'An error occurred while processing data: {e}') from e
    return processed

def load_and_process_json(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise CustomError(f'File not found: {file_path}')
    except json.JSONDecodeError:
        raise CustomError('Invalid JSON format')
    return process_data(data)

if __name__ == '__main__':
    try:
        result = load_and_process_json('data.json')
        print(result)
    except CustomError as e:
        print(f'Error: {e}')