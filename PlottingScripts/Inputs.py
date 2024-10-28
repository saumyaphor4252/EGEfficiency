i
port sys
import ROOT
sys.dont_write_bytecode = True
eosDir  ="/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/NEW/GitHub/EGEfficiency/PlottingScripts/"

def getFilters(cmsPath):
    filts = []
    for fil in cmsPath.split(",")[0].split("+"):
        if "Filter" in fil:
            filts.append(fil.replace("process.", ""))
    return filts

#---------------
# Plotting 
#---------------
outPlotDir  = "%s/%s"%(eosDir, "plots")

# For plotting efficiency
forOverlay = {}
forOverlay["2023postBPix"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/NEW/2023_Samples/CMSSW_13_0_14/src/EGTools/TrigTools/test/Efficiency_Calculator_2023_16102024_32WP.root")
forOverlay["Winter2024"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/NEW/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Calculator_2024_16102024_32WP.root")
forOverlay["Winter24-HcalSiPM"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/NEW/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Calculator_2024_HcalSiPM_32WP.root")
#forOverlay["Run3Winter2024"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/400000Events/Efficiency_Modified_2024_07082024.root")

# For efficiency by Filters
#forOverlay["No Change 133X"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_NoChange.root")
#forOverlay["HcalSiPM"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_HcalSiPM.root")
#forOverlay["HcalZS"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_HcalZS.root")
#forOverlay["HcalResponseCorrs"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_HcalResponse.root")
#forOverlay["HcalSiPM"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_HcalSiPM.root")

forRatio = []
forRatio.append(["Winter2024", "2023postBPix"])
