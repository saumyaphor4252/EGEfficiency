# EGEfficiency
```
cmsrel CMSSW_13_0_10
cd CMSSW_13_0_10/src
cmsenv
voms-proxy-init --voms cms
cp /tmp/x509up_<XYZ> /afs/cern.ch/user/s/ssaumya/private/x509up_<XYZ>
git cms-init
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6
git clone git@github.com:RSalvatico/EGEfficiency.git EGTools
# Update HLTrigger/Configuration/python/Tools/dasFileQuery.py
# dasgoclient --query='file dataset=/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixDRPremix-KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/GEN-SIM-RAW  | grep file.name,file.nevents' --limit 400 | awk '{sum += $2} END {print sum}'
# Every file has 4000 events: We need 4mill events, so we need 1000 files.
vi HLTrigger/Configuration/python/Tools/dasFileQuery.py
scram b -j 10
cd EGTools/TrigTools/test
hltGetConfiguration /dev/CMSSW_13_0_0/GRun/V140 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v5,HLT_Ele32_WPTight_Gsf_v19,HLT_Ele115_CaloIdVT_GsfTrkIdT_v19,HLT_Ele135_CaloIdVT_GsfTrkIdT_v12,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23,HLT_DoubleEle33_CaloIdL_MW_v22,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 130X_mcRun3_2023_realistic_postBPix_v2 --max-events 4000000 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2023_v1_2_0_xml --input dataset:/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixDRPremix-KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/GEN-SIM-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
edmConfigDump hlt.py > hlt_config.py
./cmsCondorData.py /afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/NEW/2023_Samples/CMSSW_13_0_14/src/ /eos/cms/store/group/phys_egamma/ssaumya/Run3Winter24/2023_Samples/16102024 -n 1 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_<XYZ>
./sub_total.jobb
```


