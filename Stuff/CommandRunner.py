import subprocess

class CommandRunner:
    def Run(self, commands):
        return subprocess.run(commands, capture_output=True, text=True, encoding='utf-8', errors='replace')