# ASD 03-11 模块代表性阅读清单

日期：2026-07-06

用途：用户已读完 `01` 与 `02` 模块后，对剩余模块进行压缩阅读。原则是每个模块只读最具代表性的十几篇；同模块其余 note 可暂时跳过，仅在写作需要补例子时回查。

筛选依据：

- 只从当前 `Data/papers.csv` 中 `active_confirmed_core=True` 且 `note_exists=True` 的记录选。
- 以 `primary_module_for_filing` 为主，避免同一跨模块论文在多个模块重复消耗阅读时间。
- 优先覆盖该模块的主要 ASD 形态：LLM agent、multi-agent、robotic/self-driving lab、closed-loop optimization、scientific data analysis、domain-specific discovery。
- 保留少量历史锚点，因为它们常常比最新 agent paper 更能解释该模块的谱系。

## 03 Chemical Sciences

建议读 15 篇。读完这些后，化学模块的其他 note 可以先跳过。

1. `ASD-0094` Boiko 2023, Coscientist  
   Note: [Boiko_2023_Coscientist.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Boiko_2023_Coscientist.md>)
   代表意义：LLM 驱动 autonomous chemical research 的核心标志性论文。

2. `ASD-0093` Bran 2024, ChemCrow  
   Note: [Bran_2024_ChemCrow.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Bran_2024_ChemCrow.md>)
   代表意义：chemistry tool use agent 的基础入口，适合理解工具增强路线。

3. `ASD-0012` Yoshikawa 2023, Large language models for chemistry robotics  
   Note: [Yoshikawa_2023_Chemistry_Robotics_LLMs.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Yoshikawa_2023_Chemistry_Robotics_LLMs.md>)
   代表意义：LLM 与 chemistry robotics 接合的早期代表。

4. `ASD-0005` Song 2025, Robotic AI Chemist  
   Note: [Song_2025_Robotic_AI_Chemist.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Song_2025_Robotic_AI_Chemist.md>)
   代表意义：multi-agent + robotic chemist + on-demand chemical research。

5. `ASD-0158` Coley 2019, AI-planning flow synthesis platform  
   Note: [Coley_2019_Flow_Synthesis_AI_Planning.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Coley_2019_Flow_Synthesis_AI_Planning.md>)
   代表意义：AI planning + robotic flow synthesis 的历史锚点。

6. `ASD-0603` Bedard 2018, reconfigurable reaction optimization  
   Note: [Bedard_2018_Reconfigurable_Reaction_Optimization.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Bedard_2018_Reconfigurable_Reaction_Optimization.md>)
   代表意义：自动化反应优化平台，说明 LLM 之前的 self-driving chemistry 基础。

7. `ASD-0600` Mehr 2020, automatic execution of chemical synthesis literature  
   Note: [Mehr_2020_Universal_Chemical_Synthesis_Literature.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Mehr_2020_Universal_Chemical_Synthesis_Literature.md>)
   代表意义：把文献转成可执行化学程序，是 literature-to-lab 路线代表。

8. `ASD-0037` Dai 2024, autonomous mobile robots for exploratory synthetic chemistry  
   Note: [Dai_2024_Autonomous_Mobile_Robots.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Dai_2024_Autonomous_Mobile_Robots.md>)
   代表意义：移动机器人探索合成化学，体现实验空间自主探索。

9. `ASD-0056` Strieth-Kalthoff 2024, organic laser emitters  
   Note: [StriethKalthoff_2024_Organic_Laser_Emitters.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/StriethKalthoff_2024_Organic_Laser_Emitters.md>)
   代表意义：分布式、异步、闭环化学发现的强案例。

10. `ASD-0381` Bennett 2024, self-driving catalysis Pareto-front mapping  
    Note: [Bennett_2024_FastCat_Pareto_Front.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Bennett_2024_FastCat_Pareto_Front.md>)
    代表意义：催化反应多目标闭环优化。

