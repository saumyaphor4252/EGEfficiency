# L1T INFO:  L1REPACK:FullMC will unpack Calorimetry and Muon L1T inputs, re-emulate L1T (Stage-2), and pack uGT, uGMT, and Calo Stage-2 output.
import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.AlpakaCore.ProcessAcceleratorAlpaka import ProcessAcceleratorAlpaka
from HeterogeneousCore.CUDACore.ProcessAcceleratorCUDA import ProcessAcceleratorCUDA
from HeterogeneousCore.ROCmCore.ProcessAcceleratorROCm import ProcessAcceleratorROCm

process = cms.Process("HLTX")

process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring( (
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/62538166-8a72-4313-a450-3468044081c5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/a6148b69-e8fe-4ae5-826a-3f49e9dfdbd1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/68ffd033-119e-45b8-870c-33dbdc869c0d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0a7fab63-c9a9-47a5-a75d-884f22c2fe8b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/207f8197-20e1-428c-a293-44e07e9489df.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2c805266-3c9f-476c-b154-459fe64970b6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/80fd1761-5f6c-4639-b70a-7786ea2337a1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a0b71de2-3b85-44d6-91f5-51adcf95fb78.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8f44315b-931b-47ec-89de-53861cc94fd9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e850e0a7-bdfc-439d-b68b-50d3eb6486fe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dd467700-0b6d-4cc2-acfc-d51ce2336f57.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/98186153-d131-4879-9e31-52ca43922622.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/38bf4b41-a59b-4a52-b1cf-3abb4feb533e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/235dda82-cda1-44a0-b895-55570bcf21b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/369475c0-1722-47d0-aeaf-9b1306a10030.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/30eb0956-2d9a-41d8-a782-4dcf07b46839.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/06e3428e-30af-4eaf-8828-c8981d3bc9b8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dfab3485-4910-48f1-bc75-c5aecba87784.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6cd54989-db49-48c1-b9ca-61df83a00bbb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/40e6bef7-a029-486e-ba6c-3656dd0b10ba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/096baa03-d55b-42d4-ba98-288051d7cfe0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/709a3cdb-70a3-491c-a67c-31578b5a2ec5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7b22d682-c717-4eba-aac2-bd8a3652239d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/914e1b41-c720-4af7-828b-65d973f11360.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/863f33f3-318b-4c96-bf72-98579ccfc145.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7ff3960b-fcd0-427d-ae70-e6bf506dc117.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/be959798-5437-4587-9d5e-dad798bcb3d2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/beac166a-c82f-4434-88bd-532447d71cc6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/62d4c345-82a5-4b17-afdb-37f8e919888e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/91067391-536b-4de2-a8ee-67e0745fef6c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9ef02344-32e3-40b1-83b3-3200fa9e09fc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/9e361ed9-64be-4c2b-9958-ca8ecd0a86ab.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a341fa10-0686-41a4-893d-12181aaa3f38.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/aa5dc6e9-7004-453f-bc9b-f2bbe09c6a56.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/a7c53947-61fe-4f36-af65-177117ffeac7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/33863787-ae14-43cf-8e00-969b72a59e3b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a7a23c5c-53fe-4bb8-b4a1-a9294d3cfcdc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/54e94947-0059-4518-9787-a3381fe891af.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/31286c29-2e7e-438a-9048-4ef3aff70881.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b8443b65-e707-4c84-b611-4e3a117e9ad9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f94ced6c-8384-4eba-bec0-de50d21ff191.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f5f97b83-b080-4222-b462-5a40c0d5aceb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/86db8ab7-1a56-44c0-90b2-51a82f82b1a0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/35289923-9f97-435b-a252-7486af47fe65.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5e285922-a3dd-4f43-b09a-a0a1501acebc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/2c5195aa-e884-4454-a3e2-d0909ddd4399.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/07253491-f948-4e03-864a-3859eced7976.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4a267f4f-9e4d-4461-97a6-f7c00040669f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/00674a86-3a2a-49c7-b571-a4ccca006423.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b7106511-fc1f-4323-8934-247a3dfb3bd7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3656f9cd-d979-4d57-b45a-2baee5c5bea7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6d7bcf80-d833-4f3c-a280-9ba1cb04dbbc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7bbba883-b2ef-400e-89f2-b4ae49cf6fa8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4b5fa1e4-8d0d-44c5-a990-130ed8d9ab4c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cb2f99ea-5ce9-441a-aa4a-5985c00ab179.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6d73df3e-d4a9-46b1-b83b-286dbed9ea60.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7bee64c8-f43d-4ed4-a698-2e276f40f4af.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9465dd37-1e00-4dfd-9813-54910443b963.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9fda987c-9c08-4ad0-80b7-4afc8d81495e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f6661afc-1aac-4625-9392-9462cf528a04.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/02b4211e-e11a-4e51-8a55-0d3808d32a5c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/27120744-5b6f-4388-b5d9-793f9a39992e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2d7b4dc5-c787-4d1c-9868-3c4b87b05bbd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/78321015-7933-47cb-a58a-153039c6fc51.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/67ff90f6-26fe-4a1c-9a87-a51cae0ec5d5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/850b029a-35e7-411a-affa-59e2cf1f8f51.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/966ff500-4f6c-4d8a-90ef-bbfce56ca84e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5eb2e50c-043c-40f9-9c37-b6b01f264580.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/31797901-7d32-42f0-847b-9a5374738fc8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/498fedc2-4eac-4a95-bb8c-4905e7004d7d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6ef2e33f-949b-43a6-8e44-ac4b39a2d60f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/21f1c9e6-bbaa-4dda-b354-b286b46c29fa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b6769325-1e48-4b5e-a00d-0bf0ad537c21.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b4e75e6d-5797-436e-be94-0005bf4b7e71.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/91a1957d-c17a-47e3-a519-c9e7c3f3836f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/37f3d777-fa4c-4c12-a2e3-e768869420a9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6f3f1176-5214-4c8d-bd9b-a9046bf079ae.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f56f603d-f464-499e-947f-cca3481fb170.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a9549139-a549-45f2-adbb-0151618eb54e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/11db590d-1535-43f3-874f-86ff44bf5cd2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2f0ea3ab-e7b3-42e8-b8b0-4e411cdb16dc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6e8fe34f-46cb-4250-af99-98fcaa68f964.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8608406f-c18e-41fb-b4e1-b40ebaa3c141.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/a4300ec9-a2f6-4502-a036-bede8da61fb6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6c507545-ad17-4454-85d9-8ff61f0e2049.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2049e31a-f9ea-4edb-9d85-ff0291ba6c88.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/667ecd3e-cf2b-402b-9a97-b377e8c98a11.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4e004a01-bd76-4e10-acda-951d4e960676.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/791a11be-576d-4e0a-b1d4-2be9b1e4a4bb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8864b36f-c46f-4864-8d51-e2ebe3acacef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/225958ac-46e4-41ce-a3c5-bcaa526df351.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/82f890b8-9baf-49f5-8a56-39e70acfc554.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/aa7f9bc8-f20a-432b-9732-604cded89e40.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e65659f6-8a07-40cf-825f-c3ffcca6e9a9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1793acf8-4341-47a9-9e2d-9583f2d388b7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/282aa2ad-4c11-4490-b840-4ba30c706619.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4f51c565-196b-488b-812d-f0251137a9aa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f0569f23-b4dd-4445-99e6-31f63703b812.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1c5886ee-923e-45ed-a46e-8ac8072d81ba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/36bc4fde-8558-4e57-a4db-f9ed79c6a1ec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/85f5a597-a49d-4384-b60a-79bf745e827a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/40369fe3-efea-41b5-81cf-b1202c287803.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2a3ba4b1-123f-4c98-8841-526e2705a851.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/be56fc82-3eff-4d1c-add5-829059d2608c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/85b5ed67-b0f6-49ed-a704-364ae7ee263b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/48f8d123-c0a3-4084-90a3-545b3b777d9a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2180ad2c-424c-4eda-97d6-53a62b31a307.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/45ca4d11-e019-424b-b57f-79acc77749cb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ee12d512-160d-4056-b84d-7c7fe4cd39a1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/69d25779-01bd-47bc-8b8f-1fd8cce61090.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8bce88c0-d0dc-45a3-b7db-a2760c9486e0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ac565179-1d5d-448f-aa5d-4458c39709f9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/95fe6c91-b5b6-4d2c-ad03-f8fb2b052c84.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b8d1d451-27b2-4e70-b139-e1058c0a4046.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c270ffd6-8eb5-4fab-b6ed-9cb46f043bc2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/afef51ba-1b8d-451c-9e3b-57e78abb51fa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/05b3720f-a7e6-4f61-950d-b323523e6bcc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e4da4656-d5bf-4ba0-8d78-d9a1cf700224.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e4e5ddce-40b8-4140-81a9-ad3c86d7378f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/23243f16-23e1-46ed-8268-cf6a4f1c19a3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ee5cb5d1-5606-477d-9f8a-5dedf80dc690.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ea1b9405-57b3-47a9-a636-218cbeb58ed4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cdba8008-7764-43e9-9af7-ec08510999ca.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/d1c4e82e-6f1b-488e-907f-6bc235a4c04d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2ec629e8-14af-4cd8-b101-63877bfd3265.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/788d3e9d-92f3-4d28-b2bd-d20f811d0931.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/31736175-c0bf-44e6-bcd9-6bea05857e8a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e2bf9154-97fb-479e-be7d-cc02b796f780.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/298424f8-1124-429a-9235-80989db17516.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/80f8fe40-1e89-4032-8396-3aa238cb9a07.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/370a0801-d21e-469d-acf6-36900ba313a8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7bc4bf59-c73b-441c-8a10-bae5d05c7e62.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3d72f5cd-4cc1-415e-9902-79502959de4a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/41eb9752-326b-45ce-ab12-1b5d2085d24d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/15144fcf-17a8-4ee9-a34f-d635005bbfcd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/62bb5df7-806c-4824-a574-bbe5d119a6ca.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5ac8612c-c527-45d7-a750-85083ac0186c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/60362646-e0a1-4438-9d6f-086c144e14f6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/65999552-0296-477a-b789-4278917cfa23.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/67ff97c3-864b-4d9e-9912-812328b9af7c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5c79d467-c828-4f52-9100-4c08352c2957.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1a54fc17-9251-4e18-8e6c-afbccc7d9123.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/28bfce7e-0f5b-4366-b827-44b6d534cfa6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f2de7167-b0fd-4c08-a717-104d314696d7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/09852649-ee4b-468b-a271-f54ed0cc8f2b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7c3b96d7-57a9-4897-904b-20f464ff0611.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3f743986-0556-48a8-96ad-28e0c3241e0a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f395c848-db1c-4436-b0fc-9d2fbb186062.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/721b7448-1099-42ca-b3ae-83296efd8e09.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9034c683-24d0-4ad2-8bea-6e423040ee9a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bfa66fdc-e5a5-416d-8a78-74201bceb16d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c485a285-d7c9-44a0-9cef-45f6d82de23c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/01dc0951-ec26-4836-bab1-bd936a4b9a37.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a0801235-dda5-45cc-882b-f033303b34c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5c970fe9-4361-409c-a56a-ce005f9936a8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/383f7294-ccec-45f5-ad02-4c506b1efd8a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1b71f5c8-60ed-4c49-a0d2-8e28b5e2d8dc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/74045d72-1738-4a6b-af7f-edda532a43bc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/92385ffe-3e4b-443a-b03a-1e9e08892582.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a5d73d7e-8eb4-4b58-9171-e891070099cb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bffa316b-86df-48ed-86fb-604f9b2bd97c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/027060d2-a4bf-40b5-be83-037a819a5e71.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/d1842dab-7ab4-45fa-ae98-59ed60e77416.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8c1d7c41-669f-404d-aee0-682835e5a06d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/78151d91-113f-4e2c-b0ad-ea8538cb0d13.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f884a219-ae5b-47db-909b-61288cc5826e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d41ff0f8-d90c-4588-b6b3-72175911f7e9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/574e4ca8-6e25-4063-8120-c04f9da440d4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dc4c5a28-17d5-4aea-9995-3e4606f38d62.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a2501a96-9adf-4634-8099-44d360768f7b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d358ce23-3273-4631-86b7-bdcfdc47b5a0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e2027479-51ba-4034-a9a1-11f6451e1a1c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/77689c4e-f860-4a7e-ba73-d3f131b71bb9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/900eee65-a487-4fff-886d-40b0c7aad2f1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/904e648d-3180-4e14-a484-27eb386a3840.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e3e57262-c73a-4ea6-a0bb-fdfcffa27d0a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/748b0a72-754b-47ba-a1be-3cef99c20764.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e144ff2d-25c0-4cd1-a4d3-7bcda751af08.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/73f7546e-417a-423e-abf0-d1e8452db81d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e42962c5-bb48-4f9a-9ccd-fcfa4e80981f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e6f7ea26-9659-4535-974a-8473f13cc295.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/659082ad-7a40-44e3-a9cb-209a41efe6c0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/097a2f7f-7071-4c53-a85c-a893234bb07f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/207ba163-513a-4aae-91bd-c346b6b2c2c7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a247a9e7-2ab6-4646-8d33-03cd9536be8b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9e9fe336-d68f-44fc-877f-45a5b8ddb20c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b912155c-cc70-4d88-b8f7-19d0f45afb53.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/238b7984-a20f-419a-9e2e-a38da2743e53.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/1fab6e4f-e833-440e-bfde-16fe422f3ae8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8760c649-f603-4c13-8992-ca782e357467.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ec0be261-8270-4ffe-ba0c-846541cde5da.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/03c5b31b-a4b3-47e1-accb-c3473d151fcd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/62f4dffa-a582-4065-bb3d-28f3104f84e9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a99829a8-38c5-40e6-b138-0ba302fd3226.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/68b1a0a4-1141-4002-92f7-d7cf686372d7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/9a1b9776-2e50-465a-8218-15012b07d33c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/81abe49a-4ea5-4395-888c-c46eee64c19a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/847166c2-bd16-4174-a546-51a46d65ec26.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/d5c5a683-3c25-429c-a0ac-8760aa9b0737.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b17b4292-ef43-4b4c-8691-04a90886ffe1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c6b24974-7398-4410-992a-e4f96d26debe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ff62e314-602a-470c-9f16-5ec975ddbef6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/c6cf08d9-b290-4ab0-af98-7105a3d59721.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4fe71cf7-a798-4b6b-82a9-69b25927a13e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d8a22c17-e78b-404c-9134-78a45b163c17.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/adc555a3-ed58-4012-8419-c953a715f831.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b67e89b2-313a-42f3-a6d2-8f6571e9b6fe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7df282b4-9f06-453c-98d4-7ba6e1b05013.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ac6fcc72-3d33-4ff9-887d-9575ea9c5cde.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3a5191e6-0b93-416b-b777-a1086ab1e03f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ce4bca75-b2fa-4255-b4b8-fdeff69b0636.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b475a2a1-a31c-4620-9c48-48682fd619eb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/86f5b954-8662-4557-9804-14ab792bfab5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/3d2db559-e928-4726-b9ea-ae97c6164f97.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ce5d193a-e916-4957-9f96-8641113cd753.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/90df1a84-7dee-4e6d-a16b-0c530a951217.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/689a02c1-6e44-49c4-919b-8d5234f9732b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9b5a0635-48bd-4f91-ba43-9640ebc168f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/725b62cb-bec8-4e30-8a5f-adc04e096bf5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/08142e1c-e76d-46e1-bd92-7118a6ff4746.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/970aefd9-d34f-4660-b088-95bf9eb26b6e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fcaa2c39-08a7-40d5-9217-a75db54d8ee8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6dae32ae-a7e1-4da1-ad3d-f889afddf94a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dbf46d4e-026f-47fb-a6aa-b152007c5592.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/5814e85c-f953-4d2b-8f98-c11f910711f8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b5fc840d-002e-403d-901e-31886d7db81e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c837c493-6023-49d3-96fb-0637fa95aeb1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/036d1142-8dec-4472-a941-cbe022843650.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/396eabdd-28a3-4477-b5c9-c48843908922.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/448c0fc2-974f-4f6e-8e14-a76e73834e65.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e180ec90-d8c0-487e-aa21-6bb18d333193.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/33f5329c-eb96-4754-8be9-4833cbe89e24.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/eba11992-391e-45d8-bf8f-0704966f397e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9965b042-24aa-4501-89fc-d0519edd00dd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/616c4bc9-9e5f-408d-ad75-287ead34bea2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/73a6f590-7289-49f6-a54f-3399634eb41d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/2b6e7d9f-4322-48e6-af24-35c0e28cfe81.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/39398d24-6f80-47ac-bcd2-3073d1dbd6c0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/590864bc-1973-40a4-ac19-e9886941c667.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a406a2ae-c728-4c45-bdba-5e4fecf021cd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bb120f2d-d663-4a2b-9d8c-89ca8944c812.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cac9cbe8-926a-4d68-be76-d8aa85b99e56.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4c933775-d418-436e-89c7-e07e51348c29.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/941c4c89-44c7-4b66-9b70-d3fc92470f24.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0ec82a05-14d0-4d84-822b-7361c44e8cd9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ad0236b1-7d47-44da-81ee-c8712c991c6b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a4ac3475-0dfd-4bfc-8032-51a7174e6ddf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/97d1c02b-4213-4cf1-854f-1f38ee856d35.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/77d7898e-187f-4b94-976d-2390082b8d41.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b5fe5902-3533-4df9-9461-ba94a070c8d0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bcbc5eed-acf3-410e-944f-0f3c27f00763.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fc4774bf-a601-43b1-b587-d08e22e9a2ba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/c1ec2e4b-a0ab-4359-a029-f401eadeca8b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/f5ad77fa-9f7b-4819-a6f4-73998aeb4494.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cb484a4d-70fd-40c9-8128-f9e27f9ab19d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ddc5c9a6-d383-4696-8d09-073b242417b1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/df4fa833-787c-45a3-aa4d-1de16999248d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/45e8434c-5597-420e-acae-a942a264afec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a4fccba9-49d5-42d5-950a-f2d865cd5ebb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7ce04665-129f-4e9b-8a9f-135a67e45527.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a1f4055b-21f9-4166-9282-0cb7f49decd8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b84020ff-e504-4704-8a93-0c459f871044.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e76fa0ca-438c-4ba0-af7f-6adcd6f4d8ac.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f7283138-d9d1-42d0-b528-c74c6a440536.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/43955637-885e-4e73-8355-3c0d71019d60.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c129896a-06cc-491b-bb92-79cf604c71cf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3d666829-4fe5-4dce-bdb4-6356a2b0744f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2d91ca10-31ec-442d-b1fe-5e50615c46ce.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/acf28402-ac08-4880-a036-d80de2698046.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/1358cd6f-164f-456e-8dee-93dac9586d60.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/0b12e0b4-c3eb-48ef-9141-0d3c212e4de1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/47f3f624-0ebd-4875-95b0-ae98b1714616.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6a07806b-5849-427d-91a9-22a116cde367.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ac7cabf0-ff30-4728-931a-d18537825c65.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/95d7aa33-5d03-4560-ab20-39622e99da19.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4078c070-7039-4909-a178-6b8569b0f926.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c43507b5-7a20-4f70-b031-f0a728d41f33.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/439b7da8-de11-47e5-bfe0-47c2a5042517.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/890a8e54-884f-4d84-89b2-8152b03fc8a3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a6e4e17d-12b8-4c70-b4ec-7c0f96bf45e7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a34c79e5-83cd-4395-a577-2e79f4f766ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7e2acfb6-bccd-4010-b68a-03a5c32fee99.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/82b345c2-daa7-4122-b8e1-59f80ed017f1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/46d68fc7-52ac-4e0d-90ea-3143064501bb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e015806c-2164-4986-9278-e79f00fa5409.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/886f523e-7553-4a09-acec-f685e4eb21da.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b68a92e2-3e31-4c8a-81eb-85202954ff14.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/36b215fb-536f-4665-ba33-c106d0b49ea9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1d488300-3d48-4cb8-95d7-c2b116379901.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b7c9e87d-9224-4216-a027-ca02a5cff4df.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b9b9b0ee-ee23-4ae8-b5ff-5b842c086f82.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2f8af95e-705e-4940-880d-99afd4130b7f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ca538903-30e1-4cec-a2f4-c137ce8aca0c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3a6a2c60-7b2c-4d87-8a42-6270cefe717d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ccc08e42-9bd8-405b-a070-c6a9ac25f36a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6bc0da35-9082-4d24-9fff-6fc4dacf6af0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2587879e-2dd1-4bc1-b6e9-eba22aba684d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ab9385b1-6688-43f2-b7c2-8f0e18891847.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d22b4dd0-056a-4e21-9400-50b30945a816.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/66cde40d-d1f7-491a-98b2-62c0cd28fc09.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bf2b6c1e-9d79-4f05-9665-0fd04c775dff.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/05d2388e-1845-4c30-b0f7-9509029a462c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bea41ec4-3b45-4ea9-bf77-5b2cdc9642c7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f166170b-2468-49c2-9ff9-988a13f82b5d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/daa6bdf7-31a0-4dcd-8298-949ef0917f46.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f43a3f21-e918-42d4-9584-911bb9737ef4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/28b9ac0c-0a25-4cbf-b2ee-5f7bc29d9a49.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0a1d4739-28b8-4877-827a-1ecd0bb799e9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ef70fcb3-162a-4bea-8248-eccd9cb8078c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dcb72ea9-e42e-4ec4-a82c-838b7ed7c86d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/a987a351-01ac-4d81-a9c9-702940c7d34b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/40b37e9b-699c-48e0-904c-86f4c6dcce1a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ad6a2b9a-ca1d-40c1-8f7f-e0b21aa39e94.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a880360c-d49d-4b82-81b8-f84ed3dc1068.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1964679c-42fa-43ba-bb78-4a5a2b3036ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/546d7a98-f022-4c33-82af-bb99c8827d2e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d14de7fa-9438-40d3-b3f2-a1f83a857bdc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/766e5bad-210c-450b-8e74-b6578bbca609.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e54e8126-7e59-43b1-b98f-334776e3e375.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/37a8ab2e-6b5c-4bc4-b10c-9622ec5409d2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7f3e3c7a-89ff-44ce-96e9-aa4cb319bde1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/de56b251-ad8b-4c91-b795-d87302518fda.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7c7d2341-6beb-470b-aab4-948e189b11d0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cd9523cd-499a-4368-ac90-e82dbcce4028.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/edf907f4-7ca0-4d77-9d77-2b19fa077a9a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/093fcc64-6117-4796-9ef4-c2c26fd41b82.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3b64e53d-c1fa-4ee5-a2ea-976f2280fa10.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/247737df-e136-4057-8c20-40494a2f872f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/86ca54e1-2a18-4be3-95c2-cdcc1d03e161.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/4056a81f-568c-45cf-bdfd-0bbae88bbe7c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b2a086ef-ead8-426a-b6d1-f041a7df77ab.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/590755ec-cb4c-4c73-bbe9-4a43985d8ad0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7a990850-10a4-4873-9dc3-6968e6c8668f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/235d8554-63db-49bd-ab9d-214dead28b13.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dc5fbb23-c148-4e85-a353-994ddb75f5aa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4c848d6c-9c88-4af8-a05e-392cd7214701.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5d8c2fc9-6fab-42dc-8098-468c86180afc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6e449549-a873-434b-aacc-50fc0596bdb7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f3f2ebfb-6086-4f35-a2df-ced0568722a3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/15388e1f-2e59-49a4-a637-49bcfd89111f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7728ad2c-3b26-455e-9efc-46b4688092ff.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2fa4dac8-a2d3-474c-8f81-08376cc88758.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e33ab167-90e1-4e1e-9d7e-d434392b03f8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/517f1779-a929-45f1-8ff3-097fedbde27c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b4891e43-4d22-4147-8bc8-27173f8c26af.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ce073276-f575-4af4-8f11-7f2005e1c983.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/de3a37ba-55e2-43b5-aa30-4d44b5a924c3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2dc1a519-24d1-45f1-a667-0f4d42b86fd8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d6f5f422-b63f-4aa1-a786-7439c0cba1d3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/07948a42-bca2-47f1-92b3-3d035c1c985c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/5d28342c-f613-4213-a901-9cc918fd2cc2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/73d88dbb-ade2-4517-9374-aae8925c8eee.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/9ba0f651-a5f5-4a28-b004-61c9c2f1eb27.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/235ec545-53da-46a4-aec7-6fadb8f2fdbb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/1b93f266-2715-44e3-82f7-718cc78bb787.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/275e6260-e735-46cb-a4bf-802e14c74561.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8460d8a2-af13-495e-a07d-dec9a01fadec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d678858b-8755-4ca4-b851-ffbcb720e30e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/786c4bdb-bd7f-4083-8038-12c23b368c1a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f5948b57-54fb-41eb-b0d1-49ee203c9dbf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6b6042aa-51d1-4317-8101-0e9dadc1de87.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/91e1b418-1109-4730-b315-cd72041739d7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ada2a759-27e2-4af2-909e-b78ea24c7f2a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e740916a-c73a-4857-8a47-83b86ab2cce4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7055cdf1-d860-4ba7-b20a-a5b6ee4a7ce3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a296c12b-5ae5-4752-90d2-e9ca01f04ff4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/da687ff9-87e4-4732-999a-90818f8c0c76.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/73c7a430-2144-4328-91f7-d15f1d46c508.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d52b1c4a-819f-4a30-afd2-fbaf362675d5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/61a3e892-8f2a-4f9b-9250-07b6eec415b2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/45d0413f-49c7-4db9-bd5a-64caf7d18930.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0e23aab8-8951-41f9-9bc0-a36963dc300f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/16f838cd-f6fd-4561-881c-07189dd409c7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/64b42275-1b44-477b-bf78-69ccc521a31c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d135bd10-6997-4fee-b8f7-5f1d8ebd1be4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fc19336e-2193-45b1-baba-ea6cae034fb1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7021a782-2008-47ca-ab7d-04f677480b7a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/161a78af-bcc6-401d-b426-e21522c59ffb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1dd7b81c-5703-48c4-a923-0dd1d32bc6b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/aba17759-497e-4613-97d5-7bb45475ca72.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b1e93783-f297-4325-9c63-2c3a49ff9519.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ba74b431-dbb5-48b3-a576-064cd7eb1cd6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/e1cca34e-869b-4779-9c94-5c1597042c3a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0b82dd36-1e5e-49b3-ae91-a9da07c73cba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1863ca9c-2d4f-4ade-a11b-296a541d9391.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/18f55b0d-1582-4e1d-b19d-47dc19e09df3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/093e3862-42e8-445f-9926-52d153396585.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5211dfd1-0c6b-4a1f-9aed-6eb9d41f453e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/718f1ba8-11e5-4557-84b5-00e530ca2c90.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1fed0a6e-5572-43c7-87cc-4a0f9d8c2dcc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/909be7ad-4d6a-4c8c-9b39-c66785db8287.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ae85d3c8-f869-4443-a9ce-257410b3d54c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b57241c0-b160-4ebb-a1c6-a3477929510b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ed761675-0621-4c79-99ab-111d649f2c1b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3cad3c99-f7a6-43e9-8113-37c1703874de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/967c32b8-485e-4e66-a936-939dd2cadab1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d01900f5-882c-401f-bc75-f202d966276a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/52c5bee4-92a2-4d64-951b-5eff97a0ac77.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2afb8bc6-97ba-4b54-a99a-0c243e46a9ce.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3c8a29d3-5591-4361-acc2-d537e4ded14f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/aea02671-e9e7-46c0-b583-673a28c6f98e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/0abe4222-8fce-451b-965b-4e816687724a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/140bb2a9-beb5-4ece-979b-9f56f6ee7a1d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/574a508f-702d-4e37-8fc4-af4e4570c279.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8ceb5b33-03cd-41f8-93cd-a9de50bb4a77.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/976fa66a-4a10-4242-b0ce-a41d046f083e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/25868b88-14fd-455f-b42f-422ee07c8cc6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/0e98a424-b280-49d2-adb3-b67dd4cebd77.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/47a33ec0-c219-4fb7-8504-99114e3bd991.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/297c9873-fec1-4f66-86e4-37e91be4785a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ac6b724c-323f-4fc1-80e4-cdbd7dd4a2ec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/a806dd2b-3b85-4282-9ea1-06176bfa722c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/fc5873ad-94d2-43a9-b0cd-96f95a946be2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7e800e9c-0044-496f-b44f-9cf8cd2cf9a4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/51ab5a5e-a62b-4ae6-aa76-9bd30ca1eaef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/6f3f4620-ffef-4c35-83c1-6aa3ee43fa27.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/011313d8-206b-4c7c-84de-656d5d812a95.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/89a5b5a3-8802-44a4-b42e-34c23506fef6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9f1f9321-4abe-4f7a-a43f-f8b5f2913d1f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/aba808b9-b44c-476b-8a33-4dea8ace06ab.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a8f428c3-5075-4084-b34e-7733ef3d1365.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/fde4d3a7-2d8b-4b75-99db-cee4c1297d35.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/51733d95-14f6-4429-8eba-9801256cae4f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/532864d9-472f-46a6-af6b-57103049364a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ae3c1d09-af4f-49f3-87df-0ab55eddfce5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c469c01f-d7d9-40f0-8f26-aa5af559c971.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/14468491-e03e-4062-a696-a720e36463c5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/5dc09583-25f6-4e54-a40f-9dc36043383c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/739d9b40-a53f-424d-91d0-22ba9167dc9a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/552e56f6-d142-4011-89d1-93dbf5a9e0ad.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1e9da592-9700-4737-adae-786028ea089e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0aea257a-fec3-4403-a421-e02bc98614ec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4a7644d6-568a-46c9-85f6-78d27e0d93c6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5db0cc74-686b-416c-8780-986a2e7b319b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/36f7a617-fbae-47d1-ab62-6000808b0283.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0e75721c-d7de-4882-9cf1-bfe5fc2d08fc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3167be5e-b209-43ae-ada8-17f18928220d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9a21809c-cfbb-4a53-8904-6da33c380d3f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/93b92aec-7712-4565-96d6-5dcef631f15a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ffa16223-2cb5-415e-944a-88da03779417.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/baa9809e-a9d1-4beb-8910-97e10b6e12f5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0ec4f366-1d18-4f52-b563-88ac72dfd62d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/4d993327-7533-4392-8fe1-ec1d74d5b5c6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/d20a0116-39d3-4ea7-9cf1-98a908bec458.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5a953153-5035-472c-a9cb-1d1978bef834.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f6ac6644-a48e-48b3-9146-7ad303f55564.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e832b0c3-f688-4718-aa44-83eacd9c8dc1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0ad08f79-634c-474f-a85f-dc62aea8cafd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5a3f1dd1-56a1-4163-869c-13fb9b7a44e6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c3cd5a75-ec8c-48e5-b61e-166f61ad9d5b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4da38d24-f28c-41bf-855f-0e5bf932a4b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a9238ae2-8bdf-49cf-aa8f-1e3517cc2677.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/49eab5dc-ea17-43ef-bd9a-93cc64e363bd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/38e43eb1-f2b8-4fde-883f-837589288b09.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/86bf8bbc-a77f-43fb-ad9b-dcebe8fc039d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/5da524ad-a602-4312-8374-5a39c52c8992.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9caa6614-6cf2-4222-be28-af00fd3c015d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/da2aef90-66f5-4416-9f26-c5e166386620.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e1ccc784-ac24-4b56-b049-7716383ef144.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8e75f0f7-5029-4db1-9c65-43f7e9cffcfd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d86c7551-331a-444f-9697-b80fa700b975.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9430b5b8-de1e-47fd-8d68-1aa7c3777b41.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4f82e5be-c6e2-4b76-ac5c-0e330975e718.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f7b5b0eb-d4f1-42a7-b4c2-06d979264f3a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8eb92581-7e12-40ac-bb57-e76494e5ffff.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/05372500-b8cb-4a38-a995-3f76e1519b63.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/642644f5-d9bb-4fae-858c-c82529ef2281.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/91007dc0-7f20-4f4c-93ef-116a453ae44c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bdffeee3-1bb2-4459-92a1-9a1366325c9d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b1f34d54-f8e9-4679-aaf0-65239d4b963f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/604df127-be72-4f14-852f-199401266110.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2372c410-7073-4144-bd10-0b4550f33d8c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bb807084-b678-4539-9f59-25f28ee83cca.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d4357417-62d1-4482-9796-cc1e94db8292.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/53bbd2d5-d895-44f2-8ed8-e827e7094016.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/63de5e2d-c687-494c-9ba6-396c37f33c19.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/25fa6063-7a2e-4c4b-b6d5-eb7e4c51efd9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3578c8df-f2b7-41cb-a4b9-25acfe4bdfbb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/635bd365-5cc5-4f27-bf3b-ff7127e8803d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/97303b3f-7ee4-42f3-8d89-33caabeb53cf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9c6d13d7-cd12-4eda-b9e8-1ef91355128e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c938f1c3-8f1b-46f2-bd09-436463471bf2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fd302406-599b-47b6-a232-ee64bfecf268.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f35fdd22-f55f-47c7-bed3-2d399d467cc9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/58a76702-cecc-4803-8cf2-1289faa04422.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/aa0973ce-caee-4693-a5ee-aacd00817fe8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/97184506-b3a8-437d-96f1-1a826be0e8bf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b1fb89db-b621-4ac8-8ca2-d75893b235de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/009378eb-7b4d-4bfc-b02f-5bbd5f2a5e34.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/22e2f7ed-79d8-46b6-a6d2-07ea6fdd426c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bd670bcd-d57f-4412-a086-df6e1c9602b1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6d22ce4d-b741-44a3-a69d-b57fa40971d0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cd801324-7c9c-44a6-8db0-7e2bc08ab4e7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/48923df4-99d6-4f80-8f42-c3769b6ef8fb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6efe920f-5fc0-44f7-8018-736f18513187.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e09aa7a4-c465-45aa-939f-d6157c48a620.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/4f82f6da-b92f-405c-9db5-cfefb1ef6c09.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d904fc09-3e25-41c7-baa4-982d2cc17d50.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/599cbe44-1099-4167-8f11-4f3552730d02.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/080f7d8c-a822-474c-8172-d561cb60ac4a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1f4024a5-01f3-40a8-847d-833b6f1eb031.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/edd04f58-0bc1-4b66-8241-370a62a4bc1d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/24d47519-a7b5-4f5a-a372-261dc742129f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/eb0d60f4-5eaf-423c-a156-1710b3a9347a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/0202cb22-8ea4-40d7-aacd-b78e7034e4da.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f9f0b01e-2bc0-449b-8d8f-3c01dacf5ead.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2da157e5-1378-4e7f-9a20-0a4b08137792.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b6276402-badc-4a94-bb54-0b0300e227f4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ba9c0f8d-f544-4242-8c72-8e0376a65c40.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fcb7aa85-7054-4728-92ec-6de96414db32.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3703c6d9-8ec3-4829-a94b-78b58fb1d4f3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e8e8024a-76fa-4a45-a726-52a647d47ffc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/8eebe05d-78c8-42bb-ae6c-74078ea12744.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8409e83b-29f4-46f7-b8db-32494ef0c19d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6cee213b-1602-4121-af19-4c5674c8a733.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/15a9167d-e059-4445-a944-f7923119387a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8fa5c525-e524-4a86-bd85-fc74607d6c24.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/62ea0111-489c-405d-831c-1304e0a6b69c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/74fedbbd-9a6e-4ca5-8f45-fb61b478bdbf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/75d903ee-7add-43c1-86fe-ca8169afa3b6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2fd33636-aae9-42c1-aafb-9703305309ad.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/012c4538-1bc5-4f82-a9cd-2196fa3ee42c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2016c185-c4c8-459e-9890-1206535817c5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8a8e6978-6423-4f10-b230-77be9b0816a0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bad631ec-1763-4769-93f6-f6030b4f0db0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e565c556-2772-4c1e-bf40-250807171030.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1daa08ff-2a93-4001-9067-ee289c398843.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/26cdab1f-3582-4974-8c02-f131a9405c07.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cd65863a-bfe6-4c1e-a600-366ff1d5fa50.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/420cfb58-8465-4377-b5fb-725f77925389.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3a723adb-2f23-4e58-bf63-3eb79da03b37.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f58c89bc-e31c-4357-8be4-247bc4b14246.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6be654ff-9776-4de8-8320-d47c05fa63f6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ef8d67b5-ad58-4663-9e33-670521745816.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e89b43d8-9085-445e-9dea-ee00115c1679.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8d37a18b-6bbc-4924-9142-5fcddc334b7b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8261b580-ffb0-44c1-b643-8b8d265c7f81.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8d5acecf-d411-4a41-aafa-bc1a2ee90fd2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c782115a-24f3-46c8-a37d-148a08611a4c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1e112f34-3217-4522-b575-2c9d7185d5bf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f55c357d-a148-44b5-bcf2-61f47713fbd8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5b6f6a76-39a7-4a6e-b9e2-d44f3e23480b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/96dfdd38-7929-4c6f-be04-856fe3fbb804.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/85a47468-33b2-48f5-ad1d-44c6c1f2b5b1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/67424c6d-0950-45bd-ba11-1804a4a6bed9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3a4d4368-8c20-4290-832b-c6c762a17d34.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/03f35fb8-18dc-4793-808b-9faf3fb27e99.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/eac28ccc-25df-44f8-9736-a225da434c4c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e0e3c61c-89e2-4e66-99bd-db74a1d0b0d0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/50fb962d-707c-40fe-9a6a-ace057f6a72e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/975d9a0f-4584-4490-bd1d-fa979d45152d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ba35d236-bbe8-43d2-a982-9e76a67bd1d7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c1c9f428-5187-4c2c-8b07-3e4b1b5433bd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6437973f-48fd-4cd8-a621-51c47df54d69.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6a30b4e6-2f71-4c9b-b910-74a2dad8fb52.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b1226be9-f07a-4275-88af-7b353ffe8000.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/69459d23-2db9-4b52-ae7b-669afb4cad2c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9a6296f4-05f1-4f09-9dbf-199ef2bca620.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1999d7ef-824e-4a1e-91d9-33c8867ac415.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/010e7f35-d988-4b34-85c1-207e8ae21a35.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/16c42007-3283-4207-a332-e19dad6898b3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f878b1bc-fb91-4068-a82d-d8ac9b396f52.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/51bde983-4f79-44fd-ba16-85671f6de742.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fedf9c0d-35d7-41e7-98d7-cffb828abfd1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/8771f0f5-3b84-4df1-9207-882abd37fa4a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/644f32af-af67-4bb6-ac1e-99bdd28f6d3e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dd3f657a-727f-48a9-9ae9-e20ee3279ae0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/777a1df2-6ad7-45f1-966a-6efe823a246f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/905650d9-36b4-439a-aefe-8b3106da8cfe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/9a58016b-c7fd-4e26-b760-e44e624e9059.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b74beac5-90f3-4c3e-bee8-97fbcc4ad4fd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/255ba3fb-0d8b-40b8-860b-6012d29dacaf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/123fdcd1-c928-4469-9691-6a0c0c98f236.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e0177875-e4b5-470a-9cb8-5e7b8920dbe3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/73ba454c-bed0-4e07-9d63-84941e7b16e8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/76015b08-6576-496f-b206-3dedfa2aed2d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/702b1744-f150-4afc-8d72-2efa5021934e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/a75b9b5c-8850-444c-966a-39fa42b149de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0dc9034a-b327-4be5-ac19-43bc66d2355f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d5dda165-e5ed-4763-9671-09bc66fbad6e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/93963c0c-b090-4cae-9c3f-403000f6b797.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b30c611c-82a1-4eed-910c-aa121fad9b88.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/e7fe1100-5500-481c-b43d-a10ace5eb0e9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9904ecd5-c95c-49f8-8526-5ed390c7167e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/cb065642-d466-49bc-8cd0-98aa51439187.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ac85ee09-63b9-49ad-8630-a4919cd8b449.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/432d567e-7734-4848-ba5f-9ffc032e5118.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bc909d9a-3d8f-444c-874a-3f6cafce090a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fd6c5765-f0b9-45ea-a20a-a21c3f65aa56.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bf214719-7b5c-4e8b-9d05-1ff8cb66b6fc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/60245306-add5-4fa2-8644-dec4efb34a07.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/23bb9917-b7d1-4bfa-acda-6da6dabee69f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ff3d7a64-5267-4c90-a743-4f255f2ac385.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bc4263b4-145a-48a0-a748-a8fa82f5750e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0a0c8e71-f560-43d1-b588-6537bdc73360.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4b008e5b-a937-4f94-b163-30bd8aa12133.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cca8da2c-7963-4f00-a9a5-699e4285ad9d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a5689f13-6b80-4e00-a52a-eab05b9dfdbb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/da300cc7-2080-4eb7-8ad1-441460c0a87f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9ac4a385-5aa9-45e6-b425-eda408738f85.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3545a1b5-a9ce-42db-9b8a-8c686cd94113.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/97742450-51cf-4d02-91cd-3ce5a0ffcdd6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a8e404c3-0865-4090-8ec8-5aacdf8cf898.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ed2ca6f7-4ebf-4567-aa7c-ab71e155599d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fd794a7d-63dd-4a81-826d-da5f00abcbf7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8ca68c44-4547-413f-97ca-3ead3fa3ccb2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1df35e0c-5731-4ab9-83e0-81243aabec0b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a4b52953-d90c-4a60-baaa-1bd02ff7a4de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c5175417-4461-4a37-ac10-931937b02dc8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ef0907b4-3863-40d3-b536-0aed43182c00.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1cf39c16-ce7e-4f24-8fcf-ec8c8e0e6e49.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6d43f45d-4782-47db-922e-0c679e700319.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7ebce207-f326-4d56-a7eb-dc51e40b6a8c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9d091118-5cfc-4816-b23b-87603a6c83f6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2557d837-e6d0-42ac-be4d-3f52416d9871.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6dd18194-36ba-4138-a1b3-4bd0b2c5e290.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0f5e0de3-c834-4845-9691-c62a4c6729e1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/301086a3-4ca3-44b8-b311-e13fd89efd07.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/cbfbe8b9-37e1-4664-b126-61c20fc76ef7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2a6b208f-2abf-43d7-94de-2a41d9550095.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/28c2eebc-eb33-4bba-aa81-528cbf96c6e0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/43bee8c1-fecb-4adc-873b-34853fc9abe0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a0953e9d-33fb-4b97-b11e-ddd1ad856db6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/590a7aa6-2c3c-4f0c-bad2-67046d77b829.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/89701fac-9c26-443e-9ca2-289020eec4f1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e40326c9-a487-4187-b8a1-08da5f54d875.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f219eba1-42cc-4df4-b1a5-71dd7b54d2c1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f259b3ca-d883-4226-a07f-cf3f2e7f7781.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/067b20b0-3110-48e8-b0eb-6976bacad805.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/6c3635ef-15a2-4e2c-ae44-4be10ef55a65.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fc7aa0d3-c890-4b18-9cf4-b8fb2d68c18e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/637e0c00-c478-41d0-833b-755000c923d0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/987db898-54f6-4a96-8b4f-a56aa09fc2b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1ecc96a8-9ad1-443f-aa85-6f442d0a6671.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/44e8dcd1-a107-46f7-92a3-d29d16bd77ac.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2da56712-8671-471d-895e-ee676d35c42e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/46ccdf6c-00c4-45a6-a88d-c40c9273cd41.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d8e73696-916b-4372-8327-b90cd2649c24.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b6d54bfb-f417-45ff-a2d6-9fefdbb802bc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a7361281-5eee-481c-8b73-dce033f7948b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/07305940-f0a0-4f8d-bb54-c2730d4ed179.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/84729649-a9ce-48cb-a221-0f0f940192ce.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1b3971d9-75bc-45c7-b912-331b26497987.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bd6adaef-05a5-4763-88bb-194bbd15bdbe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e0c350d4-5371-4a54-abd3-c65ecf9967b1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/12cb499e-567a-4bf3-86c8-102e15c1a59d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/22fe184c-df85-465e-89b6-d9b8f921c1c2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a2a9a25a-3161-4a53-90cf-170f5b853296.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/041e743f-a543-4c62-a1ba-cca7998b4616.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ec74dd1f-9cea-455f-8258-166ff9b31f71.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d55f92e7-f4d7-4109-bfab-0f58998b269e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/18e16ee4-5e2f-404c-a03b-4ffd1cd03efd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/476ab717-12eb-4963-975f-235437723ece.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bbbf737c-4a3d-4900-a18d-60629d3f519f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3bdf075a-c9dc-4537-9621-7fa05f0be734.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fd662022-4935-48e5-8845-1025513826fe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8278df7b-db9d-46ab-9b78-a919dd8f96c1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/9d17c355-ad25-4197-bd9c-40d5ed63d256.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3f1187ea-c5c4-471f-be40-e12721351d9b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ebaa6fca-d61a-4cd0-9d01-8108b1e022de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/483116f6-4006-4f3c-90d9-59e2593a21d8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2cb644b0-bfcf-44e4-95c7-2d6f3711d644.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/96124590-74e2-408e-ab44-aa96e4174ff1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/98af419e-b251-462f-bedf-1882cdf8bc9d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/af7a9335-1ab0-461a-93a1-30a0f99ef953.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c0b73d4f-d2a9-487c-8ef9-d91f576d0564.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c310a076-e452-417f-9ac2-e5820a2041c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/91ab8cc0-db33-4a93-9ad7-938f1c76a95b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/820ef29d-f585-4f65-bee0-d0331c833f6c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/87487451-aef0-4b5f-80ac-71d21eebd88f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cea1ac80-fb29-43d5-b254-3498dd47c9b2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ec2aac2b-38e6-4143-bd18-292d503437c2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ad1d557b-19d6-45ff-b36c-ed5bdb39174f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3ad09db4-c9f3-449d-a3b2-d53506ee1032.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/77350e6b-b31a-4d87-8e0e-b9689f879203.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/76815316-e678-432b-b971-a40766c04112.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ecbf42ce-b84c-497b-b289-e2168f2a7181.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fe9b41ae-a2f4-42a0-acd7-f4f7cbabcba3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/138fc0de-a5cc-45c2-ba96-b4eaf42ddda0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8ea25949-142b-43ca-b426-483631d9b5a0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/751c0a78-4f03-4379-8396-acc5cbed2e69.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a3a17900-8ead-4e71-9cac-446e79d3652b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c24897dc-f919-4b27-a504-06fbaafa77b8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/78575da9-2b8e-40db-a18a-6829e74316e2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/e1df8dce-f5ea-4d82-ba7c-04ff50e043a4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ec3c7e97-3663-4f32-a964-630a13f16dd2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0585a9a2-5c8b-4775-9cf0-f847bdd3fa51.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5b2ad02c-6c28-41f3-9117-f132176645b9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c17b99ab-f38c-44e5-afd4-21047ca980ab.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dc6d93b6-b1ba-4c6a-a9e5-c31b8d9ec018.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1d3d1a35-066e-4d03-b752-51708f946641.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7d4608c4-43d7-4b0f-a8a1-f9b2ef70db46.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/85003cf1-ff33-45ef-9e98-948220375a61.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/30c2aba2-6702-4773-8b8e-e6aa9dda340e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c63023eb-92c3-4de4-b058-3906cc362997.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/23bea72f-3279-4609-96fe-60ac99dfb9dd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0324ae17-276f-4538-8dce-0d41cff429eb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/788f8979-de73-4d88-ab8e-a4a3ac190228.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6eee01c5-882f-487e-92d9-c658f4d23ec5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a074d5a0-18f8-40d3-9f93-8abdd3eb9ea8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/61e523a7-d24e-4840-b60e-8ba23f7af716.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a76fe2cf-cb87-4334-baf1-0609669daa2e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6755f38f-add0-4470-af00-d70a1c06a0fd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ecbe9013-467d-4e75-a34f-707fc57ec620.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/93d3aeae-d979-48bd-9a36-f6fe7f73f401.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/33621c4c-f4ef-4d1a-92be-028609f094be.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/034dcde5-6b5c-4606-af1e-77c446435558.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bd606688-2164-4e0b-aa26-18460b63bbf6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5eab1da2-e57b-410c-9279-358e4a80d8d7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/99a7cc54-74d7-4c2d-a691-f09207e3a6e4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9f91911f-cc29-41b1-84bb-df62bf17c21e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c6fa0582-d227-4de8-8518-f2e7acc46cf4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6bdad341-9193-4ad2-9707-6826e0546a8e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/a0681938-32c1-458a-a3de-89eb06b8033f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6efab450-a725-45d0-beef-24d00c71b56e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fa706566-06fb-42fb-9527-aadf0c1560ee.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f8f644c5-3910-4f4a-bb3a-30af95176d62.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/14976fe5-b9b8-43d1-aad2-da63fa880bf4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/de9cc06d-7ad9-4dc1-b45e-0bc47ec5e178.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a1da6570-2a7c-4fd5-988e-6aaa047fc951.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/394af6f1-d38d-4a66-bca6-1ee0aed085c4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/714f92cd-c329-4e7c-8015-c88c100bd875.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/16c91dd1-8ab7-4d75-8448-ded6195b66bb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5041de5e-c48c-45df-a5a4-b21b854843d9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c6081361-454a-4b1c-b40f-9b92f0ed0a49.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/83868e08-d8fb-4e82-a209-15363e534408.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8906d217-9fa7-40d7-96c6-abfc42728dc6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/84594d58-3221-4897-a5ac-045eeb0493e2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b3388edc-b43a-4370-a46e-96913812aeaf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/7ec4f13d-4e24-4835-a39f-543b2246cfa2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/1c8d9755-a680-40f3-ab53-edc75be814ee.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4a161087-516d-41b9-b750-69369f6a73dd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/cd61ccaa-9557-43e4-9512-62324507c3c5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/564c9272-c83b-4c4b-8fc9-9b28894ee46b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8769e68d-e9e0-48b5-aaad-c6cdc9ecead5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e738ac5e-d59c-400f-952e-7960b3dc9df5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d93bf756-6660-4e34-905a-bcbcaff23008.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/816d0036-d66f-45d2-b4a5-028b75cd80fb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e7d91890-094d-4767-b4ea-368050c8e7b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/308e6722-eb28-42c4-a4ee-c8393078d25e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/da2f7c05-1d39-4fce-94a4-3617f2d0fba0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/52900cdf-6f3f-4ef7-bca9-9c0603a16838.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/736efd31-7a75-4a86-8731-a4fae1161940.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/0c87e43c-3c8b-49dc-8524-cd70de8daa5e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/075938eb-c918-44b5-8989-6a4e172ae935.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/af303488-3539-4ba1-9425-0a95e165d734.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/76f102c8-f6d4-490a-919b-147065ad9db2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/16a93f99-0b55-4fee-8088-40dbdeda9a1a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5714792b-6e1b-4ff2-b5aa-a36a4cc3edbf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/339c7b21-ad18-4ca7-ac46-62549a835b73.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/f3da304e-ff01-4829-8ae9-33a7a1bd75f1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/f9042a8b-9d63-4abc-9096-0280283e0f90.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/09ada4bd-92b5-4a4d-bc50-3f027e5f5c47.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5e731a70-5182-4ff0-bfb6-0023ad57dc25.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f58f4915-887e-4310-a2b8-d4aa269e57d5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d114f4e8-9c4e-47bb-9392-a85ee609f6ea.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c8905df2-d009-4aa6-bc90-d5412cc9b750.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/abf05eaa-e1a8-439e-bb09-ecce34ba91f9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/74085e86-e6f8-489f-b091-a8867917b950.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3b3b17e4-6639-47fe-883f-2602854e224b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4d531fe5-0b46-41c2-829a-aebe906ff548.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/037b5b2d-deb4-4f7a-87b5-629e69a2ce72.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b6de9e44-ef04-4cd6-9700-c038ad245431.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a6d3d37b-dead-4371-ae1c-8aa3b92b575d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/49f3f253-a669-4ff1-9790-2ab9eefb57a5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/39deb035-a5af-4e89-b01c-d7922c51b5e6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ea95b111-0ccf-4548-8fcb-02cff134ec5c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/10468f35-61d2-4fa9-bd38-7e66ef679d58.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a450aeff-974c-497d-9478-ef7545aa1f86.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/34b7ca3b-5e0d-4f0e-a463-0b578432eee7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/48200688-a1bd-45a0-a13d-eb5fffc875f7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a5d33c4b-3a42-4492-a4cc-5489e1a4650f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1ff39c16-998e-4430-9dfb-697f512460c7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/86ce6a1a-8b75-4074-95de-ee7bb994de6b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e7a0a185-1a7c-47ff-ad3f-fe406752e335.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/d1f5c45a-ad56-45e6-bdb7-64fdfebd01b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/0206b9ec-78b0-41f6-a255-21c04c967d21.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a5d7c250-7270-4612-bccb-6e6c900b8eaf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ef59d7d0-4636-4e7c-aa8c-4adcc6221021.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ff2e3a7d-c844-405a-8402-74c4de0da545.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/074bd537-d299-47c4-9dea-d13cbf27213c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/576d8c9a-0fe4-466b-97ba-a5187b9a8866.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/978b6fb4-ea4e-429b-8c8e-6e4c8683fd9f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b7ff48b1-4f40-437a-ae31-8d65a385f6fb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9e0d1733-3a7b-49a9-b942-1ea21ed6fa25.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e6fd52c7-6eb7-46cb-b1ab-422b1f163f8e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f61405d9-e22c-4ead-816a-e4ea9f5e1563.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ff21d685-7e7b-4966-b4b7-7d577b1dc558.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3175df55-bac7-4bed-92aa-650d394dbd5b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8aa18e64-8f53-4820-a8e6-c6ab1733d307.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5d0f8f55-626e-4041-8e3c-af4393e7dc07.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1ed986e6-660c-4ff5-9432-5a0dde2ec868.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/52dd0487-28bd-42e6-be6f-3f573ebc0c6a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dc24dadd-2f01-43b6-afb6-a8bbc11387aa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/210ef2b0-6a72-4a3d-89d6-2b7c1a8cef24.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0686da82-cfb8-43e3-b8a2-b86a4aec373a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/201ea0f1-b0cf-47a4-a880-808955be0d3d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f8635786-a414-4df1-ad72-d959bbf93d45.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/1fb82efd-526a-4ffe-890b-08c3a35420d4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/fb0b9641-d163-4f08-af15-15274d483ec5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/45cc49bb-a253-4280-aac6-20a7e7d8e0b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/09bd173e-4fbb-4ad1-bd5f-db7b1dd76ffd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ca8d2c5c-bff9-475d-9fd5-efdd833702df.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/df3139ca-fa3a-4a71-b4f3-2ffd7511c7e5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/db92cf07-4a9d-4dea-88b0-7c9d39bb92a7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c80c1928-7ce4-4319-9bd3-db88f0539956.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/00d899f2-8ab4-4043-946a-cd1ac5e6806f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/046a47d7-aa23-4d8d-8a17-2b000d4ed39d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/94eab9ee-fe41-4526-9b8a-9110059ebeee.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/dd70e084-0b16-45b2-ad1e-a5fbfb8e8d5b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3dd87b18-f309-480b-8d3e-031515dad5f4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/56a1557d-4db7-41a0-8903-952ef4d9227f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/94de4de4-32c1-4ff4-9dd9-0b1c1c5e2b33.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f16c826c-31b5-4987-b432-5ccbf20823bf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4ab42581-ae9d-4a44-9615-89972c309ce1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f7a506a5-a2d5-4d54-8639-8dec593cebc8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a1bd3a61-d53d-4bdc-bd7e-14ed3d017067.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/33202473-dc5c-41a7-a5c3-3b455cf9010b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4ef6c2a3-c4d1-47a2-90ec-5eac578b55de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5902acdf-ca34-43ea-9e02-3217637dc1a1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e9634242-3767-463b-84e2-f97e0c7b2ed7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/0a6f6c40-5f12-4e8d-8f63-720523b822d8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/725e4b49-8890-4a73-ae38-22fc3729f33a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/58475e7d-fc73-401c-bf55-b88c64b7d896.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e440716f-d1b2-496d-ab9b-36cfa2d5ac8d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2d5937a4-342e-427f-bafd-ed77daf249b8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/f0923ce4-118a-42db-ba68-1694413483e5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a1113a01-625c-49ea-a385-73edc3460bee.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b7f80ff7-12d6-407b-8814-31374bd4922a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f6650e3a-6666-4f48-b1d4-6b5e756146fc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b2a19f3e-7ca7-4afa-b365-08b4b6e1e25d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a0362e69-7183-4ca5-bb20-b7ac24ce2cef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/86569339-7dfa-4cfc-9825-fb03e37d0520.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/891f7002-a5d0-4a1b-be49-30fa201bd2a3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/3b3f3454-6550-4c34-9aa8-d954178df67d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d3d4e0cc-acd5-4616-9c32-f9509363d5e3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/832ca5bd-bbf8-4079-9825-90b8bc3ebed6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bcc7a8e3-9a0d-482e-a387-2f103c97f0fa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/6477fdc2-be06-4ab7-a580-442fd12a52ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5d53af22-82e5-4f4c-8cb5-cfda30578dba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/8a7283d2-c89a-4434-8803-9cd9b23309f9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d520fa19-6d60-4186-8021-2f1691c8d014.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ae8ca84c-dd30-49ea-9af1-610a70c1fa4e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cbd5d50b-1316-492c-a6a7-ede5f89db96f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1a63b278-93cc-4b08-8de4-ac7468a6b2e6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/df894764-c6ca-446b-bac2-af41e0e95a71.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f52dec98-b11d-4078-8bc4-cf7bc3c22cff.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/36e874b7-7769-49ee-9630-594df214ad6d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5c671ef3-fe19-44aa-aa4b-9f14577d2f50.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3d2151c6-4719-421b-b109-aff23145bffa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/879001f1-3a0e-409d-8e37-dce730eccdd4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c4d70d46-0d54-405d-ac0c-d1f4dfad2711.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fe52201d-b5d6-48de-aea8-688a80fd5f53.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2731d4a9-e6b3-4482-a62d-01ad282870e3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/581efb43-5ec3-4749-ba6e-e67f3b5759e0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/eea693d0-da0f-4579-a722-b228ea6300bd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/314b3d50-6c45-4972-b2ea-40bd03db58bb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b6f091e2-72ef-45bd-a8b5-d513f37b76df.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b40d2d7e-7181-4601-b21a-5a72e86f2da1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ff0b35f5-f551-4b7a-acf9-7631770f3f89.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ad64b45c-22e7-4f9b-905f-20d93cd63f9b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3b8d2608-9a9e-4390-a761-0e87adba753d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7e812d86-d5d4-4e77-972a-5b0c0cd7c795.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d421df12-ebf3-4065-b8e7-6b2c49c57946.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1587c98c-e176-4d1f-baaf-2a52408f5f98.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b58e3ddf-b271-44aa-9458-d8cb6b300c01.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7565e677-b1cf-4c7b-a58c-8bef6ab79763.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5c445149-2608-41d7-b528-734bfd3b2f42.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/78cb456c-22bc-4f2c-9bd9-4c984cb68141.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/979a1516-8f98-4522-906d-2ba1d5feceac.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/5f4ffa27-176e-4bd6-b990-80655111054e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/13a270dc-94e4-4822-8f72-e89491d55832.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f7b3b22d-c4fb-481c-b2f1-7f6260b4cf8c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/289d81b5-ea1c-45de-ac6c-18bd618fd315.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/71d12a91-5d15-4b22-8086-60e4c81d98b7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cefbd345-310e-4350-a49b-3d2ec832fa6d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1dcc26a7-5676-4e06-826c-53483deb7ee6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1db51efb-4293-46eb-aaff-fc1d9918222e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/325f1b8c-5bde-4c4a-b926-855c163d15ad.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2420bf91-e7af-4a8e-af0f-1b1fd22233c8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/78d7fe92-3bd1-49bd-af90-6a5d5838c39e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a65df307-f68e-4d3a-9d85-5073fba3f37c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/be7feb70-d64b-4866-9093-f68f18236d6e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/a08373d9-6f92-479d-aa43-7f2b41516689.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/2f63a80a-ff41-4157-ae59-7a26215f6224.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/afc37807-4208-45ae-b7f8-325f2502f2d8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/14325e6f-c4a1-487c-a9cf-f6a45af58211.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cc5bf139-84e5-43b4-8fda-1eba45149e68.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a12a4eaa-58b9-4588-8438-edc5fa9e870a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cde31ae0-7287-4c8c-8c41-43c9c09f4d78.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e62634c8-1ae7-4b99-9d97-f0f3b9dcc6b6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/925f8733-7eb8-4b0b-a671-b994cb608d4c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/57ac034d-1774-470e-af12-592d4d6213f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/013bb38d-245d-4121-8e85-0aaeb7b09cfc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ae54e577-c4fb-4fd6-a27b-b9740a0ec8b5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ad8ec635-3ed2-4d44-8ab2-93b53a816f6a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/62c77717-f172-4ee4-9ae8-3b7fb3d74e2a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8d12c31c-50db-4660-a61b-4c95d5a27f44.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/af28462e-99da-48a8-a6f1-f16a73167187.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e1c3837c-668b-46fd-ba51-1dd78807fc05.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/49870d08-dae4-4f7c-ba12-1f2a60ef67f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ffb012d9-dd7b-4aef-b5fa-19f2f9d6c500.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6c18f887-bc09-487c-af85-e904e23b5db5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d6f871bc-7191-44a6-ad47-ba372c53d888.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/fa2deb67-5abb-4869-a014-0afd6717f79f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3e0e4b79-3db5-409d-9a27-07834f2f4fd2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/48ff59d7-0f51-4d8b-b860-d5e5ac1358ab.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8edf6afe-0a29-4690-b714-8a14093d8112.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c59287c2-4e3c-4a9e-8529-257e16d4396d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/10416ab4-8f8c-4174-aef7-4c2d984ce1f7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fb7b35aa-b755-4515-a592-8c9733d76421.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/133d2046-6340-4583-acf0-3acff1602f3a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/357e1052-c43d-434e-be7e-d56ed118db46.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2e4d6056-5172-4d2e-a936-a0616ad42e41.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b57fdd7e-713b-4def-8d21-c6c25af8c1e8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ef0f6a91-1a48-4d5b-b032-cba305df010b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2c706b53-1d0e-4a22-bcb1-5a087bc4e3c2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6347e4b1-efb3-4bf9-afd1-ada9525d69f8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b383be74-96ac-43ed-b00a-bc27ababa76c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/42ba5969-6210-4a63-86d6-1487eb61a9f5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/8adf2166-cefb-4bf8-907d-5b3b0b9c04db.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/87fc3e74-469d-4d75-a621-c310c7f27cd1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bb5f3e0e-4da0-4993-b997-4b31dbe31232.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6d2c486e-ed6f-4cb2-abb4-9f982cc0725d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f0e6b81f-ee57-486c-8abb-07efe5c9de13.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/699e5a01-f34d-405c-afa4-627067e4f764.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f293c8a5-ff62-40c0-8535-0e76c99bbc84.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b448825a-9a77-49c0-b4dd-d48822466313.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/07e2aab4-ff0d-4b99-9286-d746fc290c10.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/390aecbf-ffd6-4221-bf51-a6344c71a47f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/99d95d64-7e93-46c1-be8c-68be3b11af13.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/64f6d129-b865-4ec7-b9f3-f1e89b8e1618.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/037b7a2c-d452-4962-a532-df326ba9a349.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/7ba38ec3-3475-4401-8f1c-3737a2767593.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8f67bd2a-e50a-429e-ba36-4757e228bb65.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/58cf14b6-4607-4ef9-96c0-69d942521318.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/f1036dd7-6b07-4b62-92a3-c3eb392d7879.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d0bfd962-a0ee-4b70-9db5-fed4513c532b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7f3e5a6f-b0ef-48a1-b7fc-18a372463a73.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d39e400c-7e84-4127-a642-f9e1a8a2227a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bede15c5-ccc0-4607-ab52-fa7efc34b177.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/70ec7a1a-7863-42a6-b177-cf237c500664.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8d12dd52-32e9-4f44-8710-67e27c296c37.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/350fdc14-3b0c-4b04-81b8-1c85d56448d4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c0598786-862d-431a-80e7-8a324f2e70c2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/438d4b8d-f664-4ce8-8d7e-ceac7031271a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e316a6e0-8ba3-4188-8333-21662242e153.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/534fe6a4-e732-4962-a6bd-c82bc5d4eb03.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cb6f020f-7c3b-4645-9684-4ee66a365b53.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ddd97134-2c06-44e6-b689-a20779ada143.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/44531f77-afc6-4ac2-94e1-d78078c85fc5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7c1a1d3d-721a-4238-9ac2-41dc840d8bdb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1ae1a23b-245c-4d7c-9398-b361e87d182b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/83b415ed-e3e5-474c-aa74-c5482a0e704f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cde5b66d-1318-4b9a-972d-88906c3d65ea.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b8f9a6a9-8920-4103-8e34-4032bc71e98c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/35b83020-05e4-4846-80d1-be39519e4bbc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c377e117-c0b2-400f-8394-1d8ded7ac98d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f10dd307-b344-4eea-bdf1-9dbf2918a89e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ef0dc3ab-2b92-4f1e-8cd6-7ea83acf9c3a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/70ee688e-e229-451d-a9dd-e25f4e1fe89c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0c3466e8-af09-4d5d-b211-f7d7a9fefca0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/03139d87-e197-4ccd-bfd5-e7004f9f6d93.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d81295b7-6fab-4776-abaf-b21faaa37c16.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/aec763fc-e9e8-4eea-aaf8-483763f24bc2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ea19c86d-6a7b-466f-9af8-b806807bfc00.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6e549aaa-f419-4c2b-b71b-26017034c066.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9a8f09c1-e81e-422e-8bf9-44274eb4a601.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a93b8cd9-e00d-4ef4-80a7-b3106d0572f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3cec390e-cb8b-4e43-bd76-f359fa1503c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f7965f69-e166-416c-a098-ad76d3e9f6f3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/668b39e9-1d4e-4862-bb64-e28ac9ba00ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b2922b41-1a5d-415f-9e7e-7290d29b69a2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/74b71b20-a668-4f83-801f-03af503265f8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a63da458-eefc-47df-afc3-e98013915116.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e4fa72c7-231f-42a7-b861-7efd2e565c90.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f259472a-f3d4-4642-b26d-dfd7e12a0864.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c5b854b0-f31e-455f-b90c-1f1a007ed333.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/62573c7c-122e-4f1c-9670-b19de0962fa0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6a70e15d-673e-46a5-9bf2-31397fc8d7e0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/98f6f228-f6f1-4219-bffa-8a15fef4e63f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/de974a45-71f5-40d6-b86f-a5c29490e1a7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0c01fa2f-f402-40bb-8514-42c99e822961.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9a228c59-8f69-443a-8ac0-0cc8da0df16a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/427b05e8-6fa4-47f5-9f76-fd48160ac03a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b13b0653-259a-45fb-b254-25e72f3d1a07.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/37674f6e-74a9-49ef-af72-1e4a41529ba7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/85789ff5-81bf-42d2-a498-985ef9d0dbb6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ea120079-7c94-4498-b0f8-1d61424ae4b3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0117d4c0-01f0-4982-871f-c7a790a79278.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6ca5d80a-2fa0-4585-a163-bfbbc7549453.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/dc626e0b-824f-4b8a-94d2-ff143d11646c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/557f28f6-6398-4107-b13e-3aeb7e8f7a15.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/29a2b6e4-d648-45fc-a0a6-c097096d04f9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6755931c-569f-4688-9dbd-45b4d667b095.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8d2bc04c-6a12-42b5-921e-0a2e3dc585e8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2ea3896f-f5c9-4625-983d-09808c2d1ace.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9da917c6-7a63-49f7-bd67-604059a92c49.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a0683011-574c-433d-a0fc-8cfc937b7810.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/adf5caf1-e1ea-4dc7-b139-71a77e397171.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d75b59c7-1cf8-485b-bc56-b1f65422d377.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dec1dd1c-c485-4dd6-b402-a104b73cd0ca.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/f4a7a866-93a3-45db-8b91-076def83d9de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/19c1b5f3-1376-4f61-b6f7-180e716a1ce9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fec68f8c-ab9e-4a47-afd7-5811e6af2812.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/69ce5be3-6064-43a2-b2d1-c1dfe8c18b18.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/182d08b9-539e-408d-884c-233c0ee26e02.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3034d778-e564-4dc7-a69c-0dc80988f0a8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6e7f3925-d4e2-4e04-b3b3-91c68121ebc8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/6a506ecd-36b3-4e2d-897b-621f570ba4a5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1cd3fd8b-bb5e-42a6-97ba-331369926dcc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/7861ba09-0273-4c63-bf95-0974c311b37a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/62d18214-436d-4ae7-9ead-47e53ad51ba4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d1215248-0630-4920-88ef-270d255fbcf9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/90038b21-9d0c-4b57-bbf7-3223019030ad.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7133833d-46c6-4229-8ed8-7dffefbd0a9a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4d0b92a6-e288-4018-a178-ee30b2e8b451.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d79891f3-8b69-4b8e-bcaf-365477e0cfcb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fcca02d6-d74f-429d-b4ef-f166f98f769e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/688abd3c-998e-4140-909d-36bb6162235d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a4da80e5-1892-440b-a8f5-5b0e0af75c41.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ddbcd457-2bbc-4df6-9af3-3841d2ec66be.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9a1ee7d6-03ef-4e34-89d4-4b2406006e2e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ab1fe98f-bda1-4fd4-a1ce-2757bb006627.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a052f4e0-ed98-4b02-b0f0-250f10ee7432.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/57eded94-53b1-40af-b6e2-29c65b330b53.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7cfc622a-911e-4206-beb4-9e5d1f5ac03f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8db87af6-429a-4bd4-b7cc-e6683f4b2a28.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/405be05c-3b34-452e-ba7f-38ce2890d3a5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dd7ef228-ee9b-40f9-938f-b052d80ab59d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2b121949-08aa-406d-bfc1-5326c346e5fc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/68d5a351-7ad7-46a2-978d-0641680aee39.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/cb79abe8-f76f-498b-b519-6f7eb9b54121.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a2aa8e28-a83e-4e57-898b-45f0058057a9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d9df0ddf-446f-4825-94db-6f8ef1d7fc77.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ddf4b414-bba4-476d-a96b-21c2f9d27ad3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/08bbf835-c03d-4707-aa18-49ffb5925353.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c780616f-1e38-4081-be14-b2fd7840b51f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6afbe7e5-2b66-4e92-a179-6253c3277ebc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6616705b-a78a-40bc-8ebe-1e0d2f1b0eda.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3d4a9a57-dc24-45dd-bd55-005b8520ce69.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a1391007-45ff-41f4-8ae9-a0b426632c43.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6bb09e0d-ec76-432c-b0d7-2bf097c2e251.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/06296520-689b-48d5-8e1f-6f07190868e4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/88ed51a5-01f7-4f0f-ae88-490f47ec4727.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cf105134-e943-4d3f-a7c5-13d9026f44cc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b4bfa73f-091e-41b5-ad7c-2c37f7461c03.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f9c0353b-3813-4c9a-b042-56734cb16a78.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/177e512a-71c1-4bc4-9f0c-53401498bdae.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1acca140-eff8-4086-baf6-d583f67eea1a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7053f7f5-e13e-4750-aaa2-33ca548de452.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8f456c1b-aa73-4e26-949c-539aa93e179a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bebdd1a3-af07-495e-9130-12d3fbd5b13b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/59f7222c-c022-4055-b085-52bd4ce82487.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ef9de618-1ca0-4ee5-b63a-4a0f0057ba37.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cc84761b-801f-4de6-ae73-7fb90e67a8d8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/235e36c0-e740-437f-90c2-8e0f23613172.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d227da98-b01c-4263-89bb-1c146d2de22c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7f63c861-74ba-4667-9e29-732a81c3703c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/029dddd5-332f-4e37-8760-fb75eeed16c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8fb1ca61-c615-4758-8711-bb9b0d13862f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9ac3ea89-9373-47b2-8ff4-13f72428ec77.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9b4eec79-cb3f-4f78-94f0-8e2256a95207.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6164e731-874f-4601-a6b3-0314ce2f69fe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/648bd923-a1e9-4807-8fb0-bd76bb3fdee4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/78e33242-311d-489d-b347-a89053209704.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e54a141b-4e6a-4eac-896e-ec8ee8a649de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d9630952-16e3-4f51-bf1e-64c787b163f6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/61dd0155-930e-47cf-8ab8-22e4f05a7d52.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a6ced55e-4e83-404e-95f9-46387b445971.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d40182d7-4b09-47b1-83f2-0df1936391ff.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e2048f73-f0c0-4f94-b370-3352a127766f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/444df2bd-2779-4786-9c16-23bd7d85d4d2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/d3a13d4c-fc30-47b8-81de-3e70b405b9f2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ac4bbe3f-aef0-4628-a848-0a41892b66dc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/4842f0bd-5a91-45f6-aeb1-e6c3044e8b39.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/878f8568-8337-4266-910a-a50480407cf7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/c5825334-d6ae-42d2-8b25-f787b64da3c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/00215c7c-a229-4639-a51d-2698931950ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2316d4d7-9475-41a0-a171-cca0c7bb6806.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ea06182c-c229-424b-9ea9-184750d45d2f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/5d0b9d41-12ae-4446-b02b-d6da24130fcd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/cb6d6dcb-2492-4169-bfa8-adbeae1f70a4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f3780638-8ac4-4111-b231-73884024e7bf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e5f66896-a335-41f2-954d-0cab11bd0e13.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/2daefeac-6e3f-4f2e-a7a5-9d4ed986abed.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/36304869-0e2b-42cd-b150-8b757a0ab566.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/67e18143-4e9d-4568-92d5-c84faff5bfc1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f953b417-322a-4ee6-9078-84eeb82ee0a2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3e166bf2-13ab-4e8f-a703-03c9ab794b65.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/19a56b5c-db16-443c-a142-39ed72196e12.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5515decb-029b-493e-b932-971fb23c2c04.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5ddd65cb-f01c-4511-966a-65f3ba58f035.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/67c74400-8167-4f28-9748-9c2f2a94c5b6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/70459585-be63-41fb-8db2-019954b23b29.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/8adbb61f-229e-4194-8f72-bba04b249660.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1e71af5d-9d2d-4000-9c1e-5b7b85283085.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/67bea436-8e43-483b-a608-3521848c8d8b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/dbe4c18f-f2b2-4d6b-8938-80a3be8ae559.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/0ce72669-4426-4b58-867e-c2b920008407.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/3917f6d3-1bd1-4598-ba88-7c89f381ad4a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/41174701-6211-498c-a8f9-f0962d318c98.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9b2406ad-0f86-411b-a5ba-e9396b1d8456.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/77d96158-34aa-48b1-bdb5-000f8b39198a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b9061fb4-210b-4f1e-8964-d67a6b994591.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bf45bc66-4bfa-40d1-8674-b3dfbbac0127.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d5a74fd8-28dc-405a-aaf2-3f0fdba2c152.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/b009614e-0a30-46cb-9df3-62ff4f362ccf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6695ad27-3678-435a-8a01-4e64475a203f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/70a6f74b-2979-4791-94c4-6452925f5d5f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/90148b02-7158-4442-a494-a6184abc8ff2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/915fe291-92b6-4b7a-8362-92d527b53319.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/da53206d-c885-4923-af7a-f23ea3d748ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9f2b4df4-ba18-417b-b15c-c3466095c918.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e43ba932-1191-42ed-86ac-abb766944392.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/eeff7e9e-e911-4e27-adc9-fedc0fe9bc8e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/96cadea1-1201-42e8-8cfb-99ab808b5c99.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/835825e9-4565-488c-8627-460457fdcee6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b31530b2-7b30-4994-94d2-9fe51b013f24.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c1e4e4ad-e129-41e2-b0d7-eb925539d72b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e7019687-2092-4a10-935f-2450aa6b2470.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/5e346749-039a-4c66-8d78-d4e9f7941d72.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6f740f5a-c4ff-4b6c-a587-274e3da82128.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/5715c92e-c1e8-4dd5-9ed0-f95679d8c4f3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e9dd7bab-ae94-43d5-9d7e-89419a08218a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/414e5eb0-682b-4f8c-a884-19ded4cb0a29.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/6d384e11-a47e-46ba-9036-3cf4b7ed6fac.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/8fe923f2-69c3-46fa-8af9-1438bf2d8ed0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/944a9293-ad71-4d08-acd4-affcf47b020d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/90d49257-9c36-4e55-8596-da2d7dc52700.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/08cbf9f0-267c-415a-a6ca-39e506f270b5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/705d4a70-be9f-410e-9083-e5cd5ec4a79d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f4a14a4d-8c14-4251-871f-4f09bddeb4ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f6c1eb26-b8a5-4d4a-b314-59e9a5838402.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/fdc73dac-3722-4e97-9890-ade11d57f36b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c16a45a0-fe17-4709-a846-87e8bac2f961.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/c74587bf-1080-4161-bcce-56a0ff4f3c0d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a913eb39-de97-40ab-9ae3-4dce314d9b3c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/84108839-9f40-450f-b3bb-56f3120cc9bd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/9b72f78c-ea1c-4316-a0af-afe47b022129.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b58d69e7-914e-40a2-b969-3d245a99b2ed.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b6537916-53fe-4532-87b1-8cda71c52c75.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a987680e-a3c9-4d7e-9cd0-bcfe6147a243.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/7db4f4ab-1583-4e80-a02f-0e6a98d8e64f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/78b0254e-ba69-46e5-95c5-7784425f0da5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/348af674-7739-48e3-91c1-7159448e4f54.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/b3f00590-40c3-4e35-b73a-b62940aa70f3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a624206a-c794-48b5-a400-f5c0c6d40a94.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/f8dc79de-b614-47f1-90a5-c6b6833a8941.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/08d5b59f-c94f-438c-ac22-8d8e2808ff66.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/43899f98-0003-4531-8d4b-6d537e293b84.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/bfe7baa0-c29f-4216-80c9-d2a15c1cdba9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/36195d73-db5b-48c8-9788-92c9687f5371.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/01e43c54-28cf-4f97-8201-d20129401d6e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/fd37415a-56fe-46bf-b137-351a1cd1871a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/a8d38e4c-d192-403f-bb92-de619df4c402.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/a46f040e-bd27-4f1f-b6fe-dcc2e7c2247a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/824acc15-661e-4134-acc6-3e1492284c55.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/34d8b701-eba0-44db-ac7c-c77059d59ab1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/1b2fbb81-a044-4c99-b9af-2b6fa995a92e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/96ace0f0-c7da-43cc-b539-526de0b56c4a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/d3f329da-720d-49fa-aa28-80fa5250fe79.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/42143569-71ec-418f-ba8b-294ae1d59dd9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/c67690ea-8923-43ca-9290-1eaf0ffb3f77.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/0dbb9dac-a521-4995-9222-260f97464f3f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/de81c3cb-fb0b-4ef9-ba68-5cbb5dc28e22.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580001/ad55d8e8-09e9-4f28-9efc-98c1e7db5519.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/e9598930-c060-4a77-a80e-df1d00648f7d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/ad91fcbe-a913-42a9-b623-4b2aeed4300f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v14_RV245_2024-v1/2580000/2152facb-7f0e-4b9b-ae38-77cf5abd352c.root'
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
    tableName = cms.string('/dev/CMSSW_14_0_0/GRun/V156')
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
    maxPtForLooperReconstruction = cms.double(0.0),
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
        'AlCa_AK8PFJet40_v25',
        'AlCa_PFJet40_v30'
    ),
    AlCaLumiPixelsCountsExpress = cms.vstring('AlCa_LumiPixelsCounts_Random_v8'),
    AlCaLumiPixelsCountsPrompt = cms.vstring(
        'AlCa_LumiPixelsCounts_Random_v8',
        'AlCa_LumiPixelsCounts_ZeroBias_v10'
    ),
    AlCaP0 = cms.vstring(
        'AlCa_EcalEtaEBonly_v23',
        'AlCa_EcalEtaEEonly_v23',
        'AlCa_EcalPi0EBonly_v23',
        'AlCa_EcalPi0EEonly_v23'
    ),
    AlCaPPSExpress = cms.vstring(
        'HLT_PPSMaxTracksPerArm1_v7',
        'HLT_PPSMaxTracksPerRP4_v7'
    ),
    AlCaPPSPrompt = cms.vstring(
        'HLT_PPSMaxTracksPerArm1_v7',
        'HLT_PPSMaxTracksPerRP4_v7'
    ),
    AlCaPhiSym = cms.vstring('AlCa_EcalPhiSym_v18'),
    BTagMu = cms.vstring(
        'HLT_BTagMu_AK4DiJet110_Mu5_v23',
        'HLT_BTagMu_AK4DiJet170_Mu5_v22',
        'HLT_BTagMu_AK4DiJet20_Mu5_v23',
        'HLT_BTagMu_AK4DiJet40_Mu5_v23',
        'HLT_BTagMu_AK4DiJet70_Mu5_v23',
        'HLT_BTagMu_AK4Jet300_Mu5_v22',
        'HLT_BTagMu_AK8DiJet170_Mu5_v19',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v12',
        'HLT_BTagMu_AK8Jet300_Mu5_v22'
    ),
    Commissioning = cms.vstring(
        'HLT_IsoTrackHB_v12',
        'HLT_IsoTrackHE_v12',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v7',
        'HLT_PFJet40_GPUvsCPU_v5'
    ),
    Cosmics = cms.vstring('HLT_L1SingleMuCosmics_v6'),
    DQMGPUvsCPU = cms.vstring(
        'DQM_EcalReconstruction_v10',
        'DQM_HcalReconstruction_v8',
        'DQM_PixelReconstruction_v10'
    ),
    DQMOnlineBeamspot = cms.vstring(
        'HLT_HT300_Beamspot_v21',
        'HLT_ZeroBias_Beamspot_v14'
    ),
    DQMPPSRandom = cms.vstring('HLT_PPSRandom_v1'),
    DisplacedJet = cms.vstring(
        'HLT_CaloMET60_DTCluster50_v9',
        'HLT_CaloMET60_DTClusterNoMB1S50_v9',
        'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v9',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v9',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v9',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v9',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v9',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v9',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v9',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v9',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p7_v4',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p8_v4',
        'HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v6',
        'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v9',
        'HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v6',
        'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3nsInclusive_v5',
        'HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive_v5',
        'HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive_v5',
        'HLT_HT350_v5',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v21',
        'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v9',
        'HLT_HT425_v17',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v8',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive_v5',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v7',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v7',
        'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v7',
        'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless_v5',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v7',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless_v5',
        'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive_v5',
        'HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive_v5',
        'HLT_HT550_DisplacedDijet60_Inclusive_v21',
        'HLT_L1MET_DTCluster50_v9',
        'HLT_L1MET_DTClusterNoMB1S50_v9',
        'HLT_L1Mu6HT240_v7',
        'HLT_L1SingleLLPJet_v5',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless_v7',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive_v7',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless_v7',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive_v7',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless_v5',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive_v5',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless_v5',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless_v7',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive_v7',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive_v5',
        'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v9',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v9',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v9',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v9',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v9',
        'HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5_v9',
        'HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5_v9',
        'HLT_PFJet200_TimeGt2p5ns_v8',
        'HLT_PFJet200_TimeLtNeg2p5ns_v8'
    ),
    EGamma0 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v12',
        'HLT_DiPhoton10Time1ns_v8',
        'HLT_DiPhoton10Time1p2ns_v8',
        'HLT_DiPhoton10Time1p4ns_v8',
        'HLT_DiPhoton10Time1p6ns_v8',
        'HLT_DiPhoton10Time1p8ns_v8',
        'HLT_DiPhoton10Time2ns_v8',
        'HLT_DiPhoton10_CaloIdL_v8',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v22',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v9',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v9',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v21',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v21',
        'HLT_DiphotonMVA14p25_Mass90_v1',
        'HLT_DiphotonMVA14p25_Tight_Mass90_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v8',
        'HLT_DoubleEle25_CaloIdL_MW_v13',
        'HLT_DoubleEle27_CaloIdL_MW_v13',
        'HLT_DoubleEle33_CaloIdL_MW_v26',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v8',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v30',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v30',
        'HLT_DoubleEle8_eta1p22_mMax6_v8',
        'HLT_DoublePhoton33_CaloIdL_v15',
        'HLT_DoublePhoton70_v15',
        'HLT_DoublePhoton85_v23',
        'HLT_ECALHT800_v18',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v23',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v28',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v16',
        'HLT_Ele14_eta2p5_IsoVVVL_Gsf_PFHT200_PNetBTag0p53_v3',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v26',
        'HLT_Ele15_IsoVVVL_PFHT450_v26',
        'HLT_Ele15_IsoVVVL_PFHT600_v30',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v17',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v26',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v28',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v28',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v27',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v27',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v11',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Loose_eta2p3_CrossL1_v4',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Medium_eta2p3_CrossL1_v4',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Tight_eta2p3_CrossL1_v4',
        'HLT_Ele28_HighEta_SC20_Mass55_v21',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v23',
        'HLT_Ele30_WPTight_Gsf_v9',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v23',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v17',
        'HLT_Ele32_WPTight_Gsf_v23',
        'HLT_Ele35_WPTight_Gsf_v17',
        'HLT_Ele38_WPTight_Gsf_v17',
        'HLT_Ele40_WPTight_Gsf_v17',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v10',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v10',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v28',
        'HLT_Ele50_IsoVVVL_PFHT450_v26',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v26',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v28',
        'HLT_Photon100EBHE10_v10',
        'HLT_Photon110EB_TightID_TightIso_AK8CaloJet30_v1',
        'HLT_Photon110EB_TightID_TightIso_AK8PFJet30_v3',
        'HLT_Photon110EB_TightID_TightIso_CaloJet30_v1',
        'HLT_Photon110EB_TightID_TightIso_PFJet30_v4',
        'HLT_Photon110EB_TightID_TightIso_v10',
        'HLT_Photon120_R9Id90_HE10_IsoM_v22',
        'HLT_Photon120_v21',
        'HLT_Photon150_v15',
        'HLT_Photon165_R9Id90_HE10_IsoM_v23',
        'HLT_Photon175_v23',
        'HLT_Photon200_v22',
        'HLT_Photon20_HoverELoose_v18',
        'HLT_Photon300_NoHE_v21',
        'HLT_Photon30EB_TightID_TightIso_v10',
        'HLT_Photon30_HoverELoose_v18',
        'HLT_Photon32_OneProng32_M50To105_v8',
        'HLT_Photon33_v13',
        'HLT_Photon34_R9Id90_CaloIdL_IsoL_DisplacedIdL_MediumChargedIsoDisplacedPFTauHPS34_v6',
        'HLT_Photon35_TwoProngs35_v11',
        'HLT_Photon40EB_TightID_TightIso_v1',
        'HLT_Photon40EB_v1',
        'HLT_Photon45EB_TightID_TightIso_v1',
        'HLT_Photon45EB_v1',
        'HLT_Photon50EB_TightID_TightIso_AK8CaloJet30_v1',
        'HLT_Photon50EB_TightID_TightIso_AK8PFJet30_v3',
        'HLT_Photon50EB_TightID_TightIso_CaloJet30_v1',
        'HLT_Photon50EB_TightID_TightIso_PFJet30_v4',
        'HLT_Photon50EB_TightID_TightIso_v6',
        'HLT_Photon50EB_v2',
        'HLT_Photon50_R9Id90_HE10_IsoM_v22',
        'HLT_Photon50_TimeGt2p5ns_v5',
        'HLT_Photon50_TimeLtNeg2p5ns_v5',
        'HLT_Photon50_v21',
        'HLT_Photon55EB_TightID_TightIso_v2',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v8',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v8',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v8',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v7',
        'HLT_Photon75EB_TightID_TightIso_v6',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v15',
        'HLT_Photon75_R9Id90_HE10_IsoM_v22',
        'HLT_Photon75_v21',
        'HLT_Photon90EB_TightID_TightIso_v6',
        'HLT_Photon90_R9Id90_HE10_IsoM_v22',
        'HLT_Photon90_v21',
        'HLT_SingleEle8_SingleEGL1_v7',
        'HLT_SingleEle8_v7'
    ),
    EGamma1 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v12',
        'HLT_DiPhoton10Time1ns_v8',
        'HLT_DiPhoton10Time1p2ns_v8',
        'HLT_DiPhoton10Time1p4ns_v8',
        'HLT_DiPhoton10Time1p6ns_v8',
        'HLT_DiPhoton10Time1p8ns_v8',
        'HLT_DiPhoton10Time2ns_v8',
        'HLT_DiPhoton10_CaloIdL_v8',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v22',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v9',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v9',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v21',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v21',
        'HLT_DiphotonMVA14p25_Mass90_v1',
        'HLT_DiphotonMVA14p25_Tight_Mass90_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v8',
        'HLT_DoubleEle25_CaloIdL_MW_v13',
        'HLT_DoubleEle27_CaloIdL_MW_v13',
        'HLT_DoubleEle33_CaloIdL_MW_v26',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v8',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v30',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v30',
        'HLT_DoubleEle8_eta1p22_mMax6_v8',
        'HLT_DoublePhoton33_CaloIdL_v15',
        'HLT_DoublePhoton70_v15',
        'HLT_DoublePhoton85_v23',
        'HLT_ECALHT800_v18',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v23',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v28',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v16',
        'HLT_Ele14_eta2p5_IsoVVVL_Gsf_PFHT200_PNetBTag0p53_v3',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v26',
        'HLT_Ele15_IsoVVVL_PFHT450_v26',
        'HLT_Ele15_IsoVVVL_PFHT600_v30',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v17',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v26',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v28',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v28',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v27',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v27',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v11',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Loose_eta2p3_CrossL1_v4',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Medium_eta2p3_CrossL1_v4',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Tight_eta2p3_CrossL1_v4',
        'HLT_Ele28_HighEta_SC20_Mass55_v21',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v23',
        'HLT_Ele30_WPTight_Gsf_v9',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v23',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v17',
        'HLT_Ele32_WPTight_Gsf_v23',
        'HLT_Ele35_WPTight_Gsf_v17',
        'HLT_Ele38_WPTight_Gsf_v17',
        'HLT_Ele40_WPTight_Gsf_v17',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v10',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v10',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v28',
        'HLT_Ele50_IsoVVVL_PFHT450_v26',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v26',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v28',
        'HLT_Photon100EBHE10_v10',
        'HLT_Photon110EB_TightID_TightIso_AK8CaloJet30_v1',
        'HLT_Photon110EB_TightID_TightIso_AK8PFJet30_v3',
        'HLT_Photon110EB_TightID_TightIso_CaloJet30_v1',
        'HLT_Photon110EB_TightID_TightIso_PFJet30_v4',
        'HLT_Photon110EB_TightID_TightIso_v10',
        'HLT_Photon120_R9Id90_HE10_IsoM_v22',
        'HLT_Photon120_v21',
        'HLT_Photon150_v15',
        'HLT_Photon165_R9Id90_HE10_IsoM_v23',
        'HLT_Photon175_v23',
        'HLT_Photon200_v22',
        'HLT_Photon20_HoverELoose_v18',
        'HLT_Photon300_NoHE_v21',
        'HLT_Photon30EB_TightID_TightIso_v10',
        'HLT_Photon30_HoverELoose_v18',
        'HLT_Photon32_OneProng32_M50To105_v8',
        'HLT_Photon33_v13',
        'HLT_Photon34_R9Id90_CaloIdL_IsoL_DisplacedIdL_MediumChargedIsoDisplacedPFTauHPS34_v6',
        'HLT_Photon35_TwoProngs35_v11',
        'HLT_Photon40EB_TightID_TightIso_v1',
        'HLT_Photon40EB_v1',
        'HLT_Photon45EB_TightID_TightIso_v1',
        'HLT_Photon45EB_v1',
        'HLT_Photon50EB_TightID_TightIso_AK8CaloJet30_v1',
        'HLT_Photon50EB_TightID_TightIso_AK8PFJet30_v3',
        'HLT_Photon50EB_TightID_TightIso_CaloJet30_v1',
        'HLT_Photon50EB_TightID_TightIso_PFJet30_v4',
        'HLT_Photon50EB_TightID_TightIso_v6',
        'HLT_Photon50EB_v2',
        'HLT_Photon50_R9Id90_HE10_IsoM_v22',
        'HLT_Photon50_TimeGt2p5ns_v5',
        'HLT_Photon50_TimeLtNeg2p5ns_v5',
        'HLT_Photon50_v21',
        'HLT_Photon55EB_TightID_TightIso_v2',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v8',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v8',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v8',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v7',
        'HLT_Photon75EB_TightID_TightIso_v6',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v15',
        'HLT_Photon75_R9Id90_HE10_IsoM_v22',
        'HLT_Photon75_v21',
        'HLT_Photon90EB_TightID_TightIso_v6',
        'HLT_Photon90_R9Id90_HE10_IsoM_v22',
        'HLT_Photon90_v21',
        'HLT_SingleEle8_SingleEGL1_v7',
        'HLT_SingleEle8_v7'
    ),
    EcalLaser = cms.vstring('HLT_EcalCalibration_v4'),
    EphemeralHLTPhysics0 = cms.vstring('HLT_EphemeralPhysics_v7'),
    EphemeralHLTPhysics1 = cms.vstring('HLT_EphemeralPhysics_v7'),
    EphemeralHLTPhysics2 = cms.vstring('HLT_EphemeralPhysics_v7'),
    EphemeralHLTPhysics3 = cms.vstring('HLT_EphemeralPhysics_v7'),
    EphemeralHLTPhysics4 = cms.vstring('HLT_EphemeralPhysics_v7'),
    EphemeralHLTPhysics5 = cms.vstring('HLT_EphemeralPhysics_v7'),
    EphemeralHLTPhysics6 = cms.vstring('HLT_EphemeralPhysics_v7'),
    EphemeralHLTPhysics7 = cms.vstring('HLT_EphemeralPhysics_v7'),
    EphemeralZeroBias0 = cms.vstring('HLT_EphemeralZeroBias_v7'),
    EphemeralZeroBias1 = cms.vstring('HLT_EphemeralZeroBias_v7'),
    EphemeralZeroBias2 = cms.vstring('HLT_EphemeralZeroBias_v7'),
    EphemeralZeroBias3 = cms.vstring('HLT_EphemeralZeroBias_v7'),
    EphemeralZeroBias4 = cms.vstring('HLT_EphemeralZeroBias_v7'),
    EphemeralZeroBias5 = cms.vstring('HLT_EphemeralZeroBias_v7'),
    EphemeralZeroBias6 = cms.vstring('HLT_EphemeralZeroBias_v7'),
    EphemeralZeroBias7 = cms.vstring('HLT_EphemeralZeroBias_v7'),
    EventDisplay = cms.vstring(
        'HLT_DoublePhoton85_v23',
        'HLT_PFJet500_v31',
        'HLT_Physics_v12'
    ),
    ExpressAlignment = cms.vstring(
        'HLT_HT300_Beamspot_v21',
        'HLT_ZeroBias_Beamspot_v14'
    ),
    ExpressPhysics = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v27',
        'HLT_IsoMu20_v25',
        'HLT_IsoMu24_v23',
        'HLT_IsoMu27_v26',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v25',
        'HLT_Physics_v12',
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v6',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v10',
        'HLT_ZeroBias_IsolatedBunches_v10',
        'HLT_ZeroBias_v11'
    ),
    HLTMonitor = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v27',
        'HLT_Ele32_WPTight_Gsf_v23',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v10',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v21',
        'HLT_HT550_DisplacedDijet60_Inclusive_v21',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v10',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v25',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50_v7',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v11',
        'HLT_PFHT510_v27',
        'HLT_PFJet260_v30',
        'HLT_PFJet320_v30',
        'HLT_PFMET130_PFMHT130_IDTight_v30',
        'HLT_PFMET140_PFMHT140_IDTight_v30'
    ),
    HLTPhysics = cms.vstring('HLT_Physics_v12'),
    HcalNZS = cms.vstring(
        'HLT_HcalNZS_v19',
        'HLT_HcalPhiSym_v21'
    ),
    JetMET0 = cms.vstring(
        'HLT_AK8DiPFJet250_250_SoftDropMass40_v4',
        'HLT_AK8DiPFJet250_250_SoftDropMass50_v4',
        'HLT_AK8DiPFJet260_260_SoftDropMass30_v4',
        'HLT_AK8DiPFJet260_260_SoftDropMass40_v4',
        'HLT_AK8DiPFJet270_270_SoftDropMass30_v4',
        'HLT_AK8DiPFJet280_280_SoftDropMass30_v10',
        'HLT_AK8DiPFJet290_290_SoftDropMass30_v4',
        'HLT_AK8PFJet140_v25',
        'HLT_AK8PFJet200_v25',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v7',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53_v7',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55_v7',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60_v7',
        'HLT_AK8PFJet220_SoftDropMass40_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03_v7',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05_v7',
        'HLT_AK8PFJet230_SoftDropMass40_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06_v7',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10_v7',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03_v7',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05_v7',
        'HLT_AK8PFJet260_v26',
        'HLT_AK8PFJet275_Nch40_v4',
        'HLT_AK8PFJet275_Nch45_v4',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06_v7',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10_v7',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03_v7',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05_v7',
        'HLT_AK8PFJet320_v26',
        'HLT_AK8PFJet380_SoftDropMass30_v4',
        'HLT_AK8PFJet400_SoftDropMass30_v4',
        'HLT_AK8PFJet400_v26',
        'HLT_AK8PFJet40_v26',
        'HLT_AK8PFJet425_SoftDropMass30_v4',
        'HLT_AK8PFJet450_SoftDropMass30_v4',
        'HLT_AK8PFJet450_v26',
        'HLT_AK8PFJet500_v26',
        'HLT_AK8PFJet550_v21',
        'HLT_AK8PFJet60_v25',
        'HLT_AK8PFJet80_v26',
        'HLT_AK8PFJetFwd140_v24',
        'HLT_AK8PFJetFwd200_v24',
        'HLT_AK8PFJetFwd260_v25',
        'HLT_AK8PFJetFwd320_v25',
        'HLT_AK8PFJetFwd400_v25',
        'HLT_AK8PFJetFwd40_v25',
        'HLT_AK8PFJetFwd450_v25',
        'HLT_AK8PFJetFwd500_v25',
        'HLT_AK8PFJetFwd60_v24',
        'HLT_AK8PFJetFwd80_v24',
        'HLT_CaloJet500_NoJetID_v20',
        'HLT_CaloJet550_NoJetID_v15',
        'HLT_CaloMET350_NotCleaned_v12',
        'HLT_CaloMET90_NotCleaned_v12',
        'HLT_CaloMHT90_v12',
        'HLT_DiPFJetAve100_HFJEC_v27',
        'HLT_DiPFJetAve140_v23',
        'HLT_DiPFJetAve160_HFJEC_v26',
        'HLT_DiPFJetAve180_PPSMatch_Xi0p3_QuadJet_Max2ProtPerRP_v4',
        'HLT_DiPFJetAve200_v23',
        'HLT_DiPFJetAve220_HFJEC_v26',
        'HLT_DiPFJetAve260_HFJEC_v9',
        'HLT_DiPFJetAve260_v24',
        'HLT_DiPFJetAve300_HFJEC_v26',
        'HLT_DiPFJetAve320_v24',
        'HLT_DiPFJetAve400_v24',
        'HLT_DiPFJetAve40_v24',
        'HLT_DiPFJetAve500_v24',
        'HLT_DiPFJetAve60_HFJEC_v25',
        'HLT_DiPFJetAve60_v24',
        'HLT_DiPFJetAve80_HFJEC_v27',
        'HLT_DiPFJetAve80_v24',
        'HLT_DoublePFJets100_PNetBTag_0p11_v4',
        'HLT_DoublePFJets116MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_DoublePFJets128MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_DoublePFJets200_PNetBTag_0p11_v4',
        'HLT_DoublePFJets350_PNetBTag_0p11_v4',
        'HLT_DoublePFJets40_PNetBTag_0p11_v4',
        'HLT_L1AXOVTight_v2',
        'HLT_L1ETMHadSeeds_v8',
        'HLT_MET105_IsoTrk50_v17',
        'HLT_MET120_IsoTrk50_v17',
        'HLT_Mu12_DoublePFJets100_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets200_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets350_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_Mu12_DoublePFJets40_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_Mu12eta2p3_PFJet40_v11',
        'HLT_Mu12eta2p3_v11',
        'HLT_PFHT1050_v28',
        'HLT_PFHT180_v27',
        'HLT_PFHT250_v27',
        'HLT_PFHT350_v29',
        'HLT_PFHT370_v27',
        'HLT_PFHT430_v27',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v22',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v22',
        'HLT_PFHT510_v27',
        'HLT_PFHT590_v27',
        'HLT_PFHT680_v27',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v22',
        'HLT_PFHT780_v27',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v22',
        'HLT_PFHT890_v27',
        'HLT_PFJet110_v10',
        'HLT_PFJet140_v29',
        'HLT_PFJet200_v29',
        'HLT_PFJet260_v30',
        'HLT_PFJet320_v30',
        'HLT_PFJet400_v30',
        'HLT_PFJet40_v31',
        'HLT_PFJet450_v31',
        'HLT_PFJet500_v31',
        'HLT_PFJet550_v21',
        'HLT_PFJet60_v31',
        'HLT_PFJet80_v31',
        'HLT_PFJetFwd140_v28',
        'HLT_PFJetFwd200_v28',
        'HLT_PFJetFwd260_v29',
        'HLT_PFJetFwd320_v29',
        'HLT_PFJetFwd400_v29',
        'HLT_PFJetFwd40_v29',
        'HLT_PFJetFwd450_v29',
        'HLT_PFJetFwd500_v29',
        'HLT_PFJetFwd60_v29',
        'HLT_PFJetFwd80_v28',
        'HLT_PFMET105_IsoTrk50_v11',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v19',
        'HLT_PFMET120_PFMHT120_IDTight_v30',
        'HLT_PFMET130_PFMHT130_IDTight_v30',
        'HLT_PFMET140_PFMHT140_IDTight_v30',
        'HLT_PFMET200_BeamHaloCleaned_v19',
        'HLT_PFMET200_NotCleaned_v19',
        'HLT_PFMET250_NotCleaned_v19',
        'HLT_PFMET300_NotCleaned_v19',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v19',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v30',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v29',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v29',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v21',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v19'
    ),
    JetMET1 = cms.vstring(
        'HLT_AK8DiPFJet250_250_SoftDropMass40_v4',
        'HLT_AK8DiPFJet250_250_SoftDropMass50_v4',
        'HLT_AK8DiPFJet260_260_SoftDropMass30_v4',
        'HLT_AK8DiPFJet260_260_SoftDropMass40_v4',
        'HLT_AK8DiPFJet270_270_SoftDropMass30_v4',
        'HLT_AK8DiPFJet280_280_SoftDropMass30_v10',
        'HLT_AK8DiPFJet290_290_SoftDropMass30_v4',
        'HLT_AK8PFJet140_v25',
        'HLT_AK8PFJet200_v25',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v7',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53_v7',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55_v7',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60_v7',
        'HLT_AK8PFJet220_SoftDropMass40_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03_v7',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05_v7',
        'HLT_AK8PFJet230_SoftDropMass40_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06_v7',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10_v7',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03_v7',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05_v7',
        'HLT_AK8PFJet260_v26',
        'HLT_AK8PFJet275_Nch40_v4',
        'HLT_AK8PFJet275_Nch45_v4',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06_v7',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10_v7',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03_v7',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05_v7',
        'HLT_AK8PFJet320_v26',
        'HLT_AK8PFJet380_SoftDropMass30_v4',
        'HLT_AK8PFJet400_SoftDropMass30_v4',
        'HLT_AK8PFJet400_v26',
        'HLT_AK8PFJet40_v26',
        'HLT_AK8PFJet425_SoftDropMass30_v4',
        'HLT_AK8PFJet450_SoftDropMass30_v4',
        'HLT_AK8PFJet450_v26',
        'HLT_AK8PFJet500_v26',
        'HLT_AK8PFJet550_v21',
        'HLT_AK8PFJet60_v25',
        'HLT_AK8PFJet80_v26',
        'HLT_AK8PFJetFwd140_v24',
        'HLT_AK8PFJetFwd200_v24',
        'HLT_AK8PFJetFwd260_v25',
        'HLT_AK8PFJetFwd320_v25',
        'HLT_AK8PFJetFwd400_v25',
        'HLT_AK8PFJetFwd40_v25',
        'HLT_AK8PFJetFwd450_v25',
        'HLT_AK8PFJetFwd500_v25',
        'HLT_AK8PFJetFwd60_v24',
        'HLT_AK8PFJetFwd80_v24',
        'HLT_CaloJet500_NoJetID_v20',
        'HLT_CaloJet550_NoJetID_v15',
        'HLT_CaloMET350_NotCleaned_v12',
        'HLT_CaloMET90_NotCleaned_v12',
        'HLT_CaloMHT90_v12',
        'HLT_DiPFJetAve100_HFJEC_v27',
        'HLT_DiPFJetAve140_v23',
        'HLT_DiPFJetAve160_HFJEC_v26',
        'HLT_DiPFJetAve180_PPSMatch_Xi0p3_QuadJet_Max2ProtPerRP_v4',
        'HLT_DiPFJetAve200_v23',
        'HLT_DiPFJetAve220_HFJEC_v26',
        'HLT_DiPFJetAve260_HFJEC_v9',
        'HLT_DiPFJetAve260_v24',
        'HLT_DiPFJetAve300_HFJEC_v26',
        'HLT_DiPFJetAve320_v24',
        'HLT_DiPFJetAve400_v24',
        'HLT_DiPFJetAve40_v24',
        'HLT_DiPFJetAve500_v24',
        'HLT_DiPFJetAve60_HFJEC_v25',
        'HLT_DiPFJetAve60_v24',
        'HLT_DiPFJetAve80_HFJEC_v27',
        'HLT_DiPFJetAve80_v24',
        'HLT_DoublePFJets100_PNetBTag_0p11_v4',
        'HLT_DoublePFJets116MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_DoublePFJets128MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_DoublePFJets200_PNetBTag_0p11_v4',
        'HLT_DoublePFJets350_PNetBTag_0p11_v4',
        'HLT_DoublePFJets40_PNetBTag_0p11_v4',
        'HLT_L1AXOVTight_v2',
        'HLT_L1ETMHadSeeds_v8',
        'HLT_MET105_IsoTrk50_v17',
        'HLT_MET120_IsoTrk50_v17',
        'HLT_Mu12_DoublePFJets100_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets200_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets350_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_Mu12_DoublePFJets40_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_Mu12eta2p3_PFJet40_v11',
        'HLT_Mu12eta2p3_v11',
        'HLT_PFHT1050_v28',
        'HLT_PFHT180_v27',
        'HLT_PFHT250_v27',
        'HLT_PFHT350_v29',
        'HLT_PFHT370_v27',
        'HLT_PFHT430_v27',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v22',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v22',
        'HLT_PFHT510_v27',
        'HLT_PFHT590_v27',
        'HLT_PFHT680_v27',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v22',
        'HLT_PFHT780_v27',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v22',
        'HLT_PFHT890_v27',
        'HLT_PFJet110_v10',
        'HLT_PFJet140_v29',
        'HLT_PFJet200_v29',
        'HLT_PFJet260_v30',
        'HLT_PFJet320_v30',
        'HLT_PFJet400_v30',
        'HLT_PFJet40_v31',
        'HLT_PFJet450_v31',
        'HLT_PFJet500_v31',
        'HLT_PFJet550_v21',
        'HLT_PFJet60_v31',
        'HLT_PFJet80_v31',
        'HLT_PFJetFwd140_v28',
        'HLT_PFJetFwd200_v28',
        'HLT_PFJetFwd260_v29',
        'HLT_PFJetFwd320_v29',
        'HLT_PFJetFwd400_v29',
        'HLT_PFJetFwd40_v29',
        'HLT_PFJetFwd450_v29',
        'HLT_PFJetFwd500_v29',
        'HLT_PFJetFwd60_v29',
        'HLT_PFJetFwd80_v28',
        'HLT_PFMET105_IsoTrk50_v11',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v19',
        'HLT_PFMET120_PFMHT120_IDTight_v30',
        'HLT_PFMET130_PFMHT130_IDTight_v30',
        'HLT_PFMET140_PFMHT140_IDTight_v30',
        'HLT_PFMET200_BeamHaloCleaned_v19',
        'HLT_PFMET200_NotCleaned_v19',
        'HLT_PFMET250_NotCleaned_v19',
        'HLT_PFMET300_NotCleaned_v19',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v19',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v30',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v29',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v29',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v21',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v19'
    ),
    L1Accept = cms.vstring(
        'DST_Physics_v14',
        'DST_ZeroBias_v9'
    ),
    MonteCarlo = cms.vstring(
        'MC_AK4CaloJetsFromPV_v16',
        'MC_AK4CaloJets_v17',
        'MC_AK4PFJetPNet_v3',
        'MC_AK4PFJets_v27',
        'MC_AK8CaloHT_v16',
        'MC_AK8PFHT_v26',
        'MC_AK8PFJetPNet_v3',
        'MC_AK8PFJets_v27',
        'MC_CaloHT_v16',
        'MC_CaloMET_JetIdCleaned_v17',
        'MC_CaloMET_v16',
        'MC_CaloMHT_v16',
        'MC_Diphoton10_10_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass10_v21',
        'MC_DoubleEle5_CaloIdL_MW_v24',
        'MC_DoubleMuNoFiltersNoVtx_v15',
        'MC_DoubleMu_TrkIsoVVL_DZ_v21',
        'MC_Egamma_Open_Unseeded_v6',
        'MC_Egamma_Open_v6',
        'MC_Ele15_Ele10_CaloIdL_TrackIdL_IsoVL_DZ_v23',
        'MC_Ele5_WPTight_Gsf_v16',
        'MC_IsoMu_v25',
        'MC_PFHT_v26',
        'MC_PFMET_v27',
        'MC_PFMHT_v26',
        'MC_PFScouting_v4',
        'MC_ReducedIterativeTracking_v20'
    ),
    Muon0 = cms.vstring(
        'HLT_CascadeMu100_v11',
        'HLT_CscCluster100_Ele5_v2',
        'HLT_CscCluster100_Mu5_v4',
        'HLT_CscCluster100_PNetTauhPFJet10_Loose_v4',
        'HLT_CscCluster50_Photon20Unseeded_v2',
        'HLT_CscCluster50_Photon30Unseeded_v2',
        'HLT_CscCluster_Loose_v8',
        'HLT_CscCluster_Medium_v8',
        'HLT_CscCluster_Tight_v8',
        'HLT_DisplacedMu24_MediumChargedIsoDisplacedPFTauHPS24_v6',
        'HLT_DoubleCscCluster100_v5',
        'HLT_DoubleCscCluster75_v5',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v10',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v9',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v9',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v9',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v9',
        'HLT_DoubleL2Mu50_v9',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v8',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v8',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v9',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v8',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v8',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v8',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_noDCA_v4',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_v4',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v20',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v20',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v20',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v20',
        'HLT_DoubleMu43NoFiltersNoVtx_v12',
        'HLT_DoubleMu48NoFiltersNoVtx_v12',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v18',
        'HLT_HighPtTkMu100_v10',
        'HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v11',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Loose_eta2p3_CrossL1_v4',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Medium_eta2p3_CrossL1_v4',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Tight_eta2p3_CrossL1_v4',
        'HLT_IsoMu20_v25',
        'HLT_IsoMu24_OneProng32_v7',
        'HLT_IsoMu24_TwoProngs35_v11',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v11',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v11',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_CrossL1_v6',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v11',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_PNet1Tauh0p50_v4',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_v4',
        'HLT_IsoMu24_eta2p1_PFHT250_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Loose_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Medium_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Tight_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet20_eta2p2_SingleL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_PFJet60_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_PFJet75_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Loose_eta2p3_CrossL1_ETau_Monitoring_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_eta2p3_CrossL1_ETau_Monitoring_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_eta2p3_CrossL1_ETau_Monitoring_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet45_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_SinglePFJet25_PNet1Tauh0p50_v4',
        'HLT_IsoMu24_eta2p1_v25',
        'HLT_IsoMu24_v23',
        'HLT_IsoMu27_MediumChargedIsoDisplacedPFTauHPS24_eta2p1_SingleL1_v6',
        'HLT_IsoMu27_v26',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06_v7',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_v10',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v10',
        'HLT_IsoTrk200_L1SingleMuShower_v2',
        'HLT_IsoTrk400_L1SingleMuShower_v2',
        'HLT_L1CSCShower_DTCluster50_v8',
        'HLT_L1CSCShower_DTCluster75_v8',
        'HLT_L2Mu50NoVtx_3Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
        'HLT_L2Mu50NoVtx_3Cha_VetoL3Mu0DxyMax1cm_v2',
        'HLT_L3Mu30NoVtx_DxyMin0p01cm_v1',
        'HLT_L3Mu50NoVtx_DxyMin0p01cm_v1',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v8',
        'HLT_Mu12_IsoVVL_PFHT150_PNetBTag0p53_v3',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v25',
        'HLT_Mu15_IsoVVVL_PFHT450_v25',
        'HLT_Mu15_IsoVVVL_PFHT600_v29',
        'HLT_Mu15_v13',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8CaloJet30_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8PFJet30_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_CaloJet30_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_PFJet30_v4',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v25',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v24',
        'HLT_Mu17_TrkIsoVVL_v23',
        'HLT_Mu17_v23',
        'HLT_Mu18_Mu9_SameSign_v14',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v13',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v13',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v13',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v13',
        'HLT_Mu19_TrkIsoVVL_v14',
        'HLT_Mu19_v14',
        'HLT_Mu20_v22',
        'HLT_Mu27_v23',
        'HLT_Mu37_TkMu27_v15',
        'HLT_Mu3_PFJet40_v26',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v12',
        'HLT_Mu50_IsoVVVL_PFHT450_v25',
        'HLT_Mu50_L1SingleMuShower_v9',
        'HLT_Mu50_v23',
        'HLT_Mu55_v13',
        'HLT_Mu8_TrkIsoVVL_v22',
        'HLT_Mu8_v22',
        'HLT_TripleMu_10_5_5_DZ_v20',
        'HLT_TripleMu_12_10_5_v20',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v13',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v18',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v15'
    ),
    Muon1 = cms.vstring(
        'HLT_CascadeMu100_v11',
        'HLT_CscCluster100_Ele5_v2',
        'HLT_CscCluster100_Mu5_v4',
        'HLT_CscCluster100_PNetTauhPFJet10_Loose_v4',
        'HLT_CscCluster50_Photon20Unseeded_v2',
        'HLT_CscCluster50_Photon30Unseeded_v2',
        'HLT_CscCluster_Loose_v8',
        'HLT_CscCluster_Medium_v8',
        'HLT_CscCluster_Tight_v8',
        'HLT_DisplacedMu24_MediumChargedIsoDisplacedPFTauHPS24_v6',
        'HLT_DoubleCscCluster100_v5',
        'HLT_DoubleCscCluster75_v5',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v10',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v9',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v9',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v9',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v9',
        'HLT_DoubleL2Mu50_v9',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v8',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v8',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v9',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v8',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v8',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v8',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_noDCA_v4',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_v4',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v20',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v20',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v20',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v20',
        'HLT_DoubleMu43NoFiltersNoVtx_v12',
        'HLT_DoubleMu48NoFiltersNoVtx_v12',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v18',
        'HLT_HighPtTkMu100_v10',
        'HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v11',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Loose_eta2p3_CrossL1_v4',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Medium_eta2p3_CrossL1_v4',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Tight_eta2p3_CrossL1_v4',
        'HLT_IsoMu20_v25',
        'HLT_IsoMu24_OneProng32_v7',
        'HLT_IsoMu24_TwoProngs35_v11',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v11',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v11',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_CrossL1_v6',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v11',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_PNet1Tauh0p50_v4',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_v4',
        'HLT_IsoMu24_eta2p1_PFHT250_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Loose_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Medium_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Tight_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet20_eta2p2_SingleL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_PFJet60_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_PFJet75_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Loose_eta2p3_CrossL1_ETau_Monitoring_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_eta2p3_CrossL1_ETau_Monitoring_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_eta2p3_CrossL1_ETau_Monitoring_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet45_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_SinglePFJet25_PNet1Tauh0p50_v4',
        'HLT_IsoMu24_eta2p1_v25',
        'HLT_IsoMu24_v23',
        'HLT_IsoMu27_MediumChargedIsoDisplacedPFTauHPS24_eta2p1_SingleL1_v6',
        'HLT_IsoMu27_v26',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06_v7',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_v10',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v10',
        'HLT_IsoTrk200_L1SingleMuShower_v2',
        'HLT_IsoTrk400_L1SingleMuShower_v2',
        'HLT_L1CSCShower_DTCluster50_v8',
        'HLT_L1CSCShower_DTCluster75_v8',
        'HLT_L2Mu50NoVtx_3Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
        'HLT_L2Mu50NoVtx_3Cha_VetoL3Mu0DxyMax1cm_v2',
        'HLT_L3Mu30NoVtx_DxyMin0p01cm_v1',
        'HLT_L3Mu50NoVtx_DxyMin0p01cm_v1',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v8',
        'HLT_Mu12_IsoVVL_PFHT150_PNetBTag0p53_v3',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v25',
        'HLT_Mu15_IsoVVVL_PFHT450_v25',
        'HLT_Mu15_IsoVVVL_PFHT600_v29',
        'HLT_Mu15_v13',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8CaloJet30_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8PFJet30_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_CaloJet30_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_PFJet30_v4',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v25',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v24',
        'HLT_Mu17_TrkIsoVVL_v23',
        'HLT_Mu17_v23',
        'HLT_Mu18_Mu9_SameSign_v14',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v13',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v13',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v13',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v13',
        'HLT_Mu19_TrkIsoVVL_v14',
        'HLT_Mu19_v14',
        'HLT_Mu20_v22',
        'HLT_Mu27_v23',
        'HLT_Mu37_TkMu27_v15',
        'HLT_Mu3_PFJet40_v26',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v12',
        'HLT_Mu50_IsoVVVL_PFHT450_v25',
        'HLT_Mu50_L1SingleMuShower_v9',
        'HLT_Mu50_v23',
        'HLT_Mu55_v13',
        'HLT_Mu8_TrkIsoVVL_v22',
        'HLT_Mu8_v22',
        'HLT_TripleMu_10_5_5_DZ_v20',
        'HLT_TripleMu_12_10_5_v20',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v13',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v18',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v15'
    ),
    MuonEG = cms.vstring(
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v27',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v27',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v27',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v25',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v17',
        'HLT_Mu17_Photon30_IsoCaloId_v16',
        'HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId_v9',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v25',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v17',
        'HLT_Mu27_Ele37_CaloIdL_MW_v15',
        'HLT_Mu37_Ele27_CaloIdL_MW_v15',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v9',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v9',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v13',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v13',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v28',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v28',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v29',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v29',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50_v7',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_PNet1BTag0p20_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_PNet2BTagMean0p55_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v7',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_v7',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_v7',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v23',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v21'
    ),
    NoBPTX = cms.vstring(
        'HLT_CDC_L2cosmic_10_er1p0_v8',
        'HLT_CDC_L2cosmic_5p5_er1p0_v8',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v12',
        'HLT_L2Mu10_NoVertex_NoBPTX_v13',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v12',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v11',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v12',
        'HLT_UncorrectedJetE30_NoBPTX_v12',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v12',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v12'
    ),
    OnlineMonitor = cms.vstring( (
        'HLT_AK8DiPFJet250_250_SoftDropMass40_v4',
        'HLT_AK8DiPFJet250_250_SoftDropMass50_v4',
        'HLT_AK8DiPFJet260_260_SoftDropMass30_v4',
        'HLT_AK8DiPFJet260_260_SoftDropMass40_v4',
        'HLT_AK8DiPFJet270_270_SoftDropMass30_v4',
        'HLT_AK8DiPFJet280_280_SoftDropMass30_v10',
        'HLT_AK8DiPFJet290_290_SoftDropMass30_v4',
        'HLT_AK8PFJet140_v25',
        'HLT_AK8PFJet200_v25',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v7',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53_v7',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55_v7',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60_v7',
        'HLT_AK8PFJet220_SoftDropMass40_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03_v7',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05_v7',
        'HLT_AK8PFJet230_SoftDropMass40_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06_v7',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10_v7',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03_v7',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05_v7',
        'HLT_AK8PFJet260_v26',
        'HLT_AK8PFJet275_Nch40_v4',
        'HLT_AK8PFJet275_Nch45_v4',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06_v7',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10_v7',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03_v7',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05_v7',
        'HLT_AK8PFJet320_v26',
        'HLT_AK8PFJet380_SoftDropMass30_v4',
        'HLT_AK8PFJet400_SoftDropMass30_v4',
        'HLT_AK8PFJet400_v26',
        'HLT_AK8PFJet40_v26',
        'HLT_AK8PFJet425_SoftDropMass30_v4',
        'HLT_AK8PFJet450_SoftDropMass30_v4',
        'HLT_AK8PFJet450_v26',
        'HLT_AK8PFJet500_v26',
        'HLT_AK8PFJet550_v21',
        'HLT_AK8PFJet60_v25',
        'HLT_AK8PFJet80_v26',
        'HLT_AK8PFJetFwd140_v24',
        'HLT_AK8PFJetFwd200_v24',
        'HLT_AK8PFJetFwd260_v25',
        'HLT_AK8PFJetFwd320_v25',
        'HLT_AK8PFJetFwd400_v25',
        'HLT_AK8PFJetFwd40_v25',
        'HLT_AK8PFJetFwd450_v25',
        'HLT_AK8PFJetFwd500_v25',
        'HLT_AK8PFJetFwd60_v24',
        'HLT_AK8PFJetFwd80_v24',
        'HLT_BTagMu_AK4DiJet110_Mu5_v23',
        'HLT_BTagMu_AK4DiJet170_Mu5_v22',
        'HLT_BTagMu_AK4DiJet20_Mu5_v23',
        'HLT_BTagMu_AK4DiJet40_Mu5_v23',
        'HLT_BTagMu_AK4DiJet70_Mu5_v23',
        'HLT_BTagMu_AK4Jet300_Mu5_v22',
        'HLT_BTagMu_AK8DiJet170_Mu5_v19',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v12',
        'HLT_BTagMu_AK8Jet300_Mu5_v22',
        'HLT_CDC_L2cosmic_10_er1p0_v8',
        'HLT_CDC_L2cosmic_5p5_er1p0_v8',
        'HLT_CaloJet500_NoJetID_v20',
        'HLT_CaloJet550_NoJetID_v15',
        'HLT_CaloMET350_NotCleaned_v12',
        'HLT_CaloMET60_DTCluster50_v9',
        'HLT_CaloMET60_DTClusterNoMB1S50_v9',
        'HLT_CaloMET90_NotCleaned_v12',
        'HLT_CaloMHT90_v12',
        'HLT_CascadeMu100_v11',
        'HLT_CscCluster50_Photon20Unseeded_v2',
        'HLT_CscCluster50_Photon30Unseeded_v2',
        'HLT_CscCluster_Loose_v8',
        'HLT_CscCluster_Medium_v8',
        'HLT_CscCluster_Tight_v8',
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v12',
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v27',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v27',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v27',
        'HLT_DiPFJetAve100_HFJEC_v27',
        'HLT_DiPFJetAve140_v23',
        'HLT_DiPFJetAve160_HFJEC_v26',
        'HLT_DiPFJetAve200_v23',
        'HLT_DiPFJetAve220_HFJEC_v26',
        'HLT_DiPFJetAve260_HFJEC_v9',
        'HLT_DiPFJetAve260_v24',
        'HLT_DiPFJetAve300_HFJEC_v26',
        'HLT_DiPFJetAve320_v24',
        'HLT_DiPFJetAve400_v24',
        'HLT_DiPFJetAve40_v24',
        'HLT_DiPFJetAve500_v24',
        'HLT_DiPFJetAve60_HFJEC_v25',
        'HLT_DiPFJetAve60_v24',
        'HLT_DiPFJetAve80_HFJEC_v27',
        'HLT_DiPFJetAve80_v24',
        'HLT_DiPhoton10Time1ns_v8',
        'HLT_DiPhoton10Time1p2ns_v8',
        'HLT_DiPhoton10Time1p4ns_v8',
        'HLT_DiPhoton10Time1p6ns_v8',
        'HLT_DiPhoton10Time1p8ns_v8',
        'HLT_DiPhoton10Time2ns_v8',
        'HLT_DiPhoton10_CaloIdL_v8',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v22',
        'HLT_Dimuon0_Jpsi3p5_Muon2_v15',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_v18',
        'HLT_Dimuon0_Jpsi_v18',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v18',
        'HLT_Dimuon0_LowMass_L1_4_v18',
        'HLT_Dimuon0_LowMass_L1_TM530_v16',
        'HLT_Dimuon0_LowMass_v18',
        'HLT_Dimuon0_Upsilon_L1_4p5_v19',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v17',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v19',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v16',
        'HLT_Dimuon0_Upsilon_NoVertexing_v17',
        'HLT_Dimuon10_Upsilon_y1p4_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v12',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v17',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v15',
        'HLT_Dimuon14_PsiPrime_v23',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v16',
        'HLT_Dimuon18_PsiPrime_v24',
        'HLT_Dimuon24_Phi_noCorrL1_v16',
        'HLT_Dimuon24_Upsilon_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_v24',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v8',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v9',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v9',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v21',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v21',
        'HLT_DiphotonMVA14p25_Mass90_v1',
        'HLT_DiphotonMVA14p25_Tight_Mass90_v1',
        'HLT_DisplacedMu24_MediumChargedIsoDisplacedPFTauHPS24_v6',
        'HLT_DoubleCscCluster100_v5',
        'HLT_DoubleCscCluster75_v5',
        'HLT_DoubleEle25_CaloIdL_MW_v13',
        'HLT_DoubleEle27_CaloIdL_MW_v13',
        'HLT_DoubleEle33_CaloIdL_MW_v26',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v30',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v30',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v10',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v9',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v9',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v9',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v9',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v9',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v9',
        'HLT_DoubleL2Mu50_v9',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v8',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v8',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v9',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v8',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v8',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v8',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_noDxy_v6',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_v11',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS36_Trk1_eta2p1_v6',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_v6',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_v10',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_v10',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v16',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_noDCA_v4',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_v4',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v20',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v20',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v20',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v20',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v14',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v14',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v16',
        'HLT_DoubleMu3_Trk_Tau3mu_v22',
        'HLT_DoubleMu43NoFiltersNoVtx_v12',
        'HLT_DoubleMu48NoFiltersNoVtx_v12',
        'HLT_DoubleMu4_3_Bs_v25',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_3_Jpsi_v25',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v17',
        'HLT_DoubleMu4_JpsiTrk_Bc_v10',
        'HLT_DoubleMu4_Jpsi_Displaced_v17',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v17',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v18',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v25',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v14',
        'HLT_DoublePFJets100_PNetBTag_0p11_v4',
        'HLT_DoublePFJets116MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_DoublePFJets128MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_DoublePFJets200_PNetBTag_0p11_v4',
        'HLT_DoublePFJets350_PNetBTag_0p11_v4',
        'HLT_DoublePFJets40_PNetBTag_0p11_v4',
        'HLT_DoublePhoton33_CaloIdL_v15',
        'HLT_DoublePhoton70_v15',
        'HLT_DoublePhoton85_v23',
        'HLT_ECALHT800_v18',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v23',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v28',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v16',
        'HLT_Ele14_eta2p5_IsoVVVL_Gsf_PFHT200_PNetBTag0p53_v3',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v26',
        'HLT_Ele15_IsoVVVL_PFHT450_v26',
        'HLT_Ele15_IsoVVVL_PFHT600_v30',
        'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v17',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v26',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v28',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v28',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v27',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v27',
        'HLT_Ele28_HighEta_SC20_Mass55_v21',
        'HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v23',
        'HLT_Ele30_WPTight_Gsf_v9',
        'HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v23',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v17',
        'HLT_Ele32_WPTight_Gsf_v23',
        'HLT_Ele35_WPTight_Gsf_v17',
        'HLT_Ele38_WPTight_Gsf_v17',
        'HLT_Ele40_WPTight_Gsf_v17',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v10',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v10',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v28',
        'HLT_Ele50_IsoVVVL_PFHT450_v26',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v26',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v28',
        'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v9',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v9',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v9',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v9',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v9',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v9',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v9',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v9',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p7_v4',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p8_v4',
        'HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v6',
        'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v9',
        'HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v6',
        'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3nsInclusive_v5',
        'HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive_v5',
        'HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive_v5',
        'HLT_HT350_v5',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v21',
        'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v9',
        'HLT_HT425_v17',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v8',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive_v5',
        'HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive_v5',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v7',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v7',
        'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v7',
        'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless_v5',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v7',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless_v5',
        'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive_v5',
        'HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive_v5',
        'HLT_HT550_DisplacedDijet60_Inclusive_v21',
        'HLT_HcalNZS_v19',
        'HLT_HcalPhiSym_v21',
        'HLT_HighPtTkMu100_v10',
        'HLT_IsoMu20_v25',
        'HLT_IsoMu24_OneProng32_v7',
        'HLT_IsoMu24_TwoProngs35_v11',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1_v11',
        'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v11',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_CrossL1_v6',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v11',
        'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v10',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_PNet1Tauh0p50_v4',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_v4',
        'HLT_IsoMu24_eta2p1_PFHT250_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Loose_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Medium_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Tight_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_L2NN_eta2p3_CrossL1_v4',
        'HLT_IsoMu24_eta2p1_SinglePFJet25_PNet1Tauh0p50_v4',
        'HLT_IsoMu24_eta2p1_v25',
        'HLT_IsoMu24_v23',
        'HLT_IsoMu27_MediumChargedIsoDisplacedPFTauHPS24_eta2p1_SingleL1_v6',
        'HLT_IsoMu27_v26',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06_v7',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_v10',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v7',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v7',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v10',
        'HLT_IsoTrackHB_v12',
        'HLT_IsoTrackHE_v12',
        'HLT_L1CSCShower_DTCluster50_v8',
        'HLT_L1CSCShower_DTCluster75_v8',
        'HLT_L1ETMHadSeeds_v8',
        'HLT_L1MET_DTCluster50_v9',
        'HLT_L1MET_DTClusterNoMB1S50_v9',
        'HLT_L1Mu6HT240_v7',
        'HLT_L1SingleLLPJet_v5',
        'HLT_L1SingleMuCosmics_v6',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless_v7',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive_v7',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless_v7',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive_v7',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless_v5',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive_v5',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless_v5',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless_v7',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive_v7',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive_v5',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v7',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v12',
        'HLT_L2Mu10_NoVertex_NoBPTX_v13',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v12',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v11',
        'HLT_L2Mu50NoVtx_3Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v2',
        'HLT_L2Mu50NoVtx_3Cha_VetoL3Mu0DxyMax1cm_v2',
        'HLT_L3Mu30NoVtx_DxyMin0p01cm_v1',
        'HLT_L3Mu50NoVtx_DxyMin0p01cm_v1',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v8',
        'HLT_MET105_IsoTrk50_v17',
        'HLT_MET120_IsoTrk50_v17',
        'HLT_Mu12_DoublePFJets100_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets200_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets350_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_Mu12_DoublePFJets40_PNetBTag_0p11_v4',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_PNet2BTag_0p11_v4',
        'HLT_Mu12_IsoVVL_PFHT150_PNetBTag0p53_v3',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v25',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v17',
        'HLT_Mu12eta2p3_PFJet40_v11',
        'HLT_Mu12eta2p3_v11',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v25',
        'HLT_Mu15_IsoVVVL_PFHT450_v25',
        'HLT_Mu15_IsoVVVL_PFHT600_v29',
        'HLT_Mu15_v13',
        'HLT_Mu17_Photon30_IsoCaloId_v16',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8CaloJet30_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8PFJet30_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_CaloJet30_v3',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_PFJet30_v4',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v15',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v25',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v24',
        'HLT_Mu17_TrkIsoVVL_v23',
        'HLT_Mu17_v23',
        'HLT_Mu18_Mu9_SameSign_v14',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v13',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v13',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v13',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v13',
        'HLT_Mu19_TrkIsoVVL_v14',
        'HLT_Mu19_v14',
        'HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId_v9',
        'HLT_Mu20_v22',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v25',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v17',
        'HLT_Mu25_TkMu0_Phi_v18',
        'HLT_Mu27_Ele37_CaloIdL_MW_v15',
        'HLT_Mu27_v23',
        'HLT_Mu30_TkMu0_Psi_v11',
        'HLT_Mu30_TkMu0_Upsilon_v11',
        'HLT_Mu37_Ele27_CaloIdL_MW_v15',
        'HLT_Mu37_TkMu27_v15',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v9',
        'HLT_Mu3_PFJet40_v26',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v12',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v12',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v9',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v13',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v13',
        'HLT_Mu4_L1DoubleMu_v11',
        'HLT_Mu50_IsoVVVL_PFHT450_v25',
        'HLT_Mu50_L1SingleMuShower_v9',
        'HLT_Mu50_v23',
        'HLT_Mu55_v13',
        'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v9',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v9',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v9',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v9',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v9',
        'HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5_v9',
        'HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5_v9',
        'HLT_Mu7p5_L2Mu2_Jpsi_v20',
        'HLT_Mu7p5_L2Mu2_Upsilon_v20',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v28',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v28',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v29',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v29',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50_v7',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_PNet1BTag0p20_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_PNet2BTagMean0p55_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_v4',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v7',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_v7',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_v7',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v23',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v21',
        'HLT_Mu8_TrkIsoVVL_v22',
        'HLT_Mu8_v22',
        'HLT_PFHT1050_v28',
        'HLT_PFHT180_v27',
        'HLT_PFHT250_v27',
        'HLT_PFHT350_v29',
        'HLT_PFHT370_v27',
        'HLT_PFHT430_v27',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v22',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v22',
        'HLT_PFHT510_v27',
        'HLT_PFHT590_v27',
        'HLT_PFHT680_v27',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v22',
        'HLT_PFHT780_v27',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v22',
        'HLT_PFHT890_v27',
        'HLT_PFJet110_v10',
        'HLT_PFJet140_v29',
        'HLT_PFJet200_TimeGt2p5ns_v8',
        'HLT_PFJet200_TimeLtNeg2p5ns_v8',
        'HLT_PFJet200_v29',
        'HLT_PFJet260_v30',
        'HLT_PFJet320_v30',
        'HLT_PFJet400_v30',
        'HLT_PFJet40_v31',
        'HLT_PFJet450_v31',
        'HLT_PFJet500_v31',
        'HLT_PFJet550_v21',
        'HLT_PFJet60_v31',
        'HLT_PFJet80_v31',
        'HLT_PFJetFwd140_v28',
        'HLT_PFJetFwd200_v28',
        'HLT_PFJetFwd260_v29',
        'HLT_PFJetFwd320_v29',
        'HLT_PFJetFwd400_v29',
        'HLT_PFJetFwd40_v29',
        'HLT_PFJetFwd450_v29',
        'HLT_PFJetFwd500_v29',
        'HLT_PFJetFwd60_v29',
        'HLT_PFJetFwd80_v28',
        'HLT_PFMET105_IsoTrk50_v11',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v19',
        'HLT_PFMET120_PFMHT120_IDTight_v30',
        'HLT_PFMET130_PFMHT130_IDTight_v30',
        'HLT_PFMET140_PFMHT140_IDTight_v30',
        'HLT_PFMET200_BeamHaloCleaned_v19',
        'HLT_PFMET200_NotCleaned_v19',
        'HLT_PFMET250_NotCleaned_v19',
        'HLT_PFMET300_NotCleaned_v19',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v19',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v30',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v29',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v10',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v29',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v21',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v19',
        'HLT_Photon100EBHE10_v10',
        'HLT_Photon110EB_TightID_TightIso_AK8CaloJet30_v1',
        'HLT_Photon110EB_TightID_TightIso_AK8PFJet30_v3',
        'HLT_Photon110EB_TightID_TightIso_CaloJet30_v1',
        'HLT_Photon110EB_TightID_TightIso_PFJet30_v4',
        'HLT_Photon110EB_TightID_TightIso_v10',
        'HLT_Photon120_R9Id90_HE10_IsoM_v22',
        'HLT_Photon120_v21',
        'HLT_Photon150_v15',
        'HLT_Photon165_R9Id90_HE10_IsoM_v23',
        'HLT_Photon175_v23',
        'HLT_Photon200_v22',
        'HLT_Photon20_HoverELoose_v18',
        'HLT_Photon300_NoHE_v21',
        'HLT_Photon30EB_TightID_TightIso_v10',
        'HLT_Photon30_HoverELoose_v18',
        'HLT_Photon32_OneProng32_M50To105_v8',
        'HLT_Photon33_v13',
        'HLT_Photon34_R9Id90_CaloIdL_IsoL_DisplacedIdL_MediumChargedIsoDisplacedPFTauHPS34_v6',
        'HLT_Photon35_TwoProngs35_v11',
        'HLT_Photon40EB_TightID_TightIso_v1',
        'HLT_Photon40EB_v1',
        'HLT_Photon45EB_TightID_TightIso_v1',
        'HLT_Photon45EB_v1',
        'HLT_Photon50EB_TightID_TightIso_AK8CaloJet30_v1',
        'HLT_Photon50EB_TightID_TightIso_AK8PFJet30_v3',
        'HLT_Photon50EB_TightID_TightIso_CaloJet30_v1',
        'HLT_Photon50EB_TightID_TightIso_PFJet30_v4',
        'HLT_Photon50EB_TightID_TightIso_v6',
        'HLT_Photon50_R9Id90_HE10_IsoM_v22',
        'HLT_Photon50_TimeGt2p5ns_v5',
        'HLT_Photon50_TimeLtNeg2p5ns_v5',
        'HLT_Photon50_v21',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v8',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v8',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v8',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v7',
        'HLT_Photon75EB_TightID_TightIso_v6',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v15',
        'HLT_Photon75_R9Id90_HE10_IsoM_v22',
        'HLT_Photon75_v21',
        'HLT_Photon90EB_TightID_TightIso_v6',
        'HLT_Photon90_R9Id90_HE10_IsoM_v22',
        'HLT_Photon90_v21',
        'HLT_Physics_v12',
        'HLT_QuadPFJet100_88_70_30_v8',
        'HLT_QuadPFJet103_88_75_15_v15',
        'HLT_QuadPFJet105_88_75_30_v7',
        'HLT_QuadPFJet105_88_76_15_v15',
        'HLT_QuadPFJet111_90_80_15_v15',
        'HLT_QuadPFJet111_90_80_30_v7',
        'HLT_Random_v3',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v14',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v15',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v12',
        'HLT_TripleMu_10_5_5_DZ_v20',
        'HLT_TripleMu_12_10_5_v20',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v13',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v18',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v15',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v12',
        'HLT_UncorrectedJetE30_NoBPTX_v12',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v12',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v12',
        'HLT_ZeroBias_Alignment_v6',
        'HLT_ZeroBias_FirstBXAfterTrain_v8',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v10',
        'HLT_ZeroBias_FirstCollisionInTrain_v9',
        'HLT_ZeroBias_IsolatedBunches_v10',
        'HLT_ZeroBias_LastCollisionInTrain_v8',
        'HLT_ZeroBias_v11'
     ) ),
    ParkingDoubleMuonLowMass0 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v15',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_v18',
        'HLT_Dimuon0_Jpsi_v18',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v18',
        'HLT_Dimuon0_LowMass_L1_4_v18',
        'HLT_Dimuon0_LowMass_L1_TM530_v16',
        'HLT_Dimuon0_LowMass_v18',
        'HLT_Dimuon0_Upsilon_L1_4p5_v19',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v17',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v19',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v16',
        'HLT_Dimuon0_Upsilon_NoVertexing_v17',
        'HLT_Dimuon10_Upsilon_y1p4_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v12',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v17',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v15',
        'HLT_Dimuon14_PsiPrime_v23',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v16',
        'HLT_Dimuon18_PsiPrime_v24',
        'HLT_Dimuon24_Phi_noCorrL1_v16',
        'HLT_Dimuon24_Upsilon_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_v24',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v16',
        'HLT_DoubleMu2_Jpsi_LowPt_v4',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v14',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v14',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v16',
        'HLT_DoubleMu3_Trk_Tau3mu_v22',
        'HLT_DoubleMu4_3_Bs_v25',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_3_Jpsi_v25',
        'HLT_DoubleMu4_3_LowMass_SS_v4',
        'HLT_DoubleMu4_3_LowMass_v11',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v17',
        'HLT_DoubleMu4_JpsiTrk_Bc_v10',
        'HLT_DoubleMu4_Jpsi_Displaced_v17',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v17',
        'HLT_DoubleMu4_LowMass_Displaced_v11',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v25',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v14',
        'HLT_Mu25_TkMu0_Phi_v18',
        'HLT_Mu30_TkMu0_Psi_v11',
        'HLT_Mu30_TkMu0_Upsilon_v11',
        'HLT_Mu4_L1DoubleMu_v11',
        'HLT_Mu7p5_L2Mu2_Jpsi_v20',
        'HLT_Mu7p5_L2Mu2_Upsilon_v20',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v14',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v15',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v12'
    ),
    ParkingDoubleMuonLowMass1 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v15',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_v18',
        'HLT_Dimuon0_Jpsi_v18',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v18',
        'HLT_Dimuon0_LowMass_L1_4_v18',
        'HLT_Dimuon0_LowMass_L1_TM530_v16',
        'HLT_Dimuon0_LowMass_v18',
        'HLT_Dimuon0_Upsilon_L1_4p5_v19',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v17',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v19',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v16',
        'HLT_Dimuon0_Upsilon_NoVertexing_v17',
        'HLT_Dimuon10_Upsilon_y1p4_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v12',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v17',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v15',
        'HLT_Dimuon14_PsiPrime_v23',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v16',
        'HLT_Dimuon18_PsiPrime_v24',
        'HLT_Dimuon24_Phi_noCorrL1_v16',
        'HLT_Dimuon24_Upsilon_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_v24',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v16',
        'HLT_DoubleMu2_Jpsi_LowPt_v4',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v14',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v14',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v16',
        'HLT_DoubleMu3_Trk_Tau3mu_v22',
        'HLT_DoubleMu4_3_Bs_v25',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_3_Jpsi_v25',
        'HLT_DoubleMu4_3_LowMass_SS_v4',
        'HLT_DoubleMu4_3_LowMass_v11',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v17',
        'HLT_DoubleMu4_JpsiTrk_Bc_v10',
        'HLT_DoubleMu4_Jpsi_Displaced_v17',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v17',
        'HLT_DoubleMu4_LowMass_Displaced_v11',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v25',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v14',
        'HLT_Mu25_TkMu0_Phi_v18',
        'HLT_Mu30_TkMu0_Psi_v11',
        'HLT_Mu30_TkMu0_Upsilon_v11',
        'HLT_Mu4_L1DoubleMu_v11',
        'HLT_Mu7p5_L2Mu2_Jpsi_v20',
        'HLT_Mu7p5_L2Mu2_Upsilon_v20',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v14',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v15',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v12'
    ),
    ParkingDoubleMuonLowMass2 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v15',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_v18',
        'HLT_Dimuon0_Jpsi_v18',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v18',
        'HLT_Dimuon0_LowMass_L1_4_v18',
        'HLT_Dimuon0_LowMass_L1_TM530_v16',
        'HLT_Dimuon0_LowMass_v18',
        'HLT_Dimuon0_Upsilon_L1_4p5_v19',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v17',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v19',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v16',
        'HLT_Dimuon0_Upsilon_NoVertexing_v17',
        'HLT_Dimuon10_Upsilon_y1p4_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v12',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v17',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v15',
        'HLT_Dimuon14_PsiPrime_v23',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v16',
        'HLT_Dimuon18_PsiPrime_v24',
        'HLT_Dimuon24_Phi_noCorrL1_v16',
        'HLT_Dimuon24_Upsilon_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_v24',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v16',
        'HLT_DoubleMu2_Jpsi_LowPt_v4',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v14',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v14',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v16',
        'HLT_DoubleMu3_Trk_Tau3mu_v22',
        'HLT_DoubleMu4_3_Bs_v25',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_3_Jpsi_v25',
        'HLT_DoubleMu4_3_LowMass_SS_v4',
        'HLT_DoubleMu4_3_LowMass_v11',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v17',
        'HLT_DoubleMu4_JpsiTrk_Bc_v10',
        'HLT_DoubleMu4_Jpsi_Displaced_v17',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v17',
        'HLT_DoubleMu4_LowMass_Displaced_v11',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v25',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v14',
        'HLT_Mu25_TkMu0_Phi_v18',
        'HLT_Mu30_TkMu0_Psi_v11',
        'HLT_Mu30_TkMu0_Upsilon_v11',
        'HLT_Mu4_L1DoubleMu_v11',
        'HLT_Mu7p5_L2Mu2_Jpsi_v20',
        'HLT_Mu7p5_L2Mu2_Upsilon_v20',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v14',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v15',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v12'
    ),
    ParkingDoubleMuonLowMass3 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v15',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_v18',
        'HLT_Dimuon0_Jpsi_v18',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v18',
        'HLT_Dimuon0_LowMass_L1_4_v18',
        'HLT_Dimuon0_LowMass_L1_TM530_v16',
        'HLT_Dimuon0_LowMass_v18',
        'HLT_Dimuon0_Upsilon_L1_4p5_v19',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v17',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v19',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v16',
        'HLT_Dimuon0_Upsilon_NoVertexing_v17',
        'HLT_Dimuon10_Upsilon_y1p4_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v12',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v17',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v15',
        'HLT_Dimuon14_PsiPrime_v23',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v16',
        'HLT_Dimuon18_PsiPrime_v24',
        'HLT_Dimuon24_Phi_noCorrL1_v16',
        'HLT_Dimuon24_Upsilon_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_v24',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v16',
        'HLT_DoubleMu2_Jpsi_LowPt_v4',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v14',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v14',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v16',
        'HLT_DoubleMu3_Trk_Tau3mu_v22',
        'HLT_DoubleMu4_3_Bs_v25',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_3_Jpsi_v25',
        'HLT_DoubleMu4_3_LowMass_SS_v4',
        'HLT_DoubleMu4_3_LowMass_v11',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v17',
        'HLT_DoubleMu4_JpsiTrk_Bc_v10',
        'HLT_DoubleMu4_Jpsi_Displaced_v17',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v17',
        'HLT_DoubleMu4_LowMass_Displaced_v11',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v25',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v14',
        'HLT_Mu25_TkMu0_Phi_v18',
        'HLT_Mu30_TkMu0_Psi_v11',
        'HLT_Mu30_TkMu0_Upsilon_v11',
        'HLT_Mu4_L1DoubleMu_v11',
        'HLT_Mu7p5_L2Mu2_Jpsi_v20',
        'HLT_Mu7p5_L2Mu2_Upsilon_v20',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v14',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v15',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v12'
    ),
    ParkingDoubleMuonLowMass4 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v15',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_v18',
        'HLT_Dimuon0_Jpsi_v18',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v18',
        'HLT_Dimuon0_LowMass_L1_4_v18',
        'HLT_Dimuon0_LowMass_L1_TM530_v16',
        'HLT_Dimuon0_LowMass_v18',
        'HLT_Dimuon0_Upsilon_L1_4p5_v19',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v17',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v19',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v16',
        'HLT_Dimuon0_Upsilon_NoVertexing_v17',
        'HLT_Dimuon10_Upsilon_y1p4_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v12',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v17',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v15',
        'HLT_Dimuon14_PsiPrime_v23',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v16',
        'HLT_Dimuon18_PsiPrime_v24',
        'HLT_Dimuon24_Phi_noCorrL1_v16',
        'HLT_Dimuon24_Upsilon_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_v24',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v16',
        'HLT_DoubleMu2_Jpsi_LowPt_v4',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v14',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v14',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v16',
        'HLT_DoubleMu3_Trk_Tau3mu_v22',
        'HLT_DoubleMu4_3_Bs_v25',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_3_Jpsi_v25',
        'HLT_DoubleMu4_3_LowMass_SS_v4',
        'HLT_DoubleMu4_3_LowMass_v11',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v17',
        'HLT_DoubleMu4_JpsiTrk_Bc_v10',
        'HLT_DoubleMu4_Jpsi_Displaced_v17',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v17',
        'HLT_DoubleMu4_LowMass_Displaced_v11',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v25',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v14',
        'HLT_Mu25_TkMu0_Phi_v18',
        'HLT_Mu30_TkMu0_Psi_v11',
        'HLT_Mu30_TkMu0_Upsilon_v11',
        'HLT_Mu4_L1DoubleMu_v11',
        'HLT_Mu7p5_L2Mu2_Jpsi_v20',
        'HLT_Mu7p5_L2Mu2_Upsilon_v20',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v14',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v15',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v12'
    ),
    ParkingDoubleMuonLowMass5 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v15',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_v18',
        'HLT_Dimuon0_Jpsi_v18',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v18',
        'HLT_Dimuon0_LowMass_L1_4_v18',
        'HLT_Dimuon0_LowMass_L1_TM530_v16',
        'HLT_Dimuon0_LowMass_v18',
        'HLT_Dimuon0_Upsilon_L1_4p5_v19',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v17',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v19',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v16',
        'HLT_Dimuon0_Upsilon_NoVertexing_v17',
        'HLT_Dimuon10_Upsilon_y1p4_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v12',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v17',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v15',
        'HLT_Dimuon14_PsiPrime_v23',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v16',
        'HLT_Dimuon18_PsiPrime_v24',
        'HLT_Dimuon24_Phi_noCorrL1_v16',
        'HLT_Dimuon24_Upsilon_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_v24',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v16',
        'HLT_DoubleMu2_Jpsi_LowPt_v4',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v14',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v14',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v16',
        'HLT_DoubleMu3_Trk_Tau3mu_v22',
        'HLT_DoubleMu4_3_Bs_v25',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_3_Jpsi_v25',
        'HLT_DoubleMu4_3_LowMass_SS_v4',
        'HLT_DoubleMu4_3_LowMass_v11',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v17',
        'HLT_DoubleMu4_JpsiTrk_Bc_v10',
        'HLT_DoubleMu4_Jpsi_Displaced_v17',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v17',
        'HLT_DoubleMu4_LowMass_Displaced_v11',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v25',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v14',
        'HLT_Mu25_TkMu0_Phi_v18',
        'HLT_Mu30_TkMu0_Psi_v11',
        'HLT_Mu30_TkMu0_Upsilon_v11',
        'HLT_Mu4_L1DoubleMu_v11',
        'HLT_Mu7p5_L2Mu2_Jpsi_v20',
        'HLT_Mu7p5_L2Mu2_Upsilon_v20',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v14',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v15',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v12'
    ),
    ParkingDoubleMuonLowMass6 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v15',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_v18',
        'HLT_Dimuon0_Jpsi_v18',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v18',
        'HLT_Dimuon0_LowMass_L1_4_v18',
        'HLT_Dimuon0_LowMass_L1_TM530_v16',
        'HLT_Dimuon0_LowMass_v18',
        'HLT_Dimuon0_Upsilon_L1_4p5_v19',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v17',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v19',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v16',
        'HLT_Dimuon0_Upsilon_NoVertexing_v17',
        'HLT_Dimuon10_Upsilon_y1p4_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v12',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v17',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v15',
        'HLT_Dimuon14_PsiPrime_v23',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v16',
        'HLT_Dimuon18_PsiPrime_v24',
        'HLT_Dimuon24_Phi_noCorrL1_v16',
        'HLT_Dimuon24_Upsilon_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_v24',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v16',
        'HLT_DoubleMu2_Jpsi_LowPt_v4',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v14',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v14',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v16',
        'HLT_DoubleMu3_Trk_Tau3mu_v22',
        'HLT_DoubleMu4_3_Bs_v25',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_3_Jpsi_v25',
        'HLT_DoubleMu4_3_LowMass_SS_v4',
        'HLT_DoubleMu4_3_LowMass_v11',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v17',
        'HLT_DoubleMu4_JpsiTrk_Bc_v10',
        'HLT_DoubleMu4_Jpsi_Displaced_v17',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v17',
        'HLT_DoubleMu4_LowMass_Displaced_v11',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v25',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v14',
        'HLT_Mu25_TkMu0_Phi_v18',
        'HLT_Mu30_TkMu0_Psi_v11',
        'HLT_Mu30_TkMu0_Upsilon_v11',
        'HLT_Mu4_L1DoubleMu_v11',
        'HLT_Mu7p5_L2Mu2_Jpsi_v20',
        'HLT_Mu7p5_L2Mu2_Upsilon_v20',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v14',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v15',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v12'
    ),
    ParkingDoubleMuonLowMass7 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v15',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v17',
        'HLT_Dimuon0_Jpsi_NoVertexing_v18',
        'HLT_Dimuon0_Jpsi_v18',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v18',
        'HLT_Dimuon0_LowMass_L1_4_v18',
        'HLT_Dimuon0_LowMass_L1_TM530_v16',
        'HLT_Dimuon0_LowMass_v18',
        'HLT_Dimuon0_Upsilon_L1_4p5_v19',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v17',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v19',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v16',
        'HLT_Dimuon0_Upsilon_NoVertexing_v17',
        'HLT_Dimuon10_Upsilon_y1p4_v11',
        'HLT_Dimuon12_Upsilon_y1p4_v12',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v17',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v15',
        'HLT_Dimuon14_PsiPrime_v23',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v16',
        'HLT_Dimuon18_PsiPrime_v24',
        'HLT_Dimuon24_Phi_noCorrL1_v16',
        'HLT_Dimuon24_Upsilon_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_noCorrL1_v16',
        'HLT_Dimuon25_Jpsi_v24',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v16',
        'HLT_DoubleMu2_Jpsi_LowPt_v4',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v14',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v14',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v16',
        'HLT_DoubleMu3_Trk_Tau3mu_v22',
        'HLT_DoubleMu4_3_Bs_v25',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_3_Jpsi_v25',
        'HLT_DoubleMu4_3_LowMass_SS_v4',
        'HLT_DoubleMu4_3_LowMass_v11',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v10',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v17',
        'HLT_DoubleMu4_JpsiTrk_Bc_v10',
        'HLT_DoubleMu4_Jpsi_Displaced_v17',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v17',
        'HLT_DoubleMu4_LowMass_Displaced_v11',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v25',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v14',
        'HLT_Mu25_TkMu0_Phi_v18',
        'HLT_Mu30_TkMu0_Psi_v11',
        'HLT_Mu30_TkMu0_Upsilon_v11',
        'HLT_Mu4_L1DoubleMu_v11',
        'HLT_Mu7p5_L2Mu2_Jpsi_v20',
        'HLT_Mu7p5_L2Mu2_Upsilon_v20',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v14',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v14',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v15',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v12'
    ),
    ParkingHH = cms.vstring(
        'HLT_PFHT250_QuadPFJet25_PNet1BTag0p20_PNet1Tauh0p50_v4',
        'HLT_PFHT250_QuadPFJet25_PNet2BTagMean0p55_v4',
        'HLT_PFHT250_QuadPFJet25_v4',
        'HLT_PFHT250_QuadPFJet30_PNet1BTag0p20_PNet1Tauh0p50_v4',
        'HLT_PFHT250_QuadPFJet30_PNet2BTagMean0p55_v4',
        'HLT_PFHT280_QuadPFJet30_PNet1BTag0p20_PNet1Tauh0p50_v4',
        'HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v7',
        'HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p60_v7',
        'HLT_PFHT280_QuadPFJet30_v7',
        'HLT_PFHT280_QuadPFJet35_PNet2BTagMean0p60_v7',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_PNet3BTag_2p0_v3',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_PNet3BTag_4p3_v3',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v11',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v19',
        'HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70_v8',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_PNet2BTag_4p3_v4',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_PNet2BTag_5p6_v4',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_v4',
        'HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50_v7',
        'HLT_PFHT400_SixPFJet32_v19',
        'HLT_PFHT450_SixPFJet36_PNetBTag0p35_v7',
        'HLT_PFHT450_SixPFJet36_v18'
    ),
    ParkingLLP = cms.vstring(
        'HLT_HT350_DelayedJet40_SingleDelay1p5To3p5nsInclusive_v5',
        'HLT_HT350_DelayedJet40_SingleDelay1p6To3p5nsInclusive_v5',
        'HLT_HT350_DelayedJet40_SingleDelay1p75To3p5nsInclusive_v5',
        'HLT_HT360_DisplacedDijet40_Inclusive1PtrkShortSig5_v5',
        'HLT_HT360_DisplacedDijet45_Inclusive1PtrkShortSig5_v5',
        'HLT_HT390_DisplacedDijet40_Inclusive1PtrkShortSig5_v5',
        'HLT_HT390_DisplacedDijet45_Inclusive1PtrkShortSig5_v5',
        'HLT_HT390eta2p0_DisplacedDijet40_Inclusive1PtrkShortSig5_v5',
        'HLT_HT430_DelayedJet40_SingleDelay1To1p5nsInclusive_v5',
        'HLT_HT430_DelayedJet40_SingleDelay1p1To1p6nsInclusive_v5',
        'HLT_HT430_DelayedJet40_SingleDelay1p25To1p75nsInclusive_v5',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v21',
        'HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5_v9',
        'HLT_HT650_DisplacedDijet60_Inclusive_v21',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5To4nsInclusive_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p6To4nsInclusive_v5',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75To4nsInclusive_v5'
    ),
    ParkingSingleMuon0 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon1 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon10 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon11 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon2 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon3 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon4 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon5 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon6 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon7 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon8 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingSingleMuon9 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v4',
        'HLT_Mu0_Barrel_L1HP11_v4',
        'HLT_Mu0_Barrel_L1HP6_IP6_v1',
        'HLT_Mu0_Barrel_L1HP6_v1',
        'HLT_Mu0_Barrel_L1HP7_v1',
        'HLT_Mu0_Barrel_L1HP8_v2',
        'HLT_Mu0_Barrel_L1HP9_v2',
        'HLT_Mu0_Barrel_v4',
        'HLT_Mu10_Barrel_L1HP11_IP6_v4',
        'HLT_Mu6_Barrel_L1HP7_IP6_v1',
        'HLT_Mu7_Barrel_L1HP8_IP6_v2',
        'HLT_Mu8_Barrel_L1HP9_IP6_v2',
        'HLT_Mu9_Barrel_L1HP10_IP6_v4'
    ),
    ParkingVBF0 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet100_88_70_30_v8',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet103_88_75_15_v15',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet105_88_75_30_v7',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet105_88_76_15_v15',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet111_90_80_15_v15',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v8',
        'HLT_QuadPFJet111_90_80_30_v7',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v6',
        'HLT_VBF_DiPFJet125_45_Mjj1200_v4',
        'HLT_VBF_DiPFJet45_Mjj650_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet45_Mjj750_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v4',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v4',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v4',
        'HLT_VBF_DiPFJet75_45_Mjj850_DiPFJet60_v4',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v11',
        'HLT_VBF_DoublePNetTauhPFJet20_eta2p2_v4'
    ),
    ParkingVBF1 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet100_88_70_30_v8',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet103_88_75_15_v15',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet105_88_75_30_v7',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet105_88_76_15_v15',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet111_90_80_15_v15',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v8',
        'HLT_QuadPFJet111_90_80_30_v7',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v6',
        'HLT_VBF_DiPFJet125_45_Mjj1200_v4',
        'HLT_VBF_DiPFJet45_Mjj650_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet45_Mjj750_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v4',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v4',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v4',
        'HLT_VBF_DiPFJet75_45_Mjj850_DiPFJet60_v4',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v11',
        'HLT_VBF_DoublePNetTauhPFJet20_eta2p2_v4'
    ),
    ParkingVBF2 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet100_88_70_30_v8',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet103_88_75_15_v15',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet105_88_75_30_v7',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet105_88_76_15_v15',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet111_90_80_15_v15',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v8',
        'HLT_QuadPFJet111_90_80_30_v7',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v6',
        'HLT_VBF_DiPFJet125_45_Mjj1200_v4',
        'HLT_VBF_DiPFJet45_Mjj650_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet45_Mjj750_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v4',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v4',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v4',
        'HLT_VBF_DiPFJet75_45_Mjj850_DiPFJet60_v4',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v11',
        'HLT_VBF_DoublePNetTauhPFJet20_eta2p2_v4'
    ),
    ParkingVBF3 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet100_88_70_30_v8',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet103_88_75_15_v15',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet105_88_75_30_v7',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet105_88_76_15_v15',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet111_90_80_15_v15',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v8',
        'HLT_QuadPFJet111_90_80_30_v7',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v6',
        'HLT_VBF_DiPFJet125_45_Mjj1200_v4',
        'HLT_VBF_DiPFJet45_Mjj650_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet45_Mjj750_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v4',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v4',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v4',
        'HLT_VBF_DiPFJet75_45_Mjj850_DiPFJet60_v4',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v11',
        'HLT_VBF_DoublePNetTauhPFJet20_eta2p2_v4'
    ),
    ParkingVBF4 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet100_88_70_30_v8',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet103_88_75_15_v15',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet105_88_75_30_v7',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet105_88_76_15_v15',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet111_90_80_15_v15',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v8',
        'HLT_QuadPFJet111_90_80_30_v7',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v6',
        'HLT_VBF_DiPFJet125_45_Mjj1200_v4',
        'HLT_VBF_DiPFJet45_Mjj650_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet45_Mjj750_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v4',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v4',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v4',
        'HLT_VBF_DiPFJet75_45_Mjj850_DiPFJet60_v4',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v11',
        'HLT_VBF_DoublePNetTauhPFJet20_eta2p2_v4'
    ),
    ParkingVBF5 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet100_88_70_30_v8',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet103_88_75_15_v15',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet105_88_75_30_v7',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet105_88_76_15_v15',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet111_90_80_15_v15',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v8',
        'HLT_QuadPFJet111_90_80_30_v7',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v6',
        'HLT_VBF_DiPFJet125_45_Mjj1200_v4',
        'HLT_VBF_DiPFJet45_Mjj650_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet45_Mjj750_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v4',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v4',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v4',
        'HLT_VBF_DiPFJet75_45_Mjj850_DiPFJet60_v4',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v11',
        'HLT_VBF_DoublePNetTauhPFJet20_eta2p2_v4'
    ),
    ParkingVBF6 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet100_88_70_30_v8',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet103_88_75_15_v15',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet105_88_75_30_v7',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet105_88_76_15_v15',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet111_90_80_15_v15',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v8',
        'HLT_QuadPFJet111_90_80_30_v7',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v6',
        'HLT_VBF_DiPFJet125_45_Mjj1200_v4',
        'HLT_VBF_DiPFJet45_Mjj650_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet45_Mjj750_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v4',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v4',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v4',
        'HLT_VBF_DiPFJet75_45_Mjj850_DiPFJet60_v4',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v11',
        'HLT_VBF_DoublePNetTauhPFJet20_eta2p2_v4'
    ),
    ParkingVBF7 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet100_88_70_30_v8',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet103_88_75_15_v15',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v8',
        'HLT_QuadPFJet105_88_75_30_v7',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet105_88_76_15_v15',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v4',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v4',
        'HLT_QuadPFJet111_90_80_15_v15',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v8',
        'HLT_QuadPFJet111_90_80_30_v7',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v6',
        'HLT_VBF_DiPFJet125_45_Mjj1200_v4',
        'HLT_VBF_DiPFJet45_Mjj650_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet45_Mjj750_MediumDeepTauPFTauHPS45_L2NN_eta2p1_v4',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v4',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Ele22_eta2p1_WPTight_Gsf_v4',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v4',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v4',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v4',
        'HLT_VBF_DiPFJet75_45_Mjj850_DiPFJet60_v4',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v4',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v4',
        'HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1_v11',
        'HLT_VBF_DoublePNetTauhPFJet20_eta2p2_v4'
    ),
    RPCMonitor = cms.vstring('AlCa_RPCMuonNormalisation_v21'),
    ScoutingPFMonitor = cms.vstring(
        'DST_PFScouting_AXOLoose_v2',
        'DST_PFScouting_AXONominal_v4',
        'DST_PFScouting_AXOTight_v4',
        'DST_PFScouting_AXOVLoose_v2',
        'DST_PFScouting_AXOVTight_v2',
        'DST_PFScouting_CICADALoose_v1',
        'DST_PFScouting_CICADAMedium_v1',
        'DST_PFScouting_CICADATight_v1',
        'DST_PFScouting_CICADAVLoose_v1',
        'DST_PFScouting_CICADAVTight_v1',
        'DST_PFScouting_DoubleEG_v4',
        'DST_PFScouting_DoubleMuon_v4',
        'DST_PFScouting_JetHT_v4',
        'DST_PFScouting_SingleMuon_v4',
        'DST_PFScouting_SinglePhotonEB_v1',
        'DST_PFScouting_ZeroBias_v2',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v23',
        'HLT_Ele35_WPTight_Gsf_v17',
        'HLT_IsoMu27_v26',
        'HLT_Mu50_v23',
        'HLT_PFHT1050_v28',
        'HLT_Photon200_v22'
    ),
    ScoutingPFRun3 = cms.vstring(
        'DST_PFScouting_AXOLoose_v2',
        'DST_PFScouting_AXONominal_v4',
        'DST_PFScouting_AXOTight_v4',
        'DST_PFScouting_AXOVLoose_v2',
        'DST_PFScouting_AXOVTight_v2',
        'DST_PFScouting_CICADALoose_v1',
        'DST_PFScouting_CICADAMedium_v1',
        'DST_PFScouting_CICADATight_v1',
        'DST_PFScouting_CICADAVLoose_v1',
        'DST_PFScouting_CICADAVTight_v1',
        'DST_PFScouting_DatasetMuon_v4',
        'DST_PFScouting_DoubleEG_v4',
        'DST_PFScouting_DoubleMuon_v4',
        'DST_PFScouting_JetHT_v4',
        'DST_PFScouting_SingleMuon_v4',
        'DST_PFScouting_SinglePhotonEB_v1',
        'DST_PFScouting_ZeroBias_v2'
    ),
    Tau = cms.vstring(
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_noDxy_v6',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_v11',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS36_Trk1_eta2p1_v6',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_v6',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_v10',
        'HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_v10',
        'HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1_v10',
        'HLT_DoublePNetTauhPFJet26_L2NN_eta2p3_PFJet60_v4',
        'HLT_DoublePNetTauhPFJet26_L2NN_eta2p3_PFJet75_v4',
        'HLT_DoublePNetTauhPFJet30_Medium_L2NN_eta2p3_v4',
        'HLT_DoublePNetTauhPFJet30_Tight_L2NN_eta2p3_v4',
        'HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1_v11',
        'HLT_SinglePNetTauhPFJet130_Loose_L2NN_eta2p3_v4',
        'HLT_SinglePNetTauhPFJet130_Medium_L2NN_eta2p3_v4',
        'HLT_SinglePNetTauhPFJet130_Tight_L2NN_eta2p3_v4'
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
        'HLT_ZeroBias_Alignment_v6',
        'HLT_ZeroBias_FirstBXAfterTrain_v8',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v10',
        'HLT_ZeroBias_FirstCollisionInTrain_v9',
        'HLT_ZeroBias_IsolatedBunches_v10',
        'HLT_ZeroBias_LastCollisionInTrain_v8',
        'HLT_ZeroBias_v11'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
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
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm4',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp4',
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
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
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
        'JetMET/vertices',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_pt',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_eta',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_phi',
        'Muons/MuonRecoAnalyzer/Res_TkGlb_qOverlap',
        'Muons/diMuonHistograms/GlbGlbMuon_LM',
        'Muons/diMuonHistograms/GlbGlbMuon_HM',
        'Muons/Isolation/global/relPFIso_R03',
        'Muons/globalMuons/GeneralProperties/NumberOfMeanRecHitsPerTrack_glb',
        'Muons/standAloneMuonsUpdatedAtVtx/HitProperties/NumberOfValidRecHitsPerTrack_sta',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_pt',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_eta'
    )
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
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
    modulesToCallForTryToContinue = cms.untracked.vstring(),
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
    HLTMonitor = cms.vstring('HLTMonitor'),
    NanoDST = cms.vstring('L1Accept'),
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
    ParkingSingleMuon0 = cms.vstring('ParkingSingleMuon0'),
    ParkingSingleMuon1 = cms.vstring('ParkingSingleMuon1'),
    ParkingSingleMuon10 = cms.vstring('ParkingSingleMuon10'),
    ParkingSingleMuon11 = cms.vstring('ParkingSingleMuon11'),
    ParkingSingleMuon2 = cms.vstring('ParkingSingleMuon2'),
    ParkingSingleMuon3 = cms.vstring('ParkingSingleMuon3'),
    ParkingSingleMuon4 = cms.vstring('ParkingSingleMuon4'),
    ParkingSingleMuon5 = cms.vstring('ParkingSingleMuon5'),
    ParkingSingleMuon6 = cms.vstring('ParkingSingleMuon6'),
    ParkingSingleMuon7 = cms.vstring('ParkingSingleMuon7'),
    ParkingSingleMuon8 = cms.vstring('ParkingSingleMuon8'),
    ParkingSingleMuon9 = cms.vstring('ParkingSingleMuon9'),
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


