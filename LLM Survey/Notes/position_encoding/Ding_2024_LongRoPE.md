# LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens
**作者**: Yiran Ding, Li Lyna Zhang, Chengruidong Zhang, Yuanyuan Xu, Ning Shang, Jiahang Xu, Fan Yang, Mao Yang | **年份**: 2024 | **来源**: Microsoft Research / arXiv | **arXiv**: 2402.13753

## 0. 摘要翻译
本文提出 LongRoPE，一种将 LLM 上下文窗口扩展至超过 200 万 token 的方法，同时保持在原始短上下文窗口上的性能。LongRoPE 引入三项关键创新：（1）通过搜索发现 RoPE 维度上存在的非均匀位置插值模式，即使无微调也可实现 8 倍扩展；（2）渐进式扩展策略，先微调至 256k 再通过第二轮搜索扩展至 2048k；（3）在原始短上下文上进行重新调整以恢复短上下文性能。

## 1. 方法动机
a) **为什么提出**: 已有方法（PI、YaRN）虽能扩展上下文，但在极端长度（百万级 token）下效果有限，且往往牺牲短上下文性能。
b) **现有痛点**: 
   - PI 的均匀缩放在极端扩展下损失过多位置信息
   - YaRN 的分区策略是手工设计的，可能不是最优的
   - 扩展后在短上下文任务上的性能退化
   - 需要大量微调数据和计算资源
c) **研究假设**: RoPE 各维度的最优缩放因子不是均匀的，通过搜索可以找到更好的非均匀缩放方案。渐进式扩展可以逐步适应更长的上下文。

## 2. 方法设计
a) **pipeline**: 
   1. **搜索阶段**：对 RoPE 每个维度独立搜索最优的缩放/插值因子
   2. **第一次扩展**：使用搜索到的因子微调模型至 256k
   3. **第二次搜索+扩展**：在 256k 基础上再次搜索，扩展至 2048k
   4. **短上下文恢复**：在原始短上下文（如 4k/8k）上重新调整 RoPE 因子
   5. 推理时根据输入长度动态切换因子

b) **模块功能**: 
   - 搜索算法：进化搜索找到每个 RoPE 维度的最优缩放因子
   - 渐进扩展：避免一步到位的极端压缩
   - 短上下文恢复：专门的因子集保持短上下文性能

c) **公式解释**:
   - 非均匀插值: $\theta'_i = \theta_i / \lambda_i$，其中 $\lambda_i$ 是第 $i$ 个维度的独立缩放因子
   - 搜索目标：最小化目标长度上的困惑度
   - 每个维度的 $\lambda_i$ 通过进化搜索优化，而非手工设计

## 3. 与其他方法对比
a) **本质不同**: 
   - 与 PI：PI 所有维度使用相同缩放因子，LongRoPE 每个维度独立优化
   - 与 YaRN：YaRN 将维度分为三组，LongRoPE 对每个维度单独搜索
   - 独创渐进式扩展 + 短上下文恢复策略
b) **创新点**: 
   - 发现 RoPE 维度的非均匀性，通过搜索找到最优缩放
   - 渐进式扩展避免一步到位的信息损失
   - 短上下文恢复策略解决"扩展后短上下文退化"问题
c) **适用场景**: 需要极长上下文（百万 token 级）的应用；在 Llama 2 和 Mistral 模型上验证。

## 4. 实验表现
a) **验证方式**: 在 LLaMA2 7B 和 Mistral 7B 上验证，评估困惑度和 passkey retrieval。
b) **关键数据**: 
   - 成功扩展至 2048k（200 万 token）上下文
   - 在 passkey retrieval 任务上 2048k 长度内保持高准确率
   - 短上下文恢复后，4k 上下文性能仅下降 <0.5 困惑度
   - 无微调的 8x 扩展（通过搜索到的非均匀因子）
c) **局限性**: 
   - 搜索过程需要一定计算资源
   - 缩放因子是模型特定的，不同模型需要重新搜索
   - 2048k 上下文的实际应用仍受硬件限制

## 5. 总结
a) **一句话概括**: LongRoPE 通过搜索每个 RoPE 维度的最优非均匀缩放因子，配合渐进式扩展和短上下文恢复策略，首次将 LLM 上下文窗口扩展至 200 万 token 量级。
b) **速记 pipeline**: Evolutionary Search per-dim $\lambda_i$ → Stage 1: Fine-tune to 256k → Stage 2: Search+Extend to 2048k → Short Context Recovery → Dynamic Factor Switching at Inference
