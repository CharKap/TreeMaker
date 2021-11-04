import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16/step4_MINIAODv2_mMed-1400_mDark-2_kappa-0p92_aligned-down_n-500_part-5.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16/step4_MINIAODv2_mMed-1400_mDark-2_kappa-0p92_aligned-down_n-500_part-8.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16/step4_MINIAODv2_mMed-1400_mDark-2_kappa-0p92_aligned-down_n-500_part-9.root',
] )
