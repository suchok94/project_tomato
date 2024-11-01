import json
import configparser

def json_load(path):
    with open(path, "r") as read_file:
        data = json.load(read_file)
    return data

def txt_load(path):
    with open(path, "r") as read_file:
        data = read_file.read()
    return data

def take_path():

    config = configparser.ConfigParser()
    config.read('config.ini')
    path = config.get('Paths', 'storage_path')

    return path