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

    #dir = "/eos/cms/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1"
    dir = "/eos/cms/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4"
    #dir = "/eos/cms/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv6_RV245_2024-v1"
    li2 = []
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(dir)):
        for x in filenames:
            dirpath = dirpath.replace("/eos/cms","")
            li2.append(os.path.join(dirpath,x))

    #print(len(li2))
    Unaccessible = set(files)-set(li2)
    print("Unaccessible: {}".format(len(Unaccessible)))
    accessible = list(set(files).intersection(set(li2)))
    print("Accessible: {}".format(len(accessible)))
    print(len(accessible))
    return accessible

#dasFileQuery("/RelValZEE_14/CMSSW_14_0_9-PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/GEN-SIM-DIGI-RAW")
dasFileQuery("/RelValZEE_14/CMSSW_14_0_9-PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/GEN-SIM-DIGI-RAW")
#dasFileQuery("/RelValZEE_14/CMSSW_14_0_9-PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv6_RV245_2024-v1/GEN-SIM-DIGI-RAW")