11. `ASD-0506` Angello 2024, closed-loop transfer yields chemical knowledge  
    Note: [Angello_2024_ClosedLoop_Transfer_Chemical_Knowledge.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Angello_2024_ClosedLoop_Transfer_Chemical_Knowledge.md>)
    代表意义：从优化走向可迁移 chemical knowledge 的代表。

12. `ASD-0290` Sprueill 2024, ChemReasoner  
    Note: [Sprueill_2024_ChemReasoner.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Sprueill_2024_ChemReasoner.md>)
    代表意义：量子化学反馈参与 LLM reasoning/search。

13. `ASD-0070` Liu 2025, MOOSE-Chem3  
    Note: [Liu_2025_MOOSE_Chem3.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Liu_2025_MOOSE_Chem3.md>)
    代表意义：实验反馈驱动 hypothesis ranking。

14. `ASD-0665` Unknown 2026, TSAgent  
    Note: [Unknown_2026_TSAgent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Unknown_2026_TSAgent.md>)
    代表意义：transition state search 的 domain-specific agent。

15. `ASD-0838` Advincula 2026, Autonomous Flow Chemistry  
    Note: [Advincula_2026_Autonomous_Flow_Chemistry.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/03_Chemical_Sciences/Advincula_2026_Autonomous_Flow_Chemistry.md>)
    代表意义：连续流化学中的 ML-driven autonomous discovery。

## 04 Materials Science

建议读 15 篇。材料模块最大，读完这些后可先跳过其他材料 note。

1. `ASD-0001` Zhou 2025, MAPPS  
   Note: [Zhou_2025_MAPPS.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Zhou_2025_MAPPS.md>)
   代表意义：材料发现 agent 的综述式入口，串联 planning、physics、scientist-in-loop。

2. `ASD-0016` Szymanski 2023, A-Lab  
   Note: [Szymanski_2023_A_Lab.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Szymanski_2023_A_Lab.md>)
   代表意义：autonomous laboratory for novel materials 的核心案例。

3. `ASD-0379` MacLeod 2022, Pareto-front materials SDL  
   Note: [MacLeod_2022_Pareto_Front_Materials.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/MacLeod_2022_Pareto_Front_Materials.md>)
   代表意义：self-driving lab 推进材料性质 Pareto front。

4. `ASD-0503` MacLeod 2020, thin-film SDL  
   Note: [MacLeod_2020_SelfDriving_ThinFilm_Lab.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/MacLeod_2020_SelfDriving_ThinFilm_Lab.md>)
   代表意义：薄膜材料自驱实验室的经典代表。

5. `ASD-0410` Kusne 2020, CAMEO  
   Note: [Kusne_2020_CAMEO_Materials_Discovery.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Kusne_2020_CAMEO_Materials_Discovery.md>)
   代表意义：Bayesian active learning on-the-fly materials discovery。

6. `ASD-0455` Burger 2020, mobile robotic chemist  
   Note: [Burger_2020_Mobile_Robotic_Chemist.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Burger_2020_Mobile_Robotic_Chemist.md>)
   代表意义：机器人科学家在材料/光催化发现中的标志性案例。

7. `ASD-0466` Nikolaev 2014, CNT wall-selective growth  
   Note: [Nikolaev_2014_CNT_Wall_Selectivity.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Nikolaev_2014_CNT_Wall_Selectivity.md>)
   代表意义：自动化实验发现材料生长条件的早期锚点。

8. `ASD-0389` Li 2020, MAOSIC chiral perovskite  
   Note: [Li_2020_MAOSIC_Chiral_Perovskite.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Li_2020_MAOSIC_Chiral_Perovskite.md>)
   代表意义：cloud lab + perovskite nanocrystal discovery。

9. `ASD-0487` Dave 2020, battery electrolytes  
   Note: [Dave_2020_Autonomous_Battery_Electrolytes.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Dave_2020_Autonomous_Battery_Electrolytes.md>)
   代表意义：电池电解液闭环发现代表。

10. `ASD-0505` Szymanski 2023, ARROWS3  
    Note: [Szymanski_2023_ARROWS3_SolidState_Synthesis.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Szymanski_2023_ARROWS3_SolidState_Synthesis.md>)
    代表意义：solid-state synthesis 与 precursor selection。

