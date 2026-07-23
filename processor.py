def process_data(data):
    """
    Process input data and perform operations.
    Args:
        data (list): A list of numerical values to process.
    Returns:
        dict: A dictionary with statistics of the data.
    """
    if not data:
        return {'mean': 0, 'max': 0, 'min': 0}
    mean_value = sum(data) / len(data)
    max_value = max(data)
    min_value = min(data)
    return {
        'mean': mean_value,
        'max': max_value,
        'min': min_value
    }


def save_results(results, filename):
    """
    Save the results to a specified file.
    Args:
        results (dict): The results to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, 'w') as file:
        for key, value in results.items():
            file.write(f'{key}: {value}\n')


def load_data_from_file(filename):
    """
    Load data from a specified file.
    Args:
        filename (str): The name of the file to load data from.
    Returns:
        list: A list of numerical values loaded from the file.
    """
    data = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                data.append(float(line.strip()))
            except ValueError:
                continue  # Ignore non-float lines
    return data