import json
import os

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'database': {
        'user': 'admin',
        'password': 'password',
        'name': 'app_db'
    }
}

class ConfigLoader:
    def __init__(self, config_file=None):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self):
        if self.config_file and os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        if self.config_file:
            with open(self.config_file, 'w') as file:
                json.dump(self.config, file, indent=4)

if __name__ == '__main__':
    config_loader = ConfigLoader('config.json')
    print(config_loader.config)