from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from WMCore.DataStructs.LumiList import LumiList

config = config()

config.section_('General')
config.General.requestName = 'pPb_8TeV-OniaSkim-PADoubleMuon-Trk-v3_180619'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hiOniaTrk_pPb_80X_DATA_cfg.py'
#config.JobType.outputFiles = ['oniaTree_numEvent1000.root']
#config.JobType.maxMemoryMB = 3500

config.section_('Data')
config.Data.inputDataset = '/PADoubleMuon/PARun2016C-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 2
config.Data.splitting = 'LumiBased'
config.Data.runRange = '285479-285832'
### Use when running firts time
config.Data.lumiMask = 'Cert_285479-285832_HI8TeV_PromptReco_pPb_Collisions16_JSON_NoL1T_MuonPhys.txt'
### When submiting the jobs again, please use:
#config.Data.lumiMask = '<NAME OF MISSING LUMI MASK FROM PREVIOUS CRAB JOB>'
# The missing lumimask can be obtain after using crab report -d <path to crab job dir>

config.Data.publication = False
config.Data.outputDatasetTag = 'pPb_8TeV-OniaSkim-PADoubleMuon-Trk-v3_180619'
config.Data.outLFNDirBase =  '/store/user/%s/pPb_8TeV-OniaSkim/%s' % (getUsernameFromSiteDB(), config.Data.outputDatasetTag)

#config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T3_KR_KISTI'
