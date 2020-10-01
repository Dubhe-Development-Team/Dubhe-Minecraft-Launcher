import requests, os, platform, json
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
                version = requests.get("https://bmclapi2.bangbang93.com/forge/minecraft/" + str(mcVer))
        else:
            for mcVer in mcVersion:
                version = requests.get(api_load + "forge/minecraft/" + str(mcVer))

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
        version = "Warning, are you crazing?"

    if type(version) == str:
        # 返回值
        return version
    else:
        return version.text


def dlMinecraft(Version, Category, Name):
    file = requests.get(api_load + "version/" + Version + "/" + Category)
    if Category == "client":
        file_dir = ".minecraft/versions/" + Name
        file_ru = os.path.exists(file_dir)
        if not file_ru:
            file_json = requests.get(api_load + "version/" + Version + "/json")
            os.makedirs('.minecraft/versions/' + Name, exist_ok=True)
            with open(file_dir + "/" + Name + ".jar", "wb") as code:
                code.write(file.content)
            with open(file_dir + "/" + Name + ".json", "wb") as code:
                code.write(json.dumps(file_json.content, indent=4))
        else:
            return print("目录已存在")
    elif Category == "server":
        with open(Name + ".jar", "wb") as code:
            code.write(file.content)
    else:
        return print("文件不存在")


def dlJava():
    global api_load
    if api == "mojang":
        api_load = "https://bmclapi2.bangbang93.com/"
    system = platform.architecture()
    if system == ('32bit', 'ELF'):
        java = requests.get(api_load + "java/jre_x86.rpm")
        with open("jre_x86.rpm", "wb") as code:
            code.write(java.content)
    elif system == ('64bit', 'ELF'):
        java = requests.get(api_load + "java/jre_x64.rpm")
        with open("jre_x86.rpm", "wb") as code:
            code.write(java.content)
    elif system == ('32bit', 'WindowsPE'):
        java = requests.get(api_load + "java/jre_x86.exe")
        with open("jre_x86.exe", "wb") as code:
            code.write(java.content)
    elif system == ('64bit', 'WindowsPE'):
        java = requests.get(api_load + "java/jre_x64.exe")
        with open("jre_x64.exe", "wb") as code:
            code.write(java.content)
