import subprocess
import sys
import re
from colorama import init, Fore

# Initialize colorama
init()

# Set the URL for redirection
redirect_url = "https://github.com/TejasLamba2006"

# Print colored text with redirection URL
print(Fore.MAGENTA + "Made by " + Fore.BLUE + "visa2code")
print(Fore.YELLOW + f"Click here to visit my GitHub profile: {redirect_url}")

command = ['node', '--version']

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
stdout, _ = process.communicate()

node_version = stdout.decode('utf-8').strip()

match = re.match(r"v(\d+)", node_version)
if match:
    node_major_version = int(match.group(1))
else:
    print(Fore.RED + "Error: Failed to extract Node.js version.")
    sys.exit(1)

if node_major_version < 18:
    print(Fore.RED + "Error: Node.js version 18 or higher is required to run this script.")
    sys.exit(1)

print(Fore.GREEN + "Starting Nuke Bot...")
command_run = ['node', 'Zero-Tool/nuke-bot/index.js']
process = subprocess.Popen(command_run, shell=False)
process.communicate()
