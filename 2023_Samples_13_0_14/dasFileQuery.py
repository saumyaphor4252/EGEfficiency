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
             ['dasgoclient', '--query', query, '--format', 'json'], # , '--limit', '100'],
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
    jsondict = run_dasgoclient(query_file)
    
    for data in jsondict['data']:
        for file in data['file']:
            files.append(file['name'])
    #print("Files printing..")        
    #print(files)

    dir = "/eos/cms/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/"
    li2 = []
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(dir)):
        for x in filenames:
            dirpath = dirpath.replace("/eos/cms","")
            li2.append(os.path.join(dirpath,x))

    #print(len(li2))
    Unaccessible = set(files)-set(li2)
    #print("Unaccessible: {}".format(len(Unaccessible)))
    accessible = list(set(files).intersection(set(li2)))
    #print("Accessible: {}".format(len(accessible)))
    #print(accessible)
    return accessible [:1000]

#dasFileQuery("/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixDRPremix-KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/GEN-SIM-RAW")
