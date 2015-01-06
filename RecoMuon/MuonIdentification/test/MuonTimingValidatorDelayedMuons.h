#ifndef RecoMuon_MuonIdentification_MuonTimingValidatorDelayedMuons_H
#define RecoMuon_MuonIdentification_MuonTimingValidatorDelayedMuons_H

/** \class MuonTimingValidatorDelayedMuons
 *  Analyzer of the timing information in the reco::Muon object
 *
 *  $Date: 2010/03/25 14:08:50 $
 *  $Revision: 1.6 $
 *  \author P. Traczyk    CERN
 */

// Base Class Headers
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"

#include "SimDataFormats/Track/interface/SimTrack.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/TrackExtraFwd.h"
#include "DataFormats/TrackReco/interface/TrackToTrackMap.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtra.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtraMap.h"

#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment4DCollection.h"
#include "DataFormats/DTRecHit/interface/DTRecHitCollection.h"
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"

#include <TROOT.h>
#include <TSystem.h>

namespace edm {
  class ParameterSet;
  //  class Event;
  class EventSetup;
  class InputTag;
}

class TFile;
class TH1F;
class TH2F;
//class TrackRef;
//class SimTrackRef;
//class MuonRef;
class MuonServiceProxy;
class TTree;

class MuonTimingValidatorDelayedMuons : public edm::EDAnalyzer {
public:
  explicit MuonTimingValidatorDelayedMuons(const edm::ParameterSet&);
  ~MuonTimingValidatorDelayedMuons();
  
  typedef std::pair< reco::TrackRef, SimTrackRef> CandToSim;
  typedef std::pair< reco::TrackRef, SimTrackRef> CandStaSim;
  typedef std::pair< reco::TrackRef, SimTrackRef> CandMuonSim;
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  virtual float calculateDistance(const math::XYZVector&, const math::XYZVector&);
  virtual TH1F* divideErr(TH1F*, TH1F*, TH1F*);


  // ----------member data ---------------------------

  edm::InputTag TKtrackTags_; 
  edm::InputTag MuonTags_; 
  edm::InputTag TimeTags_; 
  edm::InputTag SIMtrackTags_; 

  std::string out, open, txtout;
  double  theMinEta, theMaxEta, theMinPt, thePtCut, theMinPtres, theMaxPtres, theScale;
  int theDtCut, theCscCut, theDtChambersCut;
  int theNBins;

  edm::Handle<reco::MuonCollection> MuCollection;
  edm::Handle<reco::MuonCollection> MuCollectionT;
  edm::Handle<reco::TrackCollection> TKTrackCollection;
  edm::Handle<reco::TrackCollection> STATrackCollection;
  edm::Handle<reco::TrackCollection> GLBTrackCollection;
  edm::Handle<reco::TrackCollection> PMRTrackCollection;
  edm::Handle<reco::TrackCollection> GMRTrackCollection;
  edm::Handle<reco::TrackCollection> FMSTrackCollection;
  edm::Handle<reco::TrackCollection> SLOTrackCollection;
  edm::Handle<edm::SimTrackContainer> SIMTrackCollection;

  edm::Handle<reco::MuonTimeExtraMap> timeMap1;
  edm::Handle<reco::MuonTimeExtraMap> timeMap2;
  edm::Handle<reco::MuonTimeExtraMap> timeMap3;
  
  //ROOT Pointers
  TFile* hFile;
  TStyle* effStyle;

  TH1F* hi_sta_pt  ;
  TH1F* hi_tk_pt   ;
  TH1F* hi_glb_pt  ;
  TH1F* hi_sta_phi ;
  TH1F* hi_tk_phi  ;
  TH1F* hi_glb_phi ;

  TH1F* hi_mutime_vtx;
  TH1F* hi_mutime_vtx_err;

  TH1F* hi_dtcsc_vtx;
  TH1F* hi_dtecal_vtx;
  TH1F* hi_ecalcsc_vtx;
  TH1F* hi_dthcal_vtx;
  TH1F* hi_hcalcsc_vtx;
  TH1F* hi_hcalecal_vtx;

