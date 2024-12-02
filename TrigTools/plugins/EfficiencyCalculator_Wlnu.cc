#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/EgammaObject.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "CondFormats/DataRecord/interface/L1TGlobalParametersRcd.h"
#include "DataFormats/HLTReco/interface/TriggerFilterObjectWithRefs.h"
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"

#include <vector>
#include <string>
#include <iostream>
#include <TH1F.h>
#include <TH2D.h>
#include <TFile.h>
#include <TLorentzVector.h>
#include <TTree.h>
#include "Math/VectorUtil.h"
#include <stdlib.h>

#define TWOPI 6.283185308

class EfficiencyCalculator : public edm::one::EDAnalyzer<edm::one::WatchRuns> {
 
private:
  
  std::string hltProcess_; // Name of HLT process, usually "HLT", but when customized: "HLTX" or "MYHLT"
  edm::EDGetTokenT<std::vector<pat::Electron> > eleToken_;
  edm::EDGetTokenT<std::vector<pat::MET> > metToken_;
  edm::EDGetTokenT<edm::TriggerResults > hltToken_;
  edm::EDGetTokenT<std::vector<pat::TriggerObjectStandAlone> > triggerObjectsToken_;

  edm::Service<TFileService> fs;
  double endcap_end_ = 2.5;

  TH1D* num_ele_pt_EB1;
  TH1D* num_ele_pt_EB2;
  TH1D* num_ele_pt_EE1;
  TH1D* num_ele_pt_EE2;
  TH1D* num_ele_pt_EB;
  TH1D* num_ele_pt_EE;
  TH1D* num_ele_pt;
  TH1D* num_ele_eta;
  TH1D* num_ele_phi;

  TH1D* den_ele_pt_EB1;
  TH1D* den_ele_pt_EB2;
  TH1D* den_ele_pt_EE1;
  TH1D* den_ele_pt_EE2;
  TH1D* den_ele_pt_EB;
  TH1D* den_ele_pt_EE;
  TH1D* den_ele_pt;
  TH1D* den_ele_eta;
  TH1D* den_ele_phi;

  float barrel_end_ = 1.4442;
  TH2D* occupancy_phi_eta_all;

public:
  explicit EfficiencyCalculator(const edm::ParameterSet& iConfig);
  ~EfficiencyCalculator(){}
  
 private:
  virtual void beginRun(const edm::Run& run,const edm::EventSetup& iSetup);
  virtual void endRun(edm::Run const&, edm::EventSetup const&) override{}
  virtual void analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup);
  virtual void endJob(){};
};