process.hltPSetMap = cms.EDProducer("ParameterSetBlobProducer")


process.hltTriggerSummaryAOD = cms.EDProducer("TriggerSummaryProducerAOD",
    moduleLabelPatternsToMatch = cms.vstring('hlt*'),
    moduleLabelPatternsToSkip = cms.vstring(),
    processName = cms.string('@'),
    throw = cms.bool(False)
)


process.hltTriggerSummaryRAW = cms.EDProducer("TriggerSummaryProducerRAW",
    processName = cms.string('@')
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
    useHCALFBLUT = cms.bool(False),
    useHCALLUT = cms.bool(True),
    useHFLUT = cms.bool(True),
    useLSB = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.simCaloStage2Layer1Summary = cms.EDProducer("L1TCaloSummaryCICADAv2",
    CICADAModelVersion = cms.string('CICADAModel_v2p1'),
    boostedJetPtFactor = cms.double(1.5),
    caloScaleFactor = cms.double(0.5),
    eGammaIsolationFactor = cms.double(0.3),
    eGammaSeed = cms.uint32(5),
    firmwareVersion = cms.int32(1),
    jetSeed = cms.uint32(10),
    nPumBins = cms.uint32(18),
    pumLUT00n = cms.vdouble(
        0.43, 0.32, 0.29, 0.36, 0.33,
        0.25, 0.25, 0.25, 0.25, 0.25,
        0.25, 0.25, 0.25
    ),
    pumLUT00p = cms.vdouble(
        0.45, 0.32, 0.29, 0.35, 0.31,
        0.25, 0.25, 0.25, 0.25, 0.25,
        0.25, 0.25, 0.25
    ),
    pumLUT01n = cms.vdouble(
        0.6, 0.39, 0.33, 0.44, 0.39,
        0.26, 0.27, 0.26, 0.26, 0.25,
        0.25, 0.25, 0.25
    ),
    pumLUT01p = cms.vdouble(
        0.6, 0.39, 0.33, 0.41, 0.35,
        0.26, 0.27, 0.26, 0.26, 0.25,
        0.25, 0.25, 0.25
    ),
    pumLUT02n = cms.vdouble(
        0.76, 0.52, 0.46, 0.57, 0.52,
        0.33, 0.41, 0.34, 0.31, 0.29,
        0.27, 0.26, 0.25
    ),
    pumLUT02p = cms.vdouble(
        0.75, 0.52, 0.46, 0.55, 0.48,
        0.34, 0.42, 0.34, 0.31, 0.29,
        0.27, 0.26, 0.25
    ),
    pumLUT03n = cms.vdouble(
        0.9, 0.63, 0.56, 0.69, 0.62,
        0.39, 0.58, 0.41, 0.37, 0.33,
        0.29, 0.27, 0.25
    ),
    pumLUT03p = cms.vdouble(
        0.9, 0.64, 0.56, 0.66, 0.57,
        0.39, 0.58, 0.41, 0.37, 0.33,
        0.29, 0.26, 0.25
    ),
    pumLUT04n = cms.vdouble(
        1.03, 0.74, 0.66, 0.8, 0.72,
        0.45, 0.8, 0.5, 0.45, 0.39,
        0.32, 0.28, 0.25
    ),
    pumLUT04p = cms.vdouble(
        1.03, 0.76, 0.67, 0.77, 0.67,
        0.46, 0.81, 0.5, 0.45, 0.39,
        0.32, 0.27, 0.25
    ),
    pumLUT05n = cms.vdouble(
        1.17, 0.86, 0.77, 0.92, 0.83,
        0.53, 1.09, 0.6, 0.55, 0.47,
        0.37, 0.29, 0.26
    ),
    pumLUT05p = cms.vdouble(
        1.18, 0.88, 0.77, 0.89, 0.77,
        0.54, 1.1, 0.61, 0.55, 0.47,
        0.35, 0.29, 0.26
    ),
    pumLUT06n = cms.vdouble(
        1.32, 0.98, 0.88, 1.04, 0.93,
        0.61, 1.44, 0.72, 0.66, 0.57,
        0.42, 0.31, 0.26
    ),
    pumLUT06p = cms.vdouble(
        1.32, 1.0, 0.89, 1.01, 0.88,
        0.63, 1.46, 0.73, 0.67, 0.57,
        0.41, 0.3, 0.26
    ),
    pumLUT07n = cms.vdouble(
        1.47, 1.11, 1.01, 1.17, 1.05,
        0.71, 1.86, 0.86, 0.81, 0.69,
        0.5, 0.34, 0.27
    ),
    pumLUT07p = cms.vdouble(
        1.48, 1.14, 1.01, 1.13, 0.99,
        0.73, 1.89, 0.87, 0.82, 0.7,
        0.47, 0.33, 0.27
    ),
    pumLUT08n = cms.vdouble(
        1.63, 1.26, 1.14, 1.3, 1.17,
        0.82, 2.37, 1.02, 0.98, 0.85,
        0.59, 0.37, 0.28
    ),
    pumLUT08p = cms.vdouble(
        1.64, 1.28, 1.15, 1.26, 1.11,
        0.85, 2.41, 1.03, 0.99, 0.86,
        0.56, 0.36, 0.28
    ),
    pumLUT09n = cms.vdouble(
        1.81, 1.41, 1.28, 1.45, 1.31,
        0.95, 2.98, 1.2, 1.18, 1.03,
        0.71, 0.42, 0.3
    ),
    pumLUT09p = cms.vdouble(
        1.82, 1.45, 1.29, 1.41, 1.24,
        0.98, 3.02, 1.21, 1.19, 1.05,
        0.67, 0.4, 0.29
    ),
    pumLUT10n = cms.vdouble(
        2.01, 1.58, 1.43, 1.62, 1.45,
        1.1, 3.7, 1.41, 1.42, 1.26,
        0.87, 0.48, 0.32
    ),
    pumLUT10p = cms.vdouble(
        2.02, 1.61, 1.46, 1.58, 1.38,
        1.13, 3.73, 1.42, 1.43, 1.27,
        0.82, 0.46, 0.31
    ),
    pumLUT11n = cms.vdouble(
        2.24, 1.78, 1.61, 1.78, 1.6,
        1.27, 4.55, 1.64, 1.71, 1.55,
        1.08, 0.57, 0.36
    ),
    pumLUT11p = cms.vdouble(
        2.21, 1.82, 1.63, 1.75, 1.53,
        1.31, 4.67, 1.67, 1.71, 1.57,
        1.01, 0.54, 0.36
    ),
    pumLUT12n = cms.vdouble(
        2.5, 2.0, 1.82, 1.91, 1.81,
        1.56, 5.56, 1.85, 2.01, 1.87,
        1.31, 0.68, 0.42
    ),
    pumLUT12p = cms.vdouble(
        2.44, 2.02, 1.9, 2.01, 1.7,
        1.51, 5.61, 1.96, 2.04, 1.8,
        1.24, 0.65, 0.43
    ),
    pumLUT13n = cms.vdouble(
        2.96, 2.4, 2.14, 2.41, 2.01,
        1.76, 8.05, 2.41, 2.43, 2.17,
        1.67, 0.9, 0.59
    ),
    pumLUT13p = cms.vdouble(
        3.28, 2.64, 2.26, 2.23, 1.97,
        1.89, 7.61, 2.27, 2.33, 2.26,
        1.44, 0.79, 0.52
    ),
    pumLUT14n = cms.vdouble(
        2.96, 2.4, 2.14, 2.41, 2.01,
        1.76, 8.05, 2.41, 2.43, 2.17,
        1.67, 0.9, 0.59
    ),
    pumLUT14p = cms.vdouble(
        3.28, 2.64, 2.26, 2.23, 1.97,
        1.89, 7.61, 2.27, 2.33, 2.26,
        1.44, 0.79, 0.52
    ),
    pumLUT15n = cms.vdouble(
        2.96, 2.4, 2.14, 2.41, 2.01,
        1.76, 8.05, 2.41, 2.43, 2.17,
        1.67, 0.9, 0.59
    ),
    pumLUT15p = cms.vdouble(
        3.28, 2.64, 2.26, 2.23, 1.97,
        1.89, 7.61, 2.27, 2.33, 2.26,
        1.44, 0.79, 0.52
    ),
    pumLUT16n = cms.vdouble(
        2.96, 2.4, 2.14, 2.41, 2.01,
        1.76, 8.05, 2.41, 2.43, 2.17,
        1.67, 0.9, 0.59
    ),
    pumLUT16p = cms.vdouble(
        3.28, 2.64, 2.26, 2.23, 1.97,
        1.89, 7.61, 2.27, 2.33, 2.26,
        1.44, 0.79, 0.52
    ),
    pumLUT17n = cms.vdouble(
        2.96, 2.4, 2.14, 2.41, 2.01,
        1.76, 8.05, 2.41, 2.43, 2.17,
        1.67, 0.9, 0.59
    ),
    pumLUT17p = cms.vdouble(
        3.28, 2.64, 2.26, 2.23, 1.97,
        1.89, 7.61, 2.27, 2.33, 2.26,
        1.44, 0.79, 0.52
    ),
    tauIsolationFactor = cms.double(0.3),
    tauSeed = cms.uint32(10),
    testPatterns = cms.VPSet(
        cms.PSet(
            iPhi_1 = cms.vuint32(
                0, 0, 1, 0, 1,
                0, 2, 3, 0, 0,
                0, 3, 6, 0
            ),
            iPhi_10 = cms.vuint32(
                0, 0, 1, 0, 12,
                2, 0, 0, 0, 1,
                0, 1, 0, 2
            ),
            iPhi_11 = cms.vuint32(
                5, 0, 0, 1, 0,
                0, 1, 4, 2, 0,
                15, 0, 0, 212
            ),
            iPhi_12 = cms.vuint32(
                4, 0, 2, 0, 2,
                1, 1, 4, 1, 0,
                2, 3, 0, 0
            ),
            iPhi_13 = cms.vuint32(
                0, 4, 1, 2, 182,
                0, 2, 2, 0, 0,
                0, 1, 1, 0
            ),
            iPhi_14 = cms.vuint32(
                0, 10, 0, 0, 0,
                0, 1, 1, 1, 0,
                1, 0, 0, 2
            ),
            iPhi_15 = cms.vuint32(
                6, 1, 0, 1, 0,
                1, 0, 0, 0, 1,
                0, 0, 1, 12
            ),
            iPhi_16 = cms.vuint32(
                0, 0, 0, 1, 0,
                1, 0, 0, 3, 1,
                0, 0, 0, 1
            ),
            iPhi_17 = cms.vuint32(
                0, 0, 0, 0, 0,
                2, 0, 4, 2, 0,
                3, 0, 0, 2
            ),
            iPhi_18 = cms.vuint32(
                2, 0, 0, 0, 0,
                1, 0, 4, 0, 2,
                4, 5, 0, 0
            ),
            iPhi_2 = cms.vuint32(
                2, 1, 0, 0, 0,
                1, 1, 1, 0, 0,
                1, 0, 0, 2
            ),
            iPhi_3 = cms.vuint32(
                0, 0, 0, 0, 0,
                1, 0, 0, 5, 0,
                0, 0, 0, 1
            ),
            iPhi_4 = cms.vuint32(
                0, 1, 0, 0, 0,
                1, 0, 0, 31, 1,
                8, 7, 2, 8
            ),
            iPhi_5 = cms.vuint32(
                1, 0, 1, 0, 0,
                1, 0, 1, 2, 4,
                0, 0, 0, 0
            ),
            iPhi_6 = cms.vuint32(
                0, 0, 0, 0, 4,
                0, 0, 1, 0, 0,
                0, 0, 0, 6
            ),
            iPhi_7 = cms.vuint32(
                0, 3, 1, 2, 1,
                5, 1, 0, 0, 0,
                0, 0, 1, 1
            ),
            iPhi_8 = cms.vuint32(
                0, 0, 3, 2, 0,
                2, 3, 3, 8, 10,
                1, 2, 0, 27
            ),
            iPhi_9 = cms.vuint32(
                6, 0, 0, 2, 0,
                0, 2, 0, 0, 0,
                1, 0, 0, 1
            )
        ),
        cms.PSet(
            iPhi_1 = cms.vuint32(
                3, 5, 6, 2, 1,
                0, 9, 0, 1, 1,
                2, 1, 1, 5
            ),
            iPhi_10 = cms.vuint32(
                10, 0, 2, 0, 3,
                0, 1, 2, 12, 0,
                20, 4, 0, 7
            ),
            iPhi_11 = cms.vuint32(
                16, 2, 4, 1, 0,
                2, 3, 15, 4, 1,
                0, 6, 5, 5
            ),
            iPhi_12 = cms.vuint32(
                3, 0, 1, 0, 1,
                1, 4, 2, 9, 115,
                38, 2, 3, 1
            ),
            iPhi_13 = cms.vuint32(
                10, 3, 10, 15, 2,
                0, 8, 8, 0, 2,
                2, 0, 1, 8
            ),
            iPhi_14 = cms.vuint32(
                4, 0, 0, 0, 1,
                4, 0, 1, 1, 1,
                1, 1, 0, 2
            ),
            iPhi_15 = cms.vuint32(
                11, 1, 1, 2, 1,
                3, 5, 4, 4, 2,
                0, 1, 0, 13
            ),
            iPhi_16 = cms.vuint32(
                6, 1, 1, 1, 0,
                1, 3, 2, 1, 10,
                3, 0, 0, 15
            ),
            iPhi_17 = cms.vuint32(
                4, 0, 0, 1, 2,
                1, 1, 2, 0, 1,
                0, 1, 0, 3
            ),
            iPhi_18 = cms.vuint32(
                5, 0, 0, 0, 4,
                1, 0, 2, 5, 31,
                0, 1, 1, 5
            ),
            iPhi_2 = cms.vuint32(
                4, 2, 1, 0, 5,
                0, 0, 2, 4, 11,
                10, 1, 1, 12
            ),
            iPhi_3 = cms.vuint32(
                5, 0, 0, 2, 1,
                2, 1, 1, 19, 20,
                237, 0, 2, 2
            ),
            iPhi_4 = cms.vuint32(
                5, 1, 0, 3, 2,
                1, 2, 3, 3, 1,
                2, 1, 1, 7
            ),
            iPhi_5 = cms.vuint32(
                1, 1, 1, 2, 0,
                0, 0, 3, 5, 2,
                1, 1, 3, 14
            ),
            iPhi_6 = cms.vuint32(
                4, 0, 2, 2, 0,
                0, 0, 2, 1, 3,
                3, 1, 0, 3
            ),
            iPhi_7 = cms.vuint32(
                1, 4, 62, 6, 0,
                1, 10, 2, 2, 5,
                1, 1, 0, 7
            ),
            iPhi_8 = cms.vuint32(
                13, 1, 0, 2, 1,
                5, 1, 3, 1, 0,
                1, 0, 4, 2
            ),
            iPhi_9 = cms.vuint32(
                4, 1, 2, 1, 6,
                2, 6, 0, 2, 2,
                1, 0, 0, 6
            )
        ),
        cms.PSet(
            iPhi_1 = cms.vuint32(
                4, 2, 2, 0, 0,
                0, 4, 6, 1, 0,
                0, 2, 2, 7
            ),
            iPhi_10 = cms.vuint32(
                27, 2, 0, 0, 0,
                2, 3, 1, 3, 0,
                0, 2, 0, 0
            ),
            iPhi_11 = cms.vuint32(
                8, 2, 3, 5, 5,
                1, 1, 0, 4, 2,
                2, 0, 0, 5
            ),
            iPhi_12 = cms.vuint32(
                6, 6, 1, 0, 0,
                2, 0, 3, 1, 3,
                2, 1, 0, 2
            ),
            iPhi_13 = cms.vuint32(
                0, 2, 2, 1, 0,
                0, 7, 6, 0, 0,
                0, 0, 1, 352
            ),
            iPhi_14 = cms.vuint32(
                8, 0, 0, 1, 1,
                1, 2, 2, 1, 4,
                0, 0, 0, 2
            ),
            iPhi_15 = cms.vuint32(
                3, 0, 0, 0, 1,
                3, 3, 3, 0, 1,
                0, 0, 0, 2
            ),
            iPhi_16 = cms.vuint32(
                3, 166, 0, 4, 0,
                2, 3, 1, 1, 1,
                0, 0, 0, 6
            ),
            iPhi_17 = cms.vuint32(
                2, 2, 1, 0, 0,
                0, 0, 2, 5, 0,
                0, 0, 0, 2
            ),
            iPhi_18 = cms.vuint32(
                6, 3, 0, 2, 0,
                4, 7, 1, 4, 4,
                0, 0, 1, 2
            ),
            iPhi_2 = cms.vuint32(
                2, 2, 0, 1, 1,
                1, 0, 0, 1, 2,
                2, 1, 0, 0
            ),
            iPhi_3 = cms.vuint32(
                0, 0, 0, 1, 52,
                0, 3, 2, 7, 2,
                0, 0, 1, 4
            ),
            iPhi_4 = cms.vuint32(
                4, 0, 0, 0, 51,
                6, 53, 4, 1, 0,
                0, 0, 0, 0
            ),
            iPhi_5 = cms.vuint32(
                10, 0, 0, 0, 1,
                1, 4, 1, 0, 0,
                0, 0, 0, 8
            ),
            iPhi_6 = cms.vuint32(
                2, 0, 2, 0, 1,
                5, 1, 3, 4, 0,
                1, 0, 1, 14
            ),
            iPhi_7 = cms.vuint32(
                1, 0, 1, 1, 0,
                0, 8, 9, 2, 3,
                0, 1, 0, 3
            ),
            iPhi_8 = cms.vuint32(
                4, 0, 23, 62, 31,
                0, 5, 3, 3, 1,
                0, 0, 0, 4
            ),
            iPhi_9 = cms.vuint32(
                100, 3, 10, 5, 0,
                2, 0, 2, 1, 2,
                0, 0, 0, 0
            )
        )
    ),
    useTestPatterns = cms.bool(False),
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
        ProtobufFileName = cms.string('model_graph.displ.16.pb'),
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
    EtSumZdcInputTag = cms.InputTag("etSumZdcProducer"),
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
    codedVetoThresholds = cms.PSet(
        ieta1 = cms.int32(0),
        ieta10 = cms.int32(0),
        ieta11 = cms.int32(0),
        ieta12 = cms.int32(0),
        ieta13 = cms.int32(0),
        ieta14 = cms.int32(0),
        ieta15 = cms.int32(0),
        ieta16 = cms.int32(0),
        ieta17 = cms.int32(0),
        ieta18 = cms.int32(0),
        ieta19 = cms.int32(0),
        ieta2 = cms.int32(0),
        ieta20 = cms.int32(0),
        ieta21 = cms.int32(0),
        ieta22 = cms.int32(0),
        ieta23 = cms.int32(0),
        ieta24 = cms.int32(0),
        ieta25 = cms.int32(0),
        ieta26 = cms.int32(0),
        ieta27 = cms.int32(0),
        ieta28 = cms.int32(0),
        ieta3 = cms.int32(0),
        ieta4 = cms.int32(0),
        ieta5 = cms.int32(0),
        ieta6 = cms.int32(0),
        ieta7 = cms.int32(0),
        ieta8 = cms.int32(0),
        ieta9 = cms.int32(0)
    ),
    inputLabel = cms.VInputTag("unpackHcal", "unpackHcal"),
    inputUpgradeLabel = cms.VInputTag("unpackHcal", "unpackHcal"),
    latency = cms.int32(1),
    numberOfFilterPresamplesHBQIE11 = cms.int32(0),
    numberOfFilterPresamplesHEQIE11 = cms.int32(0),
    numberOfPresamples = cms.int32(2),
    numberOfPresamplesHF = cms.int32(1),
    numberOfSamples = cms.int32(4),
    numberOfSamplesHF = cms.int32(2),
    overrideDBvetoThresholdsHB = cms.bool(False),
    overrideDBvetoThresholdsHE = cms.bool(False),
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
    extrapolFactorsFilename = cms.FileInPath('L1Trigger/L1TMuon/data/omtf_config/ExtrapolationFactors_simple.xml'),
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


process.hltBoolFalse = cms.EDFilter("HLTBool",
    result = cms.bool(False)
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
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm4',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp4',
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
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
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
        'JetMET/vertices',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_pt',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_eta',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_phi',
        'Muons/MuonRecoAnalyzer/Res_TkGlb_qOverlap',
        'Muons/diMuonHistograms/GlbGlbMuon_LM',
        'Muons/diMuonHistograms/GlbGlbMuon_HM',
        'Muons/Isolation/global/relPFIso_R03',
        'Muons/globalMuons/GeneralProperties/NumberOfMeanRecHitsPerTrack_glb',
        'Muons/standAloneMuonsUpdatedAtVtx/HitProperties/NumberOfValidRecHitsPerTrack_sta',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_pt',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_eta'
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


process.ProcessAcceleratorAlpaka = ProcessAcceleratorAlpaka()


process.ProcessAcceleratorCUDA = ProcessAcceleratorCUDA()


process.ProcessAcceleratorROCm = ProcessAcceleratorROCm()


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
    PixelShapeFile = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
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
    PluginName = cms.string(''),
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
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    opticsLabel = cms.string(''),
    useNewLHCInfo = cms.bool(True)
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


process.ecalElectronicsMappingHostESProducer = cms.ESProducer("EcalElectronicsMappingHostESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.ecalMultifitConditionsHostESProducer = cms.ESProducer("EcalMultifitConditionsHostESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.ecalMultifitParametersHostESProducer = cms.ESProducer("EcalMultifitParametersHostESProducer@alpaka",
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
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
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
    pTChargeCutThreshold = cms.double(15.0)
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
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
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
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
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
    PixelShapeFile = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
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


process.hltESPPFClusterParams = cms.ESProducer("PFClusterParamsESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string(''),
    initialClusteringStep = cms.PSet(
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('HCAL_BARREL1'),
                gatheringThreshold = cms.vdouble(0.1, 0.2, 0.3, 0.3)
            ),
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThreshold = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                )
            )
        )
    ),
    pfClusterBuilder = cms.PSet(
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(5),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('HCAL_BARREL1'),
                recHitEnergyNorm = cms.vdouble(0.1, 0.2, 0.3, 0.3)
            ),
            cms.PSet(
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
        )
    ),
    seedFinder = cms.PSet(
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('HCAL_BARREL1'),
                seedingThreshold = cms.vdouble(0.125, 0.25, 0.35, 0.35),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                seedingThreshold = cms.vdouble(
                    0.1375, 0.275, 0.275, 0.275, 0.275,
                    0.275, 0.275
                ),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    )
)


