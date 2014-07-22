import FWCore.ParameterSet.Config as cms

process = cms.Process("Test")

process.source = cms.Source("PoolSource",
    #debugFlag = cms.untracked.bool(True),
    #debugVebosity = cms.untracked.uint32(1),
	
    fileNames = cms.untracked.vstring(

        #'/store/relval/CMSSW_3_2_1/RelValSingleMuPt100/GEN-SIM-RECO/MC_31X_V3-v1/0006/DC15F12B-9477-DE11-B1E0-000423D98C20.root',
        #'/store/relval/CMSSW_3_2_1/RelValSingleMuPt100/GEN-SIM-RECO/MC_31X_V3-v1/0006/40D6FEFD-8F77-DE11-95A7-001D09F27067.root',
        #'/store/relval/CMSSW_3_2_1/RelValSingleMuPt100/GEN-SIM-RECO/MC_31X_V3-v1/0005/50EE1208-8177-DE11-8B17-001D09F231B0.root'
    #'root://eoscms//eos/cms/store/user/jalimena/NoBPTX_Run2012D_cosmics_allphi_RECO/208593/46518E45-9840-E211-9BB3-E0CB4E4408E3.root'
    'file:/uscms_data/d3/alimena/NoBPTX_cosmics_allphi_RECO/208593/46518E45-9840-E211-9BB3-E0CB4E4408E3.root'
    )
)

process.maxEvents = cms.untracked.PSet(
	#input=cms.untracked.int32(100)
        #input=cms.untracked.int32(100000)
        input=cms.untracked.int32(-1)
)

process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
process.load("Geometry.CommonDetUnit.globalTrackingGeometry_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("RecoMuon.MuonIdentification.muonTimingDelayedMuons_cfi")
from Configuration.StandardSequences.Reconstruction_cff import *
from RecoMuon.MuonIdentification.muonTimingDelayedMuons_cfi import *

process.muonAnalyzer = cms.EDAnalyzer("MuonTimingValidatorDelayedMuons",
                                      TKtracks = cms.untracked.InputTag("generalTracks"),
                                      #STAtracks = cms.untracked.InputTag("standAloneMuons"),
                                      STAtracks = cms.untracked.InputTag("refittedStandAloneMuons"),
                                      Muons = cms.untracked.InputTag("muons"),
                                      nbins = cms.int32(100),
                                      #nbins = cms.int32(60),
                                      PtresMax = cms.double(200.0),
                                      #PtresMax = cms.double(2000.0),
                                      Timing = cms.untracked.InputTag("muontimingDelayedMuons"),
                                      simPtMin = cms.double(5.0),
                                      PtresMin = cms.double(-1000.0),
                                      PtCut = cms.double(20.0),
                                      #PtCut = cms.double(1.0),
                                      #PtCut = cms.double(0.0),
                                      #etaMax = cms.double(2.4),
                                      etaMax = cms.double(1.0),
                                      etaMin = cms.double(0.0),
                                      PlotScale = cms.double(1.0),
                                      DTcut  = cms.int32(8),
                                      #DTcut  = cms.int32(3),
                                      CSCcut = cms.int32(4),
                                      DTChambersCut  = cms.int32(1),
                                      #DTChambersCut  = cms.int32(0),
                                      open = cms.string('recreate'),
                                      #out = cms.string('test_timing_allphi_cosmics.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_prune20.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_prune10.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_prune5.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_prune2.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DT8.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_prune20.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_prune10.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_prune5.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_prune2.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DT8_DTChambers2.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_Upper_beta1.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_invbetaerror1p5.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_LESSinvbetaerror1p5.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_upper.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_upper_prune20.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_upper_prune10.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_upper_prune5.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_upper_prune2.root'),
                                      #out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2_includeTheta.root'),
                                      out = cms.string('test_timing_allphi_cosmics_pt20_eta1_DTChambers2.root'),
                                      txtout = cms.string('allphi_cosmics')
                                      )

#process.prefer("GlobalTag")

process.GlobalTag.globaltag = 'FT_R_70_V1::All'
#process.GlobalTag.globaltag = 'FT_53_V10_AN2::All'
#process.GlobalTag.globaltag = 'MC_3XY_V14::All'
#process.GlobalTag.globaltag = 'STARTUP_V7::All'

process.p = cms.Path(muontimingDelayedMuons)

process.mutest = cms.Path(process.muonAnalyzer)

process.schedule = cms.Schedule(process.p,process.mutest)	
# process.schedule = cms.Schedule(process.mutest)	

