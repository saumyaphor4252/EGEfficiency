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
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "CondFormats/DataRecord/interface/L1TGlobalParametersRcd.h"
#include "DataFormats/HLTReco/interface/TriggerFilterObjectWithRefs.h"
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

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
  // edm::EDGetTokenT<std::vector<trigger::EgammaObject> > eleToken_; // For RAW data
  edm::EDGetTokenT<std::vector<reco::GsfElectron> > eleToken_; // For RAW-RECO data
  edm::EDGetTokenT<edm::TriggerResults > hltToken_;
  edm::EDGetTokenT<trigger::TriggerEvent > hltsevtToken_;
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
  virtual void endJob(){}
};


EfficiencyCalculator::EfficiencyCalculator(const edm::ParameterSet& iConfig):
  hltProcess_("MYHLT")
{
  eleToken_     = consumes<std::vector<reco::GsfElectron> >(edm::InputTag("gedGsfElectrons","","RECO")); // For RAW-RECO
  hltToken_     = consumes<edm::TriggerResults>(edm::InputTag("TriggerResults","","MYHLT"));
  hltsevtToken_ = consumes<trigger::TriggerEvent>(edm::InputTag("hltTriggerSummaryAOD","","MYHLT"));
  
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

const int getFilterIndex(const trigger::TriggerEvent& trigEvt, const std::string filterName){
  for(auto i=0; i < trigEvt.sizeFilters(); i++){

    if(filterName==trigEvt.filterLabel(i)) return i;
  }
  return trigEvt.sizeFilters();  
}

std::vector<const trigger::TriggerObject*> getListFilterPassedObj(const std::string filterName,const trigger::TriggerEvent& hlts){
  std::vector<const trigger::TriggerObject*> eg_trig_objs;
  const int filterIndex = getFilterIndex(hlts,filterName);
  if(filterIndex < hlts.sizeFilters() ){
    for(auto filterKey : hlts.filterKeys(filterIndex)){
      auto& obj = hlts.getObjects()[filterKey];
      eg_trig_objs.push_back(&obj);
    }
  }
  return eg_trig_objs;
}

std::vector<const trigger::TriggerObject*> matchTrigObjs(const float eta,const float phi,const float pT,std::vector<const trigger::TriggerObject*> trigObjs,const float maxDeltaR=0.1, const float maxDpT=0.1)
{
  std::vector<const trigger::TriggerObject*> matchedObjs;
  const float maxDR2 = maxDeltaR*maxDeltaR;
  for(auto& trigObj : trigObjs){
    const float deltaR2 = reco::deltaR2(eta, phi, trigObj->eta(), trigObj->phi());
    if(deltaR2 < maxDR2 && (fabs(pT - trigObj->pt())/pT) < maxDpT) matchedObjs.push_back(trigObj);
  }
  return matchedObjs;
}

float calculateInvMass(const reco::GsfElectron tagElectron, const reco::GsfElectron probeCandidate) { // For RAW-RECO

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
  // edm::Handle<std::vector<trigger::EgammaObject> > ele; // For RAW
  edm::Handle<std::vector<reco::GsfElectron> > ele; // For RAW-RECO
  iEvent.getByToken(eleToken_,ele);

  edm::Handle<edm::TriggerResults > hlt;
  iEvent.getByToken(hltToken_,hlt);

  edm::Handle<trigger::TriggerEvent > hltsevt;
  iEvent.getByToken(hltsevtToken_,hltsevt);

  auto trig_objs_filter = getListFilterPassedObj("hltEle32WPTightGsfTrackIsoFilter",*hltsevt.product());

  auto electrons = ele.product();
 
  // Only retain events with at least two offline electrons
  if(electrons->size() < 2) return;

  //Create a list of tags
  std::vector<reco::GsfElectron> listOfTags; //For RAW-RECO

  for(auto& el : *electrons){
    if(fabs(el.eta()) > barrel_end_ || el.pt() < 32.) continue;

    auto matchedTrigObjsTags = matchTrigObjs(el.eta(),el.phi(),el.pt(),trig_objs_filter);

	for(auto trigObj : matchedTrigObjsTags){
      listOfTags.push_back(el);
	}
  }

  // Now look for matching probes
  bool isGoodPair = false;
  for(auto& el : *electrons){

    if(fabs(el.eta()) > endcap_end_) continue;

	// Check the tag-probe invariant mass and charge compatibility with Z-->ee events
    for(auto tag : listOfTags){
      float invMass = calculateInvMass(tag, el);
      isGoodPair = (fabs(invMass - 91.1876) < 30. && tag.pdgId()*el.pdgId() < 0)? true : false;
	  if(isGoodPair) break;
    }

	// Only continue if a good probe is found
    if(!isGoodPair) continue;

    // Fill denominators and occupancy histograms based on the probe passing the above ID
    if (fabs(el.eta()) < 1.0 ) den_ele_pt_EB1->Fill(el.pt());
    if (fabs(el.eta()) > 1.0 && fabs(el.eta()) < 1.44 ) den_ele_pt_EB2->Fill(el.pt());
    if (fabs(el.eta()) < 1.44) den_ele_pt_EB->Fill(el.pt());
	if (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.0) den_ele_pt_EE1->Fill(el.pt());
    if (fabs(el.eta()) > 2.00 && fabs(el.eta()) < 2.5) den_ele_pt_EE2->Fill(el.pt());
    if (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.5) den_ele_pt_EE->Fill(el.pt());

    if ( (fabs(el.eta()) < 1.44) || (fabs(el.eta()) > 1.56 && fabs(el.eta()) < 2.5)) den_ele_pt->Fill(el.pt());

    if (el.pt() > 32.) {
      den_ele_eta->Fill(el.eta());
      den_ele_phi->Fill(el.phi());
    }

    // Create a list of probes matched to trigger objects based on DeltaR < 0.1
	auto matchedTrigObjsProbes = matchTrigObjs(el.eta(),el.phi(),el.pt(),trig_objs_filter);
    //auto matchedTrigObjsProbes = matchTrigObjs(el.eta(),el.phi(),unpackedTriggerObjects);
    auto nmatch_filter = matchedTrigObjsProbes.size();

    // Fill numerators based on the passing of a certain trigger filter
	if(nmatch_filter>0){
      for(auto trigObj : matchedTrigObjsProbes){

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

        if (el.pt() > 32.) {
          num_ele_eta->Fill(el.eta());
          num_ele_phi->Fill(el.phi());
	      occupancy_phi_eta_all->Fill(el.eta(),el.phi());
        }
	    break; // Avoid to fill the numerator more than once with the same object if more than one offline-online matching is found
        
	  }	
    }
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(EfficiencyCalculator);
