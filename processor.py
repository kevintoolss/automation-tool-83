import sys
import json
from validators import validate_input

def main_processing_loop(data):
    for item in data:
        # Validate input item
        if not validate_input(item):
            print(f'Invalid input: {item}')
            continue  # Skip to the next item if validation fails
        # Process the valid item
        process_item(item)

def process_item(item):
    print(f'Processing item: {item}')

if __name__ == '__main__':
    # Example input data
    input_data = ['valid_item1', 'invalid_item', 'valid_item2']
    main_processing_loop(input_data)