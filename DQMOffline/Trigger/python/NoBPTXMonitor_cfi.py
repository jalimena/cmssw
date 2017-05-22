import FWCore.ParameterSet.Config as cms

hltNoBPTXmonitoring = cms.EDAnalyzer(
    "NoBPTXMonitor",
    FolderName = cms.string('HLT/NoBPTX/Jets/'),
    histoPSet = cms.PSet(
        jetPtPSet = cms.PSet(
            nbins = cms.int32 (  200  ),
            xmin  = cms.double(   -0.5),
            xmax  = cms.double(19999.5),
            ),
        muonPtPSet = cms.PSet(
            nbins = cms.int32 (  200  ),
            xmin  = cms.double(   -0.5),
            xmax  = cms.double(19999.5),
            ),
        ),
    jets      = cms.InputTag("ak4CaloJets"), 
    muons     = cms.InputTag("displacedStandAloneMuons"), 
    numGenericTriggerEventPSet = cms.PSet(
        andOr         = cms.bool( False ),
        andOrHlt      = cms.bool(True), # True:=OR; False:=AND
        #dbLabel       = cms.string("ExoDQMTrigger"), # it does not exist yet, we should consider the possibility of using the DB, but as it is now it will need a label per path !
        #hltDBKey      = cms.string("EXO_HLT_NoBPTX"),
        hltInputTag   = cms.InputTag( "TriggerResults::HLT" ),
        hltPaths      = cms.vstring("HLT_UncorrectedJetE60_NoBPTX3BX_v*"), # HLT_ZeroBias_v*
        errorReplyHlt = cms.bool( False ),
        verbosityLevel = cms.uint32(1),
        ),
    denGenericTriggerEventPSet = cms.PSet(
        andOr         = cms.bool( False ),
        dcsInputTag   = cms.InputTag( "scalersRawToDigi" ),
        dcsPartitions = cms.vint32 ( 24, 25, 26, 27, 28, 29 ), # 24-27: strip, 28-29: pixel, we should add all other detectors !
        andOrDcs      = cms.bool( False ),
        errorReplyDcs = cms.bool( True ),
        verbosityLevel = cms.uint32(1),
        ),
    muonSelection = cms.string("nDtChambersWithValidHits > 3 & nValidRpcHits > 1 & nValidCscHits < 1"),
    jetSelection = cms.string("abs(eta) < 1."),
)
