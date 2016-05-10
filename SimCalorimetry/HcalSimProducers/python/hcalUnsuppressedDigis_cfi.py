import FWCore.ParameterSet.Config as cms
from SimCalorimetry.HcalSimProducers.hcalSimParameters_cfi import *

# make a block so other modules, such as the data mixing module, can
# also run simulation

hcalSimBlock = cms.PSet(    
    hcalSimParameters,
    # whether cells with MC signal get noise added
    doNoise = cms.bool(True),
    HcalPreMixStage1 = cms.bool(False),
    HcalPreMixStage2 = cms.bool(False),
    # whether cells with no MC signal get an empty signal created
    # These empty signals can get noise via the doNoise flag
    doEmpty = cms.bool(True),
    doHPDNoise = cms.bool(False),
    doIonFeedback = cms.bool(True),
    doThermalNoise = cms.bool(True),
    # fudge factors for "Cholesky" noise simulation (obsolete)
    HBTuningParameter = cms.double(0.875),
    HETuningParameter = cms.double(0.9),
    HFTuningParameter = cms.double(1.025),
    HOTuningParameter = cms.double(1),
    # use old way of noise simulation  
    useOldHB = cms.bool(True),
    useOldHE = cms.bool(True),
    useOldHF = cms.bool(True),
    useOldHO = cms.bool(True),
    HBHEUpgradeQIE = cms.bool(True),
    HFUpgradeQIE   = cms.bool(False),
    HFQIE8         = cms.bool(True),
    HFQIE10        = cms.bool(False),
    #HPDNoiseLibrary = cms.PSet(
    #   FileName = cms.FileInPath("SimCalorimetry/HcalSimAlgos/data/hpdNoiseLibrary.root"),
    #   HPDName = cms.untracked.string("HPD")
    #),
    doTimeSlew = cms.bool(True),
    doHFWindow = cms.bool(False),
    hitsProducer = cms.string('g4SimHits'),
    injectTestHits = cms.bool(False),
    ChangeResponse = cms.bool(False),
    CorrFactorFile = cms.FileInPath("SimCalorimetry/HcalSimProducers/data/calor_corr01.txt"),
    DelivLuminosity = cms.double(0),
    TestNumbering = cms.bool(False),
    HEDarkening = cms.bool(False),
    HFDarkening = cms.bool(False),
    minFCToDelay=cms.double(5.) # old TC model! set to 5 for the new one
)

from Configuration.StandardSequences.Eras import eras
eras.fastSim.toModify( hcalSimBlock, hitsProducer=cms.string('famosSimHits') )
eras.run2_HF_2016.toModify( hcalSimBlock, HFQIE8=cms.bool(True), HFQIE10=cms.bool(True) )
    
#from CondCore.CondDB.CondDB_cfi import *
#CondDB_cholesky = CondDB.clone( connect = cms.string('sqlite_file:CondFormats/HcalObjects/data/cholesky_sql.db') )
#es_cholesky = cms.ESSource("PoolDBESSource",
#    CondDB_cholesky,
#    timetype = cms.string('runnumber'),
#    toGet = cms.VPSet(
#        cms.PSet(
#            record = cms.string("HcalCholeskyMatricesRcd"),
#            tag = cms.string("TestCholesky")
#        )),
#    appendToDataLabel = cms.string('reference'),
#    authenticationMethod = cms.untracked.uint32(0),
#)


#es_cholesky = cms.ESSource('HcalTextCalibrations',
#    input = cms.VPSet(
#        cms.PSet(
#            object = cms.string('CholeskyMatrices'),
#            file = cms.FileInPath("CondFormats/HcalObjects/data/CholeskyMatrices.txt")
#        ),
#    ),
#    appendToDataLabel = cms.string('reference')
#)
