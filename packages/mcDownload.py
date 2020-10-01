import requests
from packages import readConfig

# 读取使用的API
api = readConfig.readJson("../config.json", "downloadAPI")

if api == "bmcl":
    api_load = "https://bmclapi2.bangbang93.com/"
elif api == "mcbbs":
    api_load = "https://download.mcbbs.net/"
elif api == "mojang":
    api_load = "http://launchermeta.mojang.com/"


def getList(download):

    # Minecraft本体列表
    if download == "mc":
        version = requests.get(api_load + "mc/game/version_manifest.json")

    # Forge列表
    elif download == "forge":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/forge/download")
        else:
            version = requests.get(api_load + "forge/list/")

    # Liteloadder列表
    elif download == "liteloader":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/liteloader/list")
        else:
            version = requests.get(api_load + "liteloader/list")

    # Optifine列表
    elif download == "optifine":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/optifine/versionList")
        else:
            version = requests.get(api_load + "optifine/versionList")

    # Java列表
    elif download == "java":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/java/list")
        else:
            version = requests.get(api_load + "java/list")