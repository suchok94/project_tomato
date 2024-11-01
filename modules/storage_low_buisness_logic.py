import json

def json_load(path):
    with open(path, "r") as read_file:
        data = json.load(read_file)
    return data

def txt_load(path):
    with open(path, "r") as read_file:
        data = read_file.read()
    return data