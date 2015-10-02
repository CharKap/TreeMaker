import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/008EC8F9-8C5E-E511-B5D7-0025905A607E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/0AA5C601-8E5E-E511-9F18-002354EF3BD0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/10111190-AC5E-E511-B13A-0025905A48B2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/1235F879-AB5E-E511-8300-0025905A6068.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/168A2E0D-8E5E-E511-8BCD-002618943831.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/1861A30A-7F5E-E511-8177-24BE05C38C91.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/187B0409-6A5E-E511-B115-00261894380D.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/18FE8918-8E5E-E511-86F6-003048FFD756.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/22A15F13-8E5E-E511-AA6E-0025905A609E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/249532AA-885E-E511-82E8-0002C92DB418.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/26A91FDE-8D5E-E511-8456-0025905B860C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/3046A39F-885E-E511-9AFC-24BE05C6B701.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/36E0479F-715E-E511-AC61-F45214C748D0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/4A5EB407-8D5E-E511-A1BA-0025905964BE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/4A882C14-8E5E-E511-A72D-0025905A60E4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/4C4BA9C9-735E-E511-97D6-B8CA3A709028.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/4C9EF014-8E5E-E511-864B-0025905A6094.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/50CA7CE0-8D5E-E511-B7B6-0025905964BE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/58E482C8-8C5E-E511-9609-0025905A4964.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/5A5AE8EE-C95E-E511-8DD0-0025905B8606.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/5C6A8AC8-8C5E-E511-BF84-0026189438A9.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/5CD60418-8E5E-E511-BD58-0025905A60C6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/5E68DD14-8E5E-E511-8BC6-0025905B8576.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/64CC48BA-305F-E511-B8DB-008CFA1111D0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/66A5F3F5-8D5E-E511-BF93-0026189438EB.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/66EAD6C9-8C5E-E511-89EC-003048FF9AC6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/70DF19AA-885E-E511-837C-F45214C748C8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/72ED52F7-B05E-E511-8595-003048FFD732.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/7AE8464C-DD5E-E511-9F4C-008CFA110C84.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/7E7FB9FD-8C5E-E511-BEA2-002590593872.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/82DA35B8-8D5E-E511-94FE-0025905A607E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/926A3183-305F-E511-A009-002618943832.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/947C4418-8E5E-E511-85FF-003048FFCB84.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/9610E717-6A5E-E511-BB7D-003048FFD732.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/9849A4CE-8D5E-E511-A725-002618943858.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/9C1A5508-8D5E-E511-8E35-0025905964CC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/A2587813-8E5E-E511-9FDC-00261894395C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/A6590DD5-8C5E-E511-94B6-0025905AA9CC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/AEF16512-8E5E-E511-B3FD-0025905A60A8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/B26D9B07-8E5E-E511-A7A2-0026189438C4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/B65F79F8-8C5E-E511-B721-0025905964A6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/BEC034FB-8D5E-E511-92AC-0025905A6082.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/C2173793-AC5E-E511-AC44-0025905B85D8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/C4266A75-305F-E511-A133-0025905A60F8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/CC5FBFB4-885E-E511-A7FC-5065F3812201.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/D20C3F13-8E5E-E511-9CE1-00261894383E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/D210B8E3-305F-E511-9645-F45214C7493C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/D2FC3A13-8E5E-E511-AE85-00259059642E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/D4D409CA-8D5E-E511-B345-0025905A6138.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/DC98C8D5-8D5E-E511-9CCF-0026189438EA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/E08746FB-8D5E-E511-B01D-002618943836.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/E0DE8604-8E5E-E511-8542-003048FF9AA6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/E2D0FAF4-715E-E511-B932-0002C92DB464.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/E8F08C01-B75E-E511-84E0-008CFA1979A0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/F6B5C3C6-8D5E-E511-9E3C-0026189438EA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/FE12B1FB-8D5E-E511-B96C-0026189438E0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/FE6CABD0-8C5E-E511-B886-00261894386F.root' ] );


secFiles.extend( [
               ] )
