# Rainbow Perovskite 2025

## 基本信息
- **论文**: Autonomous Multi-Robot Synthesis and Optimization of Metal Halide Perovskite Nanocrystals
- **作者**: Jinge Xu et al.
- **年份**: 2025
- **来源**: Nature Communications 16:7841 (2025), doi:10.1038/s41467-025-63209-4
- **关键词**: system, self-driving-lab, materials-discovery, multi-robot, perovskite

## 核心思想
Metal halide perovskite nanocrystals 具有可调光学性质，但合成空间包含连续反应条件、离散 ligand 结构和多目标输出，传统 one-parameter-at-a-time 实验难以高效探索。要实现指定 emission energy 下高 PLQY、窄 FWHM 和稳定合成，需要自动化合成、实时表征和 ML 决策闭环。

这篇论文要解决的问题是：能否用多机器人 self-driving laboratory 在混合变量、高维、多目标的 MHP nanocrystal 合成空间中自主寻找 Pareto-optimal formulations。

## 方法细节
论文提出 Rainbow，一个 multi-robot self-driving laboratory。

硬件包括四个机器人：

1. liquid handling robot：负责 precursor preparation、多步 nanocrystal synthesis、采样和废液处理；
2. characterization robot：采集 UV-Vis absorption 和 emission spectra；
3. robotic plate feeder：补充 labware；
4. robotic arm：在不同机器人之间转移样品和 labware。

AI agent 使用 mixed-variable multi-objective Bayesian optimization。流程如下：

1. 人类定义 target peak emission energy、objectives 和 precursor library；
2. 系统用 Latin hypercube sampling 初始化实验；
3. 实验结果由 characterization robot 自动提取 E_P、proxy PLQY (P_PLQY) 和 FWHM；
4. surrogate model 根据新数据重新训练，并估计不确定性；
5. classifier 避免采样 non-emissive synthesis regions；
6. agent 生成 512 组 Sobol-sampled 候选条件，并以 noisy expected hypervolume improvement (NEHVI) 选择下一批 24 个实验条件；
7. Rainbow 硬件执行下一轮 synthesis 和 characterization。

## 关键结果

1. Rainbow 集成 automated NC synthesis、real-time characterization 和 ML-driven decision-making。
2. 系统在 6-dimensional input / 3-dimensional output parameter space 中导航。
3. 实验空间同时包含连续变量和离散 ligand structures。
4. Rainbow 绘制 targeted peak emission energy 下的 PLQY-FWHM Pareto fronts。
5. 论文报告了 6 种 organic acids 的 experimental Pareto-front mappings；Rainbow 可在约 **150 min** 的 design-build-test-learn cycle 中运行，并达到约 **230 个实验条件/天** 的通量。
6. 与未使用 classifier 的 BO 相比，classifier-assisted Rainbow 的 emissive NC synthesis rate 提高 **12.5%**，而不是直接减少 12.5% 实验次数。
7. Rainbow 在目标 E_P = 1.9-2.9 eV 的多个 campaign 中，一天内发现目标 E_P 下的 Pareto front，论文称相对纯人工探索实现超过 **350x** material discovery acceleration。
8. Rainbow 识别 scalable synthesis knowledge，并通过 scaled-up NC synthesis 展示 transferability。

## 与综述的关联

在 Scientific Workflow 中，Rainbow 覆盖 Experiment Design、Execution、Result Analysis、Verification 和 Evolution。它是 self-driving lab 中“多机器人 + 实时表征 + 多目标优化”的强样本。

在 Skill Lifecycle 中，它对应：

- Representation：合成条件、ligand 结构和 optical objectives 构成实验 skill space；
- Composition：四个机器人、表征设备和 BO agent 组合；
- Execution：自动合成、采样、光谱表征；
- Evolution：surrogate model 和 classifier 在每轮实验后更新；
- Verification：Pareto-front mapping、scaled-up synthesis 和光谱指标验证。

Evidence Role 应标为 **Infrastructure + Direct**。它证明科学 discovery skill 在材料领域必须和机器人执行、在线表征和多目标优化绑定。它也补足了我们框架中“tool-chain skill”之外的 physical lab skill。

## 局限性

Rainbow 聚焦 MHP nanocrystal synthesis，不是通用材料发现平台。人类仍需定义 target peak emission energy、objectives 和 precursor library。系统发现的是合成-性能关系和 Pareto-optimal formulations，不等同于完整机制解释或跨材料类别的通用发现能力。

## 核心贡献

Rainbow 的核心贡献是展示了一个多机器人 self-driving laboratory 能在混合变量、多目标 perovskite nanocrystal 合成空间中闭环优化，自动连接合成、表征、模型更新和 Pareto-front discovery。
