# import subprocess

# def runMultipleCommands(str1):
#     # Combine commands into a single string
#     command = f"""
#     cd build && 
#     pwd &&
#     echo {str1}
#     """
#     subprocess.run(command, shell=True)

# if __name__ == '__main__':
#     runMultipleCommands('ffff')
#     str1 = 'Hello'
#     runMultipleCommands(str1)

import subprocess

def runCommands(commands):
    for command in commands:
        if command.startswith('cd '):
            path = command.split(' ')[1]
        else:
            subprocess.Popen(command, shell=True, cwd=path)

if __name__ == '__main__':
    commands = ['cd build', 'pwd', 'echo ffff', 'echo Hello']
    runCommands(commands)
    commands = ['cd build', 'ls', 'pwd', 'echo farshid', 'echo Hello', 'touch f.txt']
    runCommands(commands)