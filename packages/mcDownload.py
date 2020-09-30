import requests
from packages import readConfig

# 读取使用的API
api = readConfig.readJson("../config.json", "downloadAPI")
if api != "bmcl":
    if api == "mcbbs":
        api_load = "https://download.mcbbs.net/"
    if api == "mojang":
        api_load = "http://launchermeta.mojang.com/"
else:
    api_load = "https://bmclapi2.bangbang93.com/"


def versionList():
    version_list = requests.get(api_load + "mc/game/version_manifest.json")
