import platform
import subprocess

def GetOperatingSystem() -> str:
    return platform.system()

def GetInstalledCompiler() -> str:

    # msvc
    if 0:
        result = subprocess.run(["cl", "--version"], capture_output=True, text=True, encoding='utf-8', errors='replace')
    # clang
    # gcc

    return None

