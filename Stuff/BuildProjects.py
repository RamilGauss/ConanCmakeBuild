import os
import json

import subprocess

from CommandRunner import  CommandRunner
from SystemInfo import GetOperatingSystem

# cmake --preset conan-debug
# cmake --build --preset conan-debug


# cmake -S .\Source  --preset conan-debug

def AddEnvVarsWhereCl():
    cmdRunner = CommandRunner()
    vswhereRes = cmdRunner.Run([
        "c:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\\vswhere.exe", 
        "-legacy",  
        "-prerelease", 
        "-format", 
        "json"
    ])
    vswhereJson = json.loads(vswhereRes.stdout)
    vcvars64Path = os.path.join(vswhereJson[0]["installationPath"], "VC", "Auxiliary", "Build", "vcvars64.bat")

    vcvarsRes = cmdRunner.Run([vcvars64Path, "&&", "set", "."])
    pathVar = os.environ.get("PATH")
    # vcvarsRes = subprocess.run([vcvars64Path], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(vcvarsRes.stdout)
    print(vcvarsRes.stderr)
    afterpathVar = os.environ.get("PATH")
    print(pathVar)
    print(afterpathVar)



def PreparePreset():
    cmdRunner = CommandRunner()
    cmdRunner.Run(["cmake", "-S", ".\\Source", "--preset", "conan-debug"])

def BuildPreset():
    cmdRunner = CommandRunner()
    cmdRunner.Run(["cmake", "-S", ".\\Source", "--build", "conan-debug"])


def main():
    operatingSystem = GetOperatingSystem()
    if operatingSystem == "Windows":
        AddEnvVarsWhereCl()
    # PreparePreset()

if __name__ == "__main__":
    main()