11. `ASD-0046` Zhang 2025, TopoMAS  
    Note: [Zhang_2025_TopoMAS.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Zhang_2025_TopoMAS.md>)
    代表意义：topological materials multi-agent system。

12. `ASD-0084` Ghafarollahi 2025, AtomAgents Alloy  
    Note: [Ghafarollahi_2025_AtomAgents_Alloy.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Ghafarollahi_2025_AtomAgents_Alloy.md>)
    代表意义：physics-aware multimodal multi-agent alloy design。

13. `ASD-0096` Ansari 2024, dZiner  
    Note: [Ansari_2024_dZiner.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Ansari_2024_dZiner.md>)
    代表意义：rational inverse design with AI agents。

14. `ASD-0154` Liang 2025, AMASE  
    Note: [Liang_2025_AMASE.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Liang_2025_AMASE.md>)
    代表意义：experiment-theory real-time closed-loop interaction。

15. `ASD-0680` Liu 2026, ElementsClaw superconductors  
    Note: [Liu_2026_ElementsClaw_Superconductors.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/04_Materials_Science/Liu_2026_ElementsClaw_Superconductors.md>)
    代表意义：atomic models + language agents for superconductor discovery。

## 05 Earth and Environmental Sciences

建议读 12 篇。这个模块主题集中在 climate / Earth observation / geospatial / EO-1 历史线。

1. `ASD-0633` Guo 2025, EarthLink  
   Note: [Guo_2025_EarthLink_Climate_Science.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Guo_2025_EarthLink_Climate_Science.md>)
   代表意义：self-evolving AI agent system for climate science。

2. `ASD-0623` Wang 2026, ClimAgent  
   Note: [Wang_2026_ClimAgent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Wang_2026_ClimAgent.md>)
   代表意义：open-ended climate science analysis。

3. `ASD-0649` Pantiukhin 2026, CMIP-Forge  
   Note: [Pantiukhin_2026_CMIP_Forge.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Pantiukhin_2026_CMIP_Forge.md>)
   代表意义：retrieval、compute、self-review 的 climate workflow。

4. `ASD-0635` Zhang 2026, TianJi  
   Note: [Zhang_2026_TianJi_Autonomous_Meteorologist.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Zhang_2026_TianJi_Autonomous_Meteorologist.md>)
   代表意义：atmospheric science physical mechanism discovery。

5. `ASD-0653` Feng 2025, Earth-Agent  
   Note: [Feng_2025_Earth_Agent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Feng_2025_Earth_Agent.md>)
   代表意义：Earth observation agent 的大入口。

6. `ASD-0650` Zhao 2026, OpenEarth-Agent  
   Note: [Zhao_2026_OpenEarth_Agent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Zhao_2026_OpenEarth_Agent.md>)
   代表意义：from tool calling to tool creation for Earth observation。

7. `ASD-0726` Jaber 2026, AutoClimDS  
   Note: [Jaber_2026_AutoClimDS_Climate_Data_Science.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Jaber_2026_AutoClimDS_Climate_Data_Science.md>)
   代表意义：knowledge graph + climate data science agent。

8. `ASD-0727` Liang 2026, GeoAgentic-RAG  
   Note: [Liang_2026_GeoAgentic_RAG.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Liang_2026_GeoAgentic_RAG.md>)
   代表意义：geospatial reasoning and visual insight generation。

9. `ASD-0772` Liu 2026, TRACE Seismology  
   Note: [Liu_2026_TRACE_Seismology.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Liu_2026_TRACE_Seismology.md>)
   代表意义：seismology physical reasoning 的代表。

10. `ASD-0783` Yao 2026, RemoteAgent  
    Note: [Yao_2026_RemoteAgent_Earth_Observation.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Yao_2026_RemoteAgent_Earth_Observation.md>)
    代表意义：vague human intent 到 Earth observation action。

