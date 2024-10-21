# L1T INFO:  L1REPACK:FullMC will unpack Calorimetry and Muon L1T inputs, re-emulate L1T (Stage-2), and pack uGT, uGMT, and Calo Stage-2 output.
import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.AlpakaCore.ProcessAcceleratorAlpaka import ProcessAcceleratorAlpaka
from HeterogeneousCore.CUDACore.ProcessAcceleratorCUDA import ProcessAcceleratorCUDA
from HeterogeneousCore.ROCmCore.ProcessAcceleratorROCm import ProcessAcceleratorROCm

process = cms.Process("HLTX")

process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring( (
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9a61c53d-c650-4443-9123-e7653ddde73c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ce3044bf-85a5-476b-897c-ceaa58d3021e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/85f99452-69bc-4b0b-9fc0-11ff9113b0b5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0711fc26-26c2-4d7d-9603-d88dc5ad3970.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fde68a80-b01a-4f4a-9162-c8be76bfed21.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6e74d323-32b2-425d-92fe-6378b8d3b416.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c76a11e9-af09-45eb-9406-88a3109a2071.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/60adcd1c-684b-46ec-b2ee-75c65f3ce280.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/388aa81a-aa7a-455d-93aa-6bc0f13f7b54.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/34ef06eb-410d-4345-9eeb-b44c3ed409f1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/50eb405b-d952-434d-b6be-fd2e116f8c99.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a9d516ac-6e12-411b-822a-36b1c74a6904.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d04aeb81-e0f4-4373-98a6-079aa4112c47.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9578d7f3-0e52-4413-a7ec-8de8e5f6abf7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/60c7c076-af78-4d2c-9edf-cd1c15587f7c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/06ff12b5-b415-4259-88c8-a7e662ab7117.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/fdf4682a-4fb7-42b3-98bf-70f97c63ed71.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4a9c17a3-b903-48fc-82d6-bc675f7ee3a8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/f30a1fde-24df-4280-99e3-182340c68fcf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/561d6887-9e93-4425-812d-cf12d9218645.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cffb68d8-73dc-43bd-b04e-8b07ecbd1313.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6dac91c2-f0c2-41fe-81fd-3f4f2d1c84b5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d1b5f8d0-2d11-44ec-af12-24bedc860290.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2422cf7f-044e-4f80-bd80-50f56d8dfdf8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/61fb0007-688d-431b-a906-fe683ef68632.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/00d2837f-b109-4d2b-ae46-a41439c3b860.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/0e3c8abb-22fa-45e4-bded-d2ed4e053836.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e3140abc-66c8-45c0-9f6a-26516c857dc9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/262cb892-2053-4bce-9695-184d6d538bf5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/10ec727b-76e5-4896-9b2e-efc820e71186.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/696184bc-1a87-4a8f-b954-a54de73448f7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/842625e0-9f56-461f-9e20-88ed5c09e899.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c97c819a-dfca-4891-a9f6-1e8994c19982.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/772b3e7b-4a42-4d95-bbbe-48ccd6ba1697.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/819ef1a7-122c-4ade-9b14-4113967d2f7e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a75941a1-a5b2-4524-9372-246d46fdff95.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fcd27e2c-f5e2-4d48-918a-e2d6b243d721.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d04a0363-bf6a-4cca-87f4-5affab6103a7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0c1ce4ca-35fa-4953-9c28-6255a313dc79.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f05c10dc-b779-4098-b5c3-941c7e9b037d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/922c6ce7-8961-42ec-8493-d3cf322ba3f9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/13a9b28f-8846-4bf0-844d-43c99d01ca7e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4c3ae67e-a270-428c-90d7-f5d64084f3de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a68a4c75-2155-4ff8-aa99-b2293c90b440.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e6766601-1e76-417c-b2a5-993adeda0f00.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d11d9a60-1805-43f5-a36d-b5bbb8f0b450.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/59d81303-16c8-4451-856a-b79f96aef0e2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/61de95c5-1234-4f73-a046-3685cbb1b1c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/078642ee-69c2-4863-866c-a0e6b446938f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bb7ba981-5395-4d4c-a769-43bde75ea751.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/02e2aca9-085b-4609-834c-289fc37c4f84.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3ab298cc-db9d-4e33-935f-e6905e2e7d71.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/97cb44cb-3701-4cce-b382-a2f066562e8e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e18c8126-0049-4bf5-b4ee-75badf04beec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2efca954-6c4b-4306-b6d9-26c38b9874ce.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/140e3774-d59c-4de7-8ca2-5d6beec4fc64.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/35f5bc8b-c258-4b9e-98c5-6126f6eaa325.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/427ff720-9f7e-43ed-ad5d-24054715023d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/63c1d5a8-48e7-4472-8b66-cd58b373c2cd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/75bd68c5-f3b9-4bfc-8978-4024d134611f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/0f04c521-cb49-4f83-87e4-29520b53ce02.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d3ff4dbe-64cb-4ec0-aca9-e8905590f8e8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/646c65ec-c581-41be-9719-39ba2f12d9f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6fb5425c-b901-43e8-9d62-e42e80cc0074.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/29324991-bd19-4c7c-a594-6795fb949b15.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6390b7b6-5fb2-4217-be4a-8110cccf1822.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8bbd8522-07b5-4208-8ae2-2cee5edbd32a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bd1a1439-dd3f-4c4e-a3db-0a55595452b7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/27a073c1-5b17-44c1-bdc7-08c1f45a51f4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/36878828-1e67-49f4-8e7c-8af0f9c4f294.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/87804932-91a2-4159-a0ee-a231489d2b5b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3c9dc250-6da8-4ca7-888c-a2632242fc36.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a36c969a-a95e-45c5-b14f-921da9165b89.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8e232f8c-f6fb-489c-9f56-aec296714af6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/28dd7015-4dc5-4807-916e-39b9b20563e4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/3aae26b6-1b2b-446e-8923-3164093d3e5a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/46499c4c-868d-4e53-917a-86f448ddcba2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/88fd9e4a-5945-4eee-87e3-685572cbcb11.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/548df3b9-7126-4b73-b05b-df89fdea5742.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c3f09cb9-554d-47cd-a61b-a6345dbb79fd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/676d1b7a-2d0b-4ad6-82cf-22d75fc7193f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/8bebf594-1b52-4286-b831-05b050ed9174.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6678b9e8-17d8-43d8-b75a-e5b237cd9569.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d87c6ab4-ea9b-4dda-bb3c-db02d93ca43c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c18f1b80-5282-4c8e-bc35-90413e6327b1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0054ddb2-596c-4a03-9749-90c64fc6bfb3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4d0cc8cd-fa17-43fe-89a6-a959f0bb4956.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/eea74cf9-8fa4-46b4-92b0-5b2848b45e11.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/440d2d6b-c125-499e-965c-9c1a7cc43522.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/41c47b7a-3f52-4186-9469-568e0c41ace6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8f9af5a9-c320-42c8-97bc-50c14f59a4c8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5c1b5c02-e789-4cb9-acae-bc3dc2a6c901.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4934d597-5808-45d5-9eb2-34bf520b5234.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7e318bb7-68c5-43a0-9e5a-0560d6c8b0e8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/211f6601-c803-4dce-af76-766b8b9bd6f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e00748ba-80b2-4e55-b691-c10ee1ec22ac.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3fb0870f-7362-4f9b-ab0a-951546c84742.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4d43c4b2-a978-410c-b81a-183f10e8eb4e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b9573830-39f6-42a9-a4c3-fcbf13fb51b2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e5df0aae-d8e5-4bd3-898b-312638447fc5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/50545b77-e7f8-488f-a668-ba0fa592a5e5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/56c0fb47-1f5f-4863-a7ea-080c834154f2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b0b6eb31-d12f-4c20-9ef2-4b82b49c3d57.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b5111730-f0f3-4af7-9325-03e5da5b0555.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/e64ef6a5-bde9-4d91-81ee-5f6949eb4e36.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3b454f7d-0da5-45ce-aff3-58f2b1781eb0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f834e2b0-569c-44cf-b6a3-50a107daea7a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/03372be8-e2f0-46f8-a034-a4d53b5e9984.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/081f427b-5029-4216-af6d-83d8e0b4950d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/9d8fe4e5-835c-4fd2-8327-a7a22ccef796.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ebb01072-6d00-451f-a7f8-9df169f6ed09.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/589f6c62-4d1a-484a-8780-12b6ba50726d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cc5133b6-2f15-4af2-a20a-86d3aa5e88ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5522785f-7618-49c2-9cce-0db4435528ca.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f0dca969-5b59-4886-b4b5-49d8c5f85023.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9c1aecd1-78c0-4373-8aaf-e14b50c328ea.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6c389681-c799-43ba-b5e4-fb4d2ce3cfc3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/089ea6cf-4e0f-4527-8f13-496ec34f6c69.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/6c9eaa4e-1458-4fe2-bdc8-ec8d6f6011a9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/57d7b908-3d3b-487f-8378-a9f04e1fe37f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cdc30b34-a4e3-42b1-bc29-86dc102278b4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/65478fab-70df-4839-874a-aa2cf0428bf2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/546244f0-748b-48c5-8396-1ce748644edd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/71da730b-d7ab-40ca-a6b4-a87d446b533c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d1726345-7bef-4797-868e-37aa98f36797.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/c6ca1a2d-a50c-4128-aa86-f0f62de9cedf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3a2650cd-4102-4659-b506-2d09aa3c85ee.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8f5899c9-f945-4529-9bf2-27e3096f777c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c3da575e-723f-49f9-83ea-a705bb30c42f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/db5245da-b006-4e8f-96c5-9b4440b61644.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/311867ac-c7f4-40eb-9996-6c922fcf60db.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/55c8ae3a-7c92-40ab-ac0e-518049197953.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/516e9555-8032-43dd-a85a-b3d5e6d048ae.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2d77a1e5-c4d7-43d7-9fb9-2451e2d64d93.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9be7a954-b97f-4469-83a3-8b9ac9fa5c2f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b02008b0-69a4-433e-90e3-406744800dd9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/04b28da4-e701-4444-ba9f-c44cca3c0aad.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bf488908-96f2-4af9-8d9f-1e72b8679b0c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/466d3f90-bb49-4923-8d40-7f8090a9483b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fc33d3b4-5c3a-422e-a0dc-db7cb26acd5f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0e7dde4b-7cec-4551-b204-a89bc2083591.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3353faaf-d0f7-48ed-b092-c155399cbf82.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/280829e4-4530-4a48-b4f5-56646aa38e3c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d5f23899-1aa4-4dce-ac1f-b086f888115b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/331e10c3-298e-4f13-86c5-85e666277eb8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6e71cdfa-2a2b-418f-a44a-95a724cd8147.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f3a7a76d-a49b-4c33-885a-819979ac182d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0e3206b2-de37-4eb4-9025-8d9b6bde0dbf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d8c1f1b5-84ba-4975-8317-1fe0bdb86011.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/81059597-b1a4-4551-9f60-82bc353a9060.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9fc6fd2f-7b1c-4087-876d-d5b384217999.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/24764e0c-2074-409e-b376-67ce76bbf7c3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2bb5b354-c14e-4885-8aaa-7f4208b2df2d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ca821e92-9f2c-486a-ade5-ad9f99d342bf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b46921f5-9595-465b-b1ca-a791e4abda2b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0113a938-a3be-447a-bc15-532c278bbfdc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/21a6a3cc-6eb9-4762-a9cf-77ed024ae404.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ae0c6ab9-94fa-484f-bf14-c0821d51eeb2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b83d8e70-48a1-4fab-9b4f-cf4f8d65a1af.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cdbaf5c9-8438-4202-93ff-b539385cb855.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/dd642f12-07a0-4a9c-970c-59ccc7e65689.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5c1dd3d3-e18b-4942-96e0-ddee73b1e6b9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8a81b132-531c-43bb-a7e3-0982cb419433.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c8512990-e499-4cbf-97d4-acc4c8369ecd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/45a29a72-8b9a-4a93-a0bc-754f4c670b85.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/767c33a7-ae9f-4997-a23c-5d765ec8c391.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/1c6418c5-a043-438f-abd9-12ff5899fdb0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1850ddb9-9ed6-4c72-8ba9-47a23845971a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/600af47e-18f2-4258-b986-34eab55ec93a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3447b76b-b54d-4e89-99e5-a5b940bfde5b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/dae50010-d85d-4901-91c0-0396af6911a7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/968c34f1-cd8c-46c2-be17-3406f8b4599f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/7acf1aa0-be8d-4b86-8b36-b367319e6251.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ab0d646a-9f98-4ee0-b426-6abaf902ad05.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c3fcb6b6-2c78-420d-9e40-a2e64143af3c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/31e2f404-ad85-44c7-936a-e345dc9ce9a0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f8f7d209-3be2-4f5f-b4e6-0c3f2a4aa466.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/93fce48d-a03b-452a-9417-064fffceef4d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d8db1bfd-9a68-4543-9cb4-27571dfc68be.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8ea96a02-53de-4cc0-b4b0-999f50bd8167.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/308a6745-2033-480e-b09c-02a6863887db.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/01255f1b-5fe6-489c-8fc5-217d9b0c8e66.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e3338a04-a32f-4b0d-b2c6-7b15e885ed38.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7a851b4e-484b-4de4-b530-b32fbd00ef84.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/50a97c87-b76e-413a-b4d4-a269b32c0c77.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2b99467d-e680-4fd7-b943-83b5fd0617e0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/94aaefcc-ebc0-48a2-a663-a83f7b552947.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/db7bc270-00e3-40d9-a221-683e718abf38.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2418345f-1d33-49ef-93c0-45472a8893b3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/609c8c8f-431d-446f-b676-d5d406aef4c0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/8b54c5f7-cd4e-401b-9631-3ff9b840c818.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/947a1f73-b3ab-4621-9a54-dcaa4b0100fd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e1faf500-ee48-481e-a5ab-f065dd822f34.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b60a5eb6-08ef-438b-898a-0cba7024adb2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0dd5d8cf-c38d-4055-bc04-7ecef7e25ffc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e7f15593-9b57-41e7-afa4-b20ea13ddf51.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/04386c7e-ac40-464d-900f-d74358019440.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/a3d019d0-872d-4b8b-8031-455b7bd014c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/eeef6a45-61d8-408f-8ebf-ef1251108271.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f2715c07-4df4-445a-aa33-5dd2b5207989.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/97dca5b5-60e0-4dd8-bc2c-3234bd87f1ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1b68dae7-f42d-41b0-9def-a2aaa3bcf1c2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/7c6937f4-7cc4-4702-82bc-777d7f9a0c64.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5e19c3f0-7765-4eda-b0b4-1cc7dc0a7d70.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c3b859b3-6740-4936-8ae2-8e5aa74f2556.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/67abc113-adde-49bd-86e9-a6a1cee3285f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/673387ff-2b68-4629-b87d-b6de0b712cd6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/287acbab-d5c8-46b0-a2bb-140a439d59a0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0dad28d5-3145-4c9b-8780-7c4d24622562.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e9fb54ee-6103-4908-b699-7b27f0ed5f15.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/45f3d656-e6f6-49c2-958f-0a8ae7847660.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cfef4f89-0ffa-40ec-a5b8-fd56685c74fa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/6b110340-71b6-4be7-8df2-8a47c6ca964b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/388caebc-13a3-470b-875b-ce9267e196b6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/049c928d-7bff-461e-b09f-ea2551ad460a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/82c4acab-68b5-4b3b-abc5-0839d4fa6248.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d2f5a772-c6ad-407b-bf8f-6d2b883aa8c7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/f2fa7393-d968-42fd-877f-d243c1dba277.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/f6ab5d01-daa3-46f1-9d6b-3cddf8c5e3a6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5668a55c-1b69-4bf2-9bd6-125dc1e75233.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/acd84bdd-2a95-40cc-ae4e-9193702e1018.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/15e2ce7a-05d1-47d6-ae4c-79800d54ef75.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/43c8623a-80c0-4185-a42c-48e79269c18a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/80cfd3fd-55db-4820-8bc4-c888042c23ca.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f5fe3d2b-a76f-4d93-81c7-08e0c026bfe5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/6c09dfb6-a352-4f9c-b85b-05ef346aee83.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7afc9c73-9d7c-4ed7-a0da-81e0d1d41d71.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/72cd3c0d-ac32-41cc-af47-d560e714f8aa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bfc026a5-e8d7-4687-854f-1114f56ed308.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ce4e2208-9b61-44c3-8f92-745d7d1d53d3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/de396dbd-4afa-4fcb-a9ed-18cc7289e759.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f078d1fd-8cd4-4ee2-914a-57966dbca5ff.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/1dd49189-d2ee-4594-a932-ae19b7606a7d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1f5ee8f7-cfbd-4cbb-809a-957d863b7f29.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ab6b5018-29ef-4009-881c-d0eb8d4cbe3a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/640f3ff2-a8d9-47c5-8065-8edd9e3c466f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/802d8201-e035-498c-b63e-744a4cb3d1f9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8dc1c444-5148-4ae9-86d4-9da984da7964.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/649f60a6-5aba-4965-92e0-3c71a2f8b8f3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f43bcb1d-d7e6-4bf2-bfe9-5fd1a7dc55b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/38ff4350-9d79-49cf-b0d9-2aa173f22043.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3e14099e-e120-4a36-aa0e-773c25fceb68.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bf92996f-7713-4c82-9ebd-9fb859df4727.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d925874f-3f41-453d-8a85-7270c245aa7d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6a1e9ec6-6f03-4c1e-8b04-a98c6ee89a7d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/39ba746a-9b07-4bd3-bfe6-a1fb9a0be3b9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bbd58ad2-406a-429d-ba39-5f0a93c4cb83.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/de74d5c0-3833-4a47-9b04-98b8dc50e7d3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/82b29a01-2f7a-4feb-ab0e-5b483d9878d8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7a3a3fdd-446d-476b-a205-15923d7a569e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0d6b7dfb-5e89-4bd3-8cc9-03f85112ad21.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/92358f78-cc4c-4e57-87be-603e43df0ffa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a62694b8-6367-492b-9f70-2d1d2941abb0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/4625fed9-06a9-4d84-bdd5-813df65c1bb4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7553f780-a83a-4b62-811d-db12fedea19a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e672c6a4-a165-461f-886d-23c93bd23504.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/16a38305-b8cf-48db-a063-fff460298ce6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/deca6055-dd79-472b-b5b5-0afe169e71ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/04041787-5563-461c-8fa8-d6b348cc1456.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/3b2ce4d9-2a0d-49cd-83d8-38bb4f45d839.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/104b7875-9ba5-4588-9bfc-4e6b33a2957a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/70ba23bc-537b-43c8-9e0d-60207d758a63.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a68ace28-3dbb-4ccf-b3d5-e2df45ccad57.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/df77e55e-63a3-4fd9-84b7-b954244a3c5c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/05a6a3c2-337e-463d-aec7-52ee8c7d3bdd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4033d421-20bc-48d3-a2d4-b11a80aa30e4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/89d68546-74c3-43c1-b42e-01fe3fcb69ab.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/36ce3133-8690-47c5-b368-89e59bf40daa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/52cba838-1b72-4ce6-a837-a22791e55b25.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/80fb9f49-cb73-4fbf-a13b-eb900e218b38.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d6c67119-fcc6-4da7-9c8a-319b700daf73.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e6a0045b-088f-467d-bee0-8e39e21364b9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/f2c4b7bb-2bb3-4773-9803-b1ea2c9587af.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ecec9dc5-c41c-412b-ada3-497fba8d6212.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/505be14a-0e67-48d2-8ca3-dcc9a70ca312.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/f7ac61ca-5b1b-44da-b395-39e69b5621f4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/30f4b9ad-bee0-49be-8edb-bd4a4b974822.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/48113739-ed95-4fe4-97c4-49b8b4aa6a0c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8134f1d8-ee12-43f7-b617-ae7b450c781c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d1b5f1c4-9d4f-4cea-a179-a41653b519ca.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5e0386ff-8b8d-4518-80e0-2857e1858ad2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1f38e57a-9c88-4344-8d7c-b47b7614c9dd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0756d810-6951-458b-b0d7-810b85a6a867.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2dcf63c5-99cb-411d-8112-5c96c64dd1f8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c2718806-8d5f-4b59-a4e0-be9f2534c142.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/08dc8735-41aa-4505-83f8-ec0f34057628.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/07413f14-dd9d-459b-b8b7-ce8f224406c7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/63408500-8588-4d6d-9120-c17c4140ab10.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b24d4fc0-cdd8-465e-b6c8-9cd4193b0809.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8fa07e94-4a5e-479c-ae3f-bd2c6cee8967.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/caf1aea0-9212-4e19-ad6b-97f633a4e92f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/aa57bc70-d6bb-4d63-8a40-cdfc230a0085.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b2778e0e-f850-4f03-b70b-4c3eb4b7b392.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d7a5061c-89d7-490b-9fd1-63752ee6c7ba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/827ce367-c4be-442a-a714-5e11ddfe7f03.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/0f3593f8-4237-4627-98dd-5a432993e51f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d870b5ec-b9fb-41c9-ae0b-30bc87bff891.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/b5b1e864-754f-487c-9611-ae68c3d285fc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/02353dbb-6620-432f-82b2-e9d9cd084db1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f2f363f3-e24b-4143-89fa-e5dae89f80fb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ef7e7615-c43d-4cfe-90e9-e8b4373dfe50.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b4fd7f0f-0e18-40ef-8e0b-5bccde1eefaa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ed5b57c9-6e91-42aa-89a4-9c261a940e86.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/1871abc5-21d9-47f6-84b3-036f33e76e3f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0d3d3a46-ceb5-492a-894f-32d6f60c579b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/749bdd7c-dc02-4a6f-97df-e5eab0a8e9b1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/52fd1e3f-e1de-42b9-af74-d9d8b53e91e4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/9b85fce4-8711-4f0d-bab4-11df7207596f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3decde60-d910-4f37-b177-d1b6deeb3185.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7d0f5d95-2683-4385-b5cd-4cece17c746b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a075acbd-8500-4514-a9d8-80e406952978.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b037ccc7-bdb7-400a-a20c-710970fe9fba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e5ce6e76-426a-4838-bd75-3995e5500fa7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/86b19f3f-4bb2-4bfa-8fbf-25f816c5ed77.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a90d3976-b1b3-453c-98b5-ebf9aed34a5e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4177b8ca-f79e-4f0e-8498-1683a7210537.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/90ece2b6-8fda-4ed5-afd7-cbc5fb52b14f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b6c16b92-c7cc-4984-b5b6-d53b7c4bcd87.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5519fd95-0e42-4408-92d7-8c3317a07394.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d1c7037f-bad7-426d-97ad-ebcd75a4def6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0edd923d-9a2e-4d01-8c5a-11b600d939ff.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2d3d4b4d-a6b9-43ba-ac99-83470e4c82cd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8ae5b213-6b35-4f8f-b1dc-59aa90e45957.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/dd5648f9-c611-42fd-af78-0691e3dae936.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fbacc5c8-8d02-4559-86ad-c34b0bb76493.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/279c529e-e5ce-4d50-8cdd-77c0def99bb5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7209f930-59ff-445a-873a-563ec44bb6fb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/056f915e-531f-4f24-9593-6bf46cbb371f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7dd6ce96-f74e-4366-bcef-8cd6d948e5aa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/f6939012-88ca-458e-8375-4d5069b727dd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7fdbd055-5adf-44ca-97ae-e961247b6486.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/0428356d-a9d5-4ad4-a949-76ad8c92eeec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/05d2f26d-c68c-4fdd-9da8-58484d54d2d6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3a6075f5-e0d5-4c88-953c-ed5f67d66784.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d79ec327-f130-4fd3-bd1e-144a4f88d394.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/bfc00462-9f60-4404-851b-ef74006466df.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/afc5b519-720e-4b51-8385-57849e3087dd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3bffcd8d-9526-4820-abe3-fba119da1e6a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ce0db65b-0eb1-46a0-8bf4-413271bda607.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e5b503f2-166d-4ddb-b557-a9f6a7c70c74.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0ef36eb7-6e6e-44fc-91f1-4fe0e8e64ebb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bf856837-9017-41b1-9f39-658efe01b126.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3f5c8416-3c34-49d6-a24b-44cfe30df2bb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/735ea29a-4b5a-4081-b7fe-c89cafb289d1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/79c56d41-de19-4fe3-8f0b-c20892aabb48.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b26ea3bd-4b24-43a4-a81a-6faf214cb6f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d74c0935-80b2-4ec9-846e-7b123d6f4753.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7a33ea73-4722-448c-bd47-0d980c380b83.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7ec1f6b1-2e12-4606-8781-beb8fbdce838.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4aaea189-296e-43b6-b791-86c5433bac0a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d19a80af-b76a-4f58-9389-1d232c2fa7fd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/ff5f56bb-51db-458b-a281-0d82854db44a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6bed714d-91ce-4811-bf01-001c41f8f522.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/18d5c74d-17c1-47eb-8e3a-5e0af093bfa4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ff01a602-a54d-4646-a220-c2cb7b88b5af.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/68f06de8-6c0d-455c-8f87-8303c3f41b20.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/79ea9c96-2ec2-4026-bc31-847ee7764b3f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d016ac3d-494c-4528-a1c4-69e27fbff85f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/f150d072-33af-4141-8f6f-5d4026c361bb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/49dab273-238f-4207-b7a1-6cfa91d1fd88.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3de598cc-a7a8-430b-b251-7e17205a7995.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8c2879c8-92f4-44fd-b0c1-82507ab6df30.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7c9e5af2-e9c4-40e5-bb90-59bd66ff6394.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c1075744-d33a-496e-9f1f-35e6b42dfa51.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2dc666e2-3e89-438e-963d-332455cc4e59.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/b660e749-82f8-4fee-b304-bd1343d8b6bb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/01af87e9-5d3d-44db-977a-8f864676a026.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1157a307-e0c3-49ad-a7f7-5a8d017fa8de.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/14af3446-d8ea-47d4-8d65-deeed373700d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/99bc34aa-3761-484d-876f-9fd9e70ae293.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ba5d2f2b-72be-4637-972b-2b0f5c3fdbd4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2dbc3f59-1c81-411b-b8c1-7bfe7c008ed1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/74b6891d-f7e4-47be-8db5-6eaa33dbc216.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/344af710-e784-4063-9b0d-6460745376b9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8cca636f-1266-473a-9518-d7ab86abf5f1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ef80ebe2-6442-46a3-ae91-e771954fb8e6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d5c737fe-be3b-48a1-b0f2-7dedec239aec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/626f20df-8383-4c27-9b3f-9d9a135a686f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3e305f09-7fb4-4d19-9e7a-1ea276ca81a9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/aeaef12f-74b5-4eac-ab0c-9e43f028db0a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3f6b7b3d-1765-473c-9f17-7f6e9296830b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b03811fb-2379-4616-a85c-7afa8fb12876.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c9e0d418-8784-4e5f-a2f3-f66b9ce63e5f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/9617bda1-dd67-4bbc-997b-5b6dcb723e56.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/61b324de-ef24-4fd2-bfdb-85541ca19817.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5c6cef96-e890-4112-88db-ac0fa1caf3e6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c2616693-0d9b-4155-a6fe-7b469d27ff3f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/52fd5227-9aac-4034-884a-a04cd7adc34a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b5da9d4a-90f0-4028-b2d3-a9a2d59627c5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/eec3ff99-764b-4429-85b2-411dcdf80b48.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ae15d676-8a83-4732-bc21-efd4893f2988.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a1c18f93-77b8-45a6-939b-06d72fa744c4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/49b58281-be01-4f52-8de7-a2b100dc8ae7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/665f8b80-d862-43a7-b125-7072d8b9962f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f28864ad-83fd-42c7-96ac-60ead8de23fc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/74b4c0bc-36ec-4ac9-9bec-fed8a9acd658.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/78ac358c-0d85-4dbd-b8da-02b365f0126b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/409a432e-6b8f-47ff-9528-137309341225.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9ec3b001-2dce-4a86-bb60-c73e653039c1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1d6668c1-9c38-4a3d-a741-c88de98a99e0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cf1b5a90-c44d-4cd2-915e-835cce46cfe4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d1c164cc-25a8-4419-bbf6-04d5f745d7e3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c1fc8e9d-aebb-4783-9a30-53b682706670.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8f2fe37f-f151-4dc6-ad6a-6a4a818ebe4b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d12e9d9d-bf0e-487e-9453-3eaee6a28da6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9ede3abd-4b3b-4e76-ab62-49c72844d300.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8073b576-2949-4e73-86c7-cd6b98567175.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bea63025-e5b5-4770-9c72-89dade33dbd4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d75d9c40-2a94-461f-9987-4e110e4f85e9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/db86ecad-8bde-46db-aac0-f721bea8d1e9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/619cc405-ad49-4696-9e13-a0ce725dd92b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1c0539f8-06fd-4d29-a781-da818630f049.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/16f9fa4b-eb9a-4818-b642-5cc8bd2437cf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f5aadb31-b10e-402f-9d84-627b0e79d798.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/57b1b4e2-64df-4d63-af32-f6f6bb32eee3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c05a9ecc-e7b4-4830-b662-38f87737f335.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/0bdf316c-2fca-4b68-a0ab-1f98652a9d8a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e604e28c-94ed-4571-8dc5-3bddbaad9f88.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5ce4a2f0-d5c0-4d0e-8a36-59594e02c754.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b6b775ca-75a4-4274-bb7e-41500fafef69.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6659e4f7-eb30-4276-81b8-918d87621a70.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3698fd27-23ed-45d9-b9db-a03c9ecdf7d9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a2f0f884-fbe0-4f35-9b3b-93c9d58fe77b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1cf77378-df90-4cce-871a-aec74f93a68d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/73caeef0-6da9-496c-8909-8f43761f3fcb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c4dcb56a-3a47-40e2-94fd-4157a6214e56.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/16b11fe2-c8b4-4042-ab6a-33b63c07cb81.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/4169b90c-fd74-4dd6-acdb-fdc534638903.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c671c9b0-c183-445b-bc7d-f0fe9ecc9e59.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0442bfe1-30f5-4bf9-a148-adb720dfc98a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5e3273d8-9329-429f-a42f-1cbc4cbb853e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/23286be9-bd6b-4182-a5a8-039f60e3c241.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2833d19d-4be7-4c11-ae4c-715a60ec0d1f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9e147252-2083-41b8-a2c4-16722dff1c6e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/952a06a5-ab51-422d-8262-1d8552f4f055.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4ec63611-a468-4947-b002-57eaaa692ee6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/72f34bf1-4644-4587-85f9-0e1d675f262d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/69b7f52e-5d7b-4ec9-8d45-5ec111bfcbc1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e6bdf536-9cec-4176-a6cc-3da286bfd004.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7751e116-25ca-42a1-be2e-9c37f23ad608.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/18c9206f-9009-477f-afd2-49341d1869f7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/dfe3e268-393f-4028-921b-10fef5e927c2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9783315e-3238-49f9-80ff-2c12a95512c8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c5e215de-54a9-42ff-a20a-39f63bbb348d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3c98370b-3dc3-40a8-acf5-ce67f3636997.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2a2b7b03-8b95-43c6-9941-d37bb82ae0a1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d76cbbbc-baa3-47ce-81e8-e02b2fb50ff4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/02cdc3bf-49f8-4aa4-bd0f-6b84c297d138.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/8773c79e-5517-4b6f-9b1d-ce8fb7767956.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3d57802a-be42-4614-a4b2-30545eb4645e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/74392b59-28b1-433e-b355-2cfaf937d1ae.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2f87eb48-8121-4ba7-a262-1ab3ffaabbf4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8b342f24-fe3e-4a8d-9587-42a4da127d3b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9241956a-bec8-4c06-858e-0e3bdb1e0a2b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d487fd88-9d0b-4cea-add1-2ace9b495996.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e1bef7bd-ac42-4d0f-9f7a-a25e6babc29a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/c0517275-c667-4ce8-9702-a5f15ffa5591.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3f104939-748c-406d-9511-c19e605a0f09.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8c8b1cd3-1b6f-4966-b7bc-782f5127797d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/17215bb5-f73d-4106-a3f2-6c6799b2a163.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fb44a697-7b74-4b6a-a5d0-f0f5e58f3c0b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7309a304-e911-4921-9ec9-0bf8331176c7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/264c723b-e776-4a73-b640-41a80b4393d4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6e378ddf-4884-46ab-897c-749c7b3f86b3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e68c52fe-6123-4407-89b9-397aad45a1be.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0adc2d01-7a9d-4489-a586-f5a465321273.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5289eb8b-d096-4b60-93a5-1d48721ee886.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ac094280-bad7-40cd-9d54-c3d199afd510.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5057b0d0-561a-4b5b-852f-6e3cd4a09edc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/aa21e852-ff06-4b26-8de3-35344c7faf76.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/198e733f-79a1-4ec8-8591-556bfd776f67.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4d9e5723-ec6f-4f03-b5d5-74497439819b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/93389b26-adb8-4638-8b65-d03c494dd130.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/87f042e9-44ac-49d0-bcef-dca2fd6c721e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1a1e2b9f-4286-44e4-b9c1-37a3ea3b3831.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/39bc632a-c335-4dd5-bb7e-11403994f5e9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b877c19d-4376-4012-ab5c-c8b8ffeea067.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/dc083fdf-d553-4d9f-9174-aad047f39def.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/0e3677fd-7e8f-4579-8994-66d6c8f35490.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/470f3925-3587-421c-970d-c313bf230d1e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b50d6a75-f603-4bea-8120-0b9e8f31dbba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3a8228cd-7226-4180-a6aa-324927a8775f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/da6f70b4-9e77-41ab-b79a-c8ad33bac19b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bb560495-3820-47c2-a48e-477b10831a32.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/82ee17b5-feaf-4ba7-8ec8-b0973823e00d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/83afd1e8-63f4-4a7a-86dd-45b8a1323714.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f595a953-3a55-498e-a6c3-30e1e1cc86fe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8f1fc757-cdc8-4e52-9ea0-67f3ce40c8f2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f6c86534-695d-4bae-b8e6-cd6998ec038b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/2cfddf17-725d-433b-bf3c-7a68efd7b447.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/46653236-94bd-465f-bd05-a763cb1c0ebc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/864e7a58-0d9e-4a5a-941f-56a8b156075e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7cc3daf4-ad2b-4d56-8552-99f033760239.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/308fa07a-19b2-42eb-bd1b-5fe54585b3e9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6a1ded8f-68b3-4659-87d6-95980b59c55c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/122cffbc-e83a-4b7e-9225-c1bce0708326.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/716e4a57-0883-479b-9b48-ef51528cb778.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a93d1bd4-b42a-447d-a67c-a733abcddd03.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fbe8da54-466d-4943-ad81-b7e0d0a7c1c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/568ad09d-71ed-4d76-a221-c648d885dc5c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9860cd65-f61e-4035-88b1-3935240a8615.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/7ebf5d3f-9c4c-481e-b8ef-c6e672f6be75.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/55149562-3cbf-45eb-99bf-2903212dfdd8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0b0089fa-8361-43e0-86d0-67f6b3de301a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1911169b-6793-4621-ac79-e9056c57be7e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4da06b45-809d-4a57-83bc-f82aaac0180f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6ce4e1f3-b52e-47d4-b52a-380bf66d685d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/59a0845b-3bdc-4bcd-a632-a81785fae9e0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/99903b1a-b3c8-46e9-9e6c-16eccfbe8260.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/2133738a-8bb0-4271-874d-6241ac1d13b7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e4472d9d-ecc5-4b86-bfe2-28f2d7bbdca7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0352c1c0-2d3f-4fc3-94c1-8f58ea44a478.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c771a7a9-afba-4e30-adf0-1b5512c7d195.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ba73c981-00ad-4e02-9f30-989c0dd77ef3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d603eb04-0599-4072-b613-9458b4374c6a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9a0fe820-1047-46e6-8417-630f8b93ba37.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3ce34c26-c926-4c58-bd27-0462c964098f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/28ff107d-4370-4de7-b275-89aff7a949b9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c0570213-128c-4a0e-a860-f839a24a43c2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5e6c4331-853d-455a-9f5b-dfbdb76834ec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bcfeb991-c59e-457a-acbc-d2f9ec182041.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d1cdac25-872c-4e49-b9f7-bb1b047ccf01.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6e54292f-6785-4c1e-912b-288a046aba8b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/69fcda5c-6a84-45c6-a428-380e57fcb862.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9e00a4a9-39fb-423c-b03a-1436067fa3e4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/b282c887-9cb0-4433-b00b-ebe9affe5ff8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f800f00a-f7f3-4ba9-9667-0dc1e3039852.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6c76f781-e7ae-4590-96c3-5803fa8d7f80.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/fe1144de-710d-4b4b-9029-7aaaee32707b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4dbcd046-39fa-4d18-a31e-b4716ae72a1e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d7a9c0c0-2638-4a09-ba7f-60d6203bb9b2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ff3f3098-dcd8-48f1-b2fb-7fa2d2e9c7fd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/da3b8a54-ea0e-424a-b870-807deab9ed05.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/614151e5-010d-42eb-bc4a-0672166c3416.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5029761d-2c83-4731-ba08-de055d31cf39.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f5a37acb-361d-4402-8258-8fb386ccec1b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ce6fd8b5-51cb-453e-9230-484453ddef6b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/83a8afa1-9b3d-47d8-9d21-20152398fb44.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d6ca4cbc-c0f9-48d1-baa6-efa022ad994d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e376c80f-842d-4f6c-b01f-715d03ac925d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/59f9ad36-6872-4c47-b72b-0c655b97eda9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/54ff57b8-9035-4044-ac49-f0a75a0b4690.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/38f800da-48d1-4c97-84f7-69f1ca3358b9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/56a4c6cf-652f-43c8-811c-075ad8780fec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ce43412a-3f06-4970-b8e4-232490c87f3a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/dd3fb818-d3ef-423b-823e-b542f574a6e7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/77c5093e-a677-4366-93cd-5abcc78dd388.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/05f4e223-cdde-47c3-bc81-9d0cf1c5b9a6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/aac7945b-5e1b-4ac8-8085-ed1de55643e8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/62589285-5d41-4ba7-801f-f98f952a6e83.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7de607b0-f753-4cce-a4a2-ba031f19ccb1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/dcf36de3-225d-4754-86c3-d9c594717186.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1e1ece42-4b7c-44ff-9ff6-b691ade3bcd8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/cf32d729-5841-49f3-bd5c-dc8ae9165943.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/21c52723-5b67-4479-a04d-05dba41c0311.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/7ceae699-eeed-4519-be22-83c05bfeda99.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7f0e88c8-7cea-4914-ac7d-fd1865c789a1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/83108d97-53bc-4395-9ff4-946bf8bfef88.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4767718f-6286-49f0-b431-84963820ff33.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cc14662d-eb00-4125-9747-565299b1345f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/75799235-ad52-4b21-a76b-233fcf2d317f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/54030201-6d0a-498c-9b1b-2b9ecb2179a0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4e3c7fc2-6485-4c50-a425-aec83d20a398.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bbf88d27-8a3d-408d-9a75-a4fa10bb3bbf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5ac719e4-e728-47c7-af80-979dc4803c9a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a7b50173-60f9-414e-86ec-128ccbf5ac62.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/732faa24-4ec5-4aca-ae77-8704bb9bd68d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5046cd64-f1c7-4d66-9090-b9863ab030bd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1834931e-234b-49b2-8f7e-bc3de51232f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ffeac484-a4ce-460d-8b90-4e351c9fbcee.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8a5d2f72-cb57-4bcd-a690-c37aa9f310ea.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fcac7ec4-759f-4366-b063-49c7a40104c6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/950a96f4-1c6f-4778-88e6-d61b2d4c7b3c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/063f577c-8bd2-4b6b-9717-21408fb64920.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b081c394-0869-42fd-b45a-82f829fccb18.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/b72f1898-655e-4962-b4e5-26b6b5997f88.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/51110d2d-def1-4775-8797-22f3df04f427.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/402405a5-8096-4e03-9ec5-6fd1e4db910f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3dc2f078-79a6-4535-a158-45c351b53e77.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5e279335-2f4a-4c09-aa86-9955cd066395.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2096f0ec-1e9b-4cce-8ecd-1dc8b6e348b4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f65067ec-9a13-4118-ae40-afbe4f56b7fa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bfc51ee5-c982-418f-ab43-86103ad23780.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/eb8482d4-609b-440b-856e-aeea8608d79a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6892ab7e-502a-4f79-b991-5a0bbfac5537.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d5925757-97ad-4a20-b4ff-090f5a66e96c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/eee9d17a-e351-4f31-bdcd-af62bbb34e8d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4872adb7-6f30-447f-a47c-5361f45f96ca.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/581d9287-6612-4642-bce2-1afce82229fd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7f68544a-35f2-42de-adfa-37bbb6604f3d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/896ffbd4-0f09-4a47-b20a-27350473b3ab.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c5e3ad5e-6bf2-44e3-a3c6-a24347bda2f2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/df53101f-fe2a-46f7-a66b-7713c384be55.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/586e7739-b0c1-438a-9bdc-54493367df66.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6c158f2d-8dc9-49ee-86ba-342b1599eb02.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/db61c15b-5006-417f-b2e5-07180bcbc0bf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bdea22ad-eca8-4703-88a2-ae5a48504d03.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/02e750af-3dd8-43ed-8a45-89b3f08176d0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/8ac2ff20-cf49-4bf8-9e4c-d4da9f0ad22f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0a0ad3db-a878-4bd7-a984-6b3eea131a0f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/179455f0-705d-4346-b713-a5c9dd486458.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9aa00141-22cf-4437-b1bc-8b580ce10dbd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a586a6cd-2697-43aa-9b83-a2a347118725.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4786aabb-7279-4467-a9d1-010a3780ed64.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3b11bfe3-d191-4fad-91de-3ecadc2dfc76.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/64e96390-4d69-405d-afb1-03fe52ce7db7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a3a00226-8d05-4fc8-bcd1-262874e62a2e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ca4ba964-4cc3-47d5-9e3b-1d3116d910a7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c7008711-96dd-4a47-b913-8f8f93d791a3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f6c57afa-b694-4cfa-87a1-568d629922a2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1b23f2b5-47f5-4be7-862e-10560906bf7c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/34d1b19b-260a-4065-8adb-463aba4fda24.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/60182240-cab7-47cd-b604-bd5014721d11.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3acb00d4-6969-4a11-9318-c24dde03cf56.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0e8b71a7-c897-43f7-b462-d1feffd7e006.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a663460e-8bb3-45ff-85f9-423d777daf4a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/adbc76ac-4bb0-422b-8558-482fe3182ac3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a363f11d-36ce-4b61-9fa6-ea42f3c1df84.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8cccac42-be9d-4f32-9a71-648324f82c82.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2d5f9d74-990f-4e90-acb8-4e2c048d1e9a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4c4ba4a4-752b-4c1d-9aae-080f2b32954c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/00698c23-84fd-4243-8e4c-8f40561ba6c6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/3f8e9f9d-4b5f-4042-b199-e488713c2053.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/11235318-56b4-445d-bf6d-6b73fccd5a64.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/123fc68e-837b-4930-b43a-5520b082d79a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3614158a-9daa-4986-8073-dd93f41f4f0b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/24dee3bc-393d-4ac5-8588-09001b51a8d2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c53ae52d-5525-417a-80c4-92102f2f51d1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6b5d7e42-dbf6-4672-8b04-54f45538219e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f3748706-82a5-483c-bcc3-a28b190bb30d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fbbcd983-b193-4b60-b042-aeab4e7ea7e9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/cce3fe12-4bfb-491d-9e70-b8fb733ebd24.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d4596314-36dd-455c-b0b2-912b9a5af5e6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1b6b7f92-a9c4-48fd-8186-8ff93431cccb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/93974e57-2e17-433f-aeb5-de6b32de09c3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/237491ec-a1a7-4ce1-aa75-5dab1edd8bfc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5b7e9971-4da5-41fc-b83b-ce6a2ac10839.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/669a38f7-ac98-4aef-bdf9-d7c66e37c0e8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/132cefcd-32b0-4f37-b6b4-3b25c2b5dc55.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e2c6e1d1-9439-4e67-8ee9-67f1d21b62ce.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/55fa6568-540f-405d-ab00-3ce888ca3eaf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f7927d53-20ba-4084-b10b-be4cac5bcb6a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fd1a23cd-288a-4d1b-93dc-24c013a6d6ba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cbfe0869-d156-48e3-907b-dc7a5b5cdc0e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/3c298a70-a1af-40fa-9dbe-50df98ffeed0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/68b24c38-6f6e-4750-8b7f-63ed780123c3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/870961ca-cf0b-41ff-8591-391b93b83c64.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c2201047-6579-4152-9bea-88dd0109630f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/80d31320-9c2d-4401-a5d1-0aa5e47788aa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/87cf9140-b0b8-478f-b712-1fcba05bdac4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/257cc6f5-c195-43ba-8582-77d2651f0435.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a6cde891-6c8a-4101-a95f-5280d9bb8320.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/408e6975-90eb-4b86-8e75-98fff4e5f71d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/388917fd-4cb7-42be-b971-a72a11c19dc7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d70d08f6-33bf-419d-ad0f-a52f7e1fe90c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d1b8dca1-055a-4377-9c53-b56adde337ae.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f9b8f601-ecb3-46d6-86e6-3829386a538b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/40924f10-45fb-4941-8ea3-0748a52c1a7f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/85562622-ff4c-4c85-a728-dc59eee9ec4b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/73ac3eef-b923-4af7-94ca-66acd6a4f91c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/df2f3c2d-331d-43ac-ae6e-5f6a962bdeea.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a8362ce0-1ee9-4b8d-a2e9-90fc65103095.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/93648045-a2a9-48fb-8a3d-b03693e904d9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/86eea7c1-1b98-4914-95e7-fac707c0cc88.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/44d2b121-17ab-4d2c-aac0-0b7368a6a07e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/046e36f2-f567-4caa-b2cd-6115da07cbeb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1f1ffd23-3f31-414f-929f-2151a55c6af9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/119b8e3b-8e59-46b0-b5f0-a138bac5af2d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8de59ab9-c35b-4eed-950f-23ff4d576deb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f49b1ea3-c0b3-4b3b-9a0c-fd8d3dbf3b48.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fec92e40-3f02-4b43-8734-a04c4dc01276.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/7e92229f-caa2-4bb3-8ea0-eabe36a38425.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/23f10b30-91ca-4792-8c5c-2857b9117367.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fcf0cf7d-d39a-4aea-a793-0521afefa9f6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d5e08d01-3b8e-44fa-9a9f-39b156508099.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e1dcea42-699f-4f0a-b205-c9f229e176f2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/042ef7e7-9e70-4cb2-846f-52b6ee450d33.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/09323c7a-2c6e-49c1-a307-ad9c87e0a408.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/99b55407-a0a1-4f70-962d-1bb9d4667b2e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f2f2df1e-615f-42b5-a42e-c946be26804c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9c065f41-dd87-490c-87d6-0456c9886a2b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/38c893d4-8a5b-448b-a46b-3bb542f4f55c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/7e37c6f7-2985-4e46-9091-5b6b86a6da25.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1fc964a4-4bf2-474a-953e-26110aedae30.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3e9526e0-955a-444b-ba0d-10e337f02d7c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/4c49d7dd-f172-4c07-95db-d0266821dd46.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/949af868-68a1-48ea-a06e-04e4db5c1859.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2f3e330a-352a-49b7-8dff-8772c183e2c2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c98601c6-d126-4df7-b25f-6859f45cfc53.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e226ab6c-f04c-48c2-b2e5-fdb30acb372a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/764489b2-af69-47a2-a716-88d9a6b1f880.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/764ac288-9899-4f0f-99b9-bd751207c987.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f4dcda56-e230-41b2-9851-42b654eb738a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/513893fd-2a93-49b0-ac6f-13ebd2afd5df.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/33300def-a01c-41ab-b365-91e864e142b9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/f13a7f7b-5054-49ad-be29-cb395f3655e7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/07c1a073-d93e-4449-955c-1806efdbc5e5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/58109d22-9f0e-4496-bd0e-3db41bc8c958.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6ed87560-cecb-467e-9fdb-e4f6cf3a9d25.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8aa6fbc6-5c6f-43f4-865f-9edde428690d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3f49418d-dda4-432e-9f71-b139f52cf3b1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3916847a-0a14-4b07-a9ce-555d52688ad3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8ad4ba9e-d8de-461d-95e9-ee6dea729fbc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d12021d6-6175-46dc-8dc2-e543401081a6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/14ecd343-6f44-4d46-bdc8-e2951be41eba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/712b5496-7e30-465b-af3d-49df8b9a9406.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2095ebf9-5b7e-4cdb-9a23-ecf9c18f3d63.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3e7f82b2-72d8-4657-a539-74c0ded009f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/812d54c6-57cd-43b8-a49b-afc1130811cd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4cb83ac4-92b0-4b33-8996-2b167d5e996f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8e569521-1e2f-41a1-996c-86867c8f4ffb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a33e673f-c714-47e4-b8c5-c1c764208a8c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d30aa6b0-57b0-4d39-afee-225ba24d8da7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/afc3ae63-1248-4863-a7fa-bd460f66b478.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d335550b-f2f7-4db9-88dc-f5e2c7c3d265.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/39b7802a-f60b-4c67-9af2-4e3104c10fb8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cae7b49d-a81b-4cbb-ba0c-f0c308a95693.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/627882f0-c02e-4f1b-8fec-6b5c619eb42c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4d1c292f-2a3f-4d30-966b-0b27cfad6dd4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/17ba7555-78b3-436f-9b12-ff218ff31dd0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/213946c5-b46d-4411-97fb-0797abe85f86.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/df68020c-8614-42f1-ac50-f244c3a863f6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/19fb47a8-786e-437f-9bd9-c0e0b64bd94c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3e93bbb4-89fa-4e78-b808-25f651616c0d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d03dbb26-cd10-4001-b7c5-5bd86c436f81.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/2f641df5-18ad-4b42-9978-03f2e6df1063.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d5bf12e0-de72-4028-89af-cfc33c308c4d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9d9b34a7-8358-4411-beaf-f9086a0a42c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e6e776eb-eeb9-4966-9293-e82fb2195caa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/e432d2ce-80af-469d-a3dd-1d68f8f2ef99.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/fc34ecc5-b651-4b89-aff9-e270de03e173.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/601f692d-3745-4592-ab67-639d8dc5893a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f5279d07-18ff-4ee3-8cca-d78abb502051.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/60d5fc6e-3785-4271-b581-32d2d770bd7b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/333ed82b-4ad4-42a8-8ac8-6b88e1fe4bfe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2a45484a-d581-4fe1-8e6c-11ca44a140b5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c7a5e9f2-4ea2-4c4f-ba82-9adeb82093a1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/410a63c8-1e17-40da-a2e7-f908409a1931.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b0100837-1b1d-4565-b464-6595eb8ccf38.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/58ea41fb-93c2-4b12-a2bc-9bffd7e2a1d4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3afacf07-de33-4003-bf47-94c057afec4f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c8708d56-2d15-4dd1-8ad3-627bd303965f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c9cf02be-a208-4891-989a-a9a7569fe851.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/eb0fbe67-4726-4ae9-930e-b72eb27d514f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/141e42d2-396b-400f-bc6e-fd41f78c292b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1b81cdfb-24df-4fc7-9aa0-10491e3232d1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6cdf2ca3-98b3-43b4-87be-cdf3a98a30c7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/573548b4-535e-4961-9832-2df3aaf1a13a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1c774260-2df2-4f39-864f-7d12bc7f8b29.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1a0a49b2-6e37-4e2d-8dc4-5efe7e80f075.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/468c3877-3e3c-4dff-95a8-4051ea077539.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c8a6c50e-ded0-4ca0-97bb-ea48627ae346.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/a620c844-4530-4a0f-a89d-ed091390da35.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fd84f240-8eb4-4e6c-b5e8-9ecd09ce24f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/49a1bd8a-4e24-4ac3-935e-aa00d4d4bb2c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1a95bb75-ebed-49b3-a5f2-c33bffa45f2b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bcdd3f0f-cdf7-469f-8538-2469255785d0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/295d20e0-26a8-45ce-a426-87e2c197071b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4e6da9f0-0c0d-4705-923a-b1baf355de49.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/378f8c64-2e09-4a0e-a7c6-a12336d35e72.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f43326d2-b90d-4a62-a68e-a01c9fd2b3bc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fe346237-1560-444b-83e5-e6a92ce49a55.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/713b1a33-91e4-4e2a-ac09-baf2ac4305ff.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/93a40f78-5f6a-48e6-aa5e-b21936a48c71.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ca42acca-25d3-4737-bb51-cbb0b8cec377.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7cd506c7-87aa-44af-9351-cf6367e54000.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/004e8f82-50c9-4559-9d23-b137a2545af4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/306cc24d-764d-4598-85a5-f0e581df41d7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1ba9ec6b-5138-4f24-a17f-d9609a44d773.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1ab14482-dc99-478d-a5b9-18d087d1deb2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/55b379e8-5525-40d6-8a0e-504e2be502ea.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b0b23a57-6fa6-458c-a9ea-8651ceb3abee.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/c3200f2f-3994-4e3d-86e1-ec99510ad3e8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/98ef798c-789d-4c6d-a275-a126702dbd38.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ef7245e2-1365-4cb9-95cf-fe8678b2956c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f8ca3cf8-27c0-427a-873a-a5537b7b3878.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/8dc7c866-7d7f-41ed-9877-56a05d6a068a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e471844c-3643-43a1-af42-e444a0bd4225.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/aa678127-8cd5-4b6d-ac69-71a2863a1fb3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/29eb8d49-db77-4f6a-8845-0bb242131297.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5f86dcc1-674e-46b0-8f35-a3434cad46cd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/471df5aa-628c-4eba-a185-9d0ec301a6c4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1fa8e034-4973-4ded-842d-d8324ec56b00.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/08083466-afc6-4f24-b7ea-2f3868a0895a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c5e39865-1ac2-4542-b0fb-664a3bbf99ef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/5d4c0358-3065-4391-a442-3799c35e2f7a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/56bea749-73b6-413c-af4d-669ce1116bc5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/77aaca28-4a70-48c4-b6b2-6134fb5be90d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/ba819c03-a1b5-45f9-b1d4-0573c1eebbf3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b42af622-e8ea-4b97-9695-ec75616ec6c0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c84e3081-3495-43d2-8ca1-7fd4931af696.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/47ac1a60-0e63-4fda-912e-a69a775922eb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7abd2632-ffd0-4cbd-9d3a-253436ed6734.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0ee16cf8-2764-47a7-9e1d-fe44646c302e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cc08afda-7fa6-4589-a3a8-fa4a37dd36bf.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5c70ef51-f0be-42b3-8496-d077d301e902.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fa29c680-41d1-45d8-8a27-d658f335641f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/88951591-a792-4dc3-8bec-d1e77105d053.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a64d488f-db30-45ea-b84c-3c62d9035dc7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/80224d0d-8c75-4987-9485-1f083d4e087c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a525052b-e677-4ea2-a86c-666d7f7c876f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e1bcd063-9025-49dd-9f34-ea215ef1bcb4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/6dbd97ef-2c1c-4051-9309-9b775b7a3810.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f5979e83-c1df-46df-bf11-5132ec3dec1e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/297912db-c73e-4dc3-a108-ee86841488c3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/017b7ab7-03e4-4d23-a204-2495bd676af1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/476de150-82f8-4c8f-a276-e87905434302.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/11f960da-0d9a-4c6c-ac6b-c383403d017c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/11a9965e-4adc-4a92-adb5-5aa338e4dcf4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/1295a1e5-6632-4c4f-9d33-33b071d0ca50.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/e6166fdb-1ebe-4f40-82d2-c24a996aa55c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/847eaecf-a4b9-4ed5-9d84-fc2e21c90587.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9851a03e-de7e-4492-a299-0040731de0d5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f66efb3d-e18d-4732-9495-ed3437466a88.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5ec81681-cfa4-4c90-9f7b-646f89d08c49.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/69d9cc0d-bc9f-4405-ac4f-dbec645ed015.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/edeec13a-2673-4830-be4e-dea46ffdd6b8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/be7d4623-73e4-4ed1-b4e0-895e79403599.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/61d0cbe3-9f93-4006-bcf7-b885c1428dba.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fc7ee922-fbb3-4938-b694-7e8794bfdabb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e410067e-d589-433d-a4f5-b4fbe0d86931.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3e0dda6d-ea59-4bd0-b240-d587468daaef.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8e2e3d3c-716c-4b59-a695-cea415746922.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a01b6f00-e46d-4d78-8328-5d3bbed8029a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7ef0309d-4dfa-48e9-951e-c326e0ba810f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/52e3e917-a976-46a5-bae7-2bde61bd847f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/88f86983-aa30-4603-b448-332e75bd4259.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9cc3c3d0-0b6c-44de-9c19-eb063e6ac781.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/4f7fed1b-758b-401b-aeba-73924cd35e7d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c1c3c626-9687-43b7-ad36-913260d74615.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/c0ef40d3-6d20-48f1-adf2-239bfbf10c02.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/26e2dc3a-0622-4e98-8030-411953d2bbbb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a8bcd50f-4636-4c12-a940-8a083fd5fcf1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2f8588d8-4de8-476b-8638-b28ac07de48c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a4200604-82c7-4245-aea3-ea88797a7742.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f71875c3-02db-4bab-aa68-a2799fa34615.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9e022af0-e9e0-43d2-bed2-ade94340894d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d38f85d2-2f87-48a7-a0f8-d19ecaa6b41e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/89106cc9-3af0-4eed-905b-b64ab9e25316.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bbb97a77-eab2-46a9-86b5-56bac5e60e83.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d31f62fb-8bff-4a01-9642-6273118747f3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e492c456-f945-4849-a839-c6b66842d9c6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f0d67f3c-6708-433a-894c-d6fbd9b4ccde.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1bfaf325-24b7-42de-87d8-e03ea1c1465d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/145cf165-9c93-4b3b-9990-5af2134ae5ad.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/81af74d4-fb66-49d4-8997-e6acba661816.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/076ade36-4a9a-4706-b1f4-ee495161c73b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1da7fdd8-0f75-4071-afa4-5a840e3abcc2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d19584a5-1aed-42b6-85e9-c2010c37664d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/79bcf4b0-88df-4769-9509-a0433f74b261.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5b503754-767c-4665-822d-8037a81350c4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/197be01f-6145-4288-a191-5eae05aa181b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b76290da-ad05-4acc-91e6-3b13674858b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/b7b5f161-888f-4395-82d4-a11fa9ddecad.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5b5e2ec4-5e70-492d-bc50-3873fc69afae.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bfa5690d-2512-49ee-9eb0-e891418fdb22.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f94a10a9-cd84-4879-bbe9-4d4ba52c980e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/546abd68-3bc5-4b5b-ba7a-bd434beb23c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/277a940f-8fd5-4980-93ea-31563479d114.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e6d3d59e-e738-49d0-b123-5b94eb03d9fc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3a803b1d-b54c-4a3f-a74d-3930bd3302f5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/43ae9d2f-5ee5-4e57-90e2-dd5cf1d06e13.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7115bc83-e3a3-4f7e-8d5d-a34f330f4d4b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0b567ff9-794d-4d96-b1a9-bf99268b897c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8e68035f-4697-4e21-ab2a-ea0761581743.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/50bd10d8-57b9-44f2-81b5-04be7c0afa02.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/17abd852-747e-45be-a962-e1415224c0c1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9d99b296-f8a1-4d30-9e6d-914881b7909e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2e555d43-494d-4e4f-b536-9871efc86d2b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4f311478-e02e-4c9a-8f29-c9a87529dcc3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/824acb24-c183-4e5a-ba75-53f779add476.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/883319e1-8cd5-475c-8496-a4fb8bfd42db.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c256d12e-523b-402f-8587-875be636dd17.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/da339077-e53b-48f7-9d42-4f13eb1e58c8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/eed9f739-d54f-4656-b44e-11fda5940043.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5a213d28-3be9-43a8-a0e3-8519f5ad94ca.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8ff8cc24-fa38-418c-a668-32c92cd74cdc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5aee336b-89b6-4698-baa5-86bc75a0c843.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a2f22287-0131-42c4-ac74-efa8180dec37.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e403fe1d-c528-4826-8776-c0bbcf538771.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fb8ce6b6-1087-46b6-abbb-63e37641b916.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/53305b91-769c-40cb-9d5d-cde90dad1b1b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8c6f29d8-cd2b-4e96-a6d4-437e3199d8d9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8851047c-7888-432f-ab04-08ccad5dae65.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fddd384d-0771-44b3-8f9f-661e405e1a64.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2d526b8e-95cc-4d19-bdf6-a91e39b23359.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d1349f7e-1c67-44af-8d31-931a8970dba6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2751ab5a-20e6-4981-8cca-5e33fc22171f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/209758bc-a602-46ed-8d06-ce4288951643.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/80912dbf-af01-483c-845f-c69fc64762d1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1913080d-8bbd-4a0f-9b19-605adecf4c82.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f20525dc-2836-4e10-aea7-dcbf4d894e24.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/711392bb-da62-4cf4-8575-0f0d01f2599f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a4ab3519-da94-46d2-bbc6-b6f8d9754312.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9af6c19d-5b6b-4385-b9fc-971aa8dabcf7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/ad197a6b-f0e4-4894-ae35-a547b9fa4e2a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/348a02d6-ddf4-41f8-8238-bd16d88d6349.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/911e21d5-a267-47aa-a1cb-ba56de035a8a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8d829cba-ec2e-4464-80a2-5f1d7ae50117.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c9e4316e-c9cb-40f4-b12d-dd3636bc5ff8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/f1ce146c-e419-4ee3-a76c-2478b837797a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3c9cafa2-cd55-439e-9ee8-bec2370c5da1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/785c24cf-1adb-4180-87af-7f1e4b56e9e6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b6c2bcef-de40-454f-845d-46cdcc8b1220.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/8ffcbe36-211a-403a-a7e5-dfc025f24f48.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/767b0d11-525e-451e-8b6d-b4526e77404c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4f3c2f45-3106-4813-ac03-2648c6a57a46.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2775575c-3ccc-4171-a06d-cd5d8fbad054.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/02c0f25e-682c-4ce4-8965-d32ac9f81805.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4bf8426e-b2ef-4465-8e0f-6efe4ac88305.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b2e53e71-7e41-40bc-8fb0-1994caf7427c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e05ea815-14ff-45ee-9499-1cb41d1fb108.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e6a150e9-060b-4e59-a6ea-f0daeb190d02.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/044b6587-7ac0-4166-bba6-64d2c6193066.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7338c342-0a00-4ee6-9693-51d5e1a1843d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/382172c0-e15b-4ca1-87ca-f5ac6cff9e9a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/4038c5f5-cc13-4b98-a832-f703f61c4497.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/af3c2b06-353b-412e-95da-ebf1275e3a21.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9eabf30e-dda6-465d-a0dc-fa933d25ef85.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/99a7068f-d297-4d2e-b264-59677d9261b4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/dcb948d3-8410-43ad-b655-c8755424d4a2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/26885b0f-a783-42eb-90d2-552d6a663158.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/2bbf83cf-6cf0-4faa-a1cb-6b98983ddb5d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3350c22a-a56e-47cd-9f41-46efe17e8461.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b542e695-e4ba-47d3-8932-fd8061b05ec0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/5b6ff252-0cbf-4327-83df-7982e5173c8c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6c169544-cb22-4e25-b504-5f3633c6c9c8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/408ca45a-ffb9-486f-8d32-3b8d7c815f6a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/68b31d55-74a5-4002-ab65-25b554116502.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/debcccf8-478b-4df4-91e7-08d674bbfe23.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d3bcbbc2-de8e-40e0-9da8-a53c70e4f883.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ebe1f5a7-eec1-4d2a-a441-36034c589a88.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/38aaed32-2edc-42fc-be18-945beab9c1c9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/304ad9a7-9bdb-47f9-b85f-837a76ee4b0b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fd2b4870-64f0-4f18-ac9f-b5a02ef11aae.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/d1cf059e-1450-4e69-9d40-91d2242bec1d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7f1d4bda-09f9-4652-9197-c5ec6e025197.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/6c928064-68ec-4c20-af87-9847ad857849.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b24b38e3-5cea-4a8a-9844-d7fd2442b3d3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/319d42aa-c1eb-48d1-a6c7-4131db267eec.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fe4b1852-fb2c-476e-9693-a9ebb14ddbf1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3aa70931-d21e-4727-903a-588f89cc5e67.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9bf8e30e-a74a-4e74-8fbb-9f878e6f097e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f9f5d9d1-f4cb-43fa-98d1-04ae2ba96800.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e58390b9-ac65-4961-bb4a-e0403bab4296.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f7f6df04-1001-49b3-a3d3-c6793601a3cc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/408d4954-e6e6-4a7b-a2f3-4c395f939577.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bc668f83-9233-494a-892e-4a46b6c1a380.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/dd3e93bb-8786-4195-b3a7-bd45decb8c97.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fb92d9e0-3ba1-40f9-b635-462669a48b25.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4c798536-e80f-4834-9a64-d1ff286a709d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/583ea627-cca8-4a6f-babb-ed8dc62367aa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/627f3ca8-dcd2-4259-9348-619db30e645e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/b7168353-bafd-4fbc-821a-35fa255b9272.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/66f2a992-516e-4db3-b868-d4def471931e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a137ced7-06fb-4a9d-a48c-da176511471a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/cc03add6-b5cd-4902-afc5-beb88d8c1171.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d70da3d3-68ae-4e6f-9718-d8dec063809c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fa0e0baf-7b80-450f-a330-16e82db29781.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2bdb8a1e-fe8c-4e59-96ec-dd9d4c70b812.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/51bd09be-655e-4eaf-937e-795940ec5f33.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cec812ce-758f-4395-8b9b-3aa2a57670f1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2f403b4e-f17d-4b73-a3ec-ac4d916d594b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/28ce762b-31ab-49be-80f5-c1659907471c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b32da6d6-be8c-4e45-a9af-f9b79449a868.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/b0c4a1b2-b9e3-4003-92ac-31ce57d7d35b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/78c8b369-203f-479d-a94a-083dd193e612.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3f47b101-184f-4cd3-afce-3b931c7ef972.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7a1d2832-4d1e-40b4-ab4a-554152e274e4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d3459766-5e21-41f7-97ae-36610a4203f8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fe9f475b-bdbf-4613-879e-a5d68699641b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d838f359-c6f7-4e9f-bd5b-1cf84fa05bb0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/2149d62a-eac6-4625-ade6-2f02fe1954b0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e0d6191a-3858-4f63-bafc-adbe2686a8f0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ed5b1126-2482-42c6-817c-efbe3d3c75a0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2f7f96ba-052b-4087-8ae6-9b15ce5bba7f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4001fc67-0dde-4e92-ad62-bed5bcaa9592.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/76ed89fb-e236-4e4e-92ef-f51e60785b68.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2ede46a7-d9c2-4557-b287-9088971af4d2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b1e389af-34e8-4862-9bb1-261ad8717711.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e74afbb5-5590-4a9f-85a7-3bf78f8f763e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a8a9e612-7ce3-49f2-bdea-0aae34f3602d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ff2c47d7-b3b6-4e07-8f8f-79002b227346.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/13a76f88-3e94-46bd-98a5-ec1722e96e12.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/bb4871a4-9465-4484-b580-7525fd862103.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7df44759-b6e8-4713-af1b-a443226cf71f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f0bce199-d8f3-4b90-9193-7867ca735330.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/5b5c3b53-429f-4a5f-9d48-ff3c2d4211c5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/5fbae75d-c987-4579-8759-27714f0a4e50.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/efd91d0d-f3bd-4f60-bc40-66778e9756d8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/505ad0b9-ed10-40b9-b57c-7e6c99842693.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5698405d-7404-47a9-b601-71193d468652.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/72e50718-2f1d-45e0-9d29-957dc0691cfb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/760dd34c-217d-4261-85c2-82564972f4cb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6a0591d4-3894-42cd-8f1b-a5726247d173.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7fbdea07-415b-4656-814d-96cd02d70a23.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/01b566bc-9ab6-4523-a43a-168d3cae49f3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/eccbc7bf-c3f9-429d-a390-463a04d80efc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/25f22ad5-b30d-4299-ad3b-0c203d10ed21.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ce5fa11c-4b01-41d0-ada3-145404035c73.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/874e2970-e45b-4a9a-ab0f-0caead08022d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6f2783fc-981d-46dd-b12e-53f6162b4222.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0bf48ec5-7659-411c-a468-1c729580bc54.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/29f970b4-d979-4ac2-8064-71cebf6e9817.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4d2a0196-a54b-4937-bb22-49ec0792d0f5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6c33b8ec-02f8-415a-838c-15a2ddb7c5f2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/73eaef65-8626-4333-a4a0-49d9d3415361.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ec06839c-ec0a-449e-a9b5-440025dbe774.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/ec3f770c-307a-4a2e-8345-25366fac23c0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c73e5814-5397-45ea-b495-7a8d0a582b8b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/7abff3a0-2e50-49ae-a58c-822aa3fef8a1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/33a58366-1c41-44a9-8ef6-2aaaa8f1e2a5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/44c86f8d-1469-40b7-825f-c39817ef09b6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1525cfb4-21bc-4c8e-9c87-138e6294b7f1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/be4d8991-f392-4170-af98-0985c3d8d6a6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2cb225f4-ed1d-46d7-aa4e-a514cd40b788.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2722ea8d-d6be-46ae-afa6-3c28ec167b4d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f97eb147-2c31-4297-8cce-4104bee2cee6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/284f5140-9158-4442-ab7b-5809b4331c54.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/18a46a08-9300-4cc4-96a6-999f034fb951.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e45f9279-b012-454b-8b47-97dec92d9594.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1e15bd2b-4eb0-4236-8cfb-8cb1317dbb7c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5f171770-0d04-471b-a0e8-37b80f690e95.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/dbfc222b-328d-4b5f-a87d-4812a133fc38.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/60fb2150-389f-4cd3-beea-23bc0517b7fa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/00bb5ade-d4aa-4621-9da1-fe2200aee55a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7fa83f04-0e43-4e54-a28c-66cc3555a81f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/74593292-7676-49c0-ba7d-78a3a8cb2d30.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6322c33c-4fbd-4fa1-84d9-a817e6b55f2c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/202fbceb-9c9c-4fd8-a26c-abbd5e0ffb75.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7abd3f4b-0846-4853-abdb-0f118b2de270.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/080736c2-23cb-4470-9e16-f6d487f2ee0a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/212e2dad-a61c-4256-8352-685b5bfa1cbe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/28195e4a-c029-46f1-baef-c1b9a9a317f6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/16679163-e474-4223-8b9f-814de3ed7a2b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e5384ddf-b317-4c87-9400-ff38f295882d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ad881cda-f4aa-4112-89a8-09f727b1addb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1f0bf06a-1b08-43d7-85db-45bd30ac3201.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9b363f28-cb53-477f-9ff3-fa2cef11657c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f69a541a-ed34-49d4-af4b-886c73eb7e49.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/83c5d38a-b278-46bc-8d6d-283e7c5ad8cc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2fff283d-7a90-4412-942c-11151ef39404.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/232488dc-1da1-4af2-9b88-a2ccfb7218ce.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3ea4c9b2-7d2e-4ab0-9e2e-a36459bfa0b9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c4adde6f-4e8e-4745-a39b-f66696cc4e4f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3e430013-8245-4c8d-87c4-fa202e1d7bff.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/0c74fd51-24ce-4fa8-b617-cba72330e2cc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/909b98f2-63b9-4bef-9ee6-f61bb153d755.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/b5d71624-be01-4b44-a6bb-fcc3d4cb5ecb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/548272e3-f0a4-42c8-9424-588a9ff22be4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e649af85-94e4-4abd-b694-1ffef841ba05.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f2b2f8fc-d779-4814-a541-cd9798877281.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6ac8121c-19e3-4806-bd59-0fed265a4d78.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9a885208-3268-47a8-afeb-3be7324f878e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/92e39c5c-216e-4cb1-a20e-fc1f858585ac.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0f86384d-9901-431b-afdd-0dd122ad73c4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8603acd2-a884-4166-a80e-1231536c1305.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/98417cb3-9531-4ddb-8a60-6113c6ad1e74.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/06e551b0-c515-4440-91e5-60d2919e1478.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b96aec51-50c2-4571-ab4f-04484883e00d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/eac90147-fd98-469a-ba51-3da44f397780.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2d07eca3-3be1-41a2-a20f-37cc502a345a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/4d5c8844-4c25-49e6-aaa9-7e1309dee5f4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/869f224b-bacc-4299-b0f2-abfbffc8541c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3290dd91-beae-4ba2-94bd-fc146593e293.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/48fa9c8b-c0b1-4128-9935-50e59015033d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a2b8c059-d922-457b-9661-466f6e6468a2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bbebe55f-b65a-42f3-b7fd-10fd98d323d5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ca175c58-3eda-46cb-95b1-da757edcf9c1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/491d4fd5-06ff-4bd6-a358-65e78f8d80fa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/674a2ac5-4829-4493-b185-c021d470299b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f559a10a-a0e9-4f57-957a-f6f6dcfad018.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/e7efdea0-10ae-414e-adca-5cf430ec85b7.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9e30597d-0f19-43fb-8bc1-3fcea2fa304c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ab9b79db-d0a9-4cd2-8bb9-4b15f75d1983.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/db39f052-9edb-4ea6-b1bd-9a95f65deb09.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5929e9f4-6568-4772-8fdd-6b582bc328fe.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3d744467-cdfb-4b60-bc1c-3872e29c7405.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/9b5a0388-0fb4-4cf4-ac74-6cef5d75967d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4eac852d-45e3-4c3a-9c5c-2979598d0153.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7c5c3152-4eb5-4069-96cc-1d1a88e395b4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1db29f5d-ee00-4a61-94fc-73484e93c99f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d601eb55-fe1e-4607-8325-e35680315786.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3dad2873-25d7-471a-8df8-162bd5866f1d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ef2b8cf9-4f1b-4a44-92ea-b3353638970b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/16c5459c-5d63-4a35-9b01-7023d124249a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/243061f7-0fd5-42a0-b547-ce9131f58683.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/31e740de-6e47-493d-9add-ce93397ac380.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8ef5f647-996d-4c68-8e0f-413ea0588c1e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cbcf3418-53e3-4e3a-854b-a8efcc9f05f4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ff70b572-b725-4995-9cdc-acf5bfb64c8b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7870ff4f-4e57-4032-a303-16df15c6e339.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/fb96b304-4871-44be-9342-e1f5600f9430.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6e21132c-b058-4cd2-881c-9257ca9105d6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d2721754-d9fc-4397-a913-380c4aa8ad48.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d2f93b16-e1e2-4067-80e5-45fcf08b00ee.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e7a7d526-676f-422c-b608-4cd2d7d74e89.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/94a1bf30-d64e-442f-8016-e44a151323fc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3b5c210f-ad15-443b-9328-faa1e951de9c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/2e006c3c-5722-4a2f-83d5-39d97be6cff6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/4d9ba510-7ef8-4ca5-b067-785eafc53d2f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/bc5ad464-7e80-4c96-8046-e6d8894144cb.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2227fd88-9a30-4fa4-88ae-ec3c5a9df58a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/5783ce81-d100-4818-9c26-1c66d290b886.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b6e04ebe-b4b0-43b8-b2e2-b53605463d92.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/0d4ecc7c-a4a3-44c5-b2f4-0c8880c53189.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1df819d4-f871-4294-b90c-47f6a6f5a20d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/875ce6ef-a5aa-4851-b782-9b691e72e63e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b4001085-68ef-4b38-847f-8459488132f5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b6a1a178-de9b-48d3-8a08-3bd4ec516de8.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/b79e4096-7093-44ab-9448-036ec98539c6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/63b6344b-2b70-4339-bc69-5f1062452e73.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c19f426d-b062-45a2-bd40-d30313e212dd.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2b5a55f8-eaed-45c3-8f0e-c2ceb649114c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/38062044-4b20-4ec4-8b3d-371eec56a024.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/1865f5cf-f7c6-4c78-b8fb-6cad4b2295b6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/460c7adf-b854-47e2-8a51-c47a1554187b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f5cf9b18-832e-48f4-bd50-f83f286b915b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/11b515e0-9d58-4f1e-8188-a3223e1027e5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a69ec4ca-26cf-42bf-9a13-a40cd1c37879.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/74375e94-ff4d-4edd-b75f-923a6fa8a7f1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/cb5716a0-97bf-4bd2-90d8-1b984841f32b.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/8df1b39b-4fd6-4a03-98a5-a49b4ee49f61.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/10a088fd-7496-4d5a-bf8f-4baafe6c8e39.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3d677259-6bb3-4fc2-9afe-aa172ae2dc28.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4a019919-87a5-4b96-bbf0-e0e4c28b913f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/51323ba0-cf2c-4f49-acfd-5356ea57b501.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/489f71c8-2ab1-4949-9e7c-a2ac93913609.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/4af8b7b7-f097-45e9-8547-8cb5daeba550.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/3cc7d620-0e17-49e0-90ad-eefcd37aaab6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/14f5ec7c-501a-4ecc-a213-242493b53326.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/0d589c29-dbfb-4cc8-b12d-1a53ca5f4373.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/aaf242f2-7e19-4298-9e44-6ac1d1f899aa.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/98cda7bc-ae70-4401-a196-8b702de290f6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/ebc3fa4c-f816-474c-802c-c796f018118e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/86692655-6b1a-488f-b414-00b3f05961ad.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e1ddbcba-51bf-40da-962b-68825468e662.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/385cad71-33f1-45db-bf9c-7da3554bdcb4.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/aea8cd89-1118-4b37-b65a-c2856ca6caa3.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2eb4788d-9683-42ee-9406-ab5f904348c6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/12311248-c4c8-47e9-9f7e-a345e1228f54.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/165e48a2-83bc-48ed-bf3b-219a5bbc104f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/bd838c6d-874c-4039-9b6b-bd3da5df8657.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f1f75e0f-53c6-4b2d-9c30-9e594bafe2dc.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/6e1133fa-3d0a-4031-93fd-f9898aee9534.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/c3842af2-b283-4573-9a4c-8eabb99d83d5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6db73b67-4600-4a69-aed7-9ef723f08ca9.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/6578623b-d10c-466e-903a-bb5edc39a76c.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/53e09035-d8f3-435c-8399-9b7b95ae3c89.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/005c567e-10b4-49b0-a516-790c5d0d2d4f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/21f29691-4ed3-40e0-96b4-e222593b681d.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/d0d20656-3dbd-49da-99ca-4ab886aca4d2.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/015c977a-0778-4853-b5f8-0d9376916056.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/58e3cb1f-8f55-4c43-9e2a-688ced0cd2c5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/59bc2516-61f9-44cc-90e9-d90ada30749e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/80de2f5c-c8ab-45a4-9354-ec7a80176d38.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/04ddebd9-17da-4bf7-b1b6-ef1dead464c0.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a44e2e02-d351-4530-b504-dfa4d239a40a.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/602fd69a-ce1a-415c-869f-583dcde44f66.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/0b074e7b-e641-4e65-85bc-f7dbabd6f856.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/a4963917-982b-4f84-a7a1-67d55ac0d96f.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/f9705033-3996-48c5-b072-033a5e40b4a6.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580001/9f95379d-3e6d-4b57-8c28-03e723f21c31.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/23faf9d5-5210-4842-ae66-5fe17c6cc513.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8b4bd911-09c5-44ef-a9e5-c7ecd13aee09.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/2d449df1-641b-4a7c-b957-6eee8acf99a5.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/22025dc0-4b98-4426-a36f-06c1813d2769.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/8adc2bf7-a464-4d85-9a26-f2c82a59a16e.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/7fa7b675-685c-494f-931c-0bd939853cc1.root',
        '/store/relval/CMSSW_14_0_9/RelValZEE_14/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_EOR3_TkDPGv2_RV245_2024-v4/2580000/e6b73b68-debc-45e9-8c4f-1287cf266776.root'
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
    globaltag = cms.string('140X_mcRun3_2024_realistic_EOR3_TkDPGv2'),
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

