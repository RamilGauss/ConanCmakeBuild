
class ToolInfo:
    def __init__(self, name, commands, operatingSystem):
        self.name = name
        self.commands = commands
        self.operatingSystem = operatingSystem

toolInfoObjList = [
    { "name": "conan", "commands": ["pip", "install", "conan"], "operatingSystem": "Windows"},
    { "name": "cmake", "commands": ["pip", "install", "cmake"], "operatingSystem": "Windows"},
    { "name": "ninja", "commands": ["pip", "install", "Ninja"], "operatingSystem": "Windows"},
    { "name": "conan", "commands": ["pip3", "install", "conan"], "operatingSystem": "Linux"},
    { "name": "cmake", "commands": ["pip3", "install", "cmake"], "operatingSystem": "Linux"},
    { "name": "ninja", "commands": ["pip3", "install", "Ninja"], "operatingSystem": "Linux"},
    { "name": "msvc",  "commands": ["install_buildtools.ps1"],  "operatingSystem": "Windows"},

    # Linux draft
    # sudo apt-get install gcc
    # sudo apt-get install g++
    # sudo apt-get install clang

    # sudo apt-get install pipx
    # pipx ensurepath


    # pipx install ninja
    # pipx install cmake
    # pipx install conan
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