11. `ASD-0722` Chien 2005, Autonomous Earth-Observing Sensorweb  
    Note: [Chien_2005_Autonomous_Earth_Observing_Sensorweb.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Chien_2005_Autonomous_Earth_Observing_Sensorweb.md>)
    代表意义：Earth observation autonomy 的早期系统锚点。

12. `ASD-0859` Davies 2006, EO-1 volcanism monitoring  
    Note: [Davies_2006_EO1_Volcanism_Monitoring.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/05_Earth_and_Environmental_Sciences/Davies_2006_EO1_Volcanism_Monitoring.md>)
    代表意义：EO-1 autonomous science 在地球科学事件监测中的代表案例。

## 06 Life Sciences

建议读 15 篇。生命科学模块可用这些覆盖 bioinformatics、single-cell、protein、biofoundry、robot scientist。

1. `ASD-0501` King 2004, Robot Scientist  
   Note: [King_2004_Robot_Scientist.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/King_2004_Robot_Scientist.md>)
   代表意义：生命科学 autonomous discovery 的历史原点。

2. `ASD-0020` Roohani 2024, BioDiscoveryAgent  
   Note: [Roohani_2024_BioDiscoveryAgent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Roohani_2024_BioDiscoveryAgent.md>)
   代表意义：genetic perturbation experiment design。

3. `ASD-0034` Hao 2025, PerTurboAgent  
   Note: [Hao_2025_PerTurboAgent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Hao_2025_PerTurboAgent.md>)
   代表意义：sequential perturb-seq experiment planning。

4. `ASD-0014` Wang 2025, SpatialAgent  
   Note: [Wang_2025_SpatialAgent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Wang_2025_SpatialAgent.md>)
   代表意义：spatial biology agent 入口。

5. `ASD-0138` Xiao 2024, CellAgent  
   Note: [Xiao_2024_CellAgent_SingleCell_Analysis.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Xiao_2024_CellAgent_SingleCell_Analysis.md>)
   代表意义：single-cell analysis multi-agent framework。

6. `ASD-0085` Ghafarollahi 2024, ProtAgents  
   Note: [Ghafarollahi_2024_ProtAgents.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Ghafarollahi_2024_ProtAgents.md>)
   代表意义：protein discovery + physics/ML multi-agent。

7. `ASD-0114` Ghafarollahi 2025, SPARKS  
   Note: [Ghafarollahi_2025_Sparks_Protein_Design.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Ghafarollahi_2025_Sparks_Protein_Design.md>)
   代表意义：protein design principles discovered by multi-agent model。

8. `ASD-0370` Rapp 2024, SAMPLE protein fitness landscape  
   Note: [Rapp_2024_SAMPLE_Protein_Fitness_Landscape.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Rapp_2024_SAMPLE_Protein_Fitness_Landscape.md>)
   代表意义：protein fitness landscape self-driving lab。

9. `ASD-0518` Singh 2025, autonomous enzyme engineering  
   Note: [Singh_2025_Autonomous_Enzyme_Engineering.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Singh_2025_Autonomous_Enzyme_Engineering.md>)
   代表意义：AI-powered enzyme engineering platform。

10. `ASD-0521` Qu 2025, CRISPR-GPT  
    Note: [Qu_2025_CRISPR_GPT.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Qu_2025_CRISPR_GPT.md>)
    代表意义：gene-editing experiment automation。

11. `ASD-0049` Xin 2024, BIA  
    Note: [Xin_2024_BIA.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Xin_2024_BIA.md>)
    代表意义：bioinformatics workflow automation。

12. `ASD-0055` Su 2025, BioMaster  
    Note: [Su_2025_BioMaster.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Su_2025_BioMaster.md>)
    代表意义：multi-agent automated bioinformatics analysis。

13. `ASD-0097` Alber 2026, CellVoyager  
    Note: [Alber_2026_CellVoyager.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Alber_2026_CellVoyager.md>)
    代表意义：compbio agent autonomous biological data analysis。

14. `ASD-0745` Jin 2025, BioLab  
    Note: [Jin_2025_BioLab_Life_Sciences.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Jin_2025_BioLab_Life_Sciences.md>)
    代表意义：life sciences end-to-end multi-agent research system。

