import FWCore.ParameterSet.Config as cms
import glob
import os

process = cms.Process("USER")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '133X_mcRun3_2024_realistic_v8') 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

dir1Name = "/eos/cms/store/group/phys_egamma/ssaumya/Run3Winter24/2024_Samples/16102024/"

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

#Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string("Efficiency_Calculator_2024_16102024_32WP.root")
)

process.EfficiencyCalculator = cms.EDAnalyzer('EfficiencyCalculator',
                                              stageL1Trigger = cms.uint32(2)
)

process.p = cms.Path(process.EfficiencyCalculator)
process.schedule = cms.Schedule(process.p)
