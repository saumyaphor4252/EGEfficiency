import FWCore.ParameterSet.Config as cms
import glob
import os

process = cms.Process("USER")

reRunL1 = False

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
from Configuration.AlCa.GlobalTag import GlobalTag

#process.GlobalTag = GlobalTag(process.GlobalTag, '140X_mcRun3_2024_realistic_v14') 
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_mcRun3_2024_realistic_EOR3_TkDPGv2')
#process.GlobalTag = GlobalTag(process.GlobalTag, '140X_mcRun3_2024_realistic_EOR3_TkDPGv6')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# Input Files
#dir1Name = "/eos/user/s/ssaumya/EGammaHLT/Run3Winter/TrackerStudies/Reference/"
dir1Name = "/eos/user/s/ssaumya/EGammaHLT/Run3Winter/TrackerStudies/EOR3_v1/"
#dir1Name = "/eos/user/s/ssaumya/EGammaHLT/Run3Winter/TrackerStudies/EOR3_v2"

fileList1 = filter(os.path.isfile, glob.glob(dir1Name + "*.root"))
fList = []
for f in fileList1:
    fs = str(f).replace("/eos/","file:/eos/")
    fList.append(fs)
print(fList)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(fList
    #'root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver2-v1/80000/FEAB7D8A-048C-E811-A513-AC1F6B1AEFFC.root'
    )
)

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

# Output file
process.TFileService = cms.Service("TFileService",
#    fileName = cms.string("Efficiency_Calculator_2024_Tracker_EOR3_Studies_Reference.root")
    fileName = cms.string("Efficiency_Calculator_2024_Tracker_EOR3_Studies_Target_v1.root")
#    fileName = cms.string("Efficiency_Calculator_2024_Tracker_EOR3_Studies_Target_v2.root")
)

process.EfficiencyCalculator = cms.EDAnalyzer('EfficiencyCalculator',
    stageL1Trigger = cms.uint32(2)
)

if reRunL1:
    process.myTask = cms.Task(process.GlobalParametersRcdSource,process.GlobalParameters,process.hltGtStage2Digis,process.hltGtStage2ObjectMap)
    process.t = cms.Path(process.myTask)
    #process.p = cms.Path(process.hltL1sSingleEGor + process.EfficiencyCalculator)
    #process.p = cms.Path(process.hltL1sSingleAndDoubleEG + process.EfficiencyCalculator)
    #process.p = cms.Path(process.hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau + process.EfficiencyCalculator)
    #process.p = cms.Path(process.hltL1sSingleEGNonIsoOrWithJetAndTau + process.EfficiencyCalculator)
    process.p = cms.Path(process.hltL1sSingleEG40to50 + process.EfficiencyCalculator)
    process.schedule = cms.Schedule(process.t,process.p)
else:
    process.p = cms.Path(process.EfficiencyCalculator)
    process.schedule = cms.Schedule(process.p)