15. `ASD-0833` Jang 2026, Virtual Cells Mechanistic Reasoning  
    Note: [Jang_2026_Virtual_Cells_Mechanistic_Reasoning.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/06_Life_Sciences/Jang_2026_Virtual_Cells_Mechanistic_Reasoning.md>)
    代表意义：virtual cell mechanistic reasoning，适合作为 frontier case。

## 07 Medical and Health Sciences

建议读 15 篇。这个模块建议把 drug discovery、clinical/medical reasoning、pathology/biomarker、biomedical co-scientist 分开理解。

1. `ASD-0115` Gottweis 2025, AI Co-Scientist  
   Note: [Gottweis_2025_Co_Scientist.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Gottweis_2025_Co_Scientist.md>)
   代表意义：biomedical AI co-scientist 的核心入口。

2. `ASD-0118` Huang 2025, Biomni  
   Note: [Huang_2025_Biomni.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Huang_2025_Biomni.md>)
   代表意义：general-purpose biomedical AI agent。

3. `ASD-0002` Zhu 2025, HealthFlow  
   Note: [Zhu_2025_HealthFlow.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Zhu_2025_HealthFlow.md>)
   代表意义：healthcare research self-evolving agent。

4. `ASD-0008` Fehlis 2025, Tippy DMTA  
   Note: [Fehlis_2025_Tippy_DMTA.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Fehlis_2025_Tippy_DMTA.md>)
   代表意义：DMTA cycle laboratory automation。

5. `ASD-0024` Ock 2025, AgentD  
   Note: [Ock_2025_AgentD.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Ock_2025_AgentD.md>)
   代表意义：modular drug discovery task execution。

6. `ASD-0028` Liu 2024, DrugAgent  
   Note: [Liu_2024_DrugAgent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Liu_2024_DrugAgent.md>)
   代表意义：drug discovery programming automation。

7. `ASD-0113` Gao 2025, PharmAgents  
   Note: [Gao_2025_PharmAgents.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Gao_2025_PharmAgents.md>)
   代表意义：virtual pharma multi-agent system。

8. `ASD-0054` Swanson 2025, Virtual Lab Nanobodies  
   Note: [Swanson_2025_Virtual_Lab_Nanobodies.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Swanson_2025_Virtual_Lab_Nanobodies.md>)
   代表意义：AI agents design SARS-CoV-2 nanobodies with experimental validation。

9. `ASD-0357` Zhang 2025, OriGene  
   Note: [Zhang_2025_OriGene.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Zhang_2025_OriGene.md>)
   代表意义：virtual disease biologist for therapeutic target discovery。

10. `ASD-0531` Jiang 2026, GALILEO  
    Note: [Jiang_2026_GALILEO_Therapeutic_Discovery.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Jiang_2026_GALILEO_Therapeutic_Discovery.md>)
    代表意义：embodied AI scientist for therapeutic discovery。

11. `ASD-0548` Roberts 2026, OpenScientist  
    Note: [Roberts_2026_OpenScientist_Biomedical_Discovery.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Roberts_2026_OpenScientist_Biomedical_Discovery.md>)
    代表意义：open agentic AI co-scientist evaluation。

12. `ASD-0715` Ke 2025, BioDisco  
    Note: [Ke_2025_BioDisco.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Ke_2025_BioDisco.md>)
    代表意义：hypothesis generation with evidence and feedback。

13. `ASD-0716` Ni 2025, Bio AI Agent CAR-T  
    Note: [Ni_2025_Bio_AI_Agent_CAR_T.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Ni_2025_Bio_AI_Agent_CAR_T.md>)
    代表意义：CAR-T therapy development pipeline。

14. `ASD-0678` Schmon 2026, Latent-Y  
    Note: [Schmon_2026_Latent_Y.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Schmon_2026_Latent_Y.md>)
    代表意义：lab-validated autonomous agent for de novo drug design。

