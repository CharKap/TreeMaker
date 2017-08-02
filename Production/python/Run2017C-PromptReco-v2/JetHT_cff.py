import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/064/00000/08A0D429-EF76-E711-A28E-02163E0121D4.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/079/00000/AC828BE1-1277-E711-9C1F-02163E01A773.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/087/00000/1A79F1C8-0B77-E711-9D15-02163E01A463.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/087/00000/24EDFF13-0777-E711-83B7-02163E019E33.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/087/00000/6ACDB8AF-0477-E711-AE9D-02163E0119FA.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/087/00000/BA91AEE0-1977-E711-A1BB-02163E014173.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/087/00000/C2E8E48E-1277-E711-BC9D-02163E013849.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/101/00000/8A94223B-0F77-E711-A4CF-02163E01A6E9.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/104/00000/C01B6890-1B77-E711-848C-02163E01A384.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/105/00000/D2AAAFBF-3A77-E711-86AC-02163E01A4CB.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/106/00000/0A191DA7-2B77-E711-82F8-02163E014255.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/106/00000/0AD51F7C-3D77-E711-9D48-02163E01394B.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/106/00000/42B1FCC0-3477-E711-9FD6-02163E019D63.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/107/00000/32A6E650-3A77-E711-A789-02163E01343E.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/107/00000/94B4598E-3277-E711-A9D1-02163E01A2CC.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/117/00000/58E56AF6-4677-E711-96A4-02163E019CC4.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/02172630-6277-E711-B94A-02163E019D7C.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/02BF171E-6777-E711-BE01-02163E0135C0.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/12F97C4B-7177-E711-8F03-02163E01A1F7.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/1C2E493D-6577-E711-BD30-02163E011B72.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/2808C2D7-6B77-E711-BC06-02163E0127A9.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/3047C068-6D77-E711-96EA-02163E019D24.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/365B322B-6F77-E711-8CE7-02163E01A380.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/3EEC3F3E-6A77-E711-A17D-02163E011C3E.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/441450D2-6077-E711-B478-02163E01475C.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/502ED556-5E77-E711-AAB6-02163E019D7E.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/5A5DF13C-6977-E711-B41B-02163E01A5AE.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/6242FBE9-5B77-E711-8AEC-02163E014226.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/645FD0BF-5A77-E711-A1C3-02163E0144DE.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/647ED064-6477-E711-A140-02163E01A4CB.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/761C28D0-5F77-E711-A7FC-02163E01A35D.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/8C2698A8-7477-E711-8A53-02163E01A21E.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/8E3222BD-5E77-E711-9A15-02163E011F04.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/C4738240-5977-E711-8185-02163E011C1F.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/C8C0E1F8-6377-E711-9761-02163E011977.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/F823C628-7B77-E711-94DA-02163E01A2FB.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/122/00000/FEF0CA19-5D77-E711-9772-02163E014333.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/123/00000/00AA70E1-7577-E711-8E8D-02163E01A2C6.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/123/00000/06D726EF-6F77-E711-AAA2-02163E014613.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/123/00000/1CE992BA-6A77-E711-A4F6-02163E01A75B.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/123/00000/521841AF-7177-E711-BA46-02163E019C23.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/123/00000/94D78963-7377-E711-8BB4-02163E011BFF.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/123/00000/CA2E2419-6E77-E711-9F17-02163E01A739.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/123/00000/D4208957-7977-E711-99D1-02163E011D74.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/124/00000/1C0B06CA-7577-E711-BA9B-02163E01421C.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/124/00000/36C8B78A-7C77-E711-AE88-02163E0138FE.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/124/00000/7E1288DC-6D77-E711-B6CA-02163E012976.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/124/00000/EE1D7749-7377-E711-809A-02163E01A605.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/124/00000/F42C2761-7877-E711-A62E-02163E013982.root',
'/store/data/Run2017C/JetHT/MINIAOD/PromptReco-v2/000/300/124/00000/F84AFD79-7177-E711-B9E8-02163E012388.root' ] );
