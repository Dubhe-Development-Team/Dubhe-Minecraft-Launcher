from lib import readIni
from lib import readJson

a = readIni.readIni("config.ini", "Dubhe Launcher", "b")
print(a)
b = readIni.readIni("C:/Users/Administrator/Desktop/config.ini", "Dubhe Launcher", "b")
print(b)

c = readJson.readJson("config.json", "a")
print(c)