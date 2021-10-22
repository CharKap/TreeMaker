import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/9D999931-9DB8-A54D-B7EA-EC2DF164875C.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/317FD776-ED09-CB45-9ED3-5ABAC10A2946.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/B22A79E1-D7C4-CF4B-9054-14EABB782E2B.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8388541F-7410-A540-871B-EF7A2277915C.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/A94CC79E-B2E7-4740-A2FD-118DB3FD8E34.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/A83C3804-8A82-C64A-A9B8-2DD0CA514EB5.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8D7D67DC-C258-B34C-A4DF-FD99982CB64B.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/953E3497-F959-5342-A520-826DBC7E16EC.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8E3A1E94-9829-C141-A6E4-24DA8BC14BF3.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/C665EE2F-ECEC-B04D-923B-E6615664A1F6.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/3E90368C-0545-3E49-BD2A-3C8851B128C5.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8B2C14FF-695C-6748-B4AC-CCF38E3814AE.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/02D10F9F-BFC1-8B44-BB61-77F35C301A05.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/B93247DE-9A12-F145-B4FC-536DF9AED216.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/3DF33431-AA08-3643-B685-EE6E8201F957.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/0E568E3E-E2B8-7447-83B8-4E47354C2DEA.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/483F7F19-2A12-E14E-A451-C37552B65E8E.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/DBB6B6B2-5B94-1948-A015-761101864C64.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8DE0D520-2331-7A4F-831D-DD5FE0BD4D2E.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/91338107-6849-4B48-AC8A-96F2B8FB19F7.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/6D672EFF-0996-B147-A5E5-1A8F2EC16DA3.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/E63A6D30-6C3B-0F4B-8FAF-465034E8DC89.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/EADD7E66-EB71-0E43-B02A-806DDABB40D0.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/11561102-69B5-E844-840B-A882A439AF25.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/94E671DD-60AC-FD4D-B50D-C3101C987790.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/5C7401CD-2227-C243-B6AD-5A07401218DB.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/FCE2841E-3396-784A-850C-212470BF5CD7.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/C695BA8A-69C2-C047-A756-D25D78914E4C.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/39AC6036-ED42-6542-B44E-FD8FBF5A50A2.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/45BB8320-E5F7-8C42-B063-601B805EB241.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/F71BD145-499A-CA4D-BD24-2CF54459F944.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/F0D429D7-AC54-8644-8A6C-C0E16B68D13C.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/9E54B345-6F38-154C-81DD-ED9536A9F558.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/7AB15C87-7872-C047-83FB-BFFAEC8E8CDA.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/015DF345-64CA-D04E-9BD4-C1F97101B3AE.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/3D5D8F92-C143-0F41-B1F5-89C8270B7D20.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/012DAC35-7F39-7945-B927-AA814C2E7650.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/A507AEDE-3B0D-CE47-AD63-5D762AA4BC92.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/2B6022F5-6FC5-FD4A-BCDE-DCBD8FE35FB2.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/24423E19-E504-D94F-9622-FB557AFC0E42.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/F4369856-CF7B-AF41-AC07-151821B5FAF1.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/0B888852-6FA9-F64A-825B-CAA59D96F3F8.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/7D8099BE-5F3D-E64A-BEFF-7FE8225DC443.root',
    '/store/data/Run2017D/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/59C492F7-E91C-2547-A5CA-67D43BE0D5B2.root',
] )