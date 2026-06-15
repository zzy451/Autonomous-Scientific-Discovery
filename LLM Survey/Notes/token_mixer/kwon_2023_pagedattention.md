# Kwon et al. 2023 - Efficient Memory Management for Large Language Model Serving with PagedAttention

**论文信息**
- 标题: Efficient Memory Management for Large Language Model Serving with PagedAttention
- 作者: Woosuk Kwon, Zhuohan Li, Sicheng Zhuang, Ying Sheng, Lianmin Zheng, Chhavi P. Yadav, Zhouhan Lin, Hao Zhang, Joseph E. Gonzalez, Ion Stoica
- 年份: 2023
- arXiv: 2309.06180
- 会议: SOSP 2023

## 0. 摘要翻译
LLM推理的高吞吐服务需要同时处理多个请求。然而，现有系统因为KV cache内存管理效率低下而浪费了60-80%的GPU内存。受操作系统虚拟内存与分页机制启发，我们提出PagedAttention——一种允许KV cache存储在非连续内存空间中的注意力算法。基于此，我们构建了vLLM推理引擎，实现了近零内存浪费和灵活的内存共享。

## 1. 方法动机
a) **为什么提出**: LLM推理中KV cache占用大量GPU内存，但现有系统要求连续内存分配，导致碎片化和浪费
b) **现有方法痛点**: 
   - 预分配最大长度导致内部碎片
   - 不同请求间无法共享KV cache内存
   - 内存浪费限制了batch size和吞吐
c) **研究假设**: 借鉴OS的虚拟内存和分页机制，可以实现非连续KV cache存储

## 2. 方法设计
a) **方法流程**:
   - 将KV cache分成固定大小的"页"（blocks）
   - 使用块表(block table)映射逻辑地址到物理地址
   - 注意力计算时按块获取KV数据
   
b) **模块功能**:
   - **KV Cache Pages**: 固定大小的KV存储块（如16 tokens一块）
   - **Block Table**: 逻辑块号 → 物理块地址的映射表
   - **PagedAttention Kernel**: 支持非连续内存访问的注意力CUDA核
   - **Copy-on-Write**: 共享前缀时引用同一物理块，修改时复制
   
c) **公式解释**:
   - 注意力计算不变（仍是标准softmax attention）
   - 内存管理改变：从连续预分配变为按需分页
   - 内部碎片: 最多浪费一个block的空间（最后一块）

## 3. 与其他方法对比
a) **本质不同**: 不修改注意力计算，而是优化KV cache的内存管理
b) **创新点**: 
   - OS虚拟内存思想应用到GPU显存管理
   - 支持beam search等场景的内存共享
c) **适用场景**: LLM推理服务，尤其是高并发场景
d) **对比表格**:

| 特性 | 传统KV Cache | PagedAttention |
|------|-------------|----------------|
| 内存分配 | 连续预分配 | 非连续分页 |
| 内存浪费 | 60-80% | <4% |
| 内存共享 | 不支持 | 支持(Copy-on-Write) |
| 吞吐提升 | 基线 | 2-4x |

## 4. 实验表现
a) **验证方式**: OPT-13B/66B/175B推理吞吐测试
b) **关键数据**: 吞吐比FasterTransformer提升2-4倍；比Orca提升2-4倍
c) **优势场景**: 高并发LLM推理服务、长序列推理
d) **局限性**: 非连续访问可能引入轻微的内存访问开销

## 5. 学习与应用
a) **开源情况**: vLLM完全开源，已成为最流行的LLM推理框架之一
b) **实现细节**: block大小通常16 tokens；支持多种模型架构
c) **迁移可能性**: 已广泛应用于产业界LLM部署

## 6. 总结
a) **一句话概括**: 借鉴OS虚拟内存分页机制管理KV cache，消除内存碎片，将LLM推理吞吐提升2-4倍
b) **速记版pipeline**: KV Cache → 分页存储(Pages) → Block Table映射 → PagedAttention Kernel → 结果

**Token Mixer维度**: KV Cache管理优化，不改变注意力计算方式，而是优化KV cache的存储和访问模式
