// -*- C++ -*-
//
// Package:    MuonTimingValidatorDelayedMuons
// Class:      MuonTimingValidatorDelayedMuons
// 
/**\class MuonTimingValidatorDelayedMuons MuonTimingValidatorDelayedMuons.cc 

 Description: An example analyzer that fills muon timing information histograms 

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Piotr Traczyk
//         Created:  Wed Sep 27 14:54:28 EDT 2006
// $Id: MuonTimingValidatorDelayedMuons.cc,v 1.9 2010/03/25 14:08:50 jribnik Exp $
//
//

#include "RecoMuon/MuonIdentification/test/MuonTimingValidatorDelayedMuons.h"

// system include files
#include <memory>
#include <string>
#include <iostream>
#include <fstream>
#include <iostream>
#include <iomanip>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "RecoMuon/TrackingTools/interface/MuonServiceProxy.h"

#include "DataFormats/Common/interface/Ref.h"

#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "Geometry/DTGeometry/interface/DTGeometry.h"
#include "Geometry/DTGeometry/interface/DTLayer.h"
#include "Geometry/DTGeometry/interface/DTSuperLayer.h"
#include "DataFormats/DTRecHit/interface/DTSLRecSegment2D.h"
#include "RecoLocalMuon/DTSegment/src/DTSegmentUpdator.h"
#include "RecoLocalMuon/DTSegment/src/DTSegmentCleaner.h"
#include "RecoLocalMuon/DTSegment/src/DTHitPairForFit.h"
#include "RecoLocalMuon/DTSegment/src/DTSegmentCand.h"

#include <Geometry/CSCGeometry/interface/CSCLayer.h>
#include <DataFormats/MuonDetId/interface/CSCDetId.h>
#include <DataFormats/CSCRecHit/interface/CSCRecHit2D.h>
#include <DataFormats/CSCRecHit/interface/CSCRangeMapAccessor.h>

#include "CommonTools/Statistics/interface/ChiSquaredProbability.h"
#include "DataFormats/MuonReco/interface/MuonCocktails.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtra.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtraMap.h"

#include "Geometry/Records/interface/GlobalTrackingGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"

#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"

#include <TROOT.h>
#include <TSystem.h>
#include <TFile.h>
#include <TH1.h>
#include <TH2.h>
#include <TLegend.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TFrame.h>

//
// constructors and destructor
//
MuonTimingValidatorDelayedMuons::MuonTimingValidatorDelayedMuons(const edm::ParameterSet& iConfig) 
  :
  TKtrackTags_(iConfig.getUntrackedParameter<edm::InputTag>("TKtracks")),
  MuonTags_(iConfig.getUntrackedParameter<edm::InputTag>("Muons")),
  TimeTags_(iConfig.getUntrackedParameter<edm::InputTag>("Timing")),
  out(iConfig.getParameter<std::string>("out")),
  open(iConfig.getParameter<std::string>("open")),
  txtout(iConfig.getParameter<std::string>("txtout")),
  theMinEta(iConfig.getParameter<double>("etaMin")),
  theMaxEta(iConfig.getParameter<double>("etaMax")),
  theMinPt(iConfig.getParameter<double>("simPtMin")),
  thePtCut(iConfig.getParameter<double>("PtCut")),
  theMinPtres(iConfig.getParameter<double>("PtresMin")),
  theMaxPtres(iConfig.getParameter<double>("PtresMax")),
  theScale(iConfig.getParameter<double>("PlotScale")),
  theDtCut(iConfig.getParameter<int>("DTcut")),
  theCscCut(iConfig.getParameter<int>("CSCcut")),
  theDtChambersCut(iConfig.getParameter<int>("DTChambersCut")),
  theNBins(iConfig.getParameter<int>("nbins"))
{
  //now do what ever initialization is needed
}


MuonTimingValidatorDelayedMuons::~MuonTimingValidatorDelayedMuons()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
  if (hFile!=0) {
    hFile->Close();
    delete hFile;
  }
}


//
// member functions
//

// ------------ method called to for each event  ------------
void
MuonTimingValidatorDelayedMuons::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
//  std::cout << "*** Begin Muon Timing Validatior " << std::endl;
//  std::cout << " Event: " << iEvent.id() << "  Orbit: " << iEvent.orbitNumber() << "  BX: " << iEvent.bunchCrossing() << std::endl;

  iEvent.getByLabel( TKtrackTags_, TKTrackCollection);
  reco::TrackCollection tkTC;
  const reco::TrackCollection tkTC1 = *(TKTrackCollection.product());

  iEvent.getByLabel(MuonTags_,MuCollection);
  const reco::MuonCollection muonC = *(MuCollection.product());
  if (!muonC.size()) return;

  iEvent.getByLabel(TimeTags_.label(),"combined",timeMap1);
  const reco::MuonTimeExtraMap & timeMapCmb = *timeMap1;
  iEvent.getByLabel(TimeTags_.label(),"dt",timeMap2);
  const reco::MuonTimeExtraMap & timeMapDT = *timeMap2;
  iEvent.getByLabel(TimeTags_.label(),"csc",timeMap3);
  const reco::MuonTimeExtraMap & timeMapCSC = *timeMap3;

  edm::ESHandle<GlobalTrackingGeometry> theTrackingGeometry;
  iSetup.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry);

  reco::MuonCollection::const_iterator imuon;
  
  bool debug=false;

  int imucount=0;
  int igoodmucount=0;
  for(imuon = muonC.begin(); imuon != muonC.end(); ++imuon){
    
    //debug=false;
    debug=true;
    // if (imuon->pt()>100 && imuon->isGlobalMuon()) debug=true;
    
    //if (debug)
    //std::cout << " Event: " << iEvent.id() << " Found muon. Pt: " << imuon->p() << std::endl;
    
    if ((fabs(imuon->eta())<theMinEta) || (fabs(imuon->eta())>theMaxEta)) continue;
    
    reco::TrackRef trkTrack = imuon->track();
    if (trkTrack.isNonnull()) { 
      hi_tk_pt->Fill(((*trkTrack).pt()));
      hi_tk_phi->Fill(((*trkTrack).phi()));
      hi_tk_eta->Fill(((*trkTrack).eta()));
    }  

    //reco::TrackRef staTrack = imuon->standAloneMuon();
    //if (staTrack.isNonnull()) {
    //hi_sta_pt->Fill((*staTrack).pt());
    //hi_sta_phi->Fill((*staTrack).phi());
    //hi_sta_eta->Fill(((*staTrack).eta()));
    //}

    reco::TrackRef glbTrack = imuon->combinedMuon();
    if (glbTrack.isNonnull()) {
      hi_glb_pt->Fill((*glbTrack).pt());
      hi_glb_phi->Fill((*glbTrack).phi());
      hi_glb_eta->Fill((*glbTrack).eta()); 
      
      //if (debug)
      //std::cout << " Global Pt: " << (*glbTrack).pt() << std::endl;
    }

    // Analyze the short info stored directly in reco::Muon
    
    reco::MuonTime muonTime;
    if (imuon->isTimeValid()) { 
      muonTime = imuon->time();
//      std::cout << "    Time points: " << muonTime.nDof << "  time: " << muonTime.timeAtIpInOut << std::endl;
      if (muonTime.nDof) {
        hi_mutime_vtx->Fill(muonTime.timeAtIpInOut);
        hi_mutime_vtx_err->Fill(muonTime.timeAtIpInOutErr);
      }
    }
    
    reco::MuonEnergy muonE;
//    if (imuon->isEnergyValid() && fabs(imuon->eta())<1.5) { 
    if (imuon->isEnergyValid()) { 
      muonE = imuon->calEnergy();
      if (muonE.emMax>0.25) {
        hi_ecal_time->Fill(muonE.ecal_time);
        if (muonE.emMax>1.) hi_ecal_time_ecut->Fill(muonE.ecal_time);
        hi_ecal_energy->Fill(muonE.emMax);
        if (muonE.hadMax>0.25) hi_hcalecal_vtx->Fill(muonE.hcal_time-muonE.ecal_time);
        
        double emErr = 1.5/muonE.emMax;
        
        if (emErr>0.) {
          hi_ecal_time_err->Fill(emErr);
          hi_ecal_time_pull->Fill((muonE.ecal_time-1.)/emErr);
          //if (debug)
	  //std::cout << "     ECAL time: " << muonE.ecal_time << " +/- " << emErr << std::endl;
        }
      }

      if (muonE.hadMax>0.25) {
        hi_hcal_time->Fill(muonE.hcal_time);
        if (muonE.hadMax>1.) hi_hcal_time_ecut->Fill(muonE.hcal_time);
        hi_hcal_energy->Fill(muonE.hadMax);
        
        double hadErr = 1.; // DUMMY!!!
        
        hi_hcal_time_err->Fill(hadErr);
        hi_hcal_time_pull->Fill((muonE.hcal_time-1.)/hadErr);
        //if (debug)
	//std::cout << "     HCAL time: " << muonE.hcal_time << " +/- " << hadErr << std::endl;
      }
    }
    
    // Analyze the MuonTimeExtra information
    reco::MuonRef muonR(MuCollection,imucount);
    reco::MuonTimeExtra timec = timeMapCmb[muonR];
    reco::MuonTimeExtra timedt = timeMapDT[muonR];
    reco::MuonTimeExtra timecsc = timeMapCSC[muonR];

    hi_cmbtime_ndof->Fill(timec.nDof());
    //hi_dttime_ndof->Fill(timedt.nDof());
    hi_csctime_ndof->Fill(timecsc.nDof());

    //if (timedt.nDof()>theDtCut) {
    //if (debug) {
    //std::cout << "          DT nDof: " << timedt.nDof() << std::endl;
    //std::cout << "          DT Time: " << timedt.timeAtIpInOut() << " +/- " << timedt.inverseBetaErr() << std::endl;
    //std::cout << "         DT FreeB: " << timedt.freeInverseBeta() << " +/- " << timedt.freeInverseBetaErr() << std::endl;
    //}
      
    reco::TrackRef staTrack = imuon->standAloneMuon();
    if (staTrack.isNonnull()) {
      if((*staTrack).pt()>thePtCut){
	if (timedt.nDof()>theDtCut) {
	  if((*staTrack).hitPattern().dtStationsWithValidHits()>theDtChambersCut){
	      
	  //if(timedt.invbetaLSError()<1.5){
	  //if((*staTrack).phi()>0.){
	    //if(timedt.invbetaLS()<1.1 && timedt.invbetaLS()>0.9){
	      //std::cout << " Event: " << iEvent.id() << "  Run: "<< iEvent.run()<<std::endl;
	  igoodmucount++;

	  if (debug) {
	    std::cout << "          DT nDof: " << timedt.nDof() << std::endl;
	    std::cout << "          DT Time: " << timedt.timeAtIpInOut() << " +/- " << timedt.inverseBetaErr() << std::endl;
	    std::cout << "         DT FreeInverseBeta: " << timedt.freeInverseBeta() << " +/- " << timedt.freeInverseBetaErr() << std::endl;
	    std::cout << "         DT LS Inverse Beta: " << timedt.invbetaLS() << " +/- " << timedt.invbetaLSError() << std::endl;
	  }

	  hi_dttime_ndof->Fill(timedt.nDof());

	  hi_sta_pt->Fill((*staTrack).pt());
	  hi_sta_phi->Fill((*staTrack).phi());
	  hi_sta_eta->Fill(((*staTrack).eta()));
	  
	  hi_dttime_ibt->Fill(timedt.inverseBeta());
	  hi_dttime_ibt_pt->Fill(imuon->pt(),timedt.inverseBeta());
	  hi_dttime_ibt_ibt_err->Fill(timedt.inverseBeta(),timedt.inverseBetaErr());
	  hi_dttime_ibt_err->Fill(timedt.inverseBetaErr());
	  hi_dttime_fib->Fill(timedt.freeInverseBeta());
	  hi_dttime_fib_fib_err->Fill(timedt.freeInverseBeta(),timedt.freeInverseBetaErr());
	  hi_dttime_fib_err->Fill(timedt.freeInverseBetaErr());
	  hi_dttime_vtx->Fill(timedt.timeAtIpInOut());
	  hi_dttime_vtx_err->Fill(timedt.timeAtIpInOutErr());
	  hi_dttime_vtxr->Fill(timedt.timeAtIpOutIn());
	  hi_dttime_vtxr_err->Fill(timedt.timeAtIpOutInErr());
	  hi_dttime_errdiff->Fill(timedt.timeAtIpInOutErr()-timedt.timeAtIpOutInErr());
	  
	  if(debug) if(timedt.invbetaLS()<1.05 && timedt.invbetaLS()>0.95) std::cout<<"!!!!!!!!!!!!! invbeta is: <<"<<timedt.invbetaLS()<<" !!!!!!!!!!!!"<<std::endl;
	  dttime_nHits_hist->Fill(timedt.nDof());
	  dttime_aveHitTimeError_hist->Fill(timedt.aveHitTimeError());
	  dttime_invbetaLS_hist->Fill(timedt.invbetaLS());
	  dttime_invbetaLSError_hist->Fill(timedt.invbetaLSError());
	  dttime_yIntercept_hist->Fill(timedt.yIntercept());
	  dttime_yInterceptError_hist->Fill(timedt.yInterceptError());
	  dttime_chi2Dof_hist->Fill(timedt.chi2Dof());
	  sta_phi_dttime_invbetaLS_hist->Fill((*staTrack).phi(),timedt.invbetaLS());
	  dttime_invbetaLS_chi2Dof_hist->Fill(timedt.invbetaLS(),timedt.chi2Dof());
	  dttime_invbetaLSError_chi2Dof_hist->Fill(timedt.invbetaLSError(),timedt.chi2Dof());
	  dttime_yIntercept_chi2Dof_hist->Fill(timedt.yIntercept(),timedt.chi2Dof());
	  dttime_yInterceptError_chi2Dof_hist->Fill(timedt.yInterceptError(),timedt.chi2Dof());
	  dttime_nHits_invbetaLS_hist->Fill(timedt.nDof(),timedt.invbetaLS());
	  dttime_nHits_invbetaLSError_hist->Fill(timedt.nDof(),timedt.invbetaLSError());

	  dttime_invbetaLS_fib->Fill(timedt.invbetaLS(),timedt.freeInverseBeta());
	  dttime_invbetaLSError_fiberr->Fill(timedt.invbetaLSError(),timedt.freeInverseBetaErr());

	  dttime_localT0_hitChisq->Fill(timedt.localT00(),timedt.hitChisq0());
	  dttime_localT0_hitChisq->Fill(timedt.localT01(),timedt.hitChisq1());
	  dttime_localT0_hitChisq->Fill(timedt.localT02(),timedt.hitChisq2());
	  dttime_localT0_hitChisq->Fill(timedt.localT03(),timedt.hitChisq3());
	  dttime_localT0_hitChisq->Fill(timedt.localT04(),timedt.hitChisq4());
	  dttime_localT0_hitChisq->Fill(timedt.localT05(),timedt.hitChisq5());
	  dttime_localT0_hitChisq->Fill(timedt.localT06(),timedt.hitChisq6());
	  dttime_localT0_hitChisq->Fill(timedt.localT07(),timedt.hitChisq7());
	  dttime_localT0_hitChisq->Fill(timedt.localT08(),timedt.hitChisq8());
	  dttime_localT0_hitChisq->Fill(timedt.localT09(),timedt.hitChisq9());
	  dttime_localT0_hitChisq->Fill(timedt.localT010(),timedt.hitChisq10());
	  dttime_localT0_hitChisq->Fill(timedt.localT011(),timedt.hitChisq11());
	  dttime_localT0_hitChisq->Fill(timedt.localT012(),timedt.hitChisq12());
	  dttime_localT0_hitChisq->Fill(timedt.localT013(),timedt.hitChisq13());
	  dttime_localT0_hitChisq->Fill(timedt.localT014(),timedt.hitChisq14());
	  dttime_localT0_hitChisq->Fill(timedt.localT015(),timedt.hitChisq15());
	  dttime_localT0_hitChisq->Fill(timedt.localT016(),timedt.hitChisq16());
	  dttime_localT0_hitChisq->Fill(timedt.localT017(),timedt.hitChisq17());
	  dttime_localT0_hitChisq->Fill(timedt.localT018(),timedt.hitChisq18());
	  dttime_localT0_hitChisq->Fill(timedt.localT019(),timedt.hitChisq19());
	  dttime_localT0_hitChisq->Fill(timedt.localT020(),timedt.hitChisq20());
	  dttime_localT0_hitChisq->Fill(timedt.localT021(),timedt.hitChisq21());
	  dttime_localT0_hitChisq->Fill(timedt.localT022(),timedt.hitChisq22());
	  dttime_localT0_hitChisq->Fill(timedt.localT023(),timedt.hitChisq23());
	  dttime_localT0_hitChisq->Fill(timedt.localT024(),timedt.hitChisq24());
	  dttime_localT0_hitChisq->Fill(timedt.localT025(),timedt.hitChisq25());
	  dttime_localT0_hitChisq->Fill(timedt.localT026(),timedt.hitChisq26());
	  dttime_localT0_hitChisq->Fill(timedt.localT027(),timedt.hitChisq27());
	  dttime_localT0_hitChisq->Fill(timedt.localT028(),timedt.hitChisq28());
	  dttime_localT0_hitChisq->Fill(timedt.localT029(),timedt.hitChisq29());
	  dttime_localT0_hitChisq->Fill(timedt.localT030(),timedt.hitChisq30());
	  dttime_localT0_hitChisq->Fill(timedt.localT031(),timedt.hitChisq31());

	  //find hits that pass chi-squared cuts                                                                                                                     
	  for (int x=0; x<1000; x++) {
	    if (timedt.hitChisq0()>0. && timedt.hitChisq0()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq1()>0. && timedt.hitChisq1()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq2()>0. && timedt.hitChisq2()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq3()>0. && timedt.hitChisq3()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq4()>0. && timedt.hitChisq4()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq5()>0. && timedt.hitChisq5()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq6()>0. && timedt.hitChisq6()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq7()>0. && timedt.hitChisq7()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq8()>0. && timedt.hitChisq8()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq9()>0. && timedt.hitChisq9()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq10()>0. && timedt.hitChisq10()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq11()>0. && timedt.hitChisq11()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq12()>0. && timedt.hitChisq12()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq13()>0. && timedt.hitChisq13()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq14()>0. && timedt.hitChisq14()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq15()>0. && timedt.hitChisq15()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq16()>0. && timedt.hitChisq16()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq17()>0. && timedt.hitChisq17()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq18()>0. && timedt.hitChisq18()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq19()>0. && timedt.hitChisq19()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq20()>0. && timedt.hitChisq20()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq21()>0. && timedt.hitChisq21()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq22()>0. && timedt.hitChisq22()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq23()>0. && timedt.hitChisq23()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq24()>0. && timedt.hitChisq24()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq25()>0. && timedt.hitChisq25()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq26()>0. && timedt.hitChisq26()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq27()>0. && timedt.hitChisq27()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq28()>0. && timedt.hitChisq28()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq29()>0. && timedt.hitChisq29()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq30()>0. && timedt.hitChisq30()<1.0*x/10) nevts_passHitChisq[x]++;
	    if (timedt.hitChisq31()>0. && timedt.hitChisq31()<1.0*x/10) nevts_passHitChisq[x]++;
	  }

	  if (timedt.hitChisq0()>0.) nhits++;
	  if (timedt.hitChisq1()>0.) nhits++;
	  if (timedt.hitChisq2()>0.) nhits++;
	  if (timedt.hitChisq3()>0.) nhits++;
	  if (timedt.hitChisq4()>0.) nhits++;
	  if (timedt.hitChisq5()>0.) nhits++;
	  if (timedt.hitChisq6()>0.) nhits++;
	  if (timedt.hitChisq7()>0.) nhits++;
	  if (timedt.hitChisq8()>0.) nhits++;
	  if (timedt.hitChisq9()>0.) nhits++;
	  if (timedt.hitChisq10()>0.) nhits++;
	  if (timedt.hitChisq11()>0.) nhits++;
	  if (timedt.hitChisq12()>0.) nhits++;
	  if (timedt.hitChisq13()>0.) nhits++;
	  if (timedt.hitChisq14()>0.) nhits++;
	  if (timedt.hitChisq15()>0.) nhits++;
	  if (timedt.hitChisq16()>0.) nhits++;
	  if (timedt.hitChisq17()>0.) nhits++;
	  if (timedt.hitChisq18()>0.) nhits++;
	  if (timedt.hitChisq19()>0.) nhits++;
	  if (timedt.hitChisq20()>0.) nhits++;
	  if (timedt.hitChisq21()>0.) nhits++;
	  if (timedt.hitChisq22()>0.) nhits++;
	  if (timedt.hitChisq23()>0.) nhits++;
	  if (timedt.hitChisq24()>0.) nhits++;
	  if (timedt.hitChisq25()>0.) nhits++;
	  if (timedt.hitChisq26()>0.) nhits++;
	  if (timedt.hitChisq27()>0.) nhits++;
	  if (timedt.hitChisq28()>0.) nhits++;
	  if (timedt.hitChisq29()>0.) nhits++;
	  if (timedt.hitChisq30()>0.) nhits++;
	  if (timedt.hitChisq31()>0.) nhits++;

	  if(timedt.invbetaLS()<0.){
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT00(),timedt.hitChisq0());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT01(),timedt.hitChisq1());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT02(),timedt.hitChisq2());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT03(),timedt.hitChisq3());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT04(),timedt.hitChisq4());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT05(),timedt.hitChisq5());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT06(),timedt.hitChisq6());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT07(),timedt.hitChisq7());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT08(),timedt.hitChisq8());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT09(),timedt.hitChisq9());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT010(),timedt.hitChisq10());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT011(),timedt.hitChisq11());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT012(),timedt.hitChisq12());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT013(),timedt.hitChisq13());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT014(),timedt.hitChisq14());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT015(),timedt.hitChisq15());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT016(),timedt.hitChisq16());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT017(),timedt.hitChisq17());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT018(),timedt.hitChisq18());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT019(),timedt.hitChisq19());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT020(),timedt.hitChisq20());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT021(),timedt.hitChisq21());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT022(),timedt.hitChisq22());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT023(),timedt.hitChisq23());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT024(),timedt.hitChisq24());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT025(),timedt.hitChisq25());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT026(),timedt.hitChisq26());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT027(),timedt.hitChisq27());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT028(),timedt.hitChisq28());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT029(),timedt.hitChisq29());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT030(),timedt.hitChisq30());
	    dttime_localT0_hitChisq_LowInversebetaLS->Fill(timedt.localT031(),timedt.hitChisq31());
	    
	    //find hits that pass chi-squared cuts                                                                                                                     
	    for (int x=0; x<1000; x++) {
	      if (timedt.hitChisq0()>0. && timedt.hitChisq0()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq1()>0. && timedt.hitChisq1()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq2()>0. && timedt.hitChisq2()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq3()>0. && timedt.hitChisq3()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq4()>0. && timedt.hitChisq4()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq5()>0. && timedt.hitChisq5()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq6()>0. && timedt.hitChisq6()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq7()>0. && timedt.hitChisq7()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq8()>0. && timedt.hitChisq8()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq9()>0. && timedt.hitChisq9()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq10()>0. && timedt.hitChisq10()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq11()>0. && timedt.hitChisq11()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq12()>0. && timedt.hitChisq12()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq13()>0. && timedt.hitChisq13()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq14()>0. && timedt.hitChisq14()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq15()>0. && timedt.hitChisq15()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq16()>0. && timedt.hitChisq16()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq17()>0. && timedt.hitChisq17()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq18()>0. && timedt.hitChisq18()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq19()>0. && timedt.hitChisq19()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq20()>0. && timedt.hitChisq20()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq21()>0. && timedt.hitChisq21()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq22()>0. && timedt.hitChisq22()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq23()>0. && timedt.hitChisq23()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq24()>0. && timedt.hitChisq24()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq25()>0. && timedt.hitChisq25()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq26()>0. && timedt.hitChisq26()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq27()>0. && timedt.hitChisq27()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq28()>0. && timedt.hitChisq28()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq29()>0. && timedt.hitChisq29()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq30()>0. && timedt.hitChisq30()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	      if (timedt.hitChisq31()>0. && timedt.hitChisq31()<1.0*x/10) nevts_passHitChisq_LowInversebetaLS[x]++;
	    }
	    
	    if (timedt.hitChisq0()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq1()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq2()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq3()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq4()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq5()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq6()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq7()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq8()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq9()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq10()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq11()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq12()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq13()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq14()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq15()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq16()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq17()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq18()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq19()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq20()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq21()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq22()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq23()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq24()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq25()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq26()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq27()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq28()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq29()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq30()>0.) nhits_LowInversebetaLS++;
	    if (timedt.hitChisq31()>0.) nhits_LowInversebetaLS++;
	    
	  }//end of if invbetaLS<0
	  
	  if (timedt.inverseBetaErr()>0.)
	    hi_dttime_ibt_pull->Fill((timedt.inverseBeta()-1.)/timedt.inverseBetaErr());
	  if (timedt.freeInverseBetaErr()>0.)    
	    hi_dttime_fib_pull->Fill((timedt.freeInverseBeta()-1.)/timedt.freeInverseBetaErr());
	  if (timedt.timeAtIpInOutErr()>0.)
	    hi_dttime_vtx_pull->Fill(timedt.timeAtIpInOut()/timedt.timeAtIpInOutErr());
	  if (timedt.timeAtIpOutInErr()>0.)
	    hi_dttime_vtxr_pull->Fill(timedt.timeAtIpOutIn()/timedt.timeAtIpOutInErr());
	  
	  if (timecsc.nDof()>theCscCut)
	    hi_dtcsc_vtx->Fill(timedt.timeAtIpInOut()-timecsc.timeAtIpInOut());
	  if (imuon->isEnergyValid()) {
	    if (muonE.emMax>0.25) hi_dtecal_vtx->Fill(timedt.timeAtIpInOut()-muonE.ecal_time);
	    if (muonE.hadMax>0.25) hi_dthcal_vtx->Fill(timedt.timeAtIpInOut()-muonE.hcal_time);
	  }    

	  }//end of number of DT chambers cut
	  //}//end of invbetaLS cut	 
	  //}//end of phi cut
	}//end of if sufficient DT DOF       
      }// end of pt cut
    }//end of if sta track exists


    if (timecsc.nDof()>theCscCut) {
      //if (debug) {
      //std::cout << "         CSC nDof: " << timecsc.nDof() << std::endl;
      //std::cout << "         CSC Time: " << timecsc.timeAtIpInOut() << " +/- " << timecsc.inverseBetaErr() << std::endl;
      //std::cout << "        CSC FreeB: " << timecsc.freeInverseBeta() << " +/- " << timecsc.freeInverseBetaErr() << std::endl;
      //}
      hi_csctime_ibt->Fill(timecsc.inverseBeta());
      hi_csctime_ibt_pt->Fill(imuon->pt(),timecsc.inverseBeta());
      hi_csctime_ibt_err->Fill(timecsc.inverseBetaErr());
      hi_csctime_fib->Fill(timecsc.freeInverseBeta());
      hi_csctime_fib_err->Fill(timecsc.freeInverseBetaErr());
      hi_csctime_vtx->Fill(timecsc.timeAtIpInOut());
      hi_csctime_vtx_err->Fill(timecsc.timeAtIpInOutErr());
      hi_csctime_vtxr->Fill(timecsc.timeAtIpOutIn());
      hi_csctime_vtxr_err->Fill(timecsc.timeAtIpOutInErr());

      if (timec.inverseBetaErr()>0.)
        hi_csctime_ibt_pull->Fill((timecsc.inverseBeta()-1.)/timecsc.inverseBetaErr());
      if (timecsc.freeInverseBetaErr()>0.)    
        hi_csctime_fib_pull->Fill((timecsc.freeInverseBeta()-1.)/timecsc.freeInverseBetaErr());
      if (timecsc.timeAtIpInOutErr()>0.)
        hi_csctime_vtx_pull->Fill(timecsc.timeAtIpInOut()/timecsc.timeAtIpInOutErr());
      if (timecsc.timeAtIpOutInErr()>0.)
        hi_csctime_vtxr_pull->Fill(timecsc.timeAtIpOutIn()/timecsc.timeAtIpOutInErr());

      if (imuon->isEnergyValid()) {
        if (muonE.emMax>0.25) hi_ecalcsc_vtx->Fill(muonE.ecal_time-timecsc.timeAtIpInOut());
        if (muonE.hadMax>0.25) hi_hcalcsc_vtx->Fill(muonE.hcal_time-timecsc.timeAtIpInOut());
      }
    } //end of if sufficient CSC DOF
    
    if (timec.nDof()>0) {
      //if (debug) {
      //std::cout << "    Combined nDof: " << timec.nDof() << std::endl;
      //std::cout << "    Combined Time: " << timec.timeAtIpInOut() << " +/- " << timec.inverseBetaErr() << std::endl;
      //std::cout << "   Combined FreeB: " << timec.freeInverseBeta() << " +/- " << timec.freeInverseBetaErr() << std::endl;
      //}
      hi_cmbtime_ibt->Fill(timec.inverseBeta());
      hi_cmbtime_ibt_pt->Fill(imuon->pt(),timec.inverseBeta());
      hi_cmbtime_ibt_err->Fill(timec.inverseBetaErr());
      hi_cmbtime_fib->Fill(timec.freeInverseBeta());
      hi_cmbtime_fib_err->Fill(timec.freeInverseBetaErr());
      hi_cmbtime_vtx->Fill(timec.timeAtIpInOut());
      hi_cmbtime_vtx_err->Fill(timec.timeAtIpInOutErr());
      hi_cmbtime_vtxr->Fill(timec.timeAtIpOutIn());
      hi_cmbtime_vtxr_err->Fill(timec.timeAtIpOutInErr());

      if (timec.inverseBetaErr()>0.)
        hi_cmbtime_ibt_pull->Fill((timec.inverseBeta()-1.)/timec.inverseBetaErr());
      if (timec.freeInverseBetaErr()>0.)    
        hi_cmbtime_fib_pull->Fill((timec.freeInverseBeta()-1.)/timec.freeInverseBetaErr());
      if (timec.timeAtIpInOutErr()>0.)
        hi_cmbtime_vtx_pull->Fill(timec.timeAtIpInOut()/timec.timeAtIpInOutErr());
      if (timec.timeAtIpOutInErr()>0.)
        hi_cmbtime_vtxr_pull->Fill(timec.timeAtIpOutIn()/timec.timeAtIpOutInErr());
    }

    imucount++;
  }//end of loop over muons

  if(igoodmucount>0) hi_dt_nmuons->Fill(igoodmucount);
}


// ------------ method called once each job just before starting event loop  ------------
void 
MuonTimingValidatorDelayedMuons::beginJob()
{

  for (int x=0; x<1000; x++){
    nevts_passHitChisq[x]=0;
    nevts_passHitChisq_LowInversebetaLS[x]=0;
  }
  nhits=0;
  nhits_LowInversebetaLS=0;

  hFile = new TFile( out.c_str(), open.c_str() );
  hFile->cd();
  
  effStyle = new TStyle("effStyle","Efficiency Study Style");   
  effStyle->SetCanvasBorderMode(0);
  effStyle->SetPadBorderMode(1);
  effStyle->SetOptTitle(0);
  effStyle->SetStatFont(42);
  effStyle->SetTitleFont(22);
  effStyle->SetCanvasColor(10);
  effStyle->SetPadColor(0);
  effStyle->SetLabelFont(42,"x");
  effStyle->SetLabelFont(42,"y");
  effStyle->SetHistFillStyle(1001);
  effStyle->SetHistFillColor(0);
  effStyle->SetOptStat(0);
  effStyle->SetOptFit(0111);
  effStyle->SetStatH(0.05);
  
  hi_sta_pt   = new TH1F("hi_sta_pt","P_{T}^{STA}",theNBins,0.0,theMaxPtres);
  hi_tk_pt   = new TH1F("hi_tk_pt","P_{T}^{TK}",theNBins,0.0,theMaxPtres);
  hi_glb_pt   = new TH1F("hi_glb_pt","P_{T}^{GLB}",theNBins,0.0,theMaxPtres);
  
  hi_sta_phi = new TH1F("hi_sta_phi","#phi^{STA}",theNBins,-3.0,3.);
  hi_tk_phi  = new TH1F("hi_tk_phi","#phi^{TK}",theNBins,-3.0,3.);
  hi_glb_phi = new TH1F("hi_glb_phi","#phi^{GLB}",theNBins,-3.0,3.);
  
  hi_mutime_vtx = new TH1F("hi_mutime_vtx","Time at Vertex (inout)",theNBins,-25.*theScale,25.*theScale);
  hi_mutime_vtx_err = new TH1F("hi_mutime_vtx_err","Time at Vertex Error (inout)",theNBins,0.,25.0);
  
  hi_dtcsc_vtx = new TH1F("hi_dtcsc_vtx","Time at Vertex (DT-CSC)",theNBins,-25.*theScale,25.*theScale);
  hi_dtecal_vtx = new TH1F("hi_dtecal_vtx","Time at Vertex (DT-ECAL)",theNBins,-25.*theScale,25.*theScale);
  hi_ecalcsc_vtx = new TH1F("hi_ecalcsc_vtx","Time at Vertex (ECAL-CSC)",theNBins,-25.*theScale,25.*theScale);
  hi_dthcal_vtx = new TH1F("hi_dthcal_vtx","Time at Vertex (DT-HCAL)",theNBins,-25.*theScale,25.*theScale);
  hi_hcalcsc_vtx = new TH1F("hi_hcalcsc_vtx","Time at Vertex (HCAL-CSC)",theNBins,-25.*theScale,25.*theScale);
  hi_hcalecal_vtx = new TH1F("hi_hcalecal_vtx","Time at Vertex (HCAL-ECAL)",theNBins,-25.*theScale,25.*theScale);
  
  hi_cmbtime_ibt = new TH1F("hi_cmbtime_ibt","Inverse Beta",theNBins,0.,1.6);
  hi_cmbtime_ibt_pt = new TH2F("hi_cmbtime_ibt_pt","P{T} vs Inverse Beta",theNBins,0.0,theMaxPtres,theNBins,0.7,2.0);
  hi_cmbtime_ibt_err = new TH1F("hi_cmbtime_ibt_err","Inverse Beta Error",theNBins,0.,1.0);
  hi_cmbtime_fib = new TH1F("hi_cmbtime_fib","Free Inverse Beta",theNBins,-5.*theScale,7.*theScale);
  hi_cmbtime_fib_err = new TH1F("hi_cmbtime_fib_err","Free Inverse Beta Error",theNBins,0,5.);
  hi_cmbtime_vtx = new TH1F("hi_cmbtime_vtx","Time at Vertex (inout)",theNBins,-25.*theScale,25.*theScale);
  hi_cmbtime_vtx_err = new TH1F("hi_cmbtime_vtx_err","Time at Vertex Error (inout)",theNBins,0.,25.0);
  hi_cmbtime_vtxr = new TH1F("hi_cmbtime_vtxR","Time at Vertex (inout)",theNBins,0.,75.*theScale);
  hi_cmbtime_vtxr_err = new TH1F("hi_cmbtime_vtxR_err","Time at Vertex Error (inout)",theNBins,0.,25.0);
  hi_cmbtime_ibt_pull = new TH1F("hi_cmbtime_ibt_pull","Inverse Beta Pull",theNBins,-5.,5.0);
  hi_cmbtime_fib_pull = new TH1F("hi_cmbtime_fib_pull","Free Inverse Beta Pull",theNBins,-5.,5.0);
  hi_cmbtime_vtx_pull = new TH1F("hi_cmbtime_vtx_pull","Time at Vertex Pull (inout)",theNBins,-5.,5.0);
  hi_cmbtime_vtxr_pull = new TH1F("hi_cmbtime_vtxR_pull","Time at Vertex Pull (inout)",theNBins,-5.,5.0);
  
  hi_cmbtime_ndof = new TH1F("hi_cmbtime_ndof","Number of timing measurements",48,0.,48.0);
  
  hi_dttime_ibt = new TH1F("hi_dttime_ibt","DT Inverse Beta",theNBins,0.,1.6);
  hi_dttime_ibt_pt = new TH2F("hi_dttime_ibt_pt","P{T} vs DT Inverse Beta",theNBins,0.0,theMaxPtres,theNBins,0.,2.0);
  hi_dttime_ibt_err = new TH1F("hi_dttime_ibt_err","DT Inverse Beta Error",theNBins,0.,0.3);
  hi_dttime_ibt_ibt_err = new TH2F("hi_dttime_ibt_ibt_err","DT Inverse Beta vs Inverse Beta Error",theNBins,0,2.0,theNBins,0.,0.3);
  hi_dttime_fib = new TH1F("hi_dttime_fib","DT Free Inverse Beta",theNBins,-5.*theScale,7.*theScale);
  hi_dttime_fib_err = new TH1F("hi_dttime_fib_err","DT Free Inverse Beta Error",theNBins,0,5.);
  hi_dttime_fib_fib_err = new TH2F("hi_dttime_fib_fib_err","DT Free Inverse Beta vs Free Inverse Beta Error",theNBins,-5.*theScale,7.*theScale,theNBins,0,5.);
  hi_dttime_vtx = new TH1F("hi_dttime_vtx","DT Time at Vertex (inout)",theNBins,-50,50);
  hi_dttime_vtx_err = new TH1F("hi_dttime_vtx_err","DT Time at Vertex Error (inout)",theNBins,0.,10.0);
  hi_dttime_vtxr = new TH1F("hi_dttime_vtxR","DT Time at Vertex (inout)",theNBins,0.,100);
  hi_dttime_vtxr_err = new TH1F("hi_dttime_vtxR_err","DT Time at Vertex Error (inout)",theNBins,0.,10.0);
  hi_dttime_ibt_pull = new TH1F("hi_dttime_ibt_pull","DT Inverse Beta Pull",theNBins,-5.,5.0);
  hi_dttime_fib_pull = new TH1F("hi_dttime_fib_pull","DT Free Inverse Beta Pull",theNBins,-5.,5.0);
  hi_dttime_vtx_pull = new TH1F("hi_dttime_vtx_pull","DT Time at Vertex Pull (inout)",theNBins,-5.,5.0);
  hi_dttime_vtxr_pull = new TH1F("hi_dttime_vtxR_pull","DT Time at Vertex Pull (inout)",theNBins,-5.,5.0);
  hi_dttime_errdiff = new TH1F("hi_dttime_errdiff","DT Time at Vertex inout-outin error difference",theNBins,-2.*theScale,2.*theScale);
  hi_dttime_ndof = new TH1F("hi_dttime_ndof","Number of DT timing measurements",50,0.,50.0);
  hi_dt_nmuons   = new TH1F("hi_dt_nmuons","Number of Muons",10,0.0,10);
  
  dttime_nHits_hist = new TH1F("dttime_nHits_hist","Number of Hits",40,0,40);
  dttime_aveHitTimeError_hist = new TH1F("dttime_aveHitTimeError_hist","Average Hit Time Error",40,0,20);
  dttime_invbetaLS_hist = new TH1F("dttime_invbetaLS_hist","LS Inverse Beta",8000,-10,10);
  dttime_invbetaLSError_hist = new TH1F("dttime_invbetaLSError_hist","LS Inverse Beta Error",100,0,5);
  dttime_yIntercept_hist = new TH1F("dttime_yIntercept_hist","Y-Intercept",200,-100,100);
  dttime_yInterceptError_hist = new TH1F("dttime_yInterceptError_hist","Y-Intercept Error",100,0,100);
  dttime_chi2Dof_hist = new TH1F("dttime_chi2Dof_hist","Chisq/DOF",500,0,500);
  sta_phi_dttime_invbetaLS_hist = new TH2F("sta_phi_dttime_invbetaLS_hist","Phi vs LS Inverse Beta",64,-6.2832,6.2832,200,-10,10);
  dttime_invbetaLS_chi2Dof_hist = new TH2F("dttime_invbetaLS_chi2Dof_hist","LS Inverse Beta  vs chisq/dof",200,-10,10,500,0,500);
  dttime_yIntercept_chi2Dof_hist = new TH2F("dttime_yIntercept_chi2Dof_hist","Y-intercept vs chisq/dof",200,-100,100,500,0,500);
  dttime_invbetaLSError_chi2Dof_hist = new TH2F("dttime_invbetaLSError_chi2Dof_hist","LS Inverse Beta Error vs chisq/dof",100,0,5,500,0,500);
  dttime_yInterceptError_chi2Dof_hist = new TH2F("dttime_yInterceptError_chi2Dof_hist","Y-Intercept Error  vs chisq/dof",100,0,100,500,0,500);
  dttime_nHits_invbetaLS_hist = new TH2F("dttime_nHits_invbetaLS_hist","Number of Hits vs LS Inverse Beta",40,0,40,8000,-10,10);
  dttime_nHits_invbetaLSError_hist = new TH2F("dttime_nHits_invbetaLSError_hist","Number of Hits vs LS Inverse Beta Error",40,0,40,100,0,5);
  
  dttime_invbetaLS_fib = new TH2F("dttime_invbetaLS_fib","LS Inverse Beta vs Free Inverse Beta",8000,-10,10,theNBins,-5,5);
  dttime_invbetaLSError_fiberr = new TH2F("dttime_invbetaLSError_fiberr","LS Inverse Beta Error vs Free Inverse Beta Error",100,0,5,100,0,5);
  
  dttime_localT0_hitChisq = new TH2F("dttime_localT0_hitChisq","Time vs Hit Chisq",800,-100,100,1000,0,100);
  dttime_localT0_hitChisq_LowInversebetaLS = new TH2F("dttime_localT0_hitChisq_LowInversebetaLS","Time vs Hit Chisq",800,-100,100,1000,0,100);
  
  hi_csctime_ibt = new TH1F("hi_csctime_ibt","CSC Inverse Beta",theNBins,0.,1.6);
   hi_csctime_ibt_pt = new TH2F("hi_csctime_ibt_pt","P{T} vs CSC Inverse Beta",theNBins,0.0,theMaxPtres,theNBins,0.7,2.0);
   hi_csctime_ibt_err = new TH1F("hi_csctime_ibt_err","CSC Inverse Beta Error",theNBins,0.,1.0);
   hi_csctime_fib = new TH1F("hi_csctime_fib","CSC Free Inverse Beta",theNBins,-5.*theScale,7.*theScale);
   hi_csctime_fib_err = new TH1F("hi_csctime_fib_err","CSC Free Inverse Beta Error",theNBins,0,5.);
   hi_csctime_vtx = new TH1F("hi_csctime_vtx","CSC Time at Vertex (inout)",theNBins,-25.*theScale,25.*theScale);
   hi_csctime_vtx_err = new TH1F("hi_csctime_vtx_err","CSC Time at Vertex Error (inout)",theNBins,0.,25.0);
   hi_csctime_vtxr = new TH1F("hi_csctime_vtxR","CSC Time at Vertex (inout)",theNBins,0.,75.*theScale);
   hi_csctime_vtxr_err = new TH1F("hi_csctime_vtxR_err","CSC Time at Vertex Error (inout)",theNBins,0.,25.0);
   hi_csctime_ibt_pull = new TH1F("hi_csctime_ibt_pull","CSC Inverse Beta Pull",theNBins,-5.,5.0);
   hi_csctime_fib_pull = new TH1F("hi_csctime_fib_pull","CSC Free Inverse Beta Pull",theNBins,-5.,5.0);
   hi_csctime_vtx_pull = new TH1F("hi_csctime_vtx_pull","CSC Time at Vertex Pull (inout)",theNBins,-5.,5.0);
   hi_csctime_vtxr_pull = new TH1F("hi_csctime_vtxR_pull","CSC Time at Vertex Pull (inout)",theNBins,-5.,5.0);

   hi_csctime_ndof = new TH1F("hi_csctime_ndof","Number of CSC timing measurements",48,0.,48.0);

   hi_ecal_time = new TH1F("hi_ecal_time","ECAL Time at Vertex (inout)",theNBins,-40.*theScale,40.*theScale);
   hi_ecal_time_err = new TH1F("hi_ecal_time_err","ECAL Time at Vertex Error",theNBins,0.,20.0);
   hi_ecal_time_pull = new TH1F("hi_ecal_time_pull","ECAL Time at Vertex Pull",theNBins,-7.0,7.0);
   hi_ecal_time_ecut = new TH1F("hi_ecal_time_ecut","ECAL Time at Vertex (inout) after energy cut",theNBins,-20.*theScale,20.*theScale);
   hi_ecal_energy = new TH1F("hi_ecal_energy","ECAL max energy in 5x5 crystals",theNBins,.0,5.0);

   hi_hcal_time = new TH1F("hi_hcal_time","HCAL Time at Vertex (inout)",theNBins,-40.*theScale,40.*theScale);
   hi_hcal_time_err = new TH1F("hi_hcal_time_err","HCAL Time at Vertex Error",theNBins,0.,20.0);
   hi_hcal_time_pull = new TH1F("hi_hcal_time_pull","HCAL Time at Vertex Pull",theNBins,-7.0,7.0);
   hi_hcal_time_ecut = new TH1F("hi_hcal_time_ecut","HCAL Time at Vertex (inout) after energy cut",theNBins,-20.*theScale,20.*theScale);
   hi_hcal_energy = new TH1F("hi_hcal_energy","HCAL max energy in 5x5 crystals",theNBins,.0,5.0);

   hi_sta_eta = new TH1F("hi_sta_eta","#eta^{STA}",theNBins,-1.*theMaxEta,theMaxEta);
   hi_tk_eta  = new TH1F("hi_tk_eta","#eta^{TK}",theNBins,-1.*theMaxEta,theMaxEta);
   hi_glb_eta = new TH1F("hi_glb_eta","#eta^{GLB}",theNBins,-1.*theMaxEta,theMaxEta);

}

// ------------ method called once each job just after ending the event loop  ------------
void 
MuonTimingValidatorDelayedMuons::endJob() {

  hFile->cd();

  gROOT->SetStyle("effStyle");

  hi_tk_pt->Write();
  hi_glb_pt->Write();

  hi_tk_phi->Write();
  hi_glb_phi->Write();

  hi_tk_eta->Write();
  hi_glb_eta->Write();

  hi_mutime_vtx->Write();
  hi_mutime_vtx_err->Write();

  hFile->mkdir("differences");
  hFile->cd("differences");

  hi_dtcsc_vtx->Write();
  hi_dtecal_vtx->Write();
  hi_ecalcsc_vtx->Write();
  hi_dthcal_vtx->Write();
  hi_hcalcsc_vtx->Write();
  hi_hcalecal_vtx->Write();

  hFile->cd();
  hFile->mkdir("combined");
  hFile->cd("combined");

  hi_cmbtime_ibt->Write();
  hi_cmbtime_ibt_pt->Write();
  hi_cmbtime_ibt_err->Write();
  hi_cmbtime_fib->Write();
  hi_cmbtime_fib_err->Write();
  hi_cmbtime_vtx->Write();
  hi_cmbtime_vtx_err->Write();
  hi_cmbtime_vtxr->Write();
  hi_cmbtime_vtxr_err->Write();
  hi_cmbtime_ibt_pull->Write();
  hi_cmbtime_fib_pull->Write();
  hi_cmbtime_vtx_pull->Write();
  hi_cmbtime_vtxr_pull->Write();
  hi_cmbtime_ndof->Write();

  hFile->cd();
  hFile->mkdir("dt");
  hFile->cd("dt");

  hi_sta_pt->Write();
  hi_sta_phi->Write();
  hi_sta_eta->Write();

  hi_dttime_ibt->Write();
  hi_dttime_ibt_pt->Write();
  hi_dttime_ibt_err->Write();
  hi_dttime_ibt_ibt_err->Write();
  hi_dttime_fib->Write();
  hi_dttime_fib_err->Write();
  hi_dttime_fib_fib_err->Write();
  hi_dttime_vtx->Write();
  hi_dttime_vtx_err->Write();
  hi_dttime_vtxr->Write();
  hi_dttime_vtxr_err->Write();
  hi_dttime_ibt_pull->Write();
  hi_dttime_fib_pull->Write();
  hi_dttime_vtx_pull->Write();
  hi_dttime_vtxr_pull->Write();
  hi_dttime_errdiff->Write();
  hi_dttime_ndof->Write();
  hi_dt_nmuons->Write();
  
  dttime_nHits_hist->Write();
  dttime_aveHitTimeError_hist->Write();
  dttime_invbetaLS_hist->Write();
  dttime_invbetaLSError_hist->Write();
  dttime_yIntercept_hist->Write();
  dttime_yInterceptError_hist->Write();
  dttime_chi2Dof_hist->Write();
  sta_phi_dttime_invbetaLS_hist->Write();
  dttime_invbetaLS_chi2Dof_hist->Write();
  dttime_yIntercept_chi2Dof_hist->Write();
  dttime_invbetaLSError_chi2Dof_hist->Write();
  dttime_yInterceptError_chi2Dof_hist->Write();
  dttime_nHits_invbetaLS_hist->Write();
  dttime_nHits_invbetaLSError_hist->Write();

  dttime_invbetaLS_fib->Write();
  dttime_invbetaLSError_fiberr->Write();

  dttime_localT0_hitChisq->Write();
  dttime_localT0_hitChisq_LowInversebetaLS->Write();

  hFile->cd();
  hFile->mkdir("csc");
  hFile->cd("csc");

  hi_csctime_ibt->Write();
  hi_csctime_ibt_pt->Write();
  hi_csctime_ibt_err->Write();
  hi_csctime_fib->Write();
  hi_csctime_fib_err->Write();
  hi_csctime_vtx->Write();
  hi_csctime_vtx_err->Write();
  hi_csctime_vtxr->Write();
  hi_csctime_vtxr_err->Write();
  hi_csctime_ibt_pull->Write();
  hi_csctime_fib_pull->Write();
  hi_csctime_vtx_pull->Write();
  hi_csctime_vtxr_pull->Write();
  hi_csctime_ndof->Write();

  hFile->cd();
  hFile->mkdir("ecal");
  hFile->cd("ecal");

  hi_ecal_time->Write();
  hi_ecal_time_ecut->Write();
  hi_ecal_time_err->Write();
  hi_ecal_time_pull->Write();
  hi_ecal_energy->Write();

  hFile->cd();
  hFile->mkdir("hcal");
  hFile->cd("hcal");

  hi_hcal_time->Write();
  hi_hcal_time_ecut->Write();
  hi_hcal_time_err->Write();
  hi_hcal_time_pull->Write();
  hi_hcal_energy->Write();

  hFile->Write();

  //write out percentage of events that pass chi-squared cuts to text file
  TString outfile_ = "percent_passHitChisq_" + txtout + ".txt";
  TString outfile_LowInversebetaLS_ = "percent_passHitChisq_LowInversebetaLS_" + txtout + ".txt";
  std::ofstream outfile(outfile_);
  std::ofstream outfile_LowInversebetaLS(outfile_LowInversebetaLS_);
  for (int x=0; x<1000; x++) {                                                                                                                                                      
    outfile<<1.0*nevts_passHitChisq[x]/nhits<<" ";
    outfile_LowInversebetaLS<<1.0*nevts_passHitChisq_LowInversebetaLS[x]/nhits_LowInversebetaLS<<" ";
  }

}

float 
MuonTimingValidatorDelayedMuons::calculateDistance(const math::XYZVector& vect1, const math::XYZVector& vect2) {
  float dEta = vect1.eta() - vect2.eta();
  float dPhi = fabs(Geom::Phi<float>(vect1.phi()) - Geom::Phi<float>(vect2.phi()));
  float distance = sqrt(pow(dEta,2) + pow(dPhi,2) );

  return distance;
}

//
// return h1/h2 with recalculated errors
//
TH1F* MuonTimingValidatorDelayedMuons::divideErr(TH1F* h1, TH1F* h2, TH1F* hout) {

  hout->Reset();
  hout->Divide(h1,h2,1.,1.,"B");

  for (int i = 0; i <= hout->GetNbinsX()+1; i++ ) {
    Float_t tot   = h2->GetBinContent(i) ;
    Float_t tot_e = h2->GetBinError(i);
    Float_t eff = hout->GetBinContent(i) ;
    Float_t Err = 0.;
    if (tot > 0) Err = tot_e / tot * sqrt( eff* (1-eff) );
    if (eff == 1. || isnan(Err) || !std::isfinite(Err) ) Err=1.e-3;
    hout->SetBinError(i, Err);
  }
  return hout;
}

//define this as a plug-in
DEFINE_FWK_MODULE(MuonTimingValidatorDelayedMuons);
