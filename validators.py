def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')  
    if not user_input:
        raise ValueError('Input cannot be empty.')  
    if len(user_input) > 100:
        raise ValueError('Input cannot exceed 100 characters.')  
    return True

if __name__ == '__main__':
    inputs = ['valid input', '', 123, 'this is a very long input string that exceeds the maximum limit of one hundred characters which is not allowed']
    for inp in inputs:
        try:
            validate_input(inp)
            print(f"'{inp}' is a valid input.")
        except ValueError as e:
            print(f"'{inp}' - {e}")