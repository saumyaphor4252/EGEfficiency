import FWCore.ParameterSet.Config as cms
import glob
import os

process = cms.Process("USER")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_dataRun3_Prompt_v3') 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(200) )

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
#                                    '/store/data/Run2024G/EGamma0/MINIAOD/PromptReco-v1/000/383/811/00000/67aaee8b-778c-457f-b844-f59f268c99af.root'
#                                    'file:output.root'
                                     'file:/eos/cms/store/group/phys_egamma/ssaumya/DeepDive/HLTstep_RECO_RootFiles_Reference/stepHLT_RECO_155.root'
                )
                            )
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

#Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string("Efficiency_Modified.root")
)

process.EfficiencyCalculator = cms.EDAnalyzer('EfficiencyCalculator',
)

process.p = cms.Path(process.EfficiencyCalculator)
process.schedule = cms.Schedule(process.p)
