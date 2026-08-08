import json
import os

class ConfigLoader:
    def __init__(self, default_config_path: str):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self) -> dict:
        """Load default configuration from a JSON file."""
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def update_config(self, user_config_path: str):
        """Update configuration with user-specified settings."""
        if os.path.exists(user_config_path):
            with open(user_config_path, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)
        else:
            print(f'Warning: User config file {user_config_path} not found. Using defaults.')

    def get_config(self) -> dict:
        """Get the merged configuration."""
        return self.config

# Usage Example:
# config_loader = ConfigLoader('defaults.json')
# config_loader.update_config('user_config.json')
# config = config_loader.get_config()  
