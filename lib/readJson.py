import json


def readJson(configPath, get):
    with open(configPath, "r")as f:
        return json.loads(f.read())[get]
