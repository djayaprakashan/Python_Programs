#Introducing System Administration with Python
import os
import subprocess
#os.system("ls")
#sys-admin.py README.md
subprocess.run(["ls"]) # with one argument
subprocess.run(["ls","-l"]) # with two argument
subprocess.run(["ls","-l","README.md"]) # with three argument
os.system("cat README.md")
#subprocess.run(["cat README.MD"])

command="uname"
commandArgument="-a"
print(f'\nGathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'\nGathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])