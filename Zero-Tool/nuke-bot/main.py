import subprocess
import sys
import re

# Check Node.js version
node_version = subprocess.run(['node', '--version'], capture_output=True, text=True).stdout.strip()
match = re.match(r"v(\d+)", node_version)
if match:
    node_major_version = int(match.group(1))
else:
    print("Error: Failed to extract Node.js version.")
    sys.exit(1)

if node_major_version < 18:
    print("Error: Node.js version 18 or higher is required to run this script.")
    sys.exit(1)

# Install npm modules
subprocess.run(['npm', 'install'], check=True)

# Run the Node.js script
command = ['node', 'index.js']
print(f"Running command: {' '.join(command)}")
subprocess.run(command, check=True)
