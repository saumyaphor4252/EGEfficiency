#!/usr/bin/env python3

import os, sys, re, pprint, string, imp
from optparse import OptionParser
import FWCore.ParameterSet.Config as cms

import time
import datetime
import os
import sys

MYDIR=os.getcwd()

#get inputs
from optparse import OptionParser
parser=OptionParser()
parser.add_option("-n",dest="nPerJob",type="int",default=1,help="NUMBER of files processed per job",metavar="NUMBER")
parser.add_option("-q","--flavour",dest="jobFlavour",type="str",default="workday",help="job FLAVOUR",metavar="FLAVOUR")
parser.add_option("-p","--proxy",dest="proxyPath",type="str",default="noproxy",help="Proxy path")

opts, args = parser.parse_args()

help_text = '\n./cmsCondor.py <cfgFileName> <CMSSWrel> <remoteDir> -p <proxyPath> -n <nPerJob> -q <jobFlavour>'
help_text += '\n<cfgFileName> (mandatory) = name of your configuration file (e.g. hlt_config.py)'
help_text += '\n<CMSSWrel> (mandatory) = directory where the top of a CMSSW release is located'
help_text += '\n<remoteDir> (mandatory) = directory where the files will be transfered (e.g. on EOS)'
help_text += '\n<proxyPath> (optional) = location of your voms cms proxy. Note: keep your proxy in a private directory.'
help_text += '\n<nPerJob> (optional) = number of files processed per batch job (default=5)'
help_text += '\n<flavour> (optional) = job flavour (default=workday)\n'

cfgFileName = str(args[0])
cmsEnv = str(args[1])
remoteDir = str(args[2])

print ('config file = %s'%cfgFileName)
print ('CMSSWrel = %s'%cmsEnv)
print ('proxy = %s'%opts.proxyPath)
print ('remote directory = %s'%remoteDir)
# print 'job flavour = %s'%opts.jobFlavour

sub_total = open("sub_total.jobb","w")

# load cfg script
handle = open(cfgFileName, 'r')
cfo = imp.load_source("pycfg", cfgFileName, handle)
process = cfo.process
handle.close()

from list_cff import inputFiles
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(inputFiles)
)

