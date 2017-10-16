from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

### General ###
config.section_('General')
#config.General.requestName = 'HIForest_DATA_pPb8TeV_run285479_20170505'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#### JobType ####
config.section_('JobType')
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pPb_DATA_80X.py"
config.JobType.maxMemoryMB = 2500

#### Data ####
#config.Data.inputDataset = "/PAMinimumBias1/PARun2016C-PromptReco-v1/AOD"
config.Data.lumiMask = 'Cert_285479_HI8TeV_PromptReco_pPb_Collisions16_JSON_NoL1T.txt'
config.Data.inputDBS = "global"
config.Data.splitting = "LumiBased"
config.Data.unitsPerJob = 5
#config.Data.totalUnits = 
config.Data.publication = False
config.Data.ignoreLocality = True

#### Site ####
config.section_('Site')
config.Site.whitelist = ['T2_FR_GRIF_*',"T2_CH_CERN"]
config.Site.storageSite = 'T2_FR_GRIF_LLR'

if __name__ == '__main__':
  from CRABAPI.RawCommand import crabCommand
  for dataset in ['/PAMinimumBias1/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias10/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias11/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias12/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias13/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias14/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias15/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias16/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias17/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias18/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias19/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias2/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias20/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias3/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias4/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias5/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias6/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias7/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias8/PARun2016C-PromptReco-v1/AOD','/PAMinimumBias9/PARun2016C-PromptReco-v1/AOD']:
      config.Data.inputDataset = dataset
      config.General.requestName = dataset.split('/')[1]
      config.Data.outLFNDirBase = '/store/user/%s/DATA_pPb8TeV_run285479/%s' % (getUsernameFromSiteDB(), config.General.requestName)
      config.Data.outputDatasetTag = config.General.requestName
      crabCommand('submit', config = config)
