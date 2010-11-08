#################################################################
#                                                               #
# RPC Client Configuration file for RPC Source Output Root File #
#                      David Lomidze                            #
#                       INFN Napoli                             #
#                        Feb 2009                               #
#################################################################

import FWCore.ParameterSet.Config as cms

process = cms.Process("RPCDQMClientTest")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

#process.load("MagneticField.Engine.volumeBasedMagneticField_cfi")

process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("Geometry.RPCGeometry.rpcGeometry_cfi")

process.load("RecoLocalMuon.RPCRecHit.rpcRecHits_cfi")

#process.load("Configuration.StandardSequences.MagneticField_cff")

#process.load("CondCore.DBCommon.CondDBSetup_cfi")


##### Run as Emptry Source #######
process.source = cms.Source("EmptySource",
   firstRun = cms.untracked.uint32(1)
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")


################# DQM Client Modules ######################
process.load("DQM.RPCMonitorClient.RPCEventSummary_cfi")
process.rpcEventSummary.EventInfoPath = 'RPC/EventInfo'
#process.rpcEventSummary.RPCPrefixDir = 'RPC/RecHits'
#process.rpcEventSummary.RPCPrefixDir = 'RPC/RecHits'
process.rpcEventSummary.PrescaleFactor = 1
process.load("DQM.RPCMonitorClient.RPCMon_SS_Dbx_Global_cfi")

################# Quality Tests ############################
process.qTesterRPC = cms.EDFilter("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/RPCMonitorClient/test/RPCQualityTests.xml'),
    prescaleFactor = cms.untracked.int32(1)
)


################# Open Root file and provide MEs ############
process.ReadMeFromFile = cms.EDAnalyzer("ReadMeFromFile",
InputFile = cms.untracked.string('/afs/cern.ch/user/d/dlomidze/scratch0/DQM_ROOT_FILES/DQM_test.root')
#InputFile = cms.untracked.string('rfio:/castor/cern.ch/user/d/dlomidze/RPC/GlobalRuns/CosmicsCommissioning08-PromptReco-v2RECO/70664/root/Merge_tot.root')
#InputFile = cms.untracked.string('rfio:/castor/cern.ch/user/d/dlomidze/merged_dogo_R109606.root')                                       
#InputFile = cms.untracked.string('file:/afs/cern.ch/user/d/dlomidze/scratch0/test_2.root')
#InputFile = cms.untracked.string('file:/afs/cern.ch/user/d/dlomidze/scratch0/CMSSW_3_1_0_pre2/src/DQM/RPCMonitorDigi/python/DQM_500.000_RPCEvents.root')
)



################# DQM Client Modules ####################
process.load("DQM.RPCMonitorClient.RPCDqmClient_cfi")
process.rpcdqmclient.RPCDqmClientList = cms.untracked.vstring("RPCNoisyStripTest","RPCOccupancyTest","RPCClusterSizeTest","RPCDeadChannelTest","RPCMultiplicityTest")
process.rpcdqmclient.DiagnosticPrescale = cms.untracked.int32(1)
process.rpcdqmclient.MinimumRPCEvents = cms.untracked.int32(10)


################# RPC Event Summary Module ####################
process.load("DQM.RPCMonitorClient.RPCEventSummary_cfi")
process.rpcEventSummary.EventInfoPath = 'RPC/EventInfo'
process.rpcEventSummary.PrescaleFactor = 1

################# Quality Tests #########################
process.qTesterRPC = cms.EDFilter("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/RPCMonitorClient/test/RPCQualityTests.xml'),
    prescaleFactor = cms.untracked.int32(1)
)

###################### Chamber Quality ##################
process.rpcChamberQuality = cms.EDAnalyzer("RPCChamberQuality",
                                           MinimumRPCEvents = cms.untracked.int32(10000),
                                           PrescaleFactor = cms.untracked.int32(1) 
                                           )

########## Chamber Quality ##################
process.rpcChamberQuality = cms.EDAnalyzer("RPCChamberQuality",
                                           MinimumRPCEvents = cms.untracked.int32(10000),
                                           PrescaleFactor = cms.untracked.int32(1) 
                                           )



process.p = cms.Path(process.ReadMeFromFile*process.qTesterRPC*process.rpcdqmclient*process.rpcChamberQuality*process.dqmSaver)



#process.p = cms.Path(process.ReadMeFromFile*process.RPCOccupancyTest*process.dqmSaver)


################ DQM Enviroment ###################
process.dqmEnv.subSystemFolder = 'RPC'

############## DQM Saver ###############
process.dqmSaver.convention = 'Online'
process.dqmSaver.dirName = '.'
process.dqmSaver.producer = 'DQM'
#process.dqmSaver.saveByRun = -1
#process.dqmSaver.saveAtJobEnd = True

#dqmSaver = cms.EDFilter("DQMFileSaver",
    # Save file every N runs (-1: disabled)
#    saveByRun = cms.untracked.int32(-1),
    # Save file at the end of the job
 #   saveAtJobEnd = cms.untracked.bool(True)
  #                      )


#process.DQMStore.verbose = 1

######## DQM GUI ########
process.DQM.collectorHost = ''
process.DQM.collectorPort = 9090
process.DQM.debug = False



