import subprocess

# Your DAS query
#query = "file dataset= /DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24GS-133X_mcRun3_2024_realistic_v7-v2/GEN-SIM"
query = "file dataset= /MinBias_TuneCP5_13p6TeV-pythia8/Run3Winter24GS-133X_mcRun3_2024_realistic_v7-v1/GEN-SIM"

# Execute the dasgoclient command
#command = f"dasgoclient -query='{query}' --limit 100" # For inputFiles only
command = f"dasgoclient -query='{query}'"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Convert the output to a list
output = result.stdout.decode('utf-8').splitlines()

# Error handling
if result.returncode != 0:
    print(f"Error: {result.stderr.decode('utf-8')}")
else:
    # Now 'output' is a Python list with the result from dasgoclient
    print("DAS Output as List:", output)

cff_content = "PUFiles = ["
#cff_content = "inputFiles = ["

for dataset in output:
    cff_content += f"'{dataset}',\n"

# Close the list and the script
cff_content += "]\n"

with open('list_PU_cff.py', 'w') as file:
    file.write(cff_content)

print("CFF file 'list_PU_cff.py' has been created.")
