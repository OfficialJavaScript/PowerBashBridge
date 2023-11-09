import os, platform

exit = ['exit', 'exit()', 'close', 'stop', 'end']
userinput = ""

def command():
    os.system(clear_command)
    while True:
        try:
            userinput = input("PyPrompt # ")
            if userinput.lower() in exit:
                break
            os.system(f'{userinput}')
        except EOFError:
            break
system = platform.system().lower()
if system == "windows":
    clear_command = 'cls'
    prompt = f"powershell.exe {userinput}"
    
if system == "linux":
    clear_command = 'clear'
    prompt = f"{userinput}"

command()