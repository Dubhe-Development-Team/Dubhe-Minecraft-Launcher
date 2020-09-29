import configparser
import json


def readIni(configPath, get1, get2):
    conf = configparser.ConfigParser()
    conf.read(configPath)
    return conf.get(get1, get2)


def readJson(configPath, get):
    with open(configPath, "r")as f:
        return json.loads(f.read())[get]