
class DependencyInfo:
    def __init__(self, name, version, options):
        self.name = name
        self.version = version
        self.options = options

dependencyInfoObjList = [
    { "name": "fmt",        "version": "11.1.3",        "options" : [ "shared=True" ]},
    { "name": "openssl",    "version": "1.1.1w",         "options" : [ "shared=True" ]},
    { "name": "gtest",      "version": "1.15.0",        "options" : [ "shared=True" ]},
    { "name": "sdl",        "version": "2.30.9",        "options" : [ "shared=True" ]},
    { "name": "boost",      "version": "1.86.0",        "options" : []},
    { "name": "rapidjson",  "version": "1.1.0",         "options" : []},
    { "name": "magic_enum", "version": "0.9.7",         "options" : []},
    { "name": "lz4",        "version": "1.10.0",        "options" : []},
    { "name": "bullet3",    "version": "3.25",          "options" : []},
    { "name": "stb",        "version": "cci.20240531",  "options" : []},
    { "name": "glad",       "version": "0.1.36",        "options" : []},
    { "name": "glm",        "version": "1.0.1",         "options" : []},
    { "name": "inja",       "version": "3.4.0",         "options" : []}
]

dependencyInfoList = []

def PrepareDeps():
    for depJson in dependencyInfoObjList:
        name = depJson["name"]
        version = depJson["version"]
        options = depJson["options"]
        dep = DependencyInfo(name, version, options)
        dependencyInfoList.append(dep)

def GetDependencyInfoList():
    if len(dependencyInfoList) == 0:
        PrepareDeps()
    return dependencyInfoList
