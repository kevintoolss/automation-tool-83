import json
from typing import Any, Dict

class CustomError(Exception):
    pass

def process_data(data: Dict[str, Any]) -> Dict[str, Any]:
    try:
        if not isinstance(data, dict):
            raise CustomError('Input must be a dictionary')
        if 'key' not in data:
            raise CustomError('Missing required key')
        # Simulating data processing
        result = {'status': 'success', 'value': data['key'] * 2}
        return result
    except TypeError:
        raise CustomError('Type error during processing')
    except CustomError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': 'An unexpected error occurred: ' + str(e)}

if __name__ == '__main__':
    sample_data = {'key': 10}
    response = process_data(sample_data)
    print(json.dumps(response, indent=4))
