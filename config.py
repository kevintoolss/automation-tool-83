import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'log_level': 'INFO',
}

def load_config(file_path: str) -> Dict[str, Any]:
    """Load configuration from a JSON file, using defaults if necessary."""
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        return DEFAULT_CONFIG  # Return defaults if file not found
    except json.JSONDecodeError:
        return DEFAULT_CONFIG  # Return defaults on JSON decode error
    return {**DEFAULT_CONFIG, **config}  # Merge defaults with loaded config
