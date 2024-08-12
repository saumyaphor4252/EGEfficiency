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
Steam Twiki page: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SteamHLTRatesCalculation
Steam repo: https://github.com/sanuvarghese/SteamRatesEdmWorkflow/blob/master/Prod/cmsCondorData.py


# Working set-up for Run3Winter24 performance and studies
GT difference: https://cms-conddb.cern.ch/cmsDbBrowser/diff/Prod/gts/130X_mcRun3_2023_realistic_postBPix_v2/133X_mcRun3_2024_realistic_v8

2024 samples
```
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/
cmsrel CMSSW_13_3_3
cd CMSSW_13_3_3/src
cmsenv
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/
cmsenv
dasgoclient --query='file dataset=/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24Digi-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RAW | grep file.name,file.nevents' --limit 400 | awk '{sum += $2} END {print sum}'
vi HLTrigger/Configuration/python/Tools/dasFileQuery.py
cd EGTools/TrigTools/test
hltGetConfiguration /dev/CMSSW_13_3_0/GRun/V22 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v21,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v25,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 133X_mcRun3_2024_realistic_v8 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24Digi-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
#hltGetConfiguration /dev/CMSSW_13_3_0/GRun/V22 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v21,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v25,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 133X_mcRun3_2024_realistic_v8 --max-events 5000000 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24Digi-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
# 
cmsRun hlt.py
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test
vi run_EfficiencyCalculator.py # Update dir1 and GT accordingly
cmsRun run_EfficiencyCalculator.py

```
For Condor Submission
```
voms-proxy-init --valid 100:00
cp /tmp/x509up_u122184 /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
hltGetConfiguration /dev/CMSSW_13_3_0/GRun/V22 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v21,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v25,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 133X_mcRun3_2024_realistic_v8 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24Digi-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
edmConfigDump hlt.py > hlt_config.py
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
vi HLTrigger/Configuration/python/Tools/dasFileQuery.py # Check tor update the input files
hltGetConfiguration /dev/CMSSW_13_0_0/GRun/V140 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v19,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 130X_mcRun3_2023_realistic_postBPix_v2 --max-events 5000000 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixDRPremix-KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
cmsRun hlt.py
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_10/src/EGTools/TrigTools/test
vi run_EfficiencyCalculator.py # Update dir1 and GT accordingly
cmsRun run_EfficiencyCalculator.py

```

Submit the 2023 samples on condor
```
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_10/src
cmsenv
vi HLTrigger/Configuration/python/Tools/dasFileQuery.py # Check tor update the input files
cd EGTools/TrigTools/test
voms-proxy-init --valid 100:00
cp /tmp/x509up_u122184 /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
hltGetConfiguration /dev/CMSSW_13_0_0/GRun/V140 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v19,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 130X_mcRun3_2023_realistic_postBPix_v2 --max-events -1 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixDRPremix-KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
vi hlt.py # Check maxEvents, output.root file and input files fileNames
edmConfigDump hlt.py > hlt_config.py

./cmsCondorData.py /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_10/src/ /eos/user/s/ssaumya/EGammaHLT/Run3Winter/2023_Samples/ -n 1 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
./sub_total.jobb
```




Making Plots
```
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test
cmsenv
vi run_EfficiencyCalculator.py
## Check Global Tag
## Check dir1Name: It should be the output.root area
## Check fileList1: It should match the output file name
## Update TFileService name to output file name
cmsRun run_EfficiencyCalculator.py
# This will produce the root file in the area 
ls /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Modified_2024_06082024.root
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/CMSSW_13_0_10/src/cms-egamma-hlt/phase2/PlotHists
vi Inputs.py
# Update path for output plots directory: outPlotDir
# Update the 2024 file /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Modified_2024_06082024.root
# Comment out the filters


```


Final Commands to run on 5 million events


2024

