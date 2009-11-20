import FWCore.ParameterSet.Config as cms

process = cms.Process("rpcdqm")

################# Input ########################

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

secFiles.extend([]);

readFiles.extend( [
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/FE863236-45D3-DE11-B3BF-000423D98950.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/FC8F632B-40D3-DE11-8B38-0030487A3232.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/FC0B019A-44D3-DE11-B262-000423D99658.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/FA868F85-47D3-DE11-85E8-001D09F251BD.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/FA76E11C-4BD3-DE11-AA4B-001D09F2305C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/FA2EAE07-4AD3-DE11-8AE9-0019DB29C5FC.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F89691D2-4ED3-DE11-8FB4-00304879FBB2.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F84A5545-41D3-DE11-9170-000423D99EEE.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F81C5083-31D3-DE11-ABA5-001D09F232B9.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F6BE8DA3-56D3-DE11-B71B-001D09F2532F.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F64964D1-2BD3-DE11-B9A3-001617DBCF6A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F648EC18-2BD3-DE11-A68E-000423D98750.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F603A4EE-3CD3-DE11-BFE1-001D09F2841C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F4FF2ED0-4ED3-DE11-82A0-001D09F34488.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F4B7C02F-32D3-DE11-9CC2-0030487A18F2.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F2E6CBA0-47D3-DE11-8CB7-0030487C5CFA.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F0983A7F-4FD3-DE11-8930-003048D37580.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/F0038526-52D3-DE11-BAE1-001D09F282F5.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/EE209D94-47D3-DE11-ADD7-001617E30D52.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/ECD8BDC0-35D3-DE11-8B5C-001D09F24493.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/EA7486ED-3CD3-DE11-9392-001D09F2438A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/E8040B89-48D3-DE11-A390-001D09F24D67.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/E67C5F39-28D3-DE11-8A85-003048D2BF1C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/E65C3012-53D3-DE11-810E-001D09F24399.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/E432439A-34D3-DE11-98A3-001D09F28F11.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/E250BFAD-56D3-DE11-A107-001D09F241B9.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/E0F215E1-45D3-DE11-8870-001D09F231C9.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/E03F97EE-37D3-DE11-8E23-001D09F28F1B.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/DEC58290-49D3-DE11-9CE5-001D09F24664.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/DCFC001A-2BD3-DE11-BBE3-000423D98BE8.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/DCB6A082-2CD3-DE11-8367-001D09F295FB.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/DAD3940A-4AD3-DE11-A08C-001617C3B6C6.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/DAA8999B-34D3-DE11-A0A5-001D09F2AD84.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/DA3747B0-2ED3-DE11-A843-0019B9F72CE5.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/D8ADADF0-54D3-DE11-B6C4-001D09F24664.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/D8634D53-51D3-DE11-92B6-0030487A18A4.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/D8433309-35D3-DE11-AC2F-003048D2BED6.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/D80F7DEB-2DD3-DE11-B7C3-003048D37456.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/D67E22DD-42D3-DE11-9870-001D09F24763.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/D4184808-37D3-DE11-90F9-000423D6CA42.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/D277B289-48D3-DE11-A1B1-000423D996C8.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/D07434F0-3CD3-DE11-BCBE-001D09F29849.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/D05710C8-4BD3-DE11-A5D4-001D09F28EC1.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/CE311EE1-42D3-DE11-9D8A-000423D94524.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C8DCCB31-3BD3-DE11-B827-000423D98B08.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C86DE3D9-53D3-DE11-9579-003048D37456.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C2FF60C9-46D3-DE11-BE9A-0030487A18A4.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C2704AA5-56D3-DE11-98D3-001D09F24498.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C26916DB-4CD3-DE11-B6A4-001D09F29524.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C2559C9F-34D3-DE11-9DEA-001D09F29321.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C20ED89C-33D3-DE11-85B5-001D09F24F65.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C0D2CAA7-46D3-DE11-A3DA-001D09F24DDF.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C07E3BEA-32D3-DE11-AA5E-0030487C6090.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C07A2EA9-43D3-DE11-9E43-000423D98B6C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/C02327FA-28D3-DE11-AE7C-000423D6AF24.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/BEB893CF-30D3-DE11-9247-001D09F2438A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/BE655FCC-38D3-DE11-A0EC-000423D944FC.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/BC4FDC3E-52D3-DE11-9CCF-0030487A1990.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/BA5AD67A-4FD3-DE11-A4B8-003048D3750A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/B842B32F-32D3-DE11-BB46-0030487A3C9A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/B670A7E6-32D3-DE11-AB9D-001D09F231C9.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/B6346754-41D3-DE11-B0B9-000423D9890C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/B46B0D34-45D3-DE11-AF46-001D09F24934.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/B43F58A3-43D3-DE11-9851-0019B9F72D71.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/B22826CF-30D3-DE11-A246-001617C3B710.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/B0D2A5E2-54D3-DE11-9C64-003048D2BE08.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/B09FCD33-4BD3-DE11-AD4F-000423D6BA18.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/AEFE5759-2FD3-DE11-B303-001D09F25041.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/AE78DE34-3FD3-DE11-923D-0030487A18A4.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/AE6DC44B-3ED3-DE11-8C6C-001617E30D40.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/AC09904E-4ED3-DE11-B98E-001D09F27067.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/AACCF825-52D3-DE11-A94B-001617C3B66C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/AA649EA6-43D3-DE11-9738-003048D374F2.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/AA1F770B-37D3-DE11-A09E-003048D2C0F0.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/AA0057AD-29D3-DE11-B7F3-001617C3B710.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/A88F9CAD-2ED3-DE11-9106-001D09F24259.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/A854706B-46D3-DE11-885C-003048D2BE06.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/A234A7F5-3CD3-DE11-8A41-003048D375AA.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/A02BFDFB-45D3-DE11-BA66-001D09F2AF96.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/9E0DF760-2AD3-DE11-8C6C-001617C3B70E.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/9CFC0B9C-33D3-DE11-B34D-001D09F25041.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/9CD8162C-49D3-DE11-BB6F-001D09F24303.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/9CB8434E-42D3-DE11-B530-000423D98920.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/9CB4E32D-4ED3-DE11-B253-001D09F24691.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/9A953BEF-2DD3-DE11-9D43-003048D2C0F0.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/9A0C4643-3FD3-DE11-80F5-003048D37580.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/986FDC0A-35D3-DE11-B6F8-001D09F24259.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/96B71180-58D3-DE11-B823-00304879FBB2.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/942B7C3D-28D3-DE11-90C2-001617DC1F70.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8E874F80-48D3-DE11-B04B-001D09F24FBA.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8E57F126-3FD3-DE11-9A80-001D09F295A1.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8E4B57C9-38D3-DE11-9BEC-003048D37560.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8E00119C-33D3-DE11-BB93-0019B9F72D71.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8CE0DF2D-3BD3-DE11-8A77-000423D98C20.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8CCDD65A-2FD3-DE11-AE80-001D09F23174.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8CBBEA4E-3ED3-DE11-AC5E-000423D6CA02.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8C009E35-50D3-DE11-899B-001D09F26C5C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8AF18F0A-6DD3-DE11-897D-0030486780B8.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/88B4655C-2FD3-DE11-9ABE-0030487A18A4.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/889F6FE6-32D3-DE11-BB8D-001D09F292D1.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/869D1739-2DD3-DE11-A9D2-000423D992DC.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/84D6BA79-58D3-DE11-B482-001D09F24DA8.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8424FD11-53D3-DE11-91ED-001617C3B76A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/828B60E1-42D3-DE11-8E78-0019B9F70468.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/82583F62-2AD3-DE11-9739-001D09F24682.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8234CAF7-28D3-DE11-8391-001617E30F50.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/80BF41CE-56D3-DE11-9AA2-0030487A18A4.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/8088DE11-53D3-DE11-B264-001D09F2437B.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/7CD85830-37D3-DE11-8CEA-001D09F24FBA.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/7AD6C12F-32D3-DE11-A191-0030487A1990.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/7A18B686-31D3-DE11-84C8-001D09F2423B.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/780E0E2A-42D3-DE11-A53A-0030487A1FEC.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/76E860CF-30D3-DE11-9F23-001D09F253FC.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/76A1FE14-30D3-DE11-8A66-003048D2BF1C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/742E185A-3CD3-DE11-934B-000423D94908.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/7417EE8D-44D3-DE11-BBCF-0030487A3232.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/70204BF2-37D3-DE11-840E-001D09F2512C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/6EECE6CF-2BD3-DE11-B501-000423D99660.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/6E6D0225-3FD3-DE11-B6E7-000423D6C8EE.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/6E09817E-57D3-DE11-B30B-000423D98804.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/6C5A9188-48D3-DE11-88BD-001D09F28D54.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/6AF1B816-3AD3-DE11-AFC7-0019B9F70468.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/647E0C09-4AD3-DE11-BC53-001617DBD224.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/607A9168-40D3-DE11-BC10-000423D9A212.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/6075B962-3CD3-DE11-832A-000423D98F98.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/6025B799-4DD3-DE11-B437-001D09F251FE.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/5EC066B9-58D3-DE11-BE48-000423D98868.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/5C70B1EB-2DD3-DE11-8D2C-003048D2BF1C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/5A983732-3BD3-DE11-B989-000423D99896.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/580B8CE8-32D3-DE11-A724-001D09F25217.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/56E5D816-3AD3-DE11-BBB6-001D09F2525D.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/56D4855A-3CD3-DE11-AD83-003048D2BF1C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/5645E3EB-54D3-DE11-91DF-001D09F25217.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/54DF6415-30D3-DE11-8A12-003048D2C0F4.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/541856C9-38D3-DE11-8C0F-001D09F24EE3.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/50BEFEBD-35D3-DE11-9B58-003048D374F2.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/509EC4D8-4CD3-DE11-8D0E-001D09F24FEC.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/4C0E8BA0-43D3-DE11-A94B-000423D9939C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/489E90D8-4CD3-DE11-9712-003048D3750A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/44CFD52D-3AD3-DE11-A344-001617DBCF6A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/4083FE39-28D3-DE11-A504-003048D3750A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/3A3140AE-29D3-DE11-A0FD-000423D9890C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/3882B506-35D3-DE11-9FC3-001D09F2841C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/383643DF-42D3-DE11-8B70-001D09F26C5C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/36D0DC3C-45D3-DE11-94B4-001D09F253FC.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/3453ACB8-4BD3-DE11-9AB2-003048D2C1C4.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/343770D1-2BD3-DE11-B517-000423D6B48C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/32C73B3B-45D3-DE11-A467-001617C3B6E2.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/3270DDF3-2DD3-DE11-A344-001D09F2438A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/32604A4B-51D3-DE11-B245-003048D2BF1C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/30811B71-4FD3-DE11-BCC6-003048D2C0F0.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/2EC5BAC2-35D3-DE11-9955-001D09F29524.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/2E04CD6B-4FD3-DE11-AE40-001D09F2424A.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/2A48FFCA-46D3-DE11-8640-0030487C5CFA.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/2A3FD062-55D3-DE11-BDA6-001D09F242EA.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/264EEFBA-4BD3-DE11-A453-001D09F28F11.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/24A0405B-55D3-DE11-86FA-001D09F29619.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/247849D6-53D3-DE11-8A64-001D09F24399.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/2403C182-2CD3-DE11-AB89-001D09F2AF96.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/228D7C1D-2BD3-DE11-9B5C-000423D8F63C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/1EB33A30-42D3-DE11-919A-000423D60FF6.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/1CA5E734-2DD3-DE11-AF07-000423D6CA6E.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/1C9FAF82-2CD3-DE11-89FC-001D09F23A20.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/1C4FC419-2BD3-DE11-BBF6-000423D944F0.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/1C02A4F7-28D3-DE11-A061-001617C3B77C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/1ACC062B-52D3-DE11-A38F-000423D9890C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/1A78EADF-35D3-DE11-BC04-001D09F24FBA.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/187E315A-2FD3-DE11-A309-001D09F24691.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/16FA0B35-2DD3-DE11-9008-001D09F29524.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/16849945-55D3-DE11-9659-001D09F251B8.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/165BCAF1-37D3-DE11-A96C-001D09F28EC1.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/1617AA2B-49D3-DE11-AADB-000423D98C20.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/14FB5549-3ED3-DE11-8CBC-001D09F2305C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/122122DF-53D3-DE11-9494-001D09F27003.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/10B75935-50D3-DE11-AECD-0019B9F72BAA.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/0E06E6E6-4CD3-DE11-B42A-001D09F27067.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/08653B30-4BD3-DE11-BA75-0030487D1BCC.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/08334FB1-29D3-DE11-B520-001617C3B5F4.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/080595C9-30D3-DE11-98CD-001D09F24D4E.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/04FA9F7D-58D3-DE11-B520-0030487C6090.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/0492DB13-53D3-DE11-AC8C-001D09F23D1D.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/047C6488-57D3-DE11-8D35-0030486780B8.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/045F0C7B-57D3-DE11-B63F-001617C3B6DC.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/041E2DF2-37D3-DE11-B039-001D09F28E80.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/02F9DE30-50D3-DE11-B38D-001D09F2516D.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/028C82A4-46D3-DE11-B3AB-001D09F34488.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/026509AD-2ED3-DE11-8E74-001D09F2841C.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/0259AC60-2AD3-DE11-BE9D-001D09F29849.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/02576D81-31D3-DE11-ACDF-001D09F2983F.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/024E72EA-4ED3-DE11-AFA2-000423D98950.root',
       '/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/121/238/0057A671-41D3-DE11-B62C-001617C3B6FE.root'] );




