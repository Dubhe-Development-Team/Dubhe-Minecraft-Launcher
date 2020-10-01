import requests
from packages import readConfig

# 读取使用的API
api = readConfig.readJson("./config.json", "downloadAPI")
if api != "bmcl":
    if api == "mcbbs":
        api_load = "https://download.mcbbs.net/"
    elif api == "mojang":
        api_load = "http://launchermeta.mojang.com/"
else:
    api_load = "https://bmclapi2.bangbang93.com/"


def getList(What, *mcVersion):
    global version
    what = What

    # Minecraft本体列表
    if what == "mc":
        version = requests.get(api_load + "mc/game/version_manifest.json")

    # Forge列表
    elif what == "forge":
        if api == "mojang":
            for mcVer in mcVersion:
                version = requests.get("https://bmclapi2.bangbang93.com/forge/minecraft/" +str(mcVer))
        else:
            for mcVer in mcVersion:
                version = requests.get(api_load + "forge/minecraft/" +str(mcVer))

    # Liteloadder列表
    elif what == "liteloader":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/liteloader/list")
        else:
            version = requests.get(api_load + "liteloader/list")

    # Optifine列表
    elif what == "optifine":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/optifine/versionList")
        else:
            version = requests.get(api_load + "optifine/versionList")

    # Java列表
    elif what == "java":
        if api == "mojang":
            version = requests.get("https://bmclapi2.bangbang93.com/java/list")
        else:
            version = requests.get(api_load + "java/list")

    else:
        version = "Warning, are you crazying?"

    if type(version) == str:
        # 返回值
        return version
    else:
        return version.text