process.hltESPPFRecHitHCALParams = cms.ESProducer("PFRecHitHCALParamsESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string(''),
    energyThresholdsHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
    energyThresholdsHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    )
)


process.hltESPPFRecHitHCALTopology = cms.ESProducer("PFRecHitHCALTopologyESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string(''),
    usePFThresholdsFromDB = cms.bool(True)
)


process.hltESPPixelCPEFastHIon = cms.ESProducer("PixelCPEFastESProducerHIonPhase1",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEFastHIon'),
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


process.hltESPPixelCPEFastParamsPhase1 = cms.ESProducer("PixelCPEFastParamsESProducerAlpakaPhase1@alpaka",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEFastParams'),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
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
    PixelShapeFile = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
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


process.hltESPSiPixelCablingSoA = cms.ESProducer("SiPixelCablingSoAESProducer@alpaka",
    CablingMapLabel = cms.string(''),
    UseQualityInfo = cms.bool(False),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.hltESPSiPixelGainCalibrationForHLTSoA = cms.ESProducer("SiPixelGainCalibrationForHLTSoAESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
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
    PixelShapeFile = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
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


process.hltESPTrackSelectionTfCKF = cms.ESProducer("TfGraphDefProducer",
    ComponentName = cms.string('hltESPTrackSelectionTfCKF'),
    FileName = cms.FileInPath('RecoTracker/FinalTrackSelectors/data/TrackTfClassifier/CKF_Run3_12_5_0_pre5.pb'),
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
    PluginName = cms.string(''),
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
    siPixelQualityFromDbLabel = cms.string('')
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
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('140X_mcRun3_2024_realistic_v14'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('L1TUtmTriggerMenuRcd'),
        snapshotTime = cms.string('9999-12-31 23:59:59.000'),
        tag = cms.string('L1Menu_Collisions2024_v1_2_0_xml')
    ))
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


process.ecalMultifitParametersSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMultifitParametersRcd')
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


process.hltESSJobConfigurationGPURecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JobConfigurationGPURecord')
)


process.hltESSPFRecHitHCALParamsRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('PFRecHitHCALParamsRecord')
)


process.hltESSPFRecHitHCALTopologyRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('PFRecHitHCALTopologyRecord')
)


process.hltESSTfGraphRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('TfGraphRecord')
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


process.SimL1TCalorimeterTask = cms.Task(process.simCaloStage2Digis, process.simCaloStage2Layer1Digis, process.simCaloStage2Layer1Summary)


process.SimL1TGlobalTask = cms.Task(process.simGtStage2Digis)


process.SimL1TMuonCommonTask = cms.Task(process.simCscTriggerPrimitiveDigis, process.simDtTriggerPrimitiveDigis)


process.SimL1TechnicalTriggersTask = cms.Task(process.simGtExtFakeStage2Digis)


process.simMuonGEMPadTask = cms.Task(process.simMuonGEMPadDigiClusters, process.simMuonGEMPadDigis)


process.SimL1TMuonTask = cms.Task(process.SimL1TMuonCommonTask, process.simBmtfDigis, process.simCscTriggerPrimitiveDigisRun3, process.simEmtfDigis, process.simEmtfShowers, process.simGmtCaloSumDigis, process.simGmtShowerDigis, process.simGmtStage2Digis, process.simKBmtfDigis, process.simKBmtfStubs, process.simMuonGEMPadTask, process.simOmtfDigis, process.simTwinMuxDigis)


process.SimL1EmulatorCoreTask = cms.Task(process.SimL1TCalorimeterTask, process.SimL1TGlobalTask, process.SimL1TMuonTask, process.SimL1TechnicalTriggersTask)


process.SimL1EmulatorTask = cms.Task(process.SimL1EmulatorCoreTask, process.packCaloStage2, process.packGmtStage2, process.packGtStage2, process.rawDataCollector, process.simHcalTriggerPrimitiveDigis, process.unpackCSC, process.unpackDT, process.unpackEcal, process.unpackGEM, process.unpackHcal, process.unpackRPC)


process.SimL1Emulator = cms.Sequence(process.SimL1EmulatorTask)


process.HLTriggerFirstPath = cms.Path(process.SimL1Emulator+process.hltGetRaw+process.hltPSetMap+process.hltBoolFalse)


process.HLTriggerFinalPath = cms.Path(process.SimL1Emulator+process.hltGtStage2Digis+process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW+process.hltBoolFalse)


process.EgHLTExtraPath = cms.Path(process.hltEgammaHLTExtra)


process.MinimalOutput = cms.FinalPath(process.hltOutputMinimal)


process.schedule = cms.Schedule(*[ process.HLTriggerFirstPath, process.HLTriggerFinalPath, process.MinimalOutput, process.EgHLTExtraPath ])

