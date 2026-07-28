import sys

# Function to validate input data

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    if 'name' not in data or not isinstance(data['name'], str):
        raise ValueError('Input must contain a string key 