15. `ASD-0828` Nasser 2026, SAGE pathology biomarker discovery  
    Note: [Nasser_2026_SAGE_Pathology_Biomarker_Discovery.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/07_Medical_and_Health_Sciences/Nasser_2026_SAGE_Pathology_Biomarker_Discovery.md>)
    代表意义：computational pathology biomarker discovery。

## 08 Agricultural, Food, Forestry, Animal and Fishery Sciences

该模块目前 primary 记录只有 3 篇，建议全读。

1. `ASD-0510` Chen 2026, PhenoAssistant  
   Note: [Chen_2026_PhenoAssistant.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences/Chen_2026_PhenoAssistant.md>)
   代表意义：plant phenotyping multi-agent system。

2. `ASD-0634` Jin 2025, Aleks  
   Note: [Jin_2025_Aleks.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences/Jin_2025_Aleks.md>)
   代表意义：plant science autonomous discovery。

3. `ASD-0695` Huang 2024, FoodPuzzle  
   Note: [Huang_2024_FoodPuzzle.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/08_Agricultural_Food_Forestry_Animal_and_Fishery_Sciences/Huang_2024_FoodPuzzle.md>)
   代表意义：LLM agents as flavor scientists。

## 09 Engineering and Industrial Technology Sciences

建议读 13 篇。重点覆盖 CFD/FEA/CAD/process design/instrumentation。

1. `ASD-0504` Gongora 2020, BEAR Mechanical Design  
   Note: [Gongora_2020_BEAR_Mechanical_Design.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Gongora_2020_BEAR_Mechanical_Design.md>)
   代表意义：autonomous researcher for mechanical design 的历史锚点。

2. `ASD-0429` Deneault 2021, autonomous additive manufacturing  
   Note: [Deneault_2021_AM_ARES.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Deneault_2021_AM_ARES.md>)
   代表意义：3D printing + Bayesian optimization。

3. `ASD-0688` Feng 2025, OpenFOAMGPT 2.0  
   Note: [Feng_2025_OpenFOAMGPT_2_0.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Feng_2025_OpenFOAMGPT_2_0.md>)
   代表意义：CFD automation 的较完整版本。

4. `ASD-0782` Xu 2025, CFDagent  
   Note: [Xu_2025_CFDagent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Xu_2025_CFDagent.md>)
   代表意义：zero-shot multi-agent complex flow simulation。

5. `ASD-0052` Tian 2025, autonomous finite element analysis  
   Note: [Tian_2025_Autonomous_Finite_Element_Analysis.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Tian_2025_Autonomous_Finite_Element_Analysis.md>)
   代表意义：FEA collaboration optimization。

6. `ASD-0747` Zhang 2026, VFEAgent  
   Note: [Zhang_2026_VFEAgent_Finite_Element_Analysis.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Zhang_2026_VFEAgent_Finite_Element_Analysis.md>)
   代表意义：multimodal end-to-end automated FEA。

7. `ASD-0757` Barkley 2026, CADSmith  
   Note: [Barkley_2026_CADSmith.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Barkley_2026_CADSmith.md>)
   代表意义：multi-agent CAD generation with validation。

8. `ASD-0758` Son 2026, CAD generation with FEA feedback  
   Note: [Son_2026_CAD_Generation_FEA_Feedback.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Son_2026_CAD_Generation_FEA_Feedback.md>)
   代表意义：CAD generation agents using simulation feedback。

9. `ASD-0779` Tian 2026, Text to Simulation  
   Note: [Tian_2026_Text_to_Simulation_Process_Design.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Tian_2026_Text_to_Simulation_Process_Design.md>)
   代表意义：chemical process design workflow。

10. `ASD-0780` Schaefer 2026, agentic flowsheet simulations  
    Note: [Schaefer_2026_Agentic_Flowsheet_Process_Design.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Schaefer_2026_Agentic_Flowsheet_Process_Design.md>)
    代表意义：model-based process design。

11. `ASD-0805` Du 2026, TurboAgent  
    Note: [Du_2026_TurboAgent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Du_2026_TurboAgent.md>)
    代表意义：turbomachinery aerodynamic design。