from list_PU_cff import PUFiles
process.mix.input.fileNames = cms.untracked.vstring(PUFiles)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2023_realistic_postBPix_v2', '')
process.GlobalTag.toGet = cms.VPSet(
  cms.PSet(record = cms.string("EcalSimComponentShapeRcd"),
           tag = cms.string("EcalSimComponentShape_PhaseI"),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
          ),
  cms.PSet(record = cms.string("EcalTimeCalibConstantsRcd"),
           tag = cms.string("EcalTimeCalibConstants_mc"),
           label = cms.untracked.string('CC'),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
          ),
  cms.PSet(record = cms.string("EcalTimeOffsetConstantRcd"),
           tag = cms.string("EcalTimeOffsetConstant_cctiming_v01_mc"),
           label = cms.untracked.string('CC'),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
          ),
  cms.PSet(record = cms.string("HcalPFCutsRcd"),
           tag = cms.string("HcalPFCuts_2023_V1.0_mc"),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
          ),
  cms.PSet(record = cms.string("LHCInfoPerFillRcd"),
           tag = cms.string("LHCInfoPerFill_endFill_Run3_mc_v1"),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
          ),
  cms.PSet(record = cms.string("LHCInfoPerLSRcd"),
           tag = cms.string("LHCInfoPerLS_endFill_Run3_mc_v1"),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
          ),        
  cms.PSet(record = cms.string("HcalSiPMParametersRcd"),
           tag = cms.string("HcalSiPMParameters_2024_50fb_v1.0_mc"),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
          ),
  cms.PSet(record = cms.string("HcalPedestalsRcd"),
           tag = cms.string("HcalPedestals_2024_50fb_mc_effective"),
           label = cms.untracked.string('effective'),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
          ),
  cms.PSet(record = cms.string("HcalPedestalWidthsRcd"),
           tag = cms.string("HcalPedestalWidths_2024_50fb_mc_effective"),
           label = cms.untracked.string('effective'),
           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
          )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.RAWSIMoutput.fileName = "RAW-DIGI_Output.root"

# keep track of the original source
fullSource = process.source.clone()

nJobs = -1

try:
    process.source.fileNames
except:
    print ('No input file. Exiting.')
    sys.exit(2)
else:
    print ("Number of files in the source:",len(process.source.fileNames), ":")
    pprint.pprint(process.source.fileNames)
   
    nFiles = len(process.source.fileNames)
    nJobs = int(nFiles / opts.nPerJob)
    if (nJobs!=0 and (nFiles % opts.nPerJob) > 0) or nJobs==0:
        nJobs = nJobs + 1
      
    print ("number of jobs to be created: ", nJobs)
    

k=0
loop_mark = opts.nPerJob
#make job scripts
for i in range(0, nJobs):
    #print 'total: %d/%d  ;  %.1f %% processed '%(j,my_sum,(100*float(j)/float(my_sum)))

    jobDir = MYDIR+'/Jobs/Job_%s/'%str(i)
    os.system('mkdir -p %s'%jobDir)

    tmp_jobname="sub_%s.sh"%(str(i))
    tmp_job=open(jobDir+tmp_jobname,'w')
    tmp_job.write("#!/bin/sh\n")
    if opts.proxyPath != "noproxy":
        tmp_job.write("export X509_USER_PROXY=$1\n")
        tmp_job.write("voms-proxy-info -all\n")
        tmp_job.write("voms-proxy-info -all -file $1\n")
    #tmp_job.write("ulimit -v 7000000\n")
    tmp_job.write("cd $TMPDIR\n")
    tmp_job.write("mkdir Job_%s\n"%str(i))
    tmp_job.write("cd Job_%s\n"%str(i))
    tmp_job.write("cd %s\n"%(cmsEnv))
    tmp_job.write("eval `scramv1 runtime -sh`\n")
    tmp_job.write("cd -\n")
    tmp_job.write("cp -f %s* .\n"%(jobDir))
    tmp_job.write("cmsRun cmsDriver_conf.py\n")
    tmp_job.write("echo 'sending the file back'\n")
    tmp_job.write("cp RAW-DIGI_Output.root %s/RAW-DIGI_Output_%s.root\n"%(remoteDir, str(i)))
    tmp_job.write("rm RAW-DIGI_Output.root\n")
    tmp_job.close()
    os.system("chmod +x %s"%(jobDir+tmp_jobname))

    print ("preparing job number %s/%s"%(str(i), nJobs-1))

    iFileMin = i*opts.nPerJob
    iFileMax = (i+1)*opts.nPerJob
          
    process.source.fileNames = fullSource.fileNames[iFileMin:iFileMax]
          
    tmp_cfgFile = open(jobDir+'/cmsDriver_conf.py','w')
    tmp_cfgFile.write(process.dumpPython())
    tmp_cfgFile.close()
    

condor_str = "executable = $(filename)\n"
if opts.proxyPath != "noproxy":
    condor_str += "Proxy_path = %s\n"%opts.proxyPath
    condor_str += "arguments = $(Proxy_path) $Fp(filename) $(ClusterID) $(ProcId)\n"
else:
    condor_str += "arguments = $Fp(filename) $(ClusterID) $(ProcId)\n"
condor_str += "output = $Fp(filename)hlt.stdout\n"
condor_str += "error = $Fp(filename)hlt.stderr\n"
condor_str += "log = $Fp(filename)hlt.log\n"
condor_str += '+JobFlavour = "%s"\n'%opts.jobFlavour
condor_str += "queue filename matching ("+MYDIR+"/Jobs/Job_*/*.sh)"
condor_name = MYDIR+"/condor_cluster.sub"
condor_file = open(condor_name, "w")
condor_file.write(condor_str)
sub_total.write("condor_submit %s\n"%condor_name)
os.system("chmod +x sub_total.jobb")
