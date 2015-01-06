import FWCore.ParameterSet.Config as cms

from RecoMuon.MuonIdentification.MuonTimingFillerDelayedMuons_cfi import *

muontimingDelayedMuons = cms.EDProducer('MuonTimingProducerDelayedMuons',
  TimingFillerBlock,
  MuonCollection = cms.InputTag("muons"),
)
