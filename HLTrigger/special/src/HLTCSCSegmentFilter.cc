// -*- C++ -*-
//
// Package:    HLTCSCSegmentFilter
// Class:      HLTCSCSegmentFilter
//
/**\class HLTCSCSegmentFilter HLTCSCSegmentFilter.cc filter/HLTCSCSegmentFilter/src/HLTCSCSegmentFilter.cc

Description:

Implementation:
<Notes on implementation>
*/
//
// Original Author:  Juliette Alimena
//         Created:  Fri Apr 8 13:55:00 CET 2016
//
//

// system include files

// user include files
#include "HLTrigger/special/interface/HLTCSCSegmentFilter.h"

//
// constructors and destructor
//
HLTCSCSegmentFilter::HLTCSCSegmentFilter(const edm::ParameterSet& iConfig) : HLTFilter(iConfig),
									     cscSegmentTag_(iConfig.getParameter<edm::InputTag>("cscSegmentTag")),
									     cscSegmentToken_(consumes<CSCSegmentCollection>(cscSegmentTag_)),
									     maxN_(iConfig.getParameter<int>("maxN"))
{
}

HLTCSCSegmentFilter::~HLTCSCSegmentFilter() {
}

void
HLTCSCSegmentFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  makeHLTFilterDescription(desc);
  desc.add<edm::InputTag>("cscSegmentTag",edm::InputTag("hltCscSegments"));
  desc.add<int>("maxN",2);
  descriptions.add("hltCSCSegmentFilter",desc);
}

//
// member functions
//

// ------------ method called on each new Event  ------------
bool HLTCSCSegmentFilter::hltFilter(edm::Event& iEvent, const edm::EventSetup& iSetup, trigger::TriggerFilterObjectWithRefs & filterproduct) const {
  using namespace edm;
  using namespace std;

  if (saveTags()) filterproduct.addCollectionTag(cscSegmentTag_);

  Handle<CSCSegmentCollection> cscSegments;
  iEvent.getByToken(cscSegmentToken_,cscSegments);

  return (cscSegments->size() <= maxN_);
}

// define as a framework module
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(HLTCSCSegmentFilter);