process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR09_P_V2::All"



################# Geometry  ######################
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("CondCore.DBCommon.CondDBSetup_cfi")

################# RPC Unpacker  ######################
process.rpcunpacker = cms.EDFilter("RPCUnpackingModule",
    InputLabel = cms.InputTag("source"),
    doSynchro = cms.bool(False)
)

#process.load("EventFilter.RPCRawToDigi.RPCSQLiteCabling_cfi")

################# RPC Rec Hits  ######################
process.load("RecoLocalMuon.RPCRecHit.rpcRecHits_cfi")
process.rpcRecHits.rpcDigiLabel = 'rpcunpacker'

################# DQM Cetral Modules ###################
process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")
process.dqmEnv.subSystemFolder = 'RPC'
process.dqmSaver.convention = 'Online'

################# DQM Event Summary ####################
process.load("DQM.RPCMonitorClient.RPCEventSummary_cfi")
process.rpcEventSummary.EventInfoPath = 'RPC/EventInfo'
process.rpcEventSummary.PrescaleFactor = 1

process.load("DQM.RPCMonitorClient.RPCDCSSummary_cfi")
process.load("DQM.RPCMonitorClient.RPCDaqInfo_cfi")
process.load("DQM.RPCMonitorClient.RPCDataCertification_cfi")