12. `ASD-0511` Vriza 2026, AI agents operating scientific instruments  
    Note: [Vriza_2026_AI_Agents_Scientific_Instruments.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Vriza_2026_AI_Agents_Scientific_Instruments.md>)
    代表意义：advanced scientific instruments learning on the job。

13. `ASD-0789` Wall 2026, TEM Agent  
    Note: [Wall_2026_TEM_Agent.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/09_Engineering_and_Industrial_Technology_Sciences/Wall_2026_TEM_Agent.md>)
    代表意义：transmission electron microscopy automation。

## 10 Aerospace, Marine and Transportation Sciences

建议读 12 篇。这个模块是历史谱系很强的 autonomous science operations 模块。

1. `ASD-0645` Tran 2004, EO-1 Autonomous Sciencecraft  
   Note: [Tran_2004_Autonomous_Sciencecraft_EO1.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Tran_2004_Autonomous_Sciencecraft_EO1.md>)
   代表意义：spaceborne autonomous science 的历史起点。

2. `ASD-0703` Sherwood 2006, EO-1 and sensor webs  
   Note: [Sherwood_2006_EO1_Autonomous_Science_Agents.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Sherwood_2006_EO1_Autonomous_Science_Agents.md>)
   代表意义：autonomous science agents + sensor webs。

3. `ASD-0719` Rabideau 2006, EO-1 mission operations  
   Note: [Rabideau_2006_EO1_Mission_Operations_Onboard_Autonomy.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Rabideau_2006_EO1_Mission_Operations_Onboard_Autonomy.md>)
   代表意义：EO-1 onboard autonomy in mission operations。

4. `ASD-0691` Castano 2007, OASIS rover science  
   Note: [Castano_2007_OASIS_Rover_Science.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Castano_2007_OASIS_Rover_Science.md>)
   代表意义：opportunistic rover science。

5. `ASD-0696` Estlin 2012, AEGIS Opportunity Rover  
   Note: [Estlin_2012_AEGIS_Opportunity_Rover.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Estlin_2012_AEGIS_Opportunity_Rover.md>)
   代表意义：automated science targeting。

6. `ASD-0697` Francis 2017, AEGIS ChemCam MSL  
   Note: [Francis_2017_AEGIS_ChemCam_MSL.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Francis_2017_AEGIS_ChemCam_MSL.md>)
   代表意义：Mars Science Laboratory deployment results。

7. `ASD-0854` Estlin 2008, enabling autonomous science for Mars rover  
   Note: [Estlin_2008_Enabling_Autonomous_Science_Mars_Rover.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Estlin_2008_Enabling_Autonomous_Science_Mars_Rover.md>)
   代表意义：Mars rover autonomous science 的综合锚点。

8. `ASD-0710` Francis 2024, AEGIS SuperCam  
   Note: [Francis_2024_AEGIS_SuperCam.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Francis_2024_AEGIS_SuperCam.md>)
   代表意义：AEGIS 延续到 Perseverance rover。

9. `ASD-0693` Wagstaff 2019, Europa Clipper onboard detection  
   Note: [Wagstaff_2019_Europa_Clipper_Onboard_Detection.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Wagstaff_2019_Europa_Clipper_Onboard_Detection.md>)
   代表意义：deep-space mission onboard science event detection。

10. `ASD-0713` Wagner 2024, Europa Lander autonomy prototype  
    Note: [Wagner_2024_Europa_Lander_Autonomy_Prototype.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Wagner_2024_Europa_Lander_Autonomy_Prototype.md>)
    代表意义：complex mission autonomy prototype。

11. `ASD-0627` Kim 2025, deep space belief-state planning  
    Note: [Kim_2025_Adaptive_Science_Operations_Deep_Space.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Kim_2025_Adaptive_Science_Operations_Deep_Space.md>)
    代表意义：adaptive science operations with planning。

12. `ASD-0647` Herrmann 2024, small body science operations with RL  
    Note: [Herrmann_2022_Autonomous_Small_Body_Science_Operations.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/10_Aerospace_Marine_and_Transportation_Sciences/Herrmann_2022_Autonomous_Small_Body_Science_Operations.md>)
    代表意义：reinforcement learning for autonomous small-body science。

