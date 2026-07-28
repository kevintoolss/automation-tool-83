def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    if 'name' not in data or not isinstance(data['name'], str):
        raise ValueError('Name is required and must be a string')
    if 'age' in data:
        if not isinstance(data['age'], int) or data['age'] < 0:
            raise ValueError('Age must be a non-negative integer')
    return True


def main_processing_loop(inputs):
    for input_data in inputs:
        try:
            validate_input(input_data)
            # Process the valid input
            print(f'Processing: {input_data}')
        except ValueError as e:
            print(f'Error: {e}')

# Example usage
if __name__ == '__main__':
    sample_inputs = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': -5},
        {'name': 'Charlie'}
    ]
    main_processing_loop(sample_inputs)