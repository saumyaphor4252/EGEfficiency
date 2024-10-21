# L1T INFO:  L1REPACK:FullMC will unpack Calorimetry and Muon L1T inputs, re-emulate L1T (Stage-2), and pack uGT, uGMT, and Calo Stage-2 output.
import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.CUDACore.ProcessAcceleratorCUDA import ProcessAcceleratorCUDA
from HeterogeneousCore.CUDACore.SwitchProducerCUDA import SwitchProducerCUDA

process = cms.Process("HLTX")

process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring( (
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/451a30f2-dd30-4098-8d42-1f2e365b87d4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/ede448c9-6468-4889-872a-af2febd69640.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/18e83c84-42bb-4ecb-87c0-d7f8a67a5ba7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/ed2a7a3e-5031-4322-addc-0df34a451603.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/45963f74-6a4e-4690-90b7-e6c7f6452f22.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/750589b4-af7f-403e-970b-217dfb6aaa7a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/e721fdf8-aef9-4750-bf61-678c55017181.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/5d7fede3-2882-48f7-9018-ec4d2dc9ed17.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/24cfa3ab-f41b-4171-855f-7e9fa90dd950.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/d90f00d8-fc7d-4707-9cad-31f4b0a6ada6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/8622631e-ceb9-414e-8b7a-74427c252a6d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/77252871-59d4-4c9c-be37-bb3ccf5da3a0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/fae89cd8-3d35-4a67-965e-e658aa740a5f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/613c9acb-b61c-4a84-82f7-ec9057225658.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/023a4008-d846-4048-8411-01ed9451591f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/c1ea2053-3d27-422c-955b-10dc510789dc.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/0454c31a-d23d-4c9c-acfd-f7427d8a0e3d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/ed0bd8d1-84ad-4c20-9ace-9e075222007c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/71f9a6d5-c319-45c7-aec7-6c4da07896d4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/537f46d7-cf10-49ef-ad30-ffa9098d3a25.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/a5d237b3-b68f-479f-9082-36ee08384c8a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/fde0ba54-d38a-49b4-b1dc-fbae08febfb5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/856477b5-c4f0-4735-8c1f-856689be43f9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/88b4595b-de58-44d0-b02e-3ead307f9f4d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/ec81ec4b-71b1-4874-a13d-8468dc8be371.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/05f495cd-7510-4224-a10e-c45ec60be67d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/074b36e9-4351-46c7-9b86-51b1fa80997a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/d79ee130-36e6-43e3-8fdf-dc97a04c0dc0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/1022d96f-1975-405a-baaa-467bc2fae41e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/d2ad8053-8484-4f3c-b7e6-3080fa9fcbf3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/18f9d5de-3272-49bf-a4e5-b2b2fbe24ba1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/cec6faae-bfe2-40c3-906f-0783cd409c65.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/c08420f2-74e0-4651-84de-a47b410111f7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/bd58ebd5-33b0-4c7e-9c82-019e63aad017.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/3b2b37f9-5ddd-447b-9b4a-b62d14dc0e92.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/7c89b35d-79fa-405b-887f-7927ec1cd48a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/175a8bf6-1592-4b8e-9ae0-5aa42b8bcef4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/9a1017b2-de50-4fce-8c8d-c9f06492b21e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/b0aa983b-b7ad-4828-a38e-2a31f5c3fe4a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/87a11582-78ae-45d8-bf63-81d016b2730f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/b1c88948-33c0-4ec4-bdd6-ef4604523e34.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/0bdc64af-c5e7-4879-aebe-fc864fb476c0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/a69e751f-ecae-44da-a74e-4900aecc5f43.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/48130b8d-ec88-444d-a765-1153a6b59484.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e552fbd6-cda5-4719-82a6-88290e0a7623.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/741322ec-8e9f-4d59-9a92-89fc74863216.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/85eb6d2d-bf60-4c04-a52c-b3916140c4db.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/529c06ca-c9f3-45c7-99b3-0c1581d402d3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/f4fe0a05-3ab3-4631-a5f7-6f329f4b062c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/f9bd85be-cc40-423e-b4cc-a09aabd4a8ca.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/614b5150-ec6b-4d75-8a14-d0badd5ed18d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/94814a96-7062-4194-9d04-18f24efa7787.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/7fa96ca8-3be4-4411-a5d3-e5158c9f9c6b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/e5d9dfc7-b8a2-4977-9b4e-679d2db38697.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/d76fc5a4-a20f-4c1f-94f7-d642954445d1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/67f2e76a-57b9-4471-9a82-33c57be0714a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/cb60e9b3-6cda-4e8e-bf41-de4ec66f770e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/9440c704-1e11-4304-898b-ed2bfa0ffce9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/64ac3368-9a0c-4b60-9191-036b07c7219e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/d7ee1046-efed-4f09-bc5e-46b2a8f4f732.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/9ad97756-c954-499c-aba1-4672b91eb001.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/4d467c21-7b0c-4768-9b78-19e65bf97c9a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/b0cefbde-f8e0-467a-b6cd-f30cb5406582.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/4b0483f4-0f06-4721-a74f-c8f7147d3274.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/24e07a29-25fb-46da-bfe7-4bb96aa54d37.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/0eaa3036-42e8-42f3-af02-fb810f4a3204.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/1b971925-af84-4532-8277-dfb2ab303ae4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/fafe98f7-a18b-480d-bef8-9319b3881e5b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/fa325390-334f-44e8-b61f-8b289e85ad00.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/f4e6d58a-a058-4cdf-a1b2-aa7608feb7a1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/c8fb83ec-64c9-4187-9d78-046e2e1c2be1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/abcbb43b-fb33-466f-a983-20ae0f439d70.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/92db74ab-bcb9-4e50-aff8-a09b44e9bb43.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/8684e0dc-bde1-454f-a29f-f5c92eabb476.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/a206ba33-f783-4a77-a9d7-39423e37b445.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/5a129078-2abe-4187-8f4c-341a92390f8a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/6a9292b7-f694-4f39-8f1e-8f0601cf7662.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/0a58a79a-ea66-4afd-93e8-be9ef4a97bed.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/f77e2565-4429-400d-bee4-5180685eec6f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/88a9aa67-d2fe-4623-a9cc-9ec85322f640.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/fa2952ca-57d6-4263-b219-372cc27ad675.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/3bc4ca08-cfe0-42c7-b093-0f543d719da7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/dcdce460-b4b6-44c1-b330-e81fdabda4e0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/30dc607a-1986-417a-818b-4d48fad2bddf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/115583dd-e66d-42b9-b8f8-89e8fc842966.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/80a9a246-001e-43b1-baf3-26439fd99f2d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/0a7d8700-6b03-4d4c-a4cd-36fde928944d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/aba85662-8112-498b-8877-1f664a2a5473.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/db763295-a932-4cd2-aee4-18b83bf4c033.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/052e9321-74d5-42b3-a9ff-542aa7a17b83.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/aecddf08-fb64-4a0e-9c96-3d2f57b1bb97.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/97283c64-d038-4e42-9473-6398165426b1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/3b467a58-cb8c-43a2-9f32-c2a19fc7d83f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/2d72fc9d-e418-4143-bbb7-f1214316e9ce.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/61b46d64-260a-479c-b1f1-71e9a62c7cf7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/41cb9ee2-42ff-4c17-958a-ab60a3e6e75c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/ca605640-bdd0-476f-95ad-cb199bcedf9c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/f68da211-fda1-4ecf-9bdb-6d9c25770c99.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/81c03599-9bc4-45ab-b473-72a26c2ad3db.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/2d8ebcb0-57f6-4169-b005-cbee10d0f3f3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/aa378360-e58a-4523-abb0-8d6518c533b2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/da094d1f-4ff6-4609-9937-8b58290270f9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/4d02e344-74a4-4586-9914-3eadbe3245e8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/8d41934f-fdb0-4611-9cf4-1cb894323c40.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/1efa26bb-477c-4e2b-ae76-806f1985ee07.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/9854cab8-610b-470a-9d04-b00b148ac0d5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/168c17ce-c6ca-4970-b5b9-d32f359e3883.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ad52e114-5f5d-424e-8ede-fe7591fb0a8d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/1014876b-343d-47b2-8ec9-54335cab4c5b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/2de112bb-b4ad-40dc-b4e6-fbef588e7b4e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/7878ed23-f8a5-47ac-8c3c-df5ec2bc9ba3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/0b01f5fe-521b-4be6-9374-f20f9d7ea42d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/32967ffe-1a78-43a3-9f42-24c009d26ca8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/c260648e-77fc-42be-9815-ed124bbaad99.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/b327f203-60cc-4a0b-9bca-8414585053af.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/0be2815e-4d46-401f-a98c-57b36847246c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/1b996899-81a4-4404-902b-2ea724fdea07.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/2858eec6-a339-4664-8f46-129f48df0dba.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/c69127cd-8a70-4344-9c56-3b246a2a245c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/2a51be69-4096-43e9-9d64-2fabe5a1125a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/af5d9952-93b7-48ae-b748-3fb774d2c662.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/fd0bfa1a-e6d8-4657-ac3c-5d3ec961fdc8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/f6e31fff-b887-45e3-ba5d-041703dcf764.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/e964f52f-197b-47f7-960e-21266b1335de.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/80c15e41-3f01-4a2a-8777-5acc54a94386.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/1cd6a36b-0f8d-4c70-9645-6d6c28253538.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/92647d0f-19fe-4e86-80ce-4632aeb29f1a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/d9c9dbda-af5c-4394-8641-d09154d25f8d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/b3de111f-3313-4e95-90de-1202b9aa18f8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/7c318544-20fd-4067-b9fe-0dfcef0d7db2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/eac53c1f-339f-4e24-a5fb-c41b2d1e98b2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/48471fe6-b541-48c9-bf14-b1652f330b6c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/581576c1-ab18-480a-920b-4ae4bbd2b8c5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/cf5e09df-c332-4ba6-ba80-04f604758cb8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ef3a02b7-bbcc-47a2-85e6-25cba7e5f113.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/57aa98b2-79aa-43b2-834e-699bb33b84f7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/7c684b08-a89c-4c18-b441-df913a4711ab.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/c505389c-eca2-4949-964c-07e7b947a6aa.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/ab02734e-cff8-4205-92d8-4033c71714cb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/4248ddc5-53a5-450e-8a14-a003e4690bfa.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/4edb7445-b1b8-4cac-b592-42e31e14be2c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/240ef2c8-928d-4f35-9376-9af14ae930eb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/627fe98b-f547-4666-ad50-cce4bee51400.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/c816f37c-beca-4831-a95b-3e9c6dd82e1e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/ff51e115-4476-4a9d-849e-cf3b320bcdc0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/2e581b37-9062-4231-af23-a3c7c477042e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/a811f2bc-44a2-4803-8a37-7e67900a0a30.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/9036d367-1071-4def-b8b8-5df6a70d8166.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/a2a2b264-e533-4bd2-a77c-d20331b9f280.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/3c1b98b7-3aec-40d4-992d-d5a759372a32.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/9e44c461-f25d-45a3-8cfe-e24c785b826f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/de8a3a65-4e97-400e-970d-b122314d3fce.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/3e687044-8f91-4a1d-9ded-b7d46d5bd69d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/1a04b094-f2f5-40c6-aefa-72086a159787.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/2a7c7cbe-10bf-4427-9618-47f12f6fd687.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/60e5a29b-122d-42f4-89ac-77358fdece9b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/0a55cd30-215f-457b-94d8-7f63a448f578.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/d161ebf0-eced-466a-babd-c32f678800c0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/25ec06af-2114-41f9-81a4-5dbc52160093.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ccf83ef7-47bc-440f-8489-1cd7d0ccbb4b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/da4e1347-078c-4d40-aae5-1d02e5a74060.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/92d66ce7-1d36-44e5-a612-6ad8362b8443.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/96f3da10-7ed6-4fab-a32e-7054669524ce.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/f80f93e2-5933-40cc-bd99-c9def1e5120c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/dcd54b94-8a5c-4abf-92d9-aba982c5de01.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/4b8c8bb1-177a-424d-9733-e438963dfe48.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/c2d840f5-316b-4809-9193-ac4223bfea43.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/f5556a8b-71d7-4e46-95e7-cd6dcaf46224.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ec419e7c-da9a-4897-b786-d93793506798.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/9a40addc-86e0-47f2-aa80-d47e9b0817dd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/3d105a27-84d2-476a-ab94-eb1cd4a065b1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/4d7e8c07-d1e8-446f-869c-9e9c44a17b2f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/5e3d2292-f573-48d0-93a9-1b13c774caf0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/c610bf6a-73b6-4de1-9b55-33d327dbb3fb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/8c12036a-2f9b-4bab-9587-1a08aa6e2ee7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/31e2acb0-a10c-401e-8f0b-11a51a4421d3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/14037ce4-675f-497b-ae42-b79742693759.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/f29512d6-9395-41ee-b59d-1730a3014cfd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/045dedec-cd87-4856-9b89-02973e2f5b75.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/4edc085a-839f-42a4-8bfe-1dad282122ad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/d91d10c9-11b9-4db8-a4c0-f35d60767855.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/0a45892e-c714-4344-bcbd-76238fa90e6c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/c93dd83c-b59f-45b6-8e84-dc1d9f38bb8a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/25b64447-fc63-4a3c-9a73-854a8303de00.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/a7acd480-7191-4f28-8d70-83bc67725df2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/c33fc21a-2623-4ef4-ba78-807a9941a37b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e3d04e5f-92f1-4766-9a47-2dc4a135d67a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ab1938e8-61ee-4289-8874-b5523607eee7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/d8a19980-75ab-40ef-946f-9352809fcb67.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/9243b023-8eb7-4ed8-aeee-e9af24e467ec.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/3c3dc107-3343-41fd-a58a-a4210e2e97d5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/244007d9-fae6-419f-9609-4cfec9bbb411.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/372a4ab0-976a-4436-a5dc-00c4f954c963.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/e1d6d593-7ca8-4bc4-96dc-5a7b5d642a95.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/8833f254-5564-48b8-84b7-613e46b64cdb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/61a6d576-2a06-421a-b1a8-ac7e26a22f73.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/b1a03e6d-3fd4-4866-a150-7a492e6371b0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/11f80a11-ba5f-47bb-92ba-add3a2f660cf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/337e6fd9-d3f1-4224-a2d3-642652f2e122.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/c6f5487a-c86d-421b-a2c2-ebae8d71d20b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/5d9dc7f2-34b0-4e22-a1c2-1d8c0034387e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/98887a71-a16b-4a84-b465-46a10b79455b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/e2d68400-927f-4dab-918d-0de51deaf7ca.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/0ab25788-a824-441f-8e3c-e2d83cca4d4a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/d71b1e1e-31e5-43c8-b32c-33b2ce04d23a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/6ed4f1d5-d919-4bca-81f9-9244048b1f03.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/100fa376-7c08-4ac9-9499-473970cc058d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/46d1c780-1d55-4000-b4cc-6d637f1a0599.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/b538ae77-9be0-4dfd-870f-31e117148c66.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/15735345-063b-48cf-aeba-958d0521deff.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/1710663e-5e32-4735-a34f-8bfb66a64f62.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/20da687d-a15f-4158-8f21-695e6f0677d2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/26e34d83-9eda-4286-b83b-16eafb548bf9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/04e44fbb-c1cf-4710-97ea-de439e912463.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/861bcc40-553a-493f-bbb9-a5432f2617ba.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/67c42748-e583-457e-9518-4ba8cde9491f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/fba6ee53-4ba1-4f4c-ac10-1691d8165c3d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/b8ec3f61-b479-4cac-acce-b5b5ff67c5c2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/16d3315e-589e-41af-9c37-2d3246f4ea09.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/8c99bc61-938d-4a89-a805-d50bf376c863.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/66a8c841-9f3f-453d-b43f-52cb9702955e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/18aa1e0c-bd6c-44d2-aaa0-5784fde88550.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/80965bbc-0361-49d3-85ae-e44dece26102.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/9eb0f1d6-f262-4594-8f54-a6b30cb7a6a7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/72ea95ff-51ba-4917-8062-59e06552943c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/3751a016-6f0c-4ddd-b1a4-40052efd1cc0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/69d23215-e992-49b8-a0fc-487e67b10c69.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/70232696-d3ae-4ac3-b949-7fdea879be2d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/617e9dd1-6706-49e3-81c4-416d2488efdb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/5ef1f685-005f-4d37-bb6a-061b4a9b7fad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/e5876d62-5e5e-4b64-a819-f38478f9354c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/7553d56a-9f66-4515-9e8a-25d5d86b8296.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/0b19ef1b-21af-4182-bc67-8fc910429df9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/5d5db9e0-b9de-42bc-80ba-9d3df9b2f301.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/bd93e54e-6c63-4973-9847-6d43b51d2120.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/09cf75d0-380e-45f9-92da-55b56074f454.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/741d96ac-c720-4d97-9c47-9083e03dfb4c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/577b0545-9aad-4cb5-a22f-0f60de142519.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/cd0860f4-60dd-4aa3-a663-3a4c5d6d7680.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/56f62a0a-1767-4de8-a2fa-e59a54cd6153.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/813564c3-58da-490e-858b-f8de5d531869.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/187efc0c-3127-47d0-8e93-a3cef6d7906d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/2a11bf5d-1c6b-4855-9fbf-949355df7c8b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/60118b16-4b93-44dc-b778-6b9c0916346a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/450fc6fe-96a4-4200-bfa7-0eb0954c56fa.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/bfb30ae2-0dbd-4584-9f11-ab3aa72524b3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e10527c6-6954-48fd-9d3d-77c2bf197a9c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/e255efdb-5f87-459f-83f6-6cd6a261b4b0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/73399d90-f94e-4742-a539-75fd9770aab2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/74883258-c422-42b1-93c4-3850961ce6b1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ee17c58c-aec3-4cb0-9993-8dd43be18390.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/d8d38f93-becf-4f78-8fe0-11284a6796ce.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/6c9a8337-8a70-4a19-bcc9-f58e9b08dd80.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/13ae07da-b0f0-4869-bb9e-988fb2a0d774.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e1e25df4-cd74-4a5c-8146-a4010548266a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/31a08191-254d-4a0f-9caa-73a48f7e61ee.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/35398ba9-6e51-4b3d-b0b7-c404b7b6008f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/6d14abec-194a-4be1-ae62-f31d99dfcd14.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/5980f8dc-a47c-4f93-81bb-e27bf3d2e3c2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/f0d83960-3c99-4f26-956b-722458730bec.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/92ec50ea-ea49-4759-af1f-48c31a3ffee7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/790501bc-872c-4636-938c-80afdb7a8045.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/073e3dea-aa90-4943-b875-bcdcd235a629.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/315d9b17-a328-4a8c-bf49-0ec5b08895d4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/6dda11dc-f164-4f0d-af8e-742e22fea388.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/b9fcb882-8f6d-492b-b3fc-52bab08d3d4e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/503387cb-1eb3-489b-bda0-da87373e3847.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/8e13a4ec-0255-492f-b297-f4d3e2f123c2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/17a9fafd-28af-41ca-ad4a-94e7f077a308.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/5c4b06fa-4be3-4b74-9444-bd7e1e7d8ffa.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/6b65a2d1-b2dc-4c87-b31d-54f81a0ac075.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/34c2fb42-03f8-4b8f-81da-783c4e26541f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/d19526f9-8900-46e1-9a09-7c285bedfef1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/a9547b5d-32f0-43b9-b0d4-10e298bdadfe.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/f08a1f0e-45d8-4170-ae99-1557144d6d68.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/74647881-8d96-4696-987a-e6abfb8d6f47.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/9a29b1a9-fb6a-44dc-b0dd-bb0462f463c6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/9d4031d5-4727-4910-864b-9917f1448472.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e7c48f54-d556-4f04-b61c-a785c7c93933.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/dc5c8ba9-366e-4097-8150-61db24a65522.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/ab971a25-e279-43d3-9310-eda42e74e07a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/c7e2042e-088f-43bf-8905-ce6bfa50b4b4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/83940a28-3b12-42bf-b9c1-aa6285b01bad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/0aa22e54-d6c6-45b6-a8e1-195cc8599018.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/d6e79991-adb1-4bff-a5ff-48938a015424.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/98f1db3b-f338-4f26-89fe-eb9d70168dc6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/03cd8bd3-bbd4-4723-a075-9993ffeec93b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/d9840c4a-f528-4cd9-b246-aecc365668d5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e1626787-1295-4c9f-99c8-0230d024f9c4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/cbc0fe44-2471-440d-874b-df93c8d9598f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/4bc636e3-960b-4ad8-80b8-cb575c3ea47f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/19ba2186-47ed-4f43-8893-74a19261afd2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/62c9dea4-bd7c-43d5-9e9e-9b1a89d35c85.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/69e8b88b-8525-46cc-97e4-29d5424fa44d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/b4ed55fe-7429-44b4-a199-42a6724938b9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/076f2465-881f-4c71-9861-cfd00be53d4d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/3e654e51-7f39-4915-ab1b-a75cf344afc4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/dea4d0ff-f688-487a-8de7-5876ea53615c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/7a491071-92e3-4ce3-bc37-85d0231dc1fa.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/ac73c6e5-dc49-4d76-aaf3-d85784ab4dc0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/5167b6f2-7a26-4e67-94dd-b82c05dad599.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/32cb161f-f3bc-4dac-8fdc-7db3a24e332d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/526d2aa3-975c-43f3-b140-d395d1f238dc.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/51ebd56e-12fe-43e2-91ee-cc7d6a7d5e31.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/242b61ef-c20e-421a-a649-a8d8e0aaacc4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/3f5fa3ab-561f-4da9-83b2-4c73a51fe905.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/7d54b3b0-14d0-4cdb-8acf-85ab86e0695e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/0d748b63-dd25-42df-ab67-a27f1a22fbb4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/cb8191d4-3262-4c96-95ea-5e259c2f34f4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/813dee9f-b203-4778-bb35-9383d188c05e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/65653ebb-8ee9-4b92-a290-886e125c9359.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/8aa8b5b6-c068-41c4-9505-871f7ff89686.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/db27e035-ae75-42c4-a28f-0888e73ce025.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/8c70ff9f-68ba-42f3-843a-1c360b9538a7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/55b6e611-ac82-4baa-9f2e-8cf808781974.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/b04af790-7db9-4a74-b43f-ea0546bec71e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/9b480e79-bd69-4969-a738-5bd6a00eb9ea.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/eb34a2aa-8614-48c1-afef-acfd3903a080.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/b9b87a3a-3dc0-4843-9f03-6a52d762eed1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/911b6632-e1c6-49e9-ba5f-1ac87fb2d3ae.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/3c075074-9451-4ce6-abf9-e57b437c8f60.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/72254145-110d-4a78-bbde-2b0290a1e357.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/2f17f153-59f7-4512-9c53-92ee58b20a18.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/4389baeb-d730-4cdb-b3da-929d97291994.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/19f501ea-18e7-43ae-83b4-48814855ec1e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/6f5e486e-5dd3-4e38-9beb-a2a0df3efdb8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/341e9717-a0b7-4127-8128-d5c4277000de.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/641934bd-0aef-4c78-9c1f-fe4cd42ec9d9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/0e26b9ec-ca70-4f9e-82fd-3f41bcb5fd65.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/c16180d2-a678-4561-a7c4-ac45da853a1e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/1d56822d-3546-446b-8bcc-e8e61e6458d6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/379a0e69-a5c2-4441-9533-b78a2b18ebed.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/40c59d9c-3eaf-41a6-a1c9-3ef90d6006e2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/8d44a54b-72f6-4272-baca-729a0936321f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/fcc7c7d7-cbca-48cf-ab12-c7a085f277bc.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/f3d44444-a7e3-404e-b3f6-505e653667b9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/7fb75e49-a193-4a72-9333-fda2b7b64edf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/94337cbb-b0c5-49b1-9573-97cd4c42e327.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/ae9a05c5-6f15-45ec-a47f-a249f324248e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/0db135d0-8441-475b-94a2-ddbfa1cce699.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/f304cc76-6cd5-453e-955e-ddbace9f5605.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/09d1e8cc-f308-4b08-9869-ebed0f5a7d93.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/e9e7f074-c14f-47b5-b2a4-0b21f114a84f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/67fea125-1661-4b41-bda2-ef4d730c0239.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/957a1513-e4e5-41b8-89e9-e74c71df3e0d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/185ff7f5-5244-46dd-a5a0-d2aefe2e0ef5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/0652c782-55f3-4981-b0e7-d5a66e343f56.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/ab4552c0-508c-4a51-8556-c6449c55c936.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/7bd48db2-508d-4166-9e50-7f3d30d20e6b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/7f1e5308-1223-4cc2-9d29-10706c0747ee.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/5e9f7b74-5828-4cc8-88d7-e73ae41a2c01.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/9756842b-1592-42c4-ade0-9d5c393999b5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/72de54a6-0d2d-4090-a762-e9c3de209866.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/af919761-64c8-4d5f-bcb6-cab832d1e79f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/857d6985-3b11-479a-ae44-ab382c696f82.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/623cff42-aeb2-4485-a1d2-2f6fbe2e570e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/7b6ddce3-0067-4f79-9708-6c838ee35146.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/16be9c1c-062d-4c20-bd39-84788bb36b61.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/4337fc0c-3377-4a2b-9e49-9b63e514b49a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/534d31fb-51da-4b58-90d7-7c5e5e57e712.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/01485d6e-6390-4739-a8fa-abeee96300b1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/910cf61e-4134-43f5-bf8e-7e1764faf5f3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/eb1f5cc5-e7b2-4c58-9c86-ed24089cfbb1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/01ff8dc9-e24f-48e0-87de-91acd06f0119.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/52fd553b-ed02-4696-82f1-ed2cc5c84614.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/1f545cf5-7f63-46ae-a1b4-3a58bbbbf252.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/c740e4bc-1117-4d21-83b4-ec4f08c9e9f9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/185353d1-92e7-4dfa-a492-ce72e9b41621.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/27061fb3-79ae-4406-9cb4-624508e9499d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/4b6e2854-c736-4b8a-8319-a5e0aead0fbf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/88b734ca-0672-4f45-ad49-13655c801af1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/b9034b32-0d1b-421b-8276-90f968bcd21e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/045aedc2-dc63-4e9f-ac9a-1bfd6b28829a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/88aba3bc-bb7f-4656-83d2-eb4f84b4522a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/55dbf03b-e8cc-4d96-99b6-7f8183ad5a47.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/0920eea8-43b9-4979-9709-d8b92ac335c9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/2ce32470-b25f-4df3-928e-52c0318bac2c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/55037614-6d69-46fb-a32c-4045654a1a5e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/935c0deb-ea48-403a-b5cc-a6e282cd5147.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/98a787e6-64a6-4863-92bd-640862af5e53.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/3d94b6c9-e895-4a74-a004-c77ffdd30387.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/3b1e54d3-bd9e-4546-8dc4-b8f035903b51.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/b5d56147-2f25-4ad6-901e-075fabbde673.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/a543f5e4-d700-462b-b9e3-bf9802e2ecd8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/16760ea1-1b20-476a-b9e4-821a48837898.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/4607fa2c-3d60-466a-83fe-ec89b3a25bd9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/1fa8a3b0-a15e-49ce-b2da-597731bbe875.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/48c6484a-ac4a-4e1c-b1a5-df03c6639459.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e99c8b82-1e59-4608-9a1d-7d556a79f972.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e1191c6e-823f-4194-a504-e82eeb2c6c91.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/8346a09f-1d11-489c-86bd-5d1ea49c6c17.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/a7e6eb66-e1a1-409b-bd2c-7339923910ed.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/ba09085c-e6af-4cd1-a80f-f5fd72b18897.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/b49f42b9-c95c-46a4-9ebc-d940511ca4f9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/d67dc617-f801-4275-a67f-b46f36cf9656.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/a9ddf2b5-7e98-46a2-8e41-7d9769b92858.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/f60cf8e8-a223-4e7e-a31e-0847d585873e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/c33efd03-25d2-4329-b730-49d770e59edd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/12c7fc09-d71b-47c8-8eea-ee9fcb593bf7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/8e5424a2-776c-4468-9a20-e41141cde88e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/8998a9b7-d22f-4848-bcef-ab8cccc49fd2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/23043f5b-a639-42ae-b6c9-2f1180691c93.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/2ca1e3c0-93c5-4320-a983-debd21d73b5d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/3367c837-9f48-47c7-ba60-28bd8007e270.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/bfcd6679-37e9-4896-9811-31e4e4816c20.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/a820e8c8-af97-4f3c-b3d8-d0b4cacc00c1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/b29b678e-641f-474f-a565-c88d9ad72682.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/4c7a281a-ada9-4873-b6bb-bfdbfd79325c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/236bcbca-f0d2-4c64-aeb5-79613949a44d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/9d6e9f12-4e4c-4472-93bd-ac83d33ec46b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/7e1a3a1a-3349-4a07-86ea-3fd3205ab0b9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/dcbbc111-390b-4f05-813c-e4e2574cb9b9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/32fbace0-ce3a-4ecf-8cb7-6fcc89041a9e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/89d3a13b-92a9-4d49-894c-76919b653e89.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/0e3f0beb-0c8e-4924-b176-03249c94e05c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/abee095b-150b-4941-bd63-ba4c9b045770.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/b07b16f3-da47-4c8a-a85f-8ab9782058d5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/cde85b13-dfda-4331-966e-d7f09ce67dcf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/2ff5925b-8525-44b6-b37c-daf03cbc1744.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/b41e5bd4-2b64-4372-ba8c-315ef866bf65.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/6cb84be6-649b-4a11-abb7-02f08ea608e9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/956cfa47-0bd3-4897-84e3-035ba20fa61e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/72865776-71f8-4e67-95c3-b71900b7c7e0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/7c39f262-623c-485d-be0b-8ad062d081d8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/f56fc5ae-1ced-43e2-8ed6-403865ab4381.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/f7c791fb-9d58-4d02-8aa7-a089d1d7b3f4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/7ea933d3-6f78-4d47-ab11-d8747fa77520.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/c3ebde90-ef5a-4f80-83d4-bf8c0433bb70.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/f18d05df-1752-4c67-a5d5-240859f0968b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/023a131e-793e-4336-862e-606388314937.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/c47a413f-3624-4c43-bfe6-b3680e883d5e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/6c571517-645b-4123-b1bc-d1ebbf4bbb43.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/459edcca-c97c-453a-935a-2260faa0ad64.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/0f3a5542-a340-42dd-b226-f8d3bfac9bf2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/473495af-ad4a-440f-a1d1-16125d78ba1e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/47b2a0dd-48c1-47db-aa6b-76e23a4655c0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/6490562f-fecb-4afd-ae65-3f5c9e9d3b07.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/5b7747db-b485-4a9e-a3e3-e13d769f9b81.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/0df2348f-922a-4e47-ade6-0b90bc20aecf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/67d4e7ff-b00e-4149-a440-d7a66830001e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/bf723fb5-694a-48f8-a508-8ede75225c64.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/170ac7ee-36c6-4bc0-86ce-a18ca3394fca.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/2fd37c6c-5baa-471b-9ea8-77575275e392.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/5377756b-a83e-47b4-8b9d-2a93673e99a7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/bcd7c20e-1946-46ab-9378-e7dd58279395.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/0664bb5c-0a2a-40b7-93d5-4ef860f02afd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/ec23a018-ed90-48cd-8bdd-c220cfa39fb1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/0bb0e10b-b6f1-469d-80ed-6a93d1e71d7a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/d0036f66-52ef-4b19-96bc-2e76031c0442.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/b6cb57b6-c418-4cf1-a6c4-851232da8f27.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/6bcfdbbd-4078-424b-8c05-f8850e8fd53b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/05b66b1d-0afc-4908-9793-1f63ffe2d3b7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/746d7737-dba7-4612-8e8e-ebf773d09703.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/25f813f0-c342-4e69-a39d-66895706888e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/2dec4f39-dfe0-46c9-9dd9-07086591a6cf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/34cab64b-caff-486d-bf9c-c4c2eb49fc21.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/df27a201-1aba-474b-9aa5-b61d815ebe14.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/5f1363b6-1632-4fca-bf9e-ae3fe9934862.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/296ecde8-a529-4c02-86b9-3d34b5eab908.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/74d1db74-200d-4636-b570-aa0ae1f13451.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/410b1f96-51b2-4027-a70f-9f57391dd242.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/fee13806-2d91-4435-b85d-bec39bbc0553.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/122cb0f0-091b-41c5-9f9a-38374fc36fc9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/18efb2b8-9791-4193-abfc-f1d05ad73c92.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/6a91481b-2dbf-4c5d-b591-da170bf5090e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/13497616-72f8-4a62-8f65-6bcdb984cdcf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/1aee0a48-0fd9-4b7e-b4d7-efd0ac1fe9fb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/1241df67-5ab4-4703-93ab-b586dca89cb9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/6dd49450-059f-42a9-9981-5e3d6f7aafcc.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/36235ba1-f290-466e-8908-f33a63680010.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/005c3bd7-59df-4377-b3fe-7407d993d87c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/602afcf5-25b5-4a7d-a151-949ce7e30f6a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/63e9b166-4533-43d6-9440-073665e68989.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/c7baebf0-003c-4304-949d-4649fef1e648.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/5ac46650-562f-4d64-98d0-72d07ca84468.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/c1c2e886-471e-40b5-bc2f-1002ee17c0f3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/df7c979a-7224-4ea7-8c3e-24b556402674.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/2eecb45e-eb4a-46bd-9a83-5f0cf0e8b3bc.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/cfbc6a13-db78-4679-81db-a8341da5a62d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/2ebb6d8f-5af6-4201-b55e-2c3cbe83e243.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/cf67f441-3e3f-4116-a839-6cfcad7b4104.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/ddc2a460-e54a-4d64-9d15-77e051be4a1b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/a1fbdd57-fbf0-45b5-aec8-9e9e5cad2091.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/30b39f44-b408-4f89-b95c-71232794ce6a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/7a890c8a-e099-42fe-81bc-1890c9a79986.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/efe8ae1a-c859-4cb6-8016-43369d522878.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/9475266a-cf67-4d6a-ab33-457db011b6ca.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/41e18b92-1f2d-4824-b486-d2e5d2673875.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/bb41da0b-888f-42f9-8edf-fe92c9331889.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/8cc61338-f413-498e-82c5-8381a23f1ff6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/5698e7df-f826-4db8-9327-0c8c30ec4701.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/b995b879-2966-4cfa-babd-96948a6aed14.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/e0abf3ba-61ba-4618-bca7-eaee1c27c00e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/e4a75531-960c-4874-af5c-7a0af55c5612.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/9c0b1f7b-c5e8-4754-ac85-beb008effbc3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/53c692db-ac36-4c91-926f-991436aafc35.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/b0ba5c0b-8047-4315-8a92-bd090fa78387.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/b53231a0-0350-4826-ad3c-e40008380d28.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/ff99738a-6ffb-47b5-b53a-d727f80887b3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/2ef5fbdc-2e91-4260-8ec1-56d2af35b72e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/ae202f1e-399a-491f-adc2-c4b753c07e38.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/4e0d9459-be15-4750-9dfe-db78c8183473.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/665a9954-3539-48d5-8a8a-adc14ed0847d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/d17b4f52-6703-4877-b0a5-8c28811e5993.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/1a3e5d29-08f9-4a3d-9f81-70af7bd19165.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/08220c28-685d-4b98-ab34-48564db1d743.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/8c96242e-7104-40f5-adc9-7f72bda6d009.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/c0d8ae2e-86b8-4896-b7be-2cb2a1b2853e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/be06efa8-6c0b-481f-94d3-74a165670a0a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/373ec131-193a-4ca8-aed5-cdbf4f95a89c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/24fba4a6-a7ef-41db-b259-c4af38656fd1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ae8c9d36-ffa9-408d-9bdf-1e0135f9b70c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/85f5052b-9c9d-4e18-a215-f0545e33791c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/f0b67835-7348-4da1-91d9-65310e3f66e9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/9782317d-2b65-46b6-b514-57fac1925ccd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/dd451416-5e2d-462a-bd4a-2412910740d3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/01ace652-5a79-406d-9e8e-4429d6ff2c6b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/cf2a0270-c70b-4b53-8fbc-554e262eef87.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/c8d9244b-d4b1-4373-8a9a-3deba19ee5f8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/78c68937-b760-41eb-9f0d-90e33cf1eb10.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/40015795-6f8a-4d07-a3a5-bc4e2d81d806.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/e016567a-6159-4845-bf6b-f5340087c54b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/92d2c0b2-63e1-4dd1-bd26-49cde71b36ff.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/df680596-97db-4e68-b231-a4e26a0d649f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/d1f13ce0-e20d-4c2e-9cf3-4ee1d291265c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/2915a1ba-3a1c-4d01-8f16-dc9351065721.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/5b4b8bbe-833e-42fd-8a31-70e989de5ab9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/c0d27ea0-e353-478a-8599-a205ff7743df.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/12b721e9-a49e-44b5-8633-ce4c95c0252c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/08f5856a-a0f6-4879-bae7-0f840854be7a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/1f0d43bb-d2b7-4d1d-8fab-d29abdafe1f8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/524195d2-9204-40c9-84f3-1470634d0c8f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/3f77c3ff-7806-4fa8-aad8-f0a0802d0c7c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/d000753b-f4cb-4d2b-9426-689714dd1557.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/f69ec9c9-d16d-4ba9-b6d7-dca3b7e28f48.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/ac58b361-ee62-4a40-8a9a-90490f0bb59b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/3b7bf7b2-afcf-45ec-b6ca-93b2380ae6ae.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/521071e1-7bf8-45fa-ada6-1c140a8fbb2f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/aee1c12b-3803-4fac-aefb-79f57565717f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/765d7279-9093-489a-b88c-4fd15d6b31f3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/67481505-f6ac-44f1-9cc6-8cb95346541f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/dbb99998-4299-4a54-8bb7-c58f36a7747c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/5b3660b1-cddb-498e-b1da-69f3e301021f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/fde2219e-0fce-45e3-81b9-9990459a55eb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/276ff444-eb4e-4091-83a2-94fba3b6340e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/d8cab642-9e99-47be-a117-7fabe2de5552.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/0420bc64-dcf9-4f16-a2b4-4c38e3715c4c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/5eab5965-590d-4cff-8bec-26f3b9385885.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/dbcc3760-0a46-459b-a11f-3134521afd96.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/199b94f4-34a1-4667-87cc-9ecce2ef94c5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/0b554bd8-0af0-4233-9fc7-74cd498e8056.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/e640ef3c-7aa9-4d6c-a6dd-8e38d22f4623.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/5828efe5-94f9-4a01-956b-16ab4d0acb4e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/80469f9d-d603-43a3-817c-9c814a26cf88.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/e352c32c-ef5b-492d-be8e-c130c3abe3a9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/05ea074c-7569-4bd9-bce9-5ca0d4a789f5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/194c0b2d-bc31-490f-b526-558f878a44bd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/591ca59f-05e7-4374-be4e-f26734dc3bd6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/94f0f1b5-1157-42c0-b8c7-20ea3c8c63d4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/7caa35df-d361-4e40-9dd4-8d38df8735e8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/5afe5679-7639-4c4c-beb3-611cc95a7ea9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/2debdd56-da37-473b-9d83-1dadfb3a193d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/69fc7b47-b711-4efc-89f7-7700c51e687e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e2f9f3b3-6519-47eb-b2ac-aacaaf1648b8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/1cdea436-452a-49f8-bf0c-a0ca7833f42b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/a42864fb-89c2-4eb5-b8e4-a885ce1e4a4d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/866f9574-a46f-46a7-8572-f824c8f3b9b4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/a6780bd7-22ab-488d-830c-7370e7ee2677.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/f3edec07-a8ff-4977-aaeb-f8a466867706.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/0aa0f7dc-4ab4-4e6c-bc30-f82beadba006.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/cfb51bb0-c487-4f0f-93ec-9d9e4ff91adf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/6959c881-ea64-42c1-964e-5672a4902e6f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/91e0805f-db3e-40e6-8542-efaccad172c1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/36fe022d-bb36-4552-9e46-b1575d77b5e5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/dbb7b8e2-2242-49eb-9d5a-24a0ec099a1a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ceef41fe-d9d7-47e2-b4c4-300740aaa16b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/06f6d913-e19e-4eac-9cea-a9eeab0570a2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/86ea7190-fa54-464d-83aa-17726440ecb5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/668fdb63-86d2-494d-bf18-85b480932bce.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/d1db5131-c5bc-4c61-a9b1-c982150eb6df.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/41ca776c-102f-4c2b-9ad1-9641f0a5453c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/ed060b6f-9732-480b-911c-3d593666bae6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/584b264e-bcd8-46f5-8dd8-31b3ac80a21d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/c3c9d719-96d0-42a4-babf-ee322b7d1a5c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/b4f0c1d6-898a-4267-9e68-80db6a9d338c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/f2fae117-f8bd-4e88-8632-402e210a51f4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/f43c4c16-68cb-4b6a-baba-af6f34376c1f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/cf693e9b-fe26-4ab9-b7b1-fe06cac74f83.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/c0b48434-a6cd-402c-be99-357258553f9c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/c53c1349-3ea0-4860-b243-bafa6f2e0988.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/67360415-d2bb-4b5b-9dc3-24666f4b16d6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/98ab4821-5842-4676-89b0-3de66bd6cb7a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/99414270-6779-499f-ad52-835582460b85.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/1a5d3f77-4b01-4c57-aa65-ffc3fa8f3b42.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/be4903ec-8e07-42b6-9639-093c4d93c5ad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/e297ebb0-3ed9-4635-89cf-cddb8cf585f0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/d0ec89fd-7efa-4b1a-9f3a-da7975af5138.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/5a89339e-8549-4f6f-92d2-317fa1426809.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/57fa6856-f14e-4157-8095-87bb11c341fb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/74bddea9-01c5-4795-ac79-e0aad1017a46.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/f7bb3592-a2f3-42c9-b927-5c8b3202599b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/6f0c9729-262c-4705-8d57-43f66fd71c59.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/80242347-9b3b-4fa4-9739-ce5bd05b89de.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/7d62b0e7-c93d-4def-b320-a6380f7f71cb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/0b062bef-d8a9-43b3-8faf-eb0af2548f5f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/a59e42d2-b5c8-4362-b38c-ed5d6b004fa7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/6ddd37d6-4068-41ec-a419-4761924ca067.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/8b1c55b7-ab26-49a0-9d07-53606cb3a0dd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/9bdccebf-4ea6-484e-b60a-d70601b6a936.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/5b4d6a34-34b6-4f6e-b06c-76cb7d9f6085.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/06bee189-fa05-4c13-a3fe-0ca27a51f637.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/75212060-8467-424c-8dac-da1f068a2d1d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/772ba4c8-1046-4b29-ac76-2949e87efd35.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/38807536-b75a-4fbf-aa64-47858b2ab49b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/9cf63fcb-13e3-4b7d-b361-4f9c1c669252.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/1f4804eb-4b11-42e3-b445-f96e6ef0ec1a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/30312c73-ee65-4940-b6f3-ceaf0b439cc0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/cebb4506-304e-467b-81ae-354855d0969d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/02ee3c83-359a-41b4-a2c4-2e9e9c33c197.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/e5d7e92e-0e4c-4768-8a0d-3f4555b4f46d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e9e804bf-5787-4927-a396-8c34882a3faa.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/84698fd9-b86b-4b10-9024-57a8bee8f651.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/6294baa3-3374-47d8-a127-f079c45afa5f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/eee04836-785d-4639-8da1-da5193523897.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/3a7ca971-5bc5-43b1-96eb-3c21d8d7c738.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/8acaf15a-725f-495d-8d77-456035b42b7c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/b970241d-999c-4cdd-9685-ec7d138d007e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/56d06efa-9b28-48d1-a77f-c95e8d6d228c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/20d86fe4-1594-4988-a51c-83b7af7bf682.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/d6f14db6-02fd-41be-bef8-4fbf4711ead7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/11729957-f7da-4835-9f60-bafb54f19fc9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/eaac7eb5-87da-4ebf-aff2-933db69040fa.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/e253b0d2-91a1-467a-8a31-59ac0ad9e52f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/e21a80db-821c-46e7-96c8-0f988146f3b2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/817e289d-0b1d-4af4-bfaa-239b3cf2145b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e0ba574b-72f6-4c3c-89a4-100b6b854095.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/1ca16727-1327-4e22-bd31-27998f9e0d80.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/392b79c3-fd42-457c-a745-19d33bd6fdc3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/03c569e8-7dd4-43d0-b6e2-eca482ded425.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/7d77b44c-d571-4ec5-975e-869cff170233.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/bb16d391-4a5d-4790-8169-6b6e25637d0d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/4971017f-6c4a-4834-8adc-b78bcf388c81.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/76c1dc55-8b43-4673-b872-23bef57a087d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/8f33a833-764b-49ce-8096-ec12dfe1652e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/ada43b2f-0204-4a42-98dc-46b3aaf8a8eb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/a027ea3c-53e6-47a6-a944-3de39edd5bc2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/be018b9d-b5d7-450a-b6f4-1b7c55c99536.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/29f4d02a-9c5f-4895-964a-e687f6300859.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/b43b2970-7d5a-4908-81bf-a1093f2f194f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/b58a2bae-0a84-4996-a276-3b3d340e1341.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/f5b9fc95-a139-4208-9ad3-dadc7dd587f3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/8aa9b8cb-f7da-4e8f-be9c-fc5bb77d68e0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/93c96d9f-3a11-4ff3-89dd-e6dc323b02df.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/e0845a0b-f590-4baf-986c-07199e51c615.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/a71461a4-a64d-44c2-9ebd-7d83793ddba2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/9e61ae33-99c8-4bc7-9408-1f6af32ed72d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/b2ac4089-eeb5-400a-bc1e-c13865ddaed7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/099288f9-b34c-47a9-91e0-eef1b14dbcbc.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/cddd4543-2488-4200-8813-e88aa761aeb7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/cd6c50e0-95e8-477e-b670-0ea697ee05a8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/47112c8c-bf9e-40b3-a08c-79df58cc8749.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/18cac3f6-2fbd-4c58-b342-c435c4827d5f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/e55778bb-104e-4802-9473-dd7e4b725347.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/7f19adb8-6fa1-449d-a7c1-a84175068552.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/58f0e038-bf09-432a-94be-b64e95f86e3e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/5646e615-9cd8-4cae-87d6-e70276df7e74.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/55e6df04-3c70-4aa1-afe9-36057304d48a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/fd9314eb-7c66-4a22-b596-06b30dcfc018.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/1f4ca33a-5b0a-40d0-996b-09fb6f791fa8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/c66649c4-847d-4058-8bf4-623906a1a2cf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/d49939a4-d117-4d8c-a1b9-71e191f3e69d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/95a413c5-4409-4157-8c74-ebe94ef67e46.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/21115b65-7f0a-4d00-b512-d455e53bb3ad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/56fe6e72-8cbd-4855-a21b-4dbc65a39e8e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/edbb8cfa-0442-4133-b830-34acaf4a86e7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/a3bb7635-8e55-466f-8fb9-cae9aac15f8c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/a2553a9c-d973-4b19-a036-e0d1e9d06c22.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/fb467483-8707-44ee-8e5f-46e812fcade2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/ebb259e1-5ec5-402d-b8d0-56e309901a7d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/26d17a2f-b956-4051-89cb-91cc9087866f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/4ee6aeff-2908-4d4a-be40-490ef73a51b3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/05356b34-4a35-45e6-8fc3-5eff887fbc9c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/d36f8224-7dc0-47e5-9d1c-6894c2ca7fb1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/1544eddd-0695-45e4-96c8-daf66c72ee04.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/9408bc71-2d7c-4ffc-8429-0971d539ee93.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/9a833b34-e402-43a7-8906-027b4171360e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/4a544dd5-57d6-4e33-9bf0-d6d4fabbf7f7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/2525c777-eeaa-465d-aeb4-7219e82e88e8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/94b3835c-636d-41ca-ae24-b88b868927a1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/c0910322-17fc-4aba-8d5e-81d9c16dc37a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/6634ef59-a4e9-4e01-a1b7-40cff4e4af8b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/fdba7aa1-ee02-4ca3-81b0-b57535a61cc1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/be7bf250-e6b7-47c9-a8a8-30d775f57c1e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/a40a4e68-fef9-488f-9067-2412603ea87e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/5f1560ec-cb73-454d-9bff-e50d606871b9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/1bb8c7bd-31b9-48c0-b102-1e15da2a870b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/70cafbaf-0d40-4ae0-ae68-d9be4030a310.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/3016cac3-6a94-40cc-9d5e-64f5b0e15e56.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/e32a6cdf-c372-496e-be87-0d8c45feed6a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/f75ec553-2761-4a26-ac2b-fd272499a24a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/00811ac7-9e41-4f96-9a9a-6dacdd5deb8f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/460f1008-5c9d-4406-b205-d7ddfb0a529d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/5f2bba64-2fd6-4253-8922-27d118ba8e51.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/5d68a7a8-5ba5-43c4-95c7-6a432a409e5b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/4260d7c4-db31-41ed-a7cb-481927162de4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/fa0ab438-ecad-4a9f-a320-aedf600c9603.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/5c83faba-dc84-4d0d-8616-c30a18117e66.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/bccb5004-97d0-4014-b046-0c771f2e9315.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/04662a5f-d61b-4b8e-a316-fbfd63e5a540.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/1aa6ec18-9e99-4e94-abdb-56ec6b9bc0c9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/520ab070-5b3f-4908-b607-b7c1b67250c7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/94b40483-9842-41bc-8f79-ef7ead5a676e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/804f0d3d-663d-4b29-a544-285d0bac5f86.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/9c21af22-4a7f-4a37-9884-538d78218c35.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/10c50da2-f5af-49a6-bb29-5abfab62040c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/e4d853d4-20a4-40a6-aff5-a0e0d79ebb58.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/39509e4d-de77-45ea-8ea3-1926204da413.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/49970a5a-c1ac-4beb-8874-0068d77e880e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/2a820459-89d2-4be3-ba14-e0ae7416a017.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/3d787be1-122a-4da7-937b-7c779739914c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ae1e5fe3-1d0f-480b-9f23-de97bc2771ae.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/0c135f7a-f603-4090-9699-8605c8955fad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/083182f3-d11f-46ed-a338-77136a620b3a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/2009984a-4358-4e58-a665-5d038ec28579.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/449d85f7-1f9d-453c-ba7d-ebe920cb1cba.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/d333a6ba-d064-448f-b4f2-8c16e56ee084.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/011f05c2-2e66-4cf3-9703-0c523e54e008.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/fcea33a4-01ab-46bb-8a6b-d28ad6b6dc6e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/7788a029-10c9-441a-881d-523d3be7d5c6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/8fae55e8-030a-4727-9274-6613daf74a2f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/e8343c72-1754-4452-83a1-30fbbbee8d60.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/07396244-94c4-477e-9cd5-c4cc22b0583e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/6ebe2a66-8281-4069-90e8-03dce36a1af9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/6779dbbf-f48c-4e8b-aaf8-ab6ef562182a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/f8cc4f7d-1dbe-4394-a344-56ff05e596d2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/baf91434-c7dc-42ac-a51d-8f32951eae1e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/b9ab0485-ad76-451c-8d3b-c9dfd866b754.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/fbc365f0-6554-4e27-a3ed-564ad6e1e39d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/8e5f493a-c134-48bc-b34f-0024cc8f18d7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/40b929a8-1b9d-4b16-9c74-5ae539d95654.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/cdaabd01-507d-4558-b6e3-d8ea84390a3c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/f825b55c-45f5-4f61-a6b4-665720895246.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/a651ab06-e37e-4413-a219-a66cfee87555.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/854ba8b6-7baf-44df-9a66-72b3de32be62.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/8be74cfc-19c9-4d1a-8ecb-fac1b78b3878.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/3707b07c-7ef4-4de5-8642-e32649edf8ed.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/65838f45-3db4-43e0-be48-3a22863c3314.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/2b1ea379-0408-40a0-a4eb-8f49628e72a4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/8ce3f5b9-5584-4b94-ba32-3448fbd9e18f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/cc16983c-d839-4b9a-a33c-7fa8f0379327.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/ff6a918d-8f60-43c2-8200-1720d6aeddd0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/f5be1c2b-2f1c-4385-b478-58cc78874b3d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/52eed118-6eac-48b2-b7b3-7df1d4b3a7a3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/6f93c337-1ab2-4e46-8e84-e30e4dda3601.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/8026dabc-f9fc-4e6f-adbc-03a015bcb426.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/d58df564-3e76-4e49-bde8-653bec8e008d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/e5d8e2ca-5bbf-4f44-9d4a-68e6aeeedfad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/3d8305e1-1371-443e-b372-874d50367777.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/13926dfe-9398-4575-b2e1-f66d7e02ba1d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/c670efe3-62bb-4690-b757-caae4c2a3361.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/0d5d0753-d943-4392-9404-bc923349045a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/8cc0d154-06a0-40cb-91db-6d1cb673d491.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/f44ec176-b2b8-4e2f-b58c-61d0feca94ba.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/44707e33-c027-4e93-b543-7a7b43dadd7e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/8a0b6b68-eaf7-489d-9bd1-c1f70050f52f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/8ae453af-eaca-44db-b1fc-cd8e32a54073.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/65ef6b12-948c-441d-8efb-b67568740733.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/f04c8baf-cd8b-4a63-aefe-88e2924fcd16.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/dac7d95c-db3e-452d-b6e4-ac328258bb3a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/6f511ce9-7bee-4c12-b4fc-a7be51781105.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/f33d7633-14b7-485f-ba74-b069a28102f3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/2f271c98-f0c0-4b5b-8e0c-fad50534791d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/4314c28c-39c6-4523-90d0-e7b57746e795.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/a4f1a45e-9d17-4d83-9019-deb855c343f3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/5b525536-c4a1-4798-9845-14dfd44ba86b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/3397c1d9-6355-49f4-96b6-dc1c042ec1b3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/323c9f19-be69-4031-8071-fdbe843e996f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/e98ff043-7abb-4efd-9fcc-0a421bd41e87.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/bcffd641-e6cc-4f32-818b-2afea0c96872.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/1094b120-eea6-4364-b428-8e40a74bf501.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/9573a983-bcf6-4854-a333-e5b879aeb070.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/d33816ba-39f1-4d36-ac43-264e9848e8c1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/673fdd68-7077-4cca-98a1-b331d411fad4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/bef5dd8b-a90f-4076-9330-6b4125ddf42f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/bbc551f4-c947-48d3-8c70-11d6bdb4252a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/81e3ed31-c526-48f3-84c5-9961ee5ecd22.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/15b2742a-4e74-48f7-bef3-8c38d32413ae.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/c86d424d-5fdc-461e-aef3-e51983cec912.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/30ee7029-2161-420e-9655-4dff7c1a37f8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/be1e2912-d0e6-4239-8f51-0c622c4c6b41.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/c6f45c81-4456-4081-9029-83cc3900fb82.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/cf0c95d7-e3ec-46b5-8fed-7945de0296b6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/a86bb85e-060e-4285-8a74-60fa3fa8a980.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/f8333065-4e66-4524-9c74-d4ec3b49bc1b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/82749130-0cac-49cd-b506-d4e42f541b79.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/d2f6b082-ee72-48fd-9278-d2d015a6f335.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/9a54b33e-4002-4782-b865-4ed9b43be319.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/b82368ff-aae2-4d73-88f1-436cb3bcc3ce.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/e29f581e-2b60-47ec-b5b5-1513572595d5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/4c4cb1ae-0593-4ae4-8191-6f5a165b856e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/dd0e6602-6f8f-46e0-9816-649c9e96943d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/502668bd-a138-4a17-a660-31d22d250b07.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/97431fbf-03ab-498f-a810-04894419cb57.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/19a7ca30-4a35-4cb8-9463-7859e76e198b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ea0cba42-724e-47f8-b855-f482ff8930b3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/94f04200-d8f4-421e-939a-3fa074fe6720.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/60c90b15-fe61-4227-a1e2-db0b3a1d70b4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/903b23d3-34d4-4744-a0bc-e5fe86cdc160.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/9544fef4-1443-488b-adaa-d94282922e50.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/db561ba4-dfbb-4703-9610-042eb60e9f8f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/391025be-ec91-4a14-a39a-a07eee4cdd83.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/4bf4d6ae-e4ff-43fa-bdd3-d3a7145323f2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/f10b74c6-e018-43fa-9e17-e520879e23d0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/3ee33def-c361-49b0-b3cb-037e23888677.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/6c5b2530-7c6c-4bdc-ac16-05e5f20acb99.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/f6bcb222-c8b5-4354-8dc6-8c0f47ef6d62.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/03acda67-14c7-4c1d-a33e-78695073bdf1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/4569ed67-8fc0-4ccd-becf-f66784642dbc.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/4597071e-1f29-4e55-a863-05987b9bb73f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/c8e8990c-cb8e-4313-9509-c7f96bdf9869.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/46901ea2-72ab-446e-8bc4-2ae836113275.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/a5e94432-20dd-453c-85c0-1efcdf18ea50.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/0b774e80-9dc5-42d5-a888-aa38f360e4cd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/7068b12b-9624-4e81-8c53-7f3430d9bea1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/ef5f15da-8e60-4580-8d3f-d3045c001596.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/dfcd2fdb-6776-419f-a75c-deb8bb2bb7c8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/ea91dbd4-dbdc-481e-a848-0c203854dffe.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/872ed8d1-4e0b-42bf-8aa6-e916985999d9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/db139437-599c-4111-ae53-234d480cecd2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/3e5015c7-8344-49d4-9e9b-97e9ca429250.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/e8471eab-0721-4eb4-a732-1eedd7c51780.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/114dd545-1bf8-47e5-a032-23171058da89.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/32beb1ab-6a2b-42f0-ba1d-faeae03f00a9.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/30110bbe-4871-464c-90e9-4a6ddfdc61ce.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/13ca0589-cb57-4973-b1c2-c7b7384e0293.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/ea0b10c0-d25c-4f9e-bd79-c780961584b4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/be6926b1-0f27-4675-b2ca-2d5c1ba3ff9a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/aac0329a-2ccd-4c30-abce-bb3c48ca4bbe.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/6b01ecab-a0c9-4c5e-8de3-4165f0e204ef.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/a7b96eef-6eb0-4887-bb2c-9f2c71cdb790.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/99260f18-1639-4241-9412-fa162cd6da84.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/0420b4d7-cce3-4e4f-be60-41de0e5d1a49.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/1501922c-6ad9-4126-9d33-2191b93f0a27.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/97f297f7-593b-4e54-93a5-22d1d4449d79.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/23159c95-94ad-4ddb-8b02-69d8f01f7cbe.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/183e6999-2a3c-4445-b106-06f4bd34173b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/78116e69-3158-46f7-8ce3-351ca2e37952.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/6a21a89a-248a-4cbf-99bb-a184d2b1ff51.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/6c836204-5a0f-4f57-a3d5-fc9e3eb870da.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/85beba58-fd0d-4f81-85bc-79fbcffc2470.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/81a20cd3-e86c-4448-82fd-c807abbe7501.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/460acf60-3147-4dc5-a449-85346112c697.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/7bdaf628-c4a2-41a2-bc2c-600c7a495e25.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/06472dac-3ec0-4274-9753-4cb5797631a5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/debb87c4-9b72-4fe4-a15d-75eb32db66f0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/ed6d59d9-21bc-4b32-aba8-9b62e1156305.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/922d2b60-cbd1-4a7c-91a6-84ab4de0bc85.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/6ebbe9bc-d3bf-47b7-885a-4eba00c03da1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/c162c2f7-f696-4b05-8e19-70b1893c1652.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/cbcf770a-1f40-4136-8ff8-544a0c747d0f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/d990d075-233e-4edb-af4b-c55165d29f0c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/f2dbb709-127a-4a18-ab20-b0f07502b710.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/adf55881-1642-4736-a5fc-4486a7a748e6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/a863c29b-d851-4b01-b787-9ecbc161a922.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/65a9a9d3-603a-4647-a0bf-da0eaa1dbbdf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/737c234d-6882-4c9c-8980-5fee9976deaf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/00220bdf-156f-4858-953c-8afe9cc07f34.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/ba2a024a-7988-4d3f-bb1b-e8894e12d369.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/90ba4b22-20cd-4f46-af16-e672c20b722c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/1f9e9554-41f0-46d0-82ea-a820b50cc233.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/9dd955e5-8c0e-47c4-9f7e-5dcfcb97c3c1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/92da9499-7446-4eef-ba5b-4c4b82d3d520.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/f2cfc591-513f-4640-9e7a-6711d518d12a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/1c1394cc-c0db-471d-9604-01ad33169f42.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/8296e20a-5c25-47f8-9c6a-998a4ddb794b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/7b273f38-0e81-4c8b-ab62-1f88b1b715ae.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/55488d70-df9e-424e-b714-03eecb903d80.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/6ba62b39-33fc-4e59-90a2-52998f40f04a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/e5bd5875-e344-40c3-88ac-9c6ad0f38a9a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/cf50b344-0088-4afb-af52-c9822f568cf8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/45e09af3-8d8a-42ca-8e6c-20a01c013297.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/ae5b7c4e-4958-4e25-bf07-ac74b2b2f567.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/c4078547-815f-4955-8a27-46f2c18b6398.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/00b81866-4a50-4d61-b806-d6d65b90ed10.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/5c61a570-3276-448d-aad8-679eec740868.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/725d6042-e212-4ed7-9bbd-f6e60265283c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/7ec57806-8bb0-4371-ba38-4a47fb97d901.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/d244b0a2-f93a-4a3d-903f-fd00c92a8559.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/c0fb210a-5b5b-48d7-a09e-13b04dd12b3d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/56dc96e9-2b3f-45af-99b4-e89ab998c58c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/750daeb3-c35f-4e8a-80a8-9cd3bafb3dd4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/b2d19563-2944-4a0b-bb25-b78392dc05ca.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/e4da5885-12e8-475b-9ace-329eb53bf700.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/311f7371-a2b9-44a8-b0a4-ff1409c95792.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/25b42d31-3f3b-4225-948e-beed75e3f506.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/ec7580f6-d33e-4bad-b257-5408bb45aa0d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/02a253a2-45f9-43b4-a0b8-aff59200a608.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/97829326-a49e-4d47-9a63-c660666d66c7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/12972e8c-4938-4995-95f9-fb527dbc3ac8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/d61d030a-c10d-41a9-8131-548e38666dbf.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/dd408b73-e630-47c5-802f-ee17d8291d5a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/513cc69d-d19b-4180-ac9e-abfd1c90417d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/37769375-3e38-4e8d-b834-ff0e15f2ef99.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/20ccea9a-0dae-4b79-aee8-433dfc0a230e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/da0837da-536c-4d70-bcd7-9a339239b95e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/c276d6d7-a741-4e7a-9950-2c0690891e61.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/297f3b27-ab94-4850-858b-610abc96a3ca.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/bf03bead-70f2-42f8-b5cb-6406a3f16d52.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/6e8d59cb-e838-4fc0-a3aa-4fb71d1ec9ec.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/30dedae4-3599-41a2-a3cc-be0d4e07f655.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/bc91bfbd-da17-4789-ad15-4b8f42b848fb.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/2622d83a-d48f-4303-ac4d-519d41c524dd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/22b33659-9020-4ca3-a8bb-9054b4dc4c64.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/4b511d1d-8fff-4505-935a-c93ce6a74dad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/ce8dd802-a0bf-4b2e-a407-327e0701422d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/720280db-61ae-4ca4-9686-4064e395e20b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/9ce6f56e-1846-4d5e-be01-c81d0bf809ff.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/b204b7aa-239f-443f-93a3-5beb687b2979.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/828430ba-ab2e-4d0a-808e-dedb8e128a0c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/11e6415e-decc-4eb5-9c4e-748df0a4efb0.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/044a1831-84aa-4e66-a9ba-fd625393384d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/435baaa3-9494-4895-a815-18f3e40db1b4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/b5ba9693-a7e9-4801-96e8-7798431ace6b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/65b05197-4706-491c-94b3-55d25b803b1b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/188020a9-9fe0-4919-b081-c1327f3372d6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/e3bb642b-3048-4ddc-b32f-3cbfb374ea1f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/7a966fe9-8307-4803-a617-84adfdd0a74b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/3b4a00ea-0b97-44c6-813f-939e1e1559d1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/3812b85f-d4ca-4f7d-a074-8ed0188e22c1.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/12cd189e-5bb7-499f-9898-1edf2463da87.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/d785d5f8-b08c-42b2-b753-24ad2aacb716.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/c94d1601-4c05-47df-9733-32ffbd00d24f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/2fe370ad-29c5-43a6-b43b-4532c318dcc5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/4ca9195d-0d57-40b8-946e-85593be97292.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/c36eb774-284e-4e46-bae6-a1f96a6f0ca5.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/7f9c3798-c041-4f77-8f40-334b1ecc9b2d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/ecbd3869-938c-4b09-8308-f4c986bb0f35.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/f582895d-2819-40eb-bcb4-ec3c19b83a42.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/0b1ee128-8e7c-4cc6-baf9-bfc90149ab5b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/85607885-1264-45d3-987d-8d4ff380f0ad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/e2dd2daf-2400-41a3-b82b-7cc810d22611.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/bc70ac20-c30e-48a5-b32f-0703a4e52e4c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/1853d72d-9ea3-4959-bf70-b6b0220fa81b.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/88365ffb-daae-4272-b4c0-150db3f30fb2.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/9c66787c-878c-4efa-ae1e-dfa06cfc8040.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/375e1e4d-331c-46b2-b869-620ab0a1ad16.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/1a36b147-07bc-4662-a966-a75e3722a7ec.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/930072e8-686a-4918-ba7e-d9f9e22fd226.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/4545bca9-2e14-43dd-8439-3e3e9988852d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/6d44f3d5-3efe-4ba1-8645-3735c7bcb363.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/2f39d253-5f69-49e8-97e7-f97c09d64a23.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/636a1e1a-9c54-42ff-b02b-bafd818c4d43.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/857cfb40-31e2-426d-8cb6-20136763fdc6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/d7c89009-a477-4105-9a95-5a8f92db4c8c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/d9e25c44-8187-49d2-a1f9-e94d7f4de8aa.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/de980c55-cfde-4215-be28-88d136b6ac99.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/25df806a-4132-4c34-af62-77e81a4df05f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/e7d519f3-8786-4cb7-bf5c-e4cf7623006e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/bf8b7b1d-d0db-4d1a-b46b-f093c5f3ad3f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/5ede12f4-be14-4c94-b439-155fea6c2927.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/f130b7d3-37f9-476d-a726-efc4a0266c27.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/b2c59459-550b-4906-bb17-cfbfa1c73e64.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/fdb7e1df-5e56-4edc-be6e-fab76f832cad.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/3e22520b-1376-419f-b670-4544d613edca.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/666a96f4-e972-48ed-83ef-e4b5c332881c.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/bd815d71-0d9b-4c7a-8281-8285a211a4dd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/9d4ec5eb-9ab6-4b08-9f00-f65a17ec4e54.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/2edb756e-a637-482d-b618-f6ad61efc2da.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560005/53241c7b-a35e-4eee-93c3-7bce75d514e6.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/4e194827-a51c-4efd-b876-79ffab157fed.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/2297e65b-f3d6-4f49-b966-b0be0e4c2841.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/f76ae0c8-c43b-4b3c-90fc-207b0a876e39.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/cf849e5e-d350-4c7a-b578-5ba52845cbb7.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/1b58319e-f6e2-4b2e-8a15-61bb4a323030.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/7314ade6-4392-476c-853d-defa6d63a1a3.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/34284a18-731c-4303-9ac8-7ecad21bce2d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/f9d4cee5-5bc2-4efd-9789-7488ea514240.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/1003005c-f12b-4690-a5b8-5664febf3242.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/d0e50b60-a298-4667-b8ba-21b7e3b2884e.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560003/36a6ee9c-65bf-45f6-8c0b-22b932083678.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/97ba08df-5aab-4a83-9e33-d656e0a4a369.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/4a995145-80d1-4307-8d16-f62fe3d98738.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/66ce91b6-b196-4693-b9a7-1d10476fd900.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/bb4db1ec-a3d3-4aa6-be8f-605ee214a804.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/62d59fa1-03ef-4c84-ab09-614756e4ce88.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/eb0e52cd-40d0-45d1-994b-ff91cbff9f99.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560000/8c733ebf-64e6-4099-a6c8-2b5f8e416807.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/c01f9a1c-4672-4d64-b3ed-27c0adc92b5d.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/91700a96-8ce8-4ef1-9301-a0a913ebc62a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/3af428c3-3e9a-4c16-b15e-50e606bbad13.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/8bc640df-20e1-4fd7-bdd9-06a4123c3d7a.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/ddd97133-63fa-4f20-bd31-d18e13331ea4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560006/40d70427-ac8e-48c9-a846-19a4018330d8.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560009/5babe45e-b7c0-4a14-a442-0d449ce48d46.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/1ba1dfc2-3c82-4049-af3e-7432c9201d79.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560008/9481d6e4-9107-4b7f-84f9-1cb29fe37f59.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560001/ccc8e8bf-07d5-4357-9582-c16e317624a4.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560002/5dd5073c-7d54-475a-a6e6-0ac85134757f.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560007/42062192-7cb5-45c0-93e8-f10e89f368dd.root',
        '/store/mc/Run3Summer23BPixDRPremix/DYto2L_M-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/KeepSi_130X_mcRun3_2023_realistic_postBPix_v2-v3/2560004/4637c8a1-0c38-48a3-bf27-ca1819e7c388.root'
     ) ),
    inputCommands = cms.untracked.vstring(
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_simMuonCSCDigis_*_*',
        'keep *_simMuonRPCDigis_*_*',
        'keep *_simMuonGEMDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep *_simHcalUnsuppressedDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*'
    )
)
process.HLTConfigVersion = cms.PSet(
    tableName = cms.string('/dev/CMSSW_13_0_0/GRun/V140')
)

process.HLTIter0GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter1GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(False),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3MuonPSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(False),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2IterL3MuonPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2IterL3MuonPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter4PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedQuadStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedQuadStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedQuadStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetDetachedTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetDetachedTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetDetachedTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.5),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA')
        ),
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA')
        )
    )
)

process.HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)

process.HLTPSetJetCoreStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(8),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(10.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonTrackingRegionBuilder8356 = cms.PSet(
    DeltaEta = cms.double(0.2),
    DeltaPhi = cms.double(0.2),
    DeltaR = cms.double(0.2),
    DeltaZ = cms.double(15.9),
    EtaR_UpperLimit_Par1 = cms.double(0.25),
    EtaR_UpperLimit_Par2 = cms.double(0.15),
    Eta_fixed = cms.bool(False),
    Eta_min = cms.double(0.1),
    MeasurementTrackerName = cms.InputTag("hltESPMeasurementTracker"),
    OnDemand = cms.int32(-1),
    PhiR_UpperLimit_Par1 = cms.double(0.6),
    PhiR_UpperLimit_Par2 = cms.double(0.2),
    Phi_fixed = cms.bool(False),
    Phi_min = cms.double(0.1),
    Pt_fixed = cms.bool(False),
    Pt_min = cms.double(1.5),
    Rescale_Dz = cms.double(3.0),
    Rescale_eta = cms.double(3.0),
    Rescale_phi = cms.double(3.0),
    UseVertex = cms.bool(False),
    Z_fixed = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    input = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    maxRegions = cms.int32(2),
    precise = cms.bool(True),
    vertexCollection = cms.InputTag("pixelVertices")
)

process.HLTPSetPixelLessStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterInOutForFullTrackingPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelPairStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPixelPairStepTrajectoryFilterInOutForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPvClusterComparerForBTag = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(0.1)
)

process.HLTPSetPvClusterComparerForIT = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(1.0)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryBuilderForGsfElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryFilterForElectrons = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(-1),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTSeedFromConsecutiveHitsCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    propagator = cms.string('PropagatorWithMaterial')
)

process.HLTSeedFromProtoTracks = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSiStripClusterChargeCutForHI = cms.PSet(
    value = cms.double(2069.0)
)

process.HLTSiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.HLTSiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.HLTSiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.datasets = cms.PSet(
    AlCaLowPtJet = cms.vstring(
        'AlCa_AK8PFJet40_v19',
        'AlCa_PFJet40_v24'
    ),
    AlCaLumiPixelsCountsExpress = cms.vstring('AlCa_LumiPixelsCounts_Random_v6'),
    AlCaLumiPixelsCountsPrompt = cms.vstring(
        'AlCa_LumiPixelsCounts_Random_v6',
        'AlCa_LumiPixelsCounts_ZeroBias_v6'
    ),
    AlCaP0 = cms.vstring(
        'AlCa_EcalEtaEBonly_v18',
        'AlCa_EcalEtaEEonly_v18',
        'AlCa_EcalPi0EBonly_v18',
        'AlCa_EcalPi0EEonly_v18'
    ),
    AlCaPPSExpress = cms.vstring(
        'HLT_PPSMaxTracksPerArm1_v4',
        'HLT_PPSMaxTracksPerRP4_v4'
    ),
    AlCaPPSPrompt = cms.vstring(
        'HLT_PPSMaxTracksPerArm1_v4',
        'HLT_PPSMaxTracksPerRP4_v4'
    ),
    AlCaPhiSym = cms.vstring('AlCa_EcalPhiSym_v13'),
    BTagMu = cms.vstring(
        'HLT_BTagMu_AK4DiJet110_Mu5_v17',
        'HLT_BTagMu_AK4DiJet170_Mu5_v16',
        'HLT_BTagMu_AK4DiJet20_Mu5_v17',
        'HLT_BTagMu_AK4DiJet40_Mu5_v17',
        'HLT_BTagMu_AK4DiJet70_Mu5_v17',
        'HLT_BTagMu_AK4Jet300_Mu5_v16',
        'HLT_BTagMu_AK8DiJet170_Mu5_v13',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v6',
        'HLT_BTagMu_AK8Jet300_Mu5_v16'
    ),
    Commissioning = cms.vstring(
        'HLT_IsoTrackHB_v8',
        'HLT_IsoTrackHE_v8',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v4',
        'HLT_PFJet40_GPUvsCPU_v2'
    ),
    Cosmics = cms.vstring('HLT_L1SingleMuCosmics_v3'),
    DQMGPUvsCPU = cms.vstring(
        'DQM_EcalReconstruction_v6',
        'DQM_HcalReconstruction_v5',
        'DQM_PixelReconstruction_v6'
    ),
    DQMOnlineBeamspot = cms.vstring(
        'HLT_HT300_Beamspot_v15',
        'HLT_ZeroBias_Beamspot_v8'
    ),
    DQMPPSRandom = cms.vstring('HLT_PPSRandom_v1'),
    DisplacedJet = cms.vstring(
        'HLT_CaloMET60_DTCluster50_v5',
        'HLT_CaloMET60_DTClusterNoMB1S50_v5',
        'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v5',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v5',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v5',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v5',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v5',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5_v5',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v5',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v5',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v5',
        'HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v2',
        'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v5',
        'HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v2',
        'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v5',
        'HLT_HT350_DelayedJet40_SingleDelay3nsInclusive_v1',
        'HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive_v1',
        'HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive_v1',
        'HLT_HT350_v1',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v17',
        'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v5',
        'HLT_HT425_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v4',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless_v1',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless_v1',
        'HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive_v1',
        'HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v3',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v3',
        'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v3',
        'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v5',
        'HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless_v1',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v3',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless_v1',
        'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v5',
        'HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive_v1',
        'HLT_HT550_DisplacedDijet60_Inclusive_v17',
        'HLT_L1MET_DTCluster50_v5',
        'HLT_L1MET_DTClusterNoMB1S50_v5',
        'HLT_L1Mu6HT240_v3',
        'HLT_L1SingleLLPJet_v2',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless_v3',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive_v3',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless_v3',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive_v3',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless_v3',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive_v3',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive_v1',
        'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v5',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v5',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v5',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v5',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v5',
        'HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5_v5',
        'HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5_v5',
        'HLT_PFJet200_TimeGt2p5ns_v2',
        'HLT_PFJet200_TimeLtNeg2p5ns_v2'
    ),
    EGamma0 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v8',
        'HLT_DiPhoton10Time1ns_v4',
        'HLT_DiPhoton10Time1p2ns_v4',
        'HLT_DiPhoton10Time1p4ns_v4',
        'HLT_DiPhoton10Time1p6ns_v4',
        'HLT_DiPhoton10Time1p8ns_v4',
        'HLT_DiPhoton10Time2ns_v4',
        'HLT_DiPhoton10_CaloIdL_v4',
        'HLT_DiPhoton10sminlt0p12_v4',
        'HLT_DiPhoton10sminlt0p1_v4',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v18',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v5',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v5',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v17',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v17',
        'HLT_DoubleEle25_CaloIdL_MW_v9',
        'HLT_DoubleEle27_CaloIdL_MW_v9',
        'HLT_DoubleEle33_CaloIdL_MW_v22',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v24',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v24',
        'HLT_DoublePhoton33_CaloIdL_v11',
        'HLT_DoublePhoton70_v11',
        'HLT_DoublePhoton85_v19',
        'HLT_ECALHT800_v14',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v19',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v22',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v12',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v20',
        'HLT_Ele15_IsoVVVL_PFHT450_v20',
        'HLT_Ele15_IsoVVVL_PFHT600_v24',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v13',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v20',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v22',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v22',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v23',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v5',
        'HLT_Ele28_HighEta_SC20_Mass55_v17',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v17',
        'HLT_Ele30_WPTight_Gsf_v5',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v17',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v13',
        'HLT_Ele32_WPTight_Gsf_v19',
        'HLT_Ele35_WPTight_Gsf_v13',
        'HLT_Ele38_WPTight_Gsf_v13',
        'HLT_Ele40_WPTight_Gsf_v13',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v4',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v4',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v22',
        'HLT_Ele50_IsoVVVL_PFHT450_v20',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v22',
        'HLT_Photon100EBHE10_v6',
        'HLT_Photon110EB_TightID_TightIso_v6',
        'HLT_Photon120_R9Id90_HE10_IsoM_v18',
        'HLT_Photon120_v17',
        'HLT_Photon130EB_TightID_TightIso_v2',
        'HLT_Photon150EB_TightID_TightIso_v2',
        'HLT_Photon150_v11',
        'HLT_Photon165_R9Id90_HE10_IsoM_v19',
        'HLT_Photon175EB_TightID_TightIso_v2',
        'HLT_Photon175_v19',
        'HLT_Photon200EB_TightID_TightIso_v2',
        'HLT_Photon200_v18',
        'HLT_Photon20_HoverELoose_v14',
        'HLT_Photon300_NoHE_v17',
        'HLT_Photon30EB_TightID_TightIso_v5',
        'HLT_Photon30_HoverELoose_v14',
        'HLT_Photon32_OneProng32_M50To105_v2',
        'HLT_Photon33_v9',
        'HLT_Photon35_TwoProngs35_v5',
        'HLT_Photon50EB_TightID_TightIso_v2',
        'HLT_Photon50_R9Id90_HE10_IsoM_v18',
        'HLT_Photon50_TimeGt2p5ns_v1',
        'HLT_Photon50_TimeLtNeg2p5ns_v1',
        'HLT_Photon50_v17',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v2',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v2',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v2',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v1',
        'HLT_Photon75EB_TightID_TightIso_v2',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v9',
        'HLT_Photon75_R9Id90_HE10_IsoM_v18',
        'HLT_Photon75_v17',
        'HLT_Photon90EB_TightID_TightIso_v2',
        'HLT_Photon90_R9Id90_HE10_IsoM_v18',
        'HLT_Photon90_v17'
    ),
    EGamma1 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v8',
        'HLT_DiPhoton10Time1ns_v4',
        'HLT_DiPhoton10Time1p2ns_v4',
        'HLT_DiPhoton10Time1p4ns_v4',
        'HLT_DiPhoton10Time1p6ns_v4',
        'HLT_DiPhoton10Time1p8ns_v4',
        'HLT_DiPhoton10Time2ns_v4',
        'HLT_DiPhoton10_CaloIdL_v4',
        'HLT_DiPhoton10sminlt0p12_v4',
        'HLT_DiPhoton10sminlt0p1_v4',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v18',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v5',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v5',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v17',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v17',
        'HLT_DoubleEle25_CaloIdL_MW_v9',
        'HLT_DoubleEle27_CaloIdL_MW_v9',
        'HLT_DoubleEle33_CaloIdL_MW_v22',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v24',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v24',
        'HLT_DoublePhoton33_CaloIdL_v11',
        'HLT_DoublePhoton70_v11',
        'HLT_DoublePhoton85_v19',
        'HLT_ECALHT800_v14',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v19',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v22',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v12',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v20',
        'HLT_Ele15_IsoVVVL_PFHT450_v20',
        'HLT_Ele15_IsoVVVL_PFHT600_v24',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v13',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v20',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v22',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v22',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v23',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v5',
        'HLT_Ele28_HighEta_SC20_Mass55_v17',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v17',
        'HLT_Ele30_WPTight_Gsf_v5',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v17',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v13',
        'HLT_Ele32_WPTight_Gsf_v19',
        'HLT_Ele35_WPTight_Gsf_v13',
        'HLT_Ele38_WPTight_Gsf_v13',
        'HLT_Ele40_WPTight_Gsf_v13',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v4',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v4',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v22',
        'HLT_Ele50_IsoVVVL_PFHT450_v20',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v22',
        'HLT_Photon100EBHE10_v6',
        'HLT_Photon110EB_TightID_TightIso_v6',
        'HLT_Photon120_R9Id90_HE10_IsoM_v18',
        'HLT_Photon120_v17',
        'HLT_Photon130EB_TightID_TightIso_v2',
        'HLT_Photon150EB_TightID_TightIso_v2',
        'HLT_Photon150_v11',
        'HLT_Photon165_R9Id90_HE10_IsoM_v19',
        'HLT_Photon175EB_TightID_TightIso_v2',
        'HLT_Photon175_v19',
        'HLT_Photon200EB_TightID_TightIso_v2',
        'HLT_Photon200_v18',
        'HLT_Photon20_HoverELoose_v14',
        'HLT_Photon300_NoHE_v17',
        'HLT_Photon30EB_TightID_TightIso_v5',
        'HLT_Photon30_HoverELoose_v14',
        'HLT_Photon32_OneProng32_M50To105_v2',
        'HLT_Photon33_v9',
        'HLT_Photon35_TwoProngs35_v5',
        'HLT_Photon50EB_TightID_TightIso_v2',
        'HLT_Photon50_R9Id90_HE10_IsoM_v18',
        'HLT_Photon50_TimeGt2p5ns_v1',
        'HLT_Photon50_TimeLtNeg2p5ns_v1',
        'HLT_Photon50_v17',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v2',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v2',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v2',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v1',
        'HLT_Photon75EB_TightID_TightIso_v2',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v9',
        'HLT_Photon75_R9Id90_HE10_IsoM_v18',
        'HLT_Photon75_v17',
        'HLT_Photon90EB_TightID_TightIso_v2',
        'HLT_Photon90_R9Id90_HE10_IsoM_v18',
        'HLT_Photon90_v17'
    ),
    EcalLaser = cms.vstring('HLT_EcalCalibration_v4'),
    EphemeralHLTPhysics0 = cms.vstring('HLT_EphemeralPhysics_v4'),
    EphemeralHLTPhysics1 = cms.vstring('HLT_EphemeralPhysics_v4'),
    EphemeralHLTPhysics2 = cms.vstring('HLT_EphemeralPhysics_v4'),
    EphemeralHLTPhysics3 = cms.vstring('HLT_EphemeralPhysics_v4'),
    EphemeralHLTPhysics4 = cms.vstring('HLT_EphemeralPhysics_v4'),
    EphemeralHLTPhysics5 = cms.vstring('HLT_EphemeralPhysics_v4'),
    EphemeralHLTPhysics6 = cms.vstring('HLT_EphemeralPhysics_v4'),
    EphemeralHLTPhysics7 = cms.vstring('HLT_EphemeralPhysics_v4'),
    EphemeralZeroBias0 = cms.vstring('HLT_EphemeralZeroBias_v4'),
    EphemeralZeroBias1 = cms.vstring('HLT_EphemeralZeroBias_v4'),
    EphemeralZeroBias2 = cms.vstring('HLT_EphemeralZeroBias_v4'),
    EphemeralZeroBias3 = cms.vstring('HLT_EphemeralZeroBias_v4'),
    EphemeralZeroBias4 = cms.vstring('HLT_EphemeralZeroBias_v4'),
    EphemeralZeroBias5 = cms.vstring('HLT_EphemeralZeroBias_v4'),
    EphemeralZeroBias6 = cms.vstring('HLT_EphemeralZeroBias_v4'),
    EphemeralZeroBias7 = cms.vstring('HLT_EphemeralZeroBias_v4'),
    EventDisplay = cms.vstring(
        'HLT_DoublePhoton85_v19',
        'HLT_PFJet500_v25'
    ),
    ExpressAlignment = cms.vstring(
        'HLT_HT300_Beamspot_v15',
        'HLT_ZeroBias_Beamspot_v8'
    ),
    ExpressPhysics = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v23',
        'HLT_IsoMu20_v19',
        'HLT_IsoMu24_v17',
        'HLT_IsoMu27_v20',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v9',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v19',
        'HLT_Physics_v9',
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v3',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v7',
        'HLT_ZeroBias_IsolatedBunches_v7',
        'HLT_ZeroBias_v8'
    ),
    HLTMonitor = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v23',
        'HLT_Ele32_WPTight_Gsf_v19',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v4',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v17',
        'HLT_HT550_DisplacedDijet60_Inclusive_v17',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v4',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v5',
        'HLT_PFHT510_v21',
        'HLT_PFJet260_v24',
        'HLT_PFJet320_v24',
        'HLT_PFMET130_PFMHT130_IDTight_v24',
        'HLT_PFMET140_PFMHT140_IDTight_v24'
    ),
    HLTPhysics = cms.vstring('HLT_Physics_v9'),
    HcalNZS = cms.vstring(
        'HLT_HcalNZS_v16',
        'HLT_HcalPhiSym_v18'
    ),
    JetMET0 = cms.vstring(
        'HLT_AK8DiPFJet250_250_MassSD30_v4',
        'HLT_AK8DiPFJet250_250_MassSD50_v4',
        'HLT_AK8DiPFJet260_260_MassSD30_v4',
        'HLT_AK8DiPFJet260_260_MassSD50_v4',
        'HLT_AK8DiPFJet270_270_MassSD30_v4',
        'HLT_AK8DiPFJet280_280_MassSD30_v4',
        'HLT_AK8DiPFJet290_290_MassSD30_v4',
        'HLT_AK8PFJet140_v19',
        'HLT_AK8PFJet200_v19',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v1',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53_v1',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55_v1',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60_v1',
        'HLT_AK8PFJet220_SoftDropMass40_v5',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03_v1',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05_v1',
        'HLT_AK8PFJet230_SoftDropMass40_v5',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06_v1',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10_v1',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03_v1',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05_v1',
        'HLT_AK8PFJet260_v20',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06_v1',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10_v1',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03_v1',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05_v1',
        'HLT_AK8PFJet320_v20',
        'HLT_AK8PFJet400_MassSD30_v4',
        'HLT_AK8PFJet400_v20',
        'HLT_AK8PFJet40_v20',
        'HLT_AK8PFJet420_MassSD30_v4',
        'HLT_AK8PFJet425_SoftDropMass40_v5',
        'HLT_AK8PFJet450_MassSD30_v4',
        'HLT_AK8PFJet450_SoftDropMass40_v5',
        'HLT_AK8PFJet450_v20',
        'HLT_AK8PFJet470_MassSD30_v4',
        'HLT_AK8PFJet500_MassSD30_v4',
        'HLT_AK8PFJet500_v20',
        'HLT_AK8PFJet550_v15',
        'HLT_AK8PFJet60_v19',
        'HLT_AK8PFJet80_v20',
        'HLT_AK8PFJetFwd140_v18',
        'HLT_AK8PFJetFwd15_v7',
        'HLT_AK8PFJetFwd200_v18',
        'HLT_AK8PFJetFwd25_v7',
        'HLT_AK8PFJetFwd260_v19',
        'HLT_AK8PFJetFwd320_v19',
        'HLT_AK8PFJetFwd400_v19',
        'HLT_AK8PFJetFwd40_v19',
        'HLT_AK8PFJetFwd450_v19',
        'HLT_AK8PFJetFwd500_v19',
        'HLT_AK8PFJetFwd60_v18',
        'HLT_AK8PFJetFwd80_v18',
        'HLT_CaloJet500_NoJetID_v16',
        'HLT_CaloJet550_NoJetID_v11',
        'HLT_CaloMET350_NotCleaned_v8',
        'HLT_CaloMET90_NotCleaned_v8',
        'HLT_CaloMHT90_v8',
        'HLT_DiPFJetAve100_HFJEC_v21',
        'HLT_DiPFJetAve140_v17',
        'HLT_DiPFJetAve160_HFJEC_v20',
        'HLT_DiPFJetAve200_v17',
        'HLT_DiPFJetAve220_HFJEC_v20',
        'HLT_DiPFJetAve260_HFJEC_v3',
        'HLT_DiPFJetAve260_v18',
        'HLT_DiPFJetAve300_HFJEC_v20',
        'HLT_DiPFJetAve320_v18',
        'HLT_DiPFJetAve400_v18',
        'HLT_DiPFJetAve40_v18',
        'HLT_DiPFJetAve500_v18',
        'HLT_DiPFJetAve60_HFJEC_v19',
        'HLT_DiPFJetAve60_v18',
        'HLT_DiPFJetAve80_HFJEC_v21',
        'HLT_DiPFJetAve80_v18',
        'HLT_DoublePFJets100_PFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets200_PFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets350_PFBTagDeepJet_p71_v6',
        'HLT_DoublePFJets40_PFBTagDeepJet_p71_v5',
        'HLT_L1ETMHadSeeds_v5',
        'HLT_MET105_IsoTrk50_v13',
        'HLT_MET120_IsoTrk50_v13',
        'HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_Mu12eta2p3_PFJet40_v5',
        'HLT_Mu12eta2p3_v5',
        'HLT_PFHT1050_v22',
        'HLT_PFHT180_v21',
        'HLT_PFHT250_v21',
        'HLT_PFHT350_v23',
        'HLT_PFHT370_v21',
        'HLT_PFHT430_v21',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v16',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v16',
        'HLT_PFHT510_v21',
        'HLT_PFHT590_v21',
        'HLT_PFHT680_v21',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v16',
        'HLT_PFHT780_v21',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v16',
        'HLT_PFHT890_v21',
        'HLT_PFJet110_v4',
        'HLT_PFJet140_v23',
        'HLT_PFJet200_v23',
        'HLT_PFJet260_v24',
        'HLT_PFJet320_v24',
        'HLT_PFJet400_v24',
        'HLT_PFJet40_v25',
        'HLT_PFJet450_v25',
        'HLT_PFJet500_v25',
        'HLT_PFJet550_v15',
        'HLT_PFJet60_v25',
        'HLT_PFJet80_v25',
        'HLT_PFJetFwd140_v22',
        'HLT_PFJetFwd200_v22',
        'HLT_PFJetFwd260_v23',
        'HLT_PFJetFwd320_v23',
        'HLT_PFJetFwd400_v23',
        'HLT_PFJetFwd40_v23',
        'HLT_PFJetFwd450_v23',
        'HLT_PFJetFwd500_v23',
        'HLT_PFJetFwd60_v23',
        'HLT_PFJetFwd80_v22',
        'HLT_PFMET105_IsoTrk50_v5',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v13',
        'HLT_PFMET120_PFMHT120_IDTight_v24',
        'HLT_PFMET130_PFMHT130_IDTight_v24',
        'HLT_PFMET140_PFMHT140_IDTight_v24',
        'HLT_PFMET200_BeamHaloCleaned_v13',
        'HLT_PFMET200_NotCleaned_v13',
        'HLT_PFMET250_NotCleaned_v13',
        'HLT_PFMET300_NotCleaned_v13',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v13',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v24',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v23',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v23',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v15',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v13',
        'HLT_QuadPFJet100_88_70_30_v2',
        'HLT_QuadPFJet103_88_75_15_v9',
        'HLT_QuadPFJet105_88_75_30_v1',
        'HLT_QuadPFJet105_88_76_15_v9',
        'HLT_QuadPFJet111_90_80_15_v9',
        'HLT_QuadPFJet111_90_80_30_v1'
    ),
    JetMET1 = cms.vstring(
        'HLT_AK8DiPFJet250_250_MassSD30_v4',
        'HLT_AK8DiPFJet250_250_MassSD50_v4',
        'HLT_AK8DiPFJet260_260_MassSD30_v4',
        'HLT_AK8DiPFJet260_260_MassSD50_v4',
        'HLT_AK8DiPFJet270_270_MassSD30_v4',
        'HLT_AK8DiPFJet280_280_MassSD30_v4',
        'HLT_AK8DiPFJet290_290_MassSD30_v4',
        'HLT_AK8PFJet140_v19',
        'HLT_AK8PFJet200_v19',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v1',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53_v1',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55_v1',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60_v1',
        'HLT_AK8PFJet220_SoftDropMass40_v5',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03_v1',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05_v1',
        'HLT_AK8PFJet230_SoftDropMass40_v5',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06_v1',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10_v1',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03_v1',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05_v1',
        'HLT_AK8PFJet260_v20',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06_v1',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10_v1',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03_v1',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05_v1',
        'HLT_AK8PFJet320_v20',
        'HLT_AK8PFJet400_MassSD30_v4',
        'HLT_AK8PFJet400_v20',
        'HLT_AK8PFJet40_v20',
        'HLT_AK8PFJet420_MassSD30_v4',
        'HLT_AK8PFJet425_SoftDropMass40_v5',
        'HLT_AK8PFJet450_MassSD30_v4',
        'HLT_AK8PFJet450_SoftDropMass40_v5',
        'HLT_AK8PFJet450_v20',
        'HLT_AK8PFJet470_MassSD30_v4',
        'HLT_AK8PFJet500_MassSD30_v4',
        'HLT_AK8PFJet500_v20',
        'HLT_AK8PFJet550_v15',
        'HLT_AK8PFJet60_v19',
        'HLT_AK8PFJet80_v20',
        'HLT_AK8PFJetFwd140_v18',
        'HLT_AK8PFJetFwd15_v7',
        'HLT_AK8PFJetFwd200_v18',
        'HLT_AK8PFJetFwd25_v7',
        'HLT_AK8PFJetFwd260_v19',
        'HLT_AK8PFJetFwd320_v19',
        'HLT_AK8PFJetFwd400_v19',
        'HLT_AK8PFJetFwd40_v19',
        'HLT_AK8PFJetFwd450_v19',
        'HLT_AK8PFJetFwd500_v19',
        'HLT_AK8PFJetFwd60_v18',
        'HLT_AK8PFJetFwd80_v18',
        'HLT_CaloJet500_NoJetID_v16',
        'HLT_CaloJet550_NoJetID_v11',
        'HLT_CaloMET350_NotCleaned_v8',
        'HLT_CaloMET90_NotCleaned_v8',
        'HLT_CaloMHT90_v8',
        'HLT_DiPFJetAve100_HFJEC_v21',
        'HLT_DiPFJetAve140_v17',
        'HLT_DiPFJetAve160_HFJEC_v20',
        'HLT_DiPFJetAve200_v17',
        'HLT_DiPFJetAve220_HFJEC_v20',
        'HLT_DiPFJetAve260_HFJEC_v3',
        'HLT_DiPFJetAve260_v18',
        'HLT_DiPFJetAve300_HFJEC_v20',
        'HLT_DiPFJetAve320_v18',
        'HLT_DiPFJetAve400_v18',
        'HLT_DiPFJetAve40_v18',
        'HLT_DiPFJetAve500_v18',
        'HLT_DiPFJetAve60_HFJEC_v19',
        'HLT_DiPFJetAve60_v18',
        'HLT_DiPFJetAve80_HFJEC_v21',
        'HLT_DiPFJetAve80_v18',
        'HLT_DoublePFJets100_PFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets200_PFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets350_PFBTagDeepJet_p71_v6',
        'HLT_DoublePFJets40_PFBTagDeepJet_p71_v5',
        'HLT_L1ETMHadSeeds_v5',
        'HLT_MET105_IsoTrk50_v13',
        'HLT_MET120_IsoTrk50_v13',
        'HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_Mu12eta2p3_PFJet40_v5',
        'HLT_Mu12eta2p3_v5',
        'HLT_PFHT1050_v22',
        'HLT_PFHT180_v21',
        'HLT_PFHT250_v21',
        'HLT_PFHT350_v23',
        'HLT_PFHT370_v21',
        'HLT_PFHT430_v21',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v16',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v16',
        'HLT_PFHT510_v21',
        'HLT_PFHT590_v21',
        'HLT_PFHT680_v21',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v16',
        'HLT_PFHT780_v21',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v16',
        'HLT_PFHT890_v21',
        'HLT_PFJet110_v4',
        'HLT_PFJet140_v23',
        'HLT_PFJet200_v23',
        'HLT_PFJet260_v24',
        'HLT_PFJet320_v24',
        'HLT_PFJet400_v24',
        'HLT_PFJet40_v25',
        'HLT_PFJet450_v25',
        'HLT_PFJet500_v25',
        'HLT_PFJet550_v15',
        'HLT_PFJet60_v25',
        'HLT_PFJet80_v25',
        'HLT_PFJetFwd140_v22',
        'HLT_PFJetFwd200_v22',
        'HLT_PFJetFwd260_v23',
        'HLT_PFJetFwd320_v23',
        'HLT_PFJetFwd400_v23',
        'HLT_PFJetFwd40_v23',
        'HLT_PFJetFwd450_v23',
        'HLT_PFJetFwd500_v23',
        'HLT_PFJetFwd60_v23',
        'HLT_PFJetFwd80_v22',
        'HLT_PFMET105_IsoTrk50_v5',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v13',
        'HLT_PFMET120_PFMHT120_IDTight_v24',
        'HLT_PFMET130_PFMHT130_IDTight_v24',
        'HLT_PFMET140_PFMHT140_IDTight_v24',
        'HLT_PFMET200_BeamHaloCleaned_v13',
        'HLT_PFMET200_NotCleaned_v13',
        'HLT_PFMET250_NotCleaned_v13',
        'HLT_PFMET300_NotCleaned_v13',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v13',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v24',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v23',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v23',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v15',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v13',
        'HLT_QuadPFJet100_88_70_30_v2',
        'HLT_QuadPFJet103_88_75_15_v9',
        'HLT_QuadPFJet105_88_75_30_v1',
        'HLT_QuadPFJet105_88_76_15_v9',
        'HLT_QuadPFJet111_90_80_15_v9',
        'HLT_QuadPFJet111_90_80_30_v1'
    ),
    L1Accept = cms.vstring(
        'DST_Physics_v9',
        'DST_ZeroBias_v4'
    ),
    MonteCarlo = cms.vstring(
        'MC_AK4CaloJetsFromPV_v12',
        'MC_AK4CaloJets_v13',
        'MC_AK4PFJets_v21',
        'MC_AK8CaloHT_v12',
        'MC_AK8PFHT_v20',
        'MC_AK8PFJets_v21',
        'MC_AK8TrimPFJets_v21',
        'MC_CaloBTagDeepCSV_v12',
        'MC_CaloHT_v12',
        'MC_CaloMET_JetIdCleaned_v13',
        'MC_CaloMET_v12',
        'MC_CaloMHT_v12',
        'MC_Diphoton10_10_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass10_v17',
        'MC_DoubleEle5_CaloIdL_MW_v20',
        'MC_DoubleMuNoFiltersNoVtx_v11',
        'MC_DoubleMu_TrkIsoVVL_DZ_v15',
        'MC_Egamma_Open_Unseeded_v2',
        'MC_Egamma_Open_v2',
        'MC_Ele15_Ele10_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'MC_Ele5_WPTight_Gsf_v12',
        'MC_IsoMu_v19',
        'MC_PFBTagDeepCSV_v14',
        'MC_PFBTagDeepJet_v5',
        'MC_PFHT_v20',
        'MC_PFMET_v21',
        'MC_PFMHT_v20',
        'MC_QuadPFJet100_75_50_30_PNet2CvsL0p3And1CvsL0p5_VBF3Tight_v2',
        'MC_ReducedIterativeTracking_v16',
        'MC_Run3_PFScoutingPixelTracking_v20'
    ),
    Muon0 = cms.vstring(
        'HLT_CascadeMu100_v7',
        'HLT_CscCluster_Loose_v4',
        'HLT_CscCluster_Medium_v4',
        'HLT_CscCluster_Tight_v4',
        'HLT_DoubleCscCluster100_v1',
        'HLT_DoubleCscCluster75_v1',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v5',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v5',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v5',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v5',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v5',
        'HLT_DoubleL2Mu50_v5',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v4',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v4',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v5',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v4',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v4',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v4',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v14',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v14',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v14',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v14',
        'HLT_DoubleMu43NoFiltersNoVtx_v8',
        'HLT_DoubleMu48NoFiltersNoVtx_v8',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v12',
        'HLT_HighPtTkMu100_v6',
        'HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v5',
        'HLT_IsoMu20_v19',
        'HLT_IsoMu24_OneProng32_v1',
        'HLT_IsoMu24_TwoProngs35_v5',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v5',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v5',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v5',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_v19',
        'HLT_IsoMu24_v17',
        'HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v4',
        'HLT_IsoMu27_v20',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06_v1',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_v4',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v4',
        'HLT_L1CSCShower_DTCluster50_v4',
        'HLT_L1CSCShower_DTCluster75_v4',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v4',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v19',
        'HLT_Mu15_IsoVVVL_PFHT450_v19',
        'HLT_Mu15_IsoVVVL_PFHT600_v23',
        'HLT_Mu15_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v9',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v9',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v18',
        'HLT_Mu17_TrkIsoVVL_v17',
        'HLT_Mu17_v17',
        'HLT_Mu18_Mu9_SameSign_v8',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v7',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v7',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v7',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v7',
        'HLT_Mu19_TrkIsoVVL_v8',
        'HLT_Mu19_v8',
        'HLT_Mu20_v16',
        'HLT_Mu27_v17',
        'HLT_Mu37_TkMu27_v9',
        'HLT_Mu3_PFJet40_v20',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v6',
        'HLT_Mu50_IsoVVVL_PFHT450_v19',
        'HLT_Mu50_L1SingleMuShower_v3',
        'HLT_Mu50_v17',
        'HLT_Mu55_v7',
        'HLT_Mu8_TrkIsoVVL_v16',
        'HLT_Mu8_v16',
        'HLT_TripleMu_10_5_5_DZ_v14',
        'HLT_TripleMu_12_10_5_v14',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v7',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v12',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v10'
    ),
    Muon1 = cms.vstring(
        'HLT_CascadeMu100_v7',
        'HLT_CscCluster_Loose_v4',
        'HLT_CscCluster_Medium_v4',
        'HLT_CscCluster_Tight_v4',
        'HLT_DoubleCscCluster100_v1',
        'HLT_DoubleCscCluster75_v1',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v5',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v5',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v5',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v5',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v5',
        'HLT_DoubleL2Mu50_v5',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v4',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v4',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v5',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v4',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v4',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v4',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v14',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v14',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v14',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v14',
        'HLT_DoubleMu43NoFiltersNoVtx_v8',
        'HLT_DoubleMu48NoFiltersNoVtx_v8',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v12',
        'HLT_HighPtTkMu100_v6',
        'HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v5',
        'HLT_IsoMu20_v19',
        'HLT_IsoMu24_OneProng32_v1',
        'HLT_IsoMu24_TwoProngs35_v5',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v5',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v5',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v5',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_v19',
        'HLT_IsoMu24_v17',
        'HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v4',
        'HLT_IsoMu27_v20',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06_v1',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_v4',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v4',
        'HLT_L1CSCShower_DTCluster50_v4',
        'HLT_L1CSCShower_DTCluster75_v4',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v4',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v19',
        'HLT_Mu15_IsoVVVL_PFHT450_v19',
        'HLT_Mu15_IsoVVVL_PFHT600_v23',
        'HLT_Mu15_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v9',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v9',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v18',
        'HLT_Mu17_TrkIsoVVL_v17',
        'HLT_Mu17_v17',
        'HLT_Mu18_Mu9_SameSign_v8',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v7',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v7',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v7',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v7',
        'HLT_Mu19_TrkIsoVVL_v8',
        'HLT_Mu19_v8',
        'HLT_Mu20_v16',
        'HLT_Mu27_v17',
        'HLT_Mu37_TkMu27_v9',
        'HLT_Mu3_PFJet40_v20',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v6',
        'HLT_Mu50_IsoVVVL_PFHT450_v19',
        'HLT_Mu50_L1SingleMuShower_v3',
        'HLT_Mu50_v17',
        'HLT_Mu55_v7',
        'HLT_Mu8_TrkIsoVVL_v16',
        'HLT_Mu8_v16',
        'HLT_TripleMu_10_5_5_DZ_v14',
        'HLT_TripleMu_12_10_5_v14',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v7',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v12',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v10'
    ),
    MuonEG = cms.vstring(
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v21',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v21',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v21',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v11',
        'HLT_Mu17_Photon30_IsoCaloId_v10',
        'HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId_v5',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v11',
        'HLT_Mu27_Ele37_CaloIdL_MW_v9',
        'HLT_Mu37_Ele27_CaloIdL_MW_v9',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v5',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v5',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v9',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v9',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v22',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v22',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v23',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v23',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v5',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v5',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v5',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v17',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v15'
    ),
    NoBPTX = cms.vstring(
        'HLT_CDC_L2cosmic_10_er1p0_v4',
        'HLT_CDC_L2cosmic_5p5_er1p0_v4',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v8',
        'HLT_L2Mu10_NoVertex_NoBPTX_v9',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v8',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v7',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v9',
        'HLT_UncorrectedJetE30_NoBPTX_v9',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v9',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v9'
    ),
    OnlineMonitor = cms.vstring( (
        'HLT_AK8DiPFJet250_250_MassSD30_v4',
        'HLT_AK8DiPFJet250_250_MassSD50_v4',
        'HLT_AK8DiPFJet260_260_MassSD30_v4',
        'HLT_AK8DiPFJet260_260_MassSD50_v4',
        'HLT_AK8DiPFJet270_270_MassSD30_v4',
        'HLT_AK8DiPFJet280_280_MassSD30_v4',
        'HLT_AK8DiPFJet290_290_MassSD30_v4',
        'HLT_AK8PFJet140_v19',
        'HLT_AK8PFJet200_v19',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v1',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53_v1',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55_v1',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60_v1',
        'HLT_AK8PFJet220_SoftDropMass40_v5',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03_v1',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05_v1',
        'HLT_AK8PFJet230_SoftDropMass40_v5',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06_v1',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10_v1',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03_v1',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05_v1',
        'HLT_AK8PFJet260_v20',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06_v1',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10_v1',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03_v1',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05_v1',
        'HLT_AK8PFJet320_v20',
        'HLT_AK8PFJet400_MassSD30_v4',
        'HLT_AK8PFJet400_v20',
        'HLT_AK8PFJet40_v20',
        'HLT_AK8PFJet420_MassSD30_v4',
        'HLT_AK8PFJet425_SoftDropMass40_v5',
        'HLT_AK8PFJet450_MassSD30_v4',
        'HLT_AK8PFJet450_SoftDropMass40_v5',
        'HLT_AK8PFJet450_v20',
        'HLT_AK8PFJet470_MassSD30_v4',
        'HLT_AK8PFJet500_MassSD30_v4',
        'HLT_AK8PFJet500_v20',
        'HLT_AK8PFJet550_v15',
        'HLT_AK8PFJet60_v19',
        'HLT_AK8PFJet80_v20',
        'HLT_AK8PFJetFwd140_v18',
        'HLT_AK8PFJetFwd15_v7',
        'HLT_AK8PFJetFwd200_v18',
        'HLT_AK8PFJetFwd25_v7',
        'HLT_AK8PFJetFwd260_v19',
        'HLT_AK8PFJetFwd320_v19',
        'HLT_AK8PFJetFwd400_v19',
        'HLT_AK8PFJetFwd40_v19',
        'HLT_AK8PFJetFwd450_v19',
        'HLT_AK8PFJetFwd500_v19',
        'HLT_AK8PFJetFwd60_v18',
        'HLT_AK8PFJetFwd80_v18',
        'HLT_BTagMu_AK4DiJet110_Mu5_v17',
        'HLT_BTagMu_AK4DiJet170_Mu5_v16',
        'HLT_BTagMu_AK4DiJet20_Mu5_v17',
        'HLT_BTagMu_AK4DiJet40_Mu5_v17',
        'HLT_BTagMu_AK4DiJet70_Mu5_v17',
        'HLT_BTagMu_AK4Jet300_Mu5_v16',
        'HLT_BTagMu_AK8DiJet170_Mu5_v13',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v6',
        'HLT_BTagMu_AK8Jet300_Mu5_v16',
        'HLT_CDC_L2cosmic_10_er1p0_v4',
        'HLT_CDC_L2cosmic_5p5_er1p0_v4',
        'HLT_CaloJet500_NoJetID_v16',
        'HLT_CaloJet550_NoJetID_v11',
        'HLT_CaloMET350_NotCleaned_v8',
        'HLT_CaloMET60_DTCluster50_v5',
        'HLT_CaloMET60_DTClusterNoMB1S50_v5',
        'HLT_CaloMET90_NotCleaned_v8',
        'HLT_CaloMHT90_v8',
        'HLT_CascadeMu100_v7',
        'HLT_CscCluster_Loose_v4',
        'HLT_CscCluster_Medium_v4',
        'HLT_CscCluster_Tight_v4',
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v8',
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v21',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v21',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v21',
        'HLT_DiPFJetAve100_HFJEC_v21',
        'HLT_DiPFJetAve140_v17',
        'HLT_DiPFJetAve160_HFJEC_v20',
        'HLT_DiPFJetAve200_v17',
        'HLT_DiPFJetAve220_HFJEC_v20',
        'HLT_DiPFJetAve260_HFJEC_v3',
        'HLT_DiPFJetAve260_v18',
        'HLT_DiPFJetAve300_HFJEC_v20',
        'HLT_DiPFJetAve320_v18',
        'HLT_DiPFJetAve400_v18',
        'HLT_DiPFJetAve40_v18',
        'HLT_DiPFJetAve500_v18',
        'HLT_DiPFJetAve60_HFJEC_v19',
        'HLT_DiPFJetAve60_v18',
        'HLT_DiPFJetAve80_HFJEC_v21',
        'HLT_DiPFJetAve80_v18',
        'HLT_DiPhoton10Time1ns_v4',
        'HLT_DiPhoton10Time1p2ns_v4',
        'HLT_DiPhoton10Time1p4ns_v4',
        'HLT_DiPhoton10Time1p6ns_v4',
        'HLT_DiPhoton10Time1p8ns_v4',
        'HLT_DiPhoton10Time2ns_v4',
        'HLT_DiPhoton10_CaloIdL_v4',
        'HLT_DiPhoton10sminlt0p12_v4',
        'HLT_DiPhoton10sminlt0p1_v4',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v18',
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon10_Upsilon_y1p4_v5',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v9',
        'HLT_Dimuon14_PsiPrime_v17',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v4',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v5',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v5',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v17',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v17',
        'HLT_DoubleCscCluster100_v1',
        'HLT_DoubleCscCluster75_v1',
        'HLT_DoubleEle25_CaloIdL_MW_v9',
        'HLT_DoubleEle27_CaloIdL_MW_v9',
        'HLT_DoubleEle33_CaloIdL_MW_v22',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v24',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v24',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v5',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v4',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v5',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v5',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v5',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v5',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v5',
        'HLT_DoubleL2Mu50_v5',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v4',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v4',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v5',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v4',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v4',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v4',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_v5',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_M5to80_v2',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_v4',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_v4',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v14',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v14',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v14',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v14',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu43NoFiltersNoVtx_v8',
        'HLT_DoubleMu48NoFiltersNoVtx_v8',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_JpsiTrk_Bc_v4',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v12',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_DoublePFJets100_PFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets200_PFBTagDeepJet_p71_v5',
        'HLT_DoublePFJets350_PFBTagDeepJet_p71_v6',
        'HLT_DoublePFJets40_PFBTagDeepJet_p71_v5',
        'HLT_DoublePhoton33_CaloIdL_v11',
        'HLT_DoublePhoton70_v11',
        'HLT_DoublePhoton85_v19',
        'HLT_ECALHT800_v14',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v19',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v22',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v12',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v20',
        'HLT_Ele15_IsoVVVL_PFHT450_v20',
        'HLT_Ele15_IsoVVVL_PFHT600_v24',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v13',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v20',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v22',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v22',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v23',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23',
        'HLT_Ele28_HighEta_SC20_Mass55_v17',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v17',
        'HLT_Ele30_WPTight_Gsf_v5',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v17',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v13',
        'HLT_Ele32_WPTight_Gsf_v19',
        'HLT_Ele35_WPTight_Gsf_v13',
        'HLT_Ele38_WPTight_Gsf_v13',
        'HLT_Ele40_WPTight_Gsf_v13',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v4',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v4',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v22',
        'HLT_Ele50_IsoVVVL_PFHT450_v20',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v20',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v22',
        'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v5',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v5',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v5',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v5',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v5',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5_v5',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v5',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v5',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v5',
        'HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v2',
        'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v5',
        'HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v2',
        'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v5',
        'HLT_HT350_DelayedJet40_SingleDelay3nsInclusive_v1',
        'HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive_v1',
        'HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive_v1',
        'HLT_HT350_v1',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v17',
        'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v5',
        'HLT_HT425_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v4',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless_v1',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless_v1',
        'HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive_v1',
        'HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v3',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v3',
        'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v3',
        'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v5',
        'HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless_v1',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v3',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless_v1',
        'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v5',
        'HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive_v1',
        'HLT_HT550_DisplacedDijet60_Inclusive_v17',
        'HLT_HcalNZS_v16',
        'HLT_HcalPhiSym_v18',
        'HLT_HighPtTkMu100_v6',
        'HLT_IsoMu20_v19',
        'HLT_IsoMu24_OneProng32_v1',
        'HLT_IsoMu24_TwoProngs35_v5',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v5',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v5',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v5',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_v19',
        'HLT_IsoMu24_v17',
        'HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v4',
        'HLT_IsoMu27_v20',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06_v1',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_v4',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v1',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v1',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v4',
        'HLT_IsoTrackHB_v8',
        'HLT_IsoTrackHE_v8',
        'HLT_L1CSCShower_DTCluster50_v4',
        'HLT_L1CSCShower_DTCluster75_v4',
        'HLT_L1ETMHadSeeds_v5',
        'HLT_L1MET_DTCluster50_v5',
        'HLT_L1MET_DTClusterNoMB1S50_v5',
        'HLT_L1Mu6HT240_v3',
        'HLT_L1SingleLLPJet_v2',
        'HLT_L1SingleMuCosmics_v3',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless_v3',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive_v3',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless_v3',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive_v3',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless_v3',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive_v3',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive_v1',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v4',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v8',
        'HLT_L2Mu10_NoVertex_NoBPTX_v9',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v8',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v7',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v4',
        'HLT_MET105_IsoTrk50_v13',
        'HLT_MET120_IsoTrk50_v13',
        'HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71_v5',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71_v5',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v11',
        'HLT_Mu12eta2p3_PFJet40_v5',
        'HLT_Mu12eta2p3_v5',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v19',
        'HLT_Mu15_IsoVVVL_PFHT450_v19',
        'HLT_Mu15_IsoVVVL_PFHT600_v23',
        'HLT_Mu15_v7',
        'HLT_Mu17_Photon30_IsoCaloId_v10',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v9',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v9',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v18',
        'HLT_Mu17_TrkIsoVVL_v17',
        'HLT_Mu17_v17',
        'HLT_Mu18_Mu9_SameSign_v8',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v7',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v7',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v7',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v7',
        'HLT_Mu19_TrkIsoVVL_v8',
        'HLT_Mu19_v8',
        'HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId_v5',
        'HLT_Mu20_v16',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v19',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v11',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu27_Ele37_CaloIdL_MW_v9',
        'HLT_Mu27_v17',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu37_Ele27_CaloIdL_MW_v9',
        'HLT_Mu37_TkMu27_v9',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v5',
        'HLT_Mu3_PFJet40_v20',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v6',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v6',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v5',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v9',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v9',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu50_IsoVVVL_PFHT450_v19',
        'HLT_Mu50_L1SingleMuShower_v3',
        'HLT_Mu50_v17',
        'HLT_Mu55_v7',
        'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v5',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v5',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v5',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v5',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v5',
        'HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5_v5',
        'HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v22',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v22',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v23',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v23',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v5',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v5',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v5',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_v1',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v17',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v15',
        'HLT_Mu8_TrkIsoVVL_v16',
        'HLT_Mu8_v16',
        'HLT_PFHT1050_v22',
        'HLT_PFHT180_v21',
        'HLT_PFHT250_v21',
        'HLT_PFHT350_v23',
        'HLT_PFHT370_v21',
        'HLT_PFHT430_v21',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v16',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v16',
        'HLT_PFHT510_v21',
        'HLT_PFHT590_v21',
        'HLT_PFHT680_v21',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v16',
        'HLT_PFHT780_v21',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v16',
        'HLT_PFHT890_v21',
        'HLT_PFJet110_v4',
        'HLT_PFJet140_v23',
        'HLT_PFJet200_TimeGt2p5ns_v2',
        'HLT_PFJet200_TimeLtNeg2p5ns_v2',
        'HLT_PFJet200_v23',
        'HLT_PFJet260_v24',
        'HLT_PFJet320_v24',
        'HLT_PFJet400_v24',
        'HLT_PFJet40_v25',
        'HLT_PFJet450_v25',
        'HLT_PFJet500_v25',
        'HLT_PFJet550_v15',
        'HLT_PFJet60_v25',
        'HLT_PFJet80_v25',
        'HLT_PFJetFwd140_v22',
        'HLT_PFJetFwd200_v22',
        'HLT_PFJetFwd260_v23',
        'HLT_PFJetFwd320_v23',
        'HLT_PFJetFwd400_v23',
        'HLT_PFJetFwd40_v23',
        'HLT_PFJetFwd450_v23',
        'HLT_PFJetFwd500_v23',
        'HLT_PFJetFwd60_v23',
        'HLT_PFJetFwd80_v22',
        'HLT_PFMET105_IsoTrk50_v5',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v13',
        'HLT_PFMET120_PFMHT120_IDTight_v24',
        'HLT_PFMET130_PFMHT130_IDTight_v24',
        'HLT_PFMET140_PFMHT140_IDTight_v24',
        'HLT_PFMET200_BeamHaloCleaned_v13',
        'HLT_PFMET200_NotCleaned_v13',
        'HLT_PFMET250_NotCleaned_v13',
        'HLT_PFMET300_NotCleaned_v13',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v13',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v24',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v23',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v4',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v23',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v15',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v13',
        'HLT_Photon100EBHE10_v6',
        'HLT_Photon110EB_TightID_TightIso_v6',
        'HLT_Photon120_R9Id90_HE10_IsoM_v18',
        'HLT_Photon120_v17',
        'HLT_Photon130EB_TightID_TightIso_v2',
        'HLT_Photon150EB_TightID_TightIso_v2',
        'HLT_Photon150_v11',
        'HLT_Photon165_R9Id90_HE10_IsoM_v19',
        'HLT_Photon175EB_TightID_TightIso_v2',
        'HLT_Photon175_v19',
        'HLT_Photon200EB_TightID_TightIso_v2',
        'HLT_Photon200_v18',
        'HLT_Photon20_HoverELoose_v14',
        'HLT_Photon300_NoHE_v17',
        'HLT_Photon30EB_TightID_TightIso_v5',
        'HLT_Photon30_HoverELoose_v14',
        'HLT_Photon32_OneProng32_M50To105_v2',
        'HLT_Photon33_v9',
        'HLT_Photon35_TwoProngs35_v5',
        'HLT_Photon50EB_TightID_TightIso_v2',
        'HLT_Photon50_R9Id90_HE10_IsoM_v18',
        'HLT_Photon50_TimeGt2p5ns_v1',
        'HLT_Photon50_TimeLtNeg2p5ns_v1',
        'HLT_Photon50_v17',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v2',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v2',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v2',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v1',
        'HLT_Photon75EB_TightID_TightIso_v2',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v9',
        'HLT_Photon75_R9Id90_HE10_IsoM_v18',
        'HLT_Photon75_v17',
        'HLT_Photon90EB_TightID_TightIso_v2',
        'HLT_Photon90_R9Id90_HE10_IsoM_v18',
        'HLT_Photon90_v17',
        'HLT_Physics_v9',
        'HLT_QuadPFJet100_88_70_30_v2',
        'HLT_QuadPFJet103_88_75_15_v9',
        'HLT_QuadPFJet105_88_75_30_v1',
        'HLT_QuadPFJet105_88_76_15_v9',
        'HLT_QuadPFJet111_90_80_15_v9',
        'HLT_QuadPFJet111_90_80_30_v1',
        'HLT_Random_v3',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7',
        'HLT_TripleMu_10_5_5_DZ_v14',
        'HLT_TripleMu_12_10_5_v14',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v7',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v12',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v10',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v9',
        'HLT_UncorrectedJetE30_NoBPTX_v9',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v9',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v9',
        'HLT_ZeroBias_Alignment_v3',
        'HLT_ZeroBias_FirstBXAfterTrain_v5',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v7',
        'HLT_ZeroBias_FirstCollisionInTrain_v6',
        'HLT_ZeroBias_IsolatedBunches_v7',
        'HLT_ZeroBias_LastCollisionInTrain_v5',
        'HLT_ZeroBias_v8'
     ) ),
    ParkingDoubleElectronLowMass = cms.vstring(
        'HLT_DoubleEle10_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle10_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle10_eta1p22_mMax6_v4',
        'HLT_DoubleEle4_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle4_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle4_eta1p22_mMax6_v4',
        'HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle4p5_eta1p22_mMax6_v4',
        'HLT_DoubleEle5_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle5_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle5_eta1p22_mMax6_v4',
        'HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle5p5_eta1p22_mMax6_v4',
        'HLT_DoubleEle6_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle6_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle6_eta1p22_mMax6_v4',
        'HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v4',
        'HLT_DoubleEle7_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle7_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle7_eta1p22_mMax6_v4',
        'HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle7p5_eta1p22_mMax6_v4',
        'HLT_DoubleEle8_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle8_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle8_eta1p22_mMax6_v4',
        'HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle8p5_eta1p22_mMax6_v4',
        'HLT_DoubleEle9_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle9_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle9_eta1p22_mMax6_v4',
        'HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8_v3',
        'HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10_v3',
        'HLT_DoubleEle9p5_eta1p22_mMax6_v4',
        'HLT_SingleEle8_SingleEGL1_v3',
        'HLT_SingleEle8_v3'
    ),
    ParkingDoubleMuonLowMass0 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon10_Upsilon_y1p4_v5',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v9',
        'HLT_Dimuon14_PsiPrime_v17',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_3_LowMass_v5',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_JpsiTrk_Bc_v4',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_LowMass_Displaced_v5',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7'
    ),
    ParkingDoubleMuonLowMass1 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon10_Upsilon_y1p4_v5',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v9',
        'HLT_Dimuon14_PsiPrime_v17',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_3_LowMass_v5',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_JpsiTrk_Bc_v4',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_LowMass_Displaced_v5',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7'
    ),
    ParkingDoubleMuonLowMass2 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon10_Upsilon_y1p4_v5',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v9',
        'HLT_Dimuon14_PsiPrime_v17',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_3_LowMass_v5',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_JpsiTrk_Bc_v4',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_LowMass_Displaced_v5',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7'
    ),
    ParkingDoubleMuonLowMass3 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon10_Upsilon_y1p4_v5',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v9',
        'HLT_Dimuon14_PsiPrime_v17',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_3_LowMass_v5',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_JpsiTrk_Bc_v4',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_LowMass_Displaced_v5',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7'
    ),
    ParkingDoubleMuonLowMass4 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon10_Upsilon_y1p4_v5',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v9',
        'HLT_Dimuon14_PsiPrime_v17',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_3_LowMass_v5',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_JpsiTrk_Bc_v4',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_LowMass_Displaced_v5',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7'
    ),
    ParkingDoubleMuonLowMass5 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon10_Upsilon_y1p4_v5',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v9',
        'HLT_Dimuon14_PsiPrime_v17',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_3_LowMass_v5',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_JpsiTrk_Bc_v4',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_LowMass_Displaced_v5',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7'
    ),
    ParkingDoubleMuonLowMass6 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon10_Upsilon_y1p4_v5',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v9',
        'HLT_Dimuon14_PsiPrime_v17',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_3_LowMass_v5',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_JpsiTrk_Bc_v4',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_LowMass_Displaced_v5',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7'
    ),
    ParkingDoubleMuonLowMass7 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon10_Upsilon_y1p4_v5',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v9',
        'HLT_Dimuon14_PsiPrime_v17',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_3_LowMass_v5',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v4',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_JpsiTrk_Bc_v4',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_LowMass_Displaced_v5',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7'
    ),
    ParkingHH = cms.vstring(
        'HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v1',
        'HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p60_v1',
        'HLT_PFHT280_QuadPFJet30_v1',
        'HLT_PFHT280_QuadPFJet35_PNet2BTagMean0p60_v1',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v5',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v13',
        'HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70_v2',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5_v5',
        'HLT_PFHT400_FivePFJet_100_100_60_30_30_v12',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5_v5',
        'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94_v5',
        'HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50_v1',
        'HLT_PFHT400_SixPFJet32_v13',
        'HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59_v5',
        'HLT_PFHT450_SixPFJet36_PNetBTag0p35_v1',
        'HLT_PFHT450_SixPFJet36_v12'
    ),
    ParkingLLP = cms.vstring(
        'HLT_HT350_DelayedJet40_SingleDelay1p5To3p5nsInclusive_v1',
        'HLT_HT350_DelayedJet40_SingleDelay1p6To3p5nsInclusive_v1',
        'HLT_HT350_DelayedJet40_SingleDelay1p75To3p5nsInclusive_v1',
        'HLT_HT360_DisplacedDijet40_Inclusive1PtrkShortSig5_v1',
        'HLT_HT360_DisplacedDijet45_Inclusive1PtrkShortSig5_v1',
        'HLT_HT390_DisplacedDijet40_Inclusive1PtrkShortSig5_v1',
        'HLT_HT390_DisplacedDijet45_Inclusive1PtrkShortSig5_v1',
        'HLT_HT390eta2p0_DisplacedDijet40_Inclusive1PtrkShortSig5_v1',
        'HLT_HT430_DelayedJet40_SingleDelay1To1p5nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay1p1To1p6nsInclusive_v1',
        'HLT_HT430_DelayedJet40_SingleDelay1p25To1p75nsInclusive_v1',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v17',
        'HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5_v5',
        'HLT_HT650_DisplacedDijet60_Inclusive_v17',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5To4nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p6To4nsInclusive_v1',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75To4nsInclusive_v1'
    ),
    ParkingVBF0 = cms.vstring(
        'HLT_DiJet110_35_Mjj650_PFMET110_v13',
        'HLT_DiJet110_35_Mjj650_PFMET120_v13',
        'HLT_DiJet110_35_Mjj650_PFMET130_v13',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v4',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v20',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v20',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v21',
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v2',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v13',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet_v2',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_v2',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet_v2',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_v2',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22_v1',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_v2',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_v1',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v2',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v2',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v1',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v1',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v5'
    ),
    ParkingVBF1 = cms.vstring(
        'HLT_DiJet110_35_Mjj650_PFMET110_v13',
        'HLT_DiJet110_35_Mjj650_PFMET120_v13',
        'HLT_DiJet110_35_Mjj650_PFMET130_v13',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v4',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v20',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v20',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v21',
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v2',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v13',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet_v2',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_v2',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet_v2',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_v2',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22_v1',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_v2',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_v1',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v2',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v2',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v1',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v1',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v5'
    ),
    ParkingVBF2 = cms.vstring(
        'HLT_DiJet110_35_Mjj650_PFMET110_v13',
        'HLT_DiJet110_35_Mjj650_PFMET120_v13',
        'HLT_DiJet110_35_Mjj650_PFMET130_v13',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v4',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v20',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v20',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v21',
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v2',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v13',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet_v2',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_v2',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet_v2',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_v2',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22_v1',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_v2',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_v1',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v2',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v2',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v1',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v1',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v5'
    ),
    ParkingVBF3 = cms.vstring(
        'HLT_DiJet110_35_Mjj650_PFMET110_v13',
        'HLT_DiJet110_35_Mjj650_PFMET120_v13',
        'HLT_DiJet110_35_Mjj650_PFMET130_v13',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v4',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v20',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v20',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v21',
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v2',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v13',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet_v2',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_v2',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet_v2',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_v2',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22_v1',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_v2',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_v1',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v2',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v2',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v1',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v1',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v5'
    ),
    ParkingVBF4 = cms.vstring(
        'HLT_DiJet110_35_Mjj650_PFMET110_v13',
        'HLT_DiJet110_35_Mjj650_PFMET120_v13',
        'HLT_DiJet110_35_Mjj650_PFMET130_v13',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v4',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v20',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v20',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v21',
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v2',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v13',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet_v2',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_v2',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet_v2',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_v2',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22_v1',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_v2',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_v1',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v2',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v2',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v1',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v1',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v5'
    ),
    ParkingVBF5 = cms.vstring(
        'HLT_DiJet110_35_Mjj650_PFMET110_v13',
        'HLT_DiJet110_35_Mjj650_PFMET120_v13',
        'HLT_DiJet110_35_Mjj650_PFMET130_v13',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v4',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v20',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v20',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v21',
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v2',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v13',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet_v2',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_v2',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet_v2',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_v2',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22_v1',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_v2',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_v1',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v2',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v2',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v1',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v1',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v5'
    ),
    ParkingVBF6 = cms.vstring(
        'HLT_DiJet110_35_Mjj650_PFMET110_v13',
        'HLT_DiJet110_35_Mjj650_PFMET120_v13',
        'HLT_DiJet110_35_Mjj650_PFMET130_v13',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v4',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v20',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v20',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v21',
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v2',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v13',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet_v2',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_v2',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet_v2',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_v2',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22_v1',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_v2',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_v1',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v2',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v2',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v1',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v1',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v5'
    ),
    ParkingVBF7 = cms.vstring(
        'HLT_DiJet110_35_Mjj650_PFMET110_v13',
        'HLT_DiJet110_35_Mjj650_PFMET120_v13',
        'HLT_DiJet110_35_Mjj650_PFMET130_v13',
        'HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1_v4',
        'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v20',
        'HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v20',
        'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v21',
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v2',
        'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v5',
        'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v5',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v2',
        'HLT_TripleJet110_35_35_Mjj650_PFMET110_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET120_v13',
        'HLT_TripleJet110_35_35_Mjj650_PFMET130_v13',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet_v2',
        'HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_v2',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet_v1',
        'HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_v1',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet_v2',
        'HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_v2',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12_v1',
        'HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf_v1',
        'HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22_v1',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v2',
        'HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v2',
        'HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_v2',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet_v1',
        'HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet_v1',
        'HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_v1',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v2',
        'HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v2',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet_v1',
        'HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_v1',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v5'
    ),
    RPCMonitor = cms.vstring('AlCa_RPCMuonNormalisation_v16'),
    ReservedDoubleMuonLowMass = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v9',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v11',
        'HLT_Dimuon0_Jpsi_NoVertexing_v12',
        'HLT_Dimuon0_Jpsi_v12',
        'HLT_Dimuon0_LowMass_L1_0er1p5R_v11',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v12',
        'HLT_Dimuon0_LowMass_L1_4R_v11',
        'HLT_Dimuon0_LowMass_L1_4_v12',
        'HLT_Dimuon0_LowMass_L1_TM530_v10',
        'HLT_Dimuon0_LowMass_v12',
        'HLT_Dimuon0_Upsilon_L1_4p5_v13',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v11',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v13',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v10',
        'HLT_Dimuon0_Upsilon_NoVertexing_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v6',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v11',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v10',
        'HLT_Dimuon18_PsiPrime_v18',
        'HLT_Dimuon24_Phi_noCorrL1_v10',
        'HLT_Dimuon24_Upsilon_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_noCorrL1_v10',
        'HLT_Dimuon25_Jpsi_v18',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v10',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v8',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v8',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v10',
        'HLT_DoubleMu3_Trk_Tau3mu_v16',
        'HLT_DoubleMu4_3_Bs_v19',
        'HLT_DoubleMu4_3_Jpsi_v19',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_Displaced_v11',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v11',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v19',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v8',
        'HLT_Mu25_TkMu0_Phi_v12',
        'HLT_Mu30_TkMu0_Psi_v5',
        'HLT_Mu30_TkMu0_Upsilon_v5',
        'HLT_Mu4_L1DoubleMu_v5',
        'HLT_Mu7p5_L2Mu2_Jpsi_v14',
        'HLT_Mu7p5_L2Mu2_Upsilon_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v8',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v8',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v9',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v7'
    ),
    ScoutingPFMonitor = cms.vstring(
        'DST_Run3_DoubleMu3_PFScoutingPixelTracking_v20',
        'DST_Run3_EG16_EG12_PFScoutingPixelTracking_v20',
        'DST_Run3_EG30_PFScoutingPixelTracking_v20',
        'DST_Run3_JetHT_PFScoutingPixelTracking_v20',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v19',
        'HLT_Ele35_WPTight_Gsf_v13',
        'HLT_IsoMu27_v20',
        'HLT_Mu50_v17',
        'HLT_PFHT1050_v22',
        'HLT_Photon200_v18'
    ),
    ScoutingPFRun3 = cms.vstring(
        'DST_HLTMuon_Run3_PFScoutingPixelTracking_v20',
        'DST_Run3_DoubleMu3_PFScoutingPixelTracking_v20',
        'DST_Run3_EG16_EG12_PFScoutingPixelTracking_v20',
        'DST_Run3_EG30_PFScoutingPixelTracking_v20',
        'DST_Run3_JetHT_PFScoutingPixelTracking_v20'
    ),
    Tau = cms.vstring(
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_v5',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_M5to80_v2',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_v4',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_v4',
        'HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1_v4',
        'HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1_v5'
    ),
    TestEnablesEcalHcal = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v6'
    ),
    TestEnablesEcalHcalDQM = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v6'
    ),
    ZeroBias = cms.vstring(
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v3',
        'HLT_ZeroBias_FirstBXAfterTrain_v5',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v7',
        'HLT_ZeroBias_FirstCollisionInTrain_v6',
        'HLT_ZeroBias_IsolatedBunches_v7',
        'HLT_ZeroBias_LastCollisionInTrain_v5',
        'HLT_ZeroBias_v8'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(4000000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.nanoDQMIO_perLSoutput = cms.PSet(
    MEsToSave = cms.untracked.vstring(
        'Hcal/DigiTask/Occupancy/depth/depth1',
        'Hcal/DigiTask/Occupancy/depth/depth2',
        'Hcal/DigiTask/Occupancy/depth/depth3',
        'Hcal/DigiTask/Occupancy/depth/depth4',
        'Hcal/DigiTask/Occupancy/depth/depth5',
        'Hcal/DigiTask/Occupancy/depth/depth6',
        'Hcal/DigiTask/Occupancy/depth/depth7',
        'Hcal/DigiTask/Occupancy/depth/depthHO',
        'Hcal/DigiTask/OccupancyCut/depth/depth1',
        'Hcal/DigiTask/OccupancyCut/depth/depth2',
        'Hcal/DigiTask/OccupancyCut/depth/depth3',
        'Hcal/DigiTask/OccupancyCut/depth/depth4',
        'Hcal/DigiTask/OccupancyCut/depth/depth5',
        'Hcal/DigiTask/OccupancyCut/depth/depth6',
        'Hcal/DigiTask/OccupancyCut/depth/depth7',
        'Hcal/DigiTask/OccupancyCut/depth/depthHO',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'EcalBarrel/EBOccupancyTask/EBOT DCC entries',
        'EcalEndcap/EEOccupancyTask/EEOT DCC entries',
        'Ecal/EventInfo/processedEvents',
        'PixelPhase1/Tracks/charge_PXBarrel',
        'PixelPhase1/Tracks/charge_PXForward',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
        'HLT/Vertexing/hltPixelVertices/hltPixelVertices/goodvtxNbr',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_pt',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/LUMIanalysis/NumberEventsVsLUMI',
        'HLT/Tracking/tracks/PUmonitoring/NumberEventsVsGoodPVtx',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
        'PixelPhase1/Tracks/clusterposition_zphi_ontrack',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
        'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
        'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
        'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/NormalizedHitResiduals_TOB__Layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/NormalizedHitResiduals_TOB__Layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/NormalizedHitResiduals_TOB__Layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/NormalizedHitResiduals_TOB__Layer__6',
        'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
        'SiStrip/MechanicalView/MainDiagonal Position',
        'SiStrip/MechanicalView/NumberOfClustersInPixel',
        'SiStrip/MechanicalView/NumberOfClustersInStrip',
        'Tracking/TrackParameters/generalTracks/LSanalysis/Chi2oNDF_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfTracks_lumiFlag_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDzToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIP3DToPV_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfMissingOuterRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
        'OfflinePV/offlinePrimaryVertices/tagVtxProb',
        'OfflinePV/offlinePrimaryVertices/tagType',
        'OfflinePV/Resolution/PV/pull_x',
        'OfflinePV/Resolution/PV/pull_y',
        'OfflinePV/Resolution/PV/pull_z',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Constituents',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta_uncor',
        'JetMET/Jet/Cleanedak4PFJetsCHS/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsCHS/NJets',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Pt',
        'JetMET/MET/pfMETT1/Cleaned/METSig',
        'JetMET/vertices'
    )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(4),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.streams = cms.PSet(
    ALCALowPtJet = cms.vstring('AlCaLowPtJet'),
    ALCALumiPixelsCountsExpress = cms.vstring('AlCaLumiPixelsCountsExpress'),
    ALCALumiPixelsCountsPrompt = cms.vstring('AlCaLumiPixelsCountsPrompt'),
    ALCAP0 = cms.vstring('AlCaP0'),
    ALCAPHISYM = cms.vstring('AlCaPhiSym'),
    ALCAPPSExpress = cms.vstring('AlCaPPSExpress'),
    ALCAPPSPrompt = cms.vstring('AlCaPPSPrompt'),
    Calibration = cms.vstring('TestEnablesEcalHcal'),
    DQM = cms.vstring('OnlineMonitor'),
    DQMCalibration = cms.vstring('TestEnablesEcalHcalDQM'),
    DQMEventDisplay = cms.vstring('EventDisplay'),
    DQMGPUvsCPU = cms.vstring('DQMGPUvsCPU'),
    DQMOnlineBeamspot = cms.vstring('DQMOnlineBeamspot'),
    DQMPPSRandom = cms.vstring('DQMPPSRandom'),
    EcalCalibration = cms.vstring('EcalLaser'),
    Express = cms.vstring('ExpressPhysics'),
    ExpressAlignment = cms.vstring('ExpressAlignment'),
    ExpressCosmics = cms.vstring(),
    HLTMonitor = cms.vstring('HLTMonitor'),
    NanoDST = cms.vstring('L1Accept'),
    ParkingDoubleElectronLowMass = cms.vstring('ParkingDoubleElectronLowMass'),
    ParkingDoubleMuonLowMass0 = cms.vstring(
        'ParkingDoubleMuonLowMass0',
        'ParkingDoubleMuonLowMass1'
    ),
    ParkingDoubleMuonLowMass1 = cms.vstring(
        'ParkingDoubleMuonLowMass2',
        'ParkingDoubleMuonLowMass3'
    ),
    ParkingDoubleMuonLowMass2 = cms.vstring(
        'ParkingDoubleMuonLowMass4',
        'ParkingDoubleMuonLowMass5'
    ),
    ParkingDoubleMuonLowMass3 = cms.vstring(
        'ParkingDoubleMuonLowMass6',
        'ParkingDoubleMuonLowMass7'
    ),
    ParkingHH = cms.vstring('ParkingHH'),
    ParkingLLP = cms.vstring('ParkingLLP'),
    ParkingVBF0 = cms.vstring(
        'ParkingVBF0',
        'ParkingVBF1'
    ),
    ParkingVBF1 = cms.vstring(
        'ParkingVBF2',
        'ParkingVBF3'
    ),
    ParkingVBF2 = cms.vstring(
        'ParkingVBF4',
        'ParkingVBF5'
    ),
    ParkingVBF3 = cms.vstring(
        'ParkingVBF6',
        'ParkingVBF7'
    ),
    PhysicsCommissioning = cms.vstring(
        'Commissioning',
        'Cosmics',
        'HLTPhysics',
        'HcalNZS',
        'MonteCarlo',
        'NoBPTX',
        'ZeroBias'
    ),
    PhysicsDispJetBTagMuEGTau = cms.vstring(
        'BTagMu',
        'DisplacedJet',
        'MuonEG',
        'Tau'
    ),
    PhysicsEGamma0 = cms.vstring('EGamma0'),
    PhysicsEGamma1 = cms.vstring('EGamma1'),
    PhysicsHLTPhysics0 = cms.vstring(
        'EphemeralHLTPhysics0',
        'EphemeralHLTPhysics1'
    ),
    PhysicsHLTPhysics1 = cms.vstring(
        'EphemeralHLTPhysics2',
        'EphemeralHLTPhysics3'
    ),
    PhysicsHLTPhysics2 = cms.vstring(
        'EphemeralHLTPhysics4',
        'EphemeralHLTPhysics5'
    ),
    PhysicsHLTPhysics3 = cms.vstring(
        'EphemeralHLTPhysics6',
        'EphemeralHLTPhysics7'
    ),
    PhysicsJetMET0 = cms.vstring('JetMET0'),
    PhysicsJetMET1 = cms.vstring('JetMET1'),
    PhysicsMuon0 = cms.vstring('Muon0'),
    PhysicsMuon1 = cms.vstring('Muon1'),
    PhysicsReservedDoubleMuonLowMass = cms.vstring('ReservedDoubleMuonLowMass'),
    PhysicsScoutingPFMonitor = cms.vstring('ScoutingPFMonitor'),
    PhysicsZeroBias0 = cms.vstring(
        'EphemeralZeroBias0',
        'EphemeralZeroBias1'
    ),
    PhysicsZeroBias1 = cms.vstring(
        'EphemeralZeroBias2',
        'EphemeralZeroBias3'
    ),
    PhysicsZeroBias2 = cms.vstring(
        'EphemeralZeroBias4',
        'EphemeralZeroBias5'
    ),
    PhysicsZeroBias3 = cms.vstring(
        'EphemeralZeroBias6',
        'EphemeralZeroBias7'
    ),
    RPCMON = cms.vstring('RPCMonitor'),
    ScoutingPF = cms.vstring('ScoutingPFRun3')
)

process.hltEcalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("hltEcalDigis"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigis","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = cms.InputTag("hltEcalDigis"),
    integrityBlockSizeErrors = cms.InputTag("hltEcalDigis","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = cms.InputTag("hltEcalDigis","EcalIntegrityTTIdErrors")
)


process.hltEcalDigisFromGPU = cms.EDProducer("EcalCPUDigisProducer",
    digisInLabelEB = cms.InputTag("hltEcalDigisGPU","ebDigis"),
    digisInLabelEE = cms.InputTag("hltEcalDigisGPU","eeDigis"),
    digisOutLabelEB = cms.string('ebDigis'),
    digisOutLabelEE = cms.string('eeDigis'),
    produceDummyIntegrityCollections = cms.bool(False)
)


process.hltEcalDigisGPU = cms.EDProducer("EcalRawToDigiGPU",
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    InputLabel = cms.InputTag("rawDataCollector"),
    digisLabelEB = cms.string('ebDigis'),
    digisLabelEE = cms.string('eeDigis'),
    maxChannelsEB = cms.uint32(61200),
    maxChannelsEE = cms.uint32(14648)
)


process.hltEcalDigisLegacy = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28, 29, 30,
        31, 32, 33, 34, 35,
        36, 37, 38, 39, 40,
        41, 42, 43, 44, 45,
        46, 47, 48, 49, 50,
        51, 52, 53, 54
    ),
    orderedFedList = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.hltEcalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    ESdigiCollection = cms.string(''),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    debugMode = cms.untracked.bool(False),
    sourceTag = cms.InputTag("rawDataCollector")
)


process.hltEcalPreshowerRecHit = cms.EDProducer("ESRecHitProducer",
    ESRecoAlgo = cms.int32(0),
    ESdigiCollection = cms.InputTag("hltEcalPreshowerDigis"),
    ESrechitCollection = cms.string('EcalRecHitsES'),
    algo = cms.string('ESRecHitWorker')
)


process.hltEcalRecHit = cms.EDProducer("EcalRecHitProducer",
    ChannelStatusToBeExcluded = cms.vstring(),
    EBLaserMAX = cms.double(3.0),
    EBLaserMIN = cms.double(0.5),
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    EBuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEB"),
    EELaserMAX = cms.double(8.0),
    EELaserMIN = cms.double(0.5),
    EErechitCollection = cms.string('EcalRecHitsEE'),
    EEuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEE"),
    algo = cms.string('EcalRecHitWorkerSimple'),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    bdtWeightFileCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_onlyCracks_ZskimData2017_v1.xml'),
    bdtWeightFileNoCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_noCracks_ZskimData2017_v1.xml'),
    cleaningConfig = cms.PSet(
        cThreshold_barrel = cms.double(4.0),
        cThreshold_double = cms.double(10.0),
        cThreshold_endcap = cms.double(15.0),
        e4e1Threshold_barrel = cms.double(0.08),
        e4e1Threshold_endcap = cms.double(0.3),
        e4e1_a_barrel = cms.double(0.04),
        e4e1_a_endcap = cms.double(0.02),
        e4e1_b_barrel = cms.double(-0.024),
        e4e1_b_endcap = cms.double(-0.0125),
        e6e2thresh = cms.double(0.04),
        ignoreOutOfTimeThresh = cms.double(1000000000.0),
        tightenCrack_e1_double = cms.double(2.0),
        tightenCrack_e1_single = cms.double(2.0),
        tightenCrack_e4e1_single = cms.double(3.0),
        tightenCrack_e6e2_double = cms.double(3.0)
    ),
    dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
    dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
    ebDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebDetId"),
    ebFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebFE"),
    eeDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeDetId"),
    eeFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeFE"),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring(
            'kOk',
            'kDAC',
            'kNoLaser',
            'kNoisy'
        ),
        kNeighboursRecovered = cms.vstring(
            'kFixedG0',
            'kNonRespondingIsolated',
            'kDeadVFE'
        ),
        kNoisy = cms.vstring(
            'kNNoisy',
            'kFixedG6',
            'kFixedG1'
        ),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    killDeadChannels = cms.bool(True),
    laserCorrection = cms.bool(True),
    logWarningEtThreshold_EB_FE = cms.double(50.0),
    logWarningEtThreshold_EE_FE = cms.double(50.0),
    recoverEBFE = cms.bool(False),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    recoverEEFE = cms.bool(False),
    recoverEEIsolatedChannels = cms.bool(False),
    recoverEEVFE = cms.bool(False),
    singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
    singleChannelRecoveryThreshold = cms.double(8.0),
    skipTimeCalib = cms.bool(False),
    sum8ChannelRecoveryThreshold = cms.double(0.0),
    triggerPrimitiveDigiCollection = cms.InputTag("hltEcalDigis","EcalTriggerPrimitives")
)


process.hltEcalUncalibRecHitFromSoA = cms.EDProducer("EcalUncalibRecHitConvertGPU2CPUFormat",
    isPhase2 = cms.bool(False),
    recHitsLabelCPUEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsLabelCPUEE = cms.string('EcalUncalibRecHitsEE'),
    recHitsLabelGPUEB = cms.InputTag("hltEcalUncalibRecHitSoA","EcalUncalibRecHitsEB"),
    recHitsLabelGPUEE = cms.InputTag("hltEcalUncalibRecHitSoA","EcalUncalibRecHitsEE")
)


process.hltEcalUncalibRecHitGPU = cms.EDProducer("EcalUncalibRecHitProducerGPU",
    EBtimeConstantTerm = cms.double(0.6),
    EBtimeFitLimits_Lower = cms.double(0.2),
    EBtimeFitLimits_Upper = cms.double(1.4),
    EBtimeNconst = cms.double(28.5),
    EEtimeConstantTerm = cms.double(1.0),
    EEtimeFitLimits_Lower = cms.double(0.2),
    EEtimeFitLimits_Upper = cms.double(1.4),
    EEtimeNconst = cms.double(31.8),
    amplitudeThresholdEB = cms.double(10.0),
    amplitudeThresholdEE = cms.double(10.0),
    digisLabelEB = cms.InputTag("hltEcalDigisGPU","ebDigis"),
    digisLabelEE = cms.InputTag("hltEcalDigisGPU","eeDigis"),
    kernelMinimizeThreads = cms.untracked.vuint32(32, 1, 1),
    outOfTimeThresholdGain12mEB = cms.double(1000.0),
    outOfTimeThresholdGain12mEE = cms.double(1000.0),
    outOfTimeThresholdGain12pEB = cms.double(1000.0),
    outOfTimeThresholdGain12pEE = cms.double(1000.0),
    outOfTimeThresholdGain61mEB = cms.double(1000.0),
    outOfTimeThresholdGain61mEE = cms.double(1000.0),
    outOfTimeThresholdGain61pEB = cms.double(1000.0),
    outOfTimeThresholdGain61pEE = cms.double(1000.0),
    recHitsLabelEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsLabelEE = cms.string('EcalUncalibRecHitsEE'),
    shouldRunTimingComputation = cms.bool(True)
)


process.hltEcalUncalibRecHitLegacy = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("hltEcalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = cms.InputTag("hltEcalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
    algoPSet = cms.PSet(
        EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
        EBtimeConstantTerm = cms.double(0.6),
        EBtimeFitLimits_Lower = cms.double(0.2),
        EBtimeFitLimits_Upper = cms.double(1.4),
        EBtimeFitParameters = cms.vdouble(
            -2.015452, 3.130702, -12.3473, 41.88921, -82.83944,
            91.01147, -50.35761, 11.05621
        ),
        EBtimeNconst = cms.double(28.5),
        EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
        EEtimeConstantTerm = cms.double(1.0),
        EEtimeFitLimits_Lower = cms.double(0.2),
        EEtimeFitLimits_Upper = cms.double(1.4),
        EEtimeFitParameters = cms.vdouble(
            -2.390548, 3.553628, -17.62341, 67.67538, -133.213,
            140.7432, -75.41106, 16.20277
        ),
        EEtimeNconst = cms.double(31.8),
        activeBXs = cms.vint32(
            -5, -4, -3, -2, -1,
            0, 1, 2, 3, 4
        ),
        addPedestalUncertaintyEB = cms.double(0.0),
        addPedestalUncertaintyEE = cms.double(0.0),
        ampErrorCalculation = cms.bool(False),
        amplitudeThresholdEB = cms.double(10.0),
        amplitudeThresholdEE = cms.double(10.0),
        doPrefitEB = cms.bool(False),
        doPrefitEE = cms.bool(False),
        dynamicPedestalsEB = cms.bool(False),
        dynamicPedestalsEE = cms.bool(False),
        gainSwitchUseMaxSampleEB = cms.bool(True),
        gainSwitchUseMaxSampleEE = cms.bool(False),
        mitigateBadSamplesEB = cms.bool(False),
        mitigateBadSamplesEE = cms.bool(False),
        outOfTimeThresholdGain12mEB = cms.double(1000.0),
        outOfTimeThresholdGain12mEE = cms.double(1000.0),
        outOfTimeThresholdGain12pEB = cms.double(1000.0),
        outOfTimeThresholdGain12pEE = cms.double(1000.0),
        outOfTimeThresholdGain61mEB = cms.double(1000.0),
        outOfTimeThresholdGain61mEE = cms.double(1000.0),
        outOfTimeThresholdGain61pEB = cms.double(1000.0),
        outOfTimeThresholdGain61pEE = cms.double(1000.0),
        prefitMaxChiSqEB = cms.double(25.0),
        prefitMaxChiSqEE = cms.double(10.0),
        selectiveBadSampleCriteriaEB = cms.bool(False),
        selectiveBadSampleCriteriaEE = cms.bool(False),
        simplifiedNoiseModelForGainSwitch = cms.bool(True),
        timealgo = cms.string('RatioMethod'),
        useLumiInfoRunHeader = cms.bool(False)
    )
)


process.hltEcalUncalibRecHitSoA = cms.EDProducer("EcalCPUUncalibRecHitProducer",
    containsTimingInformation = cms.bool(True),
    isPhase2 = cms.bool(False),
    recHitsInLabelEB = cms.InputTag("hltEcalUncalibRecHitGPU","EcalUncalibRecHitsEB"),
    recHitsInLabelEE = cms.InputTag("hltEcalUncalibRecHitGPU","EcalUncalibRecHitsEE"),
    recHitsOutLabelEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsOutLabelEE = cms.string('EcalUncalibRecHitsEE')
)


process.hltEgammaCandidates = cms.EDProducer("EgammaHLTRecoEcalCandidateProducers",
    recoEcalCandidateCollection = cms.string(''),
    scHybridBarrelProducer = cms.InputTag("hltParticleFlowSuperClusterECALL1Seeded","hltParticleFlowSuperClusterECALBarrel"),
    scIslandEndcapProducer = cms.InputTag("hltParticleFlowSuperClusterECALL1Seeded","hltParticleFlowSuperClusterECALEndcapWithPreshower")
)


process.hltEgammaCandidatesUnseeded = cms.EDProducer("EgammaHLTRecoEcalCandidateProducers",
    recoEcalCandidateCollection = cms.string(''),
    scHybridBarrelProducer = cms.InputTag("hltParticleFlowSuperClusterECALUnseeded","hltParticleFlowSuperClusterECALBarrel"),
    scIslandEndcapProducer = cms.InputTag("hltParticleFlowSuperClusterECALUnseeded","hltParticleFlowSuperClusterECALEndcapWithPreshower")
)


process.hltEgammaCkfTrackCandidatesForGSF = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryBuilderForGsfElectrons')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(1000000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltEgammaElectronPixelSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.hltEgammaClusterShape = cms.EDProducer("EgammaHLTClusterShapeProducer",
    ecalRechitEB = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEB"),
    ecalRechitEE = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEE"),
    isIeta = cms.bool(True),
    multThresEB = cms.double(1.0),
    multThresEE = cms.double(1.25),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates")
)


process.hltEgammaClusterShapeUnseeded = cms.EDProducer("EgammaHLTClusterShapeProducer",
    ecalRechitEB = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
    ecalRechitEE = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
    isIeta = cms.bool(True),
    multThresEB = cms.double(1.0),
    multThresEE = cms.double(1.25),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesUnseeded")
)


process.hltEgammaEcalPFClusterIso = cms.EDProducer("EgammaHLTEcalPFClusterIsolationProducer",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    doRhoCorrection = cms.bool(False),
    drMax = cms.double(0.3),
    drVetoBarrel = cms.double(0.0),
    drVetoEndcap = cms.double(0.0),
    effectiveAreas = cms.vdouble(0.29, 0.21),
    energyBarrel = cms.double(0.0),
    energyEndcap = cms.double(0.0),
    etaStripBarrel = cms.double(0.0),
    etaStripEndcap = cms.double(0.0),
    pfClusterProducer = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0)
)


process.hltEgammaEleGsfTrackIso = cms.EDProducer("EgammaHLTElectronTrackIsolationProducers",
    beamSpotProducer = cms.InputTag("hltOnlineBeamSpot"),
    egTrkIsoConeSize = cms.double(0.2),
    egTrkIsoPtMin = cms.double(1.0),
    egTrkIsoRSpan = cms.double(999999.0),
    egTrkIsoStripBarrel = cms.double(0.01),
    egTrkIsoStripEndcap = cms.double(0.01),
    egTrkIsoVetoConeSizeBarrel = cms.double(0.03),
    egTrkIsoVetoConeSizeEndcap = cms.double(0.03),
    egTrkIsoZSpan = cms.double(0.15),
    electronProducer = cms.InputTag("hltEgammaGsfElectrons"),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    trackProducer = cms.InputTag("hltMergedTracks"),
    useGsfTrack = cms.bool(True),
    useSCRefs = cms.bool(True)
)


process.hltEgammaElectronPixelSeeds = cms.EDProducer("ElectronNHitSeedProducer",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    initialSeeds = cms.InputTag("hltElePixelSeedsCombined"),
    matcherConfig = cms.PSet(
        detLayerGeom = cms.ESInputTag("","hltESPGlobalDetLayerGeometry"),
        matchingCuts = cms.VPSet(
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.05),
                dPhiMaxHighEtThres = cms.vdouble(20.0),
                dPhiMaxLowEtGrad = cms.vdouble(-0.002),
                dRZMaxHighEt = cms.vdouble(9999.0),
                dRZMaxHighEtThres = cms.vdouble(0.0),
                dRZMaxLowEtGrad = cms.vdouble(0.0),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            )
        ),
        minNrHits = cms.vuint32(2, 3),
        minNrHitsValidLayerBins = cms.vint32(4),
        navSchool = cms.ESInputTag("","SimpleNavigationSchool"),
        paramMagField = cms.ESInputTag("","ParabolicMf"),
        useRecoVertex = cms.bool(False)
    ),
    measTkEvt = cms.InputTag("hltSiStripClusters"),
    superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatch"),
    vertices = cms.InputTag("")
)


process.hltEgammaElectronPixelSeedsUnseeded = cms.EDProducer("ElectronNHitSeedProducer",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    initialSeeds = cms.InputTag("hltElePixelSeedsCombinedUnseeded"),
    matcherConfig = cms.PSet(
        detLayerGeom = cms.ESInputTag("","hltESPGlobalDetLayerGeometry"),
        matchingCuts = cms.VPSet(
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.05),
                dPhiMaxHighEtThres = cms.vdouble(20.0),
                dPhiMaxLowEtGrad = cms.vdouble(-0.002),
                dRZMaxHighEt = cms.vdouble(9999.0),
                dRZMaxHighEtThres = cms.vdouble(0.0),
                dRZMaxLowEtGrad = cms.vdouble(0.0),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            )
        ),
        minNrHits = cms.vuint32(2, 3),
        minNrHitsValidLayerBins = cms.vint32(4),
        navSchool = cms.ESInputTag("","SimpleNavigationSchool"),
        paramMagField = cms.ESInputTag("","ParabolicMf"),
        useRecoVertex = cms.bool(False)
    ),
    measTkEvt = cms.InputTag("hltSiStripClusters"),
    superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatchUnseeded"),
    vertices = cms.InputTag("")
)


process.hltEgammaGsfElectrons = cms.EDProducer("EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag("hltOnlineBeamSpot"),
    GsfTrackProducer = cms.InputTag("hltEgammaGsfTracks"),
    TrackProducer = cms.InputTag(""),
    UseGsfTracks = cms.bool(True)
)


process.hltEgammaGsfTrackVars = cms.EDProducer("EgammaHLTGsfTrackVarProducer",
    beamSpotProducer = cms.InputTag("hltOnlineBeamSpot"),
    inputCollection = cms.InputTag("hltEgammaGsfTracks"),
    lowerTrackNrToRemoveCut = cms.int32(-1),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    upperTrackNrToRemoveCut = cms.int32(9999),
    useDefaultValuesForBarrel = cms.bool(False),
    useDefaultValuesForEndcap = cms.bool(False)
)


process.hltEgammaGsfTracks = cms.EDProducer("GsfTrackProducer",
    AlgorithmName = cms.string('gsf'),
    Fitter = cms.string('hltESPGsfElectronFittingSmoother'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string('hltESPMeasurementTracker'),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('hltESPFwdElectronPropagator'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    producer = cms.string(''),
    src = cms.InputTag("hltEgammaCkfTrackCandidatesForGSF"),
    useHitsSplitting = cms.bool(False)
)


process.hltEgammaHLTExtra = cms.EDProducer("EgammaHLTExtraProducer",
    ecal = cms.VPSet(
        cms.PSet(
            label = cms.string('EcalRecHitsEB'),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEB")
        ),
        cms.PSet(
            label = cms.string('EcalRecHitsEE'),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEE")
        )
    ),
    egCands = cms.VPSet(
        cms.PSet(
            ecalCands = cms.InputTag("hltEgammaCandidates"),
            gsfTracks = cms.InputTag("hltEgammaGsfTracks"),
            label = cms.string(''),
            pixelSeeds = cms.InputTag("hltEgammaElectronPixelSeeds")
        ),
        cms.PSet(
            ecalCands = cms.InputTag("hltEgammaCandidatesUnseeded"),
            gsfTracks = cms.InputTag("hltEgammaGsfTracksUnseeded"),
            label = cms.string('Unseeded'),
            pixelSeeds = cms.InputTag("hltEgammaElectronPixelSeedsUnseeded")
        )
    ),
    hcal = cms.VPSet(cms.PSet(
        label = cms.string(''),
        src = cms.InputTag("hltHbhereco")
    )),
    minPtToSaveHits = cms.double(8.0),
    pfClusIso = cms.VPSet(
        cms.PSet(
            label = cms.string('Ecal'),
            src = cms.InputTag("hltParticleFlowClusterECALL1Seeded")
        ),
        cms.PSet(
            label = cms.string('EcalUnseeded'),
            src = cms.InputTag("hltParticleFlowClusterECALUnseeded")
        ),
        cms.PSet(
            label = cms.string('Hcal'),
            src = cms.InputTag("hltParticleFlowClusterHCAL")
        )
    ),
    saveHitsPlusHalfPi = cms.bool(True),
    saveHitsPlusPi = cms.bool(False),
    trks = cms.VPSet(cms.PSet(
        label = cms.string(''),
        src = cms.InputTag("hltMergedTracks")
    ))
)


process.hltEgammaHcalPFClusterIso = cms.EDProducer("EgammaHLTHcalPFClusterIsolationProducer",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    doRhoCorrection = cms.bool(False),
    drMax = cms.double(0.3),
    drVetoBarrel = cms.double(0.0),
    drVetoEndcap = cms.double(0.0),
    effectiveAreas = cms.vdouble(0.2, 0.25),
    energyBarrel = cms.double(0.0),
    energyEndcap = cms.double(0.0),
    etaStripBarrel = cms.double(0.0),
    etaStripEndcap = cms.double(0.0),
    pfClusterProducerHCAL = cms.InputTag("hltParticleFlowClusterHCAL"),
    pfClusterProducerHFEM = cms.InputTag(""),
    pfClusterProducerHFHAD = cms.InputTag(""),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0),
    useEt = cms.bool(True),
    useHF = cms.bool(False)
)


process.hltEgammaHoverE = cms.EDProducer("EgammaHLTHcalVarProducerFromRecHit",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    depth = cms.int32(0),
    doEtSum = cms.bool(False),
    doRhoCorrection = cms.bool(False),
    eThresHB = cms.vdouble(0.4, 0.3, 0.3, 0.3),
    eThresHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    effectiveAreas = cms.vdouble(0.105, 0.17),
    etThresHB = cms.vdouble(0.0, 0.0, 0.0, 0.0),
    etThresHE = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0
    ),
    hbheRecHitsTag = cms.InputTag("hltHbhereco"),
    innerCone = cms.double(0.0),
    maxSeverityHB = cms.int32(9),
    maxSeverityHE = cms.int32(9),
    outerCone = cms.double(0.14),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0),
    useSingleTower = cms.bool(False)
)


process.hltEgammaHoverEUnseeded = cms.EDProducer("EgammaHLTHcalVarProducerFromRecHit",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    depth = cms.int32(0),
    doEtSum = cms.bool(False),
    doRhoCorrection = cms.bool(False),
    eThresHB = cms.vdouble(0.4, 0.3, 0.3, 0.3),
    eThresHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    effectiveAreas = cms.vdouble(0.105, 0.17),
    etThresHB = cms.vdouble(0.0, 0.0, 0.0, 0.0),
    etThresHE = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0
    ),
    hbheRecHitsTag = cms.InputTag("hltHbhereco"),
    innerCone = cms.double(0.0),
    maxSeverityHB = cms.int32(9),
    maxSeverityHE = cms.int32(9),
    outerCone = cms.double(0.14),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesUnseeded"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0),
    useSingleTower = cms.bool(False)
)


process.hltEgammaPixelMatchVars = cms.EDProducer("EgammaHLTPixelMatchVarProducer",
    dPhi1SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00112, 0.000752, -0.00122, 0.00109),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00222, 0.000196, -0.000203, 0.000447),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00236, 0.000691, 0.000199, 0.000416),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00823, -0.0029),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00282),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.010838, -0.00345),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0043),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0208, -0.0125, 0.00231),
                funcType = cms.string('TF1:=pol2'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            )
        )
    ),
    dPhi2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00013),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(1.6),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00045, -0.000199),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(1.9),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(7.94e-05),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.9),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    dRZ2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00299, 0.000299, -4.13e-06, 0.00191),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.248, -0.329, 0.148, -0.0222),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    pixelSeedsProducer = cms.InputTag("hltEgammaElectronPixelSeeds"),
    productsToWrite = cms.int32(0),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates")
)


process.hltEgammaPixelMatchVarsUnseeded = cms.EDProducer("EgammaHLTPixelMatchVarProducer",
    dPhi1SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00112, 0.000752, -0.00122, 0.00109),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00222, 0.000196, -0.000203, 0.000447),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00236, 0.000691, 0.000199, 0.000416),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00823, -0.0029),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00282),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.010838, -0.00345),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0043),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0208, -0.0125, 0.00231),
                funcType = cms.string('TF1:=pol2'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            )
        )
    ),
    dPhi2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00013),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(1.6),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00045, -0.000199),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(1.9),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(7.94e-05),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.9),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    dRZ2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00299, 0.000299, -4.13e-06, 0.00191),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.248, -0.329, 0.148, -0.0222),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    pixelSeedsProducer = cms.InputTag("hltEgammaElectronPixelSeedsUnseeded"),
    productsToWrite = cms.int32(0),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesUnseeded")
)


process.hltEgammaSuperClustersToPixelMatch = cms.EDProducer("EgammaHLTFilteredSuperClusterProducer",
    cands = cms.InputTag("hltEgammaCandidates"),
    cuts = cms.VPSet(cms.PSet(
        barrelCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        endcapCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        var = cms.InputTag("hltEgammaHoverE")
    )),
    minEtCutEB = cms.double(0.0),
    minEtCutEE = cms.double(0.0)
)


process.hltEgammaSuperClustersToPixelMatchUnseeded = cms.EDProducer("EgammaHLTFilteredSuperClusterProducer",
    cands = cms.InputTag("hltEgammaCandidatesUnseeded"),
    cuts = cms.VPSet(cms.PSet(
        barrelCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        endcapCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        var = cms.InputTag("hltEgammaHoverEUnseeded")
    )),
    minEtCutEB = cms.double(0.0),
    minEtCutEE = cms.double(0.0)
)


process.hltElePixelHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("hltPixelLayerPairs"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitDoubletsForTriplets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("hltPixelLayerTriplets"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitDoubletsForTripletsUnseeded = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("hltPixelLayerTriplets"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegionsUnseeded"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitDoubletsUnseeded = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("hltPixelLayerPairs"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegionsUnseeded"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.3),
    CAPhiCut = cms.double(0.1),
    CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    CAThetaCut = cms.double(0.004),
    CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("hltElePixelHitDoubletsForTriplets"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8.0),
        value1 = cms.double(100.0),
        value2 = cms.double(6.0)
    ),
    useBendingCorrection = cms.bool(True)
)


process.hltElePixelHitTripletsUnseeded = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.3),
    CAPhiCut = cms.double(0.1),
    CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    CAThetaCut = cms.double(0.004),
    CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("hltElePixelHitDoubletsForTripletsUnseeded"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8.0),
        value1 = cms.double(100.0),
        value2 = cms.double(6.0)
    ),
    useBendingCorrection = cms.bool(True)
)


process.hltElePixelSeedsCombined = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag("hltElePixelSeedsDoublets", "hltElePixelSeedsTriplets")
)


process.hltElePixelSeedsCombinedUnseeded = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag("hltElePixelSeedsDoubletsUnseeded", "hltElePixelSeedsTripletsUnseeded")
)


process.hltElePixelSeedsDoublets = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitDoublets")
)


process.hltElePixelSeedsDoubletsUnseeded = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitDoubletsUnseeded")
)


process.hltElePixelSeedsTriplets = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitTriplets")
)


process.hltElePixelSeedsTripletsUnseeded = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitTripletsUnseeded")
)


process.hltEleSeedsTrackingRegions = cms.EDProducer("TrackingRegionsFromSuperClustersEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        defaultZ = cms.double(0.0),
        deltaEtaRegion = cms.double(0.1),
        deltaPhiRegion = cms.double(0.4),
        measurementTrackerEvent = cms.InputTag(""),
        minBSDeltaZ = cms.double(0.0),
        nrSigmaForBSDeltaZ = cms.double(4.0),
        originHalfLength = cms.double(12.5),
        originRadius = cms.double(0.2),
        precise = cms.bool(True),
        ptMin = cms.double(1.5),
        superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatch"),
        useZInBeamspot = cms.bool(False),
        useZInVertex = cms.bool(False),
        vertices = cms.InputTag(""),
        whereToUseMeasTracker = cms.string('kNever')
    )
)


process.hltEleSeedsTrackingRegionsUnseeded = cms.EDProducer("TrackingRegionsFromSuperClustersEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        defaultZ = cms.double(0.0),
        deltaEtaRegion = cms.double(0.1),
        deltaPhiRegion = cms.double(0.4),
        measurementTrackerEvent = cms.InputTag(""),
        minBSDeltaZ = cms.double(0.0),
        nrSigmaForBSDeltaZ = cms.double(4.0),
        originHalfLength = cms.double(12.5),
        originRadius = cms.double(0.2),
        precise = cms.bool(True),
        ptMin = cms.double(1.5),
        superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatchUnseeded"),
        useZInBeamspot = cms.bool(False),
        useZInVertex = cms.bool(False),
        vertices = cms.InputTag(""),
        whereToUseMeasTracker = cms.string('kNever')
    )
)


process.hltFEDSelectorTCDS = cms.EDProducer("EvFFEDSelector",
    fedList = cms.vuint32(1024, 1025),
    inputTag = cms.InputTag("rawDataCollector")
)


process.hltFixedGridRhoFastjetAllCaloForMuons = cms.EDProducer("FixedGridRhoProducerFastjetFromRecHit",
    eThresHB = cms.vdouble(0.4, 0.3, 0.3, 0.3),
    eThresHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    ebRecHitsTag = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
    eeRecHitsTag = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
    gridSpacing = cms.double(0.55),
    hbheRecHitsTag = cms.InputTag("hltHbhereco"),
    maxRapidity = cms.double(2.5),
    skipECAL = cms.bool(False),
    skipHCAL = cms.bool(False)
)


process.hltGtStage2Digis = cms.EDProducer("L1TRawToDigi",
    CTP7 = cms.untracked.bool(False),
    DmxFWId = cms.uint32(0),
    FWId = cms.uint32(0),
    FWOverride = cms.bool(False),
    FedIds = cms.vint32(1404),
    InputLabel = cms.InputTag("rawDataCollector"),
    MTF7 = cms.untracked.bool(False),
    MinFeds = cms.uint32(0),
    Setup = cms.string('stage2::GTSetup'),
    TMTCheck = cms.bool(True),
    debug = cms.untracked.bool(False),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.hltGtStage2ObjectMap = cms.EDProducer("L1TGlobalProducer",
    AlgoBlkInputTag = cms.InputTag("hltGtStage2Digis"),
    AlgorithmTriggersUnmasked = cms.bool(True),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    AlternativeNrBxBoardDaq = cms.uint32(0),
    BstLengthBytes = cms.int32(-1),
    EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    EmulateBxInEvent = cms.int32(1),
    EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    ExtInputTag = cms.InputTag("hltGtStage2Digis"),
    GetPrescaleColumnFromData = cms.bool(False),
    JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1DataBxInEvent = cms.int32(5),
    MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    PrescaleSet = cms.uint32(1),
    PrintL1Menu = cms.untracked.bool(False),
    ProduceL1GtDaqRecord = cms.bool(True),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    RequireMenuToMatchAlgoBlkInput = cms.bool(True),
    TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    TriggerMenuLuminosity = cms.string('startup'),
    Verbosity = cms.untracked.int32(0),
    resetPSCountersEachLumiSec = cms.bool(True),
    semiRandomInitialPSCounters = cms.bool(False),
    useMuonShowers = cms.bool(True)
)


process.hltHbherecoFromGPU = cms.EDProducer("HcalCPURecHitsProducer",
    produceLegacy = cms.bool(True),
    produceSoA = cms.bool(True),
    recHitsLegacyLabelOut = cms.string(''),
    recHitsM0LabelIn = cms.InputTag("hltHbherecoGPU"),
    recHitsM0LabelOut = cms.string('')
)


process.hltHbherecoGPU = cms.EDProducer("HBHERecHitProducerGPU",
    applyTimeSlew = cms.bool(True),
    digisLabelF01HE = cms.InputTag("hltHcalDigisGPU"),
    digisLabelF3HB = cms.InputTag("hltHcalDigisGPU"),
    digisLabelF5HB = cms.InputTag("hltHcalDigisGPU"),
    firstSampleShift = cms.int32(0),
    kernelMinimizeThreads = cms.vuint32(16, 1, 1),
    kprep1dChannelsPerBlock = cms.uint32(32),
    maxTimeSamples = cms.uint32(10),
    meanTime = cms.double(0.0),
    recHitsLabelM0HBHE = cms.string(''),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    slopeTimeSlewParameters = cms.vdouble(-3.178648, -1.5610227, -1.075824),
    timeSigmaHPD = cms.double(5.0),
    timeSigmaSiPM = cms.double(2.5),
    tmaxTimeSlewParameters = cms.vdouble(16.0, 10.0, 6.25),
    ts4Thresh = cms.double(0.0),
    tzeroTimeSlewParameters = cms.vdouble(23.960177, 11.977461, 9.109694),
    useEffectivePedestals = cms.bool(True)
)


process.hltHbherecoLegacy = cms.EDProducer("HBHEPhase1Reconstructor",
    algoConfigClass = cms.string(''),
    algorithm = cms.PSet(
        Class = cms.string('SimpleHBHEPhase1Algo'),
        activeBXs = cms.vint32(
            -3, -2, -1, 0, 1,
            2, 3, 4
        ),
        applyLegacyHBMCorrection = cms.bool(False),
        applyPedConstraint = cms.bool(False),
        applyPulseJitter = cms.bool(False),
        applyTimeConstraint = cms.bool(False),
        applyTimeSlew = cms.bool(True),
        applyTimeSlewM3 = cms.bool(True),
        calculateArrivalTime = cms.bool(False),
        chiSqSwitch = cms.double(-1.0),
        correctForPhaseContainment = cms.bool(True),
        correctionPhaseNS = cms.double(6.0),
        deltaChiSqThresh = cms.double(0.001),
        dynamicPed = cms.bool(False),
        firstSampleShift = cms.int32(0),
        fitTimes = cms.int32(1),
        meanPed = cms.double(0.0),
        meanTime = cms.double(0.0),
        nMaxItersMin = cms.int32(50),
        nMaxItersNNLS = cms.int32(500),
        nnlsThresh = cms.double(1e-11),
        pulseJitter = cms.double(1.0),
        respCorrM3 = cms.double(1.0),
        samplesToAdd = cms.int32(2),
        tdcTimeShift = cms.double(0.0),
        timeMax = cms.double(12.5),
        timeMin = cms.double(-12.5),
        timeSigmaHPD = cms.double(5.0),
        timeSigmaSiPM = cms.double(2.5),
        timeSlewParsType = cms.int32(3),
        ts4Max = cms.vdouble(100.0, 20000.0, 30000.0),
        ts4Min = cms.double(0.0),
        ts4Thresh = cms.double(0.0),
        ts4chi2 = cms.vdouble(15.0, 15.0),
        useM2 = cms.bool(False),
        useM3 = cms.bool(False),
        useMahi = cms.bool(True)
    ),
    digiLabelQIE11 = cms.InputTag("hltHcalDigis"),
    digiLabelQIE8 = cms.InputTag("hltHcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    flagParametersQIE11 = cms.PSet(

    ),
    flagParametersQIE8 = cms.PSet(
        hitEnergyMinimum = cms.double(1.0),
        hitMultiplicityThreshold = cms.int32(17),
        nominalPedestal = cms.double(3.0),
        pulseShapeParameterSets = cms.VPSet(
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    0.0, 100.0, -50.0, 0.0, -15.0,
                    0.15
                )
            ),
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    100.0, 2000.0, -50.0, 0.0, -5.0,
                    0.05
                )
            ),
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    2000.0, 1000000.0, -50.0, 0.0, 95.0,
                    0.0
                )
            ),
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0,
                    0.0
                )
            )
        )
    ),
    makeRecHits = cms.bool(True),
    processQIE11 = cms.bool(True),
    processQIE8 = cms.bool(False),
    pulseShapeParametersQIE11 = cms.PSet(

    ),
    pulseShapeParametersQIE8 = cms.PSet(
        LeftSlopeCut = cms.vdouble(5.0, 2.55, 2.55),
        LeftSlopeThreshold = cms.vdouble(250.0, 500.0, 100000.0),
        LinearCut = cms.vdouble(-3.0, -0.054, -0.054),
        LinearThreshold = cms.vdouble(20.0, 100.0, 100000.0),
        MinimumChargeThreshold = cms.double(20.0),
        MinimumTS4TS5Threshold = cms.double(100.0),
        R45MinusOneRange = cms.double(0.2),
        R45PlusOneRange = cms.double(0.2),
        RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
        RMS8MaxThreshold = cms.vdouble(20.0, 100.0, 100000.0),
        RightSlopeCut = cms.vdouble(5.0, 4.15, 4.15),
        RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
        RightSlopeSmallThreshold = cms.vdouble(150.0, 200.0, 100000.0),
        RightSlopeThreshold = cms.vdouble(250.0, 400.0, 100000.0),
        TS3TS4ChargeThreshold = cms.double(70.0),
        TS3TS4UpperChargeThreshold = cms.double(20.0),
        TS4TS5ChargeThreshold = cms.double(70.0),
        TS4TS5LowerCut = cms.vdouble(
            -1.0, -0.7, -0.5, -0.4, -0.3,
            0.1
        ),
        TS4TS5LowerThreshold = cms.vdouble(
            100.0, 120.0, 160.0, 200.0, 300.0,
            500.0
        ),
        TS4TS5UpperCut = cms.vdouble(1.0, 0.8, 0.75, 0.72),
        TS4TS5UpperThreshold = cms.vdouble(70.0, 90.0, 100.0, 400.0),
        TS5TS6ChargeThreshold = cms.double(70.0),
        TS5TS6UpperChargeThreshold = cms.double(20.0),
        TriangleIgnoreSlow = cms.bool(False),
        TrianglePeakTS = cms.uint32(10000),
        UseDualFit = cms.bool(True)
    ),
    recoParamsFromDB = cms.bool(True),
    saveDroppedInfos = cms.bool(False),
    saveEffectivePedestal = cms.bool(True),
    saveInfos = cms.bool(False),
    setLegacyFlagsQIE11 = cms.bool(False),
    setLegacyFlagsQIE8 = cms.bool(False),
    setNegativeFlagsQIE11 = cms.bool(False),
    setNegativeFlagsQIE8 = cms.bool(False),
    setNoiseFlagsQIE11 = cms.bool(False),
    setNoiseFlagsQIE8 = cms.bool(False),
    setPulseShapeFlagsQIE11 = cms.bool(False),
    setPulseShapeFlagsQIE8 = cms.bool(False),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    tsFromDB = cms.bool(False),
    use8ts = cms.bool(True)
)


process.hltHcalDigis = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(False),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    silent = cms.untracked.bool(True)
)


process.hltHcalDigisGPU = cms.EDProducer("HcalDigisProducerGPU",
    digisLabelF01HE = cms.string(''),
    digisLabelF3HB = cms.string(''),
    digisLabelF5HB = cms.string(''),
    hbheDigisLabel = cms.InputTag("hltHcalDigis"),
    maxChannelsF01HE = cms.uint32(10000),
    maxChannelsF3HB = cms.uint32(10000),
    maxChannelsF5HB = cms.uint32(10000),
    qie11DigiLabel = cms.InputTag("hltHcalDigis")
)


process.hltHfprereco = cms.EDProducer("HFPreReconstructor",
    digiLabel = cms.InputTag("hltHcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    sumAllTimeSlices = cms.bool(False),
    tsFromDB = cms.bool(False)
)


process.hltHfreco = cms.EDProducer("HFPhase1Reconstructor",
    HFStripFilter = cms.PSet(
        gap = cms.int32(2),
        lstrips = cms.int32(2),
        maxStripTime = cms.double(10.0),
        maxThreshold = cms.double(100.0),
        seedHitIetaMax = cms.int32(35),
        stripThreshold = cms.double(40.0),
        timeMax = cms.double(6.0),
        verboseLevel = cms.untracked.int32(10),
        wedgeCut = cms.double(0.05)
    ),
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82,
            58.7, 63.0, 67.72, 72.86, 78.42,
            84.4, 90.8, 97.62
        ),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317,
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
            47.4813, 49.98, 52.7093
        ),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            40.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0
        ),
        long_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1
        ),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            40.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0
        ),
        short_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1
        )
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82,
            58.7, 63.0, 67.72, 72.86, 78.42,
            84.4, 90.8, 97.62
        ),
        long_optimumSlope = cms.vdouble(
            -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296,
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422,
            0.135313, 0.136289, 0.0589927
        ),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317,
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
            47.4813, 49.98, 52.7093
        ),
        short_optimumSlope = cms.vdouble(
            -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296,
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422,
            0.135313, 0.136289, 0.0589927
        )
    ),
    algoConfigClass = cms.string('HFPhase1PMTParams'),
    algorithm = cms.PSet(
        Class = cms.string('HFFlexibleTimeCheck'),
        energyWeights = cms.vdouble(
            1.0, 1.0, 1.0, 0.0, 1.0,
            0.0, 2.0, 0.0, 2.0, 0.0,
            2.0, 0.0, 1.0, 0.0, 0.0,
            1.0, 0.0, 1.0, 0.0, 2.0,
            0.0, 2.0, 0.0, 2.0, 0.0,
            1.0
        ),
        rejectAllFailures = cms.bool(True),
        soiPhase = cms.uint32(1),
        tfallIfNoTDC = cms.double(-101.0),
        timeShift = cms.double(0.0),
        tlimits = cms.vdouble(-1000.0, 1000.0, -1000.0, 1000.0),
        triseIfNoTDC = cms.double(-100.0)
    ),
    checkChannelQualityForDepth3and4 = cms.bool(False),
    inputLabel = cms.InputTag("hltHfprereco"),
    runHFStripFilter = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    useChannelQualityFromDB = cms.bool(False)
)


process.hltHoreco = cms.EDProducer("HcalHitReconstructor",
    HFInWindowStat = cms.PSet(

    ),
    PETstat = cms.PSet(

    ),
    S8S1stat = cms.PSet(

    ),
    S9S1stat = cms.PSet(

    ),
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(False),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hltHcalDigis"),
    digiTimeFromDB = cms.bool(True),
    digistat = cms.PSet(

    ),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    hfTimingTrustParameters = cms.PSet(

    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(False),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(False),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(False),
    setTimingTrustFlags = cms.bool(False),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag("hltPixelTracks"),
    InputVertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    includeFourthHit = cms.bool(True),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(False),
    useProtoTrackKinematics = cms.bool(False)
)


process.hltIter0PFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter0GroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltIter0PFLowPixelSeedsFromPixelTracks"),
    useHitsSplitting = cms.bool(False)
)


process.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter0'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltSiStripClusters"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("hltIter0PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter0PFlowTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            dr_exp = cms.vint32(4, 4, 4),
            dr_par1 = cms.vdouble(3.40282346639e+38, 0.8, 0.8),
            dr_par2 = cms.vdouble(3.40282346639e+38, 0.6, 0.6)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 4),
            dz_par1 = cms.vdouble(3.40282346639e+38, 0.75, 0.75),
            dz_par2 = cms.vdouble(3.40282346639e+38, 0.5, 0.5)
        ),
        maxChi2 = cms.vdouble(9999.0, 25.0, 16.0),
        maxChi2n = cms.vdouble(1.2, 1.0, 0.7),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 0, 0),
        minLayers = cms.vint32(3, 3, 3),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltMergedTracks = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks")
)


process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotOnlineProducer",
    beamMode = cms.untracked.uint32(11),
    changeToCMSCoordinates = cms.bool(False),
    gtEvmLabel = cms.InputTag(""),
    maxRadius = cms.double(2.0),
    maxZ = cms.double(40.0),
    setSigmaZ = cms.double(0.0),
    src = cms.InputTag(""),
    useTransientRecord = cms.bool(True)
)


process.hltOnlineBeamSpotToGPU = cms.EDProducer("BeamSpotToCUDA",
    src = cms.InputTag("hltOnlineBeamSpot")
)


process.hltOnlineMetaDataDigis = cms.EDProducer("OnlineMetaDataRawToDigi",
    onlineMetaDataInputLabel = cms.InputTag("rawDataCollector")
)


process.hltPSetMap = cms.EDProducer("ParameterSetBlobProducer")


process.hltParticleFlowClusterECALL1Seeded = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        applyCrackCorrections = cms.bool(False),
        applyMVACorrections = cms.bool(True),
        ebSrFlagLabel = cms.InputTag("hltEcalDigis"),
        eeSrFlagLabel = cms.InputTag("hltEcalDigis"),
        maxPtForMVAEvaluation = cms.double(300.0),
        recHitsEBLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        recHitsEELabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        srfAwareCorrection = cms.bool(True)
    ),
    inputECAL = cms.InputTag("hltParticleFlowClusterECALUncorrectedL1Seeded"),
    inputPS = cms.InputTag("hltParticleFlowClusterPSL1Seeded"),
    minimumPSEnergy = cms.double(0.0),
    skipPS = cms.bool(False)
)


process.hltParticleFlowClusterECALUncorrectedL1Seeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                gatheringThreshold = cms.double(0.08),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                recHitEnergyNorm = cms.double(0.08)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )
        ),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECALL1Seeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                seedingThreshold = cms.double(0.6),
                seedingThresholdPt = cms.double(0.15)
            ),
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                gatheringThreshold = cms.double(0.08),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                recHitEnergyNorm = cms.double(0.08)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )
        ),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECALUnseeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                seedingThreshold = cms.double(0.6),
                seedingThresholdPt = cms.double(0.15)
            ),
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltParticleFlowClusterECALUnseeded = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        applyCrackCorrections = cms.bool(False),
        applyMVACorrections = cms.bool(True),
        ebSrFlagLabel = cms.InputTag("hltEcalDigis"),
        eeSrFlagLabel = cms.InputTag("hltEcalDigis"),
        maxPtForMVAEvaluation = cms.double(300.0),
        recHitsEBLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        recHitsEELabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        srfAwareCorrection = cms.bool(True)
    ),
    inputECAL = cms.InputTag("hltParticleFlowClusterECALUncorrectedUnseeded"),
    inputPS = cms.InputTag("hltParticleFlowClusterPSUnseeded"),
    minimumPSEnergy = cms.double(0.0),
    skipPS = cms.bool(False)
)


process.hltParticleFlowClusterHBHE = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                gatheringThreshold = cms.vdouble(0.4, 0.3, 0.3, 0.3),
                gatheringThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThreshold = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                ),
                gatheringThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0
                )
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        clusterTimeResFromSeed = cms.bool(False),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(5),
        maxNSigmaTime = cms.double(10.0),
        minChi2Prob = cms.double(0.0),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                recHitEnergyNorm = cms.vdouble(0.4, 0.3, 0.3, 0.3)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                )
            )
        ),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08),
        timeResolutionCalcBarrel = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeResolutionCalcEndcap = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeSigmaEB = cms.double(10.0),
        timeSigmaEE = cms.double(10.0)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHBHE"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                seedingThreshold = cms.vdouble(0.6, 0.5, 0.5, 0.5),
                seedingThresholdPt = cms.vdouble(0.0, 0.0, 0.0, 0.0)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                seedingThreshold = cms.vdouble(
                    0.1375, 0.275, 0.275, 0.275, 0.275,
                    0.275, 0.275
                ),
                seedingThresholdPt = cms.vdouble(
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0
                )
            )
        )
    )
)


process.hltParticleFlowClusterHCAL = cms.EDProducer("PFMultiDepthClusterProducer",
    clustersSource = cms.InputTag("hltParticleFlowClusterHBHE"),
    energyCorrector = cms.PSet(

    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('PFMultiDepthClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        minFractionToKeep = cms.double(1e-07),
        nSigmaEta = cms.double(2.0),
        nSigmaPhi = cms.double(2.0)
    ),
    positionReCalc = cms.PSet(

    )
)


process.hltParticleFlowClusterPSL1Seeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                recHitEnergyNorm = cms.double(6e-05)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )
        ),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitPSL1Seeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltParticleFlowClusterPSUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                recHitEnergyNorm = cms.double(6e-05)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )
        ),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitPSUnseeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltParticleFlowRecHitECALL1Seeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            name = cms.string('PFEBRecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEB")
        ),
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEE")
        )
    )
)


process.hltParticleFlowRecHitECALUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            name = cms.string('PFEBRecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEB")
        ),
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEE")
        )
    )
)


process.hltParticleFlowRecHitHBHE = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        hcalEnums = cms.vint32(1, 2),
        name = cms.string('PFRecHitHCALDenseIdNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFHBHERecHitCreator'),
        qualityTests = cms.VPSet(
            cms.PSet(
                cuts = cms.VPSet(
                    cms.PSet(
                        depth = cms.vint32(1, 2, 3, 4),
                        detectorEnum = cms.int32(1),
                        threshold = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                    ),
                    cms.PSet(
                        depth = cms.vint32(
                            1, 2, 3, 4, 5,
                            6, 7
                        ),
                        detectorEnum = cms.int32(2),
                        threshold = cms.vdouble(
                            0.1, 0.2, 0.2, 0.2, 0.2,
                            0.2, 0.2
                        )
                    )
                ),
                name = cms.string('PFRecHitQTestHCALThresholdVsDepth')
            ),
            cms.PSet(
                cleaningThresholds = cms.vdouble(0.0),
                flags = cms.vstring('Standard'),
                maxSeverities = cms.vint32(11),
                name = cms.string('PFRecHitQTestHCALChannel')
            )
        ),
        src = cms.InputTag("hltHbhereco")
    ))
)


process.hltParticleFlowRecHitPSL1Seeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(7e-06)
        )),
        src = cms.InputTag("hltRechitInRegionsES","EcalRecHitsES")
    ))
)


process.hltParticleFlowRecHitPSUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(7e-06)
        )),
        src = cms.InputTag("hltEcalPreshowerRecHit","EcalRecHitsES")
    ))
)


process.hltParticleFlowSuperClusterECALL1Seeded = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("hltOnlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('hltParticleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('hltParticleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('hltParticleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    PFSuperClusterCollectionBarrel = cms.string('hltParticleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('hltParticleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('hltParticleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    barrelRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    endcapRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    isOOTCollection = cms.bool(False),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        isHLT = cms.bool(True),
        regTrainedWithPS = cms.bool(True),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_online'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_online'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_online'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_online')
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.5),
    thresh_PFClusterES = cms.double(0.5),
    thresh_PFClusterEndcap = cms.double(0.5),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.hltParticleFlowSuperClusterECALUnseeded = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("hltOnlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("hltParticleFlowClusterECALUnseeded"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('hltParticleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('hltParticleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('hltParticleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("hltParticleFlowClusterECALUnseeded"),
    PFSuperClusterCollectionBarrel = cms.string('hltParticleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('hltParticleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('hltParticleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    barrelRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    endcapRecHits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    isOOTCollection = cms.bool(False),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        isHLT = cms.bool(True),
        regTrainedWithPS = cms.bool(True),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_online'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_online'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_online'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_online')
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.5),
    thresh_PFClusterES = cms.double(0.5),
    thresh_PFClusterEndcap = cms.double(0.5),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.hltPixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2',
        'BPix1+BPix3',
        'BPix1+BPix4',
        'BPix2+BPix3',
        'BPix2+BPix4',
        'BPix3+BPix4',
        'FPix1_pos+FPix2_pos',
        'FPix1_pos+FPix3_pos',
        'FPix2_pos+FPix3_pos',
        'BPix1+FPix1_pos',
        'BPix1+FPix2_pos',
        'BPix1+FPix3_pos',
        'BPix2+FPix1_pos',
        'BPix2+FPix2_pos',
        'BPix2+FPix3_pos',
        'BPix3+FPix1_pos',
        'BPix3+FPix2_pos',
        'BPix3+FPix3_pos',
        'BPix4+FPix1_pos',
        'BPix4+FPix2_pos',
        'BPix4+FPix3_pos',
        'FPix1_neg+FPix2_neg',
        'FPix1_neg+FPix3_neg',
        'FPix2_neg+FPix3_neg',
        'BPix1+FPix1_neg',
        'BPix1+FPix2_neg',
        'BPix1+FPix3_neg',
        'BPix2+FPix1_neg',
        'BPix2+FPix2_neg',
        'BPix2+FPix3_neg',
        'BPix3+FPix1_neg',
        'BPix3+FPix2_neg',
        'BPix3+FPix3_neg',
        'BPix4+FPix1_neg',
        'BPix4+FPix2_neg',
        'BPix4+FPix3_neg'
    )
)


process.hltPixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3',
        'BPix2+BPix3+BPix4',
        'BPix1+BPix3+BPix4',
        'BPix1+BPix2+BPix4',
        'BPix2+BPix3+FPix1_pos',
        'BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos',
        'BPix1+BPix2+FPix1_neg',
        'BPix2+FPix1_pos+FPix2_pos',
        'BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos',
        'BPix1+FPix1_neg+FPix2_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg',
        'BPix1+BPix3+FPix1_pos',
        'BPix1+BPix2+FPix2_pos',
        'BPix1+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix2_neg',
        'BPix1+FPix2_neg+FPix3_neg',
        'BPix1+FPix1_neg+FPix3_neg',
        'BPix1+FPix2_pos+FPix3_pos',
        'BPix1+FPix1_pos+FPix3_pos'
    )
)


process.hltPixelTracks = cms.EDProducer("PixelTrackProducerFromSoAPhase1",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    minNumberOfHits = cms.int32(0),
    minQuality = cms.string('loose'),
    pixelRecHitLegacySrc = cms.InputTag("hltSiPixelRecHits"),
    trackSrc = cms.InputTag("hltPixelTracksSoA")
)


process.hltPixelTracksCPU = cms.EDProducer("CAHitNtupletCUDAPhase1",
    CAThetaCutBarrel = cms.double(0.00200000009499),
    CAThetaCutForward = cms.double(0.00300000002608),
    dcaCutInnerTriplet = cms.double(0.15000000596),
    dcaCutOuterTriplet = cms.double(0.25),
    doClusterCut = cms.bool(True),
    doPtCut = cms.bool(True),
    doSharedHitCut = cms.bool(True),
    doZ0Cut = cms.bool(True),
    dupPassThrough = cms.bool(False),
    earlyFishbone = cms.bool(True),
    fillStatistics = cms.bool(False),
    fitNas4 = cms.bool(False),
    hardCurvCut = cms.double(0.0328407224959),
    idealConditions = cms.bool(False),
    includeJumpingForwardDoublets = cms.bool(True),
    lateFishbone = cms.bool(False),
    maxNumberOfDoublets = cms.uint32(524288),
    minHitsForSharingCut = cms.uint32(10),
    minHitsPerNtuplet = cms.uint32(3),
    onGPU = cms.bool(False),
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsFromLegacy"),
    ptmin = cms.double(0.899999976158),
    trackQualityCuts = cms.PSet(
        chi2Coeff = cms.vdouble(0.9, 1.8),
        chi2MaxPt = cms.double(10.0),
        chi2Scale = cms.double(8.0),
        quadrupletMaxTip = cms.double(0.5),
        quadrupletMaxZip = cms.double(12.0),
        quadrupletMinPt = cms.double(0.3),
        tripletMaxTip = cms.double(0.3),
        tripletMaxZip = cms.double(12.0),
        tripletMinPt = cms.double(0.5)
    ),
    useRiemannFit = cms.bool(False),
    useSimpleTripletCleaner = cms.bool(True)
)


process.hltPixelTracksFilter = cms.EDProducer("PixelTrackFilterByKinematicsProducer",
    chi2 = cms.double(1000.0),
    nSigmaInvPtTolerance = cms.double(0.0),
    nSigmaTipMaxTolerance = cms.double(0.0),
    ptMin = cms.double(0.1),
    tipMax = cms.double(1.0)
)


process.hltPixelTracksFitter = cms.EDProducer("PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool(False),
    scaleFactor = cms.double(0.65)
)


process.hltPixelTracksFromGPU = cms.EDProducer("PixelTrackSoAFromCUDAPhase1",
    src = cms.InputTag("hltPixelTracksGPU")
)


process.hltPixelTracksGPU = cms.EDProducer("CAHitNtupletCUDAPhase1",
    CAThetaCutBarrel = cms.double(0.00200000009499),
    CAThetaCutForward = cms.double(0.00300000002608),
    dcaCutInnerTriplet = cms.double(0.15000000596),
    dcaCutOuterTriplet = cms.double(0.25),
    doClusterCut = cms.bool(True),
    doPtCut = cms.bool(True),
    doSharedHitCut = cms.bool(True),
    doZ0Cut = cms.bool(True),
    dupPassThrough = cms.bool(False),
    earlyFishbone = cms.bool(True),
    fillStatistics = cms.bool(False),
    fitNas4 = cms.bool(False),
    hardCurvCut = cms.double(0.0328407224959),
    idealConditions = cms.bool(False),
    includeJumpingForwardDoublets = cms.bool(True),
    lateFishbone = cms.bool(False),
    maxNumberOfDoublets = cms.uint32(524288),
    minHitsForSharingCut = cms.uint32(10),
    minHitsPerNtuplet = cms.uint32(3),
    onGPU = cms.bool(True),
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsGPU"),
    ptmin = cms.double(0.899999976158),
    trackQualityCuts = cms.PSet(
        chi2Coeff = cms.vdouble(0.9, 1.8),
        chi2MaxPt = cms.double(10.0),
        chi2Scale = cms.double(8.0),
        quadrupletMaxTip = cms.double(0.5),
        quadrupletMaxZip = cms.double(12.0),
        quadrupletMinPt = cms.double(0.3),
        tripletMaxTip = cms.double(0.3),
        tripletMaxZip = cms.double(12.0),
        tripletMinPt = cms.double(0.5)
    ),
    useRiemannFit = cms.bool(False),
    useSimpleTripletCleaner = cms.bool(True)
)


process.hltPixelTracksTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        nSigmaZ = cms.double(4.0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.8)
    )
)


process.hltPixelVertices = cms.EDProducer("PixelVertexProducerFromSoA",
    TrackCollection = cms.InputTag("hltPixelTracks"),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    src = cms.InputTag("hltPixelVerticesSoA")
)


process.hltPixelVerticesCPU = cms.EDProducer("PixelVertexProducerCUDAPhase1",
    PtMax = cms.double(75.0),
    PtMin = cms.double(0.5),
    chi2max = cms.double(9.0),
    eps = cms.double(0.07),
    errmax = cms.double(0.01),
    minT = cms.int32(2),
    onGPU = cms.bool(False),
    oneKernel = cms.bool(True),
    pixelTrackSrc = cms.InputTag("hltPixelTracksSoA"),
    useDBSCAN = cms.bool(False),
    useDensity = cms.bool(True),
    useIterative = cms.bool(False)
)


process.hltPixelVerticesFromGPU = cms.EDProducer("PixelVertexSoAFromCUDA",
    src = cms.InputTag("hltPixelVerticesGPU")
)


process.hltPixelVerticesGPU = cms.EDProducer("PixelVertexProducerCUDAPhase1",
    PtMax = cms.double(75.0),
    PtMin = cms.double(0.5),
    chi2max = cms.double(9.0),
    eps = cms.double(0.07),
    errmax = cms.double(0.01),
    minT = cms.int32(2),
    onGPU = cms.bool(True),
    oneKernel = cms.bool(True),
    pixelTrackSrc = cms.InputTag("hltPixelTracksGPU"),
    useDBSCAN = cms.bool(False),
    useDensity = cms.bool(True),
    useIterative = cms.bool(False)
)


process.hltRechitInRegionsECAL = cms.EDProducer("HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet(
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","EGamma"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(5.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('EGamma')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Jet"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(170.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Jet')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Tau"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(100.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Tau')
        )
    ),
    productLabels = cms.vstring(
        'EcalRecHitsEB',
        'EcalRecHitsEE'
    ),
    recHitLabels = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE")
)


process.hltRechitInRegionsES = cms.EDProducer("HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet(
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","EGamma"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(5.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('EGamma')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Jet"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(170.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Jet')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Tau"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(100.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Tau')
        )
    ),
    productLabels = cms.vstring('EcalRecHitsES'),
    recHitLabels = cms.VInputTag("hltEcalPreshowerRecHit:EcalRecHitsES")
)


process.hltSiPixelClustersCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelClustersFromSoA = cms.EDProducer("SiPixelDigisClustersFromSoAPhase1",
    clusterThreshold_layer1 = cms.int32(4000),
    clusterThreshold_otherLayers = cms.int32(4000),
    produceDigis = cms.bool(False),
    src = cms.InputTag("hltSiPixelDigisSoA"),
    storeDigis = cms.bool(False)
)


process.hltSiPixelClustersGPU = cms.EDProducer("SiPixelRawToClusterCUDA",
    CablingMapLabel = cms.string(''),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    UseQualityInfo = cms.bool(False),
    clusterThreshold_layer1 = cms.int32(4000),
    clusterThreshold_otherLayers = cms.int32(4000),
    isRun2 = cms.bool(False)
)


process.hltSiPixelClustersLegacy = cms.EDProducer("SiPixelClusterProducer",
    ChannelThreshold = cms.int32(10),
    ClusterMode = cms.string('PixelThresholdClusterizer'),
    ClusterThreshold = cms.int32(4000),
    ClusterThreshold_L1 = cms.int32(4000),
    DropDuplicates = cms.bool(True),
    ElectronPerADCGain = cms.double(135.0),
    MissCalibrate = cms.bool(True),
    Phase2Calibration = cms.bool(False),
    Phase2DigiBaseline = cms.double(1200.0),
    Phase2KinkADC = cms.int32(8),
    Phase2ReadoutMode = cms.int32(-1),
    SeedThreshold = cms.int32(1000),
    SplitClusters = cms.bool(False),
    VCaltoElectronGain = cms.int32(1),
    VCaltoElectronGain_L1 = cms.int32(1),
    VCaltoElectronOffset = cms.int32(0),
    VCaltoElectronOffset_L1 = cms.int32(0),
    maxNumberOfClusters = cms.int32(40000),
    payloadType = cms.string('HLT'),
    src = cms.InputTag("hltSiPixelDigisLegacy")
)


process.hltSiPixelDigiErrorsSoA = cms.EDProducer("SiPixelDigiErrorsSoAFromCUDA",
    src = cms.InputTag("hltSiPixelClustersGPU")
)


process.hltSiPixelDigisFromSoA = cms.EDProducer("SiPixelDigiErrorsFromSoA",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(29),
    UsePhase1 = cms.bool(True),
    UserErrorList = cms.vint32(40),
    digiErrorSoASrc = cms.InputTag("hltSiPixelDigiErrorsSoA")
)


process.hltSiPixelDigisLegacy = cms.EDProducer("SiPixelRawToDigi",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(29),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    SiPixelQualityLabel = cms.string(''),
    UsePhase1 = cms.bool(True),
    UsePilotBlade = cms.bool(False),
    UseQualityInfo = cms.bool(False),
    UserErrorList = cms.vint32()
)


process.hltSiPixelDigisSoA = cms.EDProducer("SiPixelDigisSoAFromCUDA",
    src = cms.InputTag("hltSiPixelClustersGPU")
)


process.hltSiPixelRecHitsFromGPU = cms.EDProducer("SiPixelRecHitFromCUDAPhase1",
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsGPU"),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelRecHitsFromLegacy = cms.EDProducer("SiPixelRecHitSoAFromLegacyPhase1",
    CPE = cms.string('hltESPPixelCPEFast'),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    convertToLegacy = cms.bool(True),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelRecHitsGPU = cms.EDProducer("SiPixelRecHitCUDAPhase1",
    CPE = cms.string('hltESPPixelCPEFast'),
    beamSpot = cms.InputTag("hltOnlineBeamSpotToGPU"),
    src = cms.InputTag("hltSiPixelClustersGPU")
)


process.hltSiPixelRecHitsSoAFromGPU = cms.EDProducer("SiPixelRecHitSoAFromCUDAPhase1",
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsGPU")
)


process.hltSiStripClusters = cms.EDProducer("MeasurementTrackerEventProducer",
    Phase2TrackerCluster1DProducer = cms.string(''),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("hltSiPixelDigis"),
    inactivePixelDetectorLabels = cms.VInputTag("hltSiPixelDigis"),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    measurementTracker = cms.string('hltESPMeasurementTracker'),
    pixelCablingMapLabel = cms.string(''),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string('hltSiStripRawToClustersFacility'),
    switchOffPixelsIfEmpty = cms.bool(True),
    vectorHits = cms.InputTag(""),
    vectorHitsRej = cms.InputTag("")
)


process.hltSiStripExcludedFEDListProducer = cms.EDProducer("SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag("rawDataCollector")
)


process.hltSiStripRawToClustersFacility = cms.EDProducer("SiStripClusterizerFromRaw",
    Algorithms = cms.PSet(
        CommonModeNoiseSubtractionMode = cms.string('Median'),
        PedestalSubtractionFedMode = cms.bool(True),
        SiStripFedZeroSuppressionMode = cms.uint32(4),
        TruncateInSuppressor = cms.bool(True),
        Use10bitsTruncation = cms.bool(False),
        doAPVRestore = cms.bool(False),
        useCMMeanMap = cms.bool(False)
    ),
    Clusterizer = cms.PSet(
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        ChannelThreshold = cms.double(2.0),
        ClusterThreshold = cms.double(5.0),
        ConditionsLabel = cms.string(''),
        MaxAdjacentBad = cms.uint32(0),
        MaxSequentialBad = cms.uint32(1),
        MaxSequentialHoles = cms.uint32(0),
        RemoveApvShots = cms.bool(True),
        SeedThreshold = cms.double(3.0),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
        ),
        setDetId = cms.bool(True)
    ),
    DoAPVEmulatorCheck = cms.bool(False),
    HybridZeroSuppressed = cms.bool(False),
    ProductLabel = cms.InputTag("rawDataCollector"),
    onDemand = cms.bool(True)
)


process.hltTriggerSummaryAOD = cms.EDProducer("TriggerSummaryProducerAOD",
    moduleLabelPatternsToMatch = cms.vstring('hlt*'),
    moduleLabelPatternsToSkip = cms.vstring(),
    processName = cms.string('@'),
    throw = cms.bool(False)
)


process.hltTriggerSummaryRAW = cms.EDProducer("TriggerSummaryProducerRAW",
    processName = cms.string('@')
)


process.hltTrimmedPixelVertices = cms.EDProducer("PixelVertexCollectionTrimmer",
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    ),
    fractionSumPt2 = cms.double(0.3),
    maxVtx = cms.uint32(100),
    minSumPt2 = cms.double(0.0),
    src = cms.InputTag("hltPixelVertices")
)


process.packCaloStage2 = cms.EDProducer("L1TDigiToRaw",
    FWId = cms.uint32(1),
    FedId = cms.int32(1366),
    InputLabel = cms.InputTag("simCaloStage2Digis"),
    Setup = cms.string('stage2::CaloSetup'),
    TowerInputLabel = cms.InputTag("simCaloStage2Layer1Digis"),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.packGmtStage2 = cms.EDProducer("L1TDigiToRaw",
    BMTFInputLabel = cms.InputTag("simKBmtfDigis","BMTF"),
    EMTFInputLabel = cms.InputTag("simEmtfDigis","EMTF"),
    EMTFShowerInputLabel = cms.InputTag("simEmtfShowers","EMTF"),
    FWId = cms.uint32(134217728),
    FedId = cms.int32(1402),
    ImdInputLabelBMTF = cms.InputTag("simGmtStage2Digis","imdMuonsBMTF"),
    ImdInputLabelEMTFNeg = cms.InputTag("simGmtStage2Digis","imdMuonsEMTFNeg"),
    ImdInputLabelEMTFPos = cms.InputTag("simGmtStage2Digis","imdMuonsEMTFPos"),
    ImdInputLabelOMTFNeg = cms.InputTag("simGmtStage2Digis","imdMuonsOMTFNeg"),
    ImdInputLabelOMTFPos = cms.InputTag("simGmtStage2Digis","imdMuonsOMTFPos"),
    InputLabel = cms.InputTag("simGmtStage2Digis"),
    OMTFInputLabel = cms.InputTag("simOmtfDigis","OMTF"),
    Setup = cms.string('stage2::GMTSetup'),
    ShowerInputLabel = cms.InputTag("simGmtShowerDigis"),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.packGtStage2 = cms.EDProducer("L1TDigiToRaw",
    EGammaInputTag = cms.InputTag("simCaloStage2Digis"),
    EtSumInputTag = cms.InputTag("simCaloStage2Digis"),
    ExtInputTag = cms.InputTag("simGtExtFakeStage2Digis"),
    FWId = cms.uint32(4432),
    FedId = cms.int32(1404),
    GtInputTag = cms.InputTag("simGtStage2Digis"),
    JetInputTag = cms.InputTag("simCaloStage2Digis"),
    MuonInputTag = cms.InputTag("simGmtStage2Digis"),
    Setup = cms.string('stage2::GTSetup'),
    ShowerInputLabel = cms.InputTag("simGmtShowerDigis"),
    TauInputTag = cms.InputTag("simCaloStage2Digis"),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.rawDataCollector = cms.EDProducer("RawDataCollectorByLabel",
    RawCollectionList = cms.VInputTag("packCaloStage2", "packGmtStage2", "packGtStage2", cms.InputTag("rawDataCollector","","@skipCurrentProcess")),
    verbose = cms.untracked.int32(0)
)


process.simBmtfDigis = cms.EDProducer("L1TMuonBarrelTrackProducer",
    DTDigi_Source = cms.InputTag("simTwinMuxDigis"),
    DTDigi_Theta_Source = cms.InputTag("simDtTriggerPrimitiveDigis"),
    Debug = cms.untracked.int32(0)
)


process.simCaloStage2Digis = cms.EDProducer("L1TStage2Layer2Producer",
    firmware = cms.int32(1),
    towerToken = cms.InputTag("simCaloStage2Layer1Digis"),
    useStaticConfig = cms.bool(False)
)


process.simCaloStage2Layer1Digis = cms.EDProducer("L1TCaloLayer1",
    ecalToken = cms.InputTag("unpackEcal","EcalTriggerPrimitives"),
    firmwareVersion = cms.int32(3),
    hcalToken = cms.InputTag("simHcalTriggerPrimitiveDigis"),
    unpackEcalMask = cms.bool(False),
    unpackHcalMask = cms.bool(False),
    useCalib = cms.bool(True),
    useECALLUT = cms.bool(True),
    useHCALLUT = cms.bool(True),
    useHFLUT = cms.bool(True),
    useLSB = cms.bool(True),
    verbose = cms.bool(False)
)


process.simCscTriggerPrimitiveDigis = cms.EDProducer("CSCTriggerPrimitivesProducer",
    CSCComparatorDigiProducer = cms.InputTag("unpackCSC","MuonCSCComparatorDigi"),
    CSCWireDigiProducer = cms.InputTag("unpackCSC","MuonCSCWireDigi"),
    GEMPadDigiClusterProducer = cms.InputTag("simMuonGEMPadDigiClusters"),
    MaxBX = cms.int32(11),
    MinBX = cms.int32(5),
    alctPhase1 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(4),
        alctGhostCancellationSideQuality = cms.bool(False),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(False),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(4),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    alctPhase2 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    alctPhase2GEM = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    checkBadChambers = cms.bool(False),
    clctPhase1 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctLocalShowerThresh = cms.int32(12),
        clctLocalShowerZone = cms.int32(25),
        clctMinSeparation = cms.uint32(10),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctStartBxShift = cms.int32(0),
        useDeadTimeZoning = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    clctPhase2 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctLocalShowerThresh = cms.int32(12),
        clctLocalShowerZone = cms.int32(25),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        useDeadTimeZoning = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    clctPhase2GEM = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctLocalShowerThresh = cms.int32(12),
        clctLocalShowerZone = cms.int32(25),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        useDeadTimeZoning = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    commonParam = cms.PSet(
        disableME1a = cms.bool(False),
        disableME42 = cms.bool(False),
        enableAlctPhase2 = cms.bool(False),
        gangedME1a = cms.bool(False),
        run3 = cms.bool(True),
        runCCLUT_OTMB = cms.bool(True),
        runCCLUT_TMB = cms.bool(False),
        runME11ILT = cms.bool(True),
        runME11Up = cms.bool(True),
        runME21ILT = cms.bool(False),
        runME21Up = cms.bool(True),
        runME31Up = cms.bool(True),
        runME41Up = cms.bool(True),
        runPhase2 = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    copadParamGE11 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(8),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    copadParamGE21 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(8),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    debugParameters = cms.bool(True),
    keepALCTPreTriggers = cms.bool(False),
    keepCLCTPreTriggers = cms.bool(True),
    keepShowers = cms.bool(True),
    mpcParam = cms.PSet(
        dropInvalidStubs = cms.bool(False),
        dropLowQualityStubs = cms.bool(False),
        maxStubs = cms.uint32(18),
        sortStubs = cms.bool(False)
    ),
    selectedChambers = cms.vstring(),
    showerParam = cms.PSet(
        anodeShower = cms.PSet(
            minLayersCentralTBin = cms.uint32(5),
            showerNumTBins = cms.uint32(1),
            showerThresholds = cms.vuint32(
                140, 140, 140, 140, 140,
                140, 7, 14, 18, 23,
                56, 58, 12, 28, 32,
                21, 55, 57, 12, 26,
                34, 25, 62, 64, 12,
                27, 31
            )
        ),
        cathodeShower = cms.PSet(
            minLayersCentralTBin = cms.uint32(5),
            peakCheck = cms.bool(False),
            showerNumTBins = cms.uint32(3),
            showerThresholds = cms.vuint32(
                100, 100, 100, 10000, 10000,
                10000, 10000, 10000, 10000, 14,
                33, 35, 10000, 10000, 10000,
                12, 31, 33, 10000, 10000,
                10000, 14, 34, 36, 10000,
                10000, 10000
            )
        ),
        source = cms.vuint32(
            3, 1, 1, 3, 1,
            3, 1, 3, 1
        )
    ),
    tmbPhase1 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctTrigEnable = cms.uint32(0),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        sortClctBx = cms.bool(True),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctTrigEnable = cms.uint32(0),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        sortClctBx = cms.bool(True),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2GE11 = cms.PSet(
        BunchCrossingCSCminGEMwindow = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        alctTrigEnable = cms.uint32(0),
        assignGEMCSCBending = cms.bool(True),
        buildLCTfromALCTandGEM = cms.bool(True),
        buildLCTfromCLCTandGEM = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        delayGEMinOTMB = cms.uint32(0),
        dropLowQualityALCTs = cms.bool(True),
        dropLowQualityCLCTs = cms.bool(True),
        dropLowQualityCLCTs_ME1a = cms.bool(True),
        enableMatchGEMandME1a = cms.bool(True),
        enableMatchGEMandME1b = cms.bool(True),
        ignoreAlctCrossClct = cms.bool(True),
        matchCLCTpropagation = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        maxDeltaHsEven = cms.uint32(5),
        maxDeltaHsOdd = cms.uint32(10),
        maxDeltaWG = cms.uint32(7),
        mitigateSlopeByCosi = cms.bool(False),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        sortClctBx = cms.bool(True),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0),
        windowBXALCTGEM = cms.uint32(3),
        windowBXCLCTGEM = cms.uint32(7)
    ),
    tmbPhase2GE21 = cms.PSet(
        BunchCrossingCSCminGEMwindow = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        alctTrigEnable = cms.uint32(0),
        assignGEMCSCBending = cms.bool(True),
        buildLCTfromALCTandGEM = cms.bool(True),
        buildLCTfromCLCTandGEM = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        delayGEMinOTMB = cms.uint32(0),
        dropLowQualityALCTs = cms.bool(True),
        dropLowQualityCLCTs = cms.bool(True),
        dropLowQualityCLCTs_ME1a = cms.bool(True),
        enableMatchGEMandME1a = cms.bool(True),
        enableMatchGEMandME1b = cms.bool(True),
        ignoreAlctCrossClct = cms.bool(True),
        matchCLCTpropagation = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        maxDeltaHsEven = cms.uint32(5),
        maxDeltaHsOdd = cms.uint32(10),
        maxDeltaWG = cms.uint32(7),
        mitigateSlopeByCosi = cms.bool(False),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        sortClctBx = cms.bool(True),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0),
        windowBXALCTGEM = cms.uint32(3),
        windowBXCLCTGEM = cms.uint32(7)
    )
)


process.simCscTriggerPrimitiveDigisRun3 = cms.EDProducer("CSCTriggerPrimitivesProducer",
    CSCComparatorDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi"),
    CSCWireDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi"),
    GEMPadDigiClusterProducer = cms.InputTag("simMuonGEMPadDigiClusters"),
    MaxBX = cms.int32(11),
    MinBX = cms.int32(5),
    alctPhase1 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(4),
        alctGhostCancellationSideQuality = cms.bool(False),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(False),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(4),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    alctPhase2 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    alctPhase2GEM = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    checkBadChambers = cms.bool(False),
    clctPhase1 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctLocalShowerThresh = cms.int32(12),
        clctLocalShowerZone = cms.int32(25),
        clctMinSeparation = cms.uint32(10),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctStartBxShift = cms.int32(0),
        useDeadTimeZoning = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    clctPhase2 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctLocalShowerThresh = cms.int32(12),
        clctLocalShowerZone = cms.int32(25),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        useDeadTimeZoning = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    clctPhase2GEM = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctLocalShowerThresh = cms.int32(12),
        clctLocalShowerZone = cms.int32(25),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        useDeadTimeZoning = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    commonParam = cms.PSet(
        disableME1a = cms.bool(False),
        disableME42 = cms.bool(False),
        enableAlctPhase2 = cms.bool(False),
        gangedME1a = cms.bool(False),
        run3 = cms.bool(True),
        runCCLUT_OTMB = cms.bool(True),
        runCCLUT_TMB = cms.bool(False),
        runME11ILT = cms.bool(True),
        runME11Up = cms.bool(True),
        runME21ILT = cms.bool(False),
        runME21Up = cms.bool(True),
        runME31Up = cms.bool(True),
        runME41Up = cms.bool(True),
        runPhase2 = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    copadParamGE11 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(8),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    copadParamGE21 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(8),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    debugParameters = cms.bool(True),
    keepALCTPreTriggers = cms.bool(False),
    keepCLCTPreTriggers = cms.bool(True),
    keepShowers = cms.bool(True),
    mpcParam = cms.PSet(
        dropInvalidStubs = cms.bool(False),
        dropLowQualityStubs = cms.bool(False),
        maxStubs = cms.uint32(18),
        sortStubs = cms.bool(False)
    ),
    selectedChambers = cms.vstring(),
    showerParam = cms.PSet(
        anodeShower = cms.PSet(
            minLayersCentralTBin = cms.uint32(5),
            showerNumTBins = cms.uint32(1),
            showerThresholds = cms.vuint32(
                140, 140, 140, 140, 140,
                140, 7, 14, 18, 23,
                56, 58, 12, 28, 32,
                21, 55, 57, 12, 26,
                34, 25, 62, 64, 12,
                27, 31
            )
        ),
        cathodeShower = cms.PSet(
            minLayersCentralTBin = cms.uint32(5),
            peakCheck = cms.bool(False),
            showerNumTBins = cms.uint32(3),
            showerThresholds = cms.vuint32(
                100, 100, 100, 10000, 10000,
                10000, 10000, 10000, 10000, 14,
                33, 35, 10000, 10000, 10000,
                12, 31, 33, 10000, 10000,
                10000, 14, 34, 36, 10000,
                10000, 10000
            )
        ),
        source = cms.vuint32(
            3, 1, 1, 3, 1,
            3, 1, 3, 1
        )
    ),
    tmbPhase1 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctTrigEnable = cms.uint32(0),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        sortClctBx = cms.bool(True),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2 = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctTrigEnable = cms.uint32(0),
        ignoreAlctCrossClct = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        sortClctBx = cms.bool(True),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbPhase2GE11 = cms.PSet(
        BunchCrossingCSCminGEMwindow = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        alctTrigEnable = cms.uint32(0),
        assignGEMCSCBending = cms.bool(True),
        buildLCTfromALCTandGEM = cms.bool(True),
        buildLCTfromCLCTandGEM = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        delayGEMinOTMB = cms.uint32(0),
        dropLowQualityALCTs = cms.bool(True),
        dropLowQualityCLCTs = cms.bool(True),
        dropLowQualityCLCTs_ME1a = cms.bool(True),
        enableMatchGEMandME1a = cms.bool(True),
        enableMatchGEMandME1b = cms.bool(True),
        ignoreAlctCrossClct = cms.bool(True),
        matchCLCTpropagation = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        maxDeltaHsEven = cms.uint32(5),
        maxDeltaHsOdd = cms.uint32(10),
        maxDeltaWG = cms.uint32(7),
        mitigateSlopeByCosi = cms.bool(False),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        sortClctBx = cms.bool(True),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0),
        windowBXALCTGEM = cms.uint32(3),
        windowBXCLCTGEM = cms.uint32(7)
    ),
    tmbPhase2GE21 = cms.PSet(
        BunchCrossingCSCminGEMwindow = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        alctTrigEnable = cms.uint32(0),
        assignGEMCSCBending = cms.bool(True),
        buildLCTfromALCTandGEM = cms.bool(True),
        buildLCTfromCLCTandGEM = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        delayGEMinOTMB = cms.uint32(0),
        dropLowQualityALCTs = cms.bool(True),
        dropLowQualityCLCTs = cms.bool(True),
        dropLowQualityCLCTs_ME1a = cms.bool(True),
        enableMatchGEMandME1a = cms.bool(True),
        enableMatchGEMandME1b = cms.bool(True),
        ignoreAlctCrossClct = cms.bool(True),
        matchCLCTpropagation = cms.bool(True),
        matchEarliestClctOnly = cms.bool(True),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        maxDeltaHsEven = cms.uint32(5),
        maxDeltaHsOdd = cms.uint32(10),
        maxDeltaWG = cms.uint32(7),
        mitigateSlopeByCosi = cms.bool(False),
        mpcBlockMe1a = cms.uint32(0),
        preferredBxMatch = cms.vint32(
            0, -1, 1, -2, 2,
            -3, 3
        ),
        sortClctBx = cms.bool(True),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0),
        windowBXALCTGEM = cms.uint32(3),
        windowBXCLCTGEM = cms.uint32(7)
    )
)


process.simDtTriggerPrimitiveDigis = cms.EDProducer("DTTrigProd",
    DTTFSectorNumbering = cms.bool(True),
    debug = cms.untracked.bool(False),
    digiTag = cms.InputTag("unpackDT"),
    lutBtic = cms.untracked.int32(31),
    lutDumpFlag = cms.untracked.bool(False)
)


process.simEmtfDigis = cms.EDProducer("L1TMuonEndCapTrackProducer",
    BXWindow = cms.int32(2),
    CPPFEnable = cms.bool(False),
    CPPFInput = cms.InputTag("simCPPFDigis"),
    CSCComparatorInput = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi"),
    CSCEnable = cms.bool(True),
    CSCInput = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED"),
    CSCInputBXShift = cms.int32(-8),
    DTEnable = cms.bool(False),
    DTPhiInput = cms.InputTag("simTwinMuxDigis"),
    DTThetaInput = cms.InputTag("simDtTriggerPrimitiveDigis"),
    Era = cms.string('Run3_2021'),
    FWConfig = cms.bool(True),
    GEMEnable = cms.bool(False),
    GEMInput = cms.InputTag("simMuonGEMPadDigiClusters"),
    GEMInputBXShift = cms.int32(0),
    IRPCEnable = cms.bool(False),
    ME0Enable = cms.bool(False),
    ME0Input = cms.InputTag("me0TriggerConvertedPseudoDigis"),
    ME0InputBXShift = cms.int32(-8),
    MaxBX = cms.int32(3),
    MinBX = cms.int32(-3),
    RPCEnable = cms.bool(True),
    RPCInput = cms.InputTag("unpackRPC"),
    RPCInputBXShift = cms.int32(0),
    UseRun3CCLUT_OTMB = cms.bool(True),
    UseRun3CCLUT_TMB = cms.bool(False),
    spGCParams16 = cms.PSet(
        BugSameSectorPt0 = cms.bool(False),
        MaxRoadsPerZone = cms.int32(3),
        MaxTracks = cms.int32(3),
        UseSecondEarliest = cms.bool(True)
    ),
    spPAParams16 = cms.PSet(
        Bug9BitDPhi = cms.bool(False),
        BugGMTPhi = cms.bool(False),
        BugMode7CLCT = cms.bool(False),
        BugNegPt = cms.bool(False),
        FixMode15HighPt = cms.bool(True),
        ModeQualVer = cms.int32(2),
        PromoteMode7 = cms.bool(False),
        ProtobufFileName = cms.string('model_graph.displ.10.1.pb'),
        ReadPtLUTFile = cms.bool(False)
    ),
    spPCParams16 = cms.PSet(
        DuplicateTheta = cms.bool(True),
        FixME11Edges = cms.bool(True),
        FixZonePhi = cms.bool(True),
        IncludeNeighbor = cms.bool(True),
        UseNewZones = cms.bool(False),
        ZoneBoundaries = cms.vint32(0, 41, 49, 87, 127),
        ZoneOverlap = cms.int32(2)
    ),
    spPRParams16 = cms.PSet(
        PatternDefinitions = cms.vstring(
            '4,15:15,7:7,7:7,7:7',
            '3,16:16,7:7,7:6,7:6',
            '3,14:14,7:7,8:7,8:7',
            '2,18:17,7:7,7:5,7:5',
            '2,13:12,7:7,10:7,10:7',
            '1,22:19,7:7,7:0,7:0',
            '1,11:8,7:7,14:7,14:7',
            '0,30:23,7:7,7:0,7:0',
            '0,7:0,7:7,14:7,14:7'
        ),
        SymPatternDefinitions = cms.vstring(
            '4,15:15:15:15,7:7:7:7,7:7:7:7,7:7:7:7',
            '3,16:16:14:14,7:7:7:7,8:7:7:6,8:7:7:6',
            '2,18:17:13:12,7:7:7:7,10:7:7:4,10:7:7:4',
            '1,22:19:11:8,7:7:7:7,14:7:7:0,14:7:7:0',
            '0,30:23:7:0,7:7:7:7,14:7:7:0,14:7:7:0'
        ),
        UseSymmetricalPatterns = cms.bool(True)
    ),
    spTBParams16 = cms.PSet(
        BugAmbigThetaWin = cms.bool(False),
        BugME11Dupes = cms.bool(False),
        BugSt2PhDiff = cms.bool(False),
        ThetaWindow = cms.int32(8),
        ThetaWindowZone0 = cms.int32(4),
        TwoStationSameBX = cms.bool(True),
        UseSingleHits = cms.bool(False)
    ),
    verbosity = cms.untracked.int32(0)
)


process.simEmtfShowers = cms.EDProducer("L1TMuonEndCapShowerProducer",
    CSCShowerInput = cms.InputTag("simCscTriggerPrimitiveDigis"),
    enableOneLooseShower = cms.bool(True),
    enableOneNominalShower = cms.bool(True),
    enableOneTightShower = cms.bool(True),
    enableTwoLooseShowers = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
)


process.simGmtCaloSumDigis = cms.EDProducer("L1TMuonCaloSumProducer",
    caloStage2Layer2Label = cms.InputTag("simCaloStage2Layer1Digis")
)


process.simGmtShowerDigis = cms.EDProducer("L1TMuonShowerProducer",
    bxMax = cms.int32(0),
    bxMin = cms.int32(0),
    mightGet = cms.optional.untracked.vstring,
    showerInput = cms.InputTag("simEmtfShowers","EMTF")
)


process.simGmtStage2Digis = cms.EDProducer("L1TMuonProducer",
    autoBxRange = cms.bool(True),
    autoCancelMode = cms.bool(False),
    barrelTFInput = cms.InputTag("simKBmtfDigis","BMTF"),
    bmtfCancelMode = cms.string('kftracks'),
    bxMax = cms.int32(2),
    bxMin = cms.int32(-2),
    emtfCancelMode = cms.string('coordinate'),
    forwardTFInput = cms.InputTag("simEmtfDigis","EMTF"),
    overlapTFInput = cms.InputTag("simOmtfDigis","OMTF"),
    triggerTowerInput = cms.InputTag("simGmtCaloSumDigis","TriggerTowerSums")
)


process.simGtExtFakeStage2Digis = cms.EDProducer("L1TExtCondProducer",
    bxFirst = cms.int32(-2),
    bxLast = cms.int32(2),
    setBptxAND = cms.bool(True),
    setBptxMinus = cms.bool(True),
    setBptxOR = cms.bool(True),
    setBptxPlus = cms.bool(True),
    tcdsRecordLabel = cms.InputTag("")
)


process.simGtStage2Digis = cms.EDProducer("L1TGlobalProducer",
    AlgoBlkInputTag = cms.InputTag("gtStage2Digis"),
    AlgorithmTriggersUnmasked = cms.bool(True),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    EGammaInputTag = cms.InputTag("simCaloStage2Digis"),
    EtSumInputTag = cms.InputTag("simCaloStage2Digis"),
    ExtInputTag = cms.InputTag("simGtExtFakeStage2Digis"),
    GetPrescaleColumnFromData = cms.bool(False),
    JetInputTag = cms.InputTag("simCaloStage2Digis"),
    MuonInputTag = cms.InputTag("simGmtStage2Digis"),
    MuonShowerInputTag = cms.InputTag("simGmtShowerDigis"),
    RequireMenuToMatchAlgoBlkInput = cms.bool(False),
    TauInputTag = cms.InputTag("simCaloStage2Digis"),
    useMuonShowers = cms.bool(True)
)


process.simHcalTriggerPrimitiveDigis = cms.EDProducer("HcalTrigPrimDigiProducer",
    FG_HF_thresholds = cms.vuint32(17, 255),
    FG_threshold = cms.uint32(12),
    FrontEndFormatError = cms.bool(False),
    InputTagFEDRaw = cms.InputTag("rawDataCollector"),
    LSConfig = cms.untracked.PSet(
        HcalFeatureHFEMBit = cms.bool(False),
        Long_Short_Offset = cms.double(10.1),
        Long_vrs_Short_Slope = cms.double(100.2),
        Min_Long_Energy = cms.double(10),
        Min_Short_Energy = cms.double(10)
    ),
    MinSignalThreshold = cms.uint32(0),
    PMTNoiseThreshold = cms.uint32(0),
    PeakFinderAlgorithm = cms.int32(2),
    RunZS = cms.bool(False),
    ZS_threshold = cms.uint32(1),
    applySaturationFix = cms.bool(True),
    inputLabel = cms.VInputTag("unpackHcal", "unpackHcal"),
    inputUpgradeLabel = cms.VInputTag("unpackHcal", "unpackHcal"),
    latency = cms.int32(1),
    numberOfFilterPresamplesHBQIE11 = cms.int32(0),
    numberOfFilterPresamplesHEQIE11 = cms.int32(0),
    numberOfPresamples = cms.int32(2),
    numberOfPresamplesHF = cms.int32(1),
    numberOfSamples = cms.int32(4),
    numberOfSamplesHF = cms.int32(2),
    overrideDBweightsAndFilterHB = cms.bool(False),
    overrideDBweightsAndFilterHE = cms.bool(False),
    peakFilter = cms.bool(True),
    tpScales = cms.PSet(
        HBHE = cms.PSet(
            LSBQIE11 = cms.double(0.0625),
            LSBQIE11Overlap = cms.double(0.0625),
            LSBQIE8 = cms.double(0.125)
        ),
        HF = cms.PSet(
            NCTShift = cms.int32(2),
            RCTShift = cms.int32(3)
        )
    ),
    upgradeHB = cms.bool(True),
    upgradeHE = cms.bool(True),
    upgradeHF = cms.bool(True),
    useTDCInMinBiasBits = cms.bool(False),
    weights = cms.vdouble(1.0, 1.0),
    weightsQIE11 = cms.PSet(
        ieta1 = cms.vint32(255, 255),
        ieta10 = cms.vint32(255, 255),
        ieta11 = cms.vint32(255, 255),
        ieta12 = cms.vint32(255, 255),
        ieta13 = cms.vint32(255, 255),
        ieta14 = cms.vint32(255, 255),
        ieta15 = cms.vint32(255, 255),
        ieta16 = cms.vint32(255, 255),
        ieta17 = cms.vint32(255, 255),
        ieta18 = cms.vint32(255, 255),
        ieta19 = cms.vint32(255, 255),
        ieta2 = cms.vint32(255, 255),
        ieta20 = cms.vint32(255, 255),
        ieta21 = cms.vint32(255, 255),
        ieta22 = cms.vint32(255, 255),
        ieta23 = cms.vint32(255, 255),
        ieta24 = cms.vint32(255, 255),
        ieta25 = cms.vint32(255, 255),
        ieta26 = cms.vint32(255, 255),
        ieta27 = cms.vint32(255, 255),
        ieta28 = cms.vint32(255, 255),
        ieta3 = cms.vint32(255, 255),
        ieta4 = cms.vint32(255, 255),
        ieta5 = cms.vint32(255, 255),
        ieta6 = cms.vint32(255, 255),
        ieta7 = cms.vint32(255, 255),
        ieta8 = cms.vint32(255, 255),
        ieta9 = cms.vint32(255, 255)
    )
)


process.simKBmtfDigis = cms.EDProducer("L1TMuonBarrelKalmanTrackProducer",
    algoSettings = cms.PSet(
        aPhi = cms.vdouble(1.942, 0.01511, 0.01476, 0.009799),
        aPhiB = cms.vdouble(-1.508, -0.1237, -0.1496, -0.1333),
        aPhiBNLO = cms.vdouble(0.000331, 0, 0, 0),
        bPhi = cms.vdouble(-1, 0.18245, 0.20898, 0.17286),
        bPhiB = cms.vdouble(-1, 1.18245, 1.20898, 1.17286),
        chiSquare = cms.vdouble(0.0, 0.109375, 0.234375, 0.359375),
        chiSquareCut = cms.vint32(126, 126, 126, 126, 126),
        chiSquareCutCurvMax = cms.vint32(2500, 2500, 2500, 2500, 2500),
        chiSquareCutPattern = cms.vint32(7, 11, 13, 14, 15),
        chiSquareCutTight = cms.vint32(
            40, 126, 60, 126, 126,
            126
        ),
        combos1 = cms.vint32(),
        combos2 = cms.vint32(3),
        combos3 = cms.vint32(5, 6, 7),
        combos4 = cms.vint32(
            9, 10, 11, 12, 13,
            14, 15
        ),
        eLoss = cms.vdouble(0.000765, 0, 0, 0),
        etaLUT0 = cms.vdouble(8.946, 7.508, 6.279, 6.399),
        etaLUT1 = cms.vdouble(0.159, 0.116, 0.088, 0.128),
        initialK = cms.vdouble(-1.196, -1.581, -2.133, -2.263),
        initialK2 = cms.vdouble(-0.000326, -0.0007165, 0.002305, -0.00563),
        lutFile = cms.string('L1Trigger/L1TMuon/data/bmtf_luts/kalmanLUTs_v302.root'),
        mScatteringPhi = cms.vdouble(0.00249, 5.47e-05, 3.49e-05, 1.37e-05),
        mScatteringPhiB = cms.vdouble(0.00722, 0.003461, 0.004447, 0.00412),
        phiAt2 = cms.double(0.15918),
        pointResolutionPhi = cms.double(1.0),
        pointResolutionPhiB = cms.double(500.0),
        pointResolutionPhiBH = cms.vdouble(151.0, 173.0, 155.0, 153.0),
        pointResolutionPhiBL = cms.vdouble(17866.0, 19306.0, 23984.0, 23746.0),
        pointResolutionVertex = cms.double(1.0),
        trackComp = cms.vdouble(1.75, 1.25, 0.625, 0.25),
        trackCompCut = cms.vint32(
            15, 15, 15, 15, 15,
            15
        ),
        trackCompCutCurvMax = cms.vint32(
            34, 34, 34, 34, 34,
            34
        ),
        trackCompCutPattern = cms.vint32(
            3, 5, 6, 9, 10,
            12
        ),
        trackCompErr1 = cms.vdouble(2.0, 2.0, 2.0, 2.0),
        trackCompErr2 = cms.vdouble(0.21875, 0.21875, 0.21875, 0.3125),
        useOfflineAlgo = cms.bool(False),
        verbose = cms.bool(False)
    ),
    bx = cms.vint32(-2, -1, 0, 1, 2),
    src = cms.InputTag("simKBmtfStubs"),
    trackFinderSettings = cms.PSet(
        sectorSettings = cms.PSet(
            regionSettings = cms.PSet(
                verbose = cms.int32(0)
            ),
            verbose = cms.int32(0),
            wheelsToProcess = cms.vint32(-2, -1, 0, 1, 2)
        ),
        sectorsToProcess = cms.vint32(
            0, 1, 2, 3, 4,
            5, 6, 7, 8, 9,
            10, 11
        ),
        verbose = cms.int32(0)
    )
)


process.simKBmtfStubs = cms.EDProducer("L1TMuonBarrelKalmanStubProducer",
    cotTheta_1 = cms.vint32(
        105, 101, 97, 93, 88,
        84, 79, 69, 64, 58,
        52, 46, 40, 34, 21,
        14, 7, 0, -7, -14,
        -21, -34, -40, -46, -52,
        -58, -64, -69, -79, -84,
        -88, -93, -97, -101, -105
    ),
    cotTheta_2 = cms.vint32(
        93, 89, 85, 81, 77,
        73, 68, 60, 55, 50,
        45, 40, 34, 29, 17,
        12, 6, 0, -6, -12,
        -17, -29, -34, -40, -45,
        -50, -55, -60, -68, -73,
        -77, -81, -85, -89, -93
    ),
    cotTheta_3 = cms.vint32(
        81, 77, 74, 70, 66,
        62, 58, 51, 46, 42,
        38, 33, 29, 24, 15,
        10, 5, 0, -5, -10,
        -15, -24, -29, -33, -38,
        -42, -46, -51, -58, -62,
        -66, -70, -74, -77, -81
    ),
    disableMasks = cms.bool(False),
    maxBX = cms.int32(2),
    minBX = cms.int32(-2),
    minPhiQuality = cms.int32(0),
    minThetaQuality = cms.int32(0),
    srcPhi = cms.InputTag("simTwinMuxDigis"),
    srcTheta = cms.InputTag("simDtTriggerPrimitiveDigis"),
    verbose = cms.int32(0)
)


process.simMuonGEMPadDigiClusters = cms.EDProducer("GEMPadDigiClusterProducer",
    InputCollection = cms.InputTag("simMuonGEMPadDigis"),
    maxClusterSize = cms.uint32(8),
    maxClustersOHGE11 = cms.uint32(8),
    maxClustersOHGE21 = cms.uint32(8),
    maxClustersPartitionGE11 = cms.uint32(4),
    maxClustersPartitionGE21 = cms.uint32(4),
    mightGet = cms.optional.untracked.vstring,
    nOHGE11 = cms.uint32(1),
    nOHGE21 = cms.uint32(4),
    nPartitionsGE11 = cms.uint32(4),
    nPartitionsGE21 = cms.uint32(4),
    sendOverflowClusters = cms.bool(False)
)


process.simMuonGEMPadDigis = cms.EDProducer("GEMPadDigiProducer",
    InputCollection = cms.InputTag("unpackGEM"),
    mightGet = cms.optional.untracked.vstring
)


process.simOmtfDigis = cms.EDProducer("L1TMuonOverlapPhase1TrackProducer",
    XMLDumpFileName = cms.string('TestEvents.xml'),
    bxMax = cms.int32(0),
    bxMin = cms.int32(0),
    dropCSCPrimitives = cms.bool(False),
    dropDTPrimitives = cms.bool(False),
    dropRPCPrimitives = cms.bool(False),
    dumpDetailedResultToXML = cms.bool(False),
    dumpGPToXML = cms.bool(False),
    dumpResultToXML = cms.bool(False),
    eventsXMLFiles = cms.vstring('TestEvents.xml'),
    processorType = cms.string('OMTFProcessor'),
    readEventsFromXML = cms.bool(False),
    srcCSC = cms.InputTag("simCscTriggerPrimitiveDigis","MPCSORTED"),
    srcDTPh = cms.InputTag("simDtTriggerPrimitiveDigis"),
    srcDTTh = cms.InputTag("simDtTriggerPrimitiveDigis"),
    srcRPC = cms.InputTag("unpackRPC")
)


process.simTwinMuxDigis = cms.EDProducer("L1TTwinMuxProducer",
    DTDigi_Source = cms.InputTag("simDtTriggerPrimitiveDigis"),
    DTThetaDigi_Source = cms.InputTag("simDtTriggerPrimitiveDigis"),
    RPC_Source = cms.InputTag("unpackRPC")
)


process.unpackCSC = cms.EDProducer("CSCDCCUnpacker",
    B904Setup = cms.untracked.bool(False),
    B904dmb = cms.untracked.int32(3),
    B904vmecrate = cms.untracked.int32(1),
    Debug = cms.untracked.bool(False),
    DisableMappingCheck = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535558134),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    runDQM = cms.untracked.bool(False),
    useCSCShowers = cms.bool(True),
    useGEMs = cms.bool(True),
    useRPCs = cms.bool(False)
)


process.unpackDT = cms.EDProducer("DTuROSRawToDigi",
    debug = cms.untracked.bool(False),
    inputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess")
)


process.unpackEcal = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28, 29, 30,
        31, 32, 33, 34, 35,
        36, 37, 38, 39, 40,
        41, 42, 43, 44, 45,
        46, 47, 48, 49, 50,
        51, 52, 53, 54
    ),
    orderedFedList = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.unpackGEM = cms.EDProducer("GEMRawToDigiModule",
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    fedIdEnd = cms.uint32(1478),
    fedIdStart = cms.uint32(1467),
    ge21Off = cms.bool(False),
    keepDAQStatus = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    readMultiBX = cms.bool(False),
    useDBEMap = cms.bool(True)
)


process.unpackHcal = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(True),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    mightGet = cms.optional.untracked.vstring,
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    silent = cms.untracked.bool(True)
)


process.unpackRPC = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector","","@skipCurrentProcess"),
    doSynchro = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
)


process.hltEcalDigis = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltEcalDigisLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('EBDigiCollection')
            ),
            cms.PSet(
                type = cms.string('EEDigiCollection')
            ),
            cms.PSet(
                type = cms.string('EBDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EEDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EBSrFlagsSorted')
            ),
            cms.PSet(
                type = cms.string('EESrFlagsSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityBlockSizeErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityTTIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityZSXtalIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EcalPnDiodeDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalPseudoStripInputs'),
                type = cms.string('EcalPseudoStripInputDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalTriggerPrimitives'),
                type = cms.string('EcalTriggerPrimitiveDigisSorted')
            )
        )
    ),
    cuda = cms.EDAlias(
        hltEcalDigisFromGPU = cms.VPSet(
            cms.PSet(
                type = cms.string('EBDigiCollection')
            ),
            cms.PSet(
                type = cms.string('EEDigiCollection')
            )
        ),
        hltEcalDigisLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('EBDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EEDetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EBSrFlagsSorted')
            ),
            cms.PSet(
                type = cms.string('EESrFlagsSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityBlockSizeErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityTTIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalIntegrityZSXtalIdErrors'),
                type = cms.string('EcalElectronicsIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('EcalPnDiodeDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalPseudoStripInputs'),
                type = cms.string('EcalPseudoStripInputDigisSorted')
            ),
            cms.PSet(
                fromProductInstance = cms.string('EcalTriggerPrimitives'),
                type = cms.string('EcalTriggerPrimitiveDigisSorted')
            )
        )
    )
)


process.hltEcalUncalibRecHit = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltEcalUncalibRecHitLegacy = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    ),
    cuda = cms.EDAlias(
        hltEcalUncalibRecHitFromSoA = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltHbhereco = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltHbherecoLegacy = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    ),
    cuda = cms.EDAlias(
        hltHbherecoFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('HBHERecHitsSorted')
        ))
    )
)


process.hltPixelTracksSoA = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltPixelTracksCPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    ),
    cuda = cms.EDAlias(
        hltPixelTracksFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltPixelVerticesSoA = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltPixelVerticesCPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    ),
    cuda = cms.EDAlias(
        hltPixelVerticesFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltSiPixelClusters = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelClustersLegacy = cms.VPSet(cms.PSet(
            type = cms.string('SiPixelClusteredmNewDetSetVector')
        ))
    ),
    cuda = cms.EDAlias(
        hltSiPixelClustersFromSoA = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltSiPixelDigis = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelDigisLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('DetIdedmEDCollection')
            ),
            cms.PSet(
                type = cms.string('SiPixelRawDataErroredmDetSetVector')
            ),
            cms.PSet(
                type = cms.string('PixelFEDChanneledmNewDetSetVector')
            )
        )
    ),
    cuda = cms.EDAlias(
        hltSiPixelDigisFromSoA = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltSiPixelRecHits = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelRecHitsFromLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('SiPixelRecHitedmNewDetSetVector')
            ),
            cms.PSet(
                type = cms.string('uintAsHostProduct')
            )
        )
    ),
    cuda = cms.EDAlias(
        hltSiPixelRecHitsFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltSiPixelRecHitsSoA = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelRecHitsFromLegacy = cms.VPSet(
            cms.PSet(
                type = cms.string('pixelTopologyPhase1TrackingRecHitSoAHost')
            ),
            cms.PSet(
                type = cms.string('uintAsHostProduct')
            )
        )
    ),
    cuda = cms.EDAlias(
        hltSiPixelRecHitsSoAFromGPU = cms.VPSet(cms.PSet(
            type = cms.string('*')
        ))
    )
)


process.hltBoolEnd = cms.EDFilter("HLTBool",
    result = cms.bool(True)
)


process.hltBoolFalse = cms.EDFilter("HLTBool",
    result = cms.bool(False)
)


process.hltDiEG33CaloIdLClusterShapeUnseededFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltDiEG33HEUnseededFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.014),
    thrRegularEE = cms.vdouble(0.035),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShapeUnseeded","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltDiEG33EtUnseededFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(33.0),
    etcutEE = cms.double(33.0),
    inputTag = cms.InputTag("hltEgammaCandidatesWrapperUnseeded"),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(2),
    saveTags = cms.bool(True)
)


process.hltDiEG33HEUnseededFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltDiEG33EtUnseededFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.15),
    thrOverEEE = cms.vdouble(0.1),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverEUnseeded")
)


process.hltDiEle33CaloIdLMWPMS2UnseededFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltDiEle33CaloIdLPixelMatchUnseededFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(150.0),
    thrRegularEE = cms.vdouble(150.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaPixelMatchVarsUnseeded","s2")
)


process.hltDiEle33CaloIdLPixelMatchUnseededFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltDiEG33CaloIdLClusterShapeUnseededFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeedsUnseeded"),
    ncandcut = cms.int32(2),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEG115CaloIdVTClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG115EtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.011),
    thrRegularEE = cms.vdouble(0.03),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEG115CaloIdVTHEFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG115CaloIdVTClusterShapeFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.075),
    thrOverEEE = cms.vdouble(0.075),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEG115EtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(115.0),
    etcutEE = cms.double(115.0),
    inputTag = cms.InputTag("hltEGL1SingleEGNonIsoOrWithJetAndTauFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG135CaloIdVTClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG135EtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.011),
    thrRegularEE = cms.vdouble(0.03),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEG135CaloIdVTHEFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG135CaloIdVTClusterShapeFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.075),
    thrOverEEE = cms.vdouble(0.075),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEG135EtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(135.0),
    etcutEE = cms.double(135.0),
    inputTag = cms.InputTag("hltEGL1SingleEGNonIsoOrWithJetAndTauFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG30L1SingleEGOrEtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(30.0),
    etcutEE = cms.double(30.0),
    inputTag = cms.InputTag("hltEGL1SingleEGOrFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG32L1SingleEGOrEtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(32.0),
    etcutEE = cms.double(32.0),
    inputTag = cms.InputTag("hltEGL1SingleEGOrFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG33CaloIdLClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG33HEFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.014),
    thrRegularEE = cms.vdouble(0.035),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEG33EtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(33.0),
    etcutEE = cms.double(33.0),
    inputTag = cms.InputTag("hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG33HEFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG33EtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.15),
    thrOverEEE = cms.vdouble(0.1),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter = cms.EDFilter("HLTEgammaL1TMatchFilterRegional",
    L1SeedFilterTag = cms.InputTag("hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau"),
    barrel_end = cms.double(1.4791),
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(False),
    endcap_end = cms.double(2.65),
    l1CenJetsTag = cms.InputTag("hltGtStage2Digis","Jet"),
    l1IsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1NonIsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1TausTag = cms.InputTag("hltGtStage2Digis","Tau"),
    ncandcut = cms.int32(1),
    region_eta_size = cms.double(0.522),
    region_eta_size_ecap = cms.double(1.0),
    region_phi_size = cms.double(1.044),
    saveTags = cms.bool(True)
)


process.hltEGL1SingleAndDoubleEGOrPairFilter = cms.EDFilter("HLTEgammaL1TMatchFilterRegional",
    L1SeedFilterTag = cms.InputTag("hltL1sSingleAndDoubleEG"),
    barrel_end = cms.double(1.4791),
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(False),
    endcap_end = cms.double(2.65),
    l1CenJetsTag = cms.InputTag("hltGtStage2Digis","Jet"),
    l1IsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1NonIsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1TausTag = cms.InputTag("hltGtStage2Digis","Tau"),
    ncandcut = cms.int32(2),
    region_eta_size = cms.double(0.522),
    region_eta_size_ecap = cms.double(1.0),
    region_phi_size = cms.double(1.044),
    saveTags = cms.bool(True)
)


process.hltEGL1SingleEGNonIsoOrWithJetAndTauFilter = cms.EDFilter("HLTEgammaL1TMatchFilterRegional",
    L1SeedFilterTag = cms.InputTag("hltL1sSingleEGNonIsoOrWithJetAndTau"),
    barrel_end = cms.double(1.4791),
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(False),
    endcap_end = cms.double(2.65),
    l1CenJetsTag = cms.InputTag("hltGtStage2Digis","Jet"),
    l1IsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1NonIsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1TausTag = cms.InputTag("hltGtStage2Digis","Tau"),
    ncandcut = cms.int32(1),
    region_eta_size = cms.double(0.522),
    region_eta_size_ecap = cms.double(1.0),
    region_phi_size = cms.double(1.044),
    saveTags = cms.bool(True)
)


process.hltEGL1SingleEGOrFilter = cms.EDFilter("HLTEgammaL1TMatchFilterRegional",
    L1SeedFilterTag = cms.InputTag("hltL1sSingleEGor"),
    barrel_end = cms.double(1.4791),
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(False),
    endcap_end = cms.double(2.65),
    l1CenJetsTag = cms.InputTag("hltGtStage2Digis","Jet"),
    l1IsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1NonIsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1TausTag = cms.InputTag("hltGtStage2Digis","Tau"),
    ncandcut = cms.int32(1),
    region_eta_size = cms.double(0.522),
    region_eta_size_ecap = cms.double(1.0),
    region_phi_size = cms.double(1.044),
    saveTags = cms.bool(True)
)


process.hltEgammaCandidatesWrapperUnseeded = cms.EDFilter("HLTEgammaTriggerFilterObjectWrapper",
    candIsolatedTag = cms.InputTag("hltEgammaCandidatesUnseeded"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(True),
    saveTags = cms.bool(True)
)


process.hltEle115CaloIdVTGsfTrkIdTGsfDetaFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle115CaloIdVTPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.007),
    thrRegularEE = cms.vdouble(0.007),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle115CaloIdVTGsfTrkIdTGsfDphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle115CaloIdVTGsfTrkIdTGsfDetaFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.07),
    thrRegularEE = cms.vdouble(0.07),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle115CaloIdVTPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEG115CaloIdVTHEFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle135CaloIdVTGsfTrkIdTGsfDetaFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle135CaloIdVTPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.007),
    thrRegularEE = cms.vdouble(0.007),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle135CaloIdVTGsfTrkIdTGsfDphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle135CaloIdVTGsfTrkIdTGsfDetaFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.07),
    thrRegularEE = cms.vdouble(0.07),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle135CaloIdVTPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEG135CaloIdVTHEFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.013),
    thrRegularEE = cms.vdouble(0.035),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.013),
    thrRegularEE = cms.vdouble(0.035),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.01),
    thrRegularEE = cms.vdouble(0.015),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.01),
    thrRegularEE = cms.vdouble(0.015),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.07),
    thrRegularEE = cms.vdouble(0.1),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.07),
    thrRegularEE = cms.vdouble(0.1),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.29, 0.21),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.5),
    thrOverEEE = cms.vdouble(0.5),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.29, 0.21),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.5),
    thrOverEEE = cms.vdouble(0.5),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(23.0),
    etcutEE = cms.double(23.0),
    inputTag = cms.InputTag("hltEGL1SingleAndDoubleEGOrPairFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(12.0),
    etcutEE = cms.double(12.0),
    inputTag = cms.InputTag("hltEGL1SingleAndDoubleEGOrPairFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(2),
    saveTags = cms.bool(True)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.13),
    thrOverEEE = cms.vdouble(0.13),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.13),
    thrOverEEE = cms.vdouble(0.13),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.25),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.3),
    thrOverEEE = cms.vdouble(0.3),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.25),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.3),
    thrOverEEE = cms.vdouble(0.3),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(999999.0),
    thrRegularEE = cms.vdouble(999999.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(999999.0),
    thrRegularEE = cms.vdouble(999999.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(2),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.2),
    thrOverEEE = cms.vdouble(0.2),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.2),
    thrOverEEE = cms.vdouble(0.2),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
)


process.hltEle30WPTightClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG30L1SingleEGOrEtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.011),
    thrRegularEE = cms.vdouble(0.0305),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEle30WPTightEcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle30WPTightHEFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.2, 0.25, 0.3),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(1.75),
    thrRegularEB2 = cms.vdouble(1.75),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIso")
)


process.hltEle30WPTightGsfDetaFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightGsfMissingHitsFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.004),
    thrRegularEE = cms.vdouble(0.005),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle30WPTightGsfDphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightGsfDetaFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.02),
    thrRegularEE = cms.vdouble(0.023),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle30WPTightGsfMissingHitsFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightGsfOneOEMinusOneOPFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(999.0),
    thrRegularEE = cms.vdouble(1.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","MissingHits")
)


process.hltEle30WPTightGsfOneOEMinusOneOPFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightPMS2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.012),
    thrRegularEE = cms.vdouble(0.011),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP")
)


process.hltEle30WPTightGsfTrackIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle30WPTightGsfDphiFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.029, 0.111, 0.114, 0.032),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(0.838),
    thrRegularEB2 = cms.vdouble(-0.385),
    thrRegularEE1 = cms.vdouble(-0.363),
    thrRegularEE2 = cms.vdouble(0.702),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
)


process.hltEle30WPTightHEFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle30WPTightClusterShapeFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.1, 0.1, 0.3, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(0.75),
    thrRegularEB2 = cms.vdouble(2.25),
    thrRegularEE1 = cms.vdouble(3.0),
    thrRegularEE2 = cms.vdouble(5.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEle30WPTightHcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.0),
    candTag = cms.InputTag("hltEle30WPTightEcalIsoFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.2, 0.4, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(2.5),
    thrRegularEB2 = cms.vdouble(3.0),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
)


process.hltEle30WPTightPMS2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(70.0),
    thrRegularEE = cms.vdouble(45.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaPixelMatchVars","s2")
)


process.hltEle30WPTightPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEle30WPTightHcalIsoFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle32WPTightClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG32L1SingleEGOrEtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.011),
    thrRegularEE = cms.vdouble(0.0305),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEle32WPTightEcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle32WPTightHEFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.2, 0.25, 0.3),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(1.75),
    thrRegularEB2 = cms.vdouble(1.75),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIso")
)


process.hltEle32WPTightGsfDetaFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightGsfMissingHitsFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.004),
    thrRegularEE = cms.vdouble(0.005),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle32WPTightGsfDphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightGsfDetaFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.02),
    thrRegularEE = cms.vdouble(0.023),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle32WPTightGsfMissingHitsFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightGsfOneOEMinusOneOPFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(999.0),
    thrRegularEE = cms.vdouble(1.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","MissingHits")
)


process.hltEle32WPTightGsfOneOEMinusOneOPFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightPMS2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.012),
    thrRegularEE = cms.vdouble(0.011),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP")
)


process.hltEle32WPTightGsfTrackIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle32WPTightGsfDphiFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.029, 0.111, 0.114, 0.032),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(0.838),
    thrRegularEB2 = cms.vdouble(-0.385),
    thrRegularEE1 = cms.vdouble(-0.363),
    thrRegularEE2 = cms.vdouble(0.702),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
)


process.hltEle32WPTightHEFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle32WPTightClusterShapeFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.1, 0.1, 0.3, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(0.75),
    thrRegularEB2 = cms.vdouble(2.25),
    thrRegularEE1 = cms.vdouble(3.0),
    thrRegularEE2 = cms.vdouble(5.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEle32WPTightHcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.0),
    candTag = cms.InputTag("hltEle32WPTightEcalIsoFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.2, 0.4, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.03),
    thrOverEEB2 = cms.vdouble(0.03),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(2.5),
    thrRegularEB2 = cms.vdouble(3.0),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
)


process.hltEle32WPTightPMS2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(70.0),
    thrRegularEE = cms.vdouble(45.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaPixelMatchVars","s2")
)


process.hltEle32WPTightPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEle32WPTightHcalIsoFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle33CaloIdLMWPMS2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle33CaloIdLPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(150.0),
    thrRegularEE = cms.vdouble(150.0),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaPixelMatchVars","s2")
)


process.hltEle33CaloIdLPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEG33CaloIdLClusterShapeFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltL1sSingleAndDoubleEG = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleLooseIsoEG26er2p5 OR L1_SingleLooseIsoEG26er1p5 OR L1_SingleLooseIsoEG28er2p5 OR L1_SingleLooseIsoEG28er2p1 OR L1_SingleLooseIsoEG28er1p5 OR L1_SingleLooseIsoEG30er2p5 OR L1_SingleLooseIsoEG30er1p5 OR L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleIsoEG24er2p1 OR L1_SingleIsoEG26er2p1 OR L1_SingleIsoEG28er2p1 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG26er2p5 OR L1_SingleIsoEG28er2p5 OR L1_SingleIsoEG30er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5 OR L1_DoubleEG_22_10_er2p5 OR L1_DoubleEG_25_12_er2p5 OR L1_DoubleEG_25_14_er2p5 OR L1_DoubleEG_LooseIso22_12_er2p5'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleEG26er2p5 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_DoubleEG_22_10_er2p5 OR L1_DoubleEG_25_12_er2p5 OR L1_DoubleEG_25_14_er2p5 OR L1_SingleJet160er2p5 OR L1_SingleJet180 OR L1_SingleJet200 OR L1_SingleTau120er2p1 OR L1_SingleTau130er2p1'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltL1sSingleEGNonIsoOrWithJetAndTau = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleJet160er2p5 OR L1_SingleJet180 OR L1_SingleJet200 OR L1_SingleTau120er2p1 OR L1_SingleTau130er2p1 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltL1sSingleEGor = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleLooseIsoEG26er2p5 OR L1_SingleLooseIsoEG26er1p5 OR L1_SingleLooseIsoEG28er2p5 OR L1_SingleLooseIsoEG28er2p1 OR L1_SingleLooseIsoEG28er1p5 OR L1_SingleLooseIsoEG30er2p5 OR L1_SingleLooseIsoEG30er1p5 OR L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleIsoEG24er2p1 OR L1_SingleIsoEG26er2p1 OR L1_SingleIsoEG28er2p1 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG26er2p5 OR L1_SingleIsoEG28er2p5 OR L1_SingleIsoEG30er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltPreDoubleEle33CaloIdLMW = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle115CaloIdVTGsfTrkIdT = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle135CaloIdVTGsfTrkIdT = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle23Ele12CaloIdLTrackIdLIsoVL = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle30WPTightGsf = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle32WPTightGsf = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltTriggerType = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)


process.hltGetRaw = cms.EDAnalyzer("HLTGetRaw",
    RawDataCollection = cms.InputTag("rawDataCollector")
)


process.hltOutputMinimal = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AOD'),
        filterName = cms.untracked.string('')
    ),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('output.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep GlobalAlgBlkBXVector_*_*_*',
        'keep GlobalExtBlkBXVector_*_*_*',
        'keep l1tEGammaBXVector_*_EGamma_*',
        'keep l1tEtSumBXVector_*_EtSum_*',
        'keep l1tJetBXVector_*_Jet_*',
        'keep l1tMuonBXVector_*_Muon_*',
        'keep l1tTauBXVector_*_Tau_*',
        'keep *_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep recoRecoEcalCandidates*_*_*_*',
        'keep recoSuperClusters_*_*_*',
        'keep recoCaloClusters_*_*_*',
        'keep *_genParticles_*_*',
        'keep *_addPileupInfo_*_*',
        'keep *_externalLHEProducer_*_*',
        'keep *_generator_*_*',
        'keep *_hltEgammaGsfTracks*_*_*',
        'keep recoElectronSeeds_*_*_*',
        'keep *_hltEgammaHLTExtra_*_*',
        'keep *_hltNrInputEvents_*_*',
        'keep *_hltGtStage2Digis_*_*'
    )
)


process.DQMStore = cms.Service("DQMStore",
    MEsToSave = cms.untracked.vstring(
        'Hcal/DigiTask/Occupancy/depth/depth1',
        'Hcal/DigiTask/Occupancy/depth/depth2',
        'Hcal/DigiTask/Occupancy/depth/depth3',
        'Hcal/DigiTask/Occupancy/depth/depth4',
        'Hcal/DigiTask/Occupancy/depth/depth5',
        'Hcal/DigiTask/Occupancy/depth/depth6',
        'Hcal/DigiTask/Occupancy/depth/depth7',
        'Hcal/DigiTask/Occupancy/depth/depthHO',
        'Hcal/DigiTask/OccupancyCut/depth/depth1',
        'Hcal/DigiTask/OccupancyCut/depth/depth2',
        'Hcal/DigiTask/OccupancyCut/depth/depth3',
        'Hcal/DigiTask/OccupancyCut/depth/depth4',
        'Hcal/DigiTask/OccupancyCut/depth/depth5',
        'Hcal/DigiTask/OccupancyCut/depth/depth6',
        'Hcal/DigiTask/OccupancyCut/depth/depth7',
        'Hcal/DigiTask/OccupancyCut/depth/depthHO',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'EcalBarrel/EBOccupancyTask/EBOT DCC entries',
        'EcalEndcap/EEOccupancyTask/EEOT DCC entries',
        'Ecal/EventInfo/processedEvents',
        'PixelPhase1/Tracks/charge_PXBarrel',
        'PixelPhase1/Tracks/charge_PXForward',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
        'HLT/Vertexing/hltPixelVertices/hltPixelVertices/goodvtxNbr',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_pt',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/LUMIanalysis/NumberEventsVsLUMI',
        'HLT/Tracking/tracks/PUmonitoring/NumberEventsVsGoodPVtx',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
        'PixelPhase1/Tracks/clusterposition_zphi_ontrack',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
        'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
        'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
        'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/NormalizedHitResiduals_TOB__Layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/NormalizedHitResiduals_TOB__Layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/NormalizedHitResiduals_TOB__Layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/NormalizedHitResiduals_TOB__Layer__6',
        'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
        'SiStrip/MechanicalView/MainDiagonal Position',
        'SiStrip/MechanicalView/NumberOfClustersInPixel',
        'SiStrip/MechanicalView/NumberOfClustersInStrip',
        'Tracking/TrackParameters/generalTracks/LSanalysis/Chi2oNDF_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfTracks_lumiFlag_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDzToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIP3DToPV_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfMissingOuterRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
        'OfflinePV/offlinePrimaryVertices/tagVtxProb',
        'OfflinePV/offlinePrimaryVertices/tagType',
        'OfflinePV/Resolution/PV/pull_x',
        'OfflinePV/Resolution/PV/pull_y',
        'OfflinePV/Resolution/PV/pull_z',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Constituents',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta_uncor',
        'JetMET/Jet/Cleanedak4PFJetsCHS/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsCHS/NJets',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Pt',
        'JetMET/MET/pfMETT1/Cleaned/METSig',
        'JetMET/vertices'
    ),
    assertLegacySafe = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(True),
    onlineMode = cms.untracked.bool(False),
    saveByLumi = cms.untracked.bool(False),
    trackME = cms.untracked.string(''),
    verbose = cms.untracked.int32(0)
)


process.FastTimerService = cms.Service("FastTimerService",
    dqmLumiSectionsRange = cms.untracked.uint32(2500),
    dqmMemoryRange = cms.untracked.double(1000000.0),
    dqmMemoryResolution = cms.untracked.double(5000.0),
    dqmModuleMemoryRange = cms.untracked.double(100000.0),
    dqmModuleMemoryResolution = cms.untracked.double(500.0),
    dqmModuleTimeRange = cms.untracked.double(40.0),
    dqmModuleTimeResolution = cms.untracked.double(0.2),
    dqmPath = cms.untracked.string('HLT/TimerService'),
    dqmPathMemoryRange = cms.untracked.double(1000000.0),
    dqmPathMemoryResolution = cms.untracked.double(5000.0),
    dqmPathTimeRange = cms.untracked.double(100.0),
    dqmPathTimeResolution = cms.untracked.double(0.5),
    dqmTimeRange = cms.untracked.double(2000.0),
    dqmTimeResolution = cms.untracked.double(5.0),
    enableDQM = cms.untracked.bool(True),
    enableDQMTransitions = cms.untracked.bool(False),
    enableDQMbyLumiSection = cms.untracked.bool(True),
    enableDQMbyModule = cms.untracked.bool(False),
    enableDQMbyPath = cms.untracked.bool(False),
    enableDQMbyProcesses = cms.untracked.bool(True),
    jsonFileName = cms.untracked.string('resources.json'),
    printEventSummary = cms.untracked.bool(False),
    printJobSummary = cms.untracked.bool(True),
    printRunSummary = cms.untracked.bool(True),
    writeJSONSummary = cms.untracked.bool(False)
)


process.MessageLogger = cms.Service("MessageLogger",
    FastReport = cms.untracked.PSet(

    ),
    HLTrigReport = cms.untracked.PSet(

    ),
    L1GtTrigReport = cms.untracked.PSet(

    ),
    L1TGlobalSummary = cms.untracked.PSet(

    ),
    ThroughputService = cms.untracked.PSet(

    ),
    TriggerSummaryProducerAOD = cms.untracked.PSet(

    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enableStatistics = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        threshold = cms.untracked.string('INFO')
    ),
    debugModules = cms.untracked.vstring(),
    suppressDebug = cms.untracked.vstring(),
    suppressError = cms.untracked.vstring(
        'hltL3TkTracksFromL2IOHit',
        'hltL3TkTracksFromL2OIHit',
        'hltL3TkTracksFromL2OIState',
        'hltOnlineBeamSpot'
    ),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(
        'hltL3MuonsIOHit',
        'hltL3MuonsOIHit',
        'hltL3MuonsOIState',
        'hltLightPFTracks',
        'hltOnlineBeamSpot',
        'hltPixelTracks',
        'hltPixelTracksForHighMult',
        'hltSiPixelClusters',
        'hltSiPixelDigis'
    )
)


process.ThroughputService = cms.Service("ThroughputService",
    dqmPath = cms.untracked.string('HLT/Throughput'),
    dqmPathByProcesses = cms.untracked.bool(True),
    enableDQM = cms.untracked.bool(True),
    eventRange = cms.untracked.uint32(10000),
    eventResolution = cms.untracked.uint32(1),
    printEventSummary = cms.untracked.bool(False),
    timeRange = cms.untracked.double(60000.0),
    timeResolution = cms.untracked.double(5.828)
)


process.ProcessAcceleratorCUDA = ProcessAcceleratorCUDA()


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection')
)


process.CSCChannelMapperESProducer = cms.ESProducer("CSCChannelMapperESProducer",
    AlgoName = cms.string('CSCChannelMapperPostls1')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CSCIndexerESProducer = cms.ESProducer("CSCIndexerESProducer",
    AlgoName = cms.string('CSCIndexerPostls1')
)


process.CSCObjectMapESProducer = cms.ESProducer("CSCObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTPGTranscoder = cms.ESProducer("CaloTPGTranscoderULUTs",
    LUTfactor = cms.vint32(1, 2, 5, 0),
    RCTLSB = cms.double(0.25),
    ZS = cms.vint32(4, 2, 1, 0),
    hcalLUT1 = cms.FileInPath('CalibCalorimetry/CaloTPG/data/outputLUTtranscoder_physics.dat'),
    hcalLUT2 = cms.FileInPath('CalibCalorimetry/CaloTPG/data/TPGcalcDecompress2.txt'),
    ietaLowerBound = cms.vint32(1, 18, 27, 29),
    ietaUpperBound = cms.vint32(17, 26, 28, 32),
    linearLUTs = cms.bool(True),
    nominal_gain = cms.double(0.177),
    read_Ascii_Compression_LUTs = cms.bool(False),
    read_Ascii_RCT_LUTs = cms.bool(False),
    tpScales = cms.PSet(
        HBHE = cms.PSet(
            LSBQIE11 = cms.double(0.0625),
            LSBQIE11Overlap = cms.double(0.0625),
            LSBQIE8 = cms.double(0.125)
        ),
        HF = cms.PSet(
            NCTShift = cms.int32(2),
            RCTShift = cms.int32(3)
        )
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapAuto = cms.untracked.bool(False),
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz'),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.DTObjectMapESProducer = cms.ESProducer("DTObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    appendToDataLabel = cms.string(''),
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.GEMGeometryESModule = cms.ESProducer("GEMGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.GlobalParameters = cms.ESProducer("StableParametersTrivialProducer",
    IfCaloEtaNumberBits = cms.uint32(4),
    IfMuEtaNumberBits = cms.uint32(6),
    NumberChips = cms.uint32(1),
    NumberConditionChips = cms.uint32(1),
    NumberL1CenJet = cms.uint32(4),
    NumberL1EGamma = cms.uint32(12),
    NumberL1ForJet = cms.uint32(4),
    NumberL1IsoEG = cms.uint32(4),
    NumberL1Jet = cms.uint32(12),
    NumberL1JetCounts = cms.uint32(12),
    NumberL1Mu = cms.uint32(4),
    NumberL1Muon = cms.uint32(8),
    NumberL1NoIsoEG = cms.uint32(4),
    NumberL1Tau = cms.uint32(12),
    NumberL1TauJet = cms.uint32(4),
    NumberPhysTriggers = cms.uint32(512),
    NumberPhysTriggersExtended = cms.uint32(64),
    NumberPsbBoards = cms.int32(7),
    NumberTechnicalTriggers = cms.uint32(64),
    OrderConditionChip = cms.vint32(1),
    OrderOfChip = cms.vint32(1),
    PinsOnChip = cms.uint32(512),
    PinsOnConditionChip = cms.uint32(512),
    TotalBxInEvent = cms.int32(5),
    UnitLength = cms.int32(8),
    WordLength = cms.int32(64),
    appendToDataLabel = cms.string('')
)


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.HcalTPGCoderULUT = cms.ESProducer("HcalTPGCoderULUT",
    FGLUTs = cms.FileInPath('CalibCalorimetry/HcalTPGAlgos/data/HBHE_FG_LUT.dat'),
    FG_HF_thresholds = cms.vuint32(17, 255),
    LUTGenerationMode = cms.bool(True),
    MaskBit = cms.int32(32768),
    RCalibFile = cms.FileInPath('CalibCalorimetry/HcalTPGAlgos/data/RecHit-TPG-calib.dat'),
    applyFixPCC = cms.bool(True),
    contain1TSHB = cms.bool(False),
    contain1TSHE = cms.bool(False),
    containPhaseNSHB = cms.double(6.0),
    containPhaseNSHE = cms.double(6.0),
    inputLUTs = cms.FileInPath('CalibCalorimetry/HcalTPGAlgos/data/inputLUTcoder_physics.dat'),
    linearLUTs = cms.bool(True),
    overrideDBweightsAndFilterHB = cms.bool(False),
    overrideDBweightsAndFilterHE = cms.bool(False),
    read_Ascii_LUTs = cms.bool(False),
    read_FG_LUTs = cms.bool(False),
    read_XML_LUTs = cms.bool(False),
    tpScales = cms.PSet(
        HBHE = cms.PSet(
            LSBQIE11 = cms.double(0.0625),
            LSBQIE11Overlap = cms.double(0.0625),
            LSBQIE8 = cms.double(0.125)
        ),
        HF = cms.PSet(
            NCTShift = cms.int32(2),
            RCTShift = cms.int32(3)
        )
    )
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
)


process.HcalTrigTowerGeometryESProducer = cms.ESProducer("HcalTrigTowerGeometryESProducer")


process.L1DTConfigFromDB = cms.ESProducer("DTConfigDBProducer",
    DTTPGMap = cms.untracked.PSet(
    **dict(
        [
            ("wh0st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh0st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh0st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh0st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh0st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh0st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh0st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh0st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh0st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh0st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh0st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh0st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh1st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se4" , cms.untracked.vint32(50, 48, 50, 13) ),
            ("wh1st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh1st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se4" , cms.untracked.vint32(60, 48, 60, 15) ),
            ("wh1st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh1st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se4" , cms.untracked.vint32(72, 48, 72, 18) ),
            ("wh1st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh1st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh1st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh1st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh1st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh1st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh1st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh1st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh1st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh1st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh2st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("wh2st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("wh2st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("wh2st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh2st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("wh2st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh2st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh2st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("wh2st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("wh2st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("wh2st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("wh2st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("whm1st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se3" , cms.untracked.vint32(50, 48, 50, 13) ),
            ("whm1st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm1st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se3" , cms.untracked.vint32(60, 48, 60, 15) ),
            ("whm1st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm1st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se3" , cms.untracked.vint32(72, 48, 72, 18) ),
            ("whm1st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm1st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm1st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("whm1st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm1st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm1st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm1st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm1st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm1st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm1st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
        ] +
        [
            ("whm2st1se1" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se10" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se11" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se12" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se2" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se3" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se4" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se5" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se6" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se7" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se8" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st1se9" , cms.untracked.vint32(50, 58, 50, 13) ),
            ("whm2st2se1" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se10" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se11" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se12" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se2" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se3" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se4" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se5" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se6" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se7" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se8" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st2se9" , cms.untracked.vint32(60, 58, 60, 15) ),
            ("whm2st3se1" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se10" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se11" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se12" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se2" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se3" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se4" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se5" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se6" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se7" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se8" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st3se9" , cms.untracked.vint32(72, 58, 72, 18) ),
            ("whm2st4se1" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se10" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm2st4se11" , cms.untracked.vint32(48, 0, 48, 12) ),
            ("whm2st4se12" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm2st4se13" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm2st4se14" , cms.untracked.vint32(60, 0, 60, 15) ),
            ("whm2st4se2" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se3" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se4" , cms.untracked.vint32(72, 0, 72, 18) ),
            ("whm2st4se5" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se6" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se7" , cms.untracked.vint32(96, 0, 96, 24) ),
            ("whm2st4se8" , cms.untracked.vint32(92, 0, 92, 23) ),
            ("whm2st4se9" , cms.untracked.vint32(48, 0, 48, 12) ),
            ]
        )
    ),
    DTTPGParameters = cms.PSet(
        Debug = cms.untracked.bool(False),
        SectCollParameters = cms.PSet(
            Debug = cms.untracked.bool(False),
            SCCSP1 = cms.int32(0),
            SCCSP2 = cms.int32(0),
            SCCSP3 = cms.int32(0),
            SCCSP4 = cms.int32(0),
            SCCSP5 = cms.int32(0),
            SCECF1 = cms.bool(False),
            SCECF2 = cms.bool(False),
            SCECF3 = cms.bool(False),
            SCECF4 = cms.bool(False)
        ),
        TUParameters = cms.PSet(
            BtiParameters = cms.PSet(
                AC1 = cms.int32(0),
                AC2 = cms.int32(3),
                ACH = cms.int32(1),
                ACL = cms.int32(2),
                CH = cms.int32(41),
                CL = cms.int32(22),
                DEAD = cms.int32(31),
                Debug = cms.untracked.int32(0),
                KACCTHETA = cms.int32(1),
                KMAX = cms.int32(64),
                LH = cms.int32(21),
                LL = cms.int32(2),
                LTS = cms.int32(3),
                PTMS0 = cms.int32(0),
                PTMS1 = cms.int32(0),
                PTMS10 = cms.int32(1),
                PTMS11 = cms.int32(1),
                PTMS12 = cms.int32(1),
                PTMS13 = cms.int32(1),
                PTMS14 = cms.int32(1),
                PTMS15 = cms.int32(1),
                PTMS16 = cms.int32(1),
                PTMS17 = cms.int32(1),
                PTMS18 = cms.int32(1),
                PTMS19 = cms.int32(1),
                PTMS2 = cms.int32(0),
                PTMS20 = cms.int32(1),
                PTMS21 = cms.int32(1),
                PTMS22 = cms.int32(1),
                PTMS23 = cms.int32(1),
                PTMS24 = cms.int32(1),
                PTMS25 = cms.int32(1),
                PTMS26 = cms.int32(1),
                PTMS27 = cms.int32(1),
                PTMS28 = cms.int32(1),
                PTMS29 = cms.int32(1),
                PTMS3 = cms.int32(0),
                PTMS30 = cms.int32(0),
                PTMS31 = cms.int32(0),
                PTMS4 = cms.int32(1),
                PTMS5 = cms.int32(1),
                PTMS6 = cms.int32(1),
                PTMS7 = cms.int32(1),
                PTMS8 = cms.int32(1),
                PTMS9 = cms.int32(1),
                RE43 = cms.int32(2),
                RH = cms.int32(61),
                RL = cms.int32(42),
                RON = cms.bool(True),
                SET = cms.int32(7),
                ST43 = cms.int32(42),
                WEN0 = cms.int32(1),
                WEN1 = cms.int32(1),
                WEN2 = cms.int32(1),
                WEN3 = cms.int32(1),
                WEN4 = cms.int32(1),
                WEN5 = cms.int32(1),
                WEN6 = cms.int32(1),
                WEN7 = cms.int32(1),
                WEN8 = cms.int32(1),
                XON = cms.bool(False)
            ),
            Debug = cms.untracked.bool(False),
            LutParameters = cms.PSet(
                BTIC = cms.untracked.int32(0),
                D = cms.untracked.double(0),
                Debug = cms.untracked.bool(False),
                WHEEL = cms.untracked.int32(-1),
                XCN = cms.untracked.double(0)
            ),
            TSPhiParameters = cms.PSet(
                Debug = cms.untracked.bool(False),
                TSMCCE1 = cms.bool(True),
                TSMCCE2 = cms.bool(False),
                TSMCCEC = cms.bool(False),
                TSMCGS1 = cms.bool(True),
                TSMCGS2 = cms.bool(True),
                TSMGS1 = cms.int32(1),
                TSMGS2 = cms.int32(1),
                TSMHSP = cms.int32(1),
                TSMHTE1 = cms.bool(True),
                TSMHTE2 = cms.bool(False),
                TSMHTEC = cms.bool(False),
                TSMMSK1 = cms.int32(312),
                TSMMSK2 = cms.int32(312),
                TSMNOE1 = cms.bool(True),
                TSMNOE2 = cms.bool(False),
                TSMNOEC = cms.bool(False),
                TSMWORD = cms.int32(255),
                TSSCCE1 = cms.bool(True),
                TSSCCE2 = cms.bool(False),
                TSSCCEC = cms.bool(False),
                TSSCGS1 = cms.bool(True),
                TSSCGS2 = cms.bool(True),
                TSSGS1 = cms.int32(1),
                TSSGS2 = cms.int32(1),
                TSSHTE1 = cms.bool(True),
                TSSHTE2 = cms.bool(False),
                TSSHTEC = cms.bool(False),
                TSSMSK1 = cms.int32(312),
                TSSMSK2 = cms.int32(312),
                TSSNOE1 = cms.bool(True),
                TSSNOE2 = cms.bool(False),
                TSSNOEC = cms.bool(False),
                TSTREN0 = cms.bool(True),
                TSTREN1 = cms.bool(True),
                TSTREN10 = cms.bool(True),
                TSTREN11 = cms.bool(True),
                TSTREN12 = cms.bool(True),
                TSTREN13 = cms.bool(True),
                TSTREN14 = cms.bool(True),
                TSTREN15 = cms.bool(True),
                TSTREN16 = cms.bool(True),
                TSTREN17 = cms.bool(True),
                TSTREN18 = cms.bool(True),
                TSTREN19 = cms.bool(True),
                TSTREN2 = cms.bool(True),
                TSTREN20 = cms.bool(True),
                TSTREN21 = cms.bool(True),
                TSTREN22 = cms.bool(True),
                TSTREN23 = cms.bool(True),
                TSTREN3 = cms.bool(True),
                TSTREN4 = cms.bool(True),
                TSTREN5 = cms.bool(True),
                TSTREN6 = cms.bool(True),
                TSTREN7 = cms.bool(True),
                TSTREN8 = cms.bool(True),
                TSTREN9 = cms.bool(True)
            ),
            TSThetaParameters = cms.PSet(
                Debug = cms.untracked.bool(False)
            ),
            TracoParameters = cms.PSet(
                BTIC = cms.int32(32),
                DD = cms.int32(18),
                Debug = cms.untracked.int32(0),
                FHISM = cms.int32(0),
                FHTMSK = cms.int32(0),
                FHTPRF = cms.int32(1),
                FLTMSK = cms.int32(1),
                FPRGCOMP = cms.int32(2),
                FSLMSK = cms.int32(0),
                IBTIOFF = cms.int32(0),
                KPRGCOM = cms.int32(255),
                KRAD = cms.int32(0),
                LTF = cms.int32(0),
                LTS = cms.int32(0),
                LVALIDIFH = cms.int32(0),
                REUSEI = cms.int32(1),
                REUSEO = cms.int32(1),
                SHISM = cms.int32(0),
                SHTMSK = cms.int32(0),
                SHTPRF = cms.int32(1),
                SLTMSK = cms.int32(1),
                SPRGCOMP = cms.int32(2),
                SSLMSK = cms.int32(0),
                TRGENB0 = cms.int32(1),
                TRGENB1 = cms.int32(1),
                TRGENB10 = cms.int32(1),
                TRGENB11 = cms.int32(1),
                TRGENB12 = cms.int32(1),
                TRGENB13 = cms.int32(1),
                TRGENB14 = cms.int32(1),
                TRGENB15 = cms.int32(1),
                TRGENB2 = cms.int32(1),
                TRGENB3 = cms.int32(1),
                TRGENB4 = cms.int32(1),
                TRGENB5 = cms.int32(1),
                TRGENB6 = cms.int32(1),
                TRGENB7 = cms.int32(1),
                TRGENB8 = cms.int32(1),
                TRGENB9 = cms.int32(1)
            )
        )
    ),
    TracoLutsFromDB = cms.bool(True),
    UseBtiAcceptParam = cms.bool(True),
    UseT0 = cms.bool(False),
    bxOffset = cms.int32(19),
    cfgConfig = cms.bool(False),
    debug = cms.bool(False),
    debugBti = cms.int32(0),
    debugDB = cms.bool(False),
    debugLUTs = cms.bool(False),
    debugPed = cms.bool(False),
    debugSC = cms.bool(False),
    debugTSP = cms.bool(False),
    debugTST = cms.bool(False),
    debugTU = cms.bool(False),
    debugTraco = cms.int32(0),
    finePhase = cms.double(25.0)
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOppositeForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositePropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.ParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.PropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStep'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.RPCConeBuilder = cms.ESProducer("RPCConeBuilder",
    towerBeg = cms.int32(0),
    towerEnd = cms.int32(16)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiPixelTemplateStoreESProducer = cms.ESProducer("SiPixelTemplateStoreESProducer",
    appendToDataLabel = cms.string('')
)


process.SiStripClusterizerConditionsESProducer = cms.ESProducer("SiStripClusterizerConditionsESProducer",
    Label = cms.string(''),
    QualityLabel = cms.string(''),
    appendToDataLabel = cms.string('')
)


process.SiStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.SiStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SiStripRegionConnectivity = cms.ESProducer("SiStripRegionConnectivity",
    EtaDivisions = cms.untracked.uint32(20),
    EtaMax = cms.untracked.double(2.5),
    PhiDivisions = cms.untracked.uint32(20)
)


process.SimpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    minVertices = cms.uint32(1),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloConfig = cms.ESProducer("L1TCaloConfigESProducer",
    fwVersionLayer2 = cms.uint32(3),
    l1Epoch = cms.string('Stage1')
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.ctppsGeometryESModule = cms.ESProducer("CTPPSGeometryESModule",
    appendToDataLabel = cms.string(''),
    buildMisalignedGeometry = cms.bool(False),
    compactViewTag = cms.string(''),
    dbTag = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromPreprocessedDB = cms.untracked.bool(True),
    isRun2 = cms.bool(False),
    verbosity = cms.untracked.uint32(1)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    opticsLabel = cms.string('')
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalElectronicsMappingGPUESProducer = cms.ESProducer("EcalElectronicsMappingGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalGainRatiosGPUESProducer = cms.ESProducer("EcalGainRatiosGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalIntercalibConstantsGPUESProducer = cms.ESProducer("EcalIntercalibConstantsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLaserAPDPNRatiosGPUESProducer = cms.ESProducer("EcalLaserAPDPNRatiosGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLaserAPDPNRatiosRefGPUESProducer = cms.ESProducer("EcalLaserAPDPNRatiosRefGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLaserAlphasGPUESProducer = cms.ESProducer("EcalLaserAlphasGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalLinearCorrectionsGPUESProducer = cms.ESProducer("EcalLinearCorrectionsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalPedestalsGPUESProducer = cms.ESProducer("EcalPedestalsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalPulseCovariancesGPUESProducer = cms.ESProducer("EcalPulseCovariancesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalPulseShapesGPUESProducer = cms.ESProducer("EcalPulseShapesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalRechitADCToGeVConstantGPUESProducer = cms.ESProducer("EcalRechitADCToGeVConstantGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalRechitChannelStatusGPUESProducer = cms.ESProducer("EcalRechitChannelStatusGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalSamplesCorrelationGPUESProducer = cms.ESProducer("EcalSamplesCorrelationGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring(
            'kNonRespondingIsolated',
            'kDeadVFE',
            'kDeadFE',
            'kNoDataNoTP'
        ),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring(
            'kDAC',
            'kNoLaser',
            'kNoisy',
            'kNNoisy',
            'kNNNoisy',
            'kNNNNoisy',
            'kNNNNNoisy',
            'kFixedG6',
            'kFixedG1',
            'kFixedG0'
        ),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring(
            'kFaultyHardware',
            'kDead',
            'kKilled'
        ),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring(
            'kPoorReco',
            'kPoorCalib',
            'kNoisy',
            'kSaturated'
        ),
        kRecovered = cms.vstring(
            'kLeadingEdgeRecovered',
            'kTowerRecovered'
        ),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring(
            'kWeird',
            'kDiWeird'
        )
    ),
    timeThresh = cms.double(2.0)
)


process.ecalTimeBiasCorrectionsGPUESProducer = cms.ESProducer("EcalTimeBiasCorrectionsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.ecalTimeCalibConstantsGPUESProducer = cms.ESProducer("EcalTimeCalibConstantsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.fakeTwinMuxParams = cms.ESProducer("L1TTwinMuxParamsESProducer",
    CorrectDTBxwRPC = cms.bool(True),
    dphiWindowBxShift = cms.uint32(9999),
    fwVersion = cms.uint32(1),
    useLowQDT = cms.bool(False),
    useOnlyDT = cms.bool(False),
    useOnlyRPC = cms.bool(False),
    useRpcBxForDtBelowQuality = cms.uint32(4),
    verbose = cms.bool(False)
)


process.hcalChannelPropertiesESProd = cms.ESProducer("HcalChannelPropertiesEP")


process.hcalChannelQualityGPUESProducer = cms.ESProducer("HcalChannelQualityGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalConvertedEffectivePedestalWidthsGPUESProducer = cms.ESProducer("HcalConvertedEffectivePedestalWidthsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string('withTopoEff'),
    label1 = cms.string('withTopoEff'),
    label2 = cms.string(''),
    label3 = cms.string('')
)


process.hcalConvertedEffectivePedestalsGPUESProducer = cms.ESProducer("HcalConvertedEffectivePedestalsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string('withTopoEff'),
    label1 = cms.string(''),
    label2 = cms.string('')
)


process.hcalConvertedPedestalWidthsGPUESProducer = cms.ESProducer("HcalConvertedPedestalWidthsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string(''),
    label1 = cms.string(''),
    label2 = cms.string(''),
    label3 = cms.string('')
)


process.hcalConvertedPedestalsGPUESProducer = cms.ESProducer("HcalConvertedPedestalsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label0 = cms.string(''),
    label1 = cms.string(''),
    label2 = cms.string('')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalElectronicsMappingGPUESProducer = cms.ESProducer("HcalElectronicsMappingGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalGainWidthsGPUESProducer = cms.ESProducer("HcalGainWidthsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalGainsGPUESProducer = cms.ESProducer("HcalGainsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalLUTCorrsGPUESProducer = cms.ESProducer("HcalLUTCorrsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalQIECodersGPUESProducer = cms.ESProducer("HcalQIECodersGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalQIETypesGPUESProducer = cms.ESProducer("HcalQIETypesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring(
        'HcalCellMask',
        'HcalCellOff',
        'HcalCellDead'
    ),
    RecoveredRecHitBits = cms.vstring(''),
    SeverityLevels = cms.VPSet(
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(0),
            RecHitFlags = cms.vstring('')
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring('')
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring(
                'HBHEIsolatedNoise',
                'HFAnomalousHit'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring(
                'HBHEHpdHitMultiplicity',
                'HBHESpikeNoise',
                'HBHETS4TS5Noise',
                'HBHEOOTPU',
                'HBHEFlatNoise',
                'HBHENegativeNoise'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring(
                'HFLongShort',
                'HFS8S1Ratio',
                'HFPET',
                'HFSignalAsymmetry'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring('')
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(
                'HcalCellOff',
                'HcalCellDead'
            ),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring('')
        )
    ),
    appendToDataLabel = cms.string(''),
    phase = cms.uint32(1)
)


process.hcalRecoParamsWithPulseShapesGPUESProducer = cms.ESProducer("HcalRecoParamsWithPulseShapesGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalRespCorrsGPUESProducer = cms.ESProducer("HcalRespCorrsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalSiPMCharacteristicsGPUESProducer = cms.ESProducer("HcalSiPMCharacteristicsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalSiPMParametersGPUESProducer = cms.ESProducer("HcalSiPMParametersGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcalTimeCorrsGPUESProducer = cms.ESProducer("HcalTimeCorrsGPUESProducer",
    ComponentName = cms.string(''),
    appendToDataLabel = cms.string(''),
    label = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer")


process.hltBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT_v4.weights.xml.gz')
)


process.hltCombinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVRecoVertex',
        'CombinedSVPseudoVertex',
        'CombinedSVNoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltCombinedSecondaryVertexV2 = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex',
        'CombinedSVIVFV2PseudoVertex',
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum')
)


process.hltESPBwdAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPBwdAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.hltESPBwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPBwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPChi2ChargeLooseMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeLooseMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator2000 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    MaxChi2 = cms.double(2000.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutForHI')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeTightMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2MeasurementEstimator100 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator100'),
    MaxChi2 = cms.double(40.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.hltESPChi2MeasurementEstimator16 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator30 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator9 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPCloseComponentsMerger5D = cms.ESProducer("CloseComponentsMergerESProducer5D",
    ComponentName = cms.string('hltESPCloseComponentsMerger5D'),
    DistanceMeasure = cms.string('hltESPKullbackLeiblerDistance5D'),
    MaxComponents = cms.int32(12)
)


process.hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.2),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerShortSig5 = cms.ESProducer("PromptTrackCountingESProducer",
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.05),
    maxImpactParameterSig = cms.double(5.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    minimumImpactParameter = cms.double(-1.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D1stLoose = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.03),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.2),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.hltESPDummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPDummyDetLayerGeometry')
)


process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.hltESPElectronMaterialEffects = cms.ESProducer("GsfMaterialEffectsESProducer",
    BetheHeitlerCorrection = cms.int32(2),
    BetheHeitlerParametrization = cms.string('BetheHeitler_cdfmom_nC6_O5.par'),
    ComponentName = cms.string('hltESPElectronMaterialEffects'),
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    Mass = cms.double(0.000511),
    MultipleScatteringUpdator = cms.string('MultipleScatteringUpdator')
)


process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFittingSmootherIT = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPFittingSmootherIT'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFittingSmootherRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPFittingSmootherRK'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPKFFittingSmootherForLoopers'),
    standardFitter = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK')
)


process.hltESPFwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPFwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPGlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.hltESPGsfElectronFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPGsfElectronFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPGsfTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPGsfTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPGsfTrajectoryFitter = cms.ESProducer("GsfTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPGsfTrajectoryFitter'),
    GeometricalPropagator = cms.string('hltESPAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPGsfTrajectorySmoother = cms.ESProducer("GsfTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPGsfTrajectorySmoother'),
    ErrorRescaling = cms.double(100.0),
    GeometricalPropagator = cms.string('hltESPBwdAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry')
)


process.hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2MeasurementEstimator36 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2MeasurementEstimator36'),
    MaxChi2 = cms.double(36.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPKFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherForLoopers'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPRKTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPRKTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFUpdator = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('hltESPKFUpdator')
)


process.hltESPKullbackLeiblerDistance5D = cms.ESProducer("DistanceBetweenComponentsESProducer5D",
    ComponentName = cms.string('hltESPKullbackLeiblerDistance5D'),
    DistanceMeasure = cms.string('KullbackLeibler')
)


process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    appendToDataLabel = cms.string(''),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    )
)


process.hltESPMixedStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPMixedStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.hltESPMixedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMixedTripletStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPMixedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPMuonTransientTrackingRecHitBuilder')
)


process.hltESPPixelCPEFast = cms.ESProducer("PixelCPEFastESProducerPhase1",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEFast'),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.hltESPPixelCPEGeneric = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    NoTemplateErrorsWhenNoTrkAngles = cms.bool(False),
    SmallPitch = cms.bool(False),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    isPhase2 = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(False),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.hltESPPixelCPETemplateReco = cms.ESProducer("PixelCPETemplateRecoESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPETemplateReco'),
    LoadTemplatesFromDB = cms.bool(True),
    UseClusterSplitter = cms.bool(False),
    appendToDataLabel = cms.string(''),
    barrelTemplateID = cms.int32(0),
    directoryWithTemplates = cms.int32(0),
    doLorentzFromAlignment = cms.bool(False),
    forwardTemplateID = cms.int32(0),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    speed = cms.int32(-2),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True)
)


process.hltESPPixelLessStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPPixelLessStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPPixelLessStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.hltESPPixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelLessStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPPixelPairStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPPixelPairStepChi2MeasurementEstimator25 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2MeasurementEstimator25'),
    MaxChi2 = cms.double(25.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPPixelPairTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelPairTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.hltESPRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPRKTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPRKTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPRungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.hltESPSmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagator'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial')
)


process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite')
)


process.hltESPSoftLeptonByDistance = cms.ESProducer("LeptonTaggerByDistanceESProducer",
    distance = cms.double(0.5)
)


process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPStripCPEfromTrackAngle = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('hltESPStripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.hltESPTTRHBWithTrackAngle = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    appendToDataLabel = cms.string('')
)


process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPETemplateReco'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    appendToDataLabel = cms.string('')
)


process.hltESPTTRHBuilderPixelOnly = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake'),
    appendToDataLabel = cms.string('')
)


process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPTobTecStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPTobTecStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.hltESPTobTecStepFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmoother'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    standardFitter = cms.string('hltESPTobTecStepFitterSmoother')
)


process.hltESPTobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTobTecStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.09)
)


process.hltESPTrackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('hltESPTrackAlgoPriorityOrder'),
    algoOrder = cms.vstring(),
    appendToDataLabel = cms.string('')
)


process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    appendToDataLabel = cms.string(''),
    trackerGeometryLabel = cms.untracked.string(''),
    usePhase2Stacks = cms.bool(False)
)


process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(0.0),
    ValidHitBonus = cms.double(100.0),
    allowSharedFirstHit = cms.bool(False),
    fractionShared = cms.double(0.5)
)


process.hltESPTrajectoryFitterRK = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTrajectoryFitterRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPTrajectorySmootherRK = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTrajectorySmootherRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltOnlineBeamSpotESProducer = cms.ESProducer("OnlineBeamSpotESProducer",
    appendToDataLabel = cms.string(''),
    sigmaXYThreshold = cms.double(4.0),
    sigmaZThreshold = cms.double(2.0),
    timeThreshold = cms.int32(1000000)
)


process.hltPixelTracksCleanerBySharedHits = cms.ESProducer("PixelTrackCleanerBySharedHitsESProducer",
    ComponentName = cms.string('hltPixelTracksCleanerBySharedHits'),
    appendToDataLabel = cms.string(''),
    useQuadrupletAlgo = cms.bool(False)
)


process.hltTrackCleaner = cms.ESProducer("TrackCleanerESProducer",
    ComponentName = cms.string('hltTrackCleaner'),
    appendToDataLabel = cms.string('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    etaBinSize = cms.double(0.125),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(True),
    includeGEM = cms.bool(True),
    includeME0 = cms.bool(False),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.muonSeededTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(1.0),
    ValidHitBonus = cms.double(1000.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.1)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelGainCalibrationForHLTGPU = cms.ESProducer("SiPixelGainCalibrationForHLTGPUESProducer",
    appendToDataLabel = cms.string('')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    appendToDataLabel = cms.string(''),
    siPixelQualityLabel = cms.string(''),
    siPixelQualityLabel_RawToDigi = cms.string('')
)


process.siPixelROCsStatusAndMappingWrapperESProducer = cms.ESProducer("SiPixelROCsStatusAndMappingWrapperESProducer",
    CablingMapLabel = cms.string(''),
    ComponentName = cms.string(''),
    UseQualityInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CSCChannelMapperESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCChannelMapperRecord')
)


process.CSCINdexerESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCIndexerRecord')
)


process.CSCL1TPLookupTableEP = cms.ESSource("CSCL1TPLookupTableEP",
    esDiffToSlopeME11aFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME11a_even_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME11a_odd_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME11a_even_GEMlayer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME11a_odd_GEMlayer2.txt'
    ),
    esDiffToSlopeME11bFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME11b_even_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME11b_odd_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME11b_even_GEMlayer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME11b_odd_GEMlayer2.txt'
    ),
    esDiffToSlopeME21Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME21_even_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME21_odd_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME21_even_GEMlayer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/SlopeAmendment_ME21_odd_GEMlayer2.txt'
    ),
    gemCscSlopeCorrectionFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME11a_even_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME11b_even_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME21_even_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME11a_odd_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME11b_odd_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME21_odd_GEMlayer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME11a_even_GEMlayer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME11b_even_GEMlayer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME21_even_GEMlayer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME11a_odd_GEMlayer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME11b_odd_GEMlayer2.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/ExtrapolationBySlope_ME21_odd_GEMlayer2.txt'
    ),
    gemCscSlopeCosiCorrectionFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11a_even_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11b_even_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME21_even_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11a_odd_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11b_odd_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME21_odd_layer1.txt'
    ),
    gemCscSlopeCosiFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11a_even_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11a_odd_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11a_even_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11a_odd_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11b_even_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11b_odd_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11b_even_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11b_odd_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME21_even_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME21_odd_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME21_even_layer1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME21_odd_layer1.txt'
    ),
    padToEsME11aFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1a_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1a_odd.txt'
    ),
    padToEsME11bFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1b_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1b_odd.txt'
    ),
    padToEsME21Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME21_odd.txt'
    ),
    positionLUTFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat0_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat1_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat2_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat3_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat4_v1.txt'
    ),
    rollToMaxWgME11Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME11_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME11_odd.txt'
    ),
    rollToMaxWgME21Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME21_odd.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME21_odd.txt'
    ),
    rollToMinWgME11Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME11_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME11_odd.txt'
    ),
    rollToMinWgME21Files = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME21_odd.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME21_even.txt',
        'L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME21_odd.txt'
    ),
    slopeLUTFiles = cms.vstring(
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat0_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat1_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat2_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat3_v1.txt',
        'L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat4_v1.txt'
    )
)


process.GlobalParametersRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TGlobalParametersRcd')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(0),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(True),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(True),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('130X_mcRun3_2023_realistic_postBPix_v2'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet(
        cms.PSet(
            record = cms.string('BeamSpotOnlineLegacyObjectsRcd'),
            refreshTime = cms.uint64(2)
        ),
        cms.PSet(
            record = cms.string('BeamSpotOnlineHLTObjectsRcd'),
            refreshTime = cms.uint64(2)
        ),
        cms.PSet(
            record = cms.string('L1TUtmTriggerMenuRcd'),
            snapshotTime = cms.string('9999-12-31 23:59:59.000'),
            tag = cms.string('L1Menu_Collisions2023_v1_2_0_xml')
        )
    )
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.bmbtfParamsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TMuonBarrelParamsRcd')
)


process.caloConfigSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TCaloConfigRcd')
)


process.ecalMultifitParametersGPUESProducer = cms.ESSource("EcalMultifitParametersGPUESProducer",
    EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
    EBtimeFitParameters = cms.vdouble(
        -2.015452, 3.130702, -12.3473, 41.88921, -82.83944,
        91.01147, -50.35761, 11.05621
    ),
    EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
    EEtimeFitParameters = cms.vdouble(
        -2.390548, 3.553628, -17.62341, 67.67538, -133.213,
        140.7432, -75.41106, 16.20277
    ),
    appendToDataLabel = cms.string(''),
    pulseOffsets = cms.vint32(
        -3, -2, -1, 0, 1,
        2, 3, 4
    )
)


process.ecalRecHitParametersGPUESProducer = cms.ESSource("EcalRecHitParametersGPUESProducer",
    ChannelStatusToBeExcluded = cms.vstring(
        'kDAC',
        'kNoisy',
        'kNNoisy',
        'kFixedG6',
        'kFixedG1',
        'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE',
        'kDeadFE',
        'kNoDataNoTP'
    ),
    appendToDataLabel = cms.string(''),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring(
            'kOk',
            'kDAC',
            'kNoLaser',
            'kNoisy'
        ),
        kNeighboursRecovered = cms.vstring(
            'kFixedG0',
            'kNonRespondingIsolated',
            'kDeadVFE'
        ),
        kNoisy = cms.vstring(
            'kNNoisy',
            'kFixedG6',
            'kFixedG1'
        ),
        kTowerRecovered = cms.vstring('kDeadFE')
    )
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.hcalMahiPulseOffsetsGPUESProducer = cms.ESSource("HcalMahiPulseOffsetsGPUESProducer",
    appendToDataLabel = cms.string(''),
    pulseOffsets = cms.vint32(
        -3, -2, -1, 0, 1,
        2, 3, 4
    )
)


process.hltESSBTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.hltESSEcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.hltESSHcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.l1ugmtdb = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('L1TMuonGlobalParamsO2ORcd'),
        tag = cms.string('L1TMuonGlobalParamsPrototype_Stage2v0_hlt')
    ))
)


process.ppsPixelTopologyESSource = cms.ESSource("PPSPixelTopologyESSource",
    PitchSimX = cms.double(0.1),
    PitchSimY = cms.double(0.15),
    RunType = cms.string('Run3'),
    activeEdgeSigma = cms.double(0.02),
    appendToDataLabel = cms.string(''),
    deadEdgeWidth = cms.double(0.2),
    noOfPixelSimX = cms.int32(160),
    noOfPixelSimY = cms.int32(104),
    noOfPixels = cms.int32(16640),
    physActiveEdgeDist = cms.double(0.15),
    simXWidth = cms.double(16.6),
    simYWidth = cms.double(16.2),
    thickness = cms.double(0.23)
)


process.rpcconesrc = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1RPCConeBuilderRcd')
)


process.twinmuxParamsSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TTwinMuxParamsRcd')
)


process.SimL1TCalorimeterTask = cms.Task(process.simCaloStage2Digis, process.simCaloStage2Layer1Digis)


process.SimL1TGlobalTask = cms.Task(process.simGtStage2Digis)


process.SimL1TMuonCommonTask = cms.Task(process.simCscTriggerPrimitiveDigis, process.simDtTriggerPrimitiveDigis)


process.SimL1TechnicalTriggersTask = cms.Task(process.simGtExtFakeStage2Digis)


process.simMuonGEMPadTask = cms.Task(process.simMuonGEMPadDigiClusters, process.simMuonGEMPadDigis)


process.SimL1TMuonTask = cms.Task(process.SimL1TMuonCommonTask, process.simBmtfDigis, process.simCscTriggerPrimitiveDigisRun3, process.simEmtfDigis, process.simEmtfShowers, process.simGmtCaloSumDigis, process.simGmtShowerDigis, process.simGmtStage2Digis, process.simKBmtfDigis, process.simKBmtfStubs, process.simMuonGEMPadTask, process.simOmtfDigis, process.simTwinMuxDigis)


process.SimL1EmulatorCoreTask = cms.Task(process.SimL1TCalorimeterTask, process.SimL1TGlobalTask, process.SimL1TMuonTask, process.SimL1TechnicalTriggersTask)


process.SimL1EmulatorTask = cms.Task(process.SimL1EmulatorCoreTask, process.packCaloStage2, process.packGmtStage2, process.packGtStage2, process.rawDataCollector, process.simHcalTriggerPrimitiveDigis, process.unpackCSC, process.unpackDT, process.unpackEcal, process.unpackGEM, process.unpackHcal, process.unpackRPC)


process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerTask = cms.ConditionalTask(process.hltEcalDetIdToBeRecovered, process.hltEcalDigis, process.hltEcalDigisFromGPU, process.hltEcalDigisGPU, process.hltEcalDigisLegacy, process.hltEcalRecHit, process.hltEcalUncalibRecHit, process.hltEcalUncalibRecHitFromSoA, process.hltEcalUncalibRecHitGPU, process.hltEcalUncalibRecHitLegacy, process.hltEcalUncalibRecHitSoA)


process.HLTPreshowerTask = cms.ConditionalTask(process.hltEcalPreshowerDigis, process.hltEcalPreshowerRecHit)


process.HLTDoFullUnpackingEgammaEcalTask = cms.ConditionalTask(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerTask, process.HLTPreshowerTask)


process.HLTDoLocalHcalTask = cms.ConditionalTask(process.hltHbhereco, process.hltHbherecoFromGPU, process.hltHbherecoGPU, process.hltHbherecoLegacy, process.hltHcalDigis, process.hltHcalDigisGPU, process.hltHfprereco, process.hltHfreco, process.hltHoreco)


process.HLTDoLocalPixelTask = cms.ConditionalTask(process.hltOnlineBeamSpotToGPU, process.hltSiPixelClusters, process.hltSiPixelClustersCache, process.hltSiPixelClustersFromSoA, process.hltSiPixelClustersGPU, process.hltSiPixelClustersLegacy, process.hltSiPixelDigiErrorsSoA, process.hltSiPixelDigis, process.hltSiPixelDigisFromSoA, process.hltSiPixelDigisLegacy, process.hltSiPixelDigisSoA, process.hltSiPixelRecHits, process.hltSiPixelRecHitsFromGPU, process.hltSiPixelRecHitsFromLegacy, process.hltSiPixelRecHitsGPU, process.hltSiPixelRecHitsSoA, process.hltSiPixelRecHitsSoAFromGPU)


process.HLTRecoPixelTracksTask = cms.ConditionalTask(process.hltPixelTracks, process.hltPixelTracksCPU, process.hltPixelTracksFromGPU, process.hltPixelTracksGPU, process.hltPixelTracksSoA, process.hltPixelTracksTrackingRegions)


process.HLTRecopixelvertexingTask = cms.ConditionalTask(process.HLTRecoPixelTracksTask, process.hltPixelVertices, process.hltPixelVerticesCPU, process.hltPixelVerticesFromGPU, process.hltPixelVerticesGPU, process.hltPixelVerticesSoA, process.hltTrimmedPixelVertices)


process.HLTL1UnpackerSequence = cms.Sequence(process.hltGtStage2Digis+process.hltGtStage2ObjectMap)


process.HLTBeamSpot = cms.Sequence(process.hltOnlineMetaDataDigis+process.hltOnlineBeamSpot)


process.HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)


process.HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalTask)


process.HLTPFClusteringForEgamma = cms.Sequence(process.hltRechitInRegionsECAL+process.hltRechitInRegionsES+process.hltParticleFlowRecHitECALL1Seeded+process.hltParticleFlowRecHitPSL1Seeded+process.hltParticleFlowClusterPSL1Seeded+process.hltParticleFlowClusterECALUncorrectedL1Seeded+process.hltParticleFlowClusterECALL1Seeded+process.hltParticleFlowSuperClusterECALL1Seeded)


process.HLTDoLocalHcalSequence = cms.Sequence(process.HLTDoLocalHcalTask)


process.HLTFastJetForEgamma = cms.Sequence(process.hltFixedGridRhoFastjetAllCaloForMuons)


process.HLTDoLocalPixelSequence = cms.Sequence(process.HLTDoLocalPixelTask)


process.HLTDoLocalStripSequence = cms.Sequence(process.hltSiStripExcludedFEDListProducer+process.hltSiStripRawToClustersFacility+process.hltSiStripClusters)


process.HLTElePixelMatchSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.hltPixelLayerPairs+process.hltPixelLayerTriplets+process.hltEgammaHoverE+process.hltEgammaSuperClustersToPixelMatch+process.hltEleSeedsTrackingRegions+process.hltElePixelHitDoublets+process.hltElePixelHitDoubletsForTriplets+process.hltElePixelHitTriplets+process.hltElePixelSeedsDoublets+process.hltElePixelSeedsTriplets+process.hltElePixelSeedsCombined+process.hltEgammaElectronPixelSeeds+process.hltEgammaPixelMatchVars)


process.HLTEle33CaloIdLSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter+process.hltEG33EtFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEG33HEFilter+process.hltEgammaClusterShape+process.hltEG33CaloIdLClusterShapeFilter+process.HLTElePixelMatchSequence+process.hltEle33CaloIdLPixelMatchFilter)


process.HLTEle33CaloIdLMWSequence = cms.Sequence(process.HLTEle33CaloIdLSequence+process.hltEle33CaloIdLMWPMS2Filter)


process.HLTPFClusteringForEgammaUnseeded = cms.Sequence(process.hltParticleFlowRecHitECALUnseeded+process.hltParticleFlowRecHitPSUnseeded+process.hltParticleFlowClusterPSUnseeded+process.hltParticleFlowClusterECALUncorrectedUnseeded+process.hltParticleFlowClusterECALUnseeded+process.hltParticleFlowSuperClusterECALUnseeded)


process.HLTElePixelMatchUnseededSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.hltPixelLayerPairs+process.hltPixelLayerTriplets+process.hltEgammaHoverEUnseeded+process.hltEgammaSuperClustersToPixelMatchUnseeded+process.hltEleSeedsTrackingRegionsUnseeded+process.hltElePixelHitDoubletsUnseeded+process.hltElePixelHitDoubletsForTripletsUnseeded+process.hltElePixelHitTripletsUnseeded+process.hltElePixelSeedsDoubletsUnseeded+process.hltElePixelSeedsTripletsUnseeded+process.hltElePixelSeedsCombinedUnseeded+process.hltEgammaElectronPixelSeedsUnseeded+process.hltEgammaPixelMatchVarsUnseeded)


process.HLTDoubleEle33CaloIdLUnseededSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgammaUnseeded+process.hltEgammaCandidatesUnseeded+process.hltEgammaCandidatesWrapperUnseeded+process.hltDiEG33EtUnseededFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverEUnseeded+process.hltDiEG33HEUnseededFilter+process.hltEgammaClusterShapeUnseeded+process.hltDiEG33CaloIdLClusterShapeUnseededFilter+process.HLTElePixelMatchUnseededSequence+process.hltDiEle33CaloIdLPixelMatchUnseededFilter)


process.HLTDoubleEle33CaloIdLMWSequence = cms.Sequence(process.HLTDoubleEle33CaloIdLUnseededSequence+process.hltDiEle33CaloIdLMWPMS2UnseededFilter)


process.HLTEndSequence = cms.Sequence(process.hltBoolEnd)


process.HLTPFHcalClustering = cms.Sequence(process.hltParticleFlowRecHitHBHE+process.hltParticleFlowClusterHBHE+process.hltParticleFlowClusterHCAL)


process.HLTGsfElectronSequence = cms.Sequence(process.hltEgammaCkfTrackCandidatesForGSF+process.hltEgammaGsfTracks+process.hltEgammaGsfElectrons+process.hltEgammaGsfTrackVars)


process.HLTRecopixelvertexingSequence = cms.Sequence(process.hltPixelTracksFitter+process.hltPixelTracksFilter, process.HLTRecopixelvertexingTask)


process.HLTIterativeTrackingIteration0 = cms.Sequence(process.hltIter0PFLowPixelSeedsFromPixelTracks+process.hltIter0PFlowCkfTrackCandidates+process.hltIter0PFlowCtfWithMaterialTracks+process.hltIter0PFlowTrackCutClassifier+process.hltMergedTracks)


process.HLTIterativeTrackingIter02 = cms.Sequence(process.HLTIterativeTrackingIteration0)


process.HLTTrackReconstructionForPFNoMu = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTRecopixelvertexingSequence+process.HLTDoLocalStripSequence+process.HLTIterativeTrackingIter02)


process.HLTTrackReconstructionForIsoElectronIter02 = cms.Sequence(process.HLTTrackReconstructionForPFNoMu)


process.HLTEle30WPTightGsfSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleEGOrFilter+process.hltEG30L1SingleEGOrEtFilter+process.hltEgammaClusterShape+process.hltEle30WPTightClusterShapeFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEle30WPTightHEFilter+process.hltEgammaEcalPFClusterIso+process.hltEle30WPTightEcalIsoFilter+process.HLTPFHcalClustering+process.hltEgammaHcalPFClusterIso+process.hltEle30WPTightHcalIsoFilter+process.HLTElePixelMatchSequence+process.hltEle30WPTightPixelMatchFilter+process.hltEle30WPTightPMS2Filter+process.HLTGsfElectronSequence+process.hltEle30WPTightGsfOneOEMinusOneOPFilter+process.hltEle30WPTightGsfMissingHitsFilter+process.hltEle30WPTightGsfDetaFilter+process.hltEle30WPTightGsfDphiFilter+process.HLTTrackReconstructionForIsoElectronIter02+process.hltEgammaEleGsfTrackIso+process.hltEle30WPTightGsfTrackIsoFilter)


process.HLTEle32WPTightGsfSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleEGOrFilter+process.hltEG32L1SingleEGOrEtFilter+process.hltEgammaClusterShape+process.hltEle32WPTightClusterShapeFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEle32WPTightHEFilter+process.hltEgammaEcalPFClusterIso+process.hltEle32WPTightEcalIsoFilter+process.HLTPFHcalClustering+process.hltEgammaHcalPFClusterIso+process.hltEle32WPTightHcalIsoFilter+process.HLTElePixelMatchSequence+process.hltEle32WPTightPixelMatchFilter+process.hltEle32WPTightPMS2Filter+process.HLTGsfElectronSequence+process.hltEle32WPTightGsfOneOEMinusOneOPFilter+process.hltEle32WPTightGsfMissingHitsFilter+process.hltEle32WPTightGsfDetaFilter+process.hltEle32WPTightGsfDphiFilter+process.HLTTrackReconstructionForIsoElectronIter02+process.hltEgammaEleGsfTrackIso+process.hltEle32WPTightGsfTrackIsoFilter)


process.HLTEle23Ele12CaloIdLTrackIdLIsoVLSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleAndDoubleEGOrPairFilter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter+process.hltEgammaClusterShape+process.hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter+process.hltEgammaEcalPFClusterIso+process.hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter+process.HLTPFHcalClustering+process.hltEgammaHcalPFClusterIso+process.hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter+process.HLTElePixelMatchSequence+process.hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter+process.HLTGsfElectronSequence+process.hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter+process.HLTTrackReconstructionForIsoElectronIter02+process.hltEgammaEleGsfTrackIso+process.hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter)


process.HLTEle115CaloIdVTGsfTrkIdTGsfSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleEGNonIsoOrWithJetAndTauFilter+process.hltEG115EtFilter+process.hltEgammaClusterShape+process.hltEG115CaloIdVTClusterShapeFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEG115CaloIdVTHEFilter+process.HLTElePixelMatchSequence+process.hltEle115CaloIdVTPixelMatchFilter+process.HLTGsfElectronSequence+process.hltEle115CaloIdVTGsfTrkIdTGsfDetaFilter+process.hltEle115CaloIdVTGsfTrkIdTGsfDphiFilter)


process.HLTEle135CaloIdVTGsfTrkIdTGsfSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleEGNonIsoOrWithJetAndTauFilter+process.hltEG135EtFilter+process.hltEgammaClusterShape+process.hltEG135CaloIdVTClusterShapeFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEG135CaloIdVTHEFilter+process.HLTElePixelMatchSequence+process.hltEle135CaloIdVTPixelMatchFilter+process.HLTGsfElectronSequence+process.hltEle135CaloIdVTGsfTrkIdTGsfDetaFilter+process.hltEle135CaloIdVTGsfTrkIdTGsfDphiFilter)


process.SimL1Emulator = cms.Sequence(process.SimL1EmulatorTask)


process.HLTriggerFirstPath = cms.Path(process.SimL1Emulator+process.hltGetRaw+process.hltPSetMap+process.hltBoolFalse)


process.HLT_DoubleEle33_CaloIdL_MW_v22 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau+process.hltPreDoubleEle33CaloIdLMW+process.HLTEle33CaloIdLMWSequence+process.HLTDoubleEle33CaloIdLMWSequence+process.HLTEndSequence)


process.HLT_Ele30_WPTight_Gsf_v5 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sSingleEGor+process.hltPreEle30WPTightGsf+process.HLTEle30WPTightGsfSequence+process.HLTEndSequence)


process.HLT_Ele32_WPTight_Gsf_v19 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sSingleEGor+process.hltPreEle32WPTightGsf+process.HLTEle32WPTightGsfSequence+process.HLTEndSequence)


process.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sSingleAndDoubleEG+process.hltPreEle23Ele12CaloIdLTrackIdLIsoVL+process.HLTEle23Ele12CaloIdLTrackIdLIsoVLSequence+process.HLTEndSequence)


process.HLT_Ele115_CaloIdVT_GsfTrkIdT_v19 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sSingleEGNonIsoOrWithJetAndTau+process.hltPreEle115CaloIdVTGsfTrkIdT+process.HLTEle115CaloIdVTGsfTrkIdTGsfSequence+process.HLTEndSequence)


process.HLT_Ele135_CaloIdVT_GsfTrkIdT_v12 = cms.Path(process.SimL1Emulator+process.HLTBeginSequence+process.hltL1sSingleEGNonIsoOrWithJetAndTau+process.hltPreEle135CaloIdVTGsfTrkIdT+process.HLTEle135CaloIdVTGsfTrkIdTGsfSequence+process.HLTEndSequence)


process.HLTriggerFinalPath = cms.Path(process.SimL1Emulator+process.hltGtStage2Digis+process.hltFEDSelectorTCDS+process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW+process.hltBoolFalse)


process.EgHLTExtraPath = cms.Path(process.hltEgammaHLTExtra)


process.MinimalOutput = cms.FinalPath(process.hltOutputMinimal)


process.schedule = cms.Schedule(*[ process.HLTriggerFirstPath, process.HLT_DoubleEle33_CaloIdL_MW_v22, process.HLT_Ele30_WPTight_Gsf_v5, process.HLT_Ele32_WPTight_Gsf_v19, process.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v23, process.HLT_Ele115_CaloIdVT_GsfTrkIdT_v19, process.HLT_Ele135_CaloIdVT_GsfTrkIdT_v12, process.HLTriggerFinalPath, process.MinimalOutput, process.EgHLTExtraPath ])

