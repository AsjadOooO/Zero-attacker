import subprocess
import sys
import re

command = ['node', '--version']


process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
stdout, _ = process.communicate()


node_version = stdout.decode('utf-8').strip()

match = re.match(r"v(\d+)", node_version)
if match:
    node_major_version = int(match.group(1))
else:
    print("Error: Failed to extract Node.js version.")
    sys.exit(1)

if node_major_version < 18:
    print("Error: Node.js version 18 or higher is required to run this script.")
    sys.exit(1)

command = ['node', 'index.js']
print("Running command: " + ' '.join(command))
process = subprocess.Popen(command, shell=False)
process.communicate()
#made by visa2code By Zero-Security