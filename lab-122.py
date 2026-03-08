# Use os.system() to run a Bash command
# Use subprocess.run() to run Bash commands
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None,
# timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

import platform
import os
import subprocess

# linux
# os.system("ls")

# windows
os.system("dir")
subprocess.run(["dir"], shell=True)
subprocess.run(["cmd", "/c", "dir"])
result = subprocess.run(["git", "status"])
print(result.returncode)


commandArgument = "-x"

if platform.system() == "Windows":
    command = ["tasklist"]
else:
    command = ["ps", commandArgument]

print(f"Gathering active process information with command: {command} {commandArgument}")
subprocess.run(command)
