#ifndef HLTCSCSegmentFilter_h
#define HLTCSCSegmentFilter_h
// -*- C++ -*-
//
// Package:    HLTCSCSegmentFilter
// Class:      HLTCSCSegmentFilter
//
/**\class HLTCSCSegmentFilter HLTCSCSegmentFilter.cc filter/HLTCSCSegmentFilter/src/HLTCSCSegmentFilter.cc

Description: Filter to cut on CSC segments, developed to remove events with CSC segments for jet NoBPTX paths

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Juliette Alimena
//         Created:  Fri Apr 8 13:55:00 CET 2016 
//
//


// include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "HLTrigger/HLTcore/interface/HLTFilter.h"

// CSC segments
#include "DataFormats/CSCRecHit/interface/CSCSegment.h"
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"

//
// class declaration
//

class HLTCSCSegmentFilter : public HLTFilter {
public:
  explicit HLTCSCSegmentFilter(const edm::ParameterSet&);
  virtual ~HLTCSCSegmentFilter();
  static void fillDescriptions(edm::ConfigurationDescriptions & descriptions);

private:
  virtual bool hltFilter(edm::Event&, const edm::EventSetup&, trigger::TriggerFilterObjectWithRefs & filterproduct) const override;

  edm::InputTag cscSegmentTag_;
  edm::EDGetTokenT<CSCSegmentCollection> cscSegmentToken_;
  
  //max number of CSC segments
  unsigned int maxN_;
};

#endif
