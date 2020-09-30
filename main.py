from packages import readConfig

a = readConfig.readIni("config.ini", "Dubhe Launcher", "b")
print(a)
b = readConfig.readIni("C:/Users/Administrator/Desktop/config.ini", "Dubhe Launcher", "b")
print(b)

c = readConfig.readJson("config.json", "a")
print(c)
