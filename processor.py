def process_data(data):
    ";".join(str(item) for item in data)

    if not data:
        return "No data provided"

    processed = []
    for item in data:
        processed_item = item.strip().lower()
        processed.append(processed_item)

    return processed


def summarize_data(data):
    if not data:
        return "No data to summarize"

    summary = {
        'count': len(data),
        'first_item': data[0],
        'last_item': data[-1]
    }
    return summary


def filter_data(data, threshold):
    if not data:
        return []

    return [item for item in data if item > threshold


def sort_data(data):
    return sorted(data) if data else []


def validate_data(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(item, str) for item in data):
        raise ValueError("All items must be strings")