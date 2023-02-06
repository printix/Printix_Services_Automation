#this file reads the data for running the test from lab6

import yaml
from glob import glob
from os import getcwd
from random import choice

__config_path = f'{getcwd()}/Resources/'
__config_generated_path = f'{getcwd()}/Resources/generated/'

def load_service_devenv():
    with open(f'{__config_path}DevEnv.yml', 'r') as file:
        config_file = yaml.safe_load(file)
    return config_file

def load_service_testenv():
    with open(f'{__config_path}TestEnv.yml', 'r') as file:
        config_file = yaml.safe_load(file)
    return config_file

