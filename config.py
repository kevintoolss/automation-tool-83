import json
import os

DEFAULT_CONFIG = {
    'setting_1': 'default_value_1',
    'setting_2': 'default_value_2',
    'setting_3': 10,
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = {}
        self.load_configuration()

    def load_configuration(self):
        # Load defaults first
        self.config = DEFAULT_CONFIG.copy()
        
        # Check if the configuration file exists
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)

    def get(self, key, default=None):
        # Get the value of a setting, return default if not found
        return self.config.get(key, default)

    def set(self, key, value):
        # Set a specific configuration value
        self.config[key] = value
        
    def save(self):
        # Save the current configuration to a file
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)