## 11 Social, Behavioral, Economic and Knowledge System Sciences

建议读 14 篇。这个模块不是自然科学对象，而是 scientific knowledge system / peer review / reproducibility / social science automation。

1. `ASD-0132` Su 2025, VirSci  
   Note: [Su_2025_VirSci.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Su_2025_VirSci.md>)
   代表意义：multi-agent scientific idea generation。

2. `ASD-0140` Yang 2024, open-domain hypotheses discovery  
   Note: [Yang_2024_Open_Domain_Hypotheses_Discovery.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Yang_2024_Open_Domain_Hypotheses_Discovery.md>)
   代表意义：open-domain scientific hypothesis discovery。

3. `ASD-0624` Shao 2025, SciSciGPT  
   Note: [Shao_2025_SciSciGPT.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Shao_2025_SciSciGPT.md>)
   代表意义：science of science human-AI collaboration。

4. `ASD-0625` Gao 2025, ReviewAgents  
   Note: [Gao_2025_ReviewAgents.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Gao_2025_ReviewAgents.md>)
   代表意义：AI paper review benchmark/agent system。

5. `ASD-0626` Fang 2026, ProReviewer  
   Note: [Fang_2026_ProReviewer.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Fang_2026_ProReviewer.md>)
   代表意义：proactive scientific peer review agent。

6. `ASD-0652` Yu 2024, ResearchTown  
   Note: [Yu_2024_ResearchTown.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Yu_2024_ResearchTown.md>)
   代表意义：human research community simulation。

7. `ASD-0654` Zhu 2026, HLER  
   Note: [Zhu_2026_HLER.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Zhu_2026_HLER.md>)
   代表意义：economic research via multi-agent pipelines。

8. `ASD-0658` Kohler 2026, agentic reproduction of social-science results  
   Note: [Kohler_2026_Agentic_Reproduction_Social_Science.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Kohler_2026_Agentic_Reproduction_Social_Science.md>)
   代表意义：social-science reproducibility automation。

9. `ASD-0704` Zhang 2026, PaperRepro  
   Note: [Zhang_2026_PaperRepro.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Zhang_2026_PaperRepro.md>)
   代表意义：automated computational reproducibility assessment。

10. `ASD-0706` Zhang 2025, aiXiv  
    Note: [Zhang_2025_aiXiv.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Zhang_2025_aiXiv.md>)
    代表意义：AI scientist ecosystem / scientific publishing system。

11. `ASD-0717` Kumar 2026, Paper Circle  
    Note: [Kumar_2026_Paper_Circle.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Kumar_2026_Paper_Circle.md>)
    代表意义：research discovery and analysis framework。

12. `ASD-0849` Shao 2025, OmniScientist  
    Note: [Shao_2025_OmniScientist.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Shao_2025_OmniScientist.md>)
    代表意义：co-evolving ecosystem of human and AI scientists。

13. `ASD-0855` Unknown 2025, Automating Scientific Evaluation  
    Note: [Unknown_2025_Automating_Scientific_Evaluation.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Unknown_2025_Automating_Scientific_Evaluation.md>)
    代表意义：transparent and trustworthy peer review framework。

14. `ASD-0831` Balhoff 2026, phenotype ontology curation  
    Note: [Balhoff_2026_Phenotype_Ontology_Curation.md](</abs/path/C:/Users/20683/Desktop/综述/Autonomous Scientific Discovery/Notes/11_Social_Behavioral_Economic_and_Knowledge_System_Sciences/Balhoff_2026_Phenotype_Ontology_Curation.md>)
    代表意义：knowledge-system curation bottleneck 的特殊代表。

## How to Use This List

- 如果时间极紧：03、04、06、07 各读前 10 篇；05、09、10、11 各读前 8 篇；08 全读。
- 如果要写综述正文：按本清单读完即可，不需要继续逐篇读同模块剩余 note。
- 如果写到某个细分例子缺材料，再回到同模块剩余 note 中补 1-2 篇即可。
