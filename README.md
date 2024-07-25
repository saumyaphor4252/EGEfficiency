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

# Working set-up for Run3Winter24 performance and studies

2024 samples
```
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/
cmsrel CMSSW_13_3_3
cd CMSSW_13_3_3/src
cmsenv
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/
cmsenv
hltGetConfiguration /dev/CMSSW_13_3_0/GRun/V22 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v21,HLT_Ele23_Ele12_CaloIdL
_TrackIdL_IsoVL_v25,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 133X_mcRun3_2024_realistic_v8 --max-events 50000
00 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Wint
er24Digi-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrig
ger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
cmsRun hlt.py
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test
vi run_EfficiencyCalculator.py # Update dir1 and GT accordingly
cmsRun run_EfficiencyCalculator.py

```
2023 samples
```
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/
cmsrel CMSSW_13_0_10
cd CMSSW_13_0_10/src
cmsenv
git cms-init
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6
cp /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/HLTrigger/Configuration/python/Tools/dasFileQuery.py HLTrigger/Configuration/python/Tools/dasFileQuery.py
hltGetConfiguration /dev/CMSSW_13_0_0/GRun/V140 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v19,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 130X_mcRun3_2023_realistic_postBPix_v2 --max-events 5000000 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixDRPremix-KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
cmsRun hlt.py
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_10/src/EGTools/TrigTools/test
vi run_EfficiencyCalculator.py # Update dir1 and GT accordingly
cmsRun run_EfficiencyCalculator.py

```
