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

def txt_save(storage, path):
    with open(path, "w") as write_file:
        write_file.write(storage.toTxt())


def json_save(storage, path):
    with open(path, "w") as write_file:
        json.dump(storage.toJson(), write_file)



def take_path(expansion):

    config = configparser.ConfigParser()
    config.read('config.ini')
    if expansion == 'json':
        path = config.get('Paths', 'storage_path_json')
    elif expansion == 'txt':
        path = config.get('Paths', 'storage_path_txt')

    return path

def take_default_statistic():
    config = configparser.ConfigParser()
    config.read('config.ini')
    statistic = config.get('DefaultStatistic', 'Statistic')
    return statistic


def take_standard_mode():
    config = configparser.ConfigParser()
    config.read('config.ini')
    mode = config.get('StandardMode', 'Mode')
    return mode
