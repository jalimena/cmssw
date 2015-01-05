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
        #"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_9_1_cFa.root"


"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_10_1_1Mz.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_11_1_p8H.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_12_1_2mG.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_13_1_C6u.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_14_1_n9K.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_15_1_kja.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_16_1_Agv.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_17_1_fob.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_18_1_ZdS.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_19_1_RkS.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_1_1_JNj.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_20_1_Ebx.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_21_1_JsZ.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_22_1_6so.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_23_1_Yx3.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_24_1_7RV.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_25_1_1HU.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_26_1_KSs.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_27_1_UuZ.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_28_1_2e1.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_29_1_GmM.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_2_1_fQN.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_30_1_D4K.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_31_1_ZQ7.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_32_1_kVJ.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_33_1_zOq.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_34_1_7zx.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_35_1_dtY.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_36_1_1lg.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_37_1_TmK.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_38_1_Yzp.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_39_1_w2c.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_3_1_lIk.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_4_1_1b5.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_5_1_Kk9.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_6_1_Ct7.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_7_1_oue.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_8_1_njq.root",
"root://eoscms//eos/cms/store/user/jalimena/HSCPmchamp6_M-500_TuneZ2star_8TeV-pythia6/reco_mchamp500_710pre7_PRESTA71V3/757fb463512dc747d0567e39a49bf997/step3_RAW2DIGI_HLT_L1Reco_RECO_mchamp500_9_1_cFa.root"

    )
)

process.maxEvents = cms.untracked.PSet(
    #input=cms.untracked.int32(1000)
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

#process.muonAnalyzer = cms.EDAnalyzer("MuonTimingValidatorDelayedMuons",
process.muonAnalyzer = cms.EDAnalyzer("MuonTimingValidatorDelayedMuonsRSA",
                                      #TKtracks = cms.untracked.InputTag("generalTracks"),
                                      #STAtracks = cms.untracked.InputTag("standAloneMuons"),
                                      refittedStandAloneMuonTag = cms.untracked.InputTag("refittedStandAloneMuons"),
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
                                      etaMax = cms.double(2.4),
                                      etaMin = cms.double(0.0),
                                      PlotScale = cms.double(1.0),
                                      DTcut  = cms.int32(8),
                                      CSCcut = cms.int32(4),
                                      DTChambersCut  = cms.int32(1),
                                      open = cms.string('recreate'),
                                      out = cms.string('test_timing_RSA_mchamp500.root'),
                                      txtout = cms.string('mchamp500')
                                      )

#process.prefer("GlobalTag")

process.GlobalTag.globaltag = 'PRE_STA71_V3::All'
#process.GlobalTag.globaltag = 'FT_53_V10_AN2::All'
#process.GlobalTag.globaltag = 'MC_3XY_V14::All'
#process.GlobalTag.globaltag = 'STARTUP_V7::All'

process.p = cms.Path(muontimingDelayedMuons)

process.mutest = cms.Path(process.muonAnalyzer)

process.schedule = cms.Schedule(process.p,process.mutest)	
# process.schedule = cms.Schedule(process.mutest)	

