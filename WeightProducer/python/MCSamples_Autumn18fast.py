import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Autumn18
Autumn18samples = [
    MCSample('Stealth_CN-925_sgetbb' , '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD' , 'Constant', 36105, False),
    MCSample('Stealth_CN-925_sgetglgl' , '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD' , 'Constant', 39739, False),
    MCSample('Stealth_CN-600_sgetbb' , '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD' , 'Constant', 44405, False),
    MCSample('Stealth_CN-600_sgetglgl' , '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD' , 'Constant', 40560, False),
]
