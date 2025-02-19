
class ToolInfo:
    def __init__(self, name, commands, operatingSystem):
        self.name = name
        self.commands = commands
        self.operatingSystem = operatingSystem

toolInfoObjList = [
    { "name": "conan", "commands": ["pip", "install", "conan"], "operatingSystem": "any"},
    { "name": "cmake", "commands": ["pip", "install", "cmake"], "operatingSystem": "any"},
    { "name": "ninja", "commands": ["pip", "install", "Ninja"], "operatingSystem": "any"},
    { "name": "msvc",  "commands": ["install_buildtools.ps1"],  "operatingSystem": "Windows"},
]

toolInfoList = []

def PrepareTools():
    for depJson in toolInfoObjList:
        name = depJson["name"]
        commands = depJson["commands"]
        tool = ToolInfo(name, commands)
        toolInfoList.append(tool)

def GetToolInfoList():
    if len(toolInfoList) == 0:
        PrepareTools()
    return toolInfoList