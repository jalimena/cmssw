//
// Package:    MuonTimingFillerDelayedMuons
// Class:      MuonTimingFillerDelayedMuons
// 
/**\class MuonTimingFillerDelayedMuons MuonTimingFillerDelayedMuons.cc RecoMuon/MuonIdentification/src/MuonTimingFillerDelayedMuons.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Piotr Traczyk, CERN
//         Created:  Mon Mar 16 12:27:22 CET 2009
// $Id: MuonTimingFillerDelayedMuons.cc,v 1.13 2011/02/24 15:41:53 farrell3 Exp $
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

#include "DataFormats/MuonReco/interface/Muon.h" 
#include "DataFormats/MuonReco/interface/MuonFwd.h" 
#include "DataFormats/MuonReco/interface/MuonTimeExtra.h"
#include "DataFormats/MuonReco/interface/MuonTimeExtraMap.h"

#include "RecoMuon/MuonIdentification/interface/MuonTimingFillerDelayedMuons.h"
#include "RecoMuon/MuonIdentification/interface/TimeMeasurementSequence.h"
#include "DataFormats/EcalDetId/interface/EcalSubdetector.h"

//
// constructors and destructor
//
MuonTimingFillerDelayedMuons::MuonTimingFillerDelayedMuons(const edm::ParameterSet& iConfig, edm::ConsumesCollector&& iC)
{
   // Load parameters for the DTTimingExtractor
   edm::ParameterSet dtTimingParameters = iConfig.getParameter<edm::ParameterSet>("DTTimingParameters");
   theDTTimingExtractor_ = new DTTimingExtractorDelayedMuons(dtTimingParameters,iC);

   // Load parameters for the CSCTimingExtractor
   edm::ParameterSet cscTimingParameters = iConfig.getParameter<edm::ParameterSet>("CSCTimingParameters");
   theCSCTimingExtractor_ = new CSCTimingExtractorDelayedMuons(cscTimingParameters,iC);
   
   errorEB_ = iConfig.getParameter<double>("ErrorEB");
   errorEE_ = iConfig.getParameter<double>("ErrorEE");
   ecalEcut_ = iConfig.getParameter<double>("EcalEnergyCut");
   
   useDT_ = iConfig.getParameter<bool>("UseDT");
   useCSC_ = iConfig.getParameter<bool>("UseCSC");
   useECAL_ = iConfig.getParameter<bool>("UseECAL");
   
}


MuonTimingFillerDelayedMuons::~MuonTimingFillerDelayedMuons()
{
  if (theDTTimingExtractor_) delete theDTTimingExtractor_;
  if (theCSCTimingExtractor_) delete theCSCTimingExtractor_;
}


//
// member functions
//

void 
MuonTimingFillerDelayedMuons::fillTiming( const reco::Muon& muon, reco::MuonTimeExtra& dtTime, reco::MuonTimeExtra& cscTime, reco::MuonTimeExtra& combinedTime, edm::Event& iEvent, const edm::EventSetup& iSetup )
{
  TimeMeasurementSequence dtTmSeq,cscTmSeq;

  if ( !(muon.combinedMuon().isNull()) ) {
    std::cout<<"doing combined muons"<<std::endl;
    theDTTimingExtractor_->fillTiming(dtTmSeq, muon.combinedMuon(), iEvent, iSetup);
    theCSCTimingExtractor_->fillTiming(cscTmSeq, muon.combinedMuon(), iEvent, iSetup);
  } else
  if ( !(muon.standAloneMuon().isNull()) ) {
      std::cout<<"doing SA muons"<<std::endl;
      theDTTimingExtractor_->fillTiming(dtTmSeq, muon.standAloneMuon(), iEvent, iSetup);
      theCSCTimingExtractor_->fillTiming(cscTmSeq, muon.standAloneMuon(), iEvent, iSetup);
    }
  
  // Fill DT-specific timing information block     
  std::cout<<"doing DT fillTimeFromMeasurements:"<<std::endl;
  fillTimeFromMeasurements(dtTmSeq, dtTime);

  // Fill CSC-specific timing information block     
  std::cout<<"doing CSC fillTimeFromMeasurements:"<<std::endl;
  fillTimeFromMeasurements(cscTmSeq, cscTime);
       
  // Combine the TimeMeasurementSequences from all subdetectors
  std::cout<<"combining Timing Sequences from all subdetectors:"<<std::endl;
  TimeMeasurementSequence combinedTmSeq;
  combineTMSequences(muon,dtTmSeq,cscTmSeq,combinedTmSeq);

  // add ECAL info
  std::cout<<"adding ecal time:"<<std::endl;
  if (useECAL_) addEcalTime(muon,combinedTmSeq);

  // Fill the master timing block
  std::cout<<"doing combined fillTimeFromMeasurements:"<<std::endl;
  fillTimeFromMeasurements(combinedTmSeq, combinedTime);
    
  LogTrace("MuonTime") << "Global 1/beta: " << combinedTime.inverseBeta() << " +/- " << combinedTime.inverseBetaErr()<<std::endl;
  LogTrace("MuonTime") << "  Free 1/beta: " << combinedTime.freeInverseBeta() << " +/- " << combinedTime.freeInverseBetaErr()<<std::endl;
  LogTrace("MuonTime") << "  Vertex time (in-out): " << combinedTime.timeAtIpInOut() << " +/- " << combinedTime.timeAtIpInOutErr()
                       << "  # of points: " << combinedTime.nDof() <<std::endl;
  LogTrace("MuonTime") << "  Vertex time (out-in): " << combinedTime.timeAtIpOutIn() << " +/- " << combinedTime.timeAtIpOutInErr()<<std::endl;
  LogTrace("MuonTime") << "  direction: "   << combinedTime.direction() << std::endl;     
}


void MuonTimingFillerDelayedMuons::fillTimeFromMeasurements( TimeMeasurementSequence tmSeq, reco::MuonTimeExtra &muTime ) {

  std::vector <double> x,y;
  double invbeta=0, invbetaerr=0;
  double vertexTime=0, vertexTimeErr=0, vertexTimeR=0, vertexTimeRErr=0;    
  double freeBeta, freeBetaErr, freeTime, freeTimeErr;

  double local_t0_0 = -999.;
  double local_t0_1 = -999.;
  double local_t0_2 = -999.;
  double local_t0_3 = -999.;
  double local_t0_4 = -999.;
  double local_t0_5 = -999.;
  double local_t0_6 = -999.;
  double local_t0_7 = -999.;
  double local_t0_8 = -999.;
  double local_t0_9 = -999.;
  double local_t0_10 = -999.;
  double local_t0_11 = -999.;
  double local_t0_12 = -999.;
  double local_t0_13 = -999.;
  double local_t0_14 = -999.;
  double local_t0_15 = -999.;
  double local_t0_16 = -999.;
  double local_t0_17 = -999.;
  double local_t0_18 = -999.;
  double local_t0_19 = -999.;
  double local_t0_20 = -999.;
  double local_t0_21 = -999.;
  double local_t0_22 = -999.;
  double local_t0_23 = -999.;
  double local_t0_24 = -999.;
  double local_t0_25 = -999.;
  double local_t0_26 = -999.;
  double local_t0_27 = -999.;
  double local_t0_28 = -999.;
  double local_t0_29 = -999.;
  double local_t0_30 = -999.;
  double local_t0_31 = -999.;

  double correctedTime_0 = -999.;
  double correctedTime_1 = -999.;
  double correctedTime_2 = -999.;
  double correctedTime_3 = -999.;
  double correctedTime_4 = -999.;
  double correctedTime_5 = -999.;
  double correctedTime_6 = -999.;
  double correctedTime_7 = -999.;
  double correctedTime_8 = -999.;
  double correctedTime_9 = -999.;
  double correctedTime_10 = -999.;
  double correctedTime_11 = -999.;
  double correctedTime_12 = -999.;
  double correctedTime_13 = -999.;
  double correctedTime_14 = -999.;
  double correctedTime_15 = -999.;
  double correctedTime_16 = -999.;
  double correctedTime_17 = -999.;
  double correctedTime_18 = -999.;
  double correctedTime_19 = -999.;
  double correctedTime_20 = -999.;
  double correctedTime_21 = -999.;
  double correctedTime_22 = -999.;
  double correctedTime_23 = -999.;
  double correctedTime_24 = -999.;
  double correctedTime_25 = -999.;
  double correctedTime_26 = -999.;
  double correctedTime_27 = -999.;
  double correctedTime_28 = -999.;
  double correctedTime_29 = -999.;
  double correctedTime_30 = -999.;
  double correctedTime_31 = -999.;

  double distance_0 = -999.;
  double distance_1 = -999.;
  double distance_2 = -999.;
  double distance_3 = -999.;
  double distance_4 = -999.;
  double distance_5 = -999.;
  double distance_6 = -999.;
  double distance_7 = -999.;
  double distance_8 = -999.;
  double distance_9 = -999.;
  double distance_10 = -999.;
  double distance_11 = -999.;
  double distance_12 = -999.;
  double distance_13 = -999.;
  double distance_14 = -999.;
  double distance_15 = -999.;
  double distance_16 = -999.;
  double distance_17 = -999.;
  double distance_18 = -999.;
  double distance_19 = -999.;
  double distance_20 = -999.;
  double distance_21 = -999.;
  double distance_22 = -999.;
  double distance_23 = -999.;
  double distance_24 = -999.;
  double distance_25 = -999.;
  double distance_26 = -999.;
  double distance_27 = -999.;
  double distance_28 = -999.;
  double distance_29 = -999.;
  double distance_30 = -999.;
  double distance_31 = -999.;

  double hitChisq_0 = -999.;
  double hitChisq_1 = -999.;
  double hitChisq_2 = -999.;
  double hitChisq_3 = -999.;
  double hitChisq_4 = -999.;
  double hitChisq_5 = -999.;
  double hitChisq_6 = -999.;
  double hitChisq_7 = -999.;
  double hitChisq_8 = -999.;
  double hitChisq_9 = -999.;
  double hitChisq_10 = -999.;
  double hitChisq_11 = -999.;
  double hitChisq_12 = -999.;
  double hitChisq_13 = -999.;
  double hitChisq_14 = -999.;
  double hitChisq_15 = -999.;
  double hitChisq_16 = -999.;
  double hitChisq_17 = -999.;
  double hitChisq_18 = -999.;
  double hitChisq_19 = -999.;
  double hitChisq_20 = -999.;
  double hitChisq_21 = -999.;
  double hitChisq_22 = -999.;
  double hitChisq_23 = -999.;
  double hitChisq_24 = -999.;
  double hitChisq_25 = -999.;
  double hitChisq_26 = -999.;
  double hitChisq_27 = -999.;
  double hitChisq_28 = -999.;
  double hitChisq_29 = -999.;
  double hitChisq_30 = -999.;
  double hitChisq_31 = -999.;

  if (tmSeq.dstnc.size()<=1) return;
  //std::cout<<"starting..."<<std::endl;
  for (unsigned int i=0;i<tmSeq.dstnc.size();i++) {
    invbeta+=(1.+tmSeq.local_t0.at(i)/tmSeq.dstnc.at(i)*30.)*tmSeq.weightInvbeta.at(i)/tmSeq.totalWeightInvbeta;
    x.push_back(tmSeq.dstnc.at(i)/30.);
    y.push_back(tmSeq.local_t0.at(i)+tmSeq.dstnc.at(i)/30.);
    vertexTime+=tmSeq.local_t0.at(i)*tmSeq.weightVertex.at(i)/tmSeq.totalWeightVertex;
    vertexTimeR+=(tmSeq.local_t0.at(i)+2*tmSeq.dstnc.at(i)/30.)*tmSeq.weightVertex.at(i)/tmSeq.totalWeightVertex;
  }
  if(tmSeq.dstnc.size()>0){
    //std::cout<<"size>0"<<std::endl;
    local_t0_0=tmSeq.local_t0.at(0);
    std::cout<<"local_t0_0 is: "<<tmSeq.local_t0.at(0)<<std::endl;
    std::cout<<"hitChisq_0 is: "<<tmSeq.hitChisq.at(0)<<std::endl;
    std::cout<<"correctedTime_0 is: "<<tmSeq.correctedTime.at(0)<<std::endl;
    std::cout<<"distance_0 is: "<<tmSeq.dstnc.at(0)<<std::endl;
    correctedTime_0=tmSeq.correctedTime.at(0);
    distance_0=tmSeq.dstnc.at(0);
    hitChisq_0=tmSeq.hitChisq.at(0);
  }
  std::cout<<"filled for first one..."<<std::endl;
  if(tmSeq.dstnc.size()>1){
    local_t0_1=tmSeq.local_t0.at(1);
    correctedTime_1=tmSeq.correctedTime.at(1);
    distance_1=tmSeq.dstnc.at(1);
    hitChisq_1=tmSeq.hitChisq.at(1);
  }
  if(tmSeq.dstnc.size()>2){
    local_t0_2=tmSeq.local_t0.at(2);
    correctedTime_2=tmSeq.correctedTime.at(2);
    distance_2=tmSeq.dstnc.at(2);
    hitChisq_2=tmSeq.hitChisq.at(2);
  }
  if(tmSeq.dstnc.size()>3){
    local_t0_3=tmSeq.local_t0.at(3);
    correctedTime_3=tmSeq.correctedTime.at(3);
    distance_3=tmSeq.dstnc.at(3);
    hitChisq_3=tmSeq.hitChisq.at(3);
  }
  if(tmSeq.dstnc.size()>4){
    local_t0_4=tmSeq.local_t0.at(4);
    correctedTime_4=tmSeq.correctedTime.at(4);
    distance_4=tmSeq.dstnc.at(4);
    hitChisq_4=tmSeq.hitChisq.at(4);
  }
  if(tmSeq.dstnc.size()>5){
    local_t0_5=tmSeq.local_t0.at(5);
    correctedTime_5=tmSeq.correctedTime.at(5);
    distance_5=tmSeq.dstnc.at(5);
    hitChisq_5=tmSeq.hitChisq.at(5);
  }
  if(tmSeq.dstnc.size()>6){
    local_t0_6=tmSeq.local_t0.at(6);
    correctedTime_6=tmSeq.correctedTime.at(6);
    distance_6=tmSeq.dstnc.at(6);
    hitChisq_6=tmSeq.hitChisq.at(6);
  }
  if(tmSeq.dstnc.size()>7){
    local_t0_7=tmSeq.local_t0.at(7);
    correctedTime_7=tmSeq.correctedTime.at(7);
    distance_7=tmSeq.dstnc.at(7);
    hitChisq_7=tmSeq.hitChisq.at(7);
  }
  if(tmSeq.dstnc.size()>8){
    local_t0_8=tmSeq.local_t0.at(8);
    correctedTime_8=tmSeq.correctedTime.at(8);
    distance_8=tmSeq.dstnc.at(8);
    hitChisq_8=tmSeq.hitChisq.at(8);
  }
  if(tmSeq.dstnc.size()>9){
    local_t0_9=tmSeq.local_t0.at(9);
    correctedTime_9=tmSeq.correctedTime.at(9);
    distance_9=tmSeq.dstnc.at(9);
    hitChisq_9=tmSeq.hitChisq.at(9);
  }
  if(tmSeq.dstnc.size()>10){
    local_t0_10=tmSeq.local_t0.at(10);
    correctedTime_10=tmSeq.correctedTime.at(10);
    distance_10=tmSeq.dstnc.at(10);
    hitChisq_10=tmSeq.hitChisq.at(10);
  }
  //std::cout<<"filled for 10th one..."<<std::endl;
  if(tmSeq.dstnc.size()>11){
    local_t0_11=tmSeq.local_t0.at(11);
    correctedTime_11=tmSeq.correctedTime.at(11);
    distance_11=tmSeq.dstnc.at(11);
    hitChisq_11=tmSeq.hitChisq.at(11);
  }
  std::cout<<"filled for 11th one..."<<std::endl;
  if(tmSeq.dstnc.size()>12){
    //std::cout<<"local_t0_12 is: "<<tmSeq.local_t0.at(12)<<std::endl;
    //std::cout<<"hitChisq_12 is: "<<tmSeq.hitChisq.at(12)<<std::endl;
    local_t0_12=tmSeq.local_t0.at(12);
    correctedTime_12=tmSeq.correctedTime.at(12);
    distance_12=tmSeq.dstnc.at(12);
    hitChisq_12=tmSeq.hitChisq.at(12);
  }
  //std::cout<<"filled for 12th one..."<<std::endl;
  if(tmSeq.dstnc.size()>13){
    local_t0_13=tmSeq.local_t0.at(13);
    correctedTime_13=tmSeq.correctedTime.at(13);
    distance_13=tmSeq.dstnc.at(13);
    hitChisq_13=tmSeq.hitChisq.at(13);
  }
  //std::cout<<"filled for 13th one..."<<std::endl;
  if(tmSeq.dstnc.size()>14){
    local_t0_14=tmSeq.local_t0.at(14);
    correctedTime_14=tmSeq.correctedTime.at(14);
    distance_14=tmSeq.dstnc.at(14);
    hitChisq_14=tmSeq.hitChisq.at(14);
  }
  //std::cout<<"filled for 14th one..."<<std::endl;
  if(tmSeq.dstnc.size()>15){
    local_t0_15=tmSeq.local_t0.at(15);
    correctedTime_15=tmSeq.correctedTime.at(15);
    distance_15=tmSeq.dstnc.at(15);
    hitChisq_15=tmSeq.hitChisq.at(15);
  }
  //std::cout<<"filled for 15th one..."<<std::endl;
  if(tmSeq.dstnc.size()>16){
    local_t0_16=tmSeq.local_t0.at(16);
    correctedTime_16=tmSeq.correctedTime.at(16);
    distance_16=tmSeq.dstnc.at(16);
    hitChisq_16=tmSeq.hitChisq.at(16);
  }
  if(tmSeq.dstnc.size()>17){
    local_t0_17=tmSeq.local_t0.at(17);
    correctedTime_17=tmSeq.correctedTime.at(17);
    distance_17=tmSeq.dstnc.at(17);
    hitChisq_17=tmSeq.hitChisq.at(17);
  }
  if(tmSeq.dstnc.size()>18){
    local_t0_18=tmSeq.local_t0.at(18);
    correctedTime_18=tmSeq.correctedTime.at(18);
    distance_18=tmSeq.dstnc.at(18);
    hitChisq_18=tmSeq.hitChisq.at(18);
  }
  if(tmSeq.dstnc.size()>19){
    local_t0_19=tmSeq.local_t0.at(19);
    correctedTime_19=tmSeq.correctedTime.at(19);
    distance_19=tmSeq.dstnc.at(19);
    hitChisq_19=tmSeq.hitChisq.at(19);
  }
  if(tmSeq.dstnc.size()>20){
    local_t0_20=tmSeq.local_t0.at(20);
    correctedTime_20=tmSeq.correctedTime.at(20);
    distance_20=tmSeq.dstnc.at(20);
    hitChisq_20=tmSeq.hitChisq.at(20);
  }
  std::cout<<"filled for 20th one..."<<std::endl;
  if(tmSeq.dstnc.size()>21){
    local_t0_21=tmSeq.local_t0.at(21);
    correctedTime_21=tmSeq.correctedTime.at(21);
    distance_21=tmSeq.dstnc.at(21);
    hitChisq_21=tmSeq.hitChisq.at(21);
  }
  if(tmSeq.dstnc.size()>22){
    local_t0_22=tmSeq.local_t0.at(22);
    correctedTime_22=tmSeq.correctedTime.at(22);
    distance_22=tmSeq.dstnc.at(22);
    hitChisq_22=tmSeq.hitChisq.at(22);
  }
  if(tmSeq.dstnc.size()>23){
    local_t0_23=tmSeq.local_t0.at(23);
    correctedTime_23=tmSeq.correctedTime.at(23);
    distance_23=tmSeq.dstnc.at(23);
    hitChisq_23=tmSeq.hitChisq.at(23);
  }
  if(tmSeq.dstnc.size()>24){
    local_t0_24=tmSeq.local_t0.at(24);
    correctedTime_24=tmSeq.correctedTime.at(24);
    distance_24=tmSeq.dstnc.at(24);
    hitChisq_24=tmSeq.hitChisq.at(24);
  }
  if(tmSeq.dstnc.size()>25){
    local_t0_25=tmSeq.local_t0.at(25);
    correctedTime_25=tmSeq.correctedTime.at(25);
    distance_25=tmSeq.dstnc.at(25);
    hitChisq_25=tmSeq.hitChisq.at(25);
  }
  //std::cout<<"filled for 25th one..."<<std::endl;
  if(tmSeq.dstnc.size()>26){
    local_t0_26=tmSeq.local_t0.at(26);
    correctedTime_26=tmSeq.correctedTime.at(26);
    distance_26=tmSeq.dstnc.at(26);
    hitChisq_26=tmSeq.hitChisq.at(26);
  }
  if(tmSeq.dstnc.size()>27){
    local_t0_27=tmSeq.local_t0.at(27);
    correctedTime_27=tmSeq.correctedTime.at(27);
    distance_27=tmSeq.dstnc.at(27);
    hitChisq_27=tmSeq.hitChisq.at(27);
  }
  if(tmSeq.dstnc.size()>28){
    local_t0_28=tmSeq.local_t0.at(28);
    correctedTime_28=tmSeq.correctedTime.at(28);
    distance_28=tmSeq.dstnc.at(28);
    hitChisq_28=tmSeq.hitChisq.at(28);
  }
  if(tmSeq.dstnc.size()>29){
    local_t0_29=tmSeq.local_t0.at(29);
    correctedTime_29=tmSeq.correctedTime.at(29);
    distance_29=tmSeq.dstnc.at(29);
    hitChisq_29=tmSeq.hitChisq.at(29);
  }
  if(tmSeq.dstnc.size()>30){
    local_t0_30=tmSeq.local_t0.at(30);
    correctedTime_30=tmSeq.correctedTime.at(30);
    distance_30=tmSeq.dstnc.at(30);
    hitChisq_30=tmSeq.hitChisq.at(30);
  }
  if(tmSeq.dstnc.size()>31){
    local_t0_31=tmSeq.local_t0.at(31);
    correctedTime_31=tmSeq.correctedTime.at(31);
    distance_31=tmSeq.dstnc.at(31);
    hitChisq_31=tmSeq.hitChisq.at(31);
  }
  std::cout<<"set localt0's and chisq"<<std::endl;
  double diff;
  for (unsigned int i=0;i<tmSeq.dstnc.size();i++) {
    diff=(1.+tmSeq.local_t0.at(i)/tmSeq.dstnc.at(i)*30.)-invbeta;
    invbetaerr+=diff*diff*tmSeq.weightInvbeta.at(i);
    diff=tmSeq.local_t0.at(i)-vertexTime;
    vertexTimeErr+=diff*diff*tmSeq.weightVertex.at(i);
    diff=tmSeq.local_t0.at(i)+2*tmSeq.dstnc.at(i)/30.-vertexTimeR;
    vertexTimeRErr+=diff*diff*tmSeq.weightVertex.at(i);
  }
  
  double cf = 1./(tmSeq.dstnc.size()-1);
  invbetaerr=sqrt(invbetaerr/tmSeq.totalWeightInvbeta*cf);
  vertexTimeErr=sqrt(vertexTimeErr/tmSeq.totalWeightVertex*cf);
  vertexTimeRErr=sqrt(vertexTimeRErr/tmSeq.totalWeightVertex*cf);

  muTime.setInverseBeta(invbeta);
  muTime.setInverseBetaErr(invbetaerr);
  muTime.setTimeAtIpInOut(vertexTime);
  muTime.setTimeAtIpInOutErr(vertexTimeErr);
  muTime.setTimeAtIpOutIn(vertexTimeR);
  muTime.setTimeAtIpOutInErr(vertexTimeRErr);
      
  rawFit(freeBeta, freeBetaErr, freeTime, freeTimeErr, x, y);

  muTime.setFreeInverseBeta(freeBeta);
  muTime.setFreeInverseBetaErr(freeBetaErr);
    
  muTime.setNDof(tmSeq.dstnc.size());

  muTime.setAveHitTimeError(tmSeq.aveHitTimeError);
  muTime.setInvbetaLS(tmSeq.InvbetaLS);
  muTime.setYIntercept(tmSeq.yIntercept);
  muTime.setInvbetaLSError(tmSeq.InvbetaLSError);
  muTime.setYInterceptError(tmSeq.yInterceptError);
  muTime.setChi2Dof(tmSeq.chi2Dof);

  muTime.setLocalT00(local_t0_0);
  muTime.setLocalT01(local_t0_1);
  muTime.setLocalT02(local_t0_2);
  muTime.setLocalT03(local_t0_3);
  muTime.setLocalT04(local_t0_4);
  muTime.setLocalT05(local_t0_5);
  muTime.setLocalT06(local_t0_6);
  muTime.setLocalT07(local_t0_7);
  muTime.setLocalT08(local_t0_8);
  muTime.setLocalT09(local_t0_9);
  muTime.setLocalT010(local_t0_10);
  muTime.setLocalT011(local_t0_11);
  muTime.setLocalT012(local_t0_12);
  muTime.setLocalT013(local_t0_13);
  muTime.setLocalT014(local_t0_14);
  muTime.setLocalT015(local_t0_15);
  muTime.setLocalT016(local_t0_16);
  muTime.setLocalT017(local_t0_17);
  muTime.setLocalT018(local_t0_18);
  muTime.setLocalT019(local_t0_19);
  muTime.setLocalT020(local_t0_20);
  muTime.setLocalT021(local_t0_21);
  muTime.setLocalT022(local_t0_22);
  muTime.setLocalT023(local_t0_23);
  muTime.setLocalT024(local_t0_24);
  muTime.setLocalT025(local_t0_25);
  muTime.setLocalT026(local_t0_26);
  muTime.setLocalT027(local_t0_27);
  muTime.setLocalT028(local_t0_28);
  muTime.setLocalT029(local_t0_29);
  muTime.setLocalT030(local_t0_30);
  muTime.setLocalT031(local_t0_31);

  muTime.setCorrectedTime0(correctedTime_0);
  muTime.setCorrectedTime1(correctedTime_1);
  muTime.setCorrectedTime2(correctedTime_2);
  muTime.setCorrectedTime3(correctedTime_3);
  muTime.setCorrectedTime4(correctedTime_4);
  muTime.setCorrectedTime5(correctedTime_5);
  muTime.setCorrectedTime6(correctedTime_6);
  muTime.setCorrectedTime7(correctedTime_7);
  muTime.setCorrectedTime8(correctedTime_8);
  muTime.setCorrectedTime9(correctedTime_9);
  muTime.setCorrectedTime10(correctedTime_10);
  muTime.setCorrectedTime11(correctedTime_11);
  muTime.setCorrectedTime12(correctedTime_12);
  muTime.setCorrectedTime13(correctedTime_13);
  muTime.setCorrectedTime14(correctedTime_14);
  muTime.setCorrectedTime15(correctedTime_15);
  muTime.setCorrectedTime16(correctedTime_16);
  muTime.setCorrectedTime17(correctedTime_17);
  muTime.setCorrectedTime18(correctedTime_18);
  muTime.setCorrectedTime19(correctedTime_19);
  muTime.setCorrectedTime20(correctedTime_20);
  muTime.setCorrectedTime21(correctedTime_21);
  muTime.setCorrectedTime22(correctedTime_22);
  muTime.setCorrectedTime23(correctedTime_23);
  muTime.setCorrectedTime24(correctedTime_24);
  muTime.setCorrectedTime25(correctedTime_25);
  muTime.setCorrectedTime26(correctedTime_26);
  muTime.setCorrectedTime27(correctedTime_27);
  muTime.setCorrectedTime28(correctedTime_28);
  muTime.setCorrectedTime29(correctedTime_29);
  muTime.setCorrectedTime30(correctedTime_30);
  muTime.setCorrectedTime31(correctedTime_31);

  muTime.setDistance0(distance_0);
  muTime.setDistance1(distance_1);
  muTime.setDistance2(distance_2);
  muTime.setDistance3(distance_3);
  muTime.setDistance4(distance_4);
  muTime.setDistance5(distance_5);
  muTime.setDistance6(distance_6);
  muTime.setDistance7(distance_7);
  muTime.setDistance8(distance_8);
  muTime.setDistance9(distance_9);
  muTime.setDistance10(distance_10);
  muTime.setDistance11(distance_11);
  muTime.setDistance12(distance_12);
  muTime.setDistance13(distance_13);
  muTime.setDistance14(distance_14);
  muTime.setDistance15(distance_15);
  muTime.setDistance16(distance_16);
  muTime.setDistance17(distance_17);
  muTime.setDistance18(distance_18);
  muTime.setDistance19(distance_19);
  muTime.setDistance20(distance_20);
  muTime.setDistance21(distance_21);
  muTime.setDistance22(distance_22);
  muTime.setDistance23(distance_23);
  muTime.setDistance24(distance_24);
  muTime.setDistance25(distance_25);
  muTime.setDistance26(distance_26);
  muTime.setDistance27(distance_27);
  muTime.setDistance28(distance_28);
  muTime.setDistance29(distance_29);
  muTime.setDistance30(distance_30);
  muTime.setDistance31(distance_31);

  muTime.setHitChisq0(hitChisq_0);
  muTime.setHitChisq1(hitChisq_1);
  muTime.setHitChisq2(hitChisq_2);
  muTime.setHitChisq3(hitChisq_3);
  muTime.setHitChisq4(hitChisq_4);
  muTime.setHitChisq5(hitChisq_5);
  muTime.setHitChisq6(hitChisq_6);
  muTime.setHitChisq7(hitChisq_7);
  muTime.setHitChisq8(hitChisq_8);
  muTime.setHitChisq9(hitChisq_9);
  muTime.setHitChisq10(hitChisq_10);
  muTime.setHitChisq11(hitChisq_11);
  muTime.setHitChisq12(hitChisq_12);
  muTime.setHitChisq13(hitChisq_13);
  muTime.setHitChisq14(hitChisq_14);
  muTime.setHitChisq15(hitChisq_15);
  muTime.setHitChisq16(hitChisq_16);
  muTime.setHitChisq17(hitChisq_17);
  muTime.setHitChisq18(hitChisq_18);
  muTime.setHitChisq19(hitChisq_19);
  muTime.setHitChisq20(hitChisq_20);
  muTime.setHitChisq21(hitChisq_21);
  muTime.setHitChisq22(hitChisq_22);
  muTime.setHitChisq23(hitChisq_23);
  muTime.setHitChisq24(hitChisq_24);
  muTime.setHitChisq25(hitChisq_25);
  muTime.setHitChisq26(hitChisq_26);
  muTime.setHitChisq27(hitChisq_27);
  muTime.setHitChisq28(hitChisq_28);
  muTime.setHitChisq29(hitChisq_29);
  muTime.setHitChisq30(hitChisq_30);
  muTime.setHitChisq31(hitChisq_31);

  std::cout<<"set all variables..."<<std::endl;

}

void 
MuonTimingFillerDelayedMuons::combineTMSequences( const reco::Muon& muon, 
                                      TimeMeasurementSequence dtSeq, 
                                      TimeMeasurementSequence cscSeq, 
                                      TimeMeasurementSequence &cmbSeq ) {
                                        
  if (useDT_) for (unsigned int i=0;i<dtSeq.dstnc.size();i++) {
    cmbSeq.dstnc.push_back(dtSeq.dstnc.at(i));
    cmbSeq.local_t0.push_back(dtSeq.local_t0.at(i));
    cmbSeq.weightVertex.push_back(dtSeq.weightVertex.at(i));
    cmbSeq.weightInvbeta.push_back(dtSeq.weightInvbeta.at(i));
    cmbSeq.hitChisq.push_back(dtSeq.hitChisq.at(i));
    cmbSeq.correctedTime.push_back(dtSeq.correctedTime.at(i));

    cmbSeq.totalWeightVertex+=dtSeq.weightVertex.at(i);
    cmbSeq.totalWeightInvbeta+=dtSeq.weightInvbeta.at(i);
  }
  std::cout<<"in combineTMSequences, finished useDT_"<<std::endl;

  if (useCSC_) for (unsigned int i=0;i<cscSeq.dstnc.size();i++) {
    cmbSeq.dstnc.push_back(cscSeq.dstnc.at(i));
    cmbSeq.local_t0.push_back(cscSeq.local_t0.at(i));
    cmbSeq.weightVertex.push_back(cscSeq.weightVertex.at(i));
    cmbSeq.weightInvbeta.push_back(cscSeq.weightInvbeta.at(i));
    cmbSeq.hitChisq.push_back(cscSeq.hitChisq.at(i));
    cmbSeq.correctedTime.push_back(cscSeq.correctedTime.at(i));

    cmbSeq.totalWeightVertex+=cscSeq.weightVertex.at(i);
    cmbSeq.totalWeightInvbeta+=cscSeq.weightInvbeta.at(i);
  }
  std::cout<<"in combineTMSequences, finished useCSC_"<<std::endl;
}


void 
MuonTimingFillerDelayedMuons::addEcalTime( const reco::Muon& muon, 
                               TimeMeasurementSequence &cmbSeq ) {

  reco::MuonEnergy muonE;
  if (muon.isEnergyValid())  
    muonE = muon.calEnergy();
  
  // Cut on the crystal energy and restrict to the ECAL barrel for now
//  if (muonE.emMax<ecalEcut_ || fabs(muon.eta())>1.5) return;    
  if (muonE.emMax<ecalEcut_) return;    
  
  // A simple parametrization of the error on the ECAL time measurement
  double emErr;
  if (muonE.ecal_id.subdetId()==EcalBarrel) emErr= errorEB_/muonE.emMax; else
    emErr=errorEE_/muonE.emMax;
  double hitWeight = 1/(emErr*emErr);
  double hitDist=muonE.ecal_position.r();
        
  cmbSeq.local_t0.push_back(muonE.ecal_time);
  cmbSeq.weightVertex.push_back(hitWeight);
  cmbSeq.weightInvbeta.push_back(hitDist*hitDist*hitWeight/(30.*30.));

  cmbSeq.dstnc.push_back(hitDist);
  
  cmbSeq.totalWeightVertex+=hitWeight;
  cmbSeq.totalWeightInvbeta+=hitDist*hitDist*hitWeight/(30.*30.);
 
  cmbSeq.hitChisq.push_back(-999.);
  cmbSeq.correctedTime.push_back(-999.);
                                     
}



void 
MuonTimingFillerDelayedMuons::rawFit(double &a, double &da, double &b, double &db, const std::vector<double> hitsx, const std::vector<double> hitsy) {

  double s=0,sx=0,sy=0,x,y;
  double sxx=0,sxy=0;

  a=b=0;
  if (hitsx.size()==0) return;
  if (hitsx.size()==1) {
    b=hitsy[0];
  } else {
    for (unsigned int i = 0; i != hitsx.size(); i++) {
      x=hitsx[i];
      y=hitsy[i];
      sy += y;
      sxy+= x*y;
      s += 1.;
      sx += x;
      sxx += x*x;
    }

    double d = s*sxx - sx*sx;
    b = (sxx*sy- sx*sxy)/ d;
    a = (s*sxy - sx*sy) / d;
    da = sqrt(sxx/d);
    db = sqrt(s/d);
  }
}

