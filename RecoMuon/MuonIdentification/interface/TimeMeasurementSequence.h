#ifndef MuonIdentification_TimeMeasurementSequence_h
#define MuonIdentification_TimeMeasurementSequence_h

/** \class reco::TimeMeasurementSequence TimeMeasurementSequence.h RecoMuon/MuonIdentification/interface/TimeMeasurementSequence.h
 *  
 * A class holding a set of individual time measurements along the muon trajectory
 *
 * \author Piotr Traczyk, CERN
 *
 * \version $Id: TimeMeasurementSequence.h,v 1.5 2011/02/24 15:41:53 farrell3 Exp $
 *
 */

class TimeMeasurementSequence {

    public:

      std::vector <double> dstnc;
      std::vector <double> local_t0;
      std::vector <double> correctedTime;
      std::vector <double> weightVertex;
      std::vector <double> weightInvbeta;
      std::vector <double> hitChisq;
      
      double totalWeightInvbeta;
      double totalWeightVertex;
      double InvbetaLS;
      double yIntercept;
      double InvbetaLSError;
      double yInterceptError;
      double chi2Dof;
      int nHits;
      double aveHitTimeError;
      
      TimeMeasurementSequence():
	totalWeightInvbeta(0),
	totalWeightVertex(0),
	InvbetaLS(0),
	yIntercept(0),
	InvbetaLSError(0),
	yInterceptError(0),
	chi2Dof(0),
	nHits(0),
	aveHitTimeError(0)
	  {}
	
};


#endif
