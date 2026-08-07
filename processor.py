import json
from typing import Any, Dict, List, Union

class DataProcessor:
    def __init__(self, data: Union[List[Dict[str, Any]], Dict[str, Any]]):
        self.data = data

    def to_json(self) -> str:
        """Convert data to JSON string."""
        return json.dumps(self.data, indent=4)

    def filter_by_key(self, key: str, value: Any) -> Union[List[Dict[str, Any]], None]:
        """Filter the data to find entries matching a specific key-value pair."""
        if isinstance(self.data, list):
            return [item for item in self.data if item.get(key) == value]
        return None

    def update_value(self, index: int, key: str, new_value: Any) -> None:
        """Update the value of a specific key in the data at a given index."""
        if isinstance(self.data, list) and 0 <= index < len(self.data):
            self.data[index][key] = new_value

    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the data representing counts of unique items."""
        summary = {}
        if isinstance(self.data, list):
            for item in self.data:
                for k, v in item.items():
                    summary[k] = summary.get(k, 0) + 1
        return summary

# Example usage:
# data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
# processor = DataProcessor(data)
# print(processor.to_json())
# filtered = processor.filter_by_key('age', 25)
# print(filtered)
# processor.update_value(0, 'age', 26)
# print(processor.get_summary())
