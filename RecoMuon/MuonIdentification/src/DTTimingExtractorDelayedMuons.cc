// -*- C++ -*-
//
// Package:    MuonIdentification
// Class:      DTTimingExtractorDelayedMuons
// 
/**\class DTTimingExtractorDelayedMuons DTTimingExtractorDelayedMuons.cc RecoMuon/MuonIdentification/src/DTTimingExtractorDelayedMuons.cc
 *
 * Description: Produce timing information for a muon track using 1D DT hits from segments used to build the track
 *
 */
//
// Original Author:  Traczyk Piotr
//         Created:  Thu Oct 11 15:01:28 CEST 2007
// $Id: DTTimingExtractorDelayedMuons.cc,v 1.15 2013/03/06 15:41:53 jalimena Exp $
//
//

#include "RecoMuon/MuonIdentification/interface/DTTimingExtractorDelayedMuons.h"


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "RecoMuon/TrackingTools/interface/MuonServiceProxy.h"

#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "DataFormats/MuonDetId/interface/MuonSubdetId.h"
#include "Geometry/DTGeometry/interface/DTGeometry.h"
#include "Geometry/DTGeometry/interface/DTLayer.h"
#include "Geometry/DTGeometry/interface/DTChamber.h"
#include "Geometry/DTGeometry/interface/DTSuperLayer.h"
#include "DataFormats/DTRecHit/interface/DTSLRecSegment2D.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment2D.h"

#include "Geometry/Records/interface/GlobalTrackingGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment2D.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment4DCollection.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment2DCollection.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"
#include "RecoMuon/TransientTrackingRecHit/interface/MuonTransientTrackingRecHit.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackReco/interface/TrackExtraFwd.h"


// system include files
#include <memory>
#include <vector>
#include <string>
#include <iostream>
#include "TROOT.h"
#include "TH1.h"
#include "TH2.h"
#include "TF1.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TMath.h"
#include "TObject.h"
#include "TCanvas.h"

namespace edm {
  class ParameterSet;
  class EventSetup;
  class InputTag;
}

class MuonServiceProxy;

//
// constructors and destructor
//
//DTTimingExtractorDelayedMuons::DTTimingExtractorDelayedMuons(const edm::ParameterSet& iConfig)
DTTimingExtractorDelayedMuons::DTTimingExtractorDelayedMuons(const edm::ParameterSet& iConfig,edm::ConsumesCollector& iC)
  :
  DTSegmentTags_(iConfig.getParameter<edm::InputTag>("DTsegments")),
  theHitsMin_(iConfig.getParameter<int>("HitsMin")),
  thePruneCut_(iConfig.getParameter<double>("PruneCut")),
  theTimeOffset_(iConfig.getParameter<double>("DTTimeOffset")),
  theErrorPhi_(iConfig.getParameter<double>("HitErrorPhi")),
  theErrorTheta_(iConfig.getParameter<double>("HitErrorTheta")),
  useSegmentT0_(iConfig.getParameter<bool>("UseSegmentT0")),
  doWireCorr_(iConfig.getParameter<bool>("DoWireCorr")),
  dropTheta_(iConfig.getParameter<bool>("DropTheta")),
  requireBothProjections_(iConfig.getParameter<bool>("RequireBothProjections")),
  debug(iConfig.getParameter<bool>("debug"))
{
  edm::ParameterSet serviceParameters = iConfig.getParameter<edm::ParameterSet>("ServiceParameters");
  theService = new MuonServiceProxy(serviceParameters);
  
  edm::ParameterSet matchParameters = iConfig.getParameter<edm::ParameterSet>("MatchParameters");

  //theMatcher = new MuonSegmentMatcher(matchParameters, theService);
  theMatcher = new MuonSegmentMatcher(matchParameters, theService,iC);
}


