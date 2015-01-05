#ifndef MuonTiming_MuonTimingProducerDelayedMuons_h
#define MuonTiming_MuonTimingProducerDelayedMuons_h 1

// -*- C++ -*-
//
// Package:    MuonTimingProducerDelayedMuons
// Class:      MuonTimingProducerDelayedMuons
// 
/**\class MuonTimingProducerDelayedMuons MuonTimingProducerDelayedMuons.h RecoMuon/MuonIdentification/interface/MuonTimingProducerDelayedMuons.h

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Piotr Traczyk, CERN
//         Created:  Mon Mar 16 12:27:22 CET 2009
// $Id: MuonTimingProducerDelayedMuons.h,v 1.2 2009/03/27 02:23:58 ptraczyk Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/MuonReco/interface/MuonTimeExtra.h"
#include "RecoMuon/MuonIdentification/interface/MuonTimingFillerDelayedMuons.h"


//
// class decleration
//

class MuonTimingProducerDelayedMuons : public edm::EDProducer {
   public:
      explicit MuonTimingProducerDelayedMuons(const edm::ParameterSet&);
      ~MuonTimingProducerDelayedMuons();

   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
      edm::InputTag m_muonCollection;

      MuonTimingFillerDelayedMuons* theTimingFiller_;

};

#endif
