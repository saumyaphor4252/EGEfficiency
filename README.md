# EGEfficiency

To set up the repository:
```
cmsrel CMSSW_13_0_10
cd CMSSW_13_0_10/src
cmsenv
voms-proxy-init --voms cms
git cms-init
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6
git clone git@github.com:RSalvatico/EGEfficiency.git EGTools
scram b -j 4
```

Running a trigger on raw files and measuring its efficiency is a two-steps process. First, you have to dump the desired trigger configuration and run it, taking care of saving all the needed collections for further analysis. Second, you can run on the results of the first part and calculate efficiencies, occupancies, etc.

An example of `hltGetConfiguration` that can be used for this:
```
hltGetConfiguration /dev/CMSSW_13_0_0/GRun/V140 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v19,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 131X_mcRun3_2023_realistic_forEGamma_v1 --max-events -1 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2022_v1_3_0-d1_xml --input /store/relval/CMSSW_13_0_11/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_131X_mcRun3_2023_realistic_forEGamma_v1_RV209-v2/2580000/9f41598a-a01c-4a6c-9126-aedeb18eefe1.root --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
```

In the `TrigTools/test` directory of this repo there is already one of such files, called `hlt_standard.py`. This can be modified according to the needs.

In order to run this script on several input files on HT Condor, one can do
```
./cmsCondorData.py hlt_standard.py #path_to_your_src #path_to_output_folder -n 1 -q workday -p #path_to_your_grid_proxy (for example mine is /afs/cern.ch/user/r/rselvati/private/x509up)
``` 
You can check whether one job would run fine locally by doing
```
./Jobs/Job_0/sub_0.sh
```
and, if everything looks good, launch the Condor jobs via
```
./sub_total.jobb
```
The list of input files has to be specified in `cmsCondorData.py` (not that, at present, things are a bit hardcoded there...).

Once you have all the output files you need, you can run the `EfficiencyCalculator` analyzer from the `TrigTools/test` directory:
```
cmsRun run_EfficiencyCalculator.py
```
The path to the list of input files has to be specified from within that python config.