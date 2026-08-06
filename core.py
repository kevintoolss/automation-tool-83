import json

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def to_json(self):
        """Converts the data to JSON format."""
        try:
            return json.dumps(self.data)
        except (TypeError, OverflowError) as e:
            print(f"Error converting to JSON: {e}")
            return None

    def from_json(self, json_str):
        """Loads data from a JSON string."""
        try:
            self.data = json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    def add_entry(self, key, value):
        """Adds a new key-value pair to the data."""
        if isinstance(self.data, dict):
            self.data[key] = value
        else:
            print("Data is not a dictionary.")

    def get_entry(self, key):
        """Retrieves a value by key from the data."""
        return self.data.get(key, None) if isinstance(self.data, dict) else None

    def remove_entry(self, key):
        """Removes a key-value pair from the data."""
        if isinstance(self.data, dict) and key in self.data:
            del self.data[key]
        else:
            print("Key not found or data is not a dictionary.")
