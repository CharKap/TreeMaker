import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-1.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-10.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-2.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-3.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-4.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-5.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-6.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-7.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-8.root',
'root://cmseos.fnal.gov///store/group/lpcsusyhad/ExoEMJAnalysis2020/Signal.Oct.2021/UL16APV/step4_MINIAODv2_mMed-2400_mDark-20_ctau-25_unflavored-down_n-500_part-9.root',
] )
