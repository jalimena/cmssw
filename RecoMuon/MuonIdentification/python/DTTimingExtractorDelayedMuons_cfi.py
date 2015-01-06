import FWCore.ParameterSet.Config as cms

from RecoMuon.TrackingTools.MuonSegmentMatcher_cff import *

DTTimingExtractorBlock = cms.PSet(
  DTTimingParameters = cms.PSet(
    MuonSegmentMatcher,
    ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny', 
            'PropagatorWithMaterial', 
            'PropagatorWithMaterialOpposite'),
        RPCLayers = cms.bool(True)
    ),
    DTsegments = cms.InputTag("dt4DSegments"),
    #DTsegments = cms.InputTag("dt4DSegmentsMT"),
    PruneCut = cms.double(10000.),
    #PruneCut = cms.double(20.),
    #PruneCut = cms.double(10.),
    #PruneCut = cms.double(5.),
    #PruneCut = cms.double(2.),    
    DTTimeOffset = cms.double(0.),
    #HitError  = cms.double(6.0),
    HitErrorPhi  = cms.double(3.0),
    HitErrorTheta  = cms.double(6.0),
    HitsMin = cms.int32(3),
    UseSegmentT0 = cms.bool(False),
    DoWireCorr = cms.bool(True),
    DropTheta = cms.bool(True),
    #DropTheta = cms.bool(False),
    RequireBothProjections = cms.bool(False),
    #debug = cms.bool(False),
    debug = cms.bool(True),
  )
)


