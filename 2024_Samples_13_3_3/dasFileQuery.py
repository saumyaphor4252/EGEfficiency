import sys
import json
import subprocess
import os
import os.path
import itertools

def dasFileQuery(dataset):
    """Return files for given DAS query via dasgoclient"""

    def run_dasgoclient(query):
        result = subprocess.run(
             ['dasgoclient', '--query', query, '--format', 'json'],# , '--limit', '400'],
             stdout=subprocess.PIPE, 
             stderr=subprocess.PIPE,
             text=True
             )
#        print("Return code:", result.returncode)
#        print("Output:", result.stdout)
#        print("Error:", result.stderr)

        if result.returncode != 0:
            sys.stderr.write(f"Error executing dasgoclient: {result.stderr}\n")
            sys.exit(1)
        return json.loads(result.stdout)

    files = []
    query_file = f'file dataset={dataset}'
    print("Print f query...")
    jsondict = run_dasgoclient(query_file)

    for data in jsondict['data']:
        for file in data['file']:
            files.append(file['name'])

    dir = "/eos/cms/store/mc/Run3Winter24Digi/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_133X_mcRun3_2024_realistic_v8-v2/"

    li2 = []
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(dir)):
        for x in filenames:
            dirpath = dirpath.replace("/eos/cms","")
            li2.append(os.path.join(dirpath,x))

    #Unaccessible = set(files)-set(li2)
    accessible = list(set(files).intersection(set(li2)))
    print(len(accessible))
    return accessible[:5500]

dasFileQuery("/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24Digi-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RAW")
