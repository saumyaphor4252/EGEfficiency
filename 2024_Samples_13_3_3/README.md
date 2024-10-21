# EGEfficiency

```
cmsrel CMSSW_13_3_3
cd CMSSW_13_3_3/src
cmsenv
voms-proxy-init --voms cms
cp /tmp/x509up_<XYZ> /afs/cern.ch/user/s/ssaumya/private/x509up_<XYZ>
git cms-init
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6
git clone git@github.com:RSalvatico/EGEfficiency.git EGTools
# Update HLTrigger/Configuration/python/Tools/dasFileQuery.py
# dasgoclient --query='file dataset=/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixDRPremix-KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/GEN-SIM-RAW  | grep file.name,file.nevents' --limit 400 | awk '{sum += $2} END {print sum}'
vi HLTrigger/Configuration/python/Tools/dasFileQuery.py
scram b -j 10
cd EGTools/TrigTools/test
hltGetConfiguration /dev/CMSSW_13_3_0/GRun/V22 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v7,HLT_Ele32_WPTight_Gsf_v21,HLT_Ele115_CaloIdVT_GsfTrkIdT_v21,HLT_Ele135_CaloIdVT_GsfTrkIdT_v14,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v25,HLT_DoubleEle33_CaloIdL_MW_v24,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 133X_mcRun3_2024_realistic_v8 --max-events 4000000 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Winter24Digi-KeepSi_133X_mcRun3_2024_realistic_v8-v2/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
vi hlt.py # Check maxEvents, output.root file and input files fileNames
edmConfigDump hlt.py > hlt_config.py
vi ./cmsCondorData.py
# Check hlt.root, nEvents or maxEvents and output folder will be determined by argument
# Check how many jobs should be submitted, output file
./cmsCondorData.py hlt_config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/NEW/2024_Samples/CMSSW_13_3_3/src/ /eos/cms/store/group/phys_egamma/ssaumya/Run3Winter24/2024_Samples/16102024 -n 11 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_<XYZ>
# Submitted on 5500 files to meet the 4mil needs. So files per job = 11 --> 500 jobs
./sub_total.jobb
```