EfficiencyCalculator::EfficiencyCalculator(const edm::ParameterSet& iConfig):
  hltProcess_("MYHLT")
{
  eleToken_     = consumes<std::vector<pat::Electron> >(edm::InputTag("slimmedElectrons","","PAT"));
  metToken_     = consumes<std::vector<pat::MET> >(edm::InputTag("slimmedMETs","","PAT"));
  hltToken_     = consumes<edm::TriggerResults>(edm::InputTag("TriggerResults","","MYHLT"));
  triggerObjectsToken_ = consumes<std::vector<pat::TriggerObjectStandAlone> > (edm::InputTag("slimmedPatTrigger","","PAT"));
  
  // Define all the histograms to be filled
  // pT
  num_ele_pt_EB1  = fs->make<TH1D>("num_ele_pt_EB1",";pT (GeV);Events",200,0,500);
  num_ele_pt_EB2  = fs->make<TH1D>("num_ele_pt_EB2",";pT (GeV);Events",200,0,500);
  num_ele_pt_EB   = fs->make<TH1D>("num_ele_pt_EB",";pT (GeV);Events",200,0,500);
  num_ele_pt_EE1  = fs->make<TH1D>("num_ele_pt_EE1",";pT (GeV);Events",200,0,500);
  num_ele_pt_EE2  = fs->make<TH1D>("num_ele_pt_EE2",";pT (GeV);Events",200,0,500);
  num_ele_pt_EE   = fs->make<TH1D>("num_ele_pt_EE",";pT (GeV);Events",200,0,500);
  num_ele_pt      = fs->make<TH1D>("num_ele_pt",";pT (GeV);Events",200,0,500);

  den_ele_pt_EB1  = fs->make<TH1D>("den_ele_pt_EB1",";pT (GeV);Events",200,0,500);
  den_ele_pt_EB2  = fs->make<TH1D>("den_ele_pt_EB2",";pT (GeV);Events",200,0,500);
  den_ele_pt_EB   = fs->make<TH1D>("den_ele_pt_EB",";pT (GeV);Events",200,0,500);
  den_ele_pt_EE1  = fs->make<TH1D>("den_ele_pt_EE1",";pT (GeV);Events",200,0,500);
  den_ele_pt_EE2  = fs->make<TH1D>("den_ele_pt_EE2",";pT (GeV);Events",200,0,500);
  den_ele_pt_EE   = fs->make<TH1D>("den_ele_pt_EE",";pT (GeV);Events",200,0,500);
  den_ele_pt      = fs->make<TH1D>("den_ele_pt",";pT (GeV);Events",200,0,500);

  // eta
  num_ele_eta     = fs->make<TH1D>("num_ele_eta",";eta;Events",53,-2.65,2.65);
  den_ele_eta     = fs->make<TH1D>("den_ele_eta",";eta;Events",53,-2.65,2.65);

  // phi
  num_ele_phi     = fs->make<TH1D>("num_ele_phi",";phi;Events",63,-3.15,3.15);
  den_ele_phi     = fs->make<TH1D>("den_ele_phi",";phi;Events",63,-3.15,3.15);

  // occupancy
  occupancy_phi_eta_all = fs->make<TH2D>("occupancy_phi_eta_all",";#eta_{SC};#phi",50,-2.5,2.5,32,-3.2,3.2);
}

std::vector<pat::TriggerObjectStandAlone> matchTrigObjs(const float eta,const float phi,std::vector<pat::TriggerObjectStandAlone> trigObjs,const float maxDeltaR=0.1)
{
  std::vector<pat::TriggerObjectStandAlone> matchedObjs;
  const float maxDR2 = maxDeltaR*maxDeltaR;
  for(auto trigObj : trigObjs){
	const float deltaR2 = reco::deltaR2(eta, phi, trigObj.eta(), trigObj.phi());
    if(deltaR2 < maxDR2) matchedObjs.push_back(trigObj);
  }
  return matchedObjs;
}

const bool matchDRAndpT(const float eta1,const float phi1,const float pT1,const float eta2,const float phi2,const float pT2,const float maxDeltaR=0.1, const float maxDpT=0.1){
  bool isMatched = false;
  const float maxDR2 = maxDeltaR*maxDeltaR;
  const float deltaR2 = reco::deltaR2(eta1, phi1, eta2, phi2);
  const float deltaPt = fabs(pT1-pT2)/pT1;
  if(deltaR2 < maxDR2 && deltaPt < maxDpT) isMatched = true;
  return isMatched;
}

float calculateInvMass(const pat::Electron tagElectron, const pat::Electron probeCandidate) {

  TLorentzVector tag;
  TLorentzVector probe;

  tag.SetPxPyPzE(tagElectron.px(),tagElectron.py(),tagElectron.pz(),tagElectron.energy());
  probe.SetPxPyPzE(probeCandidate.px(),probeCandidate.py(),probeCandidate.pz(),probeCandidate.energy());

  float invMass = (tag + probe).M();

  return invMass;

}

//we need to initalise the menu each run (menu can and will change on run boundaries)
void EfficiencyCalculator::beginRun(const edm::Run& run,const edm::EventSetup& setup)
{
}

