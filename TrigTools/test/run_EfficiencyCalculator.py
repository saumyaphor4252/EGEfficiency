import FWCore.ParameterSet.Config as cms
import glob
import os

process = cms.Process("USER")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_dataRun3_Prompt_v3') 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# Input file source
# dir1Name = "/afs/cern.ch/user/r/rselvati/work/private/testBPIX/CMSSW_13_0_10/src/SteamRatesEdmWorkflow/Prod/hltModified/"
# fileList1 = filter(os.path.isfile, glob.glob(dir1Name + "*.root"))
# fList = []
# for f in fileList1:
#      fs = str(f).replace("/afs/","file:/afs/")
#      fList.append(fs)
# print(fList)
#from list_relval import fileList
process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring(#fList
#                                    'root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver2-v1/80000/FEAB7D8A-048C-E811-A513-AC1F6B1AEFFC.root'
                                    'file:output.root'
                )
                            )
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

#Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string("Efficiency_Modified.root")
)

process.EfficiencyCalculator = cms.EDAnalyzer('EfficiencyCalculator',
                                              stageL1Trigger = cms.uint32(2)
)

process.p = cms.Path(process.EfficiencyCalculator)
process.schedule = cms.Schedule(process.p)
