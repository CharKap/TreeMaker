#Made in python using
#import glob
#for f in glob.glob('Autumn18/*_cff.py'):
#     print  "\'"+f.replace("_cff.py","").replace("/",".")+"\',"

flist = [
'Autumn18.DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'Autumn18.DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'Autumn18.DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'Autumn18.DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'Autumn18.DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'Autumn18.DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_ext1',
'Autumn18.QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8_ext1',
'Autumn18-HEM.QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8_ext1',
'Autumn18.QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_120to170_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8_ext1',
'Autumn18.QCD_Pt_170to300_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8_ext1',
'Autumn18.QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8_ext1',
'Autumn18.QCD_Pt_300to470_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_470to600_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_470to600_TuneCP5_13TeV_pythia8_ext1',
'Autumn18.QCD_Pt_600to800_TuneCP5_13TeV_pythia8',
'Autumn18.QCD_Pt_800to1000_TuneCP5_13TeV_pythia8_ext1',
'Autumn18.QCD_Pt_80to120_TuneCP5_13TeV_pythia8',
'Autumn18.ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8_ext1',
'Autumn18.ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_ext1',
'Autumn18.ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1',
'Autumn18.ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_ext1',
'Autumn18.ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1',
'Autumn18.TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
'Autumn18.TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.TTJets_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',
'Autumn18.TTToHadronic_TuneCP5_13TeV-powheg-pythia8',
'Autumn18.TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8',
'Autumn18.TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_ext1',
'Autumn18.TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
'Autumn18.TTWW_TuneCP5_13TeV-madgraph-pythia8_ext1',
'Autumn18.TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_ext1',
'Autumn18.WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.ZJetsToNuNu_HT-100To200_13TeV-madgraph',
'Autumn18.ZJetsToNuNu_HT-1200To2500_13TeV-madgraph',
'Autumn18.ZJetsToNuNu_HT-200To400_13TeV-madgraph',
'Autumn18.ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph',
'Autumn18.ZJetsToNuNu_HT-600To800_13TeV-madgraph',
'Autumn18.ZJetsToNuNu_HT-800To1200_13TeV-madgraph',
'Autumn18.TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'Autumn18.DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'Autumn18.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8',
'Autumn18.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8',
'Autumn18.ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
'Autumn18.TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8',
'Autumn18.DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'Autumn18.ZJetsToNuNu_HT-400To600_13TeV-madgraph',
]