import os
from pprint import pprint

from dotenv import load_dotenv

from settings import app_config


def get_settings(config_name: str):
    return app_config[config_name]


print('Before load_dotenv()', os.getenv('MODE'))
env = os.getenv('MODE', 'TESTING')
settings = get_settings(config_name=env)
pprint(settings.dict())

load_dotenv()
print('After load_dotenv()', os.getenv('MODE'))
env = os.getenv('MODE', 'TESTING')
settings = get_settings(config_name=env)
pprint(settings.dict())
