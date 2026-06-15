# CycleResearcher 2024

## 基本信息
- **论文**: CycleResearcher: Improving Automated Research via Automated Review
- **作者**: Yixuan Weng, Minjun Zhu, Guangsheng Bao, Hongbo Zhang, Jindong Wang, Yue Zhang, Linyi Yang
- **年份**: 2024
- **来源**: arXiv:2411.00816; ICLR 2025
- **关键词**: automated-research, automated-review, reinforcement-learning, research-review-refinement

## 核心思想
CycleResearcher 将自动研究和自动审稿连接成 research-review-refinement 循环。

## 方法细节
系统包含 CycleResearcher 和 CycleReviewer，后者为前者提供迭代反馈，并用于偏好训练。

## 关键结果
论文报告自动 reviewer 在预测论文分数上优于单个人类 reviewer，生成论文得分接近 accepted paper level。

## 局限性
评价主要发生在模拟论文和审稿环境，科学真实性仍需人工和执行验证。

## 核心贡献
把研究生成和评审反馈整合为闭环训练框架。

## 与综述的关联
适合放入 `X2-Y5-Z1/Z2/Z3/Z6/Z7/Z8`，支撑自动研究中的 review-driven harness evolution。

## 原文核对与分类复核
- **原文核对**：原文包括 CycleResearcher 和 CycleReviewer，覆盖 literature review、manuscript preparation、peer review、paper refinement，并通过 iterative preference training 改进。
- **机制判断**：该系统的重点是 research-review cycle，本质上是研究 harness / evaluator 的共同演化。
- **分类复核**：保持 `严格 ASD`；`X2` 正确；`Y5` 正确，因为 researcher/reviewer 通过训练和反馈形成工作流能力演化；`Z1,Z2,Z3,Z6,Z7,Z8` 正确。
- **写作用途**：适合作为“科研闭环不只生成，还包括自动评审和修订”的例子。

## 深读补充（按 MARS 标准）

### 研究问题
CycleResearcher 关注能否用 open-source post-trained LLMs 自动完成研究和评审循环，而不是只让商业模型做研究助手。

### 系统架构 / 工作流
系统由 CycleResearcher 和 CycleReviewer 组成，覆盖 literature review、manuscript preparation、peer review 和 paper refinement。

### 关键机制
核心是 automated research-review cycle 与 iterative preference training。reviewer 的反馈被用于改进 researcher。

### 实验验证与证据
原文构建 Review-5k 和 Research-14k 数据集，报告 CycleReviewer 在预测论文分数方面接近人类 reviewer，CycleResearcher 生成论文可达到一定 simulated review score。

### 局限性补充
该系统的科学有效性主要由模拟评审衡量，不等同于真实科学发现或实验验证。

### XYZ 分类逐项解释
- `X2`：researcher 和 reviewer 构成角色分工。
- `Y5`：研究-评审循环和 preference training 改进 harness。
- `Z1,Z2,Z3,Z6,Z7,Z8`：覆盖文献、想法、方案、写作、评审和迭代。

### 综述写作用法
适合说明 ASD 闭环应包括 review / revision，而不只是生成研究想法。
