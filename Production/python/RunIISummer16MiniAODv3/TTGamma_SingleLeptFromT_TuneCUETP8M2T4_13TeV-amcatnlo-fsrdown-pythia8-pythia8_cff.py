import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/001B2A97-1ECA-E811-8863-AC1F6B0DE0C4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/00D60D7E-16CA-E811-B2D7-20CF3027A67F.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/02A93AE0-1BCA-E811-BCDE-0CC47A1DF81C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/066C0438-1FCA-E811-9C78-0CC47A1E0DC2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/0A292E7C-27CA-E811-915C-002590E7D7CE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/0ACEFB45-1DCA-E811-A321-00259073E3C4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/0E640F50-1ACA-E811-9DD3-20CF305B05F0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/109BB39D-35CA-E811-A5D1-002590E7DE26.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/1E563F9B-1FCA-E811-926B-002590E7DE20.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/2E1AF61A-1ACA-E811-B131-002590E7E07A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/30FA2D1D-1CCA-E811-959C-002590E7DFFE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/3C3E3AD8-1DCA-E811-9E68-AC1F6B0DE2EC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/3E8EF01D-48CA-E811-A39C-002590E7D5AE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/4090D065-1CCA-E811-BE5B-002590E7D7E2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/4870D9A1-1CCA-E811-9CA4-002590E7DEBE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/4ADBB655-3CCA-E811-A179-0CC47A1E0488.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/5C914E5A-14CA-E811-9F02-002590E7DE36.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/5C97A8CA-1BCA-E811-A7CE-AC1F6B0DE296.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/6800731A-1ECA-E811-AD8F-0CC47A1E0DC8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/68BDB9AF-2ACA-E811-B826-20CF305B05E1.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/6E252C56-1CCA-E811-9601-002590E7D5A6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/72892417-1ECA-E811-8483-0CC47A1E0466.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/7AD15CDE-19CA-E811-9340-002590E7DFD6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/7C62DB95-19CA-E811-8447-002590E7DFD6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/7E4DB655-3CCA-E811-AA9F-0CC47A1E0488.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/80CEE2B5-18CA-E811-ABB8-20CF3056169B.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/82BE1C7A-1ECA-E811-A8FD-002590E7DEBE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/8C8AFA09-E0C9-E811-AD92-002590E7D7C2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/90865472-1DCA-E811-95F1-0CC47A1DF7E8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/9E05F66D-1BCA-E811-AB7F-00259073E40A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/A0B4064B-A4CA-E811-8EF9-002590E7D7C2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/A2CC7086-1CCA-E811-933C-002590E7DDE6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/A475C94E-37CA-E811-9F65-002590E7D7DE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/B068E49A-35CA-E811-BDBA-20CF305B05D1.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/B091D4C3-1BCA-E811-84A1-002590E7DF2A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/B2FA819B-0DCA-E811-9923-002590E7E050.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/B4576061-41CA-E811-8065-0CC47ABAC0CE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/B876D73A-1ECA-E811-B365-002590E7DFEE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/BE0708F8-1BCA-E811-9D13-002590E7E004.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/C0991E8A-34CA-E811-AE46-002590E7E012.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/CE921489-1FCA-E811-9BAF-002590E7D7D0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/D00FA043-1ECA-E811-BBF3-002590E7D7CE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/D22F20F7-1DCA-E811-8F03-002590E7E00A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/D68B3984-2BCA-E811-81ED-002590E7DFE0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/DCD2905D-30CA-E811-BDD9-AC1F6B0DE3EE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/E077946D-2DCA-E811-B2DF-0CC47A1E0488.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/E4B45537-20CA-E811-B410-20CF3027A686.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/EA9D1B07-19CA-E811-A156-0CC47ABB518A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/ECFE5CE1-1CCA-E811-8FFC-002590E7E00A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/F678F3FA-1ACA-E811-B8BA-AC1F6B0DE0C4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/FA048AF6-1BCA-E811-A9EA-0CC47ABB517C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/00000/FC0BBB6D-38CA-E811-92E0-20CF305B05D1.root',
] )