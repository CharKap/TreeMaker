import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/315/00000/262E7B46-F444-E611-8652-02163E011FD5.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/315/00000/7EFCEE5B-F444-E611-AC64-02163E0124FC.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/315/00000/EE3B604A-F444-E611-9BEF-02163E014704.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/317/00000/3AEC63BC-0445-E611-B4D7-02163E012B5D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/317/00000/80672480-0545-E611-813D-02163E014137.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/317/00000/F06CE88C-0545-E611-A7FC-02163E0141DD.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/2AC09EC9-3445-E611-B2DE-02163E0123C6.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/54FF0BAD-3445-E611-A07E-02163E011C6A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/62D9F396-3445-E611-88E9-02163E0133E2.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/86CF63CB-3445-E611-AA6F-02163E013749.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/A2245DA2-3445-E611-9404-02163E0142D1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/A48F58B2-3445-E611-89CC-02163E01187B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/EA648EB6-3445-E611-9120-02163E011C7B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/327/00000/98E89C1D-5145-E611-8335-02163E0145A1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/347/00000/227F032A-5445-E611-8627-02163E013873.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/352/00000/3C983FB1-5845-E611-AFBC-02163E01365B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/355/00000/6248C991-6345-E611-A380-02163E01365F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/357/00000/42034438-6645-E611-884C-02163E013892.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/357/00000/8E413017-6645-E611-AE1F-02163E01394C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/1C41CC5E-2646-E611-B14D-02163E0137D9.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/22C03971-2646-E611-A3D7-02163E014606.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/26086752-2646-E611-8945-02163E011D3F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/4EDAAF1A-2546-E611-A621-02163E012891.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/6CE0D664-2646-E611-BCFF-02163E012114.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/6CE7B45C-2646-E611-A39F-02163E013802.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/74D6E35E-2646-E611-A18A-02163E011A73.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/96526D69-2646-E611-BBEF-02163E013829.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/B0ADBA74-2646-E611-ACFD-02163E0122DA.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/C041C04D-2646-E611-B0EF-02163E014652.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/361/00000/EEB92A47-2646-E611-8A10-02163E014116.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/36BC01DA-6246-E611-9306-02163E0143FF.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/400B97EB-6246-E611-B30B-02163E01377C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/40D079CB-6246-E611-8D77-02163E0144AA.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/4424D111-6346-E611-BE08-02163E014614.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/6EA316E2-6246-E611-AFB7-02163E011B57.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/AAAA37F6-6246-E611-93D4-02163E014167.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/AC67A74E-6346-E611-BBDA-02163E014222.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/B463C4E2-6246-E611-8947-02163E014252.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/D497731B-6346-E611-A51F-02163E01444A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/363/00000/DC50B5CD-6246-E611-968E-02163E012977.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/384/00000/00B8B284-CD46-E611-B9E6-02163E011E80.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/384/00000/0EAD8F86-CD46-E611-91A0-02163E0144B4.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/384/00000/1E304E3F-CD46-E611-8863-02163E0127B4.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/384/00000/34419B84-CD46-E611-842E-02163E0143E5.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/384/00000/6CA25B7B-CD46-E611-BDEC-02163E01354A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/434/00000/6C31C4E3-A847-E611-B290-02163E014221.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/0A46A76B-A947-E611-AC7D-02163E01369D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/24C5016E-A947-E611-8026-02163E0142EF.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/30DA6769-A947-E611-B29E-02163E013601.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/382B46B4-A947-E611-B802-02163E0143C0.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/4480B791-A947-E611-B839-02163E012523.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/526C63A0-A947-E611-8AF2-02163E01445C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/58722E92-A947-E611-BAE5-02163E0142A6.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/625DAF62-A947-E611-8B66-02163E01474A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/64A3D49A-A947-E611-BAF4-02163E011DC7.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/66DF9375-A947-E611-B310-02163E0141B0.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/70655A88-A947-E611-A0D4-02163E0143FF.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/72781883-A947-E611-A7F6-02163E013664.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/8C15F981-A947-E611-89B1-02163E013585.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/A2C9F970-A947-E611-B1D8-02163E0143A4.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/B072CD81-A947-E611-A0AE-02163E014780.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/B65C4E7A-A947-E611-9C20-02163E014627.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/BC1CD163-A947-E611-B21F-02163E014464.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/C2A1158F-A947-E611-AC34-02163E0138D5.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/E6215740-A947-E611-9C88-02163E011A84.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/EED2819A-BB47-E611-AE5D-02163E0133DD.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/437/00000/F2197573-A947-E611-96C9-02163E0122E2.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/453/00000/38E10594-3A48-E611-A539-02163E013921.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/454/00000/A80EFFDF-3E48-E611-9658-02163E011A91.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/454/00000/D6BF0AD2-3E48-E611-897D-02163E01204B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/454/00000/E4CAE4D9-3E48-E611-B92C-02163E0129A4.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/455/00000/9AF080E9-4D48-E611-AE4D-02163E014157.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/455/00000/C4BB06D8-4D48-E611-837E-02163E013925.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/456/00000/00970841-4E48-E611-985F-02163E0134BB.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/457/00000/E8F442C0-4E48-E611-8A56-02163E0137A7.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/458/00000/38B7439A-5248-E611-AE97-02163E01433B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/458/00000/A6EE428B-5348-E611-8783-02163E011C5E.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/494/00000/448953E6-5448-E611-96B9-02163E0143B1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/495/00000/2CCBF35C-5548-E611-8AF3-02163E011B6C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/495/00000/5867E2F0-5548-E611-A196-02163E01252A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/495/00000/B6466DF1-5548-E611-9938-02163E0122D3.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/06C4A87D-0649-E611-BD19-02163E013788.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/12894385-0649-E611-8DA5-02163E0126E9.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/1ED8419F-0649-E611-BEBC-02163E0138E1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/1EFC1ABC-9248-E611-94EA-02163E0142FC.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/3017DB7D-0649-E611-A91D-02163E014500.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/72C73D7E-0649-E611-A3CE-02163E0133EE.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/74B11EA2-0649-E611-AED1-02163E0144D3.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/7A3B719D-9248-E611-9875-02163E01411F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/8E7B448E-0649-E611-83BB-02163E014438.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/9C0348E1-9248-E611-BD9B-02163E01186F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/BA3BD174-0649-E611-A825-02163E013851.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/C2E81E86-0649-E611-A3C8-02163E01393D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/C4F3626C-0649-E611-96DA-02163E0119D1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/D8E71ADA-9248-E611-B694-02163E011A1C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/E2639475-0649-E611-A8EB-02163E0134C9.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/EE0C15C8-9248-E611-B628-02163E011E3B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/F0220ECB-9248-E611-8C91-02163E0143FF.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/FA159596-0649-E611-83D2-02163E01358D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/501/00000/FE9EB495-9248-E611-8ACD-02163E01234C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/502/00000/36B3BD1A-5349-E611-A71B-02163E0140EE.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/502/00000/4EB83DC9-7049-E611-BB81-02163E014109.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/502/00000/5423B4DC-7049-E611-A3C1-02163E01356F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/502/00000/FACC221E-5349-E611-B67F-02163E013511.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/00FC37C7-8749-E611-8770-02163E01464F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/02C49A6D-8749-E611-88EF-02163E0134D1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/047A5607-D449-E611-8A3F-02163E01410D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/10A2419E-8749-E611-A86C-02163E0133FC.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/10F15E6E-8749-E611-80A6-02163E01181E.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/201E8E8D-8849-E611-A308-02163E014750.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/24EDAC19-8849-E611-80E8-02163E0119D1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/2C309587-8749-E611-A018-02163E0144B9.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/4265A158-8749-E611-94FB-02163E012190.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/4888A183-8849-E611-9267-02163E012679.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/5488BB21-8849-E611-A76E-02163E011F93.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/5873FD6C-D449-E611-AC0F-02163E011D6F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/763AFE55-8849-E611-9745-02163E014700.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/784AA471-8749-E611-ADA5-02163E014496.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/94D31082-8849-E611-B3FA-02163E0140E5.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/98282859-8749-E611-8F2A-02163E011EAB.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/A258CB2F-8849-E611-92ED-02163E013969.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/A643E667-8749-E611-B58F-02163E0121CD.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/CC31AA1B-8849-E611-9C40-02163E0146A7.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/DCD35EAA-8849-E611-A265-02163E011F67.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/E45BEC82-8849-E611-B6B1-02163E0145E3.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/E4D22C5E-8749-E611-BD1D-02163E012614.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/525/00000/EAABF429-8849-E611-9B1E-02163E014107.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/527/00000/F6DC507A-BC49-E611-9560-02163E011F73.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/528/00000/7E3805CE-C149-E611-BA31-02163E011E99.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/528/00000/A21AE326-C149-E611-A9EC-02163E01387A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/542/00000/16BBC284-CE49-E611-BB3D-02163E013466.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/542/00000/5A4C3A79-CE49-E611-ABC1-02163E014508.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/542/00000/5AABC976-CE49-E611-9371-02163E0134EE.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/542/00000/763148DD-CE49-E611-A8A9-02163E01232B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/542/00000/98D13899-CE49-E611-8F1A-02163E01448F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/542/00000/9C75817B-CE49-E611-BBC6-02163E0145C5.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/542/00000/C08C4162-CE49-E611-A6B4-02163E01216C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/542/00000/D8F44F74-CE49-E611-9196-02163E01180D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/543/00000/00FCD00A-F649-E611-9DE4-02163E014487.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/543/00000/16227903-F649-E611-AB87-02163E01414C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/543/00000/186DF48C-F949-E611-B08A-02163E01452D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/543/00000/2E5673CF-2E4A-E611-B4CA-02163E0143A1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/543/00000/36934B88-F949-E611-B1D6-02163E0141DD.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/543/00000/C43A8C0B-F649-E611-80CA-02163E014481.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/543/00000/CAEE271A-F649-E611-BA3F-02163E014457.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/543/00000/D019DD0B-F649-E611-ABBA-02163E013892.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/543/00000/DC7DA198-074A-E611-A079-02163E0134F3.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/544/00000/3E6E0EC2-0A4A-E611-B524-02163E012BBE.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/544/00000/82985114-024A-E611-ADFB-02163E011D28.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/545/00000/A41EC71E-024A-E611-8B0A-02163E012630.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/545/00000/DAAEA870-494A-E611-BA93-02163E01254C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/581/00000/2A6CAA83-1D4A-E611-83ED-02163E011863.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/581/00000/426CDD58-254A-E611-816C-02163E01442C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/581/00000/B859F575-324A-E611-A452-02163E01374B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/581/00000/C64E2C32-5A4A-E611-8653-02163E01475C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/581/00000/D474F8A1-174A-E611-8006-02163E014414.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/582/00000/20A40A02-7A4A-E611-8279-02163E0145A0.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/582/00000/24F3496E-764A-E611-B4FF-02163E0146EE.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/582/00000/2A442988-714A-E611-911B-02163E01446F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/582/00000/3E5C9251-724A-E611-91A9-02163E014735.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/582/00000/4EE179EF-A24A-E611-815E-02163E01384A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/582/00000/7AE4FA60-814A-E611-9535-02163E013518.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/582/00000/DC09759C-714A-E611-86E3-02163E01449A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/582/00000/E20EFE7B-764A-E611-B4ED-02163E0135A9.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/582/00000/F69CE49F-9C4A-E611-A17F-FA163E87B9AC.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/583/00000/4AFFF7DF-884A-E611-84F0-02163E01220A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/584/00000/5C535DC6-4A4A-E611-9B5A-02163E0144DB.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/585/00000/125F9F39-B54A-E611-ACC7-02163E0141BF.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/585/00000/40ECAA58-894A-E611-83DD-02163E01460A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/586/00000/8A3C054B-894A-E611-9CEF-02163E013868.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/586/00000/B88260FF-874A-E611-BC42-02163E011CB8.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/586/00000/BCC8FA70-AF4A-E611-9070-02163E014429.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/586/00000/F6927A20-904A-E611-B7B5-02163E0138AA.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/586/00000/FC9DBCFD-874A-E611-8136-02163E01354D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/587/00000/727AC687-E74A-E611-B839-FA163E6ED13D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/587/00000/A806F408-CC4A-E611-B226-FA163EB20221.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/587/00000/B048A00B-E74A-E611-93A9-02163E01212A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/587/00000/D862A9F4-CB4A-E611-9142-02163E011876.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/587/00000/F23BA7E1-C54A-E611-9EF5-FA163E6E60F6.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/653/00000/0AA8A421-E14A-E611-B153-FA163EACB094.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/653/00000/76B16E9A-374B-E611-8ABF-02163E0144D9.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/653/00000/C273B441-EC4A-E611-8050-02163E0143BC.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/653/00000/D0ECEB3A-E44A-E611-9B84-02163E01259B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/653/00000/E436B323-F44A-E611-8379-02163E0140FB.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/655/00000/1A2DC5D9-1D4B-E611-9C21-FA163E9C37A5.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/655/00000/40D6A286-0A4B-E611-AD7D-02163E012BAF.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/655/00000/54B06CC0-044B-E611-B71A-02163E011F18.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/655/00000/78B8F252-064B-E611-818A-FA163E7DAF8C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/655/00000/8A504A84-F64A-E611-AD32-FA163ED54B28.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/655/00000/92F9D155-054B-E611-94D2-02163E014573.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/655/00000/ECB064AB-FC4A-E611-8851-02163E013870.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/655/00000/F4922097-FC4A-E611-B8CF-02163E013499.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/655/00000/F6DBB0CC-044B-E611-8DE1-02163E012A06.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/659/00000/9442E2EC-304B-E611-BD1F-02163E014370.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/659/00000/E25540E3-2A4B-E611-9E8F-02163E014314.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/3A27FC76-2F4B-E611-B5F8-FA163E6FDBBC.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/503D8CE7-394B-E611-83E0-02163E01463B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/52DD594D-324B-E611-8053-FA163E83034A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/8AAC7027-494B-E611-894D-FA163EF86B63.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/96983535-474B-E611-8B40-FA163EF736D4.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/ACF281A1-374B-E611-93C7-FA163EF5D7EB.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/B28956ED-384B-E611-AF9D-02163E013453.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/DE94A8E9-354B-E611-B5E1-FA163E0C3A19.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/E223F031-404B-E611-ADD0-02163E01467D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/E64BD959-3F4B-E611-9CA9-FA163E2930B0.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/E6C32F29-474B-E611-8E97-02163E01365B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/775/00000/FE222B85-6E4B-E611-8A4D-02163E011C4B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/2219F054-884B-E611-9AC8-02163E01392C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/506AE800-8D4B-E611-8064-02163E01439C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/5E017103-8F4B-E611-A045-02163E014581.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/6AB2F773-8A4B-E611-AB92-FA163E38C3F6.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/8486E4D6-834B-E611-99DB-02163E0144E7.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/86D6B0F1-864B-E611-A0DB-02163E0144E7.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/AC107C41-A74B-E611-B3A7-02163E0133A4.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/B0B08930-7F4B-E611-B4F9-02163E011C55.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/BEF04759-864B-E611-B05E-02163E0140EB.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/DE046EF4-814B-E611-A5E6-02163E01478F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/776/00000/EEB39705-974B-E611-AD51-02163E011C8B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/794/00000/24E1091B-D44B-E611-90FF-02163E0142A0.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/794/00000/B8930E50-D64B-E611-9151-02163E013400.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/794/00000/F04CC430-D64B-E611-8F18-02163E01392F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/794/00000/F2EE9B32-D64B-E611-81DB-02163E012155.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/807/00000/72BD3DC2-DD4B-E611-BF8D-02163E01424B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/807/00000/D4226A2C-F84B-E611-BC77-FA163EB20DDA.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/807/00000/D4C15077-EB4B-E611-8BB3-02163E014236.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/0C13B74C-944C-E611-A835-02163E01344E.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/1E96AE56-944C-E611-B1A0-FA163EAD1F95.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/285A4724-104C-E611-BC2E-FA163E226722.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/52D1B58B-114C-E611-9ED5-02163E011BB4.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/662A4F48-944C-E611-A153-FA163E30CD71.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/7ACCDA1F-084C-E611-87DB-FA163EA7D13A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/9C66874D-944C-E611-AF33-02163E01455C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/C4F830A6-0A4C-E611-8FC4-FA163E823E1B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/CA8D99E5-0D4C-E611-A72F-FA163EF5EB75.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/808/00000/EE61A84D-944C-E611-8A51-FA163E090959.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/810/00000/00359725-984C-E611-BB99-02163E01369C.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/810/00000/5CE72F38-984C-E611-AB10-02163E011E06.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/810/00000/9E2D782B-984C-E611-BE40-02163E0146E5.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/00C7E6FC-9D4C-E611-BFA1-02163E0120D3.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/02761FE6-9D4C-E611-860E-FA163E090959.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/18819BF8-9D4C-E611-BF4A-02163E014530.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/188BB1E7-9D4C-E611-AD26-FA163EE7FE75.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/1AC171EF-9D4C-E611-8B78-02163E013804.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/22D8D6ED-9D4C-E611-99D3-02163E012650.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/3E37BFEE-9D4C-E611-8EFD-02163E01262A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/5E7F02E9-9D4C-E611-84B8-02163E0141FA.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/62E58DEE-9D4C-E611-8EE9-02163E014478.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/70A46DEC-9D4C-E611-A4DA-FA163E354935.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/7EFAD1E7-9D4C-E611-B81A-FA163EF3298F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/9C0110F3-9D4C-E611-A4F3-02163E013668.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/DC5E43F0-9D4C-E611-877E-FA163EF3F59F.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/811/00000/F87872EA-9D4C-E611-B339-FA163E669A5C.root',
] )