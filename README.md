# EGEfficiency

To set up the repository:
```
cmsrel CMSSW_14_0_9
cd CMSSW_14_0_9/src
cmsenv
voms-proxy-init --voms cms
cp /tmp/x509up_u122184 /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
git cms-init
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6
git clone git@github.com:RSalvatico/EGEfficiency.git EGTools
# Update HLTrigger/Configuration/python/Tools/dasFileQuery.py
vi HLTrigger/Configuration/python/Tools/dasFileQuery.py
scram b -j 10
cd EGTools/TrigTools/test

### Reference
# /RelValZEE_14/CMSSW_14_0_9-PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/GEN-SIM-DIGI-RAW
hltGetConfiguration /dev/CMSSW_14_0_0/GRun/V156 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v7,HLT_Ele32_WPTight_Gsf_v21,HLT_Ele115_CaloIdVT_GsfTrkIdT_v21,HLT_Ele135_CaloIdVT_GsfTrkIdT_v14,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v25,HLT_DoubleEle33_CaloIdL_MW_v24,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 140X_mcRun3_2024_realistic_v14 --max-events -1 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2024_v1_2_0_xml --input dataset:/RelValZEE_14/CMSSW_14_0_9-PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/GEN-SIM-DIGI-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
vi hlt.py # Check maxEvents, output.root file and input files fileNames
edmConfigDump hlt.py > hlt_config_Reference.py
./cmsCondorData.py hlt_config_Reference.py /afs/cern.ch/work/s/ssaumya/private/Egamma/TrackerStudies/CMSSW_14_0_9/src/ /eos/user/s/ssaumya/EGammaHLT/Run3Winter/TrackerStudies/Reference -n 15 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_<XYZ>
./sub_total.jobb

### Scenario 1
# /RelValZEE_14/CMSSW_14_0_9-PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/GEN-SIM-DIGI-RAW
hltGetConfiguration /dev/CMSSW_14_0_0/GRun/V156 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v7,HLT_Ele32_WPTight_Gsf_v21,HLT_Ele115_CaloIdVT_GsfTrkIdT_v21,HLT_Ele135_CaloIdVT_GsfTrkIdT_v14,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v25,HLT_DoubleEle33_CaloIdL_MW_v24,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 140X_mcRun3_2024_realistic_EOR3_TkDPGv2 --max-events -1 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2024_v1_2_0_xml --input dataset:/RelValZEE_14/CMSSW_14_0_9-PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/GEN-SIM-DIGI-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt1.py
edmConfigDump hlt.py > hlt_config_EOR3_v1.py
./cmsCondorData.py hlt_config_EOR3_v1.py /afs/cern.ch/work/s/ssaumya/private/Egamma/TrackerStudies/CMSSW_14_0_9/src/ /eos/user/s/ssaumya/EGammaHLT/Run3Winter/TrackerStudies/EOR31 -n 15 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
./sub_total.jobb

### Scenario 2
# /RelValZEE_14/CMSSW_14_0_9-PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv6_RV245_2024-v1/GEN-SIM-DIGI-RAW
hltGetConfiguration /dev/CMSSW_14_0_0/GRun/V156 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v7,HLT_Ele32_WPTight_Gsf_v21,HLT_Ele115_CaloIdVT_GsfTrkIdT_v21,HLT_Ele135_CaloIdVT_GsfTrkIdT_v14,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v25,HLT_DoubleEle33_CaloIdL_MW_v24,HLTriggerFinalPath --output minimal --mc --process HLTX --type GRun --globaltag 140X_mcRun3_2024_realistic_EOR3_TkDPGv6 --max-events -1 --unprescale --eras Run3 --l1-emulator FullMC --l1 L1Menu_Collisions2024_v1_2_0_xml --input dataset:/RelValZEE_14/CMSSW_14_0_9-PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv6_RV245_2024-v1/GEN-SIM-DIGI-RAW --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt2.py
edmConfigDump hlt.py > hlt_config_EOR3_v2.py
./cmsCondorData.py hlt_config_EOR3_v2.py /afs/cern.ch/work/s/ssaumya/private/Egamma/TrackerStudies/CMSSW_14_0_9/src/ /eos/user/s/ssaumya/EGammaHLT/Run3Winter/TrackerStudies/EOR32 -n 15 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
./sub_total.jobb

# For the desired path, update the path in plugins/EfficiencyCalculator.cc

# Update the GT, dirName for hlt.root files and the outputfile name in test/runEfficiency_Calculator.py
# process.GlobalTag = GlobalTag(process.GlobalTag, '140X_mcRun3_2024_realistic_EOR3_TkDPGv2')
# dir1Name = "/eos/user/s/ssaumya/EGammaHLT/Run3Winter/TrackerStudies/EOR3_v1/"
# fileName = cms.string("Efficiency_Calculator_2024_Tracker_EOR3_Studies_Reference.root")

cmsRun EfficiencyCalculator.py
```