void EfficiencyCalculator::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<std::vector<pat::Electron> > ele;
  iEvent.getByToken(eleToken_,ele);

  edm::Handle<std::vector<pat::MET> > met;
  iEvent.getByToken(metToken_,met);

  edm::Handle<edm::TriggerResults > hlt;
  iEvent.getByToken(hltToken_,hlt);

  edm::Handle<std::vector<pat::TriggerObjectStandAlone> > triggerObjects;
  iEvent.getByToken(triggerObjectsToken_, triggerObjects);

  // Create a list of trigger objects with unpacked filter names
  std::vector<pat::TriggerObjectStandAlone> unpackedTriggerObjects;
  for(auto& trigObj : *triggerObjects){
    unpackedTriggerObjects.push_back(trigObj);
    unpackedTriggerObjects.back().unpackFilterLabels(iEvent,*hlt);
    //if(unpackedTriggerObjects.back().hasFilterLabel("hltEle30WPTightGsfTrackIsoFilter")){
    // std::cout << "THE FILTER EXISTS" << std::endl;
    //}
  }

  auto electrons = ele.product();
  //auto mets = met.product();

  //std::cout<<"Electrons size"<<electrons->size()<<std::endl; 
  // Only retain events with at least two offline electrons
  //if(electrons->size()>1) return;
  //std::cout<<"I passed 1 electron condition"<<std::endl;

  const pat::MET& MET = met->front();  // Assuming a single MET object
  if (MET.pt() < 20) return; // Skip the event by returning early

  for(auto& el : *electrons){

    if(fabs(el.eta()) > endcap_end_) continue;

	// Only continue if a good probe is found
    if(el.electronID("cutBasedElectronID_RunIIIWinter22_V1_tight")){	
      // Fill denominators and occupancy histograms based on the probe passing the above ID
      if (fabs(el.eta()) < 1.0 ) den_ele_pt_EB1->Fill(el.pt());
      if (fabs(el.eta()) > 1.0 && fabs(el.eta()) < 1.44 ) den_ele_pt_EB2->Fill(el.pt());
      if (fabs(el.eta()) < 1.44) den_ele_pt_EB->Fill(el.pt());
	  if (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.0) den_ele_pt_EE1->Fill(el.pt());
      if (fabs(el.eta()) > 2.00 && fabs(el.eta()) < 2.5) den_ele_pt_EE2->Fill(el.pt());
      if (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.5) den_ele_pt_EE->Fill(el.pt());

      if ( (fabs(el.eta()) < 1.44) || (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.5)) den_ele_pt->Fill(el.pt());

      if (el.pt() > 30.) {
        den_ele_eta->Fill(el.eta());
        den_ele_phi->Fill(el.phi());
      }

      // Create a list of probes matched to trigger objects based on DeltaR < 0.1
	  auto matchedTrigObjsProbes = matchTrigObjs(el.eta(),el.phi(),unpackedTriggerObjects);
      auto nmatch_filter = matchedTrigObjsProbes.size();

      // Fill numerators based on the passing of a certain trigger filter
	  if(nmatch_filter>0){
        for(auto trigObj : matchedTrigObjsProbes){
          if(trigObj.hasFilterLabel("hltEle30WPTightGsfTrackIsoFilter")){
	        // Barrel
            if (fabs(el.eta()) < 1.0 ) num_ele_pt_EB1->Fill(el.pt());
            if (fabs(el.eta()) > 1.0 && fabs(el.eta()) < 1.44) num_ele_pt_EB2->Fill(el.pt());
            if (fabs(el.eta()) < 1.44 ) num_ele_pt_EB->Fill(el.pt());

            // Endcap
            if (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.0) num_ele_pt_EE1->Fill(el.pt());
            if (fabs(el.eta()) > 2.00 && fabs(el.eta()) < 2.5) num_ele_pt_EE2->Fill(el.pt());
            if (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.5) num_ele_pt_EE->Fill(el.pt());

            // Full
            if ( (fabs(el.eta()) < 1.44) || (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.5)) num_ele_pt->Fill(el.pt());

            if (el.pt() > 30.) {
              num_ele_eta->Fill(el.eta());
              num_ele_phi->Fill(el.phi());
	          occupancy_phi_eta_all->Fill(el.eta(),el.phi());
            }
	        break; // Avoid to fill the numerator more than once with the same object if more than one offline-online matching is found
          }
		}  
	  }	  
    }
	break;
  }
}


//define this as a plug-in
DEFINE_FWK_MODULE(EfficiencyCalculator);