  TH1F* hi_cmbtime_ibt;
  TH2F* hi_cmbtime_ibt_pt;
  TH1F* hi_cmbtime_ibt_err;
  TH1F* hi_cmbtime_ibt_pull;
  TH1F* hi_cmbtime_fib;
  TH1F* hi_cmbtime_fib_err;
  TH1F* hi_cmbtime_fib_pull;
  TH1F* hi_cmbtime_vtx;
  TH1F* hi_cmbtime_vtx_err;
  TH1F* hi_cmbtime_vtx_pull;
  TH1F* hi_cmbtime_vtxr;
  TH1F* hi_cmbtime_vtxr_err;
  TH1F* hi_cmbtime_vtxr_pull;
  TH1F* hi_cmbtime_ndof;

  TH1F* hi_dttime_ibt;
  TH2F* hi_dttime_ibt_pt;
  TH1F* hi_dttime_ibt_err;
  TH2F* hi_dttime_ibt_ibt_err;
  TH1F* hi_dttime_ibt_pull;
  TH1F* hi_dttime_fib;
  TH1F* hi_dttime_fib_err;
  TH2F* hi_dttime_fib_fib_err;
  TH1F* hi_dttime_fib_pull;
  TH1F* hi_dttime_vtx;
  TH1F* hi_dttime_vtx_err;
  TH1F* hi_dttime_vtx_pull;
  TH1F* hi_dttime_vtxr;
  TH1F* hi_dttime_vtxr_err;
  TH1F* hi_dttime_vtxr_pull;
  TH1F* hi_dttime_errdiff;
  TH1F* hi_dttime_ndof;
  TH1F* hi_dt_nmuons;

  TH1F* dttime_nHits_hist;
  TH1F* dttime_aveHitTimeError_hist;
  TH1F* dttime_invbetaLS_hist;
  TH1F* dttime_invbetaLSError_hist;
  TH1F* dttime_yIntercept_hist;
  TH1F* dttime_yInterceptError_hist;
  TH1F* dttime_chi2Dof_hist;
  TH2F* sta_phi_dttime_invbetaLS_hist;
  TH2F* dttime_invbetaLS_chi2Dof_hist;
  TH2F* dttime_invbetaLSError_chi2Dof_hist;
  TH2F* dttime_yIntercept_chi2Dof_hist;
  TH2F* dttime_yInterceptError_chi2Dof_hist;
  TH2F* dttime_nHits_invbetaLS_hist;
  TH2F* dttime_nHits_invbetaLSError_hist;
  TH2F* dttime_invbetaLS_fib;
  TH2F* dttime_invbetaLSError_fiberr;

  TH2F* dttime_localT0_hitChisq;
  TH2F* dttime_localT0_hitChisq_LowInversebetaLS;

  TH1F* hi_csctime_ibt;
  TH2F* hi_csctime_ibt_pt;
  TH1F* hi_csctime_ibt_err;
  TH1F* hi_csctime_ibt_pull;
  TH1F* hi_csctime_fib;
  TH1F* hi_csctime_fib_err;
  TH1F* hi_csctime_fib_pull;
  TH1F* hi_csctime_vtx;
  TH1F* hi_csctime_vtx_err;
  TH1F* hi_csctime_vtx_pull;
  TH1F* hi_csctime_vtxr;
  TH1F* hi_csctime_vtxr_err;
  TH1F* hi_csctime_vtxr_pull;
  TH1F* hi_csctime_ndof;

  TH1F* hi_ecal_time;
  TH1F* hi_ecal_time_err;
  TH1F* hi_ecal_time_pull;
  TH1F* hi_ecal_time_ecut;
  TH1F* hi_ecal_energy;

  TH1F* hi_hcal_time;
  TH1F* hi_hcal_time_err;
  TH1F* hi_hcal_time_pull;
  TH1F* hi_hcal_time_ecut;
  TH1F* hi_hcal_energy;

