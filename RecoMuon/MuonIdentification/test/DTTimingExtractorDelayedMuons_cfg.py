import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger = cms.Service("MessageLogger",
                                    destinations  = cms.untracked.vstring( 'Info',
                                                                           'Errors',
                                                                           'Warnings',
                                                                           'Debug'),
                                    categories    = cms.untracked.vstring( 'eventNumber',
                                                                           'Root_Information',
                                                                           'EventSetupDependency'
                                                                           ),
                                    Info          = cms.untracked.PSet( threshold = cms.untracked.string('INFO'),
                                                                        Root_Information     = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
                                                                        EventSetupDependency = cms.untracked.PSet( limit = cms.untracked.int32(0) )
                                                                        ),
                                    Errors        = cms.untracked.PSet( threshold = cms.untracked.string('ERROR') ),
                                    Warnings      = cms.untracked.PSet( threshold = cms.untracked.string('WARNING') ),
                                    Debug         = cms.untracked.PSet( threshold =  cms.untracked.string('DEBUG') ),
                                    debugModules  = cms.untracked.vstring('*')
                                    )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("RecoMuon.MuonIdentification.DTTimingExtractorDelayedMuons_cfi")
from RecoMuon.MuonIdentification.DTTimingExtractorDelayedMuons_cfi import *

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(INPUTFILE)
                            )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("timing.root")
                                   )

process.p = cms.Path(process.DTTimingExtractorDelayedMuons)