```
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test
cmsenv
voms-proxy-init --valid 100:00
cp /tmp/x509up_u122184 /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
## Check how many files would be enough for your purpose
dasgoclient --query='file dataset=/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24Digi-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RAW | grep file.name,file.nevents' --limit 100
## Update the --limit argument with that file number :4000 for 3000000 events
vi ../../../HLTrigger/Configuration/python/Tools/dasFileQuery.py
# Also print the length of files to make sure it is being used
hltGetConfiguration /dev/CMSSW_13_0_0/GRun/V140 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v19,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 130X_mcRun3_2023_realistic_postBPix_v2 --max-events 5000000 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixDRPremix-KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
vi hlt.py
# Check maxEvents, fileNames, and output.root
edmConfigDump hlt.py > hlt_config.py
vi ./cmsCondorData.py
# Check hlt.root, nEvents or maxEvents and output folder will be determined by argument
# Check how many jobs should be submitted, output file
./cmsCondorData.py hlt_config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_14/src/ /eos/cms/store/group/phys_egamma/ssaumya/Run3Winter24/2023_Samples/3millionEvents/ -n 15 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
./sub_total.jobb
```


2023
```
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_14/src/EGTools/TrigTools/test
cmsenv
voms-proxy-init --valid 100:00
cp /tmp/x509up_u122184 /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
## Check how many files would be enough for your purpose
dasgoclient --query='file dataset=/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixDRPremix-KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/GEN-SIM-RAW | grep file.name,file.nevents' --limit 100
## Update the --limit argument with that file number :4000 for 3000000 events
vi ../../../HLTrigger/Configuration/python/Tools/dasFileQuery.py
# Also print the length of files to make sure it is being used
hltGetConfiguration /dev/CMSSW_13_3_0/GRun/V22 --path HLTriggerFirstPath,HLT_Ele32_WPTight_Gsf_v21,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v25,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 133X_mcRun3_2024_realistic_v8 --max-events 5000000 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24Digi-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
# Check maxEvents, fileNames, and output.root
edmConfigDump hlt.py > hlt_config.py
vi ./cmsCondorData.py
# Check hlt.root, nEvents or maxEvents and output folder will be determined by argument
# Check how many jobs should be submitted, output file
./cmsCondorData.py hlt_config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/ /eos/cms/store/group/phys_egamma/ssaumya/Run3Winter24/2024_Samples/3millionEvents/ -n 20 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
./sub_total.jobb
```


Drivers for testing new samples 
Drivers for GEN-SIM-RAW: https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_setup/TSG-Run3Winter24Digi-00001

```
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/Test_Samples/
cmsrel CMSSW_13_3_0
cd CMSSW_13_3_0/src
cmsenv
voms-proxy-init --valid 100:00
cp /tmp/x509up_u122184 /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
#cmsDriver.py  --python_filename TSG-Run3Winter24Digi-00001_1_cfg.py --eventcontent RAWSIM --pileup 2023_LHC_Simulation_12p5h_9h_hybrid2p23 --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --fileout file:TSG-Run3Winter24Digi-00001.root --pileup_input "dbs:/MinBias_TuneCP5_13p6TeV-pythia8/Run3Winter24GS-133X_mcRun3_2024_realistic_v7-v1/GEN-SIM" --conditions 133X_mcRun3_2024_realistic_v8 --customise_commands "process.RAWSIMoutput.outputCommands.extend(['keep *_simSiStripDigis*_*_*', 'keep *_simSiPixelDigis*_*_*'])" --step DIGI,L1,DIGI2RAW,HLT:2023v12 --geometry DB:Extended --filein "dbs:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24GS-133X_mcRun3_2024_realistic_v7-v1/GEN-SIM" --era Run3_2023 --no_exec --mc -n 10

cmsDriver.py --filein file:/eos/cms/store/mc/Run3Winter24GS/MinBias_TuneCP5_13p6TeV-pythia8/GEN-SIM/133X_mcRun3_2024_realistic_v7-v1/60001/4c97601b-ad3e-449a-b556-b4b72fa4a084.root --fileout file:your_output_file.root --mc --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions 130X_mcRun3_2023_realistic_postBPix_v2 --step DIGI,L1,DIGI2RAW,HLT:2023v12 --geometry DB:Extended --era Run3_2023 --nThreads 4 --python_filename Test1.py -n 10 --pileup 2023_LHC_Simulation_12p5h_9h_hybrid2p23 --pileup_input "dbs:/MinBias_TuneCP5_13p6TeV-pythia8/Run3Winter24GS-133X_mcRun3_2024_realistic_v7-v1/GEN-SIM" --no exec
#Update the Test1.py as needed
cmsRun Test1.py

```


