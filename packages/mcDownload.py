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


def getList(What):
    what = What

    # Minecraft本体列表
    if what == "mc":
        version = requests.get(api_load + "mc/game/version_manifest.json")

    # Forge列表
    if what == "forge":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/forge/download")
        else:
            version = requests.get(api_load + "forge/list/")

    # Liteloadder列表
    if what == "liteloader":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/liteloader/list")
        else:
            version = requests.get(api_load + "liteloader/list")

    # Optifine列表
    if what == "optifine":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/optifine/versionList")
        else:
            version = requests.get(api_load + "optifine/versionList")

    # Java列表
    if what == "java":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/java/list")
        else:
            version = requests.get(api_load + "java/list")