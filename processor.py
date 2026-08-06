import json

class InputValidationError(Exception):
    pass

def process_input(user_input):
    if not isinstance(user_input, str):
        raise InputValidationError("Input must be a string")
    if len(user_input) == 0:
        raise InputValidationError("Input cannot be empty")
    return user_input.strip()

def main_loop():
    while True:
        user_input = input("Enter something (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        try:
            validated_input = process_input(user_input)
            print(f"Processed Input: {validated_input}")
        except InputValidationError as e:
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    main_loop()