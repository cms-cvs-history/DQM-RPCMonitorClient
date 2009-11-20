import FWCore.ParameterSet.Config as cms

rpcChamberQuality = cms.EDAnalyzer("RPCChamberQuality",
         MinimumRPCEvents = cms.untracked.int32(10000))
