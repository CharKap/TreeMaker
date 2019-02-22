// -*- C++ -*-
//
// Package:    GoodJetsProducer
// Class:      GoodJetsProducer
//
/**\class GoodJetsProducer GoodJetsProducer.cc RA2Classic/GoodJetsProducer/src/GoodJetsProducer.cc
 *
 * Description: [one line class summary]
 *
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Thu Apr 17 10:49:52 CEST 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"
#include <DataFormats/PatCandidates/interface/Photon.h>
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include <TVector2.h>
//
// class declaration
//

class GoodJetsProducer : public edm::global::EDFilter<> {
public:
	explicit GoodJetsProducer(const edm::ParameterSet&);
	~GoodJetsProducer() override;

	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
	bool filter(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

	enum VarOptions {neutralEmEnergyFraction,neutralHadronEnergyFraction,neutralMultiplicity,chargedEmEnergyFraction,
					 chargedHadronEnergyFraction,chargedMultiplicity,nconstituents,muonEnergyFraction}; 

	// ----------member data ---------------------------
	edm::InputTag JetTag_;
	std::vector<edm::InputTag> SkipTag_;
	edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
	std::vector<edm::EDGetTokenT<edm::View<reco::Candidate>>> SkipTok_;
	double maxEta_;
	std::vector<std::string> varnames_;
	std::vector<VarOptions> vartypes_;
	std::vector<double> etamin_, etamax_, cutvalmin_, cutvalmax_;
	double jetPtFilter_;
	bool saveAllId_, saveAllPt_, ExcludeLeptonIsoTrackPhotons_, TagMode_, invertJetPtFilter_;
	double JetConeSize_;
};

//
// constructors and destructor
//
using namespace pat;
GoodJetsProducer::GoodJetsProducer(const edm::ParameterSet& iConfig) {
	TagMode_ = iConfig.getParameter<bool> ("TagMode");
	JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
	maxEta_ = iConfig.getParameter <double> ("maxJetEta");
	varnames_ = iConfig.getParameter <std::vector<std::string>> ("varnames");
	etamin_ = iConfig.getParameter <std::vector<double>> ("etamin");
	etamax_ = iConfig.getParameter <std::vector<double>> ("etamax");
	cutvalmin_ = iConfig.getParameter <std::vector<double>> ("cutvalmin");
	cutvalmax_ = iConfig.getParameter <std::vector<double>> ("cutvalmax");
	jetPtFilter_ = iConfig.getParameter <double> ("jetPtFilter");
	invertJetPtFilter_ = iConfig.getParameter <bool> ("invertJetPtFilter");
	saveAllId_ = iConfig.getParameter <bool> ("SaveAllJetsId");
	saveAllPt_ = iConfig.getParameter <bool> ("SaveAllJetsPt");

	ExcludeLeptonIsoTrackPhotons_ = iConfig.getParameter <bool> ("ExcludeLepIsoTrackPhotons");
	SkipTag_  = iConfig.getParameter<std::vector<edm::InputTag>>("SkipTag");
	JetConeSize_ = iConfig.getParameter <double> ("JetConeSize");

	JetTok_ = consumes<edm::View<pat::Jet>>(JetTag_);
	for(auto& tag: SkipTag_) SkipTok_.push_back(consumes<edm::View<reco::Candidate>>(tag));

	// check the contents of the varnames_ vector to make sure it contains only allowed values
	vartypes_.reserve(varnames_.size());
	for(auto v : varnames_) {
		if(v=="neutralEmEnergyFraction")			vartypes_.push_back(neutralEmEnergyFraction);
		else if(v=="neutralHadronEnergyFraction")	vartypes_.push_back(neutralHadronEnergyFraction);
		else if(v=="neutralMultiplicity")			vartypes_.push_back(neutralMultiplicity);
		else if(v=="chargedEmEnergyFraction")		vartypes_.push_back(chargedEmEnergyFraction);
		else if(v=="chargedHadronEnergyFraction")	vartypes_.push_back(chargedHadronEnergyFraction);
		else if(v=="chargedMultiplicity")			vartypes_.push_back(chargedMultiplicity);
		else if(v=="nconstituents")					vartypes_.push_back(nconstituents);
		else if(v=="muonEnergyFraction")			vartypes_.push_back(muonEnergyFraction);
		else if(v=="nef")							vartypes_.push_back(neutralEmEnergyFraction);
		else if(v=="nhf")							vartypes_.push_back(neutralHadronEnergyFraction);
		else if(v=="nm")							vartypes_.push_back(neutralMultiplicity);
		else if(v=="cef")							vartypes_.push_back(chargedEmEnergyFraction);
		else if(v=="chf")							vartypes_.push_back(chargedHadronEnergyFraction);
		else if(v=="cm")							vartypes_.push_back(chargedMultiplicity);
		else if(v=="nc")							vartypes_.push_back(nconstituents);
		else if(v=="mf")							vartypes_.push_back(muonEnergyFraction);
		else {
			edm::LogError("TreeMaker") << "ERROR: GoodJetsProducer: variable name " << v << " unknown";	
		}
	}

	produces<std::vector<Jet> >();
	produces<bool>("JetID");
	produces<std::vector<bool> >("JetIDMask");
	produces<std::vector<bool> >("JetLeptonMask");
}


GoodJetsProducer::~GoodJetsProducer() {
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
}


//
// member functions
//

// ------------ method called to produce the data  ------------
bool
GoodJetsProducer::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {
	using namespace edm;
	// load to be excluded leptons, isotracks and photons
	std::vector<edm::Handle<edm::View<reco::Candidate>>> excludeHandles;
	excludeHandles.reserve(SkipTag_.size());
	if(ExcludeLeptonIsoTrackPhotons_ && !SkipTag_.empty()) {
		// loop over each edm::InputTag
		for (unsigned iC = 0; iC < SkipTag_.size(); ++iC) {
			// get each collection the edm::InputTag corresponds to
			edm::Handle<edm::View<reco::Candidate>> cleanCands;
			iEvent.getByToken(SkipTok_[iC], cleanCands);
			if (cleanCands.isValid()) {
				excludeHandles.push_back(cleanCands);
			}
			else {
				edm::LogWarning("TreeMaker")<<"Warning: skip tag not valid in GoodJetsProducer: "<<SkipTag_[iC];
			}
		}
	}

	auto prodJets = std::make_unique<std::vector<Jet>>();
	auto jetsMask = std::make_unique<std::vector<bool>>();
	auto leptonMask = std::make_unique<std::vector<bool>>();
	bool result=true;
	edm::Handle< edm::View<Jet> > Jets;
	iEvent.getByToken(JetTok_,Jets);
	if(Jets.isValid()) {
		prodJets->reserve(Jets->size());
		jetsMask->reserve(Jets->size());
		leptonMask->reserve(Jets->size());
		for(const auto & iJet : *Jets) {
			if (maxEta_>0 and std::abs(iJet.eta())>maxEta_) continue;
			if (!saveAllPt_ && ( (!invertJetPtFilter_ && iJet.pt() <= jetPtFilter_) || (invertJetPtFilter_ && iJet.pt() > jetPtFilter_) ) ) continue;
			if (!iJet.isPFJet()) continue;
			//check for a candidate with infinite energy, drop the associated jet
			if (iJet.numberOfDaughters()>0 and std::isinf(iJet.daughterPtr(0)->energy())) continue;

			bool skip=false;
			if (ExcludeLeptonIsoTrackPhotons_ && !excludeHandles.empty()) {
				for (const auto & excludeHandle : excludeHandles) {
					for (const auto & exclude : *excludeHandle) {
						if (std::abs(iJet.pt() - exclude.pt() ) / exclude.pt() < 1 && deltaR(iJet.p4(),exclude.p4()) < JetConeSize_ ) {
							skip=true;
							break;
						}
						if (skip) break; //no need to keep checking
					}
				}
				if (skip) {
					prodJets->push_back(Jet(iJet));
					jetsMask->push_back(true);
					leptonMask->push_back(true);
					continue;
				}
				else leptonMask->push_back(false);
			}
			else leptonMask->push_back(false);

			//calculate the PFJetID decision
			bool good = true;
			double varval = 0.0;
			for(unsigned v=0; v<vartypes_.size(); ++v) {
				if(vartypes_[v]==neutralHadronEnergyFraction)		varval = iJet.neutralHadronEnergyFraction(); //gives raw energy in the denominator
				else if(vartypes_[v]==neutralEmEnergyFraction)		varval = iJet.neutralEmEnergyFraction(); //gives raw energy in the denominator
				else if(vartypes_[v]==neutralMultiplicity)			varval = iJet.neutralMultiplicity();
				else if(vartypes_[v]==chargedHadronEnergyFraction)	varval = iJet.chargedHadronEnergyFraction();
				else if(vartypes_[v]==chargedEmEnergyFraction)		varval = iJet.chargedEmEnergyFraction();
				else if(vartypes_[v]==chargedMultiplicity)			varval = iJet.chargedMultiplicity();
				else if(vartypes_[v]==nconstituents)				varval = iJet.neutralMultiplicity() + iJet.chargedMultiplicity();
				else if(vartypes_[v]==muonEnergyFraction)			varval = iJet.muonEnergyFraction();
				else {
					edm::LogError("TreeMaker") << "ERROR: GoodJetsProducer: unkown variable name " << v << ". Unable to select the correct value for the jet pproperty.";
					varval = 0.0;
				}
				if(abs(iJet.eta())>etamin_[v] && abs(iJet.eta())<=etamax_[v] && (varval<cutvalmin_[v] || varval>cutvalmax_[v])) {
					good = false;
					break;
				}
			}

			//save good jets, potentially regardless of id or pt
			if (good || saveAllId_) {
				prodJets->push_back(Jet(iJet));
				jetsMask->push_back(good);
			}

			//calculate event filter only for jets that pass pT cut
			if ( (!invertJetPtFilter_ && iJet.pt() > jetPtFilter_) || (invertJetPtFilter_ && iJet.pt() <= jetPtFilter_) ) {
				if(!good && !TagMode_) return false;
				result &= good;
			}
		}
	}

	// put in the event
	iEvent.put(std::move(prodJets));
	iEvent.put(std::move(jetsMask),"JetIDMask");
	iEvent.put(std::move(leptonMask),"JetLeptonMask");
	auto passing = std::make_unique<bool>(result);
	iEvent.put(std::move(passing),"JetID");
	return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GoodJetsProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GoodJetsProducer);
