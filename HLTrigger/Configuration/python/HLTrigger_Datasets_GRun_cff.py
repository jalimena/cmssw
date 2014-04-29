# getDatasets.py

import FWCore.ParameterSet.Config as cms


# dump of the Stream A Datasets defined in the HLT table as Stream A Datasets

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetInitialPD_selector
streamA_datasetInitialPD_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetInitialPD_selector.l1tResults = cms.InputTag('')
streamA_datasetInitialPD_selector.throw      = cms.bool(False)
streamA_datasetInitialPD_selector.triggerConditions = cms.vstring('HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1', 
    'HLT_Ele17_Ele8_Gsf_v1', 
    'HLT_Ele17_Ele8_Mass50_v1', 
    'HLT_Ele27_WP80_Gsf_v1', 
    'HLT_Ele27_WP80_v1', 
    'HLT_Photon20_CaloIdVL_IsoL_v1', 
    'HLT_Photon26_R9Id85_Photon18_CaloId10_Iso50_v1')