  TH1F* hi_tk_eta  ;
  TH1F* hi_sta_eta  ;
  TH1F* hi_glb_eta  ;

  int nevts_passHitChisq[1000], nevts_passHitChisq_LowInversebetaLS[1000], nhits, nhits_LowInversebetaLS;

  TTree* tree;

  //leaf types
  double LocalT0_0;
  double LocalT0_1;
  double LocalT0_2;
  double LocalT0_3;
  double LocalT0_4;
  double LocalT0_5;
  double LocalT0_6;
  double LocalT0_7;
  double LocalT0_8;
  double LocalT0_9;
  double LocalT0_10;
  double LocalT0_11;
  double LocalT0_12;
  double LocalT0_13;
  double LocalT0_14;
  double LocalT0_15;
  double LocalT0_16;
  double LocalT0_17;
  double LocalT0_18;
  double LocalT0_19;
  double LocalT0_20;
  double LocalT0_21;
  double LocalT0_22;
  double LocalT0_23;
  double LocalT0_24;
  double LocalT0_25;
  double LocalT0_26;
  double LocalT0_27;
  double LocalT0_28;
  double LocalT0_29;
  double LocalT0_30;
  double LocalT0_31;

  double CorrectedTime_0;
  double CorrectedTime_1;
  double CorrectedTime_2;
  double CorrectedTime_3;
  double CorrectedTime_4;
  double CorrectedTime_5;
  double CorrectedTime_6;
  double CorrectedTime_7;
  double CorrectedTime_8;
  double CorrectedTime_9;
  double CorrectedTime_10;
  double CorrectedTime_11;
  double CorrectedTime_12;
  double CorrectedTime_13;
  double CorrectedTime_14;
  double CorrectedTime_15;
  double CorrectedTime_16;
  double CorrectedTime_17;
  double CorrectedTime_18;
  double CorrectedTime_19;
  double CorrectedTime_20;
  double CorrectedTime_21;
  double CorrectedTime_22;
  double CorrectedTime_23;
  double CorrectedTime_24;
  double CorrectedTime_25;
  double CorrectedTime_26;
  double CorrectedTime_27;
  double CorrectedTime_28;
  double CorrectedTime_29;
  double CorrectedTime_30;
  double CorrectedTime_31;

  double Distance_0;
  double Distance_1;
  double Distance_2;
  double Distance_3;
  double Distance_4;
  double Distance_5;
  double Distance_6;
  double Distance_7;
  double Distance_8;
  double Distance_9;
  double Distance_10;
  double Distance_11;
  double Distance_12;
  double Distance_13;
  double Distance_14;
  double Distance_15;
  double Distance_16;
  double Distance_17;
  double Distance_18;
  double Distance_19;
  double Distance_20;
  double Distance_21;
  double Distance_22;
  double Distance_23;
  double Distance_24;
  double Distance_25;
  double Distance_26;
  double Distance_27;
  double Distance_28;
  double Distance_29;
  double Distance_30;
  double Distance_31;

  double HitChisq_0;
  double HitChisq_1;
  double HitChisq_2;
  double HitChisq_3;
  double HitChisq_4;
  double HitChisq_5;
  double HitChisq_6;
  double HitChisq_7;
  double HitChisq_8;
  double HitChisq_9;
  double HitChisq_10;
  double HitChisq_11;
  double HitChisq_12;
  double HitChisq_13;
  double HitChisq_14;
  double HitChisq_15;
  double HitChisq_16;
  double HitChisq_17;
  double HitChisq_18;
  double HitChisq_19;
  double HitChisq_20;
  double HitChisq_21;
  double HitChisq_22;
  double HitChisq_23;
  double HitChisq_24;
  double HitChisq_25;
  double HitChisq_26;
  double HitChisq_27;
  double HitChisq_28;
  double HitChisq_29;
  double HitChisq_30;
  double HitChisq_31;


};
#endif