################# DQM Digi Module ######################
process.load("DQM.RPCMonitorDigi.RPCDigiMonitoring_cfi")
process.rpcdigidqm.DigiEventsInterval = 10
process.rpcdigidqm.dqmshifter = True
process.rpcdigidqm.dqmexpert = True
process.rpcdigidqm.dqmsuperexpert = False
process.rpcdigidqm.DigiDQMSaveRootFile = False

################# DQM Client Modules ####################
process.load("DQM.RPCMonitorClient.RPCEventSummary_cfi")
process.rpcEventSummary.PrescaleFactor = 1

process.load("DQM.RPCMonitorClient.RPCDqmClient_cfi")
process.rpcdqmclient.RPCDqmClientList = cms.untracked.vstring("RPCNoisyStripTest","RPCOccupancyTest","RPCClusterSizeTest","RPCDeadChannelTest","RPCMultiplicityTest ")
process.rpcdqmclient.DiagnosticGlobalPrescale = cms.untracked.int32(1)
process.rpcdqmclient.NumberOfEndcapDisks  = cms.untracked.int32(3)

process.load("DQM.RPCMonitorClient.RPCMon_SS_Dbx_Global_cfi")


################### FED ##################################
process.load("DQM.RPCMonitorClient.RPCMonitorRaw_cfi")
process.load("DQM.RPCMonitorClient.RPCFEDIntegrity_cfi")
process.load("DQM.RPCMonitorClient.RPCMonitorLinkSynchro_cfi")


 ################# Quality Tests #########################
