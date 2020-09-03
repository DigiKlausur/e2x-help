import os
import sys
from traitlets.config import Config
from traitlets.config.loader import PyFileConfigLoader

config_dir = os.path.join(sys.prefix, 'share', 'e2xhelp')
config_file = 'e2xhelp_config.py'

class ConfigManager:

    def __init__(self):
        os.makedirs(config_dir, exist_ok=True)

    def get_config(self):
        path = os.path.join(config_dir, config_file)
        if os.path.exists(path):
            return PyFileConfigLoader(path).load_config()
        return Config()