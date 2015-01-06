import FWCore.ParameterSet.Config as cms

process = cms.Process("Test")

process.source = cms.Source("PoolSource",
    #debugFlag = cms.untracked.bool(True),
    #debugVebosity = cms.untracked.uint32(1),
	
    fileNames = cms.untracked.vstring(

        #'/store/relval/CMSSW_3_2_1/RelValSingleMuPt100/GEN-SIM-RECO/MC_31X_V3-v1/0006/DC15F12B-9477-DE11-B1E0-000423D98C20.root',
        #'/store/relval/CMSSW_3_2_1/RelValSingleMuPt100/GEN-SIM-RECO/MC_31X_V3-v1/0006/40D6FEFD-8F77-DE11-95A7-001D09F27067.root',
        #'/store/relval/CMSSW_3_2_1/RelValSingleMuPt100/GEN-SIM-RECO/MC_31X_V3-v1/0005/50EE1208-8177-DE11-8B17-001D09F231B0.root'
    #'root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-600_TuneZ2star_8TeV-pythia6/reco_mchamp600_533_noPU_forceMuons/a5fd4cac2592ce07df32b7c4e3a336e1/step3_RAW2DIGI_HLT_L1Reco_RECO_34_1_w58.root'

"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_10_1_p7I.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_11_1_Y4x.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_12_1_T80.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_13_1_23Q.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_14_1_7SS.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_15_1_MPV.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_16_1_27G.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_17_1_JNy.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_18_1_cK3.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_19_1_2IR.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_1_1_gJW.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_20_1_kWR.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_21_1_7G2.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_22_1_fTz.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_23_1_YLV.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_24_1_L0F.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_25_1_mCg.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_26_1_7No.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_27_1_uY2.root",
"dcap:///pnfs/cms/WAX/11/store/user/alimena/HSCPmchamp6_M-1000_TuneZ2star_8TeV-pythia6/reco_mchamp1000_539/3e7efd38df922af2041539cd5b48570c/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp1000_28_1_zvL.root",

    
    )
)

process.maxEvents = cms.untracked.PSet(
	#input=cms.untracked.int32(100)
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
                                      STAtracks = cms.untracked.InputTag("standAloneMuons"),
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
                                      #DTcut  = cms.int32(3),
                                      DTcut  = cms.int32(8),
                                      CSCcut = cms.int32(4),
                                      DTChambersCut  = cms.int32(1),
                                      #DTChambersCut  = cms.int32(0),
                                      open = cms.string('recreate'),
                                      #out = cms.string('test_timing_stop600_neutralino417.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_prune20.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_prune10.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_prune5.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_prune2.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DT8.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2_prune20.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2_prune10.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2_prune5.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2_prune2.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DT8_DTChambers2.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_invbetaerror1p5.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_LESSinvbetaerror1p5.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2_upper.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2_upper_prune20.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2_upper_prune10.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2_upper_prune5.root'),
                                      #out = cms.string('test_timing_stop600_neutralino417_pt20_eta1_DTChambers2_upper_prune2.root'),
                                      out = cms.string('test_timing_mchamp1000_pt20_eta1_DTChambers2_includeTheta.root'),
                                      txtout = cms.string('mchamp1000')
                                      )

#process.prefer("GlobalTag")

process.GlobalTag.globaltag = 'FT_53_V10_AN2::All'
#process.GlobalTag.globaltag = 'MC_3XY_V14::All'
#process.GlobalTag.globaltag = 'STARTUP_V7::All'

process.p = cms.Path(muontimingDelayedMuons)

process.mutest = cms.Path(process.muonAnalyzer)

process.schedule = cms.Schedule(process.p,process.mutest)	
# process.schedule = cms.Schedule(process.mutest)	

