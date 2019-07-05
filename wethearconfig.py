import configparser
import json

config = configparser.ConfigParser()

with open('config.json', 'r') as f:
    config = json.load(f)

def getdbfile():
    return config['DEFAULT']['DB_FILE']

def get(section, keyname):
    return config[section]['keyname']