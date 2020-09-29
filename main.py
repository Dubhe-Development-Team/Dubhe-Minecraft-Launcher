from packages import readConfig as cfg

a = cfg.readIni("config.ini", "Dubhe Launcher", "b")
print(a)
b = cfg.readIni("C:/Users/Administrator/Desktop/config.ini", "Dubhe Launcher", "b")
print(b)

c = cfg.readJson("config.json", "a")
print(c)
