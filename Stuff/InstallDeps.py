import os
import subprocess
import shutil
from string import Template

from DependencyConfig import GetDependencyInfoList
from SystemInfo import GetOperatingSystem
import ProfileInfo

def RecreateTempDir(tempFolderAbsPath):
    tempDir = tempFolderAbsPath
    if os.path.isdir(tempDir):
        shutil.rmtree(tempDir)
    os.mkdir(tempDir)

def DetectProfile(profileAbsPath):
    os.environ["CONAN_HOME"] = profileAbsPath
    os.environ["CONAN_USER_HOME"] = profileAbsPath

    cmd = ["conan", "profile", "detect"]
    subprocess.run(cmd, stdout=subprocess.PIPE)

def GenerateProfile():
    operatingSystem = GetOperatingSystem()
    buildType = "Debug"

    varDict = {
        "operatingSystem": operatingSystem,
        "buildType": buildType
    }

    profileContent = Template(ProfileInfo.template).safe_substitute(varDict)

    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    fileNamePath = os.path.join(currentDirectory, ProfileInfo.fileName)
    with open(fileNamePath, 'w') as file:
        file.write(profileContent)

def InstallDeps():
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    fileNamePath = os.path.join(currentDirectory, ProfileInfo.fileName)

    buildPath = os.path.join(currentDirectory, "build")

    deps = GetDependencyInfoList()

    for dep in deps:
        command = [
            "conan",
            "install",
            f"-of={buildPath}",
            "-b=missing",
            f"-pr:h={fileNamePath}",
            f"-pr:b={fileNamePath}",
            f"--requires={dep.name}/{dep.version}",
            "-g", "CMakeDeps",
            "-g", "CMakeToolchain"
        ]
        if len(dep.options) > 0:
            command.append("-o")
            command.append(dep.options[0])
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
        if result.returncode != 0 and result.stderr is not None:
            msgLen = len(result.stderr)
            halfLen = int(msgLen / 2)
            print(result.stderr[0:halfLen])
            print(result.stderr[halfLen:len(result.stderr)])
        else:
            print(f"{dep.name}/{dep.version} - OK")


def main():
    tempFolderAbsPath = "C:\\Temp"
    RecreateTempDir(tempFolderAbsPath)
    DetectProfile(f"{tempFolderAbsPath}\\conan2")
    GenerateProfile()
    InstallDeps()

if __name__ == "__main__":
    main()
