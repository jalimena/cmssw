#ifndef MuonIdentification_MuonTimingFillerDelayedMuons_h
#define MuonIdentification_MuonTimingFillerDelayedMuons_h 1

// -*- C++ -*-
//
// Package:    MuonTimingFillerDelayedMuons
// Class:      MuonTimingFillerDelayedMuons
// 
/**\class MuonTimingFillerDelayedMuons MuonTimingFillerDelayedMuons.h RecoMuon/MuonIdentification/interface/MuonTimingFillerDelayedMuons.h

 Description: Class filling the DT, CSC and Combined MuonTimeExtra objects

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Piotr Traczyk, CERN
//         Created:  Mon Mar 16 12:27:22 CET 2009
// $Id: MuonTimingFillerDelayedMuons.h,v 1.7 2011/02/24 15:41:53 farrell3 Exp $
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
#include "RecoMuon/MuonIdentification/interface/DTTimingExtractorDelayedMuons.h"
#include "RecoMuon/MuonIdentification/interface/CSCTimingExtractorDelayedMuons.h"

//
// class decleration
//

class MuonTimingFillerDelayedMuons {
   public:
  MuonTimingFillerDelayedMuons(const edm::ParameterSet&, edm::ConsumesCollector&& iC);
      ~MuonTimingFillerDelayedMuons();
      void fillTiming( const reco::Muon& muon, reco::MuonTimeExtra& dtTime, 
                    reco::MuonTimeExtra& cscTime, reco::MuonTimeExtra& combinedTime, 
                    edm::Event& iEvent, const edm::EventSetup& iSetup );

   private:
      void fillTimeFromMeasurements( TimeMeasurementSequence tmSeq, reco::MuonTimeExtra &muTime );
      void rawFit(double &a, double &da, double &b, double &db, 
                  const std::vector<double> hitsx, const std::vector<double> hitsy);
      void addEcalTime( const reco::Muon& muon, TimeMeasurementSequence &cmbSeq );
      void combineTMSequences( const reco::Muon& muon, TimeMeasurementSequence dtSeq, 
                               TimeMeasurementSequence cscSeq, TimeMeasurementSequence &cmbSeq );
      
      DTTimingExtractorDelayedMuons* theDTTimingExtractor_;
      CSCTimingExtractorDelayedMuons* theCSCTimingExtractor_;
      double errorEB_,errorEE_,ecalEcut_;
      bool useDT_, useCSC_, useECAL_;

};

#endif
