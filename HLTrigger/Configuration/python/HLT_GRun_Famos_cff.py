# /dev/CMSSW_7_1_1/GRun/V14 (CMSSW_7_1_0_pre7_HLT3)

import FWCore.ParameterSet.Config as cms
from FastSimulation.HighLevelTrigger.HLTSetup_cff import *


HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_7_1_1/GRun/V14')
)

HLTIter4PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTIter3PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTIter2PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTIter1PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.2 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTPSetbJetRegionalTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTPSetTrajectoryFilterL3 = cms.PSet( 
  minPt = cms.double( 0.5 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 1000000000 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTPSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTPSetTrajectoryFilterForElectrons = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minPt = cms.double( 2.0 ),
  minHitsMinPt = cms.int32( -1 ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTPSetMuonCkfTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 )
)
HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 9 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTPSetCkfTrajectoryFilterForHI = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minPt = cms.double( 11.0 )
)
HLTPSetCkfTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTPSetCkf3HitTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
HLTIter4Tau3MuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4Tau3MuESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 )
)
HLTIter4PSetTrajectoryBuilderITReg = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter4PSetTrajectoryBuilderITPA = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTrackerPA" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter4PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 )
)
HLTIter3Tau3MuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter3PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3Tau3MuESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter3PSetTrajectoryBuilderITReg = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter3PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter3PSetTrajectoryBuilderITPA = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter3PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTrackerPA" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter3PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter3PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter2Tau3MuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2Tau3MuESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter2PSetTrajectoryBuilderITReg = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter2PSetTrajectoryBuilderITPA = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTrackerPA" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter2PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter1Tau3MuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1Tau3MuESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter1PSetTrajectoryBuilderITReg = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter1PSetTrajectoryBuilderITPA = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTrackerPA" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTIter1PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTHIAllPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTHIAllPSetCkfTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTHIAllPSetCkf3HitTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkf3HitTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetbJetRegionalTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetbJetRegionalTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetTrajectoryBuilderL3 = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterL3" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetTrajectoryBuilderITReg = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTrackerReg" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetTrajectoryBuilderForElectrons = cms.PSet( 
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterForElectrons" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPElectronChi2" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 90.0 )
)
HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiEffTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetCkfTrajectoryBuilderForHI = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTrackerForHI" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetCkfTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetCkf3HitTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkf3HitTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTHIAllPSetMuonCkfTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltHIAllESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetMuonCkfTrajectoryBuilderSeedHit = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( True ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
HLTPSetMuonCkfTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
hltESSEcalSeverityLevel = cms.ESSource( "EmptyESSource",
  iovIsRunNotTime = cms.bool( True ),
  recordName = cms.string( "EcalSeverityLevelAlgoRcd" ),
  firstValid = cms.vuint32( 1 )
)
hltESSBTagRecord = cms.ESSource( "EmptyESSource",
  iovIsRunNotTime = cms.bool( True ),
  recordName = cms.string( "JetTagComputerRecord" ),
  firstValid = cms.vuint32( 1 )
)
CSCINdexerESSource = cms.ESSource( "EmptyESSource",
  iovIsRunNotTime = cms.bool( True ),
  recordName = cms.string( "CSCIndexerRecord" ),
  firstValid = cms.vuint32( 1 )
)
CSCChannelMapperESSource = cms.ESSource( "EmptyESSource",
  iovIsRunNotTime = cms.bool( True ),
  recordName = cms.string( "CSCChannelMapperRecord" ),
  firstValid = cms.vuint32( 1 )
)

AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" )
)
CSCChannelMapperESProducer = cms.ESProducer( "CSCChannelMapperESProducer",
  AlgoName = cms.string( "CSCChannelMapperStartup" )
)
CSCIndexerESProducer = cms.ESProducer( "CSCIndexerESProducer",
  AlgoName = cms.string( "CSCIndexerStartup" )
)
CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
  applyAlignment = cms.bool( False ),
  hcalTopologyConstants = cms.PSet( 
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
CastorDbProducer = cms.ESProducer( "CastorDbProducer",
  appendToDataLabel = cms.string( "" )
)
ClusterShapeHitFilterESProducer = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "ClusterShapeHitFilter" ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
  applyAlignment = cms.bool( False ),
  hcalTopologyConstants = cms.PSet( 
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
MaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
OppositeMaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "CosmicNavigationSchool" ),
  SimpleMagneticField = cms.string( "" )
)
ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
ecalSeverityLevel = cms.ESProducer( "EcalSeverityLevelESProducer",
  dbstatusMask = cms.PSet( 
    kGood = cms.vuint32( 0 ),
    kProblematic = cms.vuint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ),
    kRecovered = cms.vuint32(  ),
    kTime = cms.vuint32(  ),
    kWeird = cms.vuint32(  ),
    kBad = cms.vuint32( 11, 12, 13, 14, 15, 16 )
  ),
  timeThresh = cms.double( 2.0 ),
  flagMask = cms.PSet( 
    kGood = cms.vstring( 'kGood' ),
    kProblematic = cms.vstring( 'kPoorReco',
      'kPoorCalib',
      'kNoisy',
      'kSaturated' ),
    kRecovered = cms.vstring( 'kLeadingEdgeRecovered',
      'kTowerRecovered' ),
    kTime = cms.vstring( 'kOutOfTime' ),
    kWeird = cms.vstring( 'kWeird',
      'kDiWeird' ),
    kBad = cms.vstring( 'kFaultyHardware',
      'kDead',
      'kKilled' )
  )
)
hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  RecoveredRecHitBits = cms.vstring( 'TimingAddedBit',
    'TimingSubtractedBit' ),
  SeverityLevels = cms.VPSet( 
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerProb' ),
      Level = cms.int32( 1 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HSCP_R1R2',
  'HSCP_FracLeader',
  'HSCP_OuterEnergy',
  'HSCP_ExpFit',
  'ADCSaturationBit',
  'HBHEIsolatedNoise',
  'AddedSimHcalNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellExcludeFromHBHENoiseSummary' ),
      Level = cms.int32( 5 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEHpdHitMultiplicity',
  'HBHEPulseShape',
  'HOBit',
  'HFInTimeWindow',
  'ZDCBit',
  'CalibrationBit',
  'TimingErrorBit',
  'HBHETriangleNoise',
  'HBHETS4TS5Noise' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 8 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HFLongShort',
  'HFPET',
  'HFS8S1Ratio',
  'HFDigiTime' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 11 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEFlatNoise',
  'HBHESpikeNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerMask' ),
      Level = cms.int32( 12 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellHot' ),
      Level = cms.int32( 15 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellOff',
        'HcalCellDead' ),
      Level = cms.int32( 20 )
    )
  ),
  DropChannelStatusBits = cms.vstring( 'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead' )
)
hltCombinedSecondaryVertex = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  categoryVariableName = cms.string( "vertexCategory" ),
  trackSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( -99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVRecoVertex',
    'CombinedSVPseudoVertex',
    'CombinedSVNoVertex' ),
  correctVertexMass = cms.bool( True ),
  charmCut = cms.double( 1.5 ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackPseudoSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( 2.0 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  trackFlip = cms.bool( False )
)
hltESPAK4CaloL1L2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK5L1FastJetCorrectionESProducer',
    'hltESPAK5L2RelativeCorrectionESProducer',
    'hltESPAK5L3AbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
hltESPAK4CaloL2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK5L2RelativeCorrectionESProducer',
    'hltESPAK5L3AbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
hltESPAK4PFL1L2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK5L1PFFastJetCorrectionESProducer',
    'hltESPAK5L2PFRelativeCorrectionESProducer',
    'hltESPAK5L3PFAbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
hltESPAK4PFNoPUL1L2L3 = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK5L1PFNoPUFastJetCorrectionESProducer',
    'hltESPAK5L2PFNoPURelativeCorrectionESProducer',
    'hltESPAK5L3PFNoPUAbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
hltESPAK5L1FastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  srcRho = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
  algorithm = cms.string( "AK5CaloHLT" ),
  level = cms.string( "L1FastJet" )
)
hltESPAK5L1PFFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  srcRho = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
  algorithm = cms.string( "AK5PFHLT" ),
  level = cms.string( "L1FastJet" )
)
hltESPAK5L1PFNoPUFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  srcRho = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
  algorithm = cms.string( "AK5PFchsHLT" ),
  level = cms.string( "L1FastJet" )
)
hltESPAK5L2PFNoPURelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5PFchsHLT" ),
  level = cms.string( "L2Relative" )
)
hltESPAK5L2PFRelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5PFHLT" ),
  level = cms.string( "L2Relative" )
)
hltESPAK5L2RelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5CaloHLT" ),
  level = cms.string( "L2Relative" )
)
hltESPAK5L3AbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5CaloHLT" ),
  level = cms.string( "L3Absolute" )
)
hltESPAK5L3PFAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5PFHLT" ),
  level = cms.string( "L3Absolute" )
)
hltESPAK5L3PFNoPUAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK5PFchsHLT" ),
  level = cms.string( "L3Absolute" )
)
hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
hltESPBwdAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPBwdAnalyticalPropagator" ),
  PropagationDirection = cms.string( "oppositeToMomentum" )
)
hltESPBwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPBwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
hltESPChi2EstimatorForRefit = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 100000.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2EstimatorForRefit" )
)
hltESPChi2MeasurementEstimator = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator" )
)
hltESPChi2MeasurementEstimator16 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 16.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator16" )
)
hltESPChi2MeasurementEstimator9 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator9" )
)
hltESPCloseComponentsMerger5D = cms.ESProducer( "CloseComponentsMergerESProducer5D",
  ComponentName = cms.string( "hltESPCloseComponentsMerger5D" ),
  MaxComponents = cms.int32( 12 ),
  DistanceMeasure = cms.string( "hltESPKullbackLeiblerDistance5D" )
)
hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPEcalRegionCablingESProducer = cms.ESProducer( "EcalRegionCablingESProducer",
  esMapping = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) )
)
hltESPElectronChi2 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 2000.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPElectronChi2" )
)
hltESPElectronMaterialEffects = cms.ESProducer( "GsfMaterialEffectsESProducer",
  BetheHeitlerParametrization = cms.string( "BetheHeitler_cdfmom_nC6_O5.par" ),
  EnergyLossUpdator = cms.string( "GsfBetheHeitlerUpdator" ),
  ComponentName = cms.string( "hltESPElectronMaterialEffects" ),
  MultipleScatteringUpdator = cms.string( "MultipleScatteringUpdator" ),
  Mass = cms.double( 5.11E-4 ),
  BetheHeitlerCorrection = cms.int32( 2 )
)
hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
)
hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
)
hltESPFittingSmootherIT = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 10.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPFittingSmootherIT" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
hltESPFwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPFwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
hltESPGlobalDetLayerGeometry = cms.ESProducer( "GlobalDetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPGlobalDetLayerGeometry" )
)
hltESPGsfElectronFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPGsfTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPGsfTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPGsfElectronFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
hltESPGsfTrajectoryFitter = cms.ESProducer( "GsfTrajectoryFitterESProducer",
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectoryFitter" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  GeometricalPropagator = cms.string( "hltESPAnalyticalPropagator" )
)
hltESPGsfTrajectorySmoother = cms.ESProducer( "GsfTrajectorySmootherESProducer",
  ErrorRescaling = cms.double( 100.0 ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectorySmoother" ),
  GeometricalPropagator = cms.string( "hltESPBwdAnalyticalPropagator" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" )
)
hltESPHITTRHBuilderWithoutRefit = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "Fake" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "Fake" ),
  ComponentName = cms.string( "hltESPHITTRHBuilderWithoutRefit" )
)
hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPRKFitter" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPRKSmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" )
)
hltESPKullbackLeiblerDistance5D = cms.ESProducer( "DistanceBetweenComponentsESProducer5D",
  ComponentName = cms.string( "hltESPKullbackLeiblerDistance5D" ),
  DistanceMeasure = cms.string( "KullbackLeibler" )
)
hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
hltESPMeasurementTrackerForHI = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TID = cms.PSet( 
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTrackerForHI" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
hltESPMeasurementTrackerReg = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTrackerReg" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
)
hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  useLAAlignmentOffsets = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  UseErrorsFromTemplates = cms.bool( True ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  size_cutY = cms.double( 3.0 ),
  size_cutX = cms.double( 3.0 ),
  TruncatePixelCharge = cms.bool( True ),
  useLAWidthFromDB = cms.bool( False ),
  IrradiationBiasCorrection = cms.bool( False ),
  inflate_errors = cms.bool( False ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  Alpha2Order = cms.bool( True )
)
hltESPPixelCPETemplateReco = cms.ESProducer( "PixelCPETemplateRecoESProducer",
  DoLorentz = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPETemplateReco" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  speed = cms.int32( -2 ),
  UseClusterSplitter = cms.bool( False )
)
hltESPPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.03 ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
hltESPRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
hltESPRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKSmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True )
)
hltESPSiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagator" )
)
hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAny" )
)
hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" )
)
hltESPSmartPropagatorOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorOpposite" )
)
hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  distance = cms.double( 0.5 )
)
hltESPSoftLeptonByPt = cms.ESProducer( "LeptonTaggerByPtESProducer",
  ipSign = cms.string( "any" )
)
hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" )
)
hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
)
hltESPStraightLinePropagator = cms.ESProducer( "StraightLinePropagatorESProducer",
  ComponentName = cms.string( "hltESPStraightLinePropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
hltESPStripCPEfromTrackAngle = cms.ESProducer( "StripCPEESProducer",
  TanDiffusionAngle = cms.double( 0.01 ),
  UncertaintyScaling = cms.double( 1.42 ),
  ThicknessRelativeUncertainty = cms.double( 0.02 ),
  MaybeNoiseThreshold = cms.double( 3.5 ),
  ComponentName = cms.string( "hltESPStripCPEfromTrackAngle" ),
  MinimumUncertainty = cms.double( 0.01 ),
  ComponentType = cms.string( "StripCPEfromTrackAngle" ),
  NoiseThreshold = cms.double( 2.3 )
)
hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" )
)
hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPETemplateReco" ),
  ComponentName = cms.string( "hltESPTTRHBuilderAngleAndTemplate" )
)
hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" )
)
hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
)
hltESPTrackCounting3D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDecayLength = cms.double( 5.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  nthTrack = cms.int32( 1 )
)
hltESPTrackCounting3D2nd = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDecayLength = cms.double( 5.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  nthTrack = cms.int32( 2 )
)
hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( False )
)
hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedSeeds" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( True )
)
hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
hltHIAllESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltHIAllESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
siPixelQualityESProducer = cms.ESProducer( "SiPixelQualityESProducer",
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiPixelQualityFromDbRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiPixelDetVOffRcd" ),
      tag = cms.string( "" )
    )
  )
)
siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer" )
siStripBackPlaneCorrectionDepESProducer = cms.ESProducer( "SiStripBackPlaneCorrectionDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  BackPlaneCorrectionDeconvMode = cms.PSet( 
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  BackPlaneCorrectionPeakMode = cms.PSet( 
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
siStripLorentzAngleDepESProducer = cms.ESProducer( "SiStripLorentzAngleDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  LorentzAngleDeconvMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  LorentzAnglePeakMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
sistripconn = cms.ESProducer( "SiStripConnectivity" )
trackerTopologyConstants = cms.ESProducer( "TrackerTopologyEP",
  pxb_layerMask = cms.uint32( 15 ),
  tib_str_int_extStartBit = cms.uint32( 10 ),
  tib_layerMask = cms.uint32( 7 ),
  tib_str_fw_bwStartBit = cms.uint32( 12 ),
  pxf_bladeMask = cms.uint32( 63 ),
  pxb_moduleStartBit = cms.uint32( 2 ),
  pxb_ladderStartBit = cms.uint32( 8 ),
  pxb_layerStartBit = cms.uint32( 16 ),
  tec_wheelStartBit = cms.uint32( 14 ),
  tib_str_fw_bwMask = cms.uint32( 3 ),
  tec_ringStartBit = cms.uint32( 5 ),
  tib_moduleStartBit = cms.uint32( 2 ),
  tib_sterMask = cms.uint32( 3 ),
  tid_sideStartBit = cms.uint32( 13 ),
  tid_wheelStartBit = cms.uint32( 11 ),
  tid_ringMask = cms.uint32( 3 ),
  tid_sterMask = cms.uint32( 3 ),
  tec_petal_fw_bwStartBit = cms.uint32( 12 ),
  tec_ringMask = cms.uint32( 7 ),
  tib_strMask = cms.uint32( 63 ),
  tec_sterMask = cms.uint32( 3 ),
  tec_sideStartBit = cms.uint32( 18 ),
  pxb_moduleMask = cms.uint32( 63 ),
  pxf_panelStartBit = cms.uint32( 8 ),
  tid_sideMask = cms.uint32( 3 ),
  tob_moduleMask = cms.uint32( 7 ),
  tid_ringStartBit = cms.uint32( 9 ),
  pxf_sideMask = cms.uint32( 3 ),
  appendToDataLabel = cms.string( "" ),
  pxf_diskStartBit = cms.uint32( 16 ),
  tib_str_int_extMask = cms.uint32( 3 ),
  tec_moduleMask = cms.uint32( 7 ),
  tob_sterMask = cms.uint32( 3 ),
  tob_rod_fw_bwMask = cms.uint32( 3 ),
  tob_layerStartBit = cms.uint32( 14 ),
  tec_petal_fw_bwMask = cms.uint32( 3 ),
  tib_layerStartBit = cms.uint32( 14 ),
  tec_sterStartBit = cms.uint32( 0 ),
  tid_moduleMask = cms.uint32( 31 ),
  tib_sterStartBit = cms.uint32( 0 ),
  tid_sterStartBit = cms.uint32( 0 ),
  pxf_moduleStartBit = cms.uint32( 2 ),
  pxf_diskMask = cms.uint32( 15 ),
  pxf_sideStartBit = cms.uint32( 23 ),
  tid_module_fw_bwStartBit = cms.uint32( 7 ),
  tob_layerMask = cms.uint32( 7 ),
  tid_module_fw_bwMask = cms.uint32( 3 ),
  tob_rod_fw_bwStartBit = cms.uint32( 12 ),
  tec_petalMask = cms.uint32( 15 ),
  pxb_ladderMask = cms.uint32( 255 ),
  tec_moduleStartBit = cms.uint32( 2 ),
  tec_sideMask = cms.uint32( 3 ),
  tob_rodMask = cms.uint32( 127 ),
  tib_strStartBit = cms.uint32( 4 ),
  tec_wheelMask = cms.uint32( 15 ),
  tob_rodStartBit = cms.uint32( 5 ),
  pxf_panelMask = cms.uint32( 3 ),
  tib_moduleMask = cms.uint32( 3 ),
  pxf_bladeStartBit = cms.uint32( 10 ),
  tid_wheelMask = cms.uint32( 3 ),
  tob_sterStartBit = cms.uint32( 0 ),
  tid_moduleStartBit = cms.uint32( 2 ),
  tec_petalStartBit = cms.uint32( 8 ),
  tob_moduleStartBit = cms.uint32( 2 ),
  pxf_moduleMask = cms.uint32( 63 )
)

hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
hltL1sL1SingleMu12 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu12" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreMu17NoFilters = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltL1fL1sMu12L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu12" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "l1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet( 
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      minTime = cms.double( -3.0 ),
      stepTwoFromDigi = cms.bool( False ),
      doVdriftCorr = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      maxTime = cms.double( 420.0 ),
      tTrigModeConfig = cms.PSet( 
        vPropWire = cms.double( 24.4 ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 0 ),
        wirePropCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        doWirePropCorrection = cms.bool( True ),
        doT0Correction = cms.bool( True ),
        debug = cms.untracked.bool( False )
      ),
      useUncertDB = cms.bool( False )
    ),
    dtDigiLabel = cms.InputTag( "simMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" )
)
hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    Reco4DAlgoConfig = cms.PSet( 
      segmCleanerMode = cms.int32( 2 ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      recAlgoConfig = cms.PSet( 
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        minTime = cms.double( -3.0 ),
        stepTwoFromDigi = cms.bool( False ),
        doVdriftCorr = cms.bool( False ),
        debug = cms.untracked.bool( False ),
        maxTime = cms.double( 420.0 ),
        tTrigModeConfig = cms.PSet( 
          vPropWire = cms.double( 24.4 ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 0 ),
          wirePropCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          doWirePropCorrection = cms.bool( True ),
          doT0Correction = cms.bool( True ),
          debug = cms.untracked.bool( False )
        )
      ),
      nSharedHitsMax = cms.int32( 2 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      Reco2DAlgoConfig = cms.PSet( 
        segmCleanerMode = cms.int32( 2 ),
        recAlgoConfig = cms.PSet( 
          tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
          minTime = cms.double( -3.0 ),
          stepTwoFromDigi = cms.bool( False ),
          doVdriftCorr = cms.bool( False ),
          debug = cms.untracked.bool( False ),
          maxTime = cms.double( 420.0 ),
          tTrigModeConfig = cms.PSet( 
            vPropWire = cms.double( 24.4 ),
            doTOFCorrection = cms.bool( True ),
            tofCorrType = cms.int32( 0 ),
            wirePropCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            doWirePropCorrection = cms.bool( True ),
            doT0Correction = cms.bool( True ),
            debug = cms.untracked.bool( False )
          )
        ),
        nSharedHitsMax = cms.int32( 2 ),
        AlphaMaxPhi = cms.double( 1.0 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        MaxAllowedHits = cms.uint32( 50 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        AlphaMaxTheta = cms.double( 0.9 ),
        debug = cms.untracked.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        nUnSharedHitsMin = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nUnSharedHitsMin = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    )
)
hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME1b = cms.double( 0.007 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    UseFivePoleFit = cms.bool( True ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    CSCDebug = cms.untracked.bool( False ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    CSCUseGasGainCorrections = cms.bool( False ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    readBadChambers = cms.bool( True ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    CSCStripClusterSize = cms.untracked.int32( 3 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    readBadChannels = cms.bool( True ),
    UseParabolaFit = cms.bool( False ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    wireDigiTag = cms.InputTag( 'simMuonCSCDigis','MuonCSCWireDigi' ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    UseAverageTime = cms.bool( False ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseStaticPedestals = cms.bool( False ),
    stripDigiTag = cms.InputTag( 'simMuonCSCDigis','MuonCSCStripDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 )
)
hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_psets = cms.VPSet( 
      cms.PSet(  chamber_types = cms.vstring( 'ME1/a',
  'ME1/b',
  'ME1/2',
  'ME1/3',
  'ME2/1',
  'ME2/2',
  'ME3/1',
  'ME3/2',
  'ME4/1',
  'ME4/2' ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet( 
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          ),
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          )
        )
      )
    ),
    algo_type = cms.int32( 1 )
)
hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    rpcDigiLabel = cms.InputTag( "simMuonRPCDigis" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    deadSource = cms.string( "File" ),
    maskSource = cms.string( "File" )
)
hltL2OfflineMuonSeeds = cms.EDProducer( "MuonSeedGenerator",
    SMB_21 = cms.vdouble( 1.043, -0.124, 0.0, 0.183, 0.0, 0.0 ),
    SMB_20 = cms.vdouble( 1.011, -0.052, 0.0, 0.188, 0.0, 0.0 ),
    SMB_22 = cms.vdouble( 1.474, -0.758, 0.0, 0.185, 0.0, 0.0 ),
    OL_2213 = cms.vdouble( 0.117, 0.0, 0.0, 0.044, 0.0, 0.0 ),
    SME_11 = cms.vdouble( 3.295, -1.527, 0.112, 0.378, 0.02, 0.0 ),
    SME_13 = cms.vdouble( -1.286, 1.711, 0.0, 0.356, 0.0, 0.0 ),
    SME_12 = cms.vdouble( 0.102, 0.599, 0.0, 0.38, 0.0, 0.0 ),
    DT_34_2_scale = cms.vdouble( -11.901897, 0.0 ),
    OL_1213_0_scale = cms.vdouble( -4.488158, 0.0 ),
    OL_1222_0_scale = cms.vdouble( -5.810449, 0.0 ),
    DT_13 = cms.vdouble( 0.315, 0.068, -0.127, 0.051, -0.002, 0.0 ),
    DT_12 = cms.vdouble( 0.183, 0.054, -0.087, 0.028, 0.002, 0.0 ),
    DT_14 = cms.vdouble( 0.359, 0.052, -0.107, 0.072, -0.004, 0.0 ),
    CSC_13_3_scale = cms.vdouble( -1.701268, 0.0 ),
    CSC_23 = cms.vdouble( -0.081, 0.113, -0.029, 0.015, 0.008, 0.0 ),
    CSC_24 = cms.vdouble( 0.004, 0.021, -0.002, 0.053, 0.0, 0.0 ),
    OL_2222 = cms.vdouble( 0.107, 0.0, 0.0, 0.04, 0.0, 0.0 ),
    DT_14_2_scale = cms.vdouble( -4.808546, 0.0 ),
    SMB_10 = cms.vdouble( 1.387, -0.038, 0.0, 0.19, 0.0, 0.0 ),
    SMB_11 = cms.vdouble( 1.247, 0.72, -0.802, 0.229, -0.075, 0.0 ),
    SMB_12 = cms.vdouble( 2.128, -0.956, 0.0, 0.199, 0.0, 0.0 ),
    SME_21 = cms.vdouble( -0.529, 1.194, -0.358, 0.472, 0.086, 0.0 ),
    SME_22 = cms.vdouble( -1.207, 1.491, -0.251, 0.189, 0.243, 0.0 ),
    DT_13_2_scale = cms.vdouble( -4.257687, 0.0 ),
    CSC_34 = cms.vdouble( 0.062, -0.067, 0.019, 0.021, 0.003, 0.0 ),
    SME_22_0_scale = cms.vdouble( -3.457901, 0.0 ),
    DT_24_1_scale = cms.vdouble( -7.490909, 0.0 ),
    OL_1232_0_scale = cms.vdouble( -5.964634, 0.0 ),
    SMB_32 = cms.vdouble( 0.67, -0.327, 0.0, 0.22, 0.0, 0.0 ),
    SME_13_0_scale = cms.vdouble( 0.104905, 0.0 ),
    SMB_22_0_scale = cms.vdouble( 1.346681, 0.0 ),
    CSC_12_1_scale = cms.vdouble( -6.434242, 0.0 ),
    DT_34 = cms.vdouble( 0.044, 0.004, -0.013, 0.029, 0.003, 0.0 ),
    SME_32 = cms.vdouble( -0.901, 1.333, -0.47, 0.41, 0.073, 0.0 ),
    SME_31 = cms.vdouble( -1.594, 1.482, -0.317, 0.487, 0.097, 0.0 ),
    SMB_32_0_scale = cms.vdouble( -3.054156, 0.0 ),
    crackEtas = cms.vdouble( 0.2, 1.6, 1.7 ),
    SME_11_0_scale = cms.vdouble( 1.325085, 0.0 ),
    SMB_20_0_scale = cms.vdouble( 1.486168, 0.0 ),
    DT_13_1_scale = cms.vdouble( -4.520923, 0.0 ),
    CSC_24_1_scale = cms.vdouble( -6.055701, 0.0 ),
    CSC_01_1_scale = cms.vdouble( -1.915329, 0.0 ),
    DT_23 = cms.vdouble( 0.13, 0.023, -0.057, 0.028, 0.004, 0.0 ),
    DT_24 = cms.vdouble( 0.176, 0.014, -0.051, 0.051, 0.003, 0.0 ),
    SMB_12_0_scale = cms.vdouble( 2.283221, 0.0 ),
    SMB_30_0_scale = cms.vdouble( -3.629838, 0.0 ),
    SME_42 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    SME_41 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    CSC_12_2_scale = cms.vdouble( -1.63622, 0.0 ),
    DT_34_1_scale = cms.vdouble( -13.783765, 0.0 ),
    CSC_34_1_scale = cms.vdouble( -11.520507, 0.0 ),
    OL_2213_0_scale = cms.vdouble( -7.239789, 0.0 ),
    CSC_13_2_scale = cms.vdouble( -6.077936, 0.0 ),
    CSC_12_3_scale = cms.vdouble( -1.63622, 0.0 ),
    SME_21_0_scale = cms.vdouble( -0.040862, 0.0 ),
    OL_1232 = cms.vdouble( 0.184, 0.0, 0.0, 0.066, 0.0, 0.0 ),
    DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
    SMB_10_0_scale = cms.vdouble( 2.448566, 0.0 ),
    EnableDTMeasurement = cms.bool( True ),
    DT_24_2_scale = cms.vdouble( -6.63094, 0.0 ),
    CSC_23_2_scale = cms.vdouble( -6.079917, 0.0 ),
    scaleDT = cms.bool( True ),
    DT_12_2_scale = cms.vdouble( -3.518165, 0.0 ),
    OL_1222 = cms.vdouble( 0.848, -0.591, 0.0, 0.062, 0.0, 0.0 ),
    CSC_23_1_scale = cms.vdouble( -19.084285, 0.0 ),
    OL_1213 = cms.vdouble( 0.96, -0.737, 0.0, 0.052, 0.0, 0.0 ),
    CSC_02 = cms.vdouble( 0.612, -0.207, 0.0, 0.067, -0.001, 0.0 ),
    CSC_03 = cms.vdouble( 0.787, -0.338, 0.029, 0.101, -0.008, 0.0 ),
    CSC_01 = cms.vdouble( 0.166, 0.0, 0.0, 0.031, 0.0, 0.0 ),
    DT_23_1_scale = cms.vdouble( -5.320346, 0.0 ),
    SMB_30 = cms.vdouble( 0.505, -0.022, 0.0, 0.215, 0.0, 0.0 ),
    SMB_31 = cms.vdouble( 0.549, -0.145, 0.0, 0.207, 0.0, 0.0 ),
    crackWindow = cms.double( 0.04 ),
    CSC_14_3_scale = cms.vdouble( -1.969563, 0.0 ),
    SMB_31_0_scale = cms.vdouble( -3.323768, 0.0 ),
    DT_12_1_scale = cms.vdouble( -3.692398, 0.0 ),
    SMB_21_0_scale = cms.vdouble( 1.58384, 0.0 ),
    DT_23_2_scale = cms.vdouble( -5.117625, 0.0 ),
    SME_12_0_scale = cms.vdouble( 2.279181, 0.0 ),
    DT_14_1_scale = cms.vdouble( -5.644816, 0.0 ),
    beamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    SMB_11_0_scale = cms.vdouble( 2.56363, 0.0 ),
    CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
    CSC_13 = cms.vdouble( 0.901, -1.302, 0.533, 0.045, 0.005, 0.0 ),
    CSC_14 = cms.vdouble( 0.606, -0.181, -0.002, 0.111, -0.003, 0.0 ),
    OL_2222_0_scale = cms.vdouble( -7.667231, 0.0 ),
    EnableCSCMeasurement = cms.bool( True ),
    CSC_12 = cms.vdouble( -0.161, 0.254, -0.047, 0.042, -0.007, 0.0 )
)
hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "l1extraParticles" ),
    L1MaxEta = cms.double( 2.5 ),
    OfflineSeedLabel = cms.untracked.InputTag( "hltL2OfflineMuonSeeds" ),
    L1MinPt = cms.double( 0.0 ),
    L1MinQuality = cms.uint32( 1 ),
    GMTReadoutCollection = cms.InputTag( "gmtDigis" ),
    UseUnassociatedL1 = cms.bool( False ),
    UseOfflineSeed = cms.untracked.bool( True ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" )
)
hltL2Muons = cms.EDProducer( "L2MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny',
        'hltESPFastSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
    SeedTransformerParameters = cms.PSet( 
      Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      NMinRecHits = cms.uint32( 2 ),
      UseSubRecHits = cms.bool( False ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      RescaleError = cms.double( 100.0 )
    ),
    L2TrajBuilderParameters = cms.PSet( 
      DoRefit = cms.bool( False ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      FilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        FitDirection = cms.string( "insideOut" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 1000.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 0 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet( 
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        NMinRecHits = cms.uint32( 2 ),
        UseSubRecHits = cms.bool( False ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        RescaleError = cms.double( 100.0 )
      ),
      DoBackwardFilter = cms.bool( True ),
      SeedPosition = cms.string( "in" ),
      BWFilterParameters = cms.PSet( 
        NumberOfSigma = cms.double( 3.0 ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        FitDirection = cms.string( "outsideIn" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 100.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 0 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        BWSeedType = cms.string( "fromGenerator" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False )
    ),
    DoSeedRefit = cms.bool( False ),
    TrackLoaderParameters = cms.PSet( 
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      DoSmoothing = cms.bool( False ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( True )
    ),
    MuonTrajectoryBuilder = cms.string( "Exhaustive" )
)
hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
hltL2fL1sMu12L2Filtered12 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1fL1sMu12L1Filtered0" ),
    MinPt = cms.double( 12.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
hltL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 ),
      maxChi2 = cms.double( 40.0 ),
      errorMatrixPset = cms.PSet( 
        atIP = cms.bool( True ),
        action = cms.string( "use" ),
        errorMatrixValuesPSet = cms.PSet( 
          pf3_V12 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V13 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V11 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V14 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V15 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          pf3_V33 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          pf3_V44 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          pf3_V22 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V23 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V45 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V55 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V34 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V35 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V25 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V24 = cms.PSet( 
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          )
        )
      ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      manySeeds = cms.bool( False ),
      copyMuonRecHit = cms.bool( False ),
      ComponentName = cms.string( "TSGForRoadSearch" ),
      MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSteppingHelixPropagatorOpposite',
        'hltESPSteppingHelixPropagatorAlong' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet(  ),
    PtCut = cms.double( 1.0 )
)
hltL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIState" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
hltL3NoFiltersMuonsOIState = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "offlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIState" ),
      tkTrajBeamSpot = cms.InputTag( "offlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 9.0E99 ),
      tkTrajMaxDXYBeamSpot = cms.double( 9.0E99 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
hltL3NoFiltersTrajSeedOIHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltL3NoFiltersMuonsOIState" ),
      iterativeTSG = cms.PSet( 
        ErrorRescaling = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "unused" ),
        MaxChi2 = cms.double( 40.0 ),
        errorMatrixPset = cms.PSet( 
          atIP = cms.bool( True ),
          action = cms.string( "use" ),
          errorMatrixValuesPSet = cms.PSet( 
            pf3_V12 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V13 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V11 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V14 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V15 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
            pf3_V33 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            zAxis = cms.vdouble( -3.14159, 3.14159 ),
            pf3_V44 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
            pf3_V22 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V23 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V45 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V55 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V34 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V35 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V25 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V24 = cms.PSet( 
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            )
          )
        ),
        UpdateState = cms.bool( True ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        SelectState = cms.bool( False ),
        SigmaZ = cms.double( 25.0 ),
        ResetMethod = cms.string( "matrix" ),
        ComponentName = cms.string( "TSGFromPropagation" ),
        UseVertexState = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
        MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial',
        'hltESPSmartPropagatorAnyOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
hltL3NoFiltersTrackCandidateFromL2OIHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3NoFiltersTrajSeedOIHit" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    maxNSeeds = cms.uint32( 100000 )
)
hltL3NoFiltersTkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3NoFiltersTrackCandidateFromL2OIHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
hltL3NoFiltersMuonsOIHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "offlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3NoFiltersTkTracksFromL2OIHit" ),
      tkTrajBeamSpot = cms.InputTag( "offlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 9.0E99 ),
      tkTrajMaxDXYBeamSpot = cms.double( 9.0E99 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
hltL3NoFiltersTkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3NoFiltersMuonsOIState','hltL3NoFiltersMuonsOIHit' )
)
hltL3NoFiltersTrajSeedIOHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet( 
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltL3NoFiltersTkFromL2OICombination" ),
      iterativeTSG = cms.PSet( 
        firstTSG = cms.PSet( 
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            ComponentName = cms.string( "StandardHitTripletGenerator" ),
            GeneratorPSet = cms.PSet( 
              useBending = cms.bool( True ),
              useFixedPreFiltering = cms.bool( False ),
              maxElement = cms.uint32( 0 ),
              phiPreFiltering = cms.double( 0.3 ),
              extraHitRPhitolerance = cms.double( 0.06 ),
              useMultScattering = cms.bool( True ),
              ComponentName = cms.string( "PixelTripletHLTGenerator" ),
              extraHitRZtolerance = cms.double( 0.06 ),
              SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
            ),
            SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        ),
        PSetNames = cms.vstring( 'firstTSG',
          'secondTSG' ),
        ComponentName = cms.string( "CombinedTSG" ),
        thirdTSG = cms.PSet( 
          PSetNames = cms.vstring( 'endcapTSG',
            'barrelTSG' ),
          barrelTSG = cms.PSet(  ),
          endcapTSG = cms.PSet( 
            ComponentName = cms.string( "TSGFromOrderedHits" ),
            OrderedHitsFactoryPSet = cms.PSet( 
              maxElement = cms.uint32( 0 ),
              ComponentName = cms.string( "StandardHitPairGenerator" ),
              useOnDemandTracker = cms.untracked.int32( 0 ),
              SeedingLayers = cms.InputTag( "hltMixedLayerPairs" )
            ),
            TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
          ),
          etaSeparation = cms.double( 2.0 ),
          ComponentName = cms.string( "DualByEtaTSG" )
        ),
        secondTSG = cms.PSet( 
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet( 
            maxElement = cms.uint32( 0 ),
            ComponentName = cms.string( "StandardHitPairGenerator" ),
            useOnDemandTracker = cms.untracked.int32( 0 ),
            SeedingLayers = cms.InputTag( "hltPixelLayerPairs" )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet( 
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      OnDemand = cms.double( -1.0 ),
      Rescale_Dz = cms.double( 3.0 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Rescale_phi = cms.double( 3.0 ),
      Eta_fixed = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      Eta_min = cms.double( 0.1 ),
      Phi_fixed = cms.double( 0.2 ),
      DeltaR = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      Rescale_eta = cms.double( 3.0 ),
      Phi_min = cms.double( 0.1 ),
      UseVertex = cms.bool( False ),
      beamSpot = cms.InputTag( "offlineBeamSpot" )
    ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet( 
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
hltL3NoFiltersTrackCandidateFromL2IOHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltL3NoFiltersTrajSeedIOHit" ),
    reverseTrajectories = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    maxNSeeds = cms.uint32( 100000 )
)
hltL3NoFiltersTkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3NoFiltersTrackCandidateFromL2IOHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
hltL3NoFiltersMuonsIOHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "offlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3NoFiltersTkTracksFromL2IOHit" ),
      tkTrajBeamSpot = cms.InputTag( "offlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 9.0E99 ),
      tkTrajMaxDXYBeamSpot = cms.double( 9.0E99 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
hltL3NoFiltersTrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag( 'hltL3NoFiltersTrajSeedIOHit','hltL3TrajSeedOIState','hltL3NoFiltersTrajSeedOIHit' )
)
hltL3NoFiltersTrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
    labels = cms.VInputTag( 'hltL3NoFiltersTrackCandidateFromL2IOHit','hltL3NoFiltersTrackCandidateFromL2OIHit','hltL3TrackCandidateFromL2OIState' )
)
hltL3NoFiltersTkTracksMergeStep1 = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltL3TkTracksFromL2OIState" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltL3NoFiltersTkTracksFromL2OIHit" ),
    LostHitPenalty = cms.double( 0.0 ),
    FoundHitBonus = cms.double( 100.0 )
)
hltL3NoFiltersTkTracksFromL2 = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltL3NoFiltersTkTracksMergeStep1" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltL3NoFiltersTkTracksFromL2IOHit" ),
    LostHitPenalty = cms.double( 0.0 ),
    FoundHitBonus = cms.double( 100.0 )
)
hltL3NoFiltersMuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3NoFiltersMuonsOIState','hltL3NoFiltersMuonsOIHit','hltL3NoFiltersMuonsIOHit' )
)
hltL3NoFiltersMuons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3NoFiltersMuonsOIState','hltL3NoFiltersMuonsOIHit','hltL3NoFiltersMuonsIOHit' )
)
hltL3NoFiltersMuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag( "hltL3NoFiltersMuonsLinksCombination" ),
    InputObjects = cms.InputTag( "hltL3NoFiltersMuons" ),
    MuonPtOption = cms.string( "Tracker" )
)
hltL3NoFiltersfL1sMu12L3Filtered17 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sMu12L2Filtered12" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3NoFiltersMuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinPt = cms.double( 17.0 )
)
hltL1sMu16 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu16" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreMu40 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltL1fL1sMu16L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sMu16" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "l1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
hltL2fL1sMu16L1f0L2Filtered16Q = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1fL1sMu16L1Filtered0" ),
    MinPt = cms.double( 16.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0, 1, 0, 1 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 0.9, 1.5, 2.1, 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0, 2, 0, 2 )
)
hltL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "offlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIState" ),
      tkTrajBeamSpot = cms.InputTag( "offlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 20.0 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.1 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
hltL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2OIHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
hltL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "offlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIHit" ),
      tkTrajBeamSpot = cms.InputTag( "offlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 20.0 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.1 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
hltL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit' )
)
hltL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltL3TrackCandidateFromL2IOHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
hltL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet( 
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet( 
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "offlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet( 
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2IOHit" ),
      tkTrajBeamSpot = cms.InputTag( "offlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 20.0 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.1 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet( 
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
hltL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag( 'hltL3TrajSeedIOHit','hltL3TrajSeedOIState','hltL3TrajSeedOIHit' )
)
hltL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
    labels = cms.VInputTag( 'hltL3TrackCandidateFromL2IOHit','hltL3TrackCandidateFromL2OIHit','hltL3TrackCandidateFromL2OIState' )
)
hltL3TkTracksMergeStep1 = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltL3TkTracksFromL2OIState" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltL3TkTracksFromL2OIHit" ),
    LostHitPenalty = cms.double( 0.0 ),
    FoundHitBonus = cms.double( 100.0 )
)
hltL3TkTracksFromL2 = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltL3TkTracksMergeStep1" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltL3TkTracksFromL2IOHit" ),
    LostHitPenalty = cms.double( 0.0 ),
    FoundHitBonus = cms.double( 100.0 )
)
hltL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
hltL3Muons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState','hltL3MuonsOIHit','hltL3MuonsIOHit' )
)
hltL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag( "hltL3MuonsLinksCombination" ),
    InputObjects = cms.InputTag( "hltL3Muons" ),
    MuonPtOption = cms.string( "Tracker" )
)
hltL3fL1sMu16L1f0L2f16QL3Filtered40Q = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sMu16L1f0L2Filtered16Q" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinPt = cms.double( 40.0 )
)
hltPreIsoMu24IterTrk02 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltL3fL1sMu16L1f0L2f16QL3Filtered24Q = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sMu16L1f0L2Filtered16Q" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinPt = cms.double( 24.0 )
)
hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    tccUnpacking = cms.bool( True ),
    FedLabel = cms.InputTag( "listfeds" ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    feIdCheck = cms.bool( True ),
    silentMode = cms.untracked.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    eventPut = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    numbXtalTSamples = cms.int32( 10 ),
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    DoRegional = cms.bool( False ),
    feUnpacking = cms.bool( True ),
    forceToKeepFRData = cms.bool( False ),
    headerUnpacking = cms.bool( True ),
    memUnpacking = cms.bool( True )
)
hltEcalPreshowerDigis = cms.EDProducer( "ESRawToDigi",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    debugMode = cms.untracked.bool( False ),
    InstanceES = cms.string( "" ),
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ),
    ESdigiCollection = cms.string( "" )
)
hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    alphaEB = cms.double( 1.138 ),
    alphaEE = cms.double( 1.89 ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    AlphaBetaFilename = cms.untracked.string( "NOFILE" ),
    betaEB = cms.double( 1.655 ),
    MinAmplEndcap = cms.double( 14.0 ),
    MinAmplBarrel = cms.double( 8.0 ),
    algo = cms.string( "EcalUncalibRecHitWorkerWeights" ),
    betaEE = cms.double( 1.4 ),
    UseDynamicPedestal = cms.bool( True ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" )
)
hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeFEToBeRecovered = cms.string( "eeFE" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" )
)
hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    cleaningConfig = cms.PSet( 
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vint32(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    recoverEEFE = cms.bool( True ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    EBLaserMAX = cms.double( 3.0 ),
    flagsMapDBReco = cms.vint32( 0, 0, 0, 0, 4, -1, -1, -1, 4, 4, 7, 7, 7, 8, 9 ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    EELaserMAX = cms.double( 8.0 ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    recoverEEIsolatedChannels = cms.bool( False )
)
hltEcalPreshowerRecHit = cms.EDProducer( "ESRecHitProducer",
    ESRecoAlgo = cms.int32( 0 ),
    ESrechitCollection = cms.string( "EcalRecHitsES" ),
    algo = cms.string( "ESRecHitWorker" ),
    ESdigiCollection = cms.InputTag( "hltEcalPreshowerDigis" )
)
hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    EBThreshold = cms.double( 0.07 ),
    UseRejectedHitsOnly = cms.bool( False ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
hltFixedGridRhoFastjetAllCaloForMuons = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 2.5 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" )
)
hltL3CaloMuonCorrectedIsolations = cms.EDProducer( "L2MuonIsolationProducer",
    WriteIsolatorFloat = cms.bool( True ),
    IsolatorPSet = cms.PSet( 
      ConeSizesRel = cms.vdouble( 0.3 ),
      EffAreaSFEndcap = cms.double( 1.16 ),
      CutAbsoluteIso = cms.bool( True ),
      AndOrCuts = cms.bool( True ),
      RhoSrc = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
      ConeSizes = cms.vdouble( 0.3 ),
      ComponentName = cms.string( "CutsIsolatorWithCorrection" ),
      ReturnRelativeSum = cms.bool( False ),
      RhoScaleBarrel = cms.double( 1.0 ),
      EffAreaSFBarrel = cms.double( 1.73 ),
      CutRelativeIso = cms.bool( False ),
      EtaBounds = cms.vdouble( 2.411 ),
      Thresholds = cms.vdouble( 9.9999999E7 ),
      ReturnAbsoluteSum = cms.bool( True ),
      ThresholdsRel = cms.vdouble( 9.9999999E7 ),
      EtaBoundsRel = cms.vdouble( 2.411 ),
      RhoScaleEndcap = cms.double( 1.0 ),
      RhoMax = cms.double( 9.9999999E7 ),
      UseRhoCorrection = cms.bool( True )
    ),
    StandAloneCollectionLabel = cms.InputTag( "hltL3MuonCandidates" ),
    ExtractorPSet = cms.PSet( 
      DR_Veto_H = cms.double( 0.1 ),
      Vertex_Constraint_Z = cms.bool( False ),
      Threshold_H = cms.double( 0.5 ),
      ComponentName = cms.string( "CaloExtractor" ),
      Threshold_E = cms.double( 0.2 ),
      DR_Max = cms.double( 1.0 ),
      DR_Veto_E = cms.double( 0.07 ),
      Weight_E = cms.double( 1.0 ),
      Vertex_Constraint_XY = cms.bool( False ),
      DepositLabel = cms.untracked.string( "EcalPlusHcal" ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForAll" ),
      Weight_H = cms.double( 1.0 )
    )
)
hltL3MuonVertex = cms.EDProducer( "VertexFromTrackProducer",
    verbose = cms.untracked.bool( False ),
    useTriggerFilterElectrons = cms.bool( False ),
    beamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
    isRecoCandidate = cms.bool( True ),
    trackLabel = cms.InputTag( "hltL3MuonCandidates" ),
    useTriggerFilterMuons = cms.bool( False ),
    useBeamSpot = cms.bool( True ),
    vertexLabel = cms.InputTag( "notUsed" ),
    triggerFilterElectronsSrc = cms.InputTag( "notUsed" ),
    triggerFilterMuonsSrc = cms.InputTag( "notUsed" ),
    useVertex = cms.bool( False )
)
hltPixelVerticesL3MuonReg = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracksL3MuonReg" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
hltL3MuonCombRelIsolationsIterTrkRegIter02 = cms.EDProducer( "L3MuonCombinedRelativeIsolationProducer",
    printDebug = cms.bool( False ),
    CutsPSet = cms.PSet( 
      ConeSizes = cms.vdouble( 0.3 ),
      ComponentName = cms.string( "SimpleCuts" ),
      Thresholds = cms.vdouble( 0.15 ),
      maxNTracks = cms.int32( -1 ),
      EtaBounds = cms.vdouble( 2.411 ),
      applyCutsORmaxNTracks = cms.bool( False )
    ),
    OutputMuIsoDeposits = cms.bool( True ),
    TrackPt_Min = cms.double( -1.0 ),
    CaloDepositsLabel = cms.InputTag( "hltL3CaloMuonCorrectedIsolations" ),
    CaloExtractorPSet = cms.PSet( 
      DR_Veto_H = cms.double( 0.1 ),
      Vertex_Constraint_Z = cms.bool( False ),
      Threshold_H = cms.double( 0.5 ),
      ComponentName = cms.string( "CaloExtractor" ),
      Threshold_E = cms.double( 0.2 ),
      DR_Max = cms.double( 0.3 ),
      DR_Veto_E = cms.double( 0.07 ),
      Weight_E = cms.double( 1.0 ),
      Vertex_Constraint_XY = cms.bool( False ),
      DepositLabel = cms.untracked.string( "EcalPlusHcal" ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForAll" ),
      Weight_H = cms.double( 1.0 )
    ),
    inputMuonCollection = cms.InputTag( "hltL3MuonCandidates" ),
    TrkExtractorPSet = cms.PSet( 
      DR_VetoPt = cms.double( 0.025 ),
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltIter2L3MuonMergedReg" ),
      ReferenceRadius = cms.double( 6.0 ),
      BeamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
      ComponentName = cms.string( "PixelTrackExtractor" ),
      DR_Max = cms.double( 0.3 ),
      Diff_r = cms.double( 0.1 ),
      PropagateTracksToRadius = cms.bool( True ),
      Chi2Prob_Min = cms.double( -1.0 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "PXLS" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      VetoLeadingTrack = cms.bool( True ),
      PtVeto_Min = cms.double( 2.0 )
    ),
    UseRhoCorrectedCaloDeposits = cms.bool( True ),
    UseCaloIso = cms.bool( True )
)
hltL3crIsoL1sMu16L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15IterTrk02 = cms.EDFilter( "HLTMuonIsoFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL3fL1sMu16L1f0L2f16QL3Filtered24Q" ),
    MinN = cms.int32( 1 ),
    IsolatorPSet = cms.PSet(  ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    DepTag = cms.VInputTag( 'hltL3MuonCombRelIsolationsIterTrkRegIter02' )
)
hltL1sL1DoubleMu33HighQ = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu3er_HighQ_WdEta22" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreDoubleMu4NoFiltersJpsiDisplaced = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltDimuon33L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu33HighQ" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "l1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
hltDimuon33L2PreFiltered0 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltDimuon33L1Filtered0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
hltDoubleMu4NoFiltersJpsiDisplacedL3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltL3NoFiltersMuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltDimuon33L2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 4.0 ),
    MaxInvMass = cms.vdouble( 3.3 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 6.9 ),
    MaxDr = cms.double( 2.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 0.5 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.2 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 2.9 )
)
hltDisplacedmumuVtxProducerDoubleMu4NoFiltersJpsi = cms.EDProducer( "HLTDisplacedmumuVtxProducer",
    Src = cms.InputTag( "hltL3NoFiltersMuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltDoubleMu4NoFiltersJpsiDisplacedL3Filtered" ),
    MinPt = cms.double( 0.0 ),
    ChargeOpt = cms.int32( -1 ),
    MaxEta = cms.double( 2.5 ),
    MaxInvMass = cms.double( 999999.0 ),
    MinPtPair = cms.double( 0.0 ),
    MinInvMass = cms.double( 0.0 )
)
hltDisplacedmumuFilterDoubleMu4NoFiltersJpsi = cms.EDFilter( "HLTDisplacedmumuFilter",
    saveTags = cms.bool( True ),
    MuonTag = cms.InputTag( "hltL3NoFiltersMuonCandidates" ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinVtxProbability = cms.double( 0.1 ),
    MaxLxySignificance = cms.double( -1.0 ),
    DisplacedVertexTag = cms.InputTag( "hltDisplacedmumuVtxProducerDoubleMu4NoFiltersJpsi" ),
    FastAccept = cms.bool( True ),
    MinCosinePointingAngle = cms.double( 0.9 ),
    MaxNormalisedChi2 = cms.double( 999999.0 ),
    MinLxySignificance = cms.double( 3.0 )
)
hltL1sL1DoubleMu10MuOpenORDoubleMu103p5 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu_10_Open OR L1_DoubleMu_10_3p5" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreMu17Mu8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltL1DoubleMu10MuOpenOR3p5L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu10MuOpenORDoubleMu103p5" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "l1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
hltL2pfL1DoubleMu10MuOpenOR3p5L1f0L2PreFiltered0 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1DoubleMu10MuOpenOR3p5L1Filtered0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
hltL2fL1DoubleMu10MuOpenOR3p5L1f0L2Filtered10 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1DoubleMu10MuOpenOR3p5L1Filtered0" ),
    MinPt = cms.double( 10.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2pfL1DoubleMu10MuOpenOR3p5L1f0L2PreFiltered0" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 2 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinPt = cms.double( 8.0 )
)
hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1DoubleMu10MuOpenOR3p5L1f0L2Filtered10" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinPt = cms.double( 17.0 )
)
hltDiMuonGlb17Glb8DzFiltered0p2 = cms.EDFilter( "HLT2MuonMuonDZ",
    saveTags = cms.bool( True ),
    originTag1 = cms.VInputTag( 'hltL3MuonCandidates' ),
    originTag2 = cms.VInputTag( 'hltL3MuonCandidates' ),
    MinN = cms.int32( 1 ),
    triggerType1 = cms.int32( 83 ),
    triggerType2 = cms.int32( 83 ),
    MinDR = cms.double( 0.001 ),
    MaxDZ = cms.double( 0.2 ),
    inputTag1 = cms.InputTag( "hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8" ),
    checkSC = cms.bool( False ),
    inputTag2 = cms.InputTag( "hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17" )
)
hltPreMu17TkMu8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltL1fL1sDoubleMu10MuOpenOR3p5L1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu10MuOpenORDoubleMu103p5" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "l1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
hltL2fL1sDoubleMu10MuOpenOR3p5L1f0L2Filtered10 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1fL1sDoubleMu10MuOpenOR3p5L1Filtered0" ),
    MinPt = cms.double( 10.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
hltL3fL1sMu10MuOpenOR3p5L1f0L2f10L3Filtered17 = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 9999.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sDoubleMu10MuOpenOR3p5L1f0L2Filtered10" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 9999.0 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinPt = cms.double( 17.0 )
)
hltMuTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 1.0E9 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    InputVertexCollection = cms.InputTag( "" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    InputCollection = cms.InputTag( "hltPixelTracks" ),
    originRadius = cms.double( 1.0E9 )
)
hltDiMuonMerging = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltL3TkTracksFromL2" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltMuCtfTracks" ),
    LostHitPenalty = cms.double( 0.0 ),
    FoundHitBonus = cms.double( 100.0 )
)
hltDiMuonLinks = cms.EDProducer( "MuonLinksProducerForHLT",
    pMin = cms.double( 2.5 ),
    InclusiveTrackerTrackCollection = cms.InputTag( "hltDiMuonMerging" ),
    shareHitFraction = cms.double( 0.8 ),
    LinkCollection = cms.InputTag( "hltL3MuonsLinksCombination" ),
    ptMin = cms.double( 2.5 )
)
hltGlbTrkMuons = cms.EDProducer( "MuonIdProducer",
    TrackExtractorPSet = cms.PSet( 
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltPFMuonMerging" ),
      BeamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
      ComponentName = cms.string( "TrackExtractor" ),
      DR_Max = cms.double( 1.0 ),
      Diff_r = cms.double( 0.1 ),
      Chi2Prob_Min = cms.double( -1.0 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" )
    ),
    maxAbsEta = cms.double( 3.0 ),
    fillGlobalTrackRefits = cms.bool( False ),
    arbitrationCleanerOptions = cms.PSet( 
      Clustering = cms.bool( True ),
      ME1a = cms.bool( True ),
      ClusterDPhi = cms.double( 0.6 ),
      OverlapDTheta = cms.double( 0.02 ),
      Overlap = cms.bool( True ),
      OverlapDPhi = cms.double( 0.0786 ),
      ClusterDTheta = cms.double( 0.02 )
    ),
    globalTrackQualityInputTag = cms.InputTag( "glbTrackQual" ),
    addExtraSoftMuons = cms.bool( False ),
    debugWithTruthMatching = cms.bool( False ),
    CaloExtractorPSet = cms.PSet( 
      PrintTimeReport = cms.untracked.bool( False ),
      DR_Max = cms.double( 1.0 ),
      DepositInstanceLabels = cms.vstring( 'ecal',
        'hcal',
        'ho' ),
      Noise_HE = cms.double( 0.2 ),
      NoiseTow_EB = cms.double( 0.04 ),
      NoiseTow_EE = cms.double( 0.15 ),
      Threshold_H = cms.double( 0.5 ),
      ServiceParameters = cms.PSet( 
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False )
      ),
      Threshold_E = cms.double( 0.2 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      DepositLabel = cms.untracked.string( "Cal" ),
      UseRecHitsFlag = cms.bool( False ),
      TrackAssociatorParameters = cms.PSet( 
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        dRHcal = cms.double( 1.0 ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForPF" ),
        useEcal = cms.bool( False ),
        dREcal = cms.double( 1.0 ),
        dREcalPreselection = cms.double( 1.0 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
        dRMuon = cms.double( 9999.0 ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceX = cms.double( 5.0 ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        usePreshower = cms.bool( False ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        dRHcalPreselection = cms.double( 1.0 ),
        useMuon = cms.bool( False ),
        useCalo = cms.bool( True ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        dRMuonPreselection = cms.double( 0.2 ),
        truthMatch = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        useHcal = cms.bool( False )
      ),
      Threshold_HO = cms.double( 0.5 ),
      Noise_EE = cms.double( 0.1 ),
      Noise_EB = cms.double( 0.025 ),
      DR_Veto_H = cms.double( 0.1 ),
      CenterConeOnCalIntersection = cms.bool( False ),
      ComponentName = cms.string( "CaloExtractorByAssociator" ),
      Noise_HB = cms.double( 0.2 ),
      DR_Veto_E = cms.double( 0.07 ),
      DR_Veto_HO = cms.double( 0.1 ),
      Noise_HO = cms.double( 0.2 )
    ),
    runArbitrationCleaner = cms.bool( False ),
    fillEnergy = cms.bool( False ),
    TrackerKinkFinderParameters = cms.PSet( 
      usePosition = cms.bool( False ),
      diagonalOnly = cms.bool( False )
    ),
    TimingFillerParameters = cms.PSet( 
      UseDT = cms.bool( True ),
      ErrorDT = cms.double( 6.0 ),
      EcalEnergyCut = cms.double( 0.4 ),
      ErrorEB = cms.double( 2.085 ),
      ErrorCSC = cms.double( 7.4 ),
      CSCTimingParameters = cms.PSet( 
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        CSCTimeOffset = cms.double( 0.0 ),
        CSCStripTimeOffset = cms.double( 0.0 ),
        MatchParameters = cms.PSet( 
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" ),
          DTradius = cms.double( 0.01 ),
          TightMatchDT = cms.bool( False ),
          TightMatchCSC = cms.bool( True )
        ),
        debug = cms.bool( False ),
        UseStripTime = cms.bool( True ),
        CSCStripError = cms.double( 7.0 ),
        CSCWireError = cms.double( 8.6 ),
        CSCWireTimeOffset = cms.double( 0.0 ),
        ServiceParameters = cms.PSet( 
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
          RPCLayers = cms.bool( True )
        ),
        PruneCut = cms.double( 100.0 ),
        UseWireTime = cms.bool( True )
      ),
      DTTimingParameters = cms.PSet( 
        HitError = cms.double( 6.0 ),
        DoWireCorr = cms.bool( False ),
        MatchParameters = cms.PSet( 
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" ),
          DTradius = cms.double( 0.01 ),
          TightMatchDT = cms.bool( False ),
          TightMatchCSC = cms.bool( True )
        ),
        debug = cms.bool( False ),
        DTsegments = cms.InputTag( "hltDt4DSegments" ),
        PruneCut = cms.double( 10000.0 ),
        RequireBothProjections = cms.bool( False ),
        HitsMin = cms.int32( 5 ),
        DTTimeOffset = cms.double( 2.7 ),
        DropTheta = cms.bool( True ),
        UseSegmentT0 = cms.bool( False ),
        ServiceParameters = cms.PSet( 
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
          RPCLayers = cms.bool( True )
        )
      ),
      ErrorEE = cms.double( 6.95 ),
      UseCSC = cms.bool( True ),
      UseECAL = cms.bool( True )
    ),
    inputCollectionTypes = cms.vstring( 'inner tracks',
      'links' ),
    minCaloCompatibility = cms.double( 0.6 ),
    ecalDepositName = cms.string( "ecal" ),
    minP = cms.double( 0.0 ),
    fillIsolation = cms.bool( False ),
    jetDepositName = cms.string( "jets" ),
    hoDepositName = cms.string( "ho" ),
    writeIsoDeposits = cms.bool( False ),
    maxAbsPullX = cms.double( 4.0 ),
    maxAbsPullY = cms.double( 9999.0 ),
    minPt = cms.double( 8.0 ),
    TrackAssociatorParameters = cms.PSet( 
      muonMaxDistanceSigmaX = cms.double( 0.0 ),
      muonMaxDistanceSigmaY = cms.double( 0.0 ),
      CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
      dRHcal = cms.double( 9999.0 ),
      dRPreshowerPreselection = cms.double( 0.2 ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForPF" ),
      useEcal = cms.bool( False ),
      dREcal = cms.double( 9999.0 ),
      dREcalPreselection = cms.double( 0.05 ),
      HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
      dRMuon = cms.double( 9999.0 ),
      propagateAllDirections = cms.bool( True ),
      muonMaxDistanceX = cms.double( 5.0 ),
      muonMaxDistanceY = cms.double( 5.0 ),
      useHO = cms.bool( False ),
      trajectoryUncertaintyTolerance = cms.double( -1.0 ),
      usePreshower = cms.bool( False ),
      DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
      EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
      dRHcalPreselection = cms.double( 0.2 ),
      useMuon = cms.bool( True ),
      useCalo = cms.bool( False ),
      accountForTrajectoryChangeCalo = cms.bool( False ),
      EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      dRMuonPreselection = cms.double( 0.2 ),
      truthMatch = cms.bool( False ),
      HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
      useHcal = cms.bool( False )
    ),
    JetExtractorPSet = cms.PSet( 
      PrintTimeReport = cms.untracked.bool( False ),
      ExcludeMuonVeto = cms.bool( True ),
      TrackAssociatorParameters = cms.PSet( 
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        dRHcal = cms.double( 0.5 ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForPF" ),
        useEcal = cms.bool( False ),
        dREcal = cms.double( 0.5 ),
        dREcalPreselection = cms.double( 0.5 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
        dRMuon = cms.double( 9999.0 ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceX = cms.double( 5.0 ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        usePreshower = cms.bool( False ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        dRHcalPreselection = cms.double( 0.5 ),
        useMuon = cms.bool( False ),
        useCalo = cms.bool( True ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        dRMuonPreselection = cms.double( 0.2 ),
        truthMatch = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        useHcal = cms.bool( False )
      ),
      ServiceParameters = cms.PSet( 
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False )
      ),
      ComponentName = cms.string( "JetExtractor" ),
      DR_Max = cms.double( 1.0 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      JetCollectionLabel = cms.InputTag( "hltAntiKT4CaloJetsPFEt5" ),
      DR_Veto = cms.double( 0.1 ),
      Threshold = cms.double( 5.0 )
    ),
    fillGlobalTrackQuality = cms.bool( False ),
    minPCaloMuon = cms.double( 1.0E9 ),
    maxAbsDy = cms.double( 9999.0 ),
    fillCaloCompatibility = cms.bool( False ),
    fillMatching = cms.bool( True ),
    MuonCaloCompatibility = cms.PSet( 
      allSiPMHO = cms.bool( False ),
      PionTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root" ),
      MuonTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root" ),
      delta_eta = cms.double( 0.02 ),
      delta_phi = cms.double( 0.02 )
    ),
    fillTrackerKink = cms.bool( False ),
    hcalDepositName = cms.string( "hcal" ),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
    inputCollectionLabels = cms.VInputTag( 'hltDiMuonMerging','hltDiMuonLinks' ),
    trackDepositName = cms.string( "tracker" ),
    maxAbsDx = cms.double( 3.0 ),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
    minNumberOfMatches = cms.int32( 1 )
)
hltGlbTrkMuonCands = cms.EDProducer( "L3MuonCandidateProducerFromMuons",
    InputObjects = cms.InputTag( "hltGlbTrkMuons" )
)
hltDiMuonGlbFiltered17TrkFiltered8 = cms.EDFilter( "HLTDiMuonGlbTrkFilter",
    maxNormalizedChi2 = cms.double( 1.0E99 ),
    saveTags = cms.bool( True ),
    minMuonHits = cms.int32( -1 ),
    inputCandCollection = cms.InputTag( "hltGlbTrkMuonCands" ),
    minMass = cms.double( 1.0 ),
    trkMuonId = cms.uint32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minPtMuon1 = cms.double( 17.0 ),
    minPtMuon2 = cms.double( 8.0 ),
    minTrkHits = cms.int32( -1 ),
    inputMuonCollection = cms.InputTag( "hltGlbTrkMuons" ),
    minDR = cms.double( 0.1 ),
    allowedTypeMask = cms.uint32( 255 )
)
hltDiMuonGlb17Trk8DzFiltered0p2 = cms.EDFilter( "HLT2MuonMuonDZ",
    saveTags = cms.bool( True ),
    originTag1 = cms.VInputTag( 'hltGlbTrkMuonCands' ),
    originTag2 = cms.VInputTag( 'hltGlbTrkMuonCands' ),
    MinN = cms.int32( 1 ),
    triggerType1 = cms.int32( 83 ),
    triggerType2 = cms.int32( 83 ),
    MinDR = cms.double( 0.001 ),
    MaxDZ = cms.double( 0.2 ),
    inputTag1 = cms.InputTag( "hltDiMuonGlbFiltered17TrkFiltered8" ),
    checkSC = cms.bool( False ),
    inputTag2 = cms.InputTag( "hltDiMuonGlbFiltered17TrkFiltered8" )
)
hltPreMu17TrkIsoVVLMu8TrkIsoVVL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltL3MuonRelTrkIsolationVVL = cms.EDProducer( "L3MuonCombinedRelativeIsolationProducer",
    printDebug = cms.bool( False ),
    CutsPSet = cms.PSet( 
      ConeSizes = cms.vdouble( 0.3 ),
      ComponentName = cms.string( "SimpleCuts" ),
      Thresholds = cms.vdouble( 0.4 ),
      maxNTracks = cms.int32( -1 ),
      EtaBounds = cms.vdouble( 2.411 ),
      applyCutsORmaxNTracks = cms.bool( False )
    ),
    OutputMuIsoDeposits = cms.bool( True ),
    TrackPt_Min = cms.double( -1.0 ),
    CaloDepositsLabel = cms.InputTag( "notUsed" ),
    CaloExtractorPSet = cms.PSet( 
      DR_Veto_H = cms.double( 0.1 ),
      Vertex_Constraint_Z = cms.bool( False ),
      Threshold_H = cms.double( 0.5 ),
      ComponentName = cms.string( "CaloExtractor" ),
      Threshold_E = cms.double( 0.2 ),
      DR_Max = cms.double( 0.3 ),
      DR_Veto_E = cms.double( 0.07 ),
      Weight_E = cms.double( 1.0 ),
      Vertex_Constraint_XY = cms.bool( False ),
      DepositLabel = cms.untracked.string( "EcalPlusHcal" ),
      CaloTowerCollectionLabel = cms.InputTag( "notUsed" ),
      Weight_H = cms.double( 1.0 )
    ),
    inputMuonCollection = cms.InputTag( "hltL3MuonCandidates" ),
    TrkExtractorPSet = cms.PSet( 
      DR_VetoPt = cms.double( 0.025 ),
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltIter2L3MuonMergedReg" ),
      ReferenceRadius = cms.double( 6.0 ),
      BeamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
      ComponentName = cms.string( "PixelTrackExtractor" ),
      DR_Max = cms.double( 0.3 ),
      Diff_r = cms.double( 0.1 ),
      PropagateTracksToRadius = cms.bool( False ),
      Chi2Prob_Min = cms.double( -1.0 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "PXLS" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      VetoLeadingTrack = cms.bool( False ),
      PtVeto_Min = cms.double( 2.0 )
    ),
    UseRhoCorrectedCaloDeposits = cms.bool( False ),
    UseCaloIso = cms.bool( False )
)
hltDiMuonGlb17Glb8DzFiltered0p2RelTrkIsoFiltered0p4 = cms.EDFilter( "HLTMuonIsoFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltDiMuonGlb17Glb8DzFiltered0p2" ),
    MinN = cms.int32( 2 ),
    IsolatorPSet = cms.PSet(  ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    DepTag = cms.VInputTag( 'hltL3MuonRelTrkIsolationVVL' )
)
hltPreMu17TrkIsoVVLTkMu8TrkIsoVVL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltGlbTrkMuonVertex = cms.EDProducer( "VertexFromTrackProducer",
    verbose = cms.untracked.bool( False ),
    useTriggerFilterElectrons = cms.bool( False ),
    beamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
    isRecoCandidate = cms.bool( True ),
    trackLabel = cms.InputTag( "hltGlbTrkMuonCands" ),
    useTriggerFilterMuons = cms.bool( False ),
    useBeamSpot = cms.bool( True ),
    vertexLabel = cms.InputTag( "notUsed" ),
    triggerFilterElectronsSrc = cms.InputTag( "notUsed" ),
    triggerFilterMuonsSrc = cms.InputTag( "notUsed" ),
    useVertex = cms.bool( False )
)
hltPixelTracksGlbTrkMuonReg = cms.EDProducer( "PixelTrackProducer",
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    useFilterWithES = cms.bool( False ),
    passLabel = cms.string( "Pixel triplet primary tracks with vertex constraint" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.9 ),
        beamSpot = cms.InputTag( "offlineBeamSpot" ),
        nSigmaZ = cms.double( 4.0 ),
        sigmaZVertex = cms.double( 4.0 ),
        fixedError = cms.double( 0.5 ),
        useFixedError = cms.bool( True ),
        useFoundVertices = cms.bool( True ),
        useFakeVertices = cms.bool( True ),
        VertexCollection = cms.InputTag( "hltGlbTrkMuonVertex" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.06 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
    )
)
hltPixelVerticesGlbTrkMuonReg = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracksGlbTrkMuonReg" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
hltGlbTrkMuonRelTrkIsolationVVL = cms.EDProducer( "L3MuonCombinedRelativeIsolationProducer",
    printDebug = cms.bool( False ),
    CutsPSet = cms.PSet( 
      ConeSizes = cms.vdouble( 0.3 ),
      ComponentName = cms.string( "SimpleCuts" ),
      Thresholds = cms.vdouble( 0.4 ),
      maxNTracks = cms.int32( -1 ),
      EtaBounds = cms.vdouble( 2.411 ),
      applyCutsORmaxNTracks = cms.bool( False )
    ),
    OutputMuIsoDeposits = cms.bool( True ),
    TrackPt_Min = cms.double( -1.0 ),
    CaloDepositsLabel = cms.InputTag( "notUsed" ),
    CaloExtractorPSet = cms.PSet( 
      DR_Veto_H = cms.double( 0.1 ),
      Vertex_Constraint_Z = cms.bool( False ),
      Threshold_H = cms.double( 0.5 ),
      ComponentName = cms.string( "CaloExtractor" ),
      Threshold_E = cms.double( 0.2 ),
      DR_Max = cms.double( 0.3 ),
      DR_Veto_E = cms.double( 0.07 ),
      Weight_E = cms.double( 1.0 ),
      Vertex_Constraint_XY = cms.bool( False ),
      DepositLabel = cms.untracked.string( "EcalPlusHcal" ),
      CaloTowerCollectionLabel = cms.InputTag( "notUsed" ),
      Weight_H = cms.double( 1.0 )
    ),
    inputMuonCollection = cms.InputTag( "hltGlbTrkMuonCands" ),
    TrkExtractorPSet = cms.PSet( 
      DR_VetoPt = cms.double( 0.025 ),
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltIter2GlbTrkMuonMergedReg" ),
      ReferenceRadius = cms.double( 6.0 ),
      BeamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
      ComponentName = cms.string( "PixelTrackExtractor" ),
      DR_Max = cms.double( 0.3 ),
      Diff_r = cms.double( 0.1 ),
      PropagateTracksToRadius = cms.bool( False ),
      Chi2Prob_Min = cms.double( -1.0 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "PXLS" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      VetoLeadingTrack = cms.bool( False ),
      PtVeto_Min = cms.double( 2.0 )
    ),
    UseRhoCorrectedCaloDeposits = cms.bool( False ),
    UseCaloIso = cms.bool( False )
)
hltDiMuonGlb17Trk8DzFiltered0p2RelTrkIsoFiltered0p4 = cms.EDFilter( "HLTMuonIsoFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltDiMuonGlb17Trk8DzFiltered0p2" ),
    MinN = cms.int32( 2 ),
    IsolatorPSet = cms.PSet(  ),
    CandTag = cms.InputTag( "hltGlbTrkMuonCands" ),
    DepTag = cms.VInputTag( 'hltGlbTrkMuonRelTrkIsolationVVL' )
)
hltL1sL1SingleEG20ORL1SingleEG22 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG20 OR L1_SingleEG22" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreEle27WP80 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltRechitInRegionsECAL = cms.EDProducer( "EgammaHLTRechitInRegionsProducer",
    l1LowerThr = cms.double( 5.0 ),
    doIsolated = cms.bool( True ),
    useUncalib = cms.bool( False ),
    regionEtaMargin = cms.double( 0.14 ),
    ecalhitLabels = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    regionPhiMargin = cms.double( 0.4 ),
    l1TagNonIsolated = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 0.0 ),
    productLabels = cms.vstring( 'EcalRecHitsEB',
      'EcalRecHitsEE' ),
    l1TagIsolated = cms.InputTag( 'l1extraParticles','Isolated' )
)
hltRechitInRegionsES = cms.EDProducer( "EgammaHLTRechitInRegionsProducer",
    l1LowerThr = cms.double( 5.0 ),
    doIsolated = cms.bool( True ),
    useUncalib = cms.bool( False ),
    regionEtaMargin = cms.double( 0.14 ),
    ecalhitLabels = cms.VInputTag( 'hltEcalPreshowerRecHit:EcalRecHitsES' ),
    regionPhiMargin = cms.double( 0.4 ),
    l1TagNonIsolated = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 0.0 ),
    productLabels = cms.vstring( 'EcalRecHitsES' ),
    l1TagIsolated = cms.InputTag( 'l1extraParticles','Isolated' )
)
hltParticleFlowRecHitECALL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.08 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEBRecHitCreator" )
      ),
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.3 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEERecHitCreator" )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
hltParticleFlowRecHitPSL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsES','EcalRecHitsES' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        ),
        name = cms.string( "PFPSRecHitCreator" )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
hltParticleFlowClusterPSL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 0.3 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "PS1" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        ),
        cms.PSet(  detector = cms.string( "PS2" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSL1Seeded" )
)
hltParticleFlowClusterECALUncorrectedL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      positionCalcForConvergence = cms.PSet( 
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 ),
        minAllowedNormalization = cms.double( 0.0 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        T0_ES = cms.double( 1.2 ),
        T0_EE = cms.double( 3.1 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 1.5 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "ECAL_BARREL" ),
          recHitEnergyNorm = cms.double( 0.08 )
        ),
        cms.PSet(  detector = cms.string( "ECAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.3 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet( 
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 ),
      minAllowedNormalization = cms.double( 0.0 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      T0_ES = cms.double( 1.2 ),
      T0_EE = cms.double( 3.1 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( 0.04 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 10.0 ),
    minS4S1_b = cms.double( -0.024 ),
    singleSpikeThresh = cms.double( 4.0 ),
    detector = cms.string( "ECAL_BARREL" ),
    minS4S1_a = cms.double( 0.04 ),
    energyThresholdModifier = cms.double( 2.0 )
  ),
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.0125 ),
    singleSpikeThresh = cms.double( 15.0 ),
    detector = cms.string( "ECAL_ENDCAP" ),
    minS4S1_a = cms.double( 0.02 ),
    energyThresholdModifier = cms.double( 2.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 8 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.6 ),
          seedingThresholdPt = cms.double( 0.15 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 0.23 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALL1Seeded" )
)
hltParticleFlowClusterECALL1Seeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    minimumPSEnergy = cms.double( 0.0 ),
    inputPS = cms.InputTag( "hltParticleFlowClusterPSL1Seeded" ),
    energyCorrector = cms.PSet( 
      applyCrackCorrections = cms.bool( False ),
      algoName = cms.string( "PFClusterEMEnergyCorrector" )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedL1Seeded" )
)
hltParticleFlowSuperClusterECALL1Seeded = cms.EDProducer( "PFECALSuperClusterProducer",
    PFSuperClusterCollectionEndcap = cms.string( "hltParticleFlowSuperClusterECALEndcap" ),
    doSatelliteClusterMerge = cms.bool( False ),
    thresh_PFClusterBarrel = cms.double( 4.0 ),
    PFBasicClusterCollectionBarrel = cms.string( "hltParticleFlowBasicClusterECALBarrel" ),
    useRegression = cms.bool( False ),
    satelliteMajorityFraction = cms.double( 0.5 ),
    thresh_PFClusterEndcap = cms.double( 4.0 ),
    ESAssociation = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    PFBasicClusterCollectionPreshower = cms.string( "hltParticleFlowBasicClusterECALPreshower" ),
    use_preshower = cms.bool( True ),
    verbose = cms.untracked.bool( False ),
    thresh_SCEt = cms.double( 4.0 ),
    etawidth_SuperClusterEndcap = cms.double( 0.04 ),
    phiwidth_SuperClusterEndcap = cms.double( 0.6 ),
    useDynamicDPhiWindow = cms.bool( True ),
    PFSuperClusterCollectionBarrel = cms.string( "hltParticleFlowSuperClusterECALBarrel" ),
    regressionConfig = cms.PSet( 
      regressionKeyEE = cms.string( "pfscecal_EECorrection_offline" ),
      ecalRecHitsEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
      ecalRecHitsEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
      regressionKeyEB = cms.string( "pfscecal_EBCorrection_offline" ),
      vertexCollection = cms.InputTag( "offlinePrimaryVertices" )
    ),
    applyCrackCorrections = cms.bool( False ),
    satelliteClusterSeedThreshold = cms.double( 50.0 ),
    etawidth_SuperClusterBarrel = cms.double( 0.04 ),
    PFBasicClusterCollectionEndcap = cms.string( "hltParticleFlowBasicClusterECALEndcap" ),
    PFClusters = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    thresh_PFClusterSeedBarrel = cms.double( 4.0 ),
    ClusteringType = cms.string( "Mustache" ),
    EnergyWeight = cms.string( "Raw" ),
    BeamSpot = cms.InputTag( "offlineBeamSpot" ),
    thresh_PFClusterSeedEndcap = cms.double( 4.0 ),
    phiwidth_SuperClusterBarrel = cms.double( 0.6 ),
    thresh_PFClusterES = cms.double( 5.0 ),
    seedThresholdIsET = cms.bool( True ),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string( "hltParticleFlowSuperClusterECALEndcapWithPreshower" )
)
hltEgammaCandidates = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALBarrel' ),
    recoEcalCandidateCollection = cms.string( "" )
)
hltEGL1SingleEG20ORL1SingleEG22Filter = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    saveTags = cms.bool( False ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG20ORL1SingleEG22" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    ncandcut = cms.int32( 1 )
)
hltEG27EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    inputTag = cms.InputTag( "hltEGL1SingleEG20ORL1SingleEG22Filter" ),
    etcutEB = cms.double( 27.0 ),
    etcutEE = cms.double( 27.0 ),
    ncandcut = cms.int32( 1 )
)
hltEgammaClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    ecalRechitEB = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
hltEle27WP80ClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.03 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.01 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaClusterShape" ),
    candTag = cms.InputTag( "hltEG27EtFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaHoverE = cms.EDProducer( "EgammaHLTBcHcalIsolationProducersRegional",
    caloTowerProducer = cms.InputTag( "hltTowerMakerForAll" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.14 ),
    innerCone = cms.double( 0.0 ),
    useSingleTower = cms.bool( False ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    rhoMax = cms.double( 9.9999999E7 ),
    etMin = cms.double( 0.0 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
hltEle27WP80HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.1 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHoverE" ),
    candTag = cms.InputTag( "hltEle27WP80ClusterShapeFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaEcalPFClusterIso = cms.EDProducer( "EgammaHLTEcalPFClusterIsolationProducer",
    energyEndcap = cms.double( 0.0 ),
    effectiveAreaBarrel = cms.double( 0.149 ),
    etaStripBarrel = cms.double( 0.01 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    pfClusterProducer = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    etaStripEndcap = cms.double( 0.015 ),
    drVetoBarrel = cms.double( 0.0 ),
    drMax = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( False ),
    energyBarrel = cms.double( 0.0 ),
    effectiveAreaEndcap = cms.double( 0.097 ),
    drVetoEndcap = cms.double( 0.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 )
)
hltEle27WP80EcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.15 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.2 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEle27WP80HEFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltRegionalTowerForEgamma = cms.EDProducer( "EgammaHLTCaloTowerProducer",
    L1NonIsoCand = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    EMin = cms.double( 0.8 ),
    EtMin = cms.double( 0.5 ),
    L1IsoCand = cms.InputTag( 'l1extraParticles','Isolated' ),
    useTowersInCone = cms.double( 0.8 ),
    towerCollection = cms.InputTag( "hltTowerMakerForAll" )
)
hltParticleFlowRecHitHCALForEgamma = cms.EDProducer( "PFCTRecHitProducer",
    ECAL_Compensate = cms.bool( False ),
    ECAL_Dead_Code = cms.uint32( 10 ),
    MinLongTiming_Cut = cms.double( -5.0 ),
    ECAL_Compensation = cms.double( 0.5 ),
    MaxLongTiming_Cut = cms.double( 5.0 ),
    weight_HFhad = cms.double( 1.0 ),
    ApplyPulseDPG = cms.bool( False ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitCaloTowerNavigator" ) ),
    ECAL_Threshold = cms.double( 10.0 ),
    ApplyTimeDPG = cms.bool( False ),
    caloTowers = cms.InputTag( "hltRegionalTowerForEgamma" ),
    hcalRecHitsHBHE = cms.InputTag( "hltHbhereco" ),
    LongFibre_Fraction = cms.double( 0.1 ),
    MaxShortTiming_Cut = cms.double( 5.0 ),
    HcalMaxAllowedHFLongShortSev = cms.int32( 9 ),
    thresh_Barrel = cms.double( 0.4 ),
    navigation_HF = cms.bool( True ),
    HcalMaxAllowedHFInTimeWindowSev = cms.int32( 9 ),
    HF_Calib_29 = cms.double( 1.07 ),
    LongFibre_Cut = cms.double( 120.0 ),
    EM_Depth = cms.double( 22.0 ),
    weight_HFem = cms.double( 1.0 ),
    LongShortFibre_Cut = cms.double( 1.0E9 ),
    MinShortTiming_Cut = cms.double( -5.0 ),
    HCAL_Calib = cms.bool( True ),
    thresh_HF = cms.double( 0.4 ),
    HcalMaxAllowedHFDigiTimeSev = cms.int32( 9 ),
    thresh_Endcap = cms.double( 0.4 ),
    HcalMaxAllowedChannelStatusSev = cms.int32( 9 ),
    hcalRecHitsHF = cms.InputTag( "hltHfreco" ),
    ShortFibre_Cut = cms.double( 60.0 ),
    ApplyLongShortDPG = cms.bool( True ),
    HF_Calib = cms.bool( True ),
    HAD_Depth = cms.double( 47.0 ),
    ShortFibre_Fraction = cms.double( 0.01 ),
    HCAL_Calib_29 = cms.double( 1.35 )
)
hltParticleFlowClusterHCALForEgamma = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          recHitEnergyNorm = cms.double( 0.8 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_BARREL1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  algoName = cms.string( "RBXAndHPDCleaner" )      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.8 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_BARREL1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.1 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHCALForEgamma" )
)
hltParticleFlowClusterHFEMForEgamma = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HF_EM" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HF_EM" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 1.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.19 ),
    singleSpikeThresh = cms.double( 80.0 ),
    detector = cms.string( "HF_EM" ),
    minS4S1_a = cms.double( 0.11 ),
    energyThresholdModifier = cms.double( 1.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 0 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_EM" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( 'hltParticleFlowRecHitHCALForEgamma','HFEM' )
)
hltParticleFlowClusterHFHADForEgamma = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HF_HAD" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HF_HAD" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 1.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.08 ),
    singleSpikeThresh = cms.double( 120.0 ),
    detector = cms.string( "HF_HAD" ),
    minS4S1_a = cms.double( 0.045 ),
    energyThresholdModifier = cms.double( 1.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 0 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( 'hltParticleFlowRecHitHCALForEgamma','HFHAD' )
)
hltEgammaHcalPFClusterIso = cms.EDProducer( "EgammaHLTHcalPFClusterIsolationProducer",
    energyEndcap = cms.double( 0.0 ),
    useHF = cms.bool( False ),
    effectiveAreaBarrel = cms.double( 0.06 ),
    etaStripBarrel = cms.double( 0.0 ),
    pfClusterProducerHFHAD = cms.InputTag( "hltParticleFlowClusterHFHADForEgamma" ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    etaStripEndcap = cms.double( 0.0 ),
    drVetoBarrel = cms.double( 0.0 ),
    pfClusterProducerHCAL = cms.InputTag( "hltParticleFlowClusterHCALForEgamma" ),
    drMax = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( False ),
    energyBarrel = cms.double( 0.0 ),
    effectiveAreaEndcap = cms.double( 0.089 ),
    drVetoEndcap = cms.double( 0.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    rhoMax = cms.double( 9.9999999E7 ),
    pfClusterProducerHFEM = cms.InputTag( "hltParticleFlowClusterHFEMForEgamma" ),
    rhoScale = cms.double( 1.0 )
)
hltEle27WP80HcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.11 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.11 ),
    thrRegularEB = cms.double( 999999.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEle27WP80EcalIsoFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    endcapSuperClusters = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    SeedConfiguration = cms.PSet( 
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet( 
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        useOnDemandTracker = cms.untracked.int32( 0 ),
        SeedingLayers = cms.InputTag( "hltMixedLayerPairs" )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.004 ),
      LowPtThreshold = cms.double( 3.0 ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( "dummyVertices" )
      ),
      maxHOverE = cms.double( 999999.0 ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      DeltaPhi2 = cms.double( 0.004 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      PhiMax2 = cms.double( 0.004 ),
      preFilteredSeeds = cms.bool( False ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      initialSeeds = cms.InputTag( "globalPixelSeeds:GlobalPixel" ),
      pPhiMax1 = cms.double( 0.08 ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      z2MaxB = cms.double( 0.09 ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( "hltHbhereco" ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      rMinI = cms.double( -0.2 ),
      hOverEConeSize = cms.double( 0.0 ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 ),
      measurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" )
    ),
    barrelSuperClusters = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALBarrel' )
)
hltEle27WP80PixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( False ),
    s_a_phi1B = cms.double( 0.0069 ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    s2_threshold = cms.double( 0.4 ),
    useS = cms.bool( False ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    candTag = cms.InputTag( "hltEle27WP80HcalIsoFilter" ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    s_a_zB = cms.double( 0.012 ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
hltEgammaCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" )
)
hltEgammaCtfTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltEgammaCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
hltEgammaCtfBarrelTracks = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "loose" ),
    minNumberLayers = cms.uint32( 5 ),
    chi2n_par = cms.double( 9999.0 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 4.0 ),
    dz_par2 = cms.vdouble( 100.0, 1.0 ),
    applyAdaptedPVCuts = cms.bool( False ),
    min_eta = cms.double( -1.479 ),
    dz_par1 = cms.vdouble( 100.0, 1.0 ),
    copyTrajectories = cms.untracked.bool( False ),
    vtxNumber = cms.int32( 0 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "offlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( False ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( False ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltEgammaCtfTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "NONE" ),
    max_eta = cms.double( 1.479 ),
    d0_par2 = cms.vdouble( 100.0, 1.0 ),
    d0_par1 = cms.vdouble( 100.0, 1.0 ),
    res_par = cms.vdouble( 1.0, 0.0 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
hltEgammaCtfCleanTracks = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 3 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( True ),
    qualityBit = cms.string( "tight" ),
    minNumberLayers = cms.uint32( 5 ),
    chi2n_par = cms.double( 1.5 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 100.0, 1.0 ),
    applyAdaptedPVCuts = cms.bool( False ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 100.0, 1.0 ),
    copyTrajectories = cms.untracked.bool( False ),
    vtxNumber = cms.int32( 0 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "offlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( False ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( False ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltEgammaCtfTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "NONE" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 100.0, 1.0 ),
    d0_par1 = cms.vdouble( 100.0, 1.0 ),
    res_par = cms.vdouble( 1.0, 0.0 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
hltEgammaCtfBarrelCleanMergedTracks = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.99 ),
    promoteTrackQuality = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( False ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltEgammaCtfBarrelTracks" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltEgammaCtfCleanTracks" ),
    LostHitPenalty = cms.double( 20.0 ),
    FoundHitBonus = cms.double( 5.0 )
)
hltEgammaCtfBarrelORCleanElectrons = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "offlineBeamSpot" ),
    UseGsfTracks = cms.bool( False ),
    TrackProducer = cms.InputTag( "hltEgammaCtfBarrelCleanMergedTracks" ),
    GsfTrackProducer = cms.InputTag( "" )
)
hltEle27WP80OneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    doIsolated = cms.bool( True ),
    saveTags = cms.bool( False ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 0.05 ),
    electronIsolatedProducer = cms.InputTag( "hltEgammaCtfBarrelORCleanElectrons" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEle27WP80PixelMatchFilter" ),
    endcapcut = cms.double( 0.05 )
)
hltEgammaBarrelORCleanDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    variablesAtVtx = cms.bool( True ),
    useSCRefs = cms.bool( False ),
    BSProducer = cms.InputTag( "offlineBeamSpot" ),
    electronProducer = cms.InputTag( "hltEgammaCtfBarrelORCleanElectrons" ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    useTrackProjectionToEcal = cms.bool( False )
)
hltEle27WP80DetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.007 ),
    L1IsoCand = cms.InputTag( "hltEgammaCtfBarrelORCleanElectrons" ),
    thrRegularEB = cms.double( 0.007 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaBarrelORCleanDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltEle27WP80OneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
hltEle27WP80DphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.03 ),
    L1IsoCand = cms.InputTag( "hltEgammaCtfBarrelORCleanElectrons" ),
    thrRegularEB = cms.double( 0.06 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaBarrelORCleanDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltEle27WP80DetaFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
hltVertexFromElectronsProducer = cms.EDProducer( "VertexFromTrackProducer",
    verbose = cms.untracked.bool( False ),
    useTriggerFilterElectrons = cms.bool( True ),
    beamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
    isRecoCandidate = cms.bool( True ),
    trackLabel = cms.InputTag( "hltEgammaCtfBarrelORCleanElectrons" ),
    useTriggerFilterMuons = cms.bool( False ),
    useBeamSpot = cms.bool( True ),
    vertexLabel = cms.InputTag( "None" ),
    triggerFilterElectronsSrc = cms.InputTag( "None" ),
    triggerFilterMuonsSrc = cms.InputTag( "None" ),
    useVertex = cms.bool( False )
)
hltPixelTracksForEgamma = cms.EDProducer( "PixelTrackProducer",
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    useFilterWithES = cms.bool( False ),
    passLabel = cms.string( "Pixel triplet primary tracks with vertex constraint" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.9 ),
        originHalfLength = cms.double( 0.3 ),
        beamSpot = cms.InputTag( "offlineBeamSpot" ),
        useFixedError = cms.bool( True ),
        sigmaZVertex = cms.double( 3.0 ),
        fixedError = cms.double( 0.2 ),
        VertexCollection = cms.InputTag( "hltVertexFromElectronsProducer" ),
        useFoundVertices = cms.bool( True ),
        nSigmaZ = cms.double( 4.0 ),
        useFakeVertices = cms.bool( True )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.06 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
    )
)
hltPixelVerticesForEgamma = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracksForEgamma" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
hltEgammaEleTrackIso = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    useGsfTrack = cms.bool( False ),
    useSCRefs = cms.bool( False ),
    trackProducer = cms.InputTag( "hltIter2MergedForElectrons" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    electronProducer = cms.InputTag( "hltEgammaCtfBarrelORCleanElectrons" ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    beamSpotProducer = cms.InputTag( "offlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoZSpan = cms.double( 0.15 )
)
hltEle27WP80TrackIsoFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCtfBarrelORCleanElectrons" ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEleTrackIso" ),
    candTag = cms.InputTag( "hltEle27WP80DphiFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( 0.05 )
)
hltPreEle27WP80Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltEgammaCkfTrackCandidatesForGSF = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 1000000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryBuilderForElectrons" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPTrajectoryBuilderForElectrons" )
)
hltEgammaGsfTracks = cms.EDProducer( "GsfTrackProducer",
    src = cms.InputTag( "hltEgammaCkfTrackCandidatesForGSF" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    producer = cms.string( "" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPGsfElectronFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "hltESPMeasurementTracker" ),
    AlgorithmName = cms.string( "gsf" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    Propagator = cms.string( "hltESPFwdElectronPropagator" )
)
hltEgammaGsfElectrons = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "offlineBeamSpot" ),
    UseGsfTracks = cms.bool( True ),
    TrackProducer = cms.InputTag( "" ),
    GsfTrackProducer = cms.InputTag( "hltEgammaGsfTracks" )
)
hltEgammaGsfTrackVars = cms.EDProducer( "EgammaHLTGsfTrackVarProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    beamSpotProducer = cms.InputTag( "offlineBeamSpot" ),
    upperTrackNrToRemoveCut = cms.int32( 9999 ),
    lowerTrackNrToRemoveCut = cms.int32( -1 ),
    inputCollection = cms.InputTag( "hltEgammaGsfElectrons" )
)
hltEle27WP80GsfDetaFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.007 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.007 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVars','Deta' ),
    candTag = cms.InputTag( "hltEle27WP80PixelMatchFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle27WP80GsfDphiFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.03 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.06 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVars','Dphi' ),
    candTag = cms.InputTag( "hltEle27WP80GsfDetaFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaEleGsfTrackIso = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    useGsfTrack = cms.bool( True ),
    useSCRefs = cms.bool( True ),
    trackProducer = cms.InputTag( "hltIter2MergedForElectrons" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    electronProducer = cms.InputTag( "hltEgammaGsfElectrons" ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    beamSpotProducer = cms.InputTag( "offlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoZSpan = cms.double( 0.15 )
)
hltEle27WP80GsfTrackIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEleGsfTrackIso" ),
    candTag = cms.InputTag( "hltEle27WP80GsfDphiFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltL1sL1DoubleEG137 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleEG_13_7" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreEle17Ele8Mass50 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltEGL1DoubleEG137Filter = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    saveTags = cms.bool( False ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG137" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    ncandcut = cms.int32( 2 )
)
hltEle17Ele8EtLeg1Filter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    inputTag = cms.InputTag( "hltEGL1DoubleEG137Filter" ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 )
)
hltEle17Ele8EtLeg2Filter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    inputTag = cms.InputTag( "hltEGL1DoubleEG137Filter" ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 2 )
)
hltEle17Ele8ClusterShapeLeg1Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.011 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaClusterShape" ),
    candTag = cms.InputTag( "hltEle17Ele8EtLeg2Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8ClusterShapeLeg2Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 9999.0 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 9999.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaClusterShape" ),
    candTag = cms.InputTag( "hltEle17Ele8EtLeg2Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8HELeg1Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHoverE" ),
    candTag = cms.InputTag( "hltEle17Ele8ClusterShapeLeg1Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8HELeg2Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.15 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.1 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaHoverE" ),
    candTag = cms.InputTag( "hltEle17Ele8ClusterShapeLeg2Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8EcalIsoLeg1Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEle17Ele8HELeg1Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8EcalIsoLeg2Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 9999.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 9999.0 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaEcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEle17Ele8HELeg2Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8HcalIsoLeg1Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEle17Ele8EcalIsoLeg1Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8HcalIsoLeg2Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 9999.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 9999.0 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaHcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEle17Ele8EcalIsoLeg2Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8PixelMatchLeg1Filter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( False ),
    s_a_phi1B = cms.double( 0.0069 ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    s2_threshold = cms.double( 0.4 ),
    useS = cms.bool( False ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    candTag = cms.InputTag( "hltEle17Ele8HcalIsoLeg1Filter" ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    s_a_zB = cms.double( 0.012 ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
hltEle17Ele8PixelMatchLeg2Filter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( False ),
    s_a_phi1B = cms.double( 0.0069 ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    s2_threshold = cms.double( 0.4 ),
    useS = cms.bool( False ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    candTag = cms.InputTag( "hltEle17Ele8HcalIsoLeg2Filter" ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    s_a_zB = cms.double( 0.012 ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
hltPixelMatchElectrons = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "offlineBeamSpot" ),
    UseGsfTracks = cms.bool( False ),
    TrackProducer = cms.InputTag( "hltEgammaCtfTracks" ),
    GsfTrackProducer = cms.InputTag( "" )
)
hltEle17Ele8OneOEMinusOneOPLeg1Filter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    doIsolated = cms.bool( True ),
    saveTags = cms.bool( False ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectrons" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEle17Ele8PixelMatchLeg1Filter" ),
    endcapcut = cms.double( 999.9 )
)
hltEle17Ele8OneOEMinusOneOPLeg2Filter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    doIsolated = cms.bool( True ),
    saveTags = cms.bool( False ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectrons" ),
    ncandcut = cms.int32( 2 ),
    candTag = cms.InputTag( "hltEle17Ele8PixelMatchLeg2Filter" ),
    endcapcut = cms.double( 999.9 )
)
hltEgammaEle3HitDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    variablesAtVtx = cms.bool( True ),
    useSCRefs = cms.bool( False ),
    BSProducer = cms.InputTag( "offlineBeamSpot" ),
    electronProducer = cms.InputTag( "hltPixelMatchElectrons" ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    useTrackProjectionToEcal = cms.bool( False )
)
hltEle17Ele8DetaLeg1Filter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.008 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectrons" ),
    thrRegularEB = cms.double( 0.008 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaEle3HitDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltEle17Ele8OneOEMinusOneOPLeg1Filter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
hltEle17Ele8DetaLeg2Filter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 9999.0 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectrons" ),
    thrRegularEB = cms.double( 9999.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hltEgammaEle3HitDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltEle17Ele8OneOEMinusOneOPLeg2Filter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
hltEle17Ele8DphiLeg1Filter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectrons" ),
    thrRegularEB = cms.double( 0.07 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaEle3HitDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltEle17Ele8DetaLeg1Filter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
hltEle17Ele8DphiLeg2Filter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( False ),
    thrRegularEE = cms.double( 9999.0 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectrons" ),
    thrRegularEB = cms.double( 9999.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hltEgammaEle3HitDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltEle17Ele8DetaLeg2Filter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
hltEgammaEle3HitTrackIso = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    useGsfTrack = cms.bool( False ),
    useSCRefs = cms.bool( False ),
    trackProducer = cms.InputTag( "hltIter2MergedForElectrons" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    electronProducer = cms.InputTag( "hltPixelMatchElectrons" ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    beamSpotProducer = cms.InputTag( "offlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoZSpan = cms.double( 0.15 )
)
hltEle17Ele8TrackIsoLeg1Filter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectrons" ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEle3HitTrackIso" ),
    candTag = cms.InputTag( "hltEle17Ele8DphiLeg1Filter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( 0.05 )
)
hltEle17Ele8TrackIsoLeg2Filter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectrons" ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaEle3HitTrackIso" ),
    candTag = cms.InputTag( "hltEle17Ele8DphiLeg2Filter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( 9999.0 ),
    thrOverPtEB = cms.double( 9999.0 )
)
hltEle17Ele8MassFilter = cms.EDFilter( "HLTPMMassFilter",
    saveTags = cms.bool( True ),
    lowerMassCut = cms.double( 50.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectrons" ),
    isElectron1 = cms.untracked.bool( True ),
    isElectron2 = cms.untracked.bool( True ),
    upperMassCut = cms.double( 999999.0 ),
    candTag = cms.InputTag( "hltEle17Ele8TrackIsoLeg2Filter" ),
    reqOppCharge = cms.untracked.bool( False ),
    nZcandcut = cms.int32( 1 )
)
hltPreEle17Ele8Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltEle17Ele8GsfDetaLeg1Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.008 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.008 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVars','Deta' ),
    candTag = cms.InputTag( "hltEle17Ele8PixelMatchLeg1Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8GsfDetaLeg2Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 10.0 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 10.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVars','Deta' ),
    candTag = cms.InputTag( "hltEle17Ele8PixelMatchLeg2Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8GsfDphiLeg1Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.05 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.07 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVars','Dphi' ),
    candTag = cms.InputTag( "hltEle17Ele8GsfDetaLeg1Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8GsfDphiLeg2Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 10.0 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 10.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVars','Dphi' ),
    candTag = cms.InputTag( "hltEle17Ele8GsfDetaLeg2Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8GsfTrackIsoLeg1Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEleGsfTrackIso" ),
    candTag = cms.InputTag( "hltEle17Ele8GsfDphiLeg1Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle17Ele8GsfTrackIsoLeg2Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 9999.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 9999.0 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaEleGsfTrackIso" ),
    candTag = cms.InputTag( "hltEle17Ele8GsfDphiLeg2Filter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltL1sL1SingleEG22 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG22" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreDoubleEle33CaloIdLGsfTrkIdVL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltEGL1SingleEG22Filter = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    saveTags = cms.bool( False ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG22" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    ncandcut = cms.int32( 1 )
)
hltEG33EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    inputTag = cms.InputTag( "hltEGL1SingleEG22Filter" ),
    etcutEB = cms.double( 33.0 ),
    etcutEE = cms.double( 33.0 ),
    ncandcut = cms.int32( 1 )
)
hltEG33HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHoverE" ),
    candTag = cms.InputTag( "hltEG33EtFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEG33CaloIdLClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.014 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaClusterShape" ),
    candTag = cms.InputTag( "hltEG33HEFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEle33CaloIdLPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    s2_threshold = cms.double( 0.4 ),
    useS = cms.bool( False ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    candTag = cms.InputTag( "hltEG33CaloIdLClusterShapeFilter" ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    s_a_zB = cms.double( 0.012 ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
hltParticleFlowRecHitECALUnseeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.08 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEBRecHitCreator" )
      ),
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.3 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEERecHitCreator" )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
hltParticleFlowRecHitPSUnseeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        ),
        name = cms.string( "PFPSRecHitCreator" )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
hltParticleFlowClusterPSUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 0.3 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "PS1" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        ),
        cms.PSet(  detector = cms.string( "PS2" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSUnseeded" )
)
hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      positionCalcForConvergence = cms.PSet( 
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 ),
        minAllowedNormalization = cms.double( 0.0 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        T0_ES = cms.double( 1.2 ),
        T0_EE = cms.double( 3.1 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 1.5 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "ECAL_BARREL" ),
          recHitEnergyNorm = cms.double( 0.08 )
        ),
        cms.PSet(  detector = cms.string( "ECAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.3 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet( 
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 ),
      minAllowedNormalization = cms.double( 0.0 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      T0_ES = cms.double( 1.2 ),
      T0_EE = cms.double( 3.1 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( 0.04 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 10.0 ),
    minS4S1_b = cms.double( -0.024 ),
    singleSpikeThresh = cms.double( 4.0 ),
    detector = cms.string( "ECAL_BARREL" ),
    minS4S1_a = cms.double( 0.04 ),
    energyThresholdModifier = cms.double( 2.0 )
  ),
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.0125 ),
    singleSpikeThresh = cms.double( 15.0 ),
    detector = cms.string( "ECAL_ENDCAP" ),
    minS4S1_a = cms.double( 0.02 ),
    energyThresholdModifier = cms.double( 2.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 8 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.6 ),
          seedingThresholdPt = cms.double( 0.15 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 0.23 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALUnseeded" )
)
hltParticleFlowClusterECALUnseeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    minimumPSEnergy = cms.double( 0.0 ),
    inputPS = cms.InputTag( "hltParticleFlowClusterPSUnseeded" ),
    energyCorrector = cms.PSet( 
      applyCrackCorrections = cms.bool( False ),
      algoName = cms.string( "PFClusterEMEnergyCorrector" )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedUnseeded" )
)
hltParticleFlowSuperClusterECALUnseeded = cms.EDProducer( "PFECALSuperClusterProducer",
    PFSuperClusterCollectionEndcap = cms.string( "hltParticleFlowSuperClusterECALEndcap" ),
    doSatelliteClusterMerge = cms.bool( False ),
    thresh_PFClusterBarrel = cms.double( 4.0 ),
    PFBasicClusterCollectionBarrel = cms.string( "hltParticleFlowBasicClusterECALBarrel" ),
    useRegression = cms.bool( False ),
    satelliteMajorityFraction = cms.double( 0.5 ),
    thresh_PFClusterEndcap = cms.double( 4.0 ),
    ESAssociation = cms.InputTag( "hltParticleFlowClusterECALUnseeded" ),
    PFBasicClusterCollectionPreshower = cms.string( "hltParticleFlowBasicClusterECALPreshower" ),
    use_preshower = cms.bool( True ),
    verbose = cms.untracked.bool( False ),
    thresh_SCEt = cms.double( 4.0 ),
    etawidth_SuperClusterEndcap = cms.double( 0.04 ),
    phiwidth_SuperClusterEndcap = cms.double( 0.6 ),
    useDynamicDPhiWindow = cms.bool( True ),
    PFSuperClusterCollectionBarrel = cms.string( "hltParticleFlowSuperClusterECALBarrel" ),
    regressionConfig = cms.PSet( 
      regressionKeyEE = cms.string( "pfscecal_EECorrection_offline" ),
      ecalRecHitsEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEE' ),
      ecalRecHitsEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit','EcalRecHitsEB' ),
      regressionKeyEB = cms.string( "pfscecal_EBCorrection_offline" ),
      vertexCollection = cms.InputTag( "offlinePrimaryVertices" )
    ),
    applyCrackCorrections = cms.bool( False ),
    satelliteClusterSeedThreshold = cms.double( 50.0 ),
    etawidth_SuperClusterBarrel = cms.double( 0.04 ),
    PFBasicClusterCollectionEndcap = cms.string( "hltParticleFlowBasicClusterECALEndcap" ),
    PFClusters = cms.InputTag( "hltParticleFlowClusterECALUnseeded" ),
    thresh_PFClusterSeedBarrel = cms.double( 4.0 ),
    ClusteringType = cms.string( "Mustache" ),
    EnergyWeight = cms.string( "Raw" ),
    BeamSpot = cms.InputTag( "offlineBeamSpot" ),
    thresh_PFClusterSeedEndcap = cms.double( 4.0 ),
    phiwidth_SuperClusterBarrel = cms.double( 0.6 ),
    thresh_PFClusterES = cms.double( 5.0 ),
    seedThresholdIsET = cms.bool( True ),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string( "hltParticleFlowSuperClusterECALEndcapWithPreshower" )
)
hltEgammaCandidatesUnseeded = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALUnseeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALUnseeded','hltParticleFlowSuperClusterECALBarrel' ),
    recoEcalCandidateCollection = cms.string( "" )
)
hltEgammaCandidatesWrapperUnseeded = cms.EDFilter( "HLTEgammaTriggerFilterObjectWrapper",
    doIsolated = cms.bool( True ),
    saveTags = cms.bool( False ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    candNonIsolatedTag = cms.InputTag( "" )
)
hltDiEG33EtUnseededFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperUnseeded" ),
    etcutEB = cms.double( 33.0 ),
    etcutEE = cms.double( 33.0 ),
    ncandcut = cms.int32( 2 )
)
hltEgammaHoverEUnseeded = cms.EDProducer( "EgammaHLTBcHcalIsolationProducersRegional",
    caloTowerProducer = cms.InputTag( "hltTowerMakerForAll" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.14 ),
    innerCone = cms.double( 0.0 ),
    useSingleTower = cms.bool( False ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    rhoMax = cms.double( 9.9999999E7 ),
    etMin = cms.double( 0.0 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
hltDiEG33HEUnseededFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaHoverEUnseeded" ),
    candTag = cms.InputTag( "hltDiEG33EtUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaClusterShapeUnseeded = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
hltDiEG33CaloIdLClusterShapeUnseededFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.014 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaClusterShapeUnseeded" ),
    candTag = cms.InputTag( "hltDiEG33HEUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaElectronPixelSeedsUnseeded = cms.EDProducer( "ElectronSeedProducer",
    endcapSuperClusters = cms.InputTag( 'hltParticleFlowSuperClusterECALUnseeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    SeedConfiguration = cms.PSet( 
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet( 
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        useOnDemandTracker = cms.untracked.int32( 0 ),
        SeedingLayers = cms.InputTag( "hltMixedLayerPairs" )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.004 ),
      LowPtThreshold = cms.double( 3.0 ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( "dummyVertices" )
      ),
      maxHOverE = cms.double( 999999.0 ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      DeltaPhi2 = cms.double( 0.004 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      rMinI = cms.double( -0.2 ),
      preFilteredSeeds = cms.bool( False ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      initialSeeds = cms.InputTag( "globalPixelSeeds:GlobalPixel" ),
      pPhiMax1 = cms.double( 0.08 ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      z2MaxB = cms.double( 0.09 ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( "hltHbhereco" ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      PhiMax2 = cms.double( 0.004 ),
      hOverEConeSize = cms.double( 0.0 ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 ),
      measurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" )
    ),
    barrelSuperClusters = cms.InputTag( 'hltParticleFlowSuperClusterECALUnseeded','hltParticleFlowSuperClusterECALBarrel' )
)
hltDiEle33CaloIdLPixelMatchUnseededFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    s2_threshold = cms.double( 0.4 ),
    useS = cms.bool( False ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    candTag = cms.InputTag( "hltDiEG33CaloIdLClusterShapeUnseededFilter" ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    s_a_zB = cms.double( 0.012 ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeedsUnseeded" ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
hltEgammaCkfTrackCandidatesForGSFUnseeded = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltEgammaElectronPixelSeedsUnseeded" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 1000000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryBuilderForElectrons" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPTrajectoryBuilderForElectrons" )
)
hltEgammaGsfTracksUnseeded = cms.EDProducer( "GsfTrackProducer",
    src = cms.InputTag( "hltEgammaCkfTrackCandidatesForGSFUnseeded" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    producer = cms.string( "" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPGsfElectronFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "hltESPMeasurementTracker" ),
    AlgorithmName = cms.string( "gsf" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    Propagator = cms.string( "hltESPFwdElectronPropagator" )
)
hltEgammaGsfElectronsUnseeded = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "offlineBeamSpot" ),
    UseGsfTracks = cms.bool( True ),
    TrackProducer = cms.InputTag( "" ),
    GsfTrackProducer = cms.InputTag( "hltEgammaGsfTracksUnseeded" )
)
hltEgammaGsfTrackVarsUnseeded = cms.EDProducer( "EgammaHLTGsfTrackVarProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    beamSpotProducer = cms.InputTag( "offlineBeamSpot" ),
    upperTrackNrToRemoveCut = cms.int32( 9999 ),
    lowerTrackNrToRemoveCut = cms.int32( -1 ),
    inputCollection = cms.InputTag( "hltEgammaGsfTracksUnseeded" )
)
hltDiEle33CaloIdLGsfTrkIdVLDEtaUnseededFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.02 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.02 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVarsUnseeded','Deta' ),
    candTag = cms.InputTag( "hltDiEle33CaloIdLPixelMatchUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltDiEle33CaloIdLGsfTrkIdVLDPhiUnseededFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.15 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.15 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVarsUnseeded','Dphi' ),
    candTag = cms.InputTag( "hltDiEle33CaloIdLGsfTrkIdVLDEtaUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltL1sL1SingleEG12 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG12" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPrePhoton20CaloIdVLIsoL = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltEGL1SingleEG12Filter = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    saveTags = cms.bool( False ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG12" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    ncandcut = cms.int32( 1 )
)
hltEG20EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    inputTag = cms.InputTag( "hltEGL1SingleEG12Filter" ),
    etcutEB = cms.double( 20.0 ),
    etcutEE = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 )
)
hltEG20CaloIdVLClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.04 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.024 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaClusterShape" ),
    candTag = cms.InputTag( "hltEG20EtFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEG20CaloIdVLHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.15 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHoverE" ),
    candTag = cms.InputTag( "hltEG20CaloIdVLClusterShapeFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEG20CaloIdVLIsoLEcalIsoFilter = cms.EDFilter( "HLTEgammaGenericQuadraticFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( 0.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( 0.0 ),
    thrRegularEE = cms.double( 5.5 ),
    thrOverEEE = cms.double( 0.012 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.012 ),
    thrRegularEB = cms.double( 5.5 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEG20CaloIdVLHEFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEG20CaloIdVLIsoLHcalIsoFilter = cms.EDFilter( "HLTEgammaGenericQuadraticFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( 0.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( 0.0 ),
    thrRegularEE = cms.double( 3.5 ),
    thrOverEEE = cms.double( 0.005 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.005 ),
    thrRegularEB = cms.double( 3.5 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEG20CaloIdVLHEFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltPixelTracksForPhotons = cms.EDProducer( "PixelTrackProducer",
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    useFilterWithES = cms.bool( False ),
    passLabel = cms.string( "Pixel triplet primary tracks with vertex constraint" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.9 ),
        originHalfLength = cms.double( 24.0 ),
        beamSpot = cms.InputTag( "offlineBeamSpot" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.06 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
    )
)
hltPixelVerticesForPhotons = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracksForPhotons" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
hltEgammaHollowTrackIso = cms.EDProducer( "EgammaHLTPhotonTrackIsolationProducersRegional",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    egTrkIsoConeSize = cms.double( 0.29 ),
    trackProducer = cms.InputTag( "hltIter2MergedForPhotons" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    countTracks = cms.bool( False ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.06 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoZSpan = cms.double( 999999.0 )
)
hltEG20CaloIdVLIsoLTrackIsoFilter = cms.EDFilter( "HLTEgammaGenericQuadraticFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( 0.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( 0.0 ),
    thrRegularEE = cms.double( 3.5 ),
    thrOverEEE = cms.double( 0.002 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.002 ),
    thrRegularEB = cms.double( 3.5 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHollowTrackIso" ),
    candTag = cms.InputTag( "hltEG20CaloIdVLIsoLHcalIsoFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltPrePhoton26R9Id85Photon18CaloId10Iso50 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltEG26EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    inputTag = cms.InputTag( "hltEGL1SingleEG22Filter" ),
    etcutEB = cms.double( 26.0 ),
    etcutEE = cms.double( 26.0 ),
    ncandcut = cms.int32( 1 )
)
hltEG26HE10HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( 0.1 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHoverE" ),
    candTag = cms.InputTag( "hltEG26EtFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaR9ID = cms.EDProducer( "EgammaHLTR9IDProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' )
)
hltEG26R9Id85R9Filter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.85 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.85 ),
    lessThan = cms.bool( False ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaR9ID" ),
    candTag = cms.InputTag( "hltEG26HE10HEFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltDiEG18EtUnseededFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperUnseeded" ),
    etcutEB = cms.double( 18.0 ),
    etcutEE = cms.double( 18.0 ),
    ncandcut = cms.int32( 2 )
)
hltDiEG18HE10HEUnseededFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.1 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( 0.1 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaHoverEUnseeded" ),
    candTag = cms.InputTag( "hltDiEG18EtUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaR9IDUnseeded = cms.EDProducer( "EgammaHLTR9IDProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' )
)
hltEG18R9Id85R9UnseededFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.85 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.85 ),
    lessThan = cms.bool( False ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaR9IDUnseeded" ),
    candTag = cms.InputTag( "hltDiEG18HE10HEUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEG18CaloId10ClusterShapeUnseededFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.014 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaClusterShapeUnseeded" ),
    candTag = cms.InputTag( "hltDiEG18HE10HEUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaEcalPFClusterIsoUnseeded = cms.EDProducer( "EgammaHLTEcalPFClusterIsolationProducer",
    energyEndcap = cms.double( 0.0 ),
    effectiveAreaBarrel = cms.double( 0.149 ),
    etaStripBarrel = cms.double( 0.015 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    pfClusterProducer = cms.InputTag( "hltParticleFlowClusterECALUnseeded" ),
    etaStripEndcap = cms.double( 0.0 ),
    drVetoBarrel = cms.double( 0.0 ),
    drMax = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( False ),
    energyBarrel = cms.double( 0.0 ),
    effectiveAreaEndcap = cms.double( 0.097 ),
    drVetoEndcap = cms.double( 0.07 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 )
)
hltEG18CaloId10Iso50EcalIsoUnseededFilter = cms.EDFilter( "HLTEgammaGenericQuadraticFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( 0.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( 0.0 ),
    thrRegularEE = cms.double( 5.0 ),
    thrOverEEE = cms.double( 0.012 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( 0.012 ),
    thrRegularEB = cms.double( 5.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEcalPFClusterIsoUnseeded" ),
    candTag = cms.InputTag( "hltEG18CaloId10ClusterShapeUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltParticleFlowRecHitHCALForEgammaUnseeded = cms.EDProducer( "PFCTRecHitProducer",
    ECAL_Compensate = cms.bool( False ),
    ECAL_Dead_Code = cms.uint32( 10 ),
    MinLongTiming_Cut = cms.double( -5.0 ),
    ECAL_Compensation = cms.double( 0.5 ),
    MaxLongTiming_Cut = cms.double( 5.0 ),
    weight_HFhad = cms.double( 1.0 ),
    ApplyPulseDPG = cms.bool( False ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitCaloTowerNavigator" ) ),
    ECAL_Threshold = cms.double( 10.0 ),
    ApplyTimeDPG = cms.bool( False ),
    caloTowers = cms.InputTag( "hltTowerMakerForAll" ),
    hcalRecHitsHBHE = cms.InputTag( "hltHbhereco" ),
    LongFibre_Fraction = cms.double( 0.1 ),
    MaxShortTiming_Cut = cms.double( 5.0 ),
    HcalMaxAllowedHFLongShortSev = cms.int32( 9 ),
    thresh_Barrel = cms.double( 0.4 ),
    navigation_HF = cms.bool( True ),
    HcalMaxAllowedHFInTimeWindowSev = cms.int32( 9 ),
    HF_Calib_29 = cms.double( 1.07 ),
    LongFibre_Cut = cms.double( 120.0 ),
    EM_Depth = cms.double( 22.0 ),
    weight_HFem = cms.double( 1.0 ),
    LongShortFibre_Cut = cms.double( 1.0E9 ),
    MinShortTiming_Cut = cms.double( -5.0 ),
    HCAL_Calib = cms.bool( True ),
    thresh_HF = cms.double( 0.4 ),
    HcalMaxAllowedHFDigiTimeSev = cms.int32( 9 ),
    thresh_Endcap = cms.double( 0.4 ),
    HcalMaxAllowedChannelStatusSev = cms.int32( 9 ),
    hcalRecHitsHF = cms.InputTag( "hltHfreco" ),
    ShortFibre_Cut = cms.double( 60.0 ),
    ApplyLongShortDPG = cms.bool( True ),
    HF_Calib = cms.bool( True ),
    HAD_Depth = cms.double( 47.0 ),
    ShortFibre_Fraction = cms.double( 0.01 ),
    HCAL_Calib_29 = cms.double( 1.35 )
)
hltParticleFlowClusterHCALForEgammaUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          recHitEnergyNorm = cms.double( 0.8 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_BARREL1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  algoName = cms.string( "RBXAndHPDCleaner" )      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.8 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_BARREL1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.1 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHCALForEgammaUnseeded" )
)
hltParticleFlowClusterHFEMForEgammaUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HF_EM" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HF_EM" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 1.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.19 ),
    singleSpikeThresh = cms.double( 80.0 ),
    detector = cms.string( "HF_EM" ),
    minS4S1_a = cms.double( 0.11 ),
    energyThresholdModifier = cms.double( 1.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 0 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_EM" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( 'hltParticleFlowRecHitHCALForEgammaUnseeded','HFEM' )
)
hltParticleFlowClusterHFHADForEgammaUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HF_HAD" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HF_HAD" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 1.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.08 ),
    singleSpikeThresh = cms.double( 120.0 ),
    detector = cms.string( "HF_HAD" ),
    minS4S1_a = cms.double( 0.045 ),
    energyThresholdModifier = cms.double( 1.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 0 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( 'hltParticleFlowRecHitHCALForEgammaUnseeded','HFHAD' )
)
hltEgammaHcalPFClusterIsoUnseeded = cms.EDProducer( "EgammaHLTHcalPFClusterIsolationProducer",
    energyEndcap = cms.double( 0.0 ),
    useHF = cms.bool( False ),
    effectiveAreaBarrel = cms.double( 0.06 ),
    etaStripBarrel = cms.double( 0.0 ),
    pfClusterProducerHFHAD = cms.InputTag( "hltParticleFlowClusterHFHADForEgammaUnseeded" ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    etaStripEndcap = cms.double( 0.0 ),
    drVetoBarrel = cms.double( 0.0 ),
    pfClusterProducerHCAL = cms.InputTag( "hltParticleFlowClusterHCALForEgammaUnseeded" ),
    drMax = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( False ),
    energyBarrel = cms.double( 0.0 ),
    effectiveAreaEndcap = cms.double( 0.089 ),
    drVetoEndcap = cms.double( 0.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    rhoMax = cms.double( 9.9999999E7 ),
    pfClusterProducerHFEM = cms.InputTag( "hltParticleFlowClusterHFEMForEgammaUnseeded" ),
    rhoScale = cms.double( 1.0 )
)
hltEG18CaloId10Iso50HcalIsoUnseededFilter = cms.EDFilter( "HLTEgammaGenericQuadraticFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( 0.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( False ),
    thrOverE2EB = cms.double( 0.0 ),
    thrRegularEE = cms.double( 5.0 ),
    thrOverEEE = cms.double( 0.005 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( 0.005 ),
    thrRegularEB = cms.double( 5.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHcalPFClusterIsoUnseeded" ),
    candTag = cms.InputTag( "hltEG18CaloId10Iso50EcalIsoUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEgammaHollowTrackIsoUnseeded = cms.EDProducer( "EgammaHLTPhotonTrackIsolationProducersRegional",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    egTrkIsoConeSize = cms.double( 0.29 ),
    trackProducer = cms.InputTag( "hltIter2MergedForPhotons" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    countTracks = cms.bool( False ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.06 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoZSpan = cms.double( 999999.0 )
)
hltEG18CaloId10Iso50TrackIsoUnseededFilter = cms.EDFilter( "HLTEgammaGenericQuadraticFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( 0.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( 0.0 ),
    thrRegularEE = cms.double( 5.0 ),
    thrOverEEE = cms.double( 0.002 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( 0.002 ),
    thrRegularEB = cms.double( 5.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHollowTrackIsoUnseeded" ),
    candTag = cms.InputTag( "hltEG18CaloId10Iso50HcalIsoUnseededFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltEG26R9Id85EG18CaloId10Iso50LegCombFilter = cms.EDFilter( "HLTEgammaDoubleLegCombFilter",
    saveTags = cms.bool( True ),
    nrRequiredSecondLeg = cms.int32( 1 ),
    secondLegLastFilter = cms.InputTag( "hltEG18CaloId10Iso50TrackIsoUnseededFilter" ),
    nrRequiredFirstLeg = cms.int32( 1 ),
    maxMatchDR = cms.double( 0.01 ),
    nrRequiredUniqueLeg = cms.int32( 0 ),
    firstLegLastFilter = cms.InputTag( "hltEG18R9Id85R9UnseededFilter" )
)
hltL1sMu14erORMu16er = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu14er OR L1_SingleMu16er" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreIsoMu17eta2p1LooseIsoPFTau20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltL1fL1sMu14erORMu16erL1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sMu14erORMu16er" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "l1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
hltL2fL1sMu14erORMu16erL1f0L2Filtered14Q = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltL1fL1sMu14erORMu16erL1Filtered0" ),
    MinPt = cms.double( 14.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.1 ),
    MinNhits = cms.vint32( 0, 1, 0, 1 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 0.9, 1.5, 2.1, 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0, 2, 0, 2 )
)
hltL3fL1sMu14erORMu16erL1f0L2f14QL3Filtered17Q = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL2fL1sMu14erORMu16erL1f0L2Filtered14Q" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.1 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    MinPt = cms.double( 17.0 )
)
hltL3MuonCombRelIsolations = cms.EDProducer( "L3MuonCombinedRelativeIsolationProducer",
    printDebug = cms.bool( False ),
    CutsPSet = cms.PSet( 
      ConeSizes = cms.vdouble( 0.3 ),
      ComponentName = cms.string( "SimpleCuts" ),
      Thresholds = cms.vdouble( 0.15 ),
      maxNTracks = cms.int32( -1 ),
      EtaBounds = cms.vdouble( 2.411 ),
      applyCutsORmaxNTracks = cms.bool( False )
    ),
    OutputMuIsoDeposits = cms.bool( True ),
    TrackPt_Min = cms.double( -1.0 ),
    CaloDepositsLabel = cms.InputTag( "hltL3CaloMuonCorrectedIsolations" ),
    CaloExtractorPSet = cms.PSet( 
      DR_Veto_H = cms.double( 0.1 ),
      Vertex_Constraint_Z = cms.bool( False ),
      Threshold_H = cms.double( 0.5 ),
      ComponentName = cms.string( "CaloExtractor" ),
      Threshold_E = cms.double( 0.2 ),
      DR_Max = cms.double( 0.3 ),
      DR_Veto_E = cms.double( 0.07 ),
      Weight_E = cms.double( 1.0 ),
      Vertex_Constraint_XY = cms.bool( False ),
      DepositLabel = cms.untracked.string( "EcalPlusHcal" ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForAll" ),
      Weight_H = cms.double( 1.0 )
    ),
    inputMuonCollection = cms.InputTag( "hltL3MuonCandidates" ),
    TrkExtractorPSet = cms.PSet( 
      DR_VetoPt = cms.double( 0.025 ),
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltPixelTracks" ),
      ReferenceRadius = cms.double( 6.0 ),
      BeamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
      ComponentName = cms.string( "PixelTrackExtractor" ),
      DR_Max = cms.double( 0.3 ),
      Diff_r = cms.double( 0.1 ),
      PropagateTracksToRadius = cms.bool( True ),
      Chi2Prob_Min = cms.double( -1.0 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "PXLS" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      VetoLeadingTrack = cms.bool( True ),
      PtVeto_Min = cms.double( 2.0 )
    ),
    UseRhoCorrectedCaloDeposits = cms.bool( True ),
    UseCaloIso = cms.bool( True )
)
hltL3crIsoL1sMu14erORMu16erL1f0L2f14QL3f17QL3crIsoRhoFiltered0p15 = cms.EDFilter( "HLTMuonIsoFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL3fL1sMu14erORMu16erL1f0L2f14QL3Filtered17Q" ),
    MinN = cms.int32( 1 ),
    IsolatorPSet = cms.PSet(  ),
    CandTag = cms.InputTag( "hltL3MuonCandidates" ),
    DepTag = cms.VInputTag( 'hltL3MuonCombRelIsolations' )
)
hltTowerMakerForPF = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.4 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.4 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 1.8 ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 1.1 ),
    HOThresholdPlus2 = cms.double( 1.1 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 1.2 ),
    HOThresholdMinus1 = cms.double( 1.1 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.4 ),
    EBThreshold = cms.double( 0.07 ),
    UseRejectedHitsOnly = cms.bool( False ),
    UseHcalRecoveredHits = cms.bool( True ),
    HOThresholdMinus2 = cms.double( 1.1 ),
    HOThreshold0 = cms.double( 1.1 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
hltAntiKT4CaloJetsPF = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.4 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltTowerMakerForPF" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltAntiKT4CaloJetsPFEt5 = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAntiKT4CaloJetsPF" ),
    etMin = cms.double( 5.0 )
)
hltTauJet5 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( False ),
    MinPt = cms.double( 5.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAntiKT4CaloJetsPFEt5" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltPFMuonMerging = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltL3TkTracksFromL2" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltIter4Merged" ),
    LostHitPenalty = cms.double( 20.0 ),
    FoundHitBonus = cms.double( 5.0 )
)
hltMuonLinks = cms.EDProducer( "MuonLinksProducerForHLT",
    pMin = cms.double( 2.5 ),
    InclusiveTrackerTrackCollection = cms.InputTag( "hltPFMuonMerging" ),
    shareHitFraction = cms.double( 0.8 ),
    LinkCollection = cms.InputTag( "hltL3MuonsLinksCombination" ),
    ptMin = cms.double( 2.5 )
)
hltMuons = cms.EDProducer( "MuonIdProducer",
    TrackExtractorPSet = cms.PSet( 
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltPFMuonMerging" ),
      BeamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
      ComponentName = cms.string( "TrackExtractor" ),
      DR_Max = cms.double( 1.0 ),
      Diff_r = cms.double( 0.1 ),
      Chi2Prob_Min = cms.double( -1.0 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" )
    ),
    maxAbsEta = cms.double( 3.0 ),
    fillGlobalTrackRefits = cms.bool( False ),
    arbitrationCleanerOptions = cms.PSet( 
      Clustering = cms.bool( True ),
      ME1a = cms.bool( True ),
      ClusterDPhi = cms.double( 0.6 ),
      OverlapDTheta = cms.double( 0.02 ),
      Overlap = cms.bool( True ),
      OverlapDPhi = cms.double( 0.0786 ),
      ClusterDTheta = cms.double( 0.02 )
    ),
    globalTrackQualityInputTag = cms.InputTag( "glbTrackQual" ),
    addExtraSoftMuons = cms.bool( False ),
    debugWithTruthMatching = cms.bool( False ),
    CaloExtractorPSet = cms.PSet( 
      PrintTimeReport = cms.untracked.bool( False ),
      DR_Max = cms.double( 1.0 ),
      DepositInstanceLabels = cms.vstring( 'ecal',
        'hcal',
        'ho' ),
      Noise_HE = cms.double( 0.2 ),
      NoiseTow_EB = cms.double( 0.04 ),
      NoiseTow_EE = cms.double( 0.15 ),
      Threshold_H = cms.double( 0.5 ),
      ServiceParameters = cms.PSet( 
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False )
      ),
      Threshold_E = cms.double( 0.2 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      DepositLabel = cms.untracked.string( "Cal" ),
      UseRecHitsFlag = cms.bool( False ),
      TrackAssociatorParameters = cms.PSet( 
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        dRHcal = cms.double( 1.0 ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForPF" ),
        useEcal = cms.bool( False ),
        dREcal = cms.double( 1.0 ),
        dREcalPreselection = cms.double( 1.0 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
        dRMuon = cms.double( 9999.0 ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceX = cms.double( 5.0 ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        usePreshower = cms.bool( False ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        dRHcalPreselection = cms.double( 1.0 ),
        useMuon = cms.bool( False ),
        useCalo = cms.bool( True ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        dRMuonPreselection = cms.double( 0.2 ),
        truthMatch = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        useHcal = cms.bool( False )
      ),
      Threshold_HO = cms.double( 0.5 ),
      Noise_EE = cms.double( 0.1 ),
      Noise_EB = cms.double( 0.025 ),
      DR_Veto_H = cms.double( 0.1 ),
      CenterConeOnCalIntersection = cms.bool( False ),
      ComponentName = cms.string( "CaloExtractorByAssociator" ),
      Noise_HB = cms.double( 0.2 ),
      DR_Veto_E = cms.double( 0.07 ),
      DR_Veto_HO = cms.double( 0.1 ),
      Noise_HO = cms.double( 0.2 )
    ),
    runArbitrationCleaner = cms.bool( False ),
    fillEnergy = cms.bool( True ),
    TrackerKinkFinderParameters = cms.PSet( 
      usePosition = cms.bool( False ),
      diagonalOnly = cms.bool( False )
    ),
    TimingFillerParameters = cms.PSet( 
      UseDT = cms.bool( True ),
      ErrorDT = cms.double( 6.0 ),
      EcalEnergyCut = cms.double( 0.4 ),
      ErrorEB = cms.double( 2.085 ),
      ErrorCSC = cms.double( 7.4 ),
      CSCTimingParameters = cms.PSet( 
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        CSCTimeOffset = cms.double( 0.0 ),
        CSCStripTimeOffset = cms.double( 0.0 ),
        MatchParameters = cms.PSet( 
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" ),
          DTradius = cms.double( 0.01 ),
          TightMatchDT = cms.bool( False ),
          TightMatchCSC = cms.bool( True )
        ),
        debug = cms.bool( False ),
        UseStripTime = cms.bool( True ),
        CSCStripError = cms.double( 7.0 ),
        CSCWireError = cms.double( 8.6 ),
        CSCWireTimeOffset = cms.double( 0.0 ),
        ServiceParameters = cms.PSet( 
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
          RPCLayers = cms.bool( True )
        ),
        PruneCut = cms.double( 100.0 ),
        UseWireTime = cms.bool( True )
      ),
      DTTimingParameters = cms.PSet( 
        HitError = cms.double( 6.0 ),
        DoWireCorr = cms.bool( False ),
        MatchParameters = cms.PSet( 
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" ),
          DTradius = cms.double( 0.01 ),
          TightMatchDT = cms.bool( False ),
          TightMatchCSC = cms.bool( True )
        ),
        debug = cms.bool( False ),
        DTsegments = cms.InputTag( "hltDt4DSegments" ),
        PruneCut = cms.double( 10000.0 ),
        RequireBothProjections = cms.bool( False ),
        HitsMin = cms.int32( 5 ),
        DTTimeOffset = cms.double( 2.7 ),
        DropTheta = cms.bool( True ),
        UseSegmentT0 = cms.bool( False ),
        ServiceParameters = cms.PSet( 
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
          RPCLayers = cms.bool( True )
        )
      ),
      ErrorEE = cms.double( 6.95 ),
      UseCSC = cms.bool( True ),
      UseECAL = cms.bool( True )
    ),
    inputCollectionTypes = cms.vstring( 'inner tracks',
      'links',
      'outer tracks' ),
    minCaloCompatibility = cms.double( 0.6 ),
    ecalDepositName = cms.string( "ecal" ),
    minP = cms.double( 10.0 ),
    fillIsolation = cms.bool( True ),
    jetDepositName = cms.string( "jets" ),
    hoDepositName = cms.string( "ho" ),
    writeIsoDeposits = cms.bool( False ),
    maxAbsPullX = cms.double( 4.0 ),
    maxAbsPullY = cms.double( 9999.0 ),
    minPt = cms.double( 10.0 ),
    TrackAssociatorParameters = cms.PSet( 
      muonMaxDistanceSigmaX = cms.double( 0.0 ),
      muonMaxDistanceSigmaY = cms.double( 0.0 ),
      CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
      dRHcal = cms.double( 9999.0 ),
      dRPreshowerPreselection = cms.double( 0.2 ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForPF" ),
      useEcal = cms.bool( True ),
      dREcal = cms.double( 9999.0 ),
      dREcalPreselection = cms.double( 0.05 ),
      HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
      dRMuon = cms.double( 9999.0 ),
      propagateAllDirections = cms.bool( True ),
      muonMaxDistanceX = cms.double( 5.0 ),
      muonMaxDistanceY = cms.double( 5.0 ),
      useHO = cms.bool( True ),
      trajectoryUncertaintyTolerance = cms.double( -1.0 ),
      usePreshower = cms.bool( False ),
      DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
      EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
      dRHcalPreselection = cms.double( 0.2 ),
      useMuon = cms.bool( True ),
      useCalo = cms.bool( False ),
      accountForTrajectoryChangeCalo = cms.bool( False ),
      EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      dRMuonPreselection = cms.double( 0.2 ),
      truthMatch = cms.bool( False ),
      HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
      useHcal = cms.bool( True )
    ),
    JetExtractorPSet = cms.PSet( 
      PrintTimeReport = cms.untracked.bool( False ),
      ExcludeMuonVeto = cms.bool( True ),
      TrackAssociatorParameters = cms.PSet( 
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        dRHcal = cms.double( 0.5 ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForPF" ),
        useEcal = cms.bool( False ),
        dREcal = cms.double( 0.5 ),
        dREcalPreselection = cms.double( 0.5 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
        dRMuon = cms.double( 9999.0 ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceX = cms.double( 5.0 ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        usePreshower = cms.bool( False ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        dRHcalPreselection = cms.double( 0.5 ),
        useMuon = cms.bool( False ),
        useCalo = cms.bool( True ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        dRMuonPreselection = cms.double( 0.2 ),
        truthMatch = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        useHcal = cms.bool( False )
      ),
      ServiceParameters = cms.PSet( 
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' ),
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False )
      ),
      ComponentName = cms.string( "JetExtractor" ),
      DR_Max = cms.double( 1.0 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      JetCollectionLabel = cms.InputTag( "hltAntiKT4CaloJetsPFEt5" ),
      DR_Veto = cms.double( 0.1 ),
      Threshold = cms.double( 5.0 )
    ),
    fillGlobalTrackQuality = cms.bool( False ),
    minPCaloMuon = cms.double( 1.0E9 ),
    maxAbsDy = cms.double( 9999.0 ),
    fillCaloCompatibility = cms.bool( True ),
    fillMatching = cms.bool( True ),
    MuonCaloCompatibility = cms.PSet( 
      allSiPMHO = cms.bool( False ),
      PionTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root" ),
      MuonTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root" ),
      delta_eta = cms.double( 0.02 ),
      delta_phi = cms.double( 0.02 )
    ),
    fillTrackerKink = cms.bool( False ),
    hcalDepositName = cms.string( "hcal" ),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
    inputCollectionLabels = cms.VInputTag( 'hltPFMuonMerging','hltMuonLinks','hltL2Muons' ),
    trackDepositName = cms.string( "tracker" ),
    maxAbsDx = cms.double( 3.0 ),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
    minNumberOfMatches = cms.int32( 1 )
)
hltParticleFlowRecHitECAL = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.08 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEBRecHitCreator" )
      ),
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.3 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEERecHitCreator" )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
hltParticleFlowRecHitHCAL = cms.EDProducer( "PFCTRecHitProducer",
    ECAL_Compensate = cms.bool( False ),
    ECAL_Dead_Code = cms.uint32( 10 ),
    MinLongTiming_Cut = cms.double( -5.0 ),
    ECAL_Compensation = cms.double( 0.5 ),
    MaxLongTiming_Cut = cms.double( 5.0 ),
    weight_HFhad = cms.double( 1.0 ),
    ApplyPulseDPG = cms.bool( False ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitCaloTowerNavigator" ) ),
    ECAL_Threshold = cms.double( 10.0 ),
    ApplyTimeDPG = cms.bool( False ),
    caloTowers = cms.InputTag( "hltTowerMakerForPF" ),
    hcalRecHitsHBHE = cms.InputTag( "hltHbhereco" ),
    LongFibre_Fraction = cms.double( 0.1 ),
    MaxShortTiming_Cut = cms.double( 5.0 ),
    HcalMaxAllowedHFLongShortSev = cms.int32( 9 ),
    thresh_Barrel = cms.double( 0.4 ),
    navigation_HF = cms.bool( True ),
    HcalMaxAllowedHFInTimeWindowSev = cms.int32( 9 ),
    HF_Calib_29 = cms.double( 1.07 ),
    LongFibre_Cut = cms.double( 120.0 ),
    EM_Depth = cms.double( 22.0 ),
    weight_HFem = cms.double( 1.0 ),
    LongShortFibre_Cut = cms.double( 1.0E9 ),
    MinShortTiming_Cut = cms.double( -5.0 ),
    HCAL_Calib = cms.bool( True ),
    thresh_HF = cms.double( 0.4 ),
    HcalMaxAllowedHFDigiTimeSev = cms.int32( 9 ),
    thresh_Endcap = cms.double( 0.4 ),
    HcalMaxAllowedChannelStatusSev = cms.int32( 9 ),
    hcalRecHitsHF = cms.InputTag( "hltHfreco" ),
    ShortFibre_Cut = cms.double( 60.0 ),
    ApplyLongShortDPG = cms.bool( True ),
    HF_Calib = cms.bool( True ),
    HAD_Depth = cms.double( 47.0 ),
    ShortFibre_Fraction = cms.double( 0.01 ),
    HCAL_Calib_29 = cms.double( 1.35 )
)
hltParticleFlowRecHitPS = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        ),
        name = cms.string( "PFPSRecHitCreator" )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
hltParticleFlowClusterECALUncorrected = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      positionCalcForConvergence = cms.PSet( 
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 ),
        minAllowedNormalization = cms.double( 0.0 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        T0_ES = cms.double( 1.2 ),
        T0_EE = cms.double( 3.1 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 1.5 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "ECAL_BARREL" ),
          recHitEnergyNorm = cms.double( 0.08 )
        ),
        cms.PSet(  detector = cms.string( "ECAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.3 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet( 
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 ),
      minAllowedNormalization = cms.double( 0.0 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      T0_ES = cms.double( 1.2 ),
      T0_EE = cms.double( 3.1 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( 0.04 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 10.0 ),
    minS4S1_b = cms.double( -0.024 ),
    singleSpikeThresh = cms.double( 4.0 ),
    detector = cms.string( "ECAL_BARREL" ),
    minS4S1_a = cms.double( 0.04 ),
    energyThresholdModifier = cms.double( 2.0 )
  ),
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.0125 ),
    singleSpikeThresh = cms.double( 15.0 ),
    detector = cms.string( "ECAL_ENDCAP" ),
    minS4S1_a = cms.double( 0.02 ),
    energyThresholdModifier = cms.double( 2.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 8 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.6 ),
          seedingThresholdPt = cms.double( 0.15 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 0.23 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECAL" )
)
hltParticleFlowClusterPS = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 0.3 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "PS1" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        ),
        cms.PSet(  detector = cms.string( "PS2" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPS" )
)
hltParticleFlowClusterECAL = cms.EDProducer( "CorrectedECALPFClusterProducer",
    minimumPSEnergy = cms.double( 0.0 ),
    inputPS = cms.InputTag( "hltParticleFlowClusterPS" ),
    energyCorrector = cms.PSet( 
      applyCrackCorrections = cms.bool( False ),
      algoName = cms.string( "PFClusterEMEnergyCorrector" )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrected" )
)
hltParticleFlowClusterHCAL = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          recHitEnergyNorm = cms.double( 0.8 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_BARREL1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  algoName = cms.string( "RBXAndHPDCleaner" )      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.8 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_BARREL1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.1 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHCAL" )
)
hltParticleFlowClusterHFEM = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HF_EM" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HF_EM" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 1.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.19 ),
    singleSpikeThresh = cms.double( 80.0 ),
    detector = cms.string( "HF_EM" ),
    minS4S1_a = cms.double( 0.11 ),
    energyThresholdModifier = cms.double( 1.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 0 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_EM" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( 'hltParticleFlowRecHitHCAL','HFEM' )
)
hltParticleFlowClusterHFHAD = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HF_HAD" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HF_HAD" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 1.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.08 ),
    singleSpikeThresh = cms.double( 120.0 ),
    detector = cms.string( "HF_HAD" ),
    minS4S1_a = cms.double( 0.045 ),
    energyThresholdModifier = cms.double( 1.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 0 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( 'hltParticleFlowRecHitHCAL','HFHAD' )
)
hltLightPFTracks = cms.EDProducer( "LightPFTrackProducer",
    TrackQuality = cms.string( "none" ),
    UseQuality = cms.bool( False ),
    TkColList = cms.VInputTag( 'hltPFMuonMerging' )
)
hltParticleFlowBlockForTaus = cms.EDProducer( "PFBlockProducer",
    debug = cms.untracked.bool( False ),
    linkDefinitions = cms.VPSet( 
      cms.PSet(  useKDTree = cms.bool( True ),
        linkType = cms.string( "PS1:ECAL" ),
        linkerName = cms.string( "PreshowerAndECALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( True ),
        linkType = cms.string( "PS2:ECAL" ),
        linkerName = cms.string( "PreshowerAndECALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( True ),
        linkType = cms.string( "TRACK:ECAL" ),
        linkerName = cms.string( "TrackAndECALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( True ),
        linkType = cms.string( "TRACK:HCAL" ),
        linkerName = cms.string( "TrackAndHCALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( False ),
        linkType = cms.string( "ECAL:HCAL" ),
        linkerName = cms.string( "ECALAndHCALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( False ),
        linkType = cms.string( "HFEM:HFHAD" ),
        linkerName = cms.string( "HFEMAndHFHADLinker" )
      )
    ),
    elementImporters = cms.VPSet( 
      cms.PSet(  importerName = cms.string( "GeneralTracksImporter" ),
        useIterativeTracking = cms.bool( False ),
        source = cms.InputTag( "hltLightPFTracks" ),
        NHitCuts_byTrackAlgo = cms.vuint32( 3, 3, 3, 3, 3 ),
        muonSrc = cms.InputTag( "hltMuons" ),
        DPtOverPtCuts_byTrackAlgo = cms.vdouble( -1.0, -1.0, -1.0, -1.0, -1.0 )
      ),
      cms.PSet(  importerName = cms.string( "ECALClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterECAL" ),
        BCtoPFCMap = cms.InputTag( "" )
      ),
      cms.PSet(  importerName = cms.string( "GenericClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterHCAL" )
      ),
      cms.PSet(  importerName = cms.string( "GenericClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterHFEM" )
      ),
      cms.PSet(  importerName = cms.string( "GenericClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterHFHAD" )
      ),
      cms.PSet(  importerName = cms.string( "GenericClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterPS" )
      )
    ),
    verbose = cms.untracked.bool( False )
)
hltParticleFlowForTaus = cms.EDProducer( "PFProducer",
    photon_SigmaiEtaiEta_endcap = cms.double( 0.034 ),
    minPtForPostCleaning = cms.double( 20.0 ),
    pf_nsigma_ECAL = cms.double( 0.0 ),
    GedPhotonValueMap = cms.InputTag( 'tmpGedPhotons','valMapPFEgammaCandToPhoton' ),
    sumPtTrackIsoForPhoton = cms.double( -1.0 ),
    metFactorForFakes = cms.double( 4.0 ),
    muon_HO = cms.vdouble( 0.9, 0.9 ),
    electron_missinghits = cms.uint32( 1 ),
    metSignificanceForCleaning = cms.double( 3.0 ),
    usePFPhotons = cms.bool( False ),
    dptRel_DispVtx = cms.double( 10.0 ),
    nTrackIsoForEgammaSC = cms.uint32( 2 ),
    pf_nsigma_HCAL = cms.double( 1.0 ),
    cosmicRejectionDistance = cms.double( 1.0 ),
    useEGammaFilters = cms.bool( False ),
    useEGammaElectrons = cms.bool( False ),
    nsigma_TRACK = cms.double( 1.0 ),
    useEGammaSupercluster = cms.bool( False ),
    sumPtTrackIsoForEgammaSC_barrel = cms.double( 4.0 ),
    eventFractionForCleaning = cms.double( 0.8 ),
    usePFDecays = cms.bool( False ),
    rejectTracks_Step45 = cms.bool( False ),
    eventFractionForRejection = cms.double( 0.8 ),
    photon_MinEt = cms.double( 10.0 ),
    usePFNuclearInteractions = cms.bool( False ),
    maxSignificance = cms.double( 2.5 ),
    electron_iso_mva_endcap = cms.double( -0.1075 ),
    debug = cms.untracked.bool( False ),
    pf_convID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt" ),
    calibHF_eta_step = cms.vdouble( 0.0, 2.9, 3.0, 3.2, 4.2, 4.4, 4.6, 4.8, 5.2, 5.4 ),
    ptErrorScale = cms.double( 8.0 ),
    minSignificance = cms.double( 2.5 ),
    minMomentumForPunchThrough = cms.double( 100.0 ),
    pf_conv_mvaCut = cms.double( 0.0 ),
    useCalibrationsFromDB = cms.bool( True ),
    usePFElectrons = cms.bool( False ),
    electron_iso_combIso_endcap = cms.double( 10.0 ),
    photon_combIso = cms.double( 10.0 ),
    electron_iso_mva_barrel = cms.double( -0.1875 ),
    postHFCleaning = cms.bool( False ),
    factors_45 = cms.vdouble( 10.0, 100.0 ),
    cleanedHF = cms.VInputTag( 'hltParticleFlowRecHitHCAL:Cleaned','hltParticleFlowClusterHFHAD:Cleaned','hltParticleFlowClusterHFEM:Cleaned' ),
    coneEcalIsoForEgammaSC = cms.double( 0.3 ),
    minSignificanceReduction = cms.double( 1.4 ),
    photon_SigmaiEtaiEta_barrel = cms.double( 0.0125 ),
    calibHF_b_HADonly = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 0.94348, 0.9437, 1.0034, 1.0444, 1.0444 ),
    minPixelHits = cms.int32( 1 ),
    maxDPtOPt = cms.double( 1.0 ),
    useHO = cms.bool( False ),
    pf_electron_output_col = cms.string( "electrons" ),
    electron_noniso_mvaCut = cms.double( -0.1 ),
    GedElectronValueMap = cms.InputTag( "gedGsfElectronsTmp" ),
    useVerticesForNeutral = cms.bool( True ),
    pf_Res_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFRes.root" ),
    PFEGammaCandidates = cms.InputTag( "particleFlowEGamma" ),
    sumPtTrackIsoSlopeForPhoton = cms.double( -1.0 ),
    coneTrackIsoForEgammaSC = cms.double( 0.3 ),
    minDeltaMet = cms.double( 0.4 ),
    pt_Error = cms.double( 1.0 ),
    useProtectionsForJetMET = cms.bool( True ),
    metFactorForRejection = cms.double( 4.0 ),
    sumPtTrackIsoForEgammaSC_endcap = cms.double( 4.0 ),
    calibHF_use = cms.bool( False ),
    verbose = cms.untracked.bool( False ),
    usePFConversions = cms.bool( False ),
    trackQuality = cms.string( "highPurity" ),
    calibPFSCEle_endcap = cms.vdouble( 1.153, -16.5975, 5.668, -0.1772, 16.22, 7.326, 0.0483, -4.068, 9.406 ),
    metFactorForCleaning = cms.double( 4.0 ),
    eventFactorForCosmics = cms.double( 10.0 ),
    egammaElectrons = cms.InputTag( "" ),
    minEnergyForPunchThrough = cms.double( 100.0 ),
    minTrackerHits = cms.int32( 8 ),
    iCfgCandConnector = cms.PSet( 
      bCalibSecondary = cms.bool( False ),
      bCalibPrimary = cms.bool( False ),
      bCorrect = cms.bool( False ),
      nuclCalibFactors = cms.vdouble( 0.8, 0.15, 0.5, 0.5, 0.05 )
    ),
    rejectTracks_Bad = cms.bool( False ),
    pf_electronID_crackCorrection = cms.bool( False ),
    pf_locC_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFClusterCorr.root" ),
    calibHF_a_EMonly = cms.vdouble( 0.96945, 0.96701, 0.76309, 0.82268, 0.87583, 0.89718, 0.98674, 1.4681, 1.458, 1.458 ),
    muons = cms.InputTag( "hltMuons" ),
    metFactorForHighEta = cms.double( 25.0 ),
    minHFCleaningPt = cms.double( 5.0 ),
    muon_HCAL = cms.vdouble( 3.0, 3.0 ),
    pf_electron_mvaCut = cms.double( -0.1 ),
    ptFactorForHighEta = cms.double( 2.0 ),
    maxDeltaPhiPt = cms.double( 7.0 ),
    pf_electronID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt" ),
    sumEtEcalIsoForEgammaSC_endcap = cms.double( 2.0 ),
    calibHF_b_EMHAD = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 0.94348, 0.9437, 1.0034, 1.0444, 1.0444 ),
    pf_GlobC_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFGlobalCorr.root" ),
    photon_HoE = cms.double( 0.1 ),
    sumEtEcalIsoForEgammaSC_barrel = cms.double( 1.0 ),
    calibPFSCEle_Fbrem_endcap = cms.vdouble( 0.9, 6.5, -0.0692932, 0.101776, 0.995338, -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 0.923165, 4.74665E-4, 1.10782 ),
    punchThroughFactor = cms.double( 3.0 ),
    algoType = cms.uint32( 0 ),
    electron_iso_combIso_barrel = cms.double( 10.0 ),
    postMuonCleaning = cms.bool( True ),
    calibPFSCEle_barrel = cms.vdouble( 1.004, -1.536, 22.88, -1.467, 0.3555, 0.6227, 14.65, 2051.0, 25.0, 0.9932, -0.5444, 0.0, 0.5438, 0.7109, 7.645, 0.2904, 0.0 ),
    electron_protectionsForJetMET = cms.PSet( 
      maxE = cms.double( 50.0 ),
      maxTrackPOverEele = cms.double( 1.0 ),
      maxEcalEOverP_2 = cms.double( 0.2 ),
      maxHcalEOverEcalE = cms.double( 0.1 ),
      maxEcalEOverP_1 = cms.double( 0.5 ),
      maxHcalEOverP = cms.double( 1.0 ),
      maxEcalEOverPRes = cms.double( 0.2 ),
      maxHcalE = cms.double( 10.0 ),
      maxEeleOverPout = cms.double( 0.2 ),
      maxNtracks = cms.double( 3.0 ),
      maxEleHcalEOverEcalE = cms.double( 0.1 ),
      maxDPhiIN = cms.double( 0.1 ),
      maxEeleOverPoutRes = cms.double( 0.5 )
    ),
    electron_iso_pt = cms.double( 10.0 ),
    isolatedElectronID_mvaWeightFile = cms.string( "RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml" ),
    vertexCollection = cms.InputTag( "hltPixelVertices" ),
    X0_Map = cms.string( "RecoParticleFlow/PFProducer/data/allX0histos.root" ),
    calibPFSCEle_Fbrem_barrel = cms.vdouble( 0.6, 6.0, -0.0255975, 0.0576727, 0.975442, -5.46394E-4, 1.26147, 25.0, -0.02025, 0.04537, 0.9728, -8.962E-4, 1.172 ),
    blocks = cms.InputTag( "hltParticleFlowBlockForTaus" ),
    punchThroughMETFactor = cms.double( 4.0 ),
    metSignificanceForRejection = cms.double( 4.0 ),
    photon_protectionsForJetMET = cms.PSet( 
      sumPtTrackIsoSlope = cms.double( 0.001 ),
      sumPtTrackIso = cms.double( 2.0 )
    ),
    usePhotonReg = cms.bool( False ),
    dzPV = cms.double( 0.2 ),
    calibHF_a_EMHAD = cms.vdouble( 1.42215, 1.00496, 0.68961, 0.81656, 0.98504, 0.98504, 1.00802, 1.0593, 1.4576, 1.4576 ),
    useRegressionFromDB = cms.bool( False ),
    muon_ECAL = cms.vdouble( 0.5, 0.5 ),
    usePFSCEleCalib = cms.bool( True )
)
hltAntiKT4PFJetsForTaus = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "PFJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.4 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltParticleFlowForTaus" ),
    inputEtMin = cms.double( 0.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "hltPixelVertices" ),
    jetPtMin = cms.double( 0.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 0 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltTauPFJets08Region = cms.EDProducer( "RecoTauJetRegionProducer",
    pfCandAssocMapSrc = cms.InputTag( "" ),
    src = cms.InputTag( "hltAntiKT4PFJetsForTaus" ),
    deltaR = cms.double( 0.8 ),
    pfCandSrc = cms.InputTag( "hltParticleFlowForTaus" )
)
hltTauPFJetsRecoTauChargedHadrons = cms.EDProducer( "PFRecoTauChargedHadronProducer",
    outputSelection = cms.string( "pt > 0.5" ),
    ranking = cms.VPSet( 
      cms.PSet(  selectionPassFunction = cms.string( "-pt" ),
        selectionFailValue = cms.double( 1000.0 ),
        selection = cms.string( "algoIs(\'kChargedPFCandidate\')" ),
        name = cms.string( "ChargedPFCandidate" ),
        plugin = cms.string( "PFRecoTauChargedHadronStringQuality" )
      )
    ),
    builders = cms.VPSet( 
      cms.PSet(  minMergeChargedHadronPt = cms.double( 100.0 ),
        name = cms.string( "chargedPFCandidates" ),
        dRmergeNeutralHadronWrtOther = cms.double( 0.005 ),
        plugin = cms.string( "PFRecoTauChargedHadronFromPFCandidatePlugin" ),
        minBlockElementMatchesPhoton = cms.int32( 2 ),
        dRmergeNeutralHadronWrtNeutralHadron = cms.double( 0.01 ),
        maxUnmatchedBlockElementsPhoton = cms.int32( 1 ),
        dRmergeNeutralHadronWrtElectron = cms.double( 0.05 ),
        minBlockElementMatchesNeutralHadron = cms.int32( 2 ),
        dRmergePhotonWrtOther = cms.double( 0.005 ),
        dRmergeNeutralHadronWrtChargedHadron = cms.double( 0.005 ),
        minMergeGammaEt = cms.double( 0.0 ),
        chargedHadronCandidatesParticleIds = cms.vint32( 1, 2, 3 ),
        dRmergePhotonWrtElectron = cms.double( 0.005 ),
        dRmergePhotonWrtChargedHadron = cms.double( 0.005 ),
        dRmergePhotonWrtNeutralHadron = cms.double( 0.01 ),
        maxUnmatchedBlockElementsNeutralHadron = cms.int32( 1 ),
        minMergeNeutralHadronEt = cms.double( 0.0 ),
        qualityCuts = cms.PSet( 
          signalQualityCuts = cms.PSet( 
            minTrackPt = cms.double( 0.0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            useTracksInsteadOfPFHadrons = cms.bool( False ),
            minGammaEt = cms.double( 0.5 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minTrackHits = cms.uint32( 3 ),
            maxDeltaZ = cms.double( 9999.9 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            minNeutralHadronEt = cms.double( 30.0 )
          ),
          vxAssocQualityCuts = cms.PSet( 
            minTrackPt = cms.double( 0.0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minTrackHits = cms.uint32( 3 ),
            minGammaEt = cms.double( 0.5 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            useTracksInsteadOfPFHadrons = cms.bool( False )
          ),
          pvFindingAlgo = cms.string( "closestInDeltaZ" ),
          primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
          vertexTrackFiltering = cms.bool( False ),
          recoverLeadingTrk = cms.bool( False )
        )
      )
    ),
    jetRegionSrc = cms.InputTag( "hltTauPFJets08Region" ),
    jetSrc = cms.InputTag( "hltAntiKT4PFJetsForTaus" )
)
hltPFTauPiZeros = cms.EDProducer( "RecoTauPiZeroProducer",
    outputSelection = cms.string( "pt > 0" ),
    ranking = cms.VPSet( 
      cms.PSet(  selectionPassFunction = cms.string( "abs(mass() - 0.13579)" ),
        selectionFailValue = cms.double( 1000.0 ),
        selection = cms.string( "algoIs(\'kStrips\')" ),
        name = cms.string( "InStrip" ),
        plugin = cms.string( "RecoTauPiZeroStringQuality" )
      )
    ),
    builders = cms.VPSet( 
      cms.PSet(  name = cms.string( "s" ),
        stripPhiAssociationDistance = cms.double( 0.2 ),
        plugin = cms.string( "RecoTauPiZeroStripPlugin2" ),
        minGammaEtStripAdd = cms.double( 0.0 ),
        minGammaEtStripSeed = cms.double( 0.5 ),
        maxStripBuildIterations = cms.int32( -1 ),
        updateStripAfterEachDaughter = cms.bool( False ),
        makeCombinatoricStrips = cms.bool( False ),
        applyElecTrackQcuts = cms.bool( False ),
        stripCandidatesParticleIds = cms.vint32( 2, 4 ),
        minStripEt = cms.double( 1.0 ),
        stripEtaAssociationDistance = cms.double( 0.05 ),
        qualityCuts = cms.PSet( 
          signalQualityCuts = cms.PSet( 
            minGammaEt = cms.double( 0.5 ),
            minTrackPt = cms.double( 0.0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minTrackHits = cms.uint32( 3 ),
            maxDeltaZ = cms.double( 0.4 ),
            useTracksInsteadOfPFHadrons = cms.bool( False ),
            maxTransverseImpactParameter = cms.double( 0.2 )
          ),
          primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
          pvFindingAlgo = cms.string( "closestInDeltaZ" ),
          vertexTrackFiltering = cms.bool( False ),
          recoverLeadingTrk = cms.bool( False )
        )
      )
    ),
    massHypothesis = cms.double( 0.136 ),
    jetSrc = cms.InputTag( "hltAntiKT4PFJetsForTaus" )
)
hltPFTausSansRefFor2015 = cms.EDProducer( "RecoTauProducer",
    piZeroSrc = cms.InputTag( "hltPFTauPiZeros" ),
    modifiers = cms.VPSet( 
      cms.PSet(  ElectronPreIDProducer = cms.InputTag( "elecpreid" ),
        name = cms.string( "shrinkingConeElectronRej" ),
        plugin = cms.string( "RecoTauElectronRejectionPlugin" ),
        DataType = cms.string( "AOD" ),
        maximumForElectrionPreIDOutput = cms.double( -0.1 ),
        EcalStripSumE_deltaPhiOverQ_minValue = cms.double( -0.1 ),
        ElecPreIDLeadTkMatch_maxDR = cms.double( 0.01 ),
        EcalStripSumE_minClusEnergy = cms.double( 0.1 ),
        EcalStripSumE_deltaPhiOverQ_maxValue = cms.double( 0.5 ),
        EcalStripSumE_deltaEta = cms.double( 0.03 )
      )
    ),
    jetRegionSrc = cms.InputTag( "hltTauPFJets08Region" ),
    chargedHadronSrc = cms.InputTag( "hltTauPFJetsRecoTauChargedHadrons" ),
    jetSrc = cms.InputTag( "hltAntiKT4PFJetsForTaus" ),
    builders = cms.VPSet( 
      cms.PSet(  usePFLeptons = cms.bool( True ),
        signalConeNeutralHadrons = cms.string( "0.1" ),
        name = cms.string( "fixedConeTau" ),
        plugin = cms.string( "RecoTauBuilderConePlugin" ),
        isoConeChargedHadrons = cms.string( "0.4" ),
        isoConePiZeros = cms.string( "0.4" ),
        isoConeNeutralHadrons = cms.string( "0.4" ),
        matchingCone = cms.string( "0.4" ),
        signalConeChargedHadrons = cms.string( "0.12" ),
        leadObjectPt = cms.double( 0.5 ),
        signalConePiZeros = cms.string( "0.12" ),
        pfCandSrc = cms.InputTag( "hltParticleFlowForTaus" ),
        qualityCuts = cms.PSet( 
          pvFindingAlgo = cms.string( "closestInDeltaZ" ),
          primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
          vertexTrackFiltering = cms.bool( False ),
          recoverLeadingTrk = cms.bool( False ),
          signalQualityCuts = cms.PSet( 
            minTrackPt = cms.double( 0.0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            useTracksInsteadOfPFHadrons = cms.bool( False ),
            minGammaEt = cms.double( 0.5 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minTrackHits = cms.uint32( 3 ),
            maxDeltaZ = cms.double( 9999.9 ),
            maxTransverseImpactParameter = cms.double( 0.2 )
          ),
          vxAssocQualityCuts = cms.PSet( 
            minTrackPt = cms.double( 0.0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minTrackHits = cms.uint32( 3 ),
            minGammaEt = cms.double( 0.5 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            useTracksInsteadOfPFHadrons = cms.bool( False )
          )
        ),
        maxSignalConeChargedHadrons = cms.int32( 3 )
      )
    ),
    buildNullTaus = cms.bool( True )
)
hltPFTausFor2015 = cms.EDProducer( "RecoTauPiZeroUnembedder",
    src = cms.InputTag( "hltPFTausSansRefFor2015" )
)
hltPFTauTrackFindingDiscriminatorFor2015 = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double( 0.0 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    UseOnlyChargedHadrons = cms.bool( True ),
    PFTauProducer = cms.InputTag( "hltPFTausFor2015" )
)
hltPFTauLooseAbsoluteIsolationDiscriminatorFor2015 = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( "hltPFTausFor2015" ),
    qualityCuts = cms.PSet( 
      isolationQualityCuts = cms.PSet( 
        minTrackHits = cms.uint32( 5 ),
        minTrackPt = cms.double( 0.5 ),
        maxTrackChi2 = cms.double( 100.0 ),
        minTrackPixelHits = cms.uint32( 2 ),
        minGammaEt = cms.double( 0.5 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        maxDeltaZ = cms.double( 0.2 ),
        maxTransverseImpactParameter = cms.double( 0.05 )
      ),
      signalQualityCuts = cms.PSet( 
        minTrackPt = cms.double( 0.0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.5 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minTrackHits = cms.uint32( 3 ),
        maxDeltaZ = cms.double( 0.4 ),
        maxTransverseImpactParameter = cms.double( 0.2 )
      ),
      primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
      pvFindingAlgo = cms.string( "closestInDeltaZ" ),
      vertexTrackFiltering = cms.bool( False ),
      recoverLeadingTrk = cms.bool( False ),
      vxAssocQualityCuts = cms.PSet( 
        minTrackPt = cms.double( 0.0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.5 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minTrackHits = cms.uint32( 3 ),
        maxTransverseImpactParameter = cms.double( 0.2 )
      )
    ),
    maximumSumPtCut = cms.double( 3.0 ),
    deltaBetaPUTrackPtCutOverride = cms.double( 0.5 ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( True ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
    deltaBetaFactor = cms.string( "0.38" ),
    relativeSumPtCut = cms.double( 0.1 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    applyRelativeSumPtCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    storeRawSumPt = cms.bool( False ),
    applyRhoCorrection = cms.bool( False ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowForTaus" ),
    storeRawPUsumPt = cms.bool( False ),
    verbosity = cms.int32( 0 )
)
hltPFTauLooseRelativeIsolationDiscriminatorFor2015 = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( "hltPFTausFor2015" ),
    qualityCuts = cms.PSet( 
      isolationQualityCuts = cms.PSet( 
        minTrackHits = cms.uint32( 5 ),
        minTrackPt = cms.double( 0.5 ),
        maxTrackChi2 = cms.double( 100.0 ),
        minTrackPixelHits = cms.uint32( 2 ),
        minGammaEt = cms.double( 0.5 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        maxDeltaZ = cms.double( 0.2 ),
        maxTransverseImpactParameter = cms.double( 0.05 )
      ),
      signalQualityCuts = cms.PSet( 
        minTrackPt = cms.double( 0.0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.5 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minTrackHits = cms.uint32( 3 ),
        maxDeltaZ = cms.double( 0.4 ),
        maxTransverseImpactParameter = cms.double( 0.2 )
      ),
      primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
      pvFindingAlgo = cms.string( "closestInDeltaZ" ),
      vertexTrackFiltering = cms.bool( False ),
      recoverLeadingTrk = cms.bool( False ),
      vxAssocQualityCuts = cms.PSet( 
        minTrackPt = cms.double( 0.0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.5 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minTrackHits = cms.uint32( 3 ),
        maxTransverseImpactParameter = cms.double( 0.2 )
      )
    ),
    maximumSumPtCut = cms.double( 3.0 ),
    deltaBetaPUTrackPtCutOverride = cms.double( 0.5 ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( False ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
    deltaBetaFactor = cms.string( "0.38" ),
    relativeSumPtCut = cms.double( 0.1 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    applyRelativeSumPtCut = cms.bool( True ),
    maximumOccupancy = cms.uint32( 0 ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    storeRawSumPt = cms.bool( False ),
    applyRhoCorrection = cms.bool( False ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowForTaus" ),
    storeRawPUsumPt = cms.bool( False ),
    verbosity = cms.int32( 0 )
)
hltPFTau20For2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( False ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPFTausFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltSelectedPFTausTrackFindingFor2015 = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet( 
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauTrackFindingDiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      )
    ),
    cut = cms.string( "pt > 0" ),
    src = cms.InputTag( "hltPFTausFor2015" )
)
hltPFTau20TrackFor2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( False ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackFindingFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltSelectedPFTausTrackFindingLooseIsolationFor2015 = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet( 
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauTrackFindingDiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauLooseAbsoluteIsolationDiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      )
    ),
    cut = cms.string( "pt > 0" ),
    src = cms.InputTag( "hltPFTausFor2015" )
)
hltPFTau20TrackLooseIsoFor2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackFindingLooseIsolationFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltPFTauAgainstMuonDiscriminatorFor2015 = cms.EDProducer( "PFRecoTauDiscriminationAgainstMuon2",
    maxNumberOfHitsLast2Stations = cms.int32( -1 ),
    PFTauProducer = cms.InputTag( "hltPFTausFor2015" ),
    verbosity = cms.int32( 0 ),
    dRmuonMatchLimitedToJetArea = cms.bool( False ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    discriminatorOption = cms.string( "custom" ),
    HoPMin = cms.double( -1.0 ),
    maxNumberOfMatches = cms.int32( 1 ),
    dRmuonMatch = cms.double( 0.3 ),
    srcMuons = cms.InputTag( "" ),
    doCaloMuonVeto = cms.bool( False ),
    maskHitsRPC = cms.vint32( 0, 0, 0, 0 ),
    maskMatchesRPC = cms.vint32( 0, 0, 0, 0 ),
    maskMatchesCSC = cms.vint32( 1, 0, 0, 0 ),
    maskHitsCSC = cms.vint32( 0, 0, 0, 0 ),
    maskMatchesDT = cms.vint32( 0, 0, 0, 0 ),
    minPtMatchedMuon = cms.double( 5.0 ),
    maskHitsDT = cms.vint32( 0, 0, 0, 0 )
)
hltSelectedPFTausTrackFindingLooseIsolationAgainstMuonFor2015 = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet( 
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauTrackFindingDiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauLooseAbsoluteIsolationDiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauAgainstMuonDiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      )
    ),
    cut = cms.string( "pt > 0" ),
    src = cms.InputTag( "hltPFTausFor2015" )
)
hltPFTau20TrackLooseIsoAgainstMuonFor2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackFindingLooseIsolationAgainstMuonFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltOverlapFilterIsoMu17LooseIsoPFTau20For2015 = cms.EDFilter( "HLT2MuonPFTau",
    saveTags = cms.bool( True ),
    MinMinv = cms.double( 0.0 ),
    originTag2 = cms.VInputTag( 'hltSelectedPFTausTrackFindingLooseIsolationAgainstMuonFor2015' ),
    MinDelR = cms.double( 0.3 ),
    MinPt = cms.double( 1.0 ),
    MinN = cms.int32( 1 ),
    originTag1 = cms.VInputTag( 'hltL3MuonCandidates' ),
    triggerType1 = cms.int32( 83 ),
    triggerType2 = cms.int32( 84 ),
    MaxMinv = cms.double( -1.0 ),
    MinDeta = cms.double( 1.0 ),
    MaxDelR = cms.double( 99999.0 ),
    inputTag1 = cms.InputTag( "hltL3crIsoL1sMu14erORMu16erL1f0L2f14QL3f17QL3crIsoRhoFiltered0p15" ),
    inputTag2 = cms.InputTag( "hltPFTau20TrackLooseIsoAgainstMuonFor2015" ),
    MaxDphi = cms.double( -1.0 ),
    MaxDeta = cms.double( -1.0 ),
    MaxPt = cms.double( -1.0 ),
    MinDphi = cms.double( 0.0 )
)
hltL1sL1SingleIsoEG18erORIsoEG20erOREG22 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleIsoEG18er OR L1_SingleIsoEG20er OR L1_SingleEG22" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreEle22eta2p1WP90RhoLooseIsoPFTau20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltHybridSuperClustersL1Seeded = cms.EDProducer( "EgammaHLTHybridClusterProducer",
    xi = cms.double( 0.0 ),
    regionEtaMargin = cms.double( 0.14 ),
    regionPhiMargin = cms.double( 0.4 ),
    severityRecHitThreshold = cms.double( 4.0 ),
    RecHitFlagToBeExcluded = cms.vstring(  ),
    ecalhitcollection = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    eThreshA = cms.double( 0.003 ),
    basicclusterCollection = cms.string( "" ),
    eThreshB = cms.double( 0.1 ),
    dynamicPhiRoad = cms.bool( False ),
    useEtForXi = cms.bool( True ),
    l1UpperThr = cms.double( 999.0 ),
    excludeFlagged = cms.bool( True ),
    posCalcParameters = cms.PSet( 
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    l1LowerThr = cms.double( 5.0 ),
    doIsolated = cms.bool( True ),
    eseed = cms.double( 0.35 ),
    ethresh = cms.double( 0.1 ),
    ewing = cms.double( 0.0 ),
    RecHitSeverityToBeExcluded = cms.vstring( 'kWeird' ),
    step = cms.int32( 17 ),
    debugLevel = cms.string( "INFO" ),
    dynamicEThresh = cms.bool( False ),
    l1TagIsolated = cms.InputTag( 'l1extraParticles','Isolated' ),
    superclusterCollection = cms.string( "" ),
    HybridBarrelSeedThr = cms.double( 1.5 ),
    l1TagNonIsolated = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    l1LowerThrIgnoreIsolation = cms.double( 0.0 )
)
hltCorrectedHybridSuperClustersL1Seeded = cms.EDProducer( "EgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.03 ),
    superClusterAlgo = cms.string( "Hybrid" ),
    etThresh = cms.double( 1.0 ),
    rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1Seeded" ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet(  ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    fix_fCorrPset = cms.PSet(  ),
    modeEE = cms.int32( 0 ),
    modeEB = cms.int32( 0 ),
    dyn_fCorrPset = cms.PSet(  ),
    energyCorrectorName = cms.string( "EcalClusterEnergyCorrectionObjectSpecific" ),
    applyLocalContCorrection = cms.bool( False ),
    localContCorrectorName = cms.string( "EcalBasicClusterLocalContCorrection" ),
    crackCorrectorName = cms.string( "EcalClusterCrackCorrection" ),
    applyCrackCorrection = cms.bool( False ),
    hyb_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 1.1 ),
      fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -5.735E-4, 1.343 ),
      brLinearHighThr = cms.double( 8.0 ),
      fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 )
    )
)
hltMulti5x5BasicClustersL1Seeded = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
    l1LowerThr = cms.double( 5.0 ),
    Multi5x5BarrelSeedThr = cms.double( 0.5 ),
    Multi5x5EndcapSeedThr = cms.double( 0.18 ),
    endcapHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    barrelClusterCollection = cms.string( "notused" ),
    regionEtaMargin = cms.double( 0.3 ),
    regionPhiMargin = cms.double( 0.4 ),
    RecHitFlagToBeExcluded = cms.vstring(  ),
    l1TagNonIsolated = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    posCalcParameters = cms.PSet( 
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    VerbosityLevel = cms.string( "ERROR" ),
    doIsolated = cms.bool( True ),
    barrelHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    l1LowerThrIgnoreIsolation = cms.double( 0.0 ),
    l1TagIsolated = cms.InputTag( 'l1extraParticles','Isolated' ),
    doEndcaps = cms.bool( True ),
    doBarrel = cms.bool( False ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    l1UpperThr = cms.double( 999.0 )
)
hltMulti5x5SuperClustersL1Seeded = cms.EDProducer( "Multi5x5SuperClusterProducer",
    barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    dynamicPhiRoad = cms.bool( False ),
    endcapClusterTag = cms.InputTag( 'hltMulti5x5BasicClustersL1Seeded','multi5x5EndcapBasicClusters' ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    barrelClusterTag = cms.InputTag( 'hltMulti5x5BasicClustersL1Seeded','multi5x5BarrelBasicClusters' ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    bremRecoveryPset = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet( 
        a = cms.double( 47.85 ),
        c = cms.double( 0.1201 ),
        b = cms.double( 108.8 )
      ),
      doEndcaps = cms.bool( True ),
      doBarrel = cms.bool( False )
    ),
    endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1Seeded" )
)
hltMulti5x5EndcapSuperClustersWithPreshowerL1Seeded = cms.EDProducer( "PreshowerClusterProducer",
    assocSClusterCollection = cms.string( "" ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshClusterCollectionY = cms.string( "preshowerYClusters" ),
    preshClusterCollectionX = cms.string( "preshowerXClusters" ),
    etThresh = cms.double( 5.0 ),
    preshRecHitProducer = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
    endcapSClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersL1Seeded','multi5x5EndcapSuperClusters' ),
    preshNclust = cms.int32( 4 ),
    debugLevel = cms.string( "" ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 )
)
hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Seeded = cms.EDProducer( "EgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    superClusterAlgo = cms.string( "Multi5x5" ),
    etThresh = cms.double( 1.0 ),
    rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1Seeded" ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet(  ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    fix_fCorrPset = cms.PSet( 
      brLinearLowThr = cms.double( 0.6 ),
      fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 ),
      brLinearHighThr = cms.double( 6.0 ),
      fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 )
    ),
    modeEE = cms.int32( 0 ),
    modeEB = cms.int32( 0 ),
    dyn_fCorrPset = cms.PSet(  ),
    energyCorrectorName = cms.string( "EcalClusterEnergyCorrectionObjectSpecific" ),
    applyLocalContCorrection = cms.bool( False ),
    localContCorrectorName = cms.string( "EcalBasicClusterLocalContCorrection" ),
    crackCorrectorName = cms.string( "EcalClusterCrackCorrection" ),
    applyCrackCorrection = cms.bool( False ),
    hyb_fCorrPset = cms.PSet(  )
)
hltL1SeededRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Seeded" ),
    scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1Seeded" ),
    recoEcalCandidateCollection = cms.string( "" )
)
hltEGRegionalL1SingleIsoEG18erORIsoEG20erOREG22 = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.1 ),
    saveTags = cms.bool( False ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'l1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleIsoEG18erORIsoEG20erOREG22" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'l1extraParticles','NonIsolated' ),
    ncandcut = cms.int32( 1 )
)
hltEG22L1sIso18erOrIso20erOr22EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( False ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    inputTag = cms.InputTag( "hltEGRegionalL1SingleIsoEG18erORIsoEG20erOREG22" ),
    etcutEB = cms.double( 22.0 ),
    etcutEE = cms.double( 22.0 ),
    ncandcut = cms.int32( 1 )
)
hltL1SeededHLTClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
hltEle22WP90RhoClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( 0.03 ),
    thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( -1.0 ),
    thrRegularEB = cms.double( 0.01 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededHLTClusterShape" ),
    candTag = cms.InputTag( "hltEG22L1sIso18erOrIso20erOr22EtFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltFixedGridRhoFastjetAllCalo = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 5.0 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" )
)
hltAntiKT4CaloJets = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( 0.9 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 14327 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.4 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltCaloJetIDPassed = cms.EDProducer( "HLTCaloJetIDProducer",
    min_N90 = cms.int32( -2 ),
    min_N90hits = cms.int32( 2 ),
    min_EMF = cms.double( 1.0E-6 ),
    jetsInput = cms.InputTag( "hltAntiKT4CaloJets" ),
    JetIDParams = cms.PSet( 
      useRecHits = cms.bool( True ),
      hbheRecHitsColl = cms.InputTag( "hltHbhereco" ),
      hoRecHitsColl = cms.InputTag( "hltHoreco" ),
      hfRecHitsColl = cms.InputTag( "hltHfreco" ),
      ebRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      eeRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' )
    ),
    max_EMF = cms.double( 999.0 )
)
hltCaloJetL1FastJetCorrected = cms.EDProducer( "CaloJetCorrectionProducer",
    src = cms.InputTag( "hltCaloJetIDPassed" ),
    correctors = cms.vstring( 'hltESPAK4CaloL1L2L3' )
)
hltL1SeededPhotonEcalIsoRhoCorr = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
    useNumCrystals = cms.bool( True ),
    intRadiusEndcap = cms.double( 3.0 ),
    etMinBarrel = cms.double( -9999.0 ),
    effectiveAreaBarrel = cms.double( 0.205 ),
    tryBoth = cms.bool( True ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
    etMinEndcap = cms.double( 0.11 ),
    eMinBarrel = cms.double( 0.095 ),
    ecalEndcapRecHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    jurassicWidth = cms.double( 3.0 ),
    intRadiusBarrel = cms.double( 3.0 ),
    ecalBarrelRecHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    extRadius = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( True ),
    useIsolEt = cms.bool( True ),
    eMinEndcap = cms.double( -9999.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    rhoMax = cms.double( 9.9999999E7 ),
    subtract = cms.bool( False ),
    rhoScale = cms.double( 1.0 ),
    effectiveAreaEndcap = cms.double( 0.115 )
)
hltEle22WP90RhoEcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.035 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.07 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonEcalIsoRhoCorr" ),
    candTag = cms.InputTag( "hltEle22WP90RhoClusterShapeFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltL1SeededPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    eMinHE = cms.double( 0.8 ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.14 ),
    eMinHB = cms.double( 0.7 ),
    innerCone = cms.double( 0.0 ),
    etMinHE = cms.double( -1.0 ),
    etMinHB = cms.double( -1.0 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
hltEle22WP90RhoHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalForHE" ),
    candTag = cms.InputTag( "hltEle22WP90RhoEcalIsoFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltL1SeededPhotonHcalIsoRhoCorr = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    eMinHE = cms.double( 0.8 ),
    hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.29 ),
    eMinHB = cms.double( 0.7 ),
    innerCone = cms.double( 0.16 ),
    etMinHE = cms.double( -1.0 ),
    etMinHB = cms.double( -1.0 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( True ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( True )
)
hltEle22WP90RhoHcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    thrOverEEB = cms.double( 0.05 ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededPhotonHcalIsoRhoCorr" ),
    candTag = cms.InputTag( "hltEle22WP90RhoHEFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
hltL1SeededStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Seeded" ),
    SeedConfiguration = cms.PSet( 
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet( 
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        useOnDemandTracker = cms.untracked.int32( 0 ),
        SeedingLayers = cms.InputTag( "hltMixedLayerPairs" )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.004 ),
      LowPtThreshold = cms.double( 3.0 ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( "dummyVertices" )
      ),
      maxHOverE = cms.double( 999999.0 ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      DeltaPhi2 = cms.double( 0.004 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      PhiMax2 = cms.double( 0.004 ),
      preFilteredSeeds = cms.bool( False ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      initialSeeds = cms.InputTag( "globalPixelSeeds:GlobalPixel" ),
      pPhiMax1 = cms.double( 0.08 ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      z2MaxB = cms.double( 0.09 ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( "hltHbhereco" ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      rMinI = cms.double( -0.2 ),
      hOverEConeSize = cms.double( 0.0 ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 ),
      measurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" )
    ),
    barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1Seeded" )
)
hltEle22WP90RhoPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    L1IsoCand = cms.InputTag( "hltL1SeededRecoEcalCandidate" ),
    s2_threshold = cms.double( 0.4 ),
    useS = cms.bool( False ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    candTag = cms.InputTag( "hltEle22WP90RhoHcalIsoFilter" ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    s_a_zB = cms.double( 0.012 ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltL1SeededStartUpElectronPixelSeeds" ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
hltCtfL1SeededWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltCkfL1SeededTrackCandidates" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "MeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
hltPixelMatchElectronsL1Seeded = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "offlineBeamSpot" ),
    UseGsfTracks = cms.bool( False ),
    TrackProducer = cms.InputTag( "hltCtfL1SeededWithMaterialTracks" ),
    GsfTrackProducer = cms.InputTag( "" )
)
hltEle22WP90RhoOneOEMinusOneOPFilter = cms.EDFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    doIsolated = cms.bool( True ),
    saveTags = cms.bool( True ),
    electronNonIsolatedProducer = cms.InputTag( "" ),
    barrelcut = cms.double( 999.9 ),
    electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    ncandcut = cms.int32( 1 ),
    candTag = cms.InputTag( "hltEle22WP90RhoPixelMatchFilter" ),
    endcapcut = cms.double( 999.9 )
)
hltElectronL1SeededDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    variablesAtVtx = cms.bool( False ),
    useSCRefs = cms.bool( False ),
    BSProducer = cms.InputTag( "offlineBeamSpot" ),
    electronProducer = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    useTrackProjectionToEcal = cms.bool( False )
)
hltEle22WP90RhoDetaFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( 0.006 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.006 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltElectronL1SeededDetaDphi','Deta' ),
    candTag = cms.InputTag( "hltEle22WP90RhoOneOEMinusOneOPFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
hltEle22WP90RhoDphiFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( 0.05 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    thrRegularEB = cms.double( 0.04 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltElectronL1SeededDetaDphi','Dphi' ),
    candTag = cms.InputTag( "hltEle22WP90RhoDetaFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( -1.0 )
)
hltL1SeededElectronTrackIso = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    useGsfTrack = cms.bool( False ),
    useSCRefs = cms.bool( False ),
    trackProducer = cms.InputTag( "hltL1SeededEgammaRegionalCTFFinalFitWithMaterial" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    electronProducer = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    recoEcalCandidateProducer = cms.InputTag( "" ),
    beamSpotProducer = cms.InputTag( "offlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoZSpan = cms.double( 0.15 )
)
hltEle22WP90RhoTrackIsoFilter = cms.EDFilter( "HLTElectronGenericFilter",
    doIsolated = cms.bool( True ),
    nonIsoTag = cms.InputTag( "" ),
    L1NonIsoCand = cms.InputTag( "" ),
    thrTimesPtEB = cms.double( -1.0 ),
    saveTags = cms.bool( True ),
    thrRegularEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Seeded" ),
    thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltL1SeededElectronTrackIso" ),
    candTag = cms.InputTag( "hltEle22WP90RhoDphiFilter" ),
    thrTimesPtEE = cms.double( -1.0 ),
    thrOverPtEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( 0.05 )
)
hltOverlapFilterIsoEle20CaloJet5 = cms.EDFilter( "HLT2ElectronTau",
    saveTags = cms.bool( False ),
    MinMinv = cms.double( 0.0 ),
    originTag2 = cms.VInputTag( 'hltOriginal2' ),
    MinDelR = cms.double( 0.3 ),
    MinPt = cms.double( 1.0 ),
    MinN = cms.int32( 1 ),
    originTag1 = cms.VInputTag( 'hltOriginal1' ),
    triggerType1 = cms.int32( 82 ),
    triggerType2 = cms.int32( 84 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDelR = cms.double( 99999.0 ),
    inputTag1 = cms.InputTag( "hltEle22WP90RhoTrackIsoFilter" ),
    inputTag2 = cms.InputTag( "hltTauJet5" ),
    MaxDphi = cms.double( 9999.0 ),
    MaxDeta = cms.double( 9999.0 ),
    MaxPt = cms.double( -1.0 ),
    MinDphi = cms.double( 0.0 )
)
hltOverlapFilterIsoEle20WP90LooseIsoPFTau20For2015 = cms.EDFilter( "HLT2ElectronPFTau",
    saveTags = cms.bool( True ),
    MinMinv = cms.double( 0.0 ),
    originTag2 = cms.VInputTag( 'hltSelectedPFTausTrackFindingLooseIsolationFor2015' ),
    MinDelR = cms.double( 0.3 ),
    MinPt = cms.double( 1.0 ),
    MinN = cms.int32( 1 ),
    originTag1 = cms.VInputTag( 'hltPixelMatchElectronsL1Seeded' ),
    triggerType1 = cms.int32( 82 ),
    triggerType2 = cms.int32( 84 ),
    MaxMinv = cms.double( -1.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDelR = cms.double( 99999.0 ),
    inputTag1 = cms.InputTag( "hltEle22WP90RhoTrackIsoFilter" ),
    inputTag2 = cms.InputTag( "hltPFTau20TrackLooseIsoFor2015" ),
    MaxDphi = cms.double( -1.0 ),
    MaxDeta = cms.double( -1.0 ),
    MaxPt = cms.double( -1.0 ),
    MinDphi = cms.double( 0.0 )
)
hltL1sDoubleTauJet44erorDoubleJetC64 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleTauJet44er OR L1_DoubleJetC64" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreDoubleMediumIsoPFTau35Trk1eta2p1Prong1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltCaloTowersTau1Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( "hltTowerMakerForAll" ),
    TauId = cms.int32( 0 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Tau' ),
    minimumE = cms.double( 0.8 ),
    UseTowersInCone = cms.double( 0.8 ),
    minimumEt = cms.double( 0.5 )
)
hltIconeTau1Regional = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.2 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltCaloTowersTau1Regional" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltCaloTowersTau2Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( "hltTowerMakerForAll" ),
    TauId = cms.int32( 1 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Tau' ),
    minimumE = cms.double( 0.8 ),
    UseTowersInCone = cms.double( 0.8 ),
    minimumEt = cms.double( 0.5 )
)
hltIconeTau2Regional = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.2 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltCaloTowersTau2Regional" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltCaloTowersTau3Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( "hltTowerMakerForAll" ),
    TauId = cms.int32( 2 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Tau' ),
    minimumE = cms.double( 0.8 ),
    UseTowersInCone = cms.double( 0.8 ),
    minimumEt = cms.double( 0.5 )
)
hltIconeTau3Regional = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.2 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltCaloTowersTau3Regional" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltCaloTowersTau4Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( "hltTowerMakerForAll" ),
    TauId = cms.int32( 3 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Tau' ),
    minimumE = cms.double( 0.8 ),
    UseTowersInCone = cms.double( 0.8 ),
    minimumEt = cms.double( 0.5 )
)
hltIconeTau4Regional = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.2 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltCaloTowersTau4Regional" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltCaloTowersCentral1Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( "hltTowerMakerForAll" ),
    TauId = cms.int32( 0 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Central' ),
    minimumE = cms.double( 0.8 ),
    UseTowersInCone = cms.double( 0.8 ),
    minimumEt = cms.double( 0.5 )
)
hltIconeCentral1Regional = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.2 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltCaloTowersCentral1Regional" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltCaloTowersCentral2Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( "hltTowerMakerForAll" ),
    TauId = cms.int32( 1 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Central' ),
    minimumE = cms.double( 0.8 ),
    UseTowersInCone = cms.double( 0.8 ),
    minimumEt = cms.double( 0.5 )
)
hltIconeCentral2Regional = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.2 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltCaloTowersCentral2Regional" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltCaloTowersCentral3Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( "hltTowerMakerForAll" ),
    TauId = cms.int32( 2 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Central' ),
    minimumE = cms.double( 0.8 ),
    UseTowersInCone = cms.double( 0.8 ),
    minimumEt = cms.double( 0.5 )
)
hltIconeCentral3Regional = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.2 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltCaloTowersCentral3Regional" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltCaloTowersCentral4Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( "hltTowerMakerForAll" ),
    TauId = cms.int32( 3 ),
    TauTrigger = cms.InputTag( 'l1extraParticles','Central' ),
    minimumE = cms.double( 0.8 ),
    UseTowersInCone = cms.double( 0.8 ),
    minimumEt = cms.double( 0.5 )
)
hltIconeCentral4Regional = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.2 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltCaloTowersCentral4Regional" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltL2TauJets = cms.EDProducer( "L2TauJetsMerger",
    EtMin = cms.double( 20.0 ),
    JetSrc = cms.VInputTag( 'hltIconeTau1Regional','hltIconeTau2Regional','hltIconeTau3Regional','hltIconeTau4Regional','hltIconeCentral1Regional','hltIconeCentral2Regional','hltIconeCentral3Regional','hltIconeCentral4Regional' )
)
hltDoubleL2Tau35eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltL2TauJets" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltL2Tau25eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 25.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltL2TauJets" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltL2TausForPixelIsolation = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 84 ),
    HLTObject = cms.InputTag( "hltL2Tau25eta2p1" )
)
hltPixelVerticesReg = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracksReg" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
hltL2TauPixelIsoTagProducer = cms.EDProducer( "L2TauPixelIsoTagProducer",
    TrackSrc = cms.InputTag( "" ),
    BeamSpotSrc = cms.InputTag( "offlineBeamSpot" ),
    TrackMinNHits = cms.int32( 3 ),
    TrackMaxNChi2 = cms.double( 100.0 ),
    TrackPVMaxDZ = cms.double( 0.1 ),
    IsoConeMax = cms.double( 0.4 ),
    TrackMinPt = cms.double( 1.2 ),
    IsoConeMin = cms.double( 0.2 ),
    VertexSrc = cms.InputTag( "hltPixelVerticesReg" ),
    JetSrc = cms.InputTag( "hltL2TausForPixelIsolation" ),
    TrackMaxDxy = cms.double( 0.2 ),
    MaxNumberPV = cms.int32( 1 )
)
hltL2DiTauIsoFilter = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 2 ),
    JetTags = cms.InputTag( "hltL2TauPixelIsoTagProducer" ),
    TriggerType = cms.int32( 84 ),
    Jets = cms.InputTag( "hltL2TausForPixelIsolation" ),
    MinTag = cms.double( 0.0 ),
    MaxTag = cms.double( 0.0 )
)
hltL2TauJetsIso = cms.EDProducer( "HLTCaloJetCollectionProducer",
    TriggerTypes = cms.vint32( 84 ),
    HLTObject = cms.InputTag( "hltL2DiTauIsoFilter" )
)
hltDoubleL2IsoTau35eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltL2TauJetsIso" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltPFTauMediumAbsoluteIsolationDiscriminatorFor2015 = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( "hltPFTausFor2015" ),
    qualityCuts = cms.PSet( 
      isolationQualityCuts = cms.PSet( 
        minTrackHits = cms.uint32( 5 ),
        minTrackPt = cms.double( 0.5 ),
        maxTrackChi2 = cms.double( 100.0 ),
        minTrackPixelHits = cms.uint32( 2 ),
        minGammaEt = cms.double( 0.5 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        maxDeltaZ = cms.double( 0.2 ),
        maxTransverseImpactParameter = cms.double( 0.05 )
      ),
      signalQualityCuts = cms.PSet( 
        minTrackPt = cms.double( 0.0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.5 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minTrackHits = cms.uint32( 3 ),
        maxDeltaZ = cms.double( 0.4 ),
        maxTransverseImpactParameter = cms.double( 0.2 )
      ),
      primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
      pvFindingAlgo = cms.string( "closestInDeltaZ" ),
      vertexTrackFiltering = cms.bool( False ),
      recoverLeadingTrk = cms.bool( False ),
      vxAssocQualityCuts = cms.PSet( 
        minTrackPt = cms.double( 0.0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minTrackPixelHits = cms.uint32( 0 ),
        minTrackHits = cms.uint32( 3 ),
        minGammaEt = cms.double( 0.5 ),
        maxTransverseImpactParameter = cms.double( 0.2 )
      )
    ),
    maximumSumPtCut = cms.double( 2.0 ),
    deltaBetaPUTrackPtCutOverride = cms.double( 0.5 ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( True ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
    deltaBetaFactor = cms.string( "0.38" ),
    relativeSumPtCut = cms.double( 0.1 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    applyRelativeSumPtCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    storeRawSumPt = cms.bool( False ),
    applyRhoCorrection = cms.bool( False ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowForTaus" ),
    storeRawPUsumPt = cms.bool( False ),
    verbosity = cms.int32( 0 )
)
hltDoublePFTau35For2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPFTausFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltPFTauTrackPt1DiscriminatorFor2015 = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double( 1.0 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    UseOnlyChargedHadrons = cms.bool( True ),
    PFTauProducer = cms.InputTag( "hltPFTausFor2015" )
)
hltSelectedPFTausTrackPt1For2015 = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet( 
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauTrackPt1DiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      )
    ),
    cut = cms.string( "pt > 0" ),
    src = cms.InputTag( "hltPFTausFor2015" )
)
hltDoublePFTau35TrackPt1For2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackPt1For2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltSelectedPFTausTrackPt1MediumIsolationFor2015 = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet( 
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauTrackPt1DiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauMediumAbsoluteIsolationDiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      )
    ),
    cut = cms.string( "pt > 0" ),
    src = cms.InputTag( "hltPFTausFor2015" )
)
hltDoublePFTau35TrackPt1MediumIsolationFor2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackPt1MediumIsolationFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltSelectedPFTausTrackPt1MediumIsolationProng2For2015 = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet( 
    ),
    cut = cms.string( "signalPFChargedHadrCands().size() < 2.1" ),
    src = cms.InputTag( "hltSelectedPFTausTrackPt1MediumIsolationFor2015" )
)
hltDoublePFTau35TrackPt1MediumIsolationProng2For2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackPt1MediumIsolationProng2For2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationProng2MatchFor2015 = cms.EDProducer( "L1HLTTauMatching",
    L1TauTrigger = cms.InputTag( "hltL1sDoubleTauJet44erorDoubleJetC64" ),
    EtMin = cms.double( 0.0 ),
    JetSrc = cms.InputTag( "hltSelectedPFTausTrackPt1MediumIsolationProng2For2015" )
)
hltDoublePFTau35TrackPt1MediumIsolationProng2L1HLTMatchedFor2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationProng2MatchFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltDoublePFTau35TrackPt1MediumIsolationProng2Dz02For2015 = cms.EDFilter( "HLTPFTauPairDzMatchFilter",
    saveTags = cms.bool( True ),
    TriggerType = cms.int32( 84 ),
    JetSrc = cms.InputTag( "hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationProng2MatchFor2015" ),
    JetMinPt = cms.double( 35.0 ),
    JetMaxDZ = cms.double( 0.2 ),
    JetMinDR = cms.double( 0.5 ),
    JetMaxEta = cms.double( 2.1 )
)
hltPreDoubleMediumIsoPFTau35Trk1eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationMatchFor2015 = cms.EDProducer( "L1HLTTauMatching",
    L1TauTrigger = cms.InputTag( "hltL1sDoubleTauJet44erorDoubleJetC64" ),
    EtMin = cms.double( 0.0 ),
    JetSrc = cms.InputTag( "hltSelectedPFTausTrackPt1MediumIsolationFor2015" )
)
hltDoublePFTau35TrackPt1MediumIsolationL1HLTMatchedFor2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationMatchFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltDoublePFTau35TrackPt1MediumIsolationDz02For2015 = cms.EDFilter( "HLTPFTauPairDzMatchFilter",
    saveTags = cms.bool( True ),
    TriggerType = cms.int32( 84 ),
    JetSrc = cms.InputTag( "hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationMatchFor2015" ),
    JetMinPt = cms.double( 35.0 ),
    JetMaxDZ = cms.double( 0.2 ),
    JetMinDR = cms.double( 0.5 ),
    JetMaxEta = cms.double( 2.1 )
)
hltL1sL1ETM36or40 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ETM36 OR L1_ETM40" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreLooseIsoPFTau35Trk20Prong1MET70 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltFilterL2EtCutSingleIsoPFTau35Trk20 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 25.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 3.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltL2TauJets" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltMet = cms.EDProducer( "CaloMETProducer",
    resolutionsEra = cms.string( "Spring10" ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    jdpt9 = cms.vdouble( 0.843, 0.885, 1.245, 1.665, 1.944, 1.981, 1.972, 2.875, 3.923, 7.51 ),
    jdpt8 = cms.vdouble( 0.889, 0.939, 1.166, 1.365, 1.553, 1.805, 2.06, 2.22, 2.268, 2.247 ),
    jdpt7 = cms.vdouble( 1.094, 1.139, 1.436, 1.672, 1.831, 2.05, 2.267, 2.549, 2.785, 2.86 ),
    jdpt6 = cms.vdouble( 1.213, 1.298, 1.716, 2.015, 2.191, 2.612, 2.863, 2.879, 2.925, 2.902 ),
    jdpt5 = cms.vdouble( 1.049, 1.149, 1.607, 1.869, 2.012, 2.219, 2.289, 2.412, 2.695, 2.865 ),
    jdpt4 = cms.vdouble( 0.85, 0.961, 1.337, 1.593, 1.854, 2.005, 2.209, 2.533, 2.812, 3.047 ),
    jdpt3 = cms.vdouble( 0.929, 1.04, 1.46, 1.74, 2.042, 2.289, 2.639, 2.837, 2.946, 2.971 ),
    jdpt2 = cms.vdouble( 0.841, 0.937, 1.316, 1.605, 1.919, 2.295, 2.562, 2.722, 2.943, 3.293 ),
    jdpt1 = cms.vdouble( 0.718, 0.813, 1.133, 1.384, 1.588, 1.841, 2.115, 2.379, 2.508, 2.772 ),
    jdpt0 = cms.vdouble( 0.749, 0.829, 1.099, 1.355, 1.584, 1.807, 2.035, 2.217, 2.378, 2.591 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    alias = cms.string( "RawCaloMET" ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
    noHF = cms.bool( False ),
    PF_PhiResType2 = cms.vdouble( 0.002 ),
    PF_PhiResType3 = cms.vdouble( 0.002 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    resolutionsAlgo = cms.string( "AK5PF" ),
    PF_PhiResType6 = cms.vdouble( 0.02511 ),
    PF_PhiResType7 = cms.vdouble( 0.02511 ),
    PF_PhiResType4 = cms.vdouble( 0.0028, 0.0, 0.0022 ),
    PF_PhiResType5 = cms.vdouble( 0.1, 0.1, 0.13 ),
    ptresolthreshold = cms.double( 10.0 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
    PF_PhiResType1 = cms.vdouble( 0.002 ),
    globalThreshold = cms.double( 0.3 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    jdphi9 = cms.vdouble( 0.062, 0.059, 0.053, 0.047, 0.042, 0.045, 0.036, 0.032, 0.034, 0.044 ),
    jdphi8 = cms.vdouble( 0.059, 0.057, 0.051, 0.044, 0.038, 0.035, 0.037, 0.032, 0.028, 0.028 ),
    jdphi4 = cms.vdouble( 0.042, 0.042, 0.043, 0.042, 0.038, 0.036, 0.036, 0.033, 0.031, 0.031 ),
    jdphi3 = cms.vdouble( 0.042, 0.043, 0.044, 0.043, 0.041, 0.039, 0.039, 0.036, 0.034, 0.031 ),
    jdphi2 = cms.vdouble( 0.04, 0.04, 0.04, 0.04, 0.04, 0.038, 0.036, 0.035, 0.034, 0.033 ),
    jdphi1 = cms.vdouble( 0.034, 0.035, 0.035, 0.035, 0.035, 0.034, 0.031, 0.03, 0.029, 0.027 ),
    jdphi0 = cms.vdouble( 0.034, 0.034, 0.034, 0.034, 0.032, 0.031, 0.028, 0.027, 0.027, 0.027 ),
    jdphi7 = cms.vdouble( 0.077, 0.072, 0.059, 0.05, 0.045, 0.042, 0.039, 0.039, 0.037, 0.031 ),
    jdphi6 = cms.vdouble( 0.084, 0.08, 0.072, 0.065, 0.066, 0.06, 0.051, 0.049, 0.045, 0.045 ),
    jdphi5 = cms.vdouble( 0.069, 0.069, 0.064, 0.058, 0.053, 0.049, 0.049, 0.043, 0.039, 0.04 ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.005 ),
    HO_PhiResPar = cms.vdouble( 0.02511 ),
    PF_EtResType5 = cms.vdouble( 0.41, 0.52, 0.25 ),
    PF_EtResType4 = cms.vdouble( 0.042, 0.1, 0.0 ),
    PF_EtResType7 = cms.vdouble( 0.0, 1.22, 0.05 ),
    PF_EtResType6 = cms.vdouble( 0.0, 1.22, 0.05 ),
    PF_EtResType1 = cms.vdouble( 0.05, 0.0, 0.0 ),
    calculateSignificance = cms.bool( False ),
    PF_EtResType3 = cms.vdouble( 0.05, 0.0, 0.0 ),
    PF_EtResType2 = cms.vdouble( 0.05, 0.0, 0.0 )
)
hltMET70 = cms.EDFilter( "HLT1CaloMET",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 70.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltMet" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 87 )
)
hltPFTau35For2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPFTausFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltPFTau35TrackFor2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackFindingFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltPFTauTrackPt20DiscriminatorFor2015 = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double( 20.0 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    UseOnlyChargedHadrons = cms.bool( True ),
    PFTauProducer = cms.InputTag( "hltPFTausFor2015" )
)
hltSelectedPFTausTrackPt20For2015 = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet( 
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauTrackPt20DiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      )
    ),
    cut = cms.string( "pt > 0" ),
    src = cms.InputTag( "hltPFTausFor2015" )
)
hltPFTau35TrackPt20For2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackPt20For2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltSelectedPFTausTrackPt20IsolationFor2015 = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet( 
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauTrackPt20DiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(  discriminator = cms.InputTag( "hltPFTauLooseAbsoluteIsolationDiscriminatorFor2015" ),
        selectionCut = cms.double( 0.5 )
      )
    ),
    cut = cms.string( "pt > 0" ),
    src = cms.InputTag( "hltPFTausFor2015" )
)
hltPFTau35TrackPt20LooseIsoFor2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackPt20IsolationFor2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltSelectedPFTausTrackPt20IsolationProng2For2015 = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet( 
    ),
    cut = cms.string( "signalPFChargedHadrCands().size() < 2.1" ),
    src = cms.InputTag( "hltSelectedPFTausTrackPt20IsolationFor2015" )
)
hltPFTau35TrackPt20LooseIsoProng2For2015 = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltSelectedPFTausTrackPt20IsolationProng2For2015" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 )
)
hltL1sL1ETM36ORETM40 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ETM36 OR L1_ETM40" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPrePFMET150NoiseCleaned = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltMET90 = cms.EDFilter( "HLT1CaloMET",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 90.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltMet" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 87 )
)
hltMetClean = cms.EDProducer( "CaloMETProducer",
    resolutionsEra = cms.string( "Spring10" ),
    HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
    EE_PhiResPar = cms.vdouble( 0.02511 ),
    jdpt9 = cms.vdouble( 0.843, 0.885, 1.245, 1.665, 1.944, 1.981, 1.972, 2.875, 3.923, 7.51 ),
    jdpt8 = cms.vdouble( 0.889, 0.939, 1.166, 1.365, 1.553, 1.805, 2.06, 2.22, 2.268, 2.247 ),
    jdpt7 = cms.vdouble( 1.094, 1.139, 1.436, 1.672, 1.831, 2.05, 2.267, 2.549, 2.785, 2.86 ),
    jdpt6 = cms.vdouble( 1.213, 1.298, 1.716, 2.015, 2.191, 2.612, 2.863, 2.879, 2.925, 2.902 ),
    jdpt5 = cms.vdouble( 1.049, 1.149, 1.607, 1.869, 2.012, 2.219, 2.289, 2.412, 2.695, 2.865 ),
    jdpt4 = cms.vdouble( 0.85, 0.961, 1.337, 1.593, 1.854, 2.005, 2.209, 2.533, 2.812, 3.047 ),
    jdpt3 = cms.vdouble( 0.929, 1.04, 1.46, 1.74, 2.042, 2.289, 2.639, 2.837, 2.946, 2.971 ),
    jdpt2 = cms.vdouble( 0.841, 0.937, 1.316, 1.605, 1.919, 2.295, 2.562, 2.722, 2.943, 3.293 ),
    jdpt1 = cms.vdouble( 0.718, 0.813, 1.133, 1.384, 1.588, 1.841, 2.115, 2.379, 2.508, 2.772 ),
    jdpt0 = cms.vdouble( 0.749, 0.829, 1.099, 1.355, 1.584, 1.807, 2.035, 2.217, 2.378, 2.591 ),
    HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
    alias = cms.string( "RawCaloMET" ),
    HF_PhiResPar = cms.vdouble( 0.05022 ),
    HE_PhiResPar = cms.vdouble( 0.02511 ),
    HB_PhiResPar = cms.vdouble( 0.02511 ),
    EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
    noHF = cms.bool( False ),
    PF_PhiResType2 = cms.vdouble( 0.002 ),
    PF_PhiResType3 = cms.vdouble( 0.002 ),
    HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
    resolutionsAlgo = cms.string( "AK5PF" ),
    PF_PhiResType6 = cms.vdouble( 0.02511 ),
    PF_PhiResType7 = cms.vdouble( 0.02511 ),
    PF_PhiResType4 = cms.vdouble( 0.0028, 0.0, 0.0022 ),
    PF_PhiResType5 = cms.vdouble( 0.1, 0.1, 0.13 ),
    ptresolthreshold = cms.double( 10.0 ),
    EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
    PF_PhiResType1 = cms.vdouble( 0.002 ),
    globalThreshold = cms.double( 0.3 ),
    EB_PhiResPar = cms.vdouble( 0.00502 ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    jdphi9 = cms.vdouble( 0.062, 0.059, 0.053, 0.047, 0.042, 0.045, 0.036, 0.032, 0.034, 0.044 ),
    jdphi8 = cms.vdouble( 0.059, 0.057, 0.051, 0.044, 0.038, 0.035, 0.037, 0.032, 0.028, 0.028 ),
    jdphi4 = cms.vdouble( 0.042, 0.042, 0.043, 0.042, 0.038, 0.036, 0.036, 0.033, 0.031, 0.031 ),
    jdphi3 = cms.vdouble( 0.042, 0.043, 0.044, 0.043, 0.041, 0.039, 0.039, 0.036, 0.034, 0.031 ),
    jdphi2 = cms.vdouble( 0.04, 0.04, 0.04, 0.04, 0.04, 0.038, 0.036, 0.035, 0.034, 0.033 ),
    jdphi1 = cms.vdouble( 0.034, 0.035, 0.035, 0.035, 0.035, 0.034, 0.031, 0.03, 0.029, 0.027 ),
    jdphi0 = cms.vdouble( 0.034, 0.034, 0.034, 0.034, 0.032, 0.031, 0.028, 0.027, 0.027, 0.027 ),
    jdphi7 = cms.vdouble( 0.077, 0.072, 0.059, 0.05, 0.045, 0.042, 0.039, 0.039, 0.037, 0.031 ),
    jdphi6 = cms.vdouble( 0.084, 0.08, 0.072, 0.065, 0.066, 0.06, 0.051, 0.049, 0.045, 0.045 ),
    jdphi5 = cms.vdouble( 0.069, 0.069, 0.064, 0.058, 0.053, 0.049, 0.049, 0.043, 0.039, 0.04 ),
    HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.005 ),
    HO_PhiResPar = cms.vdouble( 0.02511 ),
    PF_EtResType5 = cms.vdouble( 0.41, 0.52, 0.25 ),
    PF_EtResType4 = cms.vdouble( 0.042, 0.1, 0.0 ),
    PF_EtResType7 = cms.vdouble( 0.0, 1.22, 0.05 ),
    PF_EtResType6 = cms.vdouble( 0.0, 1.22, 0.05 ),
    PF_EtResType1 = cms.vdouble( 0.05, 0.0, 0.0 ),
    calculateSignificance = cms.bool( False ),
    PF_EtResType3 = cms.vdouble( 0.05, 0.0, 0.0 ),
    PF_EtResType2 = cms.vdouble( 0.05, 0.0, 0.0 )
)
hltMETClean80 = cms.EDFilter( "HLT1CaloMET",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 80.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltMetClean" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 87 )
)
hltMetCleanUsingJetID = cms.EDProducer( "HLTMETCleanerUsingJetID",
    minPt = cms.double( 20.0 ),
    maxEta = cms.double( 5.0 ),
    jetsLabel = cms.InputTag( "hltAntiKT4CaloJets" ),
    usePt = cms.bool( False ),
    goodJetsLabel = cms.InputTag( "hltCaloJetIDPassed" ),
    metLabel = cms.InputTag( "hltMet" )
)
hltMETCleanUsingJetID80 = cms.EDFilter( "HLT1CaloMET",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 80.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltMetCleanUsingJetID" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 87 )
)
hltParticleFlowBlock = cms.EDProducer( "PFBlockProducer",
    debug = cms.untracked.bool( False ),
    linkDefinitions = cms.VPSet( 
      cms.PSet(  useKDTree = cms.bool( True ),
        linkType = cms.string( "PS1:ECAL" ),
        linkerName = cms.string( "PreshowerAndECALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( True ),
        linkType = cms.string( "PS2:ECAL" ),
        linkerName = cms.string( "PreshowerAndECALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( True ),
        linkType = cms.string( "TRACK:ECAL" ),
        linkerName = cms.string( "TrackAndECALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( True ),
        linkType = cms.string( "TRACK:HCAL" ),
        linkerName = cms.string( "TrackAndHCALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( False ),
        linkType = cms.string( "ECAL:HCAL" ),
        linkerName = cms.string( "ECALAndHCALLinker" )
      ),
      cms.PSet(  useKDTree = cms.bool( False ),
        linkType = cms.string( "HFEM:HFHAD" ),
        linkerName = cms.string( "HFEMAndHFHADLinker" )
      )
    ),
    elementImporters = cms.VPSet( 
      cms.PSet(  importerName = cms.string( "GeneralTracksImporter" ),
        useIterativeTracking = cms.bool( False ),
        source = cms.InputTag( "hltLightPFTracks" ),
        NHitCuts_byTrackAlgo = cms.vuint32( 3, 3, 3, 3, 3 ),
        muonSrc = cms.InputTag( "hltMuons" ),
        DPtOverPtCuts_byTrackAlgo = cms.vdouble( 0.5, 0.5, 0.5, 0.5, 0.5 )
      ),
      cms.PSet(  importerName = cms.string( "ECALClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterECALUnseeded" ),
        BCtoPFCMap = cms.InputTag( "" )
      ),
      cms.PSet(  importerName = cms.string( "GenericClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterHCAL" )
      ),
      cms.PSet(  importerName = cms.string( "GenericClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterHFEM" )
      ),
      cms.PSet(  importerName = cms.string( "GenericClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterHFHAD" )
      ),
      cms.PSet(  importerName = cms.string( "GenericClusterImporter" ),
        source = cms.InputTag( "hltParticleFlowClusterPSUnseeded" )
      )
    ),
    verbose = cms.untracked.bool( False )
)
hltParticleFlow = cms.EDProducer( "PFProducer",
    photon_SigmaiEtaiEta_endcap = cms.double( 0.034 ),
    minPtForPostCleaning = cms.double( 20.0 ),
    pf_nsigma_ECAL = cms.double( 0.0 ),
    GedPhotonValueMap = cms.InputTag( 'tmpGedPhotons','valMapPFEgammaCandToPhoton' ),
    sumPtTrackIsoForPhoton = cms.double( -1.0 ),
    metFactorForFakes = cms.double( 4.0 ),
    muon_HO = cms.vdouble( 0.9, 0.9 ),
    electron_missinghits = cms.uint32( 1 ),
    metSignificanceForCleaning = cms.double( 3.0 ),
    usePFPhotons = cms.bool( False ),
    dptRel_DispVtx = cms.double( 10.0 ),
    nTrackIsoForEgammaSC = cms.uint32( 2 ),
    pf_nsigma_HCAL = cms.double( 1.0 ),
    cosmicRejectionDistance = cms.double( 1.0 ),
    useEGammaFilters = cms.bool( False ),
    useEGammaElectrons = cms.bool( False ),
    nsigma_TRACK = cms.double( 1.0 ),
    useEGammaSupercluster = cms.bool( False ),
    sumPtTrackIsoForEgammaSC_barrel = cms.double( 4.0 ),
    eventFractionForCleaning = cms.double( 0.8 ),
    usePFDecays = cms.bool( False ),
    rejectTracks_Step45 = cms.bool( False ),
    eventFractionForRejection = cms.double( 0.8 ),
    photon_MinEt = cms.double( 10.0 ),
    usePFNuclearInteractions = cms.bool( False ),
    maxSignificance = cms.double( 2.5 ),
    electron_iso_mva_endcap = cms.double( -0.1075 ),
    debug = cms.untracked.bool( False ),
    pf_convID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt" ),
    calibHF_eta_step = cms.vdouble( 0.0, 2.9, 3.0, 3.2, 4.2, 4.4, 4.6, 4.8, 5.2, 5.4 ),
    ptErrorScale = cms.double( 8.0 ),
    minSignificance = cms.double( 2.5 ),
    minMomentumForPunchThrough = cms.double( 100.0 ),
    pf_conv_mvaCut = cms.double( 0.0 ),
    useCalibrationsFromDB = cms.bool( True ),
    usePFElectrons = cms.bool( False ),
    electron_iso_combIso_endcap = cms.double( 10.0 ),
    photon_combIso = cms.double( 10.0 ),
    electron_iso_mva_barrel = cms.double( -0.1875 ),
    postHFCleaning = cms.bool( False ),
    factors_45 = cms.vdouble( 10.0, 100.0 ),
    cleanedHF = cms.VInputTag( 'hltParticleFlowRecHitHCAL:Cleaned','hltParticleFlowClusterHFHAD:Cleaned','hltParticleFlowClusterHFEM:Cleaned' ),
    coneEcalIsoForEgammaSC = cms.double( 0.3 ),
    minSignificanceReduction = cms.double( 1.4 ),
    photon_SigmaiEtaiEta_barrel = cms.double( 0.0125 ),
    calibHF_b_HADonly = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 0.94348, 0.9437, 1.0034, 1.0444, 1.0444 ),
    minPixelHits = cms.int32( 1 ),
    maxDPtOPt = cms.double( 1.0 ),
    useHO = cms.bool( False ),
    pf_electron_output_col = cms.string( "electrons" ),
    electron_noniso_mvaCut = cms.double( -0.1 ),
    GedElectronValueMap = cms.InputTag( "gedGsfElectronsTmp" ),
    useVerticesForNeutral = cms.bool( True ),
    pf_Res_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFRes.root" ),
    PFEGammaCandidates = cms.InputTag( "particleFlowEGamma" ),
    sumPtTrackIsoSlopeForPhoton = cms.double( -1.0 ),
    coneTrackIsoForEgammaSC = cms.double( 0.3 ),
    minDeltaMet = cms.double( 0.4 ),
    pt_Error = cms.double( 1.0 ),
    useProtectionsForJetMET = cms.bool( True ),
    metFactorForRejection = cms.double( 4.0 ),
    sumPtTrackIsoForEgammaSC_endcap = cms.double( 4.0 ),
    calibHF_use = cms.bool( False ),
    verbose = cms.untracked.bool( False ),
    usePFConversions = cms.bool( False ),
    trackQuality = cms.string( "highPurity" ),
    calibPFSCEle_endcap = cms.vdouble( 1.153, -16.5975, 5.668, -0.1772, 16.22, 7.326, 0.0483, -4.068, 9.406 ),
    metFactorForCleaning = cms.double( 4.0 ),
    eventFactorForCosmics = cms.double( 10.0 ),
    egammaElectrons = cms.InputTag( "" ),
    minEnergyForPunchThrough = cms.double( 100.0 ),
    minTrackerHits = cms.int32( 8 ),
    iCfgCandConnector = cms.PSet( 
      bCalibSecondary = cms.bool( False ),
      bCalibPrimary = cms.bool( False ),
      bCorrect = cms.bool( False ),
      nuclCalibFactors = cms.vdouble( 0.8, 0.15, 0.5, 0.5, 0.05 )
    ),
    rejectTracks_Bad = cms.bool( False ),
    pf_electronID_crackCorrection = cms.bool( False ),
    pf_locC_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFClusterCorr.root" ),
    calibHF_a_EMonly = cms.vdouble( 0.96945, 0.96701, 0.76309, 0.82268, 0.87583, 0.89718, 0.98674, 1.4681, 1.458, 1.458 ),
    muons = cms.InputTag( "hltMuons" ),
    metFactorForHighEta = cms.double( 25.0 ),
    minHFCleaningPt = cms.double( 5.0 ),
    muon_HCAL = cms.vdouble( 3.0, 3.0 ),
    pf_electron_mvaCut = cms.double( -0.1 ),
    ptFactorForHighEta = cms.double( 2.0 ),
    maxDeltaPhiPt = cms.double( 7.0 ),
    pf_electronID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt" ),
    sumEtEcalIsoForEgammaSC_endcap = cms.double( 2.0 ),
    calibHF_b_EMHAD = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 0.94348, 0.9437, 1.0034, 1.0444, 1.0444 ),
    pf_GlobC_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFGlobalCorr.root" ),
    photon_HoE = cms.double( 0.1 ),
    sumEtEcalIsoForEgammaSC_barrel = cms.double( 1.0 ),
    calibPFSCEle_Fbrem_endcap = cms.vdouble( 0.9, 6.5, -0.0692932, 0.101776, 0.995338, -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 0.923165, 4.74665E-4, 1.10782 ),
    punchThroughFactor = cms.double( 3.0 ),
    algoType = cms.uint32( 0 ),
    electron_iso_combIso_barrel = cms.double( 10.0 ),
    postMuonCleaning = cms.bool( True ),
    calibPFSCEle_barrel = cms.vdouble( 1.004, -1.536, 22.88, -1.467, 0.3555, 0.6227, 14.65, 2051.0, 25.0, 0.9932, -0.5444, 0.0, 0.5438, 0.7109, 7.645, 0.2904, 0.0 ),
    electron_protectionsForJetMET = cms.PSet( 
      maxE = cms.double( 50.0 ),
      maxTrackPOverEele = cms.double( 1.0 ),
      maxEcalEOverP_2 = cms.double( 0.2 ),
      maxHcalEOverEcalE = cms.double( 0.1 ),
      maxEcalEOverP_1 = cms.double( 0.5 ),
      maxHcalEOverP = cms.double( 1.0 ),
      maxEcalEOverPRes = cms.double( 0.2 ),
      maxHcalE = cms.double( 10.0 ),
      maxEeleOverPout = cms.double( 0.2 ),
      maxNtracks = cms.double( 3.0 ),
      maxEleHcalEOverEcalE = cms.double( 0.1 ),
      maxDPhiIN = cms.double( 0.1 ),
      maxEeleOverPoutRes = cms.double( 0.5 )
    ),
    electron_iso_pt = cms.double( 10.0 ),
    isolatedElectronID_mvaWeightFile = cms.string( "RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml" ),
    vertexCollection = cms.InputTag( "hltPixelVertices" ),
    X0_Map = cms.string( "RecoParticleFlow/PFProducer/data/allX0histos.root" ),
    calibPFSCEle_Fbrem_barrel = cms.vdouble( 0.6, 6.0, -0.0255975, 0.0576727, 0.975442, -5.46394E-4, 1.26147, 25.0, -0.02025, 0.04537, 0.9728, -8.962E-4, 1.172 ),
    blocks = cms.InputTag( "hltParticleFlowBlock" ),
    punchThroughMETFactor = cms.double( 4.0 ),
    metSignificanceForRejection = cms.double( 4.0 ),
    photon_protectionsForJetMET = cms.PSet( 
      sumPtTrackIsoSlope = cms.double( 0.001 ),
      sumPtTrackIso = cms.double( 2.0 )
    ),
    usePhotonReg = cms.bool( False ),
    dzPV = cms.double( 0.2 ),
    calibHF_a_EMHAD = cms.vdouble( 1.42215, 1.00496, 0.68961, 0.81656, 0.98504, 0.98504, 1.00802, 1.0593, 1.4576, 1.4576 ),
    useRegressionFromDB = cms.bool( False ),
    muon_ECAL = cms.vdouble( 0.5, 0.5 ),
    usePFSCEleCalib = cms.bool( True )
)
hltFixedGridRhoFastjetAll = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 5.0 ),
    pfCandidatesTag = cms.InputTag( "hltParticleFlow" )
)
hltAntiKT4PFJets = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "PFJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.4 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltParticleFlow" ),
    inputEtMin = cms.double( 0.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "hltPixelVertices" ),
    jetPtMin = cms.double( 0.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 0 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltAK4PFJetL1FastL2L3Corrected = cms.EDProducer( "PFJetCorrectionProducer",
    src = cms.InputTag( "hltAntiKT4PFJets" ),
    correctors = cms.vstring( 'hltESPAK4PFL1L2L3' )
)
hltPFMETProducer = cms.EDProducer( "HLTMhtProducer",
    usePt = cms.bool( True ),
    minPtJet = cms.double( 0.0 ),
    jetsLabel = cms.InputTag( "hltAntiKT4PFJets" ),
    minNJet = cms.int32( 0 ),
    maxEtaJet = cms.double( 999.0 ),
    excludePFMuons = cms.bool( False ),
    pfCandidatesLabel = cms.InputTag( "hltParticleFlow" )
)
hltPFMET150Filter = cms.EDFilter( "HLTMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltPFMETProducer' ),
    minMht = cms.vdouble( 150.0 )
)
hltPrePFMET180NoiseCleaned = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltPFMET180Filter = cms.EDFilter( "HLTMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltPFMETProducer' ),
    minMht = cms.vdouble( 180.0 )
)
hltPreMonoCentralPFNoPUJet100PFMET100NHF0p95NCH1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltMETClean60 = cms.EDFilter( "HLT1CaloMET",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 60.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltMetClean" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 87 )
)
hltCentralJet85L1FastJetCorrected = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 85.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltPFMETNoMuProducer = cms.EDProducer( "HLTMhtProducer",
    usePt = cms.bool( True ),
    minPtJet = cms.double( 0.0 ),
    jetsLabel = cms.InputTag( "hltAntiKT4PFJets" ),
    minNJet = cms.int32( 0 ),
    maxEtaJet = cms.double( 999.0 ),
    excludePFMuons = cms.bool( True ),
    pfCandidatesLabel = cms.InputTag( "hltParticleFlow" )
)
hltPFMETorPFMETNoMu100 = cms.EDFilter( "HLTMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltPFMETProducer','hltPFMETNoMuProducer' ),
    minMht = cms.vdouble( 100.0, 100.0 )
)
hltAK4PFJetIDPassedL1FastL2L3Corrected = cms.EDProducer( "HLTPFJetIDProducer",
    CEF = cms.double( 99.0 ),
    NHF = cms.double( 0.95 ),
    minPt = cms.double( 20.0 ),
    CHF = cms.double( -99.0 ),
    NEF = cms.double( 99.0 ),
    NTOT = cms.int32( -1 ),
    NCH = cms.int32( 0 ),
    jetsInput = cms.InputTag( "hltAK4PFJetL1FastL2L3Corrected" )
)
hltCentralPFJetIDPassed85 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 85.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFJetIDPassedL1FastL2L3Corrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltOnlinePrimaryVertices = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  maxDistanceToBeam = cms.double( 1.0 ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "" )
      ),
      cms.PSet(  maxDistanceToBeam = cms.double( 1.0 ),
        useBeamConstraint = cms.bool( True ),
        minNdof = cms.double( 2.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "WithBS" )
      )
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet( 
      maxNormalizedChi2 = cms.double( 20.0 ),
      minPt = cms.double( 0.0 ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 5.0 ),
      trackQuality = cms.string( "any" ),
      minPixelLayersWithHits = cms.int32( 2 ),
      minSiliconLayersWithHits = cms.int32( 5 )
    ),
    beamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltPFMuonMerging" ),
    TkClusParameters = cms.PSet( 
      TkDAClusParameters = cms.PSet( 
        d0CutOff = cms.double( 3.0 ),
        Tmin = cms.double( 4.0 ),
        dzCutOff = cms.double( 4.0 ),
        coolingFactor = cms.double( 0.6 ),
        use_vdt = cms.untracked.bool( True ),
        vertexSize = cms.double( 0.01 )
      ),
      algorithm = cms.string( "DA" )
    )
)
hltGoodOnlinePVs = cms.EDFilter( "PrimaryVertexObjectFilter",
    src = cms.InputTag( "hltOnlinePrimaryVertices" ),
    filterParams = cms.PSet( 
      maxZ = cms.double( 24.0 ),
      minNdof = cms.double( 4.0 ),
      maxRho = cms.double( 2.0 ),
      pvSrc = cms.InputTag( "hltOnlinePrimaryVertices" )
    )
)
hltParticleFlowPtrs = cms.EDProducer( "PFCandidateFwdPtrProducer",
    src = cms.InputTag( "hltParticleFlow" )
)
hltPFPileUp = cms.EDProducer( "PFPileUp",
    checkClosestZVertex = cms.bool( False ),
    Enable = cms.bool( True ),
    PFCandidates = cms.InputTag( "hltParticleFlowPtrs" ),
    verbose = cms.untracked.bool( False ),
    Vertices = cms.InputTag( "hltGoodOnlinePVs" )
)
hltPFNoPileUp = cms.EDProducer( "TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag( "hltParticleFlowPtrs" ),
    enable = cms.bool( True ),
    topCollection = cms.InputTag( "hltPFPileUp" ),
    name = cms.untracked.string( "pileUpOnPFCandidates" ),
    verbose = cms.untracked.bool( False )
)
hltAntiKT4PFJetsNoPU = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( -9.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "PFJet" ),
    minSeed = cms.uint32( 0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.4 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltPFNoPileUp" ),
    inputEtMin = cms.double( 0.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "hltPixelVertices" ),
    jetPtMin = cms.double( 0.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 0 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)
hltAK4PFJetL1FastL2L3CorrectedNoPU = cms.EDProducer( "PFJetCorrectionProducer",
    src = cms.InputTag( "hltAntiKT4PFJetsNoPU" ),
    correctors = cms.vstring( 'hltESPAK4PFNoPUL1L2L3' )
)
hltCentralPFJet100NoPU = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 100.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFJetL1FastL2L3CorrectedNoPU" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltPreDiCentralPFNoPUJet6030PFMET100dphi0p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltCentralJet40L1FastJetCorrected = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltDiCentralJet20L1FastJetCorrected = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltMinDPhiMET0p5Filter = cms.EDFilter( "HLTMinDPhiMETFilter",
    saveTags = cms.bool( False ),
    maxNJets = cms.int32( 2 ),
    minPt = cms.double( 30.0 ),
    maxEta = cms.double( 2.6 ),
    calometLabel = cms.InputTag( "" ),
    jetsLabel = cms.InputTag( "hltAK4PFJetL1FastL2L3Corrected" ),
    usePt = cms.bool( True ),
    triggerType = cms.int32( 85 ),
    metLabel = cms.InputTag( "hltPFMETProducer" ),
    minDPhi = cms.double( 0.5 )
)
hltCentralPFJet60NoPU = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 60.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFJetL1FastL2L3CorrectedNoPU" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltDiCentralPFJet30NoPUer2p6 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 30.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFJetL1FastL2L3CorrectedNoPU" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltL1sL1DoubleJetC36ETM30ORL1DoubleJetC44ETM30 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleJetC36_ETM30 OR L1_DoubleJetC44_ETM30" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPreDiCentralPFNoPUJet60PFMET80dphi0p3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltMET65 = cms.EDFilter( "HLT1CaloMET",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 65.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltMet" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 87 )
)
hltMETClean55 = cms.EDFilter( "HLT1CaloMET",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 55.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltMetClean" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 87 )
)
hltDiCentralJet40L1FastJetCorrected = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltPFMETorPFMETNoMu80 = cms.EDFilter( "HLTMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltPFMETProducer','hltPFMETNoMuProducer' ),
    minMht = cms.vdouble( 80.0, 80.0 )
)
hltMinDPhiMET0p3Filter = cms.EDFilter( "HLTMinDPhiMETFilter",
    saveTags = cms.bool( False ),
    maxNJets = cms.int32( 2 ),
    minPt = cms.double( 30.0 ),
    maxEta = cms.double( 2.6 ),
    calometLabel = cms.InputTag( "" ),
    jetsLabel = cms.InputTag( "hltAK4PFJetL1FastL2L3Corrected" ),
    usePt = cms.bool( True ),
    triggerType = cms.int32( 85 ),
    metLabel = cms.InputTag( "hltPFMETProducer" ),
    minDPhi = cms.double( 0.3 )
)
hltDiCentralPFJet60NoPUer2p6 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 60.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFJetL1FastL2L3CorrectedNoPU" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltPreDiCentralPFNoPUJet30PFMET80BTagCSV07 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltSelectorCentralJets20L1FastJet = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    etMin = cms.double( 20.0 )
)
hltSelector4CentralJetsL1FastJet = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelectorCentralJets20L1FastJet" )
)
hltFastPVPixelVertexFilter = cms.EDFilter( "VertexSelector",
    filter = cms.bool( True ),
    src = cms.InputTag( "hltFastPrimaryVertex" ),
    cut = cms.string( "!isFake && ndof > 0 && abs(z) <= 25 && position.Rho <= 2" )
)
hltFastPVJetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltSelector4CentralJetsL1FastJet" ),
    tracks = cms.InputTag( "hltFastPVPixelTracks" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
hltFastPVJetVertexChecker = cms.EDFilter( "JetVertexChecker",
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    maxNJetsToCheck = cms.int32( 2 ),
    minPtRatio = cms.double( 0.1 ),
    doFilter = cms.bool( False ),
    jetTracks = cms.InputTag( "hltFastPVJetTracksAssociator" ),
    minPt = cms.double( 0.0 )
)
hltFastPVPixelTracksMerger = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( False ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltFastPVPixelTracks" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltFastPVPixelTracksRecover" ),
    LostHitPenalty = cms.double( 20.0 ),
    FoundHitBonus = cms.double( 5.0 )
)
hltFastPVPixelVertices = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltFastPVPixelTracksMerger" ),
    PtMin = cms.double( 0.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 10.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
hltFastPVPixelVertexSelector = cms.EDFilter( "VertexSelector",
    filter = cms.bool( True ),
    src = cms.InputTag( "hltFastPVPixelVertices" ),
    cut = cms.string( "!isFake && ndof > 0 && abs(z) <= 25 && position.Rho <= 2" )
)
hltVerticesL3 = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  maxDistanceToBeam = cms.double( 1.0 ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "" )
      ),
      cms.PSet(  maxDistanceToBeam = cms.double( 1.0 ),
        useBeamConstraint = cms.bool( True ),
        minNdof = cms.double( 0.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "WithBS" )
      )
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet( 
      maxNormalizedChi2 = cms.double( 20.0 ),
      minPt = cms.double( 0.0 ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 999.0 ),
      trackQuality = cms.string( "any" ),
      minPixelLayersWithHits = cms.int32( 2 ),
      minSiliconLayersWithHits = cms.int32( 5 )
    ),
    beamSpotLabel = cms.InputTag( "offlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltForBTagIter2Merged" ),
    TkClusParameters = cms.PSet( 
      TkDAClusParameters = cms.PSet( 
        d0CutOff = cms.double( 999.0 ),
        Tmin = cms.double( 4.0 ),
        dzCutOff = cms.double( 4.0 ),
        coolingFactor = cms.double( 0.6 ),
        use_vdt = cms.untracked.bool( True ),
        vertexSize = cms.double( 0.15 )
      ),
      algorithm = cms.string( "DA_vect" )
    )
)
hltFastPixelBLifetimeL3Associator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltSelector4CentralJetsL1FastJet" ),
    tracks = cms.InputTag( "hltForBTagIter2Merged" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
hltFastPixelBLifetimeL3TagInfos = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumNumberOfHits = cms.int32( 8 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltVerticesL3","WithBS" ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltFastPixelBLifetimeL3Associator" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( False ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 20.0 )
)
hltL3SecondaryVertexTagInfos = cms.EDProducer( "SecondaryVertexProducer",
    extSVDeltaRToJet = cms.double( 0.3 ),
    beamSpotTag = cms.InputTag( "offlineBeamSpot" ),
    vertexReco = cms.PSet( 
      primcut = cms.double( 1.8 ),
      seccut = cms.double( 6.0 ),
      smoothing = cms.bool( False ),
      weightthreshold = cms.double( 0.001 ),
      minweight = cms.double( 0.5 ),
      finder = cms.string( "avr" )
    ),
    vertexSelection = cms.PSet(  sortCriterium = cms.string( "dist3dError" ) ),
    constraint = cms.string( "BeamSpot" ),
    trackIPTagInfos = cms.InputTag( "hltFastPixelBLifetimeL3TagInfos" ),
    vertexCuts = cms.PSet( 
      distSig3dMax = cms.double( 99999.9 ),
      fracPV = cms.double( 0.65 ),
      distVal2dMax = cms.double( 2.5 ),
      useTrackWeights = cms.bool( True ),
      maxDeltaRToJetAxis = cms.double( 0.5 ),
      v0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
      distSig2dMin = cms.double( 3.0 ),
      multiplicityMin = cms.uint32( 2 ),
      distVal2dMin = cms.double( 0.01 ),
      distSig2dMax = cms.double( 99999.9 ),
      distVal3dMax = cms.double( 99999.9 ),
      minimumTrackWeight = cms.double( 0.5 ),
      distVal3dMin = cms.double( -99999.9 ),
      massMax = cms.double( 6.5 ),
      distSig3dMin = cms.double( -99999.9 )
    ),
    useExternalSV = cms.bool( False ),
    minimumTrackWeight = cms.double( 0.5 ),
    usePVError = cms.bool( True ),
    trackSelection = cms.PSet( 
      totalHitsMin = cms.uint32( 2 ),
      jetDeltaRMax = cms.double( 0.3 ),
      qualityClass = cms.string( "any" ),
      pixelHitsMin = cms.uint32( 2 ),
      sip3dSigMin = cms.double( -99999.9 ),
      sip3dSigMax = cms.double( 99999.9 ),
      normChi2Max = cms.double( 99999.9 ),
      maxDistToAxis = cms.double( 0.2 ),
      sip2dValMax = cms.double( 99999.9 ),
      maxDecayLen = cms.double( 99999.9 ),
      ptMin = cms.double( 1.0 ),
      sip2dSigMax = cms.double( 99999.9 ),
      sip2dSigMin = cms.double( -99999.9 ),
      sip3dValMax = cms.double( 99999.9 ),
      sip2dValMin = cms.double( -99999.9 ),
      sip3dValMin = cms.double( -99999.9 )
    ),
    trackSort = cms.string( "sip3dSig" ),
    extSVCollection = cms.InputTag( "secondaryVertices" )
)
hltL3CombinedSecondaryVertexBJetTags = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltCombinedSecondaryVertex" ),
    tagInfos = cms.VInputTag( 'hltFastPixelBLifetimeL3TagInfos','hltL3SecondaryVertexTagInfos' )
)
hltBLifetimeL3FilterCSV = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltL3CombinedSecondaryVertexBJetTags" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltSelector4CentralJetsL1FastJet" ),
    MinTag = cms.double( 0.7 ),
    MaxTag = cms.double( 99999.0 )
)
hltPFMET80Filter = cms.EDFilter( "HLTMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltPFMETProducer' ),
    minMht = cms.vdouble( 80.0 )
)
hltPreDiCentralPFNoPUJet30PFMET80 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltL1sL1HTT150OrHTT175 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_HTT150 OR L1_HTT175" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "l1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    L1CollectionsTag = cms.InputTag( "l1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "gtDigis" ),
    L1TechTriggerSeeding = cms.bool( False )
)
hltPrePFNoPUHT400DiCentralPFNoPUJet40PFMET80 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltHtMht = cms.EDProducer( "HLTHtMhtProducer",
    usePt = cms.bool( False ),
    minPtJetHt = cms.double( 40.0 ),
    maxEtaJetMht = cms.double( 5.0 ),
    minNJetMht = cms.int32( 0 ),
    jetsLabel = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
    maxEtaJetHt = cms.double( 3.0 ),
    minPtJetMht = cms.double( 30.0 ),
    minNJetHt = cms.int32( 0 ),
    pfCandidatesLabel = cms.InputTag( "" ),
    excludePFMuons = cms.bool( False )
)
hltHt350 = cms.EDFilter( "HLTHtMhtFilter",
    saveTags = cms.bool( False ),
    mhtLabels = cms.VInputTag( 'hltHtMht' ),
    meffSlope = cms.vdouble( 1.0 ),
    minMeff = cms.vdouble( 0.0 ),
    minMht = cms.vdouble( 0.0 ),
    htLabels = cms.VInputTag( 'hltHtMht' ),
    minHt = cms.vdouble( 350.0 )
)
hltPFHTNoPU = cms.EDProducer( "HLTHtMhtProducer",
    usePt = cms.bool( True ),
    minPtJetHt = cms.double( 40.0 ),
    maxEtaJetMht = cms.double( 999.0 ),
    minNJetMht = cms.int32( 0 ),
    jetsLabel = cms.InputTag( "hltAK4PFJetL1FastL2L3CorrectedNoPU" ),
    maxEtaJetHt = cms.double( 3.0 ),
    minPtJetMht = cms.double( 0.0 ),
    minNJetHt = cms.int32( 0 ),
    pfCandidatesLabel = cms.InputTag( "hltParticleFlow" ),
    excludePFMuons = cms.bool( False )
)
hltPFHT400NoPU = cms.EDFilter( "HLTHtMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltPFHTNoPU' ),
    meffSlope = cms.vdouble( 1.0 ),
    minMeff = cms.vdouble( 0.0 ),
    minMht = cms.vdouble( 0.0 ),
    htLabels = cms.VInputTag( 'hltPFHTNoPU' ),
    minHt = cms.vdouble( 400.0 )
)
hltDiCentralPFJet40NoPUer2p6 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.6 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4PFJetL1FastL2L3CorrectedNoPU" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
hltPrePFchMET90NoiseCleaned = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltPFchMETProducer = cms.EDProducer( "HLTTrackMETProducer",
    pfRecTracksLabel = cms.InputTag( "hltLightPFTracks" ),
    tracksLabel = cms.InputTag( "hltL3Muons" ),
    useTracks = cms.bool( False ),
    minPtJet = cms.double( 0.0 ),
    usePFCandidates = cms.bool( False ),
    jetsLabel = cms.InputTag( "hltAntiKT4PFJets" ),
    minNJet = cms.int32( 0 ),
    usePFCandidatesCharged = cms.bool( True ),
    maxEtaJet = cms.double( 999.0 ),
    excludePFMuons = cms.bool( False ),
    pfCandidatesLabel = cms.InputTag( "hltParticleFlow" ),
    usePt = cms.bool( True ),
    usePFRecTracks = cms.bool( False )
)
hltPFchMET90Filter = cms.EDFilter( "HLTMhtFilter",
    saveTags = cms.bool( True ),
    mhtLabels = cms.VInputTag( 'hltPFchMETProducer' ),
    minMht = cms.vdouble( 90.0 )
)
hltPreBTagCSV07 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "gtDigis" ),
    offset = cms.uint32( 0 )
)
hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
hltPixelVertices = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "offlineBeamSpot" ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracks" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)

HLTMuonLocalRecoSequence = cms.Sequence( cms.SequencePlaceholder( "simMuonDTDigis" ) + hltDt1DRecHits + hltDt4DSegments + cms.SequencePlaceholder( "simMuonCSCDigis" ) + hltCsc2DRecHits + hltCscSegments + cms.SequencePlaceholder( "simMuonRPCDigis" ) + hltRpcRecHits )
HLTL2muonrecoNocandSequence = cms.Sequence( HLTMuonLocalRecoSequence + hltL2OfflineMuonSeeds + hltL2MuonSeeds + hltL2Muons )
HLTL2muonrecoSequence = cms.Sequence( HLTL2muonrecoNocandSequence + hltL2MuonCandidates )
HLTL3NoFiltersmuonTkCandidateSequence = cms.Sequence( HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL3TrajSeedOIState + hltL3TrackCandidateFromL2OIState + hltL3TkTracksFromL2OIState + hltL3NoFiltersMuonsOIState + hltL3NoFiltersTrajSeedOIHit + hltL3NoFiltersTrackCandidateFromL2OIHit + hltL3NoFiltersTkTracksFromL2OIHit + hltL3NoFiltersMuonsOIHit + hltL3NoFiltersTkFromL2OICombination + hltPixelLayerTriplets + hltPixelLayerPairs + hltMixedLayerPairs + hltL3NoFiltersTrajSeedIOHit + hltL3NoFiltersTrackCandidateFromL2IOHit + hltL3NoFiltersTkTracksFromL2IOHit + hltL3NoFiltersMuonsIOHit + hltL3NoFiltersTrajectorySeed + hltL3NoFiltersTrackCandidateFromL2 )
HLTL3NoFiltersmuonrecoNocandSequence = cms.Sequence( HLTL3NoFiltersmuonTkCandidateSequence + hltL3NoFiltersTkTracksMergeStep1 + hltL3NoFiltersTkTracksFromL2 + hltL3NoFiltersMuonsLinksCombination + hltL3NoFiltersMuons )
HLTL3NoFiltersmuonrecoSequence = cms.Sequence( HLTL3NoFiltersmuonrecoNocandSequence + hltL3NoFiltersMuonCandidates )
HLTL3muonTkCandidateSequence = cms.Sequence( HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltL3TrajSeedOIState + hltL3TrackCandidateFromL2OIState + hltL3TkTracksFromL2OIState + hltL3MuonsOIState + hltL3TrajSeedOIHit + hltL3TrackCandidateFromL2OIHit + hltL3TkTracksFromL2OIHit + hltL3MuonsOIHit + hltL3TkFromL2OICombination + hltPixelLayerTriplets + hltPixelLayerPairs + hltMixedLayerPairs + hltL3TrajSeedIOHit + hltL3TrackCandidateFromL2IOHit + hltL3TkTracksFromL2IOHit + hltL3MuonsIOHit + hltL3TrajectorySeed + hltL3TrackCandidateFromL2 )
HLTL3muonrecoNocandSequence = cms.Sequence( HLTL3muonTkCandidateSequence + hltL3TkTracksMergeStep1 + hltL3TkTracksFromL2 + hltL3MuonsLinksCombination + hltL3Muons )
HLTL3muonrecoSequence = cms.Sequence( HLTL3muonrecoNocandSequence + hltL3MuonCandidates )
HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence( hltEcalDigis + hltEcalPreshowerDigis + hltEcalUncalibRecHit + hltEcalDetIdToBeRecovered + hltEcalRecHit + hltEcalPreshowerRecHit )
HLTDoLocalHcalSequence = cms.Sequence( hltHcalDigis + hltHbhereco + hltHfreco + hltHoreco )
HLTL3muoncaloisorecoSequenceNoBools = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + HLTDoLocalHcalSequence + hltTowerMakerForAll + hltFixedGridRhoFastjetAllCaloForMuons + hltL3CaloMuonCorrectedIsolations )
HLTPixelTrackingL3MuonReg = cms.Sequence( hltL3MuonVertex + HLTDoLocalPixelSequence + hltPixelLayerTriplets + hltPixelTracksL3MuonReg + hltPixelVerticesL3MuonReg )
HLTTrackReconstructionForIsoL3MuonRegIter02 = cms.Sequence( HLTPixelTrackingL3MuonReg + HLTDoLocalStripSequence + HLTIterativeTrackingL3MuonRegIter02 + hltL3MuonCombRelIsolationsIterTrkRegIter02 )
HLTTrackerMuonSequence = cms.Sequence( HLTDoLocalPixelSequence + hltPixelLayerTriplets + hltPixelTracks + HLTDoLocalStripSequence + hltMuTrackSeeds + hltMuCkfTrackCandidates + hltMuCtfTracks + HLTL3muonrecoNocandSequence + hltDiMuonMerging + hltDiMuonLinks + hltGlbTrkMuons + hltGlbTrkMuonCands )
HLTL3muontrkisorecoSequence = cms.Sequence( HLTPixelTrackingL3MuonReg + HLTDoLocalStripSequence + HLTIterativeTrackingL3MuonRegIter02 )
HLTL3muontrkisovvlSequence = cms.Sequence( HLTL3muontrkisorecoSequence + hltL3MuonRelTrkIsolationVVL )
HLTPixelTrackingGlbTrkMuonReg = cms.Sequence( hltGlbTrkMuonVertex + HLTDoLocalPixelSequence + hltPixelLayerTriplets + hltPixelTracksGlbTrkMuonReg + hltPixelVerticesGlbTrkMuonReg )
HLTglbtrkmuontrkisorecoSequence = cms.Sequence( HLTPixelTrackingGlbTrkMuonReg + HLTDoLocalStripSequence + HLTIterativeTrackingGlbTrkMuonReg )
HLTglbtrkmuontrkisovvlSequence = cms.Sequence( HLTglbtrkmuontrkisorecoSequence + hltGlbTrkMuonRelTrkIsolationVVL )
HLTPFClusteringForEgamma = cms.Sequence( hltRechitInRegionsECAL + hltRechitInRegionsES + hltParticleFlowRecHitECALL1Seeded + hltParticleFlowRecHitPSL1Seeded + hltParticleFlowClusterPSL1Seeded + hltParticleFlowClusterECALUncorrectedL1Seeded + hltParticleFlowClusterECALL1Seeded + hltParticleFlowSuperClusterECALL1Seeded )
HLTDoLocalHcalWithTowerSequence = cms.Sequence( hltHcalDigis + hltHbhereco + hltHfreco + hltHoreco + hltTowerMakerForAll )
HLTFastJetForEgamma = cms.Sequence( hltFixedGridRhoFastjetAllCaloForMuons )
HLTPFHcalClusteringForEgamma = cms.Sequence( hltRegionalTowerForEgamma + hltParticleFlowRecHitHCALForEgamma + hltParticleFlowClusterHCALForEgamma + hltParticleFlowClusterHFEMForEgamma + hltParticleFlowClusterHFHADForEgamma )
HLTRecopixelvertexingForElectronsSequence = cms.Sequence( hltPixelLayerTriplets + hltVertexFromElectronsProducer + hltPixelTracksForEgamma + hltPixelVerticesForEgamma )
HLTTrackReconstructionForIsoForElectrons = cms.Sequence( HLTDoLocalPixelSequence + HLTRecopixelvertexingForElectronsSequence + HLTDoLocalStripSequence + HLTIterativeTrackingForEgamma )
HLTEle27WP80Sequence = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgamma + hltEgammaCandidates + hltEGL1SingleEG20ORL1SingleEG22Filter + hltEG27EtFilter + hltEgammaClusterShape + hltEle27WP80ClusterShapeFilter + HLTDoLocalHcalWithTowerSequence + HLTFastJetForEgamma + hltEgammaHoverE + hltEle27WP80HEFilter + hltEgammaEcalPFClusterIso + hltEle27WP80EcalIsoFilter + HLTPFHcalClusteringForEgamma + hltEgammaHcalPFClusterIso + hltEle27WP80HcalIsoFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltMixedLayerPairs + hltEgammaElectronPixelSeeds + hltEle27WP80PixelMatchFilter + hltEgammaCkfTrackCandidates + hltEgammaCtfTracks + hltEgammaCtfBarrelTracks + hltEgammaCtfCleanTracks + hltEgammaCtfBarrelCleanMergedTracks + hltEgammaCtfBarrelORCleanElectrons + hltEle27WP80OneOEMinusOneOPFilter + hltEgammaBarrelORCleanDetaDphi + hltEle27WP80DetaFilter + hltEle27WP80DphiFilter + HLTTrackReconstructionForIsoForElectrons + hltEgammaEleTrackIso + hltEle27WP80TrackIsoFilter )
HLTGsfElectronSequence = cms.Sequence( hltEgammaCkfTrackCandidatesForGSF + hltEgammaGsfTracks + hltEgammaGsfElectrons + hltEgammaGsfTrackVars )
HLTEle27WP80GsfSequence = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgamma + hltEgammaCandidates + hltEGL1SingleEG20ORL1SingleEG22Filter + hltEG27EtFilter + hltEgammaClusterShape + hltEle27WP80ClusterShapeFilter + HLTDoLocalHcalWithTowerSequence + HLTFastJetForEgamma + hltEgammaHoverE + hltEle27WP80HEFilter + hltEgammaEcalPFClusterIso + hltEle27WP80EcalIsoFilter + HLTPFHcalClusteringForEgamma + hltEgammaHcalPFClusterIso + hltEle27WP80HcalIsoFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltMixedLayerPairs + hltEgammaElectronPixelSeeds + hltEle27WP80PixelMatchFilter + HLTGsfElectronSequence + hltEle27WP80GsfDetaFilter + hltEle27WP80GsfDphiFilter + HLTTrackReconstructionForIsoForElectrons + hltEgammaEleGsfTrackIso + hltEle27WP80GsfTrackIsoFilter )
HLTEle17Ele8Mass50Sequence = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgamma + hltEgammaCandidates + hltEGL1DoubleEG137Filter + hltEle17Ele8EtLeg1Filter + hltEle17Ele8EtLeg2Filter + hltEgammaClusterShape + hltEle17Ele8ClusterShapeLeg1Filter + hltEle17Ele8ClusterShapeLeg2Filter + HLTDoLocalHcalWithTowerSequence + HLTFastJetForEgamma + hltEgammaHoverE + hltEle17Ele8HELeg1Filter + hltEle17Ele8HELeg2Filter + hltEgammaEcalPFClusterIso + hltEle17Ele8EcalIsoLeg1Filter + hltEle17Ele8EcalIsoLeg2Filter + HLTPFHcalClusteringForEgamma + hltEgammaHcalPFClusterIso + hltEle17Ele8HcalIsoLeg1Filter + hltEle17Ele8HcalIsoLeg2Filter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltMixedLayerPairs + hltEgammaElectronPixelSeeds + hltEle17Ele8PixelMatchLeg1Filter + hltEle17Ele8PixelMatchLeg2Filter + hltEgammaCkfTrackCandidates + hltEgammaCtfTracks + hltPixelMatchElectrons + hltEle17Ele8OneOEMinusOneOPLeg1Filter + hltEle17Ele8OneOEMinusOneOPLeg2Filter + hltEgammaEle3HitDetaDphi + hltEle17Ele8DetaLeg1Filter + hltEle17Ele8DetaLeg2Filter + hltEle17Ele8DphiLeg1Filter + hltEle17Ele8DphiLeg2Filter + HLTTrackReconstructionForIsoForElectrons + hltEgammaEle3HitTrackIso + hltEle17Ele8TrackIsoLeg1Filter + hltEle17Ele8TrackIsoLeg2Filter + hltEle17Ele8MassFilter )
HLTEle17Ele8GsfSequence = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgamma + hltEgammaCandidates + hltEGL1DoubleEG137Filter + hltEle17Ele8EtLeg1Filter + hltEle17Ele8EtLeg2Filter + hltEgammaClusterShape + hltEle17Ele8ClusterShapeLeg1Filter + hltEle17Ele8ClusterShapeLeg2Filter + HLTDoLocalHcalWithTowerSequence + HLTFastJetForEgamma + hltEgammaHoverE + hltEle17Ele8HELeg1Filter + hltEle17Ele8HELeg2Filter + hltEgammaEcalPFClusterIso + hltEle17Ele8EcalIsoLeg1Filter + hltEle17Ele8EcalIsoLeg2Filter + HLTPFHcalClusteringForEgamma + hltEgammaHcalPFClusterIso + hltEle17Ele8HcalIsoLeg1Filter + hltEle17Ele8HcalIsoLeg2Filter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltMixedLayerPairs + hltEgammaElectronPixelSeeds + hltEle17Ele8PixelMatchLeg1Filter + hltEle17Ele8PixelMatchLeg2Filter + HLTGsfElectronSequence + hltEle17Ele8GsfDetaLeg1Filter + hltEle17Ele8GsfDetaLeg2Filter + hltEle17Ele8GsfDphiLeg1Filter + hltEle17Ele8GsfDphiLeg2Filter + HLTTrackReconstructionForIsoForElectrons + hltEgammaEleGsfTrackIso + hltEle17Ele8GsfTrackIsoLeg1Filter + hltEle17Ele8GsfTrackIsoLeg2Filter )
HLTPFClusteringForEgammaUnseeded = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + hltParticleFlowRecHitECALUnseeded + hltParticleFlowRecHitPSUnseeded + hltParticleFlowClusterPSUnseeded + hltParticleFlowClusterECALUncorrectedUnseeded + hltParticleFlowClusterECALUnseeded + hltParticleFlowSuperClusterECALUnseeded )
HLTElePixelMatchUnseededSequence = cms.Sequence( HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltMixedLayerPairs + hltEgammaElectronPixelSeedsUnseeded )
HLTGsfElectronUnseededSequence = cms.Sequence( hltEgammaCkfTrackCandidatesForGSFUnseeded + hltEgammaGsfTracksUnseeded + hltEgammaGsfElectronsUnseeded + hltEgammaGsfTrackVarsUnseeded )
HLTDoubleEle33CaloIdVLGsfTrkIdVLSequence = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgamma + hltEgammaCandidates + hltEGL1SingleEG22Filter + hltEG33EtFilter + HLTDoLocalHcalWithTowerSequence + HLTFastJetForEgamma + hltEgammaHoverE + hltEG33HEFilter + hltEgammaClusterShape + hltEG33CaloIdLClusterShapeFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltMixedLayerPairs + hltEgammaElectronPixelSeeds + hltEle33CaloIdLPixelMatchFilter + HLTPFClusteringForEgammaUnseeded + hltEgammaCandidatesUnseeded + hltEgammaCandidatesWrapperUnseeded + hltDiEG33EtUnseededFilter + hltEgammaHoverEUnseeded + hltDiEG33HEUnseededFilter + hltEgammaClusterShapeUnseeded + hltDiEG33CaloIdLClusterShapeUnseededFilter + HLTElePixelMatchUnseededSequence + hltDiEle33CaloIdLPixelMatchUnseededFilter + HLTGsfElectronUnseededSequence + hltDiEle33CaloIdLGsfTrkIdVLDEtaUnseededFilter + hltDiEle33CaloIdLGsfTrkIdVLDPhiUnseededFilter )
HLTRecopixelvertexingForPhotonsSequence = cms.Sequence( hltPixelLayerTriplets + hltPixelTracksForPhotons + hltPixelVerticesForPhotons )
HLTTrackReconstructionForIsoForPhotons = cms.Sequence( HLTDoLocalPixelSequence + HLTRecopixelvertexingForPhotonsSequence + HLTDoLocalStripSequence + HLTIterativeTrackingForPhotons )
HLTPhoton20CaloIdVLIsoLSequence = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgamma + hltEgammaCandidates + hltEGL1SingleEG12Filter + hltEG20EtFilter + hltEgammaClusterShape + hltEG20CaloIdVLClusterShapeFilter + HLTDoLocalHcalWithTowerSequence + HLTFastJetForEgamma + hltEgammaHoverE + hltEG20CaloIdVLHEFilter + hltEgammaEcalPFClusterIso + hltEG20CaloIdVLIsoLEcalIsoFilter + HLTPFHcalClusteringForEgamma + hltEgammaHcalPFClusterIso + hltEG20CaloIdVLIsoLHcalIsoFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + HLTTrackReconstructionForIsoForPhotons + hltEgammaHollowTrackIso + hltEG20CaloIdVLIsoLTrackIsoFilter )
HLTPFHcalClusteringForEgammaUnseeded = cms.Sequence( hltParticleFlowRecHitHCALForEgammaUnseeded + hltParticleFlowClusterHCALForEgammaUnseeded + hltParticleFlowClusterHFEMForEgammaUnseeded + hltParticleFlowClusterHFHADForEgammaUnseeded )
HLTPhoton26R9Id85Photon18CaloId10Iso50Sequence = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgamma + hltEgammaCandidates + hltEGL1SingleEG22Filter + hltEG26EtFilter + HLTDoLocalHcalWithTowerSequence + HLTFastJetForEgamma + hltEgammaHoverE + hltEG26HE10HEFilter + hltEgammaR9ID + hltEG26R9Id85R9Filter + HLTPFClusteringForEgammaUnseeded + hltEgammaCandidatesUnseeded + hltEgammaCandidatesWrapperUnseeded + hltDiEG18EtUnseededFilter + hltEgammaHoverEUnseeded + hltDiEG18HE10HEUnseededFilter + hltEgammaR9IDUnseeded + hltEG18R9Id85R9UnseededFilter + hltEgammaClusterShapeUnseeded + hltEG18CaloId10ClusterShapeUnseededFilter + hltEgammaEcalPFClusterIsoUnseeded + hltEG18CaloId10Iso50EcalIsoUnseededFilter + HLTPFHcalClusteringForEgammaUnseeded + hltEgammaHcalPFClusterIsoUnseeded + hltEG18CaloId10Iso50HcalIsoUnseededFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + HLTTrackReconstructionForIsoForPhotons + hltEgammaHollowTrackIsoUnseeded + hltEG18CaloId10Iso50TrackIsoUnseededFilter + hltEG26R9Id85EG18CaloId10Iso50LegCombFilter )
HLTL3muonisorecoSequence = cms.Sequence( HLTDoLocalPixelSequence + HLTDoLocalStripSequence + HLTRegionalCKFTracksForL3Isolation + hltL3MuonCombRelIsolations )
HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence( hltEcalDigis + hltEcalUncalibRecHit + hltEcalDetIdToBeRecovered + hltEcalRecHit )
HLTDoCaloSequencePF = cms.Sequence( HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + HLTDoLocalHcalSequence + hltTowerMakerForPF )
HLTRecoJetSequenceAK4UncorrectedPF = cms.Sequence( HLTDoCaloSequencePF + hltAntiKT4CaloJetsPF )
HLTRecoJetSequenceAK4PrePF = cms.Sequence( HLTRecoJetSequenceAK4UncorrectedPF + hltAntiKT4CaloJetsPFEt5 )
HLTTrackReconstructionForPF = cms.Sequence( HLTDoLocalPixelSequence + HLTRecopixelvertexingSequence + HLTDoLocalStripSequence + HLTIterativeTracking + hltPFMuonMerging + hltMuonLinks + hltMuons )
HLTPreshowerSequence = cms.Sequence( hltEcalPreshowerDigis + hltEcalPreshowerRecHit )
HLTParticleFlowSequenceForTaus = cms.Sequence( HLTPreshowerSequence + hltParticleFlowRecHitECAL + hltParticleFlowRecHitHCAL + hltParticleFlowRecHitPS + hltParticleFlowClusterECALUncorrected + hltParticleFlowClusterPS + hltParticleFlowClusterECAL + hltParticleFlowClusterHCAL + hltParticleFlowClusterHFEM + hltParticleFlowClusterHFHAD + hltLightPFTracks + hltParticleFlowBlockForTaus + hltParticleFlowForTaus )
HLTPFTriggerSequenceMuTau = cms.Sequence( HLTTrackReconstructionForPF + HLTParticleFlowSequenceForTaus + hltAntiKT4PFJetsForTaus )
HLTLooseIsoPFTauSequenceFor2015 = cms.Sequence( hltTauPFJets08Region + hltTauPFJetsRecoTauChargedHadrons + hltPFTauPiZeros + hltPFTausSansRefFor2015 + hltPFTausFor2015 + hltPFTauTrackFindingDiscriminatorFor2015 + hltPFTauLooseAbsoluteIsolationDiscriminatorFor2015 + hltPFTauLooseRelativeIsolationDiscriminatorFor2015 )
HLTIsoMuLooseIsoPFTauSequenceFor2015 = cms.Sequence( HLTLooseIsoPFTauSequenceFor2015 + hltPFTau20For2015 + hltSelectedPFTausTrackFindingFor2015 + hltPFTau20TrackFor2015 + hltSelectedPFTausTrackFindingLooseIsolationFor2015 + hltPFTau20TrackLooseIsoFor2015 + hltPFTauAgainstMuonDiscriminatorFor2015 + hltSelectedPFTausTrackFindingLooseIsolationAgainstMuonFor2015 + hltPFTau20TrackLooseIsoAgainstMuonFor2015 + hltOverlapFilterIsoMu17LooseIsoPFTau20For2015 )
HLTMulti5x5SuperClusterL1Seeded = cms.Sequence( hltMulti5x5BasicClustersL1Seeded + hltMulti5x5SuperClustersL1Seeded + hltMulti5x5EndcapSuperClustersWithPreshowerL1Seeded + hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Seeded )
HLTL1SeededEcalClustersSequence = cms.Sequence( hltHybridSuperClustersL1Seeded + hltCorrectedHybridSuperClustersL1Seeded + HLTMulti5x5SuperClusterL1Seeded )
HLTDoCaloSequence = cms.Sequence( HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + HLTDoLocalHcalSequence + hltTowerMakerForAll )
HLTRecoJetSequenceAK4L1FastJetCorrected = cms.Sequence( HLTDoCaloSequence + hltFixedGridRhoFastjetAllCalo + hltAntiKT4CaloJets + hltCaloJetIDPassed + hltCaloJetL1FastJetCorrected )
HLTFastJetSequenceForEgamma = cms.Sequence( HLTRecoJetSequenceAK4L1FastJetCorrected )
HLTPixelMatchElectronL1TrackingSequence = cms.Sequence( hltCkfL1SeededTrackCandidates + hltCtfL1SeededWithMaterialTracks + hltPixelMatchElectronsL1Seeded )
HLTEle22WP90RhoSequence = cms.Sequence( HLTDoFullUnpackingEgammaEcalSequence + HLTL1SeededEcalClustersSequence + hltL1SeededRecoEcalCandidate + hltEGRegionalL1SingleIsoEG18erORIsoEG20erOREG22 + hltEG22L1sIso18erOrIso20erOr22EtFilter + hltL1SeededHLTClusterShape + hltEle22WP90RhoClusterShapeFilter + HLTFastJetSequenceForEgamma + hltL1SeededPhotonEcalIsoRhoCorr + hltEle22WP90RhoEcalIsoFilter + HLTDoLocalHcalWithTowerSequence + hltL1SeededPhotonHcalForHE + hltEle22WP90RhoHEFilter + hltL1SeededPhotonHcalIsoRhoCorr + hltEle22WP90RhoHcalIsoFilter + HLTDoLocalPixelSequence + HLTDoLocalStripSequence + hltMixedLayerPairs + hltL1SeededStartUpElectronPixelSeeds + hltEle22WP90RhoPixelMatchFilter + HLTPixelMatchElectronL1TrackingSequence + hltEle22WP90RhoOneOEMinusOneOPFilter + hltElectronL1SeededDetaDphi + hltEle22WP90RhoDetaFilter + hltEle22WP90RhoDphiFilter + HLTL1SeededEgammaRegionalRecoTrackerSequence + hltL1SeededElectronTrackIso + hltEle22WP90RhoTrackIsoFilter )
HLTPFTriggerSequenceForTaus = cms.Sequence( HLTL2muonrecoSequence + HLTL3muonrecoSequence + HLTTrackReconstructionForPF + HLTParticleFlowSequenceForTaus + hltAntiKT4PFJetsForTaus )
HLTIsoEleLooseIsoPFTauSequenceFor2015 = cms.Sequence( HLTLooseIsoPFTauSequenceFor2015 + hltPFTau20For2015 + hltSelectedPFTausTrackFindingFor2015 + hltPFTau20TrackFor2015 + hltSelectedPFTausTrackFindingLooseIsolationFor2015 + hltPFTau20TrackLooseIsoFor2015 + hltOverlapFilterIsoEle20WP90LooseIsoPFTau20For2015 )
HLTCaloTausCreatorRegionalSequence = cms.Sequence( HLTDoCaloSequence + hltCaloTowersTau1Regional + hltIconeTau1Regional + hltCaloTowersTau2Regional + hltIconeTau2Regional + hltCaloTowersTau3Regional + hltIconeTau3Regional + hltCaloTowersTau4Regional + hltIconeTau4Regional + hltCaloTowersCentral1Regional + hltIconeCentral1Regional + hltCaloTowersCentral2Regional + hltIconeCentral2Regional + hltCaloTowersCentral3Regional + hltIconeCentral3Regional + hltCaloTowersCentral4Regional + hltIconeCentral4Regional )
HLTL2TauJetsSequence = cms.Sequence( HLTCaloTausCreatorRegionalSequence + hltL2TauJets )
HLTPixelTrackingSequenceRegL2Tau = cms.Sequence( HLTDoLocalPixelSequenceRegL2Tau + hltPixelLayerTripletsReg + hltPixelTracksReg + hltPixelVerticesReg )
HLTL2TauPixelIsolationSequence = cms.Sequence( hltL2Tau25eta2p1 + hltL2TausForPixelIsolation + HLTPixelTrackingSequenceRegL2Tau + hltL2TauPixelIsoTagProducer )
HLTPFReconstructionSequenceForTaus = cms.Sequence( HLTRecoJetSequenceAK4PrePF + HLTPFTriggerSequenceForTaus )
HLTMediumIsoPFTauSequenceFor2015 = cms.Sequence( hltTauPFJets08Region + hltTauPFJetsRecoTauChargedHadrons + hltPFTauPiZeros + hltPFTausSansRefFor2015 + hltPFTausFor2015 + hltPFTauTrackFindingDiscriminatorFor2015 + hltPFTauMediumAbsoluteIsolationDiscriminatorFor2015 )
HLTRecoMETSequence = cms.Sequence( HLTDoCaloSequence + hltMet )
HLTParticleFlowSequence = cms.Sequence( HLTPreshowerSequence + hltParticleFlowRecHitECALUnseeded + hltParticleFlowRecHitHCAL + hltParticleFlowRecHitPSUnseeded + hltParticleFlowClusterECALUncorrectedUnseeded + hltParticleFlowClusterPSUnseeded + hltParticleFlowClusterECALUnseeded + hltParticleFlowClusterHCAL + hltParticleFlowClusterHFEM + hltParticleFlowClusterHFHAD + hltLightPFTracks + hltParticleFlowBlock + hltParticleFlow )
HLTPFL1FastL2L3JetsSequence = cms.Sequence( hltFixedGridRhoFastjetAll + hltAntiKT4PFJets + hltAK4PFJetL1FastL2L3Corrected )
HLTPFL1FastL2L3JetTriggerSequence = cms.Sequence( HLTL2muonrecoSequence + HLTL3muonrecoSequence + HLTTrackReconstructionForPF + HLTParticleFlowSequence + HLTPFL1FastL2L3JetsSequence )
HLTPFL1FastL2L3ReconstructionSequence = cms.Sequence( HLTRecoJetSequenceAK4PrePF + HLTPFL1FastL2L3JetTriggerSequence )
HLTPFJetRecoNoPUL1FastL2L3Sequence = cms.Sequence( hltOnlinePrimaryVertices + hltGoodOnlinePVs + hltParticleFlowPtrs + hltPFPileUp + hltPFNoPileUp + hltFixedGridRhoFastjetAll + hltAntiKT4PFJetsNoPU + hltAK4PFJetL1FastL2L3CorrectedNoPU )
HLTPFnoPUL1FastL2L3JetTriggerSequence = cms.Sequence( HLTL2muonrecoSequence + HLTL3muonrecoSequence + HLTTrackReconstructionForPF + HLTParticleFlowSequence + HLTPFJetRecoNoPUL1FastL2L3Sequence )
HLTPFnoPUL1FastL2L3ReconstructionSequence = cms.Sequence( HLTRecoJetSequenceAK4PrePF + HLTPFnoPUL1FastL2L3JetTriggerSequence )
HLTFastRecopixelvertexingSequence = cms.Sequence( hltFastPrimaryVertex + hltFastPVPixelVertexFilter + hltFastPVPixelTracks + hltFastPVJetTracksAssociator + hltFastPVJetVertexChecker + hltFastPVPixelTracksRecover + hltFastPVPixelTracksMerger + hltFastPVPixelVertices )
HLTFastPrimaryVertexSequence = cms.Sequence( hltSelectorCentralJets20L1FastJet + hltSelector4CentralJetsL1FastJet + HLTDoLocalPixelSequenceRegForBTag + HLTFastRecopixelvertexingSequence )
HLTBtagCSVSequenceL3 = cms.Sequence( HLTDoLocalPixelSequenceRegForBTag + HLTDoLocalStripSequenceRegForBTag + HLTForBTagIterativeTracking + hltVerticesL3 + hltFastPixelBLifetimeL3Associator + hltFastPixelBLifetimeL3TagInfos + hltL3SecondaryVertexTagInfos + hltL3CombinedSecondaryVertexBJetTags )

HLTriggerFirstPath = cms.Path( hltGetConditions + hltGetRaw + hltBoolFalse )
HLT_Mu17_NoFilters_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleMu12 + hltPreMu17NoFilters + hltL1fL1sMu12L1Filtered0 + HLTL2muonrecoSequence + hltL2fL1sMu12L2Filtered12 + HLTL3NoFiltersmuonrecoSequence + hltL3NoFiltersfL1sMu12L3Filtered17 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu40_v1 = cms.Path( HLTBeginSequence + hltL1sMu16 + hltPreMu40 + hltL1fL1sMu16L1Filtered0 + HLTL2muonrecoSequence + hltL2fL1sMu16L1f0L2Filtered16Q + HLTL3muonrecoSequence + hltL3fL1sMu16L1f0L2f16QL3Filtered40Q + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_IsoMu24_IterTrk02_v1 = cms.Path( HLTBeginSequence + hltL1sMu16 + hltPreIsoMu24IterTrk02 + hltL1fL1sMu16L1Filtered0 + HLTL2muonrecoSequence + hltL2fL1sMu16L1f0L2Filtered16Q + HLTL3muonrecoSequence + hltL3fL1sMu16L1f0L2f16QL3Filtered24Q + HLTL3muoncaloisorecoSequenceNoBools + HLTTrackReconstructionForIsoL3MuonRegIter02 + hltL3crIsoL1sMu16L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15IterTrk02 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleMu4NoFilters_Jpsi_Displaced_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleMu33HighQ + hltPreDoubleMu4NoFiltersJpsiDisplaced + hltDimuon33L1Filtered0 + HLTL2muonrecoSequence + hltDimuon33L2PreFiltered0 + HLTL3NoFiltersmuonrecoSequence + hltDoubleMu4NoFiltersJpsiDisplacedL3Filtered + hltDisplacedmumuVtxProducerDoubleMu4NoFiltersJpsi + hltDisplacedmumuFilterDoubleMu4NoFiltersJpsi + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu17_Mu8_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleMu10MuOpenORDoubleMu103p5 + hltPreMu17Mu8 + hltL1DoubleMu10MuOpenOR3p5L1Filtered0 + HLTL2muonrecoSequence + hltL2pfL1DoubleMu10MuOpenOR3p5L1f0L2PreFiltered0 + hltL2fL1DoubleMu10MuOpenOR3p5L1f0L2Filtered10 + HLTL3muonrecoSequence + hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8 + hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17 + hltDiMuonGlb17Glb8DzFiltered0p2 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu17_TkMu8_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleMu10MuOpenORDoubleMu103p5 + hltPreMu17TkMu8 + hltL1fL1sDoubleMu10MuOpenOR3p5L1Filtered0 + HLTL2muonrecoSequence + hltL2fL1sDoubleMu10MuOpenOR3p5L1f0L2Filtered10 + HLTL3muonrecoSequence + hltL3fL1sMu10MuOpenOR3p5L1f0L2f10L3Filtered17 + HLTTrackerMuonSequence + hltDiMuonGlbFiltered17TrkFiltered8 + hltDiMuonGlb17Trk8DzFiltered0p2 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleMu10MuOpenORDoubleMu103p5 + hltPreMu17TrkIsoVVLMu8TrkIsoVVL + hltL1DoubleMu10MuOpenOR3p5L1Filtered0 + HLTL2muonrecoSequence + hltL2pfL1DoubleMu10MuOpenOR3p5L1f0L2PreFiltered0 + hltL2fL1DoubleMu10MuOpenOR3p5L1f0L2Filtered10 + HLTL3muonrecoSequence + hltL3pfL1DoubleMu10MuOpenOR3p5L1f0L2pf0L3PreFiltered8 + hltL3fL1DoubleMu10MuOpenOR3p5L1f0L2f10L3Filtered17 + hltDiMuonGlb17Glb8DzFiltered0p2 + HLTL3muontrkisovvlSequence + hltDiMuonGlb17Glb8DzFiltered0p2RelTrkIsoFiltered0p4 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleMu10MuOpenORDoubleMu103p5 + hltPreMu17TrkIsoVVLTkMu8TrkIsoVVL + hltL1fL1sDoubleMu10MuOpenOR3p5L1Filtered0 + HLTL2muonrecoSequence + hltL2fL1sDoubleMu10MuOpenOR3p5L1f0L2Filtered10 + HLTL3muonrecoSequence + hltL3fL1sMu10MuOpenOR3p5L1f0L2f10L3Filtered17 + HLTTrackerMuonSequence + hltDiMuonGlbFiltered17TrkFiltered8 + hltDiMuonGlb17Trk8DzFiltered0p2 + HLTglbtrkmuontrkisovvlSequence + hltDiMuonGlb17Trk8DzFiltered0p2RelTrkIsoFiltered0p4 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele27_WP80_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG20ORL1SingleEG22 + hltPreEle27WP80 + HLTEle27WP80Sequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele27_WP80_Gsf_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG20ORL1SingleEG22 + hltPreEle27WP80Gsf + HLTEle27WP80GsfSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele17_Ele8_Mass50_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleEG137 + hltPreEle17Ele8Mass50 + HLTEle17Ele8Mass50Sequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele17_Ele8_Gsf_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleEG137 + hltPreEle17Ele8Gsf + HLTEle17Ele8GsfSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG22 + hltPreDoubleEle33CaloIdLGsfTrkIdVL + HLTDoubleEle33CaloIdVLGsfTrkIdVLSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon20_CaloIdVL_IsoL_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG12 + hltPrePhoton20CaloIdVLIsoL + HLTPhoton20CaloIdVLIsoLSequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Photon26_R9Id85_Photon18_CaloId10_Iso50_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleEG22 + hltPrePhoton26R9Id85Photon18CaloId10Iso50 + HLTPhoton26R9Id85Photon18CaloId10Iso50Sequence + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1 = cms.Path( HLTBeginSequence + hltL1sMu14erORMu16er + hltPreIsoMu17eta2p1LooseIsoPFTau20 + hltL1fL1sMu14erORMu16erL1Filtered0 + HLTL2muonrecoSequence + hltL2fL1sMu14erORMu16erL1f0L2Filtered14Q + HLTL3muonrecoSequence + hltL3fL1sMu14erORMu16erL1f0L2f14QL3Filtered17Q + HLTL3muoncaloisorecoSequenceNoBools + HLTL3muonisorecoSequence + hltL3crIsoL1sMu14erORMu16erL1f0L2f14QL3f17QL3crIsoRhoFiltered0p15 + HLTRecoJetSequenceAK4PrePF + hltTauJet5 + HLTPFTriggerSequenceMuTau + HLTIsoMuLooseIsoPFTauSequenceFor2015 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v1 = cms.Path( HLTBeginSequence + hltL1sL1SingleIsoEG18erORIsoEG20erOREG22 + hltPreEle22eta2p1WP90RhoLooseIsoPFTau20 + HLTEle22WP90RhoSequence + HLTRecoJetSequenceAK4PrePF + hltTauJet5 + hltOverlapFilterIsoEle20CaloJet5 + HLTPFTriggerSequenceForTaus + HLTIsoEleLooseIsoPFTauSequenceFor2015 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v1 = cms.Path( HLTBeginSequence + hltL1sDoubleTauJet44erorDoubleJetC64 + hltPreDoubleMediumIsoPFTau35Trk1eta2p1Prong1 + HLTL2TauJetsSequence + hltDoubleL2Tau35eta2p1 + HLTL2TauPixelIsolationSequence + hltL2DiTauIsoFilter + hltL2TauJetsIso + hltDoubleL2IsoTau35eta2p1 + HLTPFReconstructionSequenceForTaus + HLTMediumIsoPFTauSequenceFor2015 + hltDoublePFTau35For2015 + hltPFTauTrackPt1DiscriminatorFor2015 + hltSelectedPFTausTrackPt1For2015 + hltDoublePFTau35TrackPt1For2015 + hltSelectedPFTausTrackPt1MediumIsolationFor2015 + hltDoublePFTau35TrackPt1MediumIsolationFor2015 + hltSelectedPFTausTrackPt1MediumIsolationProng2For2015 + hltDoublePFTau35TrackPt1MediumIsolationProng2For2015 + hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationProng2MatchFor2015 + hltDoublePFTau35TrackPt1MediumIsolationProng2L1HLTMatchedFor2015 + hltDoublePFTau35TrackPt1MediumIsolationProng2Dz02For2015 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v1 = cms.Path( HLTBeginSequence + hltL1sDoubleTauJet44erorDoubleJetC64 + hltPreDoubleMediumIsoPFTau35Trk1eta2p1 + HLTL2TauJetsSequence + hltDoubleL2Tau35eta2p1 + HLTL2TauPixelIsolationSequence + hltL2DiTauIsoFilter + hltL2TauJetsIso + hltDoubleL2IsoTau35eta2p1 + HLTPFReconstructionSequenceForTaus + HLTMediumIsoPFTauSequenceFor2015 + hltDoublePFTau35For2015 + hltPFTauTrackPt1DiscriminatorFor2015 + hltSelectedPFTausTrackPt1For2015 + hltDoublePFTau35TrackPt1For2015 + hltSelectedPFTausTrackPt1MediumIsolationFor2015 + hltDoublePFTau35TrackPt1MediumIsolationFor2015 + hltL1JetsHLTDoublePFTauTrackPt1MediumIsolationMatchFor2015 + hltDoublePFTau35TrackPt1MediumIsolationL1HLTMatchedFor2015 + hltDoublePFTau35TrackPt1MediumIsolationDz02For2015 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v1 = cms.Path( HLTBeginSequence + hltL1sL1ETM36or40 + hltPreLooseIsoPFTau35Trk20Prong1MET70 + HLTL2TauJetsSequence + hltFilterL2EtCutSingleIsoPFTau35Trk20 + HLTRecoMETSequence + hltMET70 + HLTPFReconstructionSequenceForTaus + HLTLooseIsoPFTauSequenceFor2015 + hltPFTau35For2015 + hltSelectedPFTausTrackFindingFor2015 + hltPFTau35TrackFor2015 + hltPFTauTrackPt20DiscriminatorFor2015 + hltSelectedPFTausTrackPt20For2015 + hltPFTau35TrackPt20For2015 + hltSelectedPFTausTrackPt20IsolationFor2015 + hltPFTau35TrackPt20LooseIsoFor2015 + hltSelectedPFTausTrackPt20IsolationProng2For2015 + hltPFTau35TrackPt20LooseIsoProng2For2015 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_PFMET150_NoiseCleaned_v1 = cms.Path( HLTBeginSequence + hltL1sL1ETM36ORETM40 + hltPrePFMET150NoiseCleaned + HLTRecoMETSequence + hltMET90 + HLTHBHENoiseCleanerSequence + hltMetClean + hltMETClean80 + HLTRecoJetSequenceAK4L1FastJetCorrected + hltMetCleanUsingJetID + hltMETCleanUsingJetID80 + HLTPFL1FastL2L3ReconstructionSequence + hltPFMETProducer + hltPFMET150Filter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_PFMET180_NoiseCleaned_v1 = cms.Path( HLTBeginSequence + hltL1sL1ETM36ORETM40 + hltPrePFMET180NoiseCleaned + HLTRecoMETSequence + hltMET90 + HLTHBHENoiseCleanerSequence + hltMetClean + hltMETClean80 + HLTRecoJetSequenceAK4L1FastJetCorrected + hltMetCleanUsingJetID + hltMETCleanUsingJetID80 + HLTPFL1FastL2L3ReconstructionSequence + hltPFMETProducer + hltPFMET180Filter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_MonoCentralPFNoPUJet100_PFMET100_NHF0p95_NCH1_v1 = cms.Path( HLTBeginSequence + hltL1sL1ETM36ORETM40 + hltPreMonoCentralPFNoPUJet100PFMET100NHF0p95NCH1 + HLTRecoMETSequence + hltMET70 + HLTHBHENoiseCleanerSequence + hltMetClean + hltMETClean60 + HLTRecoJetSequenceAK4L1FastJetCorrected + hltCentralJet85L1FastJetCorrected + HLTPFL1FastL2L3ReconstructionSequence + hltPFMETProducer + hltPFMETNoMuProducer + hltPFMETorPFMETNoMu100 + hltAK4PFJetIDPassedL1FastL2L3Corrected + hltCentralPFJetIDPassed85 + HLTPFnoPUL1FastL2L3ReconstructionSequence + hltCentralPFJet100NoPU + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiCentralPFNoPUJet60_30_PFMET100_dphi0p5_v1 = cms.Path( HLTBeginSequence + hltL1sL1ETM36ORETM40 + hltPreDiCentralPFNoPUJet6030PFMET100dphi0p5 + HLTRecoMETSequence + hltMET70 + HLTHBHENoiseCleanerSequence + hltMetClean + hltMETClean60 + HLTRecoJetSequenceAK4L1FastJetCorrected + hltCentralJet40L1FastJetCorrected + hltDiCentralJet20L1FastJetCorrected + HLTPFL1FastL2L3ReconstructionSequence + hltPFMETProducer + hltPFMETNoMuProducer + hltPFMETorPFMETNoMu100 + hltMinDPhiMET0p5Filter + HLTPFnoPUL1FastL2L3ReconstructionSequence + hltCentralPFJet60NoPU + hltDiCentralPFJet30NoPUer2p6 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiCentralPFNoPUJet60_PFMET80_dphi0p3_v1 = cms.Path( HLTBeginSequence + hltL1sL1DoubleJetC36ETM30ORL1DoubleJetC44ETM30 + hltPreDiCentralPFNoPUJet60PFMET80dphi0p3 + HLTRecoMETSequence + hltMET65 + HLTHBHENoiseCleanerSequence + hltMetClean + hltMETClean55 + HLTRecoJetSequenceAK4L1FastJetCorrected + hltDiCentralJet40L1FastJetCorrected + HLTPFL1FastL2L3ReconstructionSequence + hltPFMETProducer + hltPFMETNoMuProducer + hltPFMETorPFMETNoMu80 + hltMinDPhiMET0p3Filter + HLTPFnoPUL1FastL2L3ReconstructionSequence + hltDiCentralPFJet60NoPUer2p6 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiCentralPFNoPUJet30_PFMET80_BTagCSV07_v1 = cms.Path( HLTBeginSequence + hltL1sL1ETM36ORETM40 + hltPreDiCentralPFNoPUJet30PFMET80BTagCSV07 + HLTRecoMETSequence + hltMET65 + HLTHBHENoiseCleanerSequence + hltMetClean + hltMETClean55 + HLTRecoJetSequenceAK4L1FastJetCorrected + hltDiCentralJet20L1FastJetCorrected + HLTFastPrimaryVertexSequence + hltFastPVPixelVertexSelector + HLTBtagCSVSequenceL3 + hltBLifetimeL3FilterCSV + HLTPFL1FastL2L3ReconstructionSequence + hltPFMETProducer + hltPFMET80Filter + HLTPFnoPUL1FastL2L3ReconstructionSequence + hltDiCentralPFJet30NoPUer2p6 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_DiCentralPFNoPUJet30_PFMET80_v1 = cms.Path( HLTBeginSequence + hltL1sL1ETM36ORETM40 + hltPreDiCentralPFNoPUJet30PFMET80 + HLTRecoMETSequence + hltMET65 + HLTHBHENoiseCleanerSequence + hltMetClean + hltMETClean55 + HLTRecoJetSequenceAK4L1FastJetCorrected + hltDiCentralJet20L1FastJetCorrected + HLTPFL1FastL2L3ReconstructionSequence + hltPFMETProducer + hltPFMET80Filter + HLTPFnoPUL1FastL2L3ReconstructionSequence + hltDiCentralPFJet30NoPUer2p6 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_PFNoPUHT400_DiCentralPFNoPUJet40_PFMET80_v1 = cms.Path( HLTBeginSequence + hltL1sL1HTT150OrHTT175 + hltPrePFNoPUHT400DiCentralPFNoPUJet40PFMET80 + HLTRecoMETSequence + hltMET65 + HLTHBHENoiseCleanerSequence + hltMetClean + hltMETClean55 + HLTRecoJetSequenceAK4L1FastJetCorrected + hltHtMht + hltHt350 + hltDiCentralJet20L1FastJetCorrected + HLTPFL1FastL2L3ReconstructionSequence + hltPFMETProducer + hltPFMET80Filter + HLTPFnoPUL1FastL2L3ReconstructionSequence + hltPFHTNoPU + hltPFHT400NoPU + hltDiCentralPFJet40NoPUer2p6 + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_PFchMET90_NoiseCleaned_v1 = cms.Path( HLTBeginSequence + hltL1sL1ETM36ORETM40 + hltPrePFchMET90NoiseCleaned + HLTRecoMETSequence + hltMET90 + HLTHBHENoiseCleanerSequence + hltMetClean + hltMETClean80 + HLTRecoJetSequenceAK4L1FastJetCorrected + hltMetCleanUsingJetID + hltMETCleanUsingJetID80 + HLTPFL1FastL2L3ReconstructionSequence + hltPFchMETProducer + hltPFchMET90Filter + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLT_BTagCSV07_v0 = cms.Path( HLTBeginSequence + hltPreBTagCSV07 + HLTRecoJetSequenceAK4L1FastJetCorrected + HLTFastPrimaryVertexSequence + hltFastPVPixelVertexSelector + HLTBtagCSVSequenceL3 + hltBLifetimeL3FilterCSV + cms.SequencePlaceholder( "HLTEndSequence" ) )
HLTriggerFinalPath = cms.Path( HLTBeginSequence + hltScalersRawToDigi + hltFEDSelector + hltTriggerSummaryAOD + hltTriggerSummaryRAW )


HLTSchedule = cms.Schedule( *(HLTriggerFirstPath, HLT_Mu17_NoFilters_v1, HLT_Mu40_v1, HLT_IsoMu24_IterTrk02_v1, HLT_DoubleMu4NoFilters_Jpsi_Displaced_v1, HLT_Mu17_Mu8_v1, HLT_Mu17_TkMu8_v1, HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1, HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1, HLT_Ele27_WP80_v1, HLT_Ele27_WP80_Gsf_v1, HLT_Ele17_Ele8_Mass50_v1, HLT_Ele17_Ele8_Gsf_v1, HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1, HLT_Photon20_CaloIdVL_IsoL_v1, HLT_Photon26_R9Id85_Photon18_CaloId10_Iso50_v1, HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1, HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v1, HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v1, HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_v1, HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v1, HLT_PFMET150_NoiseCleaned_v1, HLT_PFMET180_NoiseCleaned_v1, HLT_MonoCentralPFNoPUJet100_PFMET100_NHF0p95_NCH1_v1, HLT_DiCentralPFNoPUJet60_30_PFMET100_dphi0p5_v1, HLT_DiCentralPFNoPUJet60_PFMET80_dphi0p3_v1, HLT_DiCentralPFNoPUJet30_PFMET80_BTagCSV07_v1, HLT_DiCentralPFNoPUJet30_PFMET80_v1, HLT_PFNoPUHT400_DiCentralPFNoPUJet40_PFMET80_v1, HLT_PFchMET90_NoiseCleaned_v1, HLT_BTagCSV07_v0, HLTriggerFinalPath ))

# Enable HF Noise filters in GRun menu
if 'hltHfreco' in locals():
    hltHfreco.setNoiseFlags = cms.bool( True )

# CMSSW version specific customizations
import os
cmsswVersion = os.environ['CMSSW_VERSION']

# customization for 6_2_X

# none for now