process.qTesterRPC = cms.EDAnalyzer("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/RPCMonitorClient/test/RPCQualityTests.xml'),
    prescaleFactor = cms.untracked.int32(1)
)

################ Chamber Quality ##################
process.load("DQM.RPCMonitorClient.RPCChamberQuality_cfi")
process.rpcChamberQuality.minEvents =  cms.untracked.int32(1)

############# Message Logger ####################
process.MessageLogger = cms.Service("MessageLogger",
     debugModules = cms.untracked.vstring('rpcdqmclient'),
     destinations = cms.untracked.vstring('cout'),
     cout = cms.untracked.PSet( threshold = cms.untracked.string('INFO'))
)


#process.Timing = cms.Service('Timing')

## process.options = cms.untracked.PSet(
##          wantSummary = cms.untracked.bool(True)
##          )


############## Output module ##################*_MEtoEDMConverter_*_*
process.out = cms.OutputModule("PoolOutputModule",
     fileName = cms.untracked.string('out.root'),
     outputCommands = cms.untracked.vstring("keep *")
)


################# Path ###########################
#process.rpcClientSequence = cms.Sequence(process.dqmEnv*process.readMeFromFile*process.qTesterRPC*process.rpcdqmclient*process.rpcOccupancyTest*process.rpcNoise*process.rpcChamberQuality*process.rpcEventSummary*process.dqmSaver)


process.p = cms.Path(process.rpcunpacker*process.rpcRecHits*process.rpcdigidqm*process.rpcAfterPulse*process.rpcMonitorRaw*process.dqmEnv*process.qTesterRPC*process.rpcdqmclient*process.rpcChamberQuality*process.rpcEventSummary*process.rpcDCSSummary*process.rpcDaqInfo*process.rpcDataCertification*process.rpcFEDIntegrity*process.dqmSaver)


#process.p = cms.Path(process.rpcunpacker*process.rpcRecHits*process.rpcdigidqm*process.dqmSaver)
