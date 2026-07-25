import json
import os

DEFAULT_CONFIG = {
    'setting_1': 'default_value_1',
    'setting_2': 'default_value_2',
    'setting_3': 42,
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()  

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                try:
                    user_config = json.load(f)
                    return {**DEFAULT_CONFIG, **user_config}
                except json.JSONDecodeError:
                    print('Error decoding JSON. Using defaults.')
        return DEFAULT_CONFIG

    def get(self, key, default=None):
        return self.config.get(key, default)

# Usage
if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.get('setting_1'))  # Outputs: default_value_1
