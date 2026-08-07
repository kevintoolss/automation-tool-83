import sys

# Function to validate input

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty.")

# Main processing loop

def main_processing_loop():
    while True:
        user_input = input("Enter some data (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        try:
            validate_input(user_input)
            print(f"Processing input: {user_input}")
        except ValueError as e:
            print(f"Input Error: {e}")

if __name__ == '__main__':
    main_processing_loop()