DTTimingExtractorDelayedMuons::~DTTimingExtractorDelayedMuons()
{
  if (theService) delete theService;
  if (theMatcher) delete theMatcher;
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
DTTimingExtractorDelayedMuons::fillTiming(TimeMeasurementSequence &tmSequence, reco::TrackRef muonTrack, const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

//  using reco::TrackCollection;

  if (debug) 
    std::cout << " *** Muon Timing Extractor ***" << std::endl;

  theService->update(iSetup);


  const GlobalTrackingGeometry *theTrackingGeometry = &*theService->trackingGeometry();

  // get the DT geometry
  edm::ESHandle<DTGeometry> theDTGeom;
  iSetup.get<MuonGeometryRecord>().get(theDTGeom);
  
  edm::ESHandle<Propagator> propagator;
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorAny", propagator);
  const Propagator *propag = propagator.product();

  double invbeta=0;
  double invbetaerr=0;
  double totalWeightInvbeta=0;
  double totalWeightVertex=0;
  double AveHitTimeError=0.;
  std::vector<TimeMeasurement> tms;

  math::XYZPoint  pos=muonTrack->innerPosition();
  math::XYZVector mom=muonTrack->innerMomentum();
  GlobalPoint  posp(pos.x(), pos.y(), pos.z());
  GlobalVector momv(mom.x(), mom.y(), mom.z());
  FreeTrajectoryState muonFTS(posp, momv, (TrackCharge)muonTrack->charge(), theService->magneticField().product());
  int precision = 3;
  if(debug) std::cout<<"muon track inner position is: "<<std::fixed<<std::setprecision(precision)<<pos<<std::endl;
  //if(debug) std::cout<<"muon track inner position is: "<<pos<<std::endl;

  // get the DT segments that were used to construct the muon
  std::vector<const DTRecSegment4D*> range = theMatcher->matchDT(*muonTrack,iEvent);
  if(debug) std::cout<<"range.size() is:"<<range.size()<<std::endl;
  if(debug) std::cout<<"muon track eta is:"<<muonTrack->eta()<<", muon track phi is: "<<muonTrack->phi()<<std::endl;

  // create a collection on TimeMeasurements for the track        
  for (std::vector<const DTRecSegment4D*>::iterator rechit = range.begin(); rechit!=range.end();++rechit) {
    //if(debug) std::cout<<"looping over 4D segments..."<<std::endl;

    // Create the ChamberId
    DetId id = (*rechit)->geographicalId();
    DTChamberId chamberId(id.rawId());
    int station = chamberId.station();

    // use only segments with both phi and theta projections present (optional)
    bool bothProjections = ( ((*rechit)->hasPhi()) && ((*rechit)->hasZed()) );
    
    if (requireBothProjections_ && !bothProjections){
      if(debug) std::cout<<"doesn't have both phi and theta projections"<<std::endl;
      continue;
    }

    // loop over (theta, phi) segments
    for (int phi=0; phi<2; phi++) {//bool of whether phi or theta segment
      //if(debug) std::cout<<"phi is: "<<phi<<std::endl;
      if (dropTheta_ && !phi){
	//if(debug) std::cout<<"dropping theta"<<std::endl;
	continue;
      }

      const DTRecSegment2D* segm;
      if (phi) segm = dynamic_cast<const DTRecSegment2D*>((*rechit)->phiSegment()); 
        else segm = dynamic_cast<const DTRecSegment2D*>((*rechit)->zSegment());

      if(segm == 0){
	if(debug) std::cout<<"segm==0"<<std::endl;
	continue;
      }
      if (!segm->specificRecHits().size()){
	if(debug) std::cout<<"segment doesnt have any specific rec hits"<<std::endl;
	continue;
      }

      const GeomDet* geomDet = theTrackingGeometry->idToDet(segm->geographicalId());
      const std::vector<DTRecHit1D> hits1d = segm->specificRecHits();

      // store all the hits from the segment
      for (std::vector<DTRecHit1D>::const_iterator hiti=hits1d.begin(); hiti!=hits1d.end(); hiti++) {
	//if(debug) std::cout<<"looping over hits..."<<std::endl;

	const GeomDet* dtcell = theTrackingGeometry->idToDet(hiti->geographicalId());
	TimeMeasurement thisHit;

	std::pair< TrajectoryStateOnSurface, double> tsos;
	tsos=propag->propagateWithPath(muonFTS,dtcell->surface());

        double dist;            
        double dist_straight = dtcell->toGlobal(hiti->localPosition()).mag(); 
        double x = dtcell->toGlobal(hiti->localPosition()).x(); 
        double y = dtcell->toGlobal(hiti->localPosition()).y(); 
        double z = dtcell->toGlobal(hiti->localPosition()).z(); 
	const DTLayer* layer_ = theDTGeom->layer(hiti->wireId());
	DTLayerId layer_id = layer_->id();
	if (tsos.first.isValid()) { 
	  dist = tsos.second+posp.mag(); // tsos + track inner position
	  if(debug) std::cout << "Propagate distance: " << dist << " ( innermost: " << posp.mag() << "), wheel is: "<<layer_id.wheel()<<", station is: "<<layer_id.station()<<", sector is: "<<layer_id.sector()<<", superlayer is: "<<layer_id.superlayer()<<", layer is: "<<layer_id.layer()<<std::endl;
	} else { 
	  dist = dist_straight;
	  if(debug) std::cout << "Geom distance: " << dist << std::endl; 
	}
	if(debug) std::cout << "x: " << x <<", y: "<<y<<", z: "<<z<<std::endl; 

	thisHit.driftCell = hiti->geographicalId();
	if (hiti->lrSide()==DTEnums::Left) thisHit.isLeft=true; else thisHit.isLeft=false; //which side of the DT cell
	thisHit.isPhi = phi;
	thisHit.posInLayer = geomDet->toLocal(dtcell->toGlobal(hiti->localPosition())).x();
	thisHit.distIP = dist;
	thisHit.station = station;
	if (useSegmentT0_ && segm->ist0Valid()) thisHit.timeCorr=segm->t0();
	else thisHit.timeCorr=0.;
	thisHit.timeCorr += theTimeOffset_;
	thisHit.wheel = layer_id.wheel();
	thisHit.sector = layer_id.sector();
	thisHit.superlayer = layer_id.superlayer();
	thisHit.layer = layer_id.layer();
	thisHit.x = x;
	thisHit.y = y;
	thisHit.z = z;

	// signal propagation along the wire correction for unmached theta or phi segment hits
	//29.979 is the speed of light (cm/ns)
	//0.00543 is the average drift velocity of the electron cloud in the Drift Tubes, it is used to convert hit displacement to time displacement
	//24.4 is the velocity of the signal propagation along the readout wire.
	if (doWireCorr_ && !bothProjections && tsos.first.isValid()) {
	  const DTLayer* layer = theDTGeom->layer(hiti->wireId());
	  float propgL = layer->toLocal( tsos.first.globalPosition() ).y();
	  float wirePropCorr = propgL/24.4*0.00543; // signal propagation speed along the wire
	  if (thisHit.isLeft) wirePropCorr=-wirePropCorr;
	  thisHit.posInLayer += wirePropCorr;
	  const DTSuperLayer *sl = layer->superLayer();
	  float tofCorr = sl->surface().position().mag()-tsos.first.globalPosition().mag();
	  tofCorr = (tofCorr/29.979)*0.00543;
	  if (thisHit.isLeft) tofCorr=-tofCorr;
	  thisHit.posInLayer += tofCorr;
	} else {
          // non straight-line path correction
          float slCorr = (dist_straight-dist)/29.979*0.00543;
  	  if (thisHit.isLeft) slCorr=-slCorr;
  	  thisHit.posInLayer += slCorr;
	}

	tms.push_back(thisHit);
      }
    } // phi = (0,1) 	        
  } // rechit
      
  bool modified = false;
  std::vector <Double_t> dstnc, dsegm, correctedTime, dtraj, hitWeightVertex, hitWeightInvbeta, left, hitTimeError, hitChisq_, x, y, z;
  std::vector <Int_t> station, wheel, sector, superlayer, layer;
  double p1=-99., p2=-99., e1=-99., e2=-99., chi2dof=-99.;
  Int_t size = -1;
  //double trial_chi2dof= 99999.;

  // Now loop over the measurements, calculate 1/beta and cut away outliers
  do {    
    
    modified = false;
    dstnc.clear();
    dsegm.clear();
    correctedTime.clear();
    dtraj.clear();
    hitWeightVertex.clear();
    hitWeightInvbeta.clear();
    left.clear();
    hitTimeError.clear();
    station.clear();
    wheel.clear();
    sector.clear();
    superlayer.clear();
    layer.clear();
    hitChisq_.clear();
    x.clear();
    y.clear();
    z.clear();
    
    std::vector <int> hit_idx;
    totalWeightInvbeta=0;
    totalWeightVertex=0;
    AveHitTimeError=0.;

    // Rebuild segments
    for (int sta=1;sta<5;sta++)
      for (int phi=0;phi<2;phi++) {
        std::vector <TimeMeasurement> seg;
        std::vector <int> seg_idx;
	int tmpos=0;
	for (std::vector<TimeMeasurement>::iterator tm=tms.begin(); tm!=tms.end(); ++tm) {
	  if ((tm->station==sta) && (tm->isPhi==phi)) {
	    seg.push_back(*tm);
	    seg_idx.push_back(tmpos);
	  }
	  tmpos++;  
	}
	
	unsigned int segsize = seg.size();
	if (segsize<theHitsMin_) continue;
	
	double a=0, b=0;
        std::vector <double> hitxl,hitxr,hityl,hityr;
	
	for (std::vector<TimeMeasurement>::iterator tm=seg.begin(); tm!=seg.end(); ++tm) {
	  
	  DetId id = tm->driftCell;
	  const GeomDet* dtcell = theTrackingGeometry->idToDet(id);
	  DTChamberId chamberId(id.rawId());
	  const GeomDet* dtcham = theTrackingGeometry->idToDet(chamberId);
	  
	  double celly=dtcham->toLocal(dtcell->position()).z();
          
	  if (tm->isLeft) {
	    hitxl.push_back(celly);
	    hityl.push_back(tm->posInLayer);
	  } else {
	    hitxr.push_back(celly);
	    hityr.push_back(tm->posInLayer);
	  }    
	}//end loop over time measurements
	
	if (!fitT0(a,b,hitxl,hityl,hitxr,hityr)) {
	  if (debug)
	    std::cout << "     t0 = zero, Left hits: " << hitxl.size() << " Right hits: " << hitxr.size() << std::endl;
	  continue;
	}
          
	// a segment must have at least one left and one right hit
	if ((!hitxl.size()) || (!hityl.size())) continue;
	
	int segidx=0;
	for (std::vector<TimeMeasurement>::const_iterator tm=seg.begin(); tm!=seg.end(); ++tm) {
	  
	  DetId id = tm->driftCell;
	  const GeomDet* dtcell = theTrackingGeometry->idToDet(id);
	  DTChamberId chamberId(id.rawId());
	  const GeomDet* dtcham = theTrackingGeometry->idToDet(chamberId);
	  
	  double layerZ  = dtcham->toLocal(dtcell->position()).z();
	  double segmLocalPos = b+layerZ*a;
	  double hitLocalPos = tm->posInLayer;
	  int hitSide = -tm->isLeft*2+1; //left=-1, right=+1
	  double t0_segm = (-(hitSide*segmLocalPos)+(hitSide*hitLocalPos))/0.00543+tm->timeCorr;
	  double corrected_time = tm->distIP/29.979+t0_segm;
	  double theError = -1.;
	  if(tm->isPhi) theError = theErrorPhi_;
	  else theError = theErrorTheta_;
            
	  dstnc.push_back(tm->distIP);
	  dsegm.push_back(t0_segm);
	  correctedTime.push_back(corrected_time);
	  left.push_back(hitSide);
	  hitWeightInvbeta.push_back(((double)seg.size()-2.)*tm->distIP*tm->distIP/((double)seg.size()*30.*30.*theError*theError));
          hitWeightVertex.push_back(((double)seg.size()-2.)/((double)seg.size()*theError*theError));
	  hitTimeError.push_back(theError*TMath::Sqrt((double)seg.size()/((double)seg.size()-2)));
	  hit_idx.push_back(seg_idx.at(segidx));
	  segidx++;
	  totalWeightInvbeta+=((double)seg.size()-2.)*tm->distIP*tm->distIP/((double)seg.size()*30.*30.*theError*theError);
	  totalWeightVertex+=((double)seg.size()-2.)/((double)seg.size()*theError*theError);
	  AveHitTimeError+=theError*TMath::Sqrt((double)seg.size()/((double)seg.size()-2));
	  station.push_back(tm->station);
	  wheel.push_back(tm->wheel);
	  sector.push_back(tm->sector);
	  superlayer.push_back(tm->superlayer);
	  layer.push_back(tm->layer);
	  x.push_back(tm->x);
	  y.push_back(tm->y);
	  z.push_back(tm->z);

	  //if(debug) std::cout<<"distance is: "<<tm->distIP<<", time is: "<<t0_segm<<", station is: "<<tm->station<<", superlayer is: "<<tm->superlayer<<std::endl;
	} //end loop over time measurements
      } //end loop over phi segments
    
    if (totalWeightInvbeta==0) break;        
    
    // calculate the value and error of 1/beta from the complete set of 1D hits
    if (debug)
      std::cout << " Points for global fit: " << dstnc.size() << std::endl;
    
    // inverse beta - weighted average of the contributions from individual hits
    invbeta=0;
    for (unsigned int i=0;i<dstnc.size();i++) 
      invbeta+=(1.+dsegm.at(i)/dstnc.at(i)*30.)*hitWeightInvbeta.at(i)/totalWeightInvbeta;
    
    double chimax=0.;
    std::vector<TimeMeasurement>::iterator tmmax;
    
    // the dispersion of inverse beta
    double diff;
    for (unsigned int i=0;i<dstnc.size();i++) {
      diff=(1.+dsegm.at(i)/dstnc.at(i)*30.)-invbeta;
      diff=diff*diff*hitWeightInvbeta.at(i);
      invbetaerr+=diff;
      if (diff>chimax) { 
	tmmax=tms.begin()+hit_idx.at(i);
	chimax=diff;
      }
    }
    
    invbetaerr=sqrt(invbetaerr/totalWeightInvbeta); 
    
    /*
    // cut away the outliers on original inverse beta measurement
    if (chimax>thePruneCut_) {
      tms.erase(tmmax);
      modified=true;
      if (debug) std::cout<<"chimax was "<<chimax<<", so pruned and modified=true"<<std::endl;
    }    
    */

    if (debug)
      std::cout << " Measured 1/beta: " << invbeta << " +/- " << invbetaerr << ", chimax is: "<<chimax<<std::endl;
    
    size = dstnc.size();
    if(size>0){
      AveHitTimeError = 1.*AveHitTimeError/size;
      //TGraphErrors* gr = new TGraphErrors(size,&dstnc[0],&correctedTime[0],0,&hitWeightVertex[0]);
      TGraphErrors* gr = new TGraphErrors(size,&dstnc[0],&correctedTime[0],0,&hitTimeError[0]);
      TF1 *linfit1 = new TF1("linfit1","[0]*x+[1]",dstnc.at(0),dstnc.at(dstnc.size()-1));
      //std::cout<<"made lin fin"<<std::endl;
      if(debug) gr->Fit("linfit1","R");
      else gr->Fit("linfit1","RQ");
      //std::cout<<"fit graph"<<std::endl;
      p1  = linfit1->GetParameter(0);
      p2  = linfit1->GetParameter(1);
      e1  = linfit1->GetParError(0);
      e2  = linfit1->GetParError(1);
      chi2dof = 1.0*linfit1->GetChisquare()/(linfit1->GetNDF());
      //std::cout<<"mean x of graph is: "<<gr->GetMean(1)<<", mean y of graph is: "<<gr->GetMean(2)<<std::endl;
      if(debug) {
	std::cout<<"equation of line is: "<<p1<<"x + "<<p2<<std::endl;
	std::cout<<"inverse beta = "<<p1<<" ns/cm * 30 cm/ns = "<<30.0*p1<<" +/- "<<30.0*e1<<std::endl;
	std::cout<<"delta(1/beta) = weighted sum inverse beta - LS inverse beta = "<<invbeta-30.0*p1<<std::endl;
	std::cout<<"time when d=0 is: "<<p2<<" +/- "<<e2<<std::endl;
	std::cout<<"fit chisq/dof is: "<<chi2dof<<std::endl;
      }
      
      double max_hit_chisq=0.;
      //unsigned int hit=0;
      std::vector<TimeMeasurement>::iterator tmmax_;
      const unsigned int nStations = 4;
      const unsigned int nSLs = 4;
      int station_SL[nStations][nSLs];
      //bool is_inner_station_SL[nStations][nSLs];
      //bool is_outer_station_SL[nStations][nSLs];
      for (unsigned int i=0;i<nStations;i++) {
	for (unsigned int j=0;j<nSLs;j++) {
	  station_SL[i][j]=0;
	  //is_inner_station_SL[i][j]=false;
	  //is_outer_station_SL[i][j]=false;
	}
      }
      for (unsigned int i=0;i<dstnc.size();i++) {
	if(debug) std::cout<<"for hit "<<i<<", distance is: "<<dstnc.at(i)<<", time is: "<<dsegm.at(i)<<", hit time error is: "<<hitTimeError.at(i)<<", hit chisq is: "<<((correctedTime.at(i)-(p1*dstnc.at(i)+p2))/hitTimeError.at(i))*((correctedTime.at(i)-(p1*dstnc.at(i)+p2))/hitTimeError.at(i))<<std::endl;
	if(debug) std::cout<<"  wheel is: "<<wheel.at(i)<<", station is: "<<station.at(i)<<", sector is: "<<sector.at(i)<<", superlayer is: "<<superlayer.at(i)<<", layer is: "<<layer.at(i)<<std::endl;
	if(debug) std::cout<<"  x is: "<<x.at(i)<<", y is: "<<y.at(i)<<", z is: "<<z.at(i)<<std::endl;
	station_SL[station.at(i)-1][superlayer.at(i)-1]++;
	double hit_chisq = (correctedTime.at(i)-(p1*dstnc.at(i)+p2))/hitTimeError.at(i);
	hit_chisq= hit_chisq*hit_chisq;
	hitChisq_.push_back(hit_chisq);
	if(hit_chisq>max_hit_chisq){
	  max_hit_chisq=hit_chisq;
	  tmmax_=tms.begin()+hit_idx.at(i);
	  //hit=i;
	}
      }

      // cut away the outliers: Piotr's way (on LS fit inverse beta)
      if (max_hit_chisq>thePruneCut_) {
	//if(station_SL[station.at(hit)-1][superlayer.at(hit)-1]>3){ //erase a hit only if more than 3 hits per segment
	  tms.erase(tmmax_);
	  modified=true;
	  if (debug) std::cout<<"max_hit_chisq was "<<max_hit_chisq<<", so pruned and modified=true"<<std::endl;
	  //}
	  //else if(debug) std::cout<<"was going to prune, but failed to keep at least 3 hits per segment"<<std::endl;
      }

      /*
      //D0 way
      for (unsigned int i=0;i<nStations;i++) {
	for (unsigned int j=0;j<nSLs;j++) {
	  if(station_SL[i][j]>2){
	    is_inner_station_SL[i][j]= true;
	    goto end1;
	  }
	}
      }
    end1:

      for (unsigned int i=nStations; i-- !=0;) {
	for (unsigned int j=nSLs; j-- !=0;) {
	  if(station_SL[i][j]>2){
	    is_outer_station_SL[i][j]= true;
	    goto end2;
	  }
	}
      }
    end2:
      */

      //for (unsigned int i=0;i<nStations;i++) {
      //for (unsigned int j=0;j<nSLs;j++) {
      //  if(debug) std::cout<<"is_inner_station_SL["<<i<<"]["<<j<<"] is: "<<is_inner_station_SL[i][j]<<std::endl;
      //  if(debug) std::cout<<"is_outer_station_SL["<<i<<"]["<<j<<"] is: "<<is_outer_station_SL[i][j]<<std::endl;
      //}
      //}

      /*
      if(chi2dof<trial_chi2dof){
	trial_chi2dof=chi2dof;
	if(debug) std::cout<<"trial_chi2dof is: "<<trial_chi2dof<<std::endl;
	if(is_inner_station_SL[station.at(hit)-1][superlayer.at(hit)-1] && station_SL[station.at(hit)-1][superlayer.at(hit)-1]==3){
	  modified=false;
	  if(debug) std::cout<<"is_inner_station_SL["<<station.at(hit)-1<<"]["<<superlayer.at(hit)-1<<"] is: "<<is_inner_station_SL[station.at(hit)-1][superlayer.at(hit)-1]<<", station_SL["<<station.at(hit)-1<<"]["<<superlayer.at(hit)-1<<"] is: "<<station_SL[station.at(hit)-1][superlayer.at(hit)-1]<<std::endl;
	}
	else if(is_outer_station_SL[station.at(hit)-1][superlayer.at(hit)-1] && station_SL[station.at(hit)-1][superlayer.at(hit)-1]==3){
	  modified=false;
	  if(debug) std::cout<<"is_outer_station_SL["<<station.at(hit)-1<<"]["<<superlayer.at(hit)-1<<"] is: "<<is_outer_station_SL[station.at(hit)-1][superlayer.at(hit)-1]<<", station_SL["<<station.at(hit)-1<<"]["<<superlayer.at(hit)-1<<"] is: "<<station_SL[station.at(hit)-1][superlayer.at(hit)-1]<<std::endl;
	}
	else{
	  if(station_SL[station.at(hit)-1][superlayer.at(hit)-1]>3){ //erase a hit only if more than 3 hits per segment
	    tms.erase(tmmax_);
	    modified=true;
	    if (debug) std::cout<<"max_hit_chisq was "<<max_hit_chisq<<", so pruned and modified=true"<<std::endl;
	  }
	}
      }
      */
      
    }//end of size>0
    
  } while (modified);

  for (unsigned int i=0;i<dstnc.size();i++) {
    tmSequence.dstnc.push_back(dstnc.at(i));
    tmSequence.local_t0.push_back(dsegm.at(i));
    tmSequence.correctedTime.push_back(correctedTime.at(i));
    tmSequence.weightInvbeta.push_back(hitWeightInvbeta.at(i));
    tmSequence.weightVertex.push_back(hitWeightVertex.at(i));
    tmSequence.hitChisq.push_back(hitChisq_.at(i));
    if(debug) std::cout<<"FINAL time "<<i<<" is: "<<dsegm.at(i)<<std::endl;

    for(int j=-2; j<3; j++){//loop over wheels
      if(wheel.at(i)==j){
	for(int k=1; k<5; k++){//loop over stations
	  if(station.at(i)==k){
	    for(int l=1; l<13; l++){//loop over sectors
	      if(sector.at(i)==l){
		for(int m=1; m<4; m++){//loop over superlayers
		  if(superlayer.at(i)==m){
		  }
		}
	      }
	    }
	  }
	}
      }
    }
    std::string wheel_str, station_str, sector_str, superlayer_str;
    std::ostringstream convert_wheel, convert_station, convert_sector, convert_superlayer;
    convert_wheel<<wheel.at(i);
    convert_station<<station.at(i);
    convert_sector<<sector.at(i);
    convert_superlayer<<superlayer.at(i);
    wheel_str = convert_wheel.str();
    station_str = convert_station.str();
    sector_str = convert_sector.str();
    superlayer_str = convert_superlayer.str();
    //pair<int, string> wheel_pair;
    //wheel_pair[wheel] = wheel_str;
    //std::string location_str = "wheel" + wheel_str + "_station" + station_str + "_sector" + sector_str + "_superlayer" + superlayer_str;
    //tmSequence.location_str.push_back(dsegm.at(i));
    
    //tmSequence.wheel.push_back(wheel.at(i));
    //tmSequence.station.push_back(station.at(i));
    //tmSequence.sector.push_back(sector.at(i));
    //tmSequence.superlayer.push_back(superlayer.at(i));
    //tmSequence.layer.push_back(layer.at(i));
  }

  tmSequence.totalWeightInvbeta=totalWeightInvbeta;
  tmSequence.totalWeightVertex=totalWeightVertex;
  if(size>0){
    tmSequence.InvbetaLS=30.0*p1;
    tmSequence.yIntercept=p2;
    tmSequence.InvbetaLSError=30.0*e1;
    tmSequence.yInterceptError=e2;
    tmSequence.chi2Dof=chi2dof;
    tmSequence.aveHitTimeError=AveHitTimeError;
  }
  else{
    tmSequence.InvbetaLS=-999.;
    tmSequence.yIntercept=-999.;
    tmSequence.InvbetaLSError=-999.;
    tmSequence.yInterceptError=-999.;
    tmSequence.chi2Dof=-999.;
    tmSequence.aveHitTimeError=-999.;
  }

}

double
DTTimingExtractorDelayedMuons::fitT0(double &a, double &b, std::vector<double> xl, std::vector<double> yl, std::vector<double> xr, std::vector<double> yr ) {

  double sx=0,sy=0,sxy=0,sxx=0,ssx=0,ssy=0,s=0,ss=0;

  for (unsigned int i=0; i<xl.size(); i++) {
    sx+=xl[i];
    sy+=yl[i];
    sxy+=xl[i]*yl[i];
    sxx+=xl[i]*xl[i];
    s++;
    ssx+=xl[i];
    ssy+=yl[i];
    ss++;
  } 

  for (unsigned int i=0; i<xr.size(); i++) {
    sx+=xr[i];
    sy+=yr[i];
    sxy+=xr[i]*yr[i];
    sxx+=xr[i]*xr[i];
    s++;
    ssx-=xr[i];
    ssy-=yr[i];
    ss--;
  } 

  double delta = ss*ss*sxx+s*sx*sx+s*ssx*ssx-s*s*sxx-2*ss*sx*ssx;
  
  double t0_corr=0.;

  if (delta) {
    a=(ssy*s*ssx+sxy*ss*ss+sy*sx*s-sy*ss*ssx-ssy*sx*ss-sxy*s*s)/delta;
    b=(ssx*sy*ssx+sxx*ssy*ss+sx*sxy*s-sxx*sy*s-ssx*sxy*ss-sx*ssy*ssx)/delta;
    t0_corr=(ssx*s*sxy+sxx*ss*sy+sx*sx*ssy-sxx*s*ssy-sx*ss*sxy-ssx*sx*sy)/delta;
  }

  // convert drift distance to time
  t0_corr/=-0.00543;

  return t0_corr;
}


//define this as a plug-in
//DEFINE_FWK_MODULE(DTTimingExtractorDelayedMuons);
