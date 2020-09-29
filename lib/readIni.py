import configparser

def readIni(configPath, get1, get2):
    conf = configparser.ConfigParser()
    conf.read(configPath)
    return conf.get(get1, get2)