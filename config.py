import json
import os

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'log_level': 'INFO'
}

class ConfigLoader:
    def __init__(self, config_file=None):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self):
        if self.config_file and os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def all(self):
        return self.config

# Example usage: If this module was executed directly, we can load a config file
if __name__ == '__main__':
    loader = ConfigLoader('config.json')
    print(loader.all())
