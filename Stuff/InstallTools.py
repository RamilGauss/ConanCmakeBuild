from CommandRunner import  CommandRunner
from ToolConfig import GetToolInfoList
from SystemInfo import GetOperatingSystem

def InstallTools():
    operatingSystem = GetOperatingSystem()
    tools = GetToolInfoList()

    for tool in tools:
        if tool.operatingSystem == "any" or tool.operatingSystem == operatingSystem:
            cmdRunner = CommandRunner()
            result = cmdRunner.Run(tool.commands)
            if result.returncode != 0 and result.stderr is not None:
                msgLen = len(result.stderr)
                halfLen = int(msgLen / 2)
                print(result.stderr[0:halfLen])
                print(result.stderr[halfLen:len(result.stderr)])
            else:
                print(f"{tool.name} - OK")


def main():
    InstallTools()

if __name__ == "__main__":
    main()
