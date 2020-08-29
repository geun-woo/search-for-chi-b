from CRABClient.UserUtilities import config
from WMCore.DataStructs.LumiList import LumiList

config = config()

config.section_('General')
config.General.requestName = 'conversion_test_Pbp'
#config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hiOniaTrk_pPb_80X_DATA_cfg.py'
#config.JobType.outputFiles = ['oniaTree_numEvent1000.root']
config.JobType.maxMemoryMB = 2600
config.JobType.maxJobRuntimeMin = 1315 #1315

config.section_('Data')
config.Data.inputDataset = '/PADoubleMuon/PARun2016C-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 2
config.Data.splitting = 'LumiBased'
config.Data.runRange = '285952-286496'
### Use when running firts time
config.Data.lumiMask = 'Cert_285952-286496_HI8TeV_PromptReco_Pbp_Collisions16_JSON_NoL1T_MuonPhys.txt'
### When submiting the jobs again, please use:
#config.Data.lumiMask = '<NAME OF MISSING LUMI MASK FROM PREVIOUS CRAB JOB>'
# The missing lumimask can be obtain after using crab report -d <path to crab job dir>

config.Data.publication = False # True
#config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outLFNDirBase =  '/store/user/gekim/'
config.Data.outputDatasetTag = 'conversion_test_Pbp' # crab_ + General.requestName

#config.section_('User')
config.section_('Site')
config.Site.blacklist = ['T2_US_Vanderbilt', 'T2_CH_CERN']
#config.Site.whitelist = ['T2_KR_*', 'T3_KR_*']
config.Site.storageSite = 'T2_KR_KISTI'
