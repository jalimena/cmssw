import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.NoBPTXMonitor_cfi import hltNoBPTXmonitoring

hltNoBPTXMuonsMonitoring = hltNoBPTXmonitoring.clone()
hltNoBPTXMuonsMonitoring.FolderName = cms.string('HLT/NoBPTX/Muons/')
hltNoBPTXMuonsMonitoring.numGenericTriggerEventPSet.hltPaths = cms.vstring("HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v*")
hltNoBPTXMuonsMonitoring.muonSelection = cms.string("")
hltNoBPTXMuonsMonitoring.jetSelection = cms.string("")

exoHLTNoBPTXmonitoring = cms.Sequence(
    hltNoBPTXmonitoring
    + hltNoBPTXMuonsMonitoring
)

