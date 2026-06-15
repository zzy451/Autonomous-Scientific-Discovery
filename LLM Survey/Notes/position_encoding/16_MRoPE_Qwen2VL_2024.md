# M-RoPE: Multimodal Rotary Position Embedding (Qwen2-VL)
**作者**: Peng Wang, Shuai Bai, Sinan Tan, et al. (Alibaba Qwen Team) | **年份**: 2024 | **arxiv**: 2409.12191

## 0. 摘要翻译
Qwen2-VL 是阿里巴巴通义千问团队推出的视觉语言模型，其核心位置编码创新为 M-RoPE（Multimodal Rotary Position Embedding）。M-RoPE 将 RoPE 的旋转位置编码从一维序列扩展到三维（时间、高度、宽度），为文本、图像和视频三种模态提供统一且模态感知的位置编码方案。配合动态分辨率（Naive Dynamic Resolution）机制，Qwen2-VL 能够处理任意分辨率的图像和任意长度的视频。

## 1. 方法动机
- 标准 RoPE 为一维序列设计，将所有 token 视为线性排列，无法表达图像的二维空间结构和视频的三维时空结构
- 简单地将图像 patch 展平为一维序列会丢失空间邻近性信息
- 视觉语言模型需要一种统一的位置编码方案，能同时处理文本（1D）、图像（2D）和视频（3D）的位置信息
- M-RoPE 的洞察：将 RoPE 的频率维度分组，分别编码不同的位置轴

## 2. 方法设计（重点：与六维度框架的关联）

### 2.1 三维位置 ID 设计
M-RoPE 为每个 token 分配三个位置 ID：temporal_id, height_id, width_id

**文本 token**:
- temporal_id = height_id = width_id = 递增的序列位置
- 三个维度使用相同的值，退化为标准 1D RoPE

**图像 token**:
- temporal_id = 图像在序列中的起始位置（所有 patch 共享）
- height_id = patch 在图像中的行索引
- width_id = patch 在图像中的列索引
- 这样保留了图像的 2D 空间结构

**视频 token**:
- temporal_id = 帧索引
- height_id = patch 在帧中的行索引
- width_id = patch 在帧中的列索引
- 完整保留了视频的 3D 时空结构

### 2.2 RoPE 频率维度分组
- 将 RoPE 的 d 个频率维度均分为 3 组，每组 d/3 个维度
- 第 1 组：使用 temporal_id 计算旋转角度
- 第 2 组：使用 height_id 计算旋转角度
- 第 3 组：使用 width_id 计算旋转角度
- 最终的位置编码 = 三组旋转的拼接

### 2.3 动态分辨率支持
- 图像不需要 resize 到固定分辨率，直接按原始分辨率切分 patch
- M-RoPE 的 height_id 和 width_id 自然适应不同的图像尺寸
- 视频帧数可变，temporal_id 自然适应不同长度的视频

### 与六维度框架的关联
- **位置编码维度**: M-RoPE 是 RoPE 在多模态场景下的自然扩展，从 1D 相对位置编码推广到 3D
- **与标准 RoPE 的关系**: 对纯文本输入，M-RoPE 退化为标准 RoPE（三个位置 ID 相同）
- **与 2D-RoPE 的关系**: 2D-RoPE（如 ViT 中使用的）只处理空间维度，M-RoPE 增加了时间维度
- **模态融合**: M-RoPE 提供了一种优雅的方式在同一注意力机制中融合不同模态的位置信息

## 3. 与其他方法对比
| 方法 | 维度 | 模态支持 | 动态分辨率 | 与 RoPE 兼容 |
|------|------|---------|-----------|-------------|
| 1D RoPE | 1D | 文本 | N/A | 是（本身） |
| 2D RoPE | 2D | 图像 | 是 | 是 |
| M-RoPE (Qwen2-VL) | 3D | 文本+图像+视频 | 是 | 是（退化） |
| 可学习绝对 PE | 1D | 文本 | 否 | 否 |
| ALiBi | 1D | 文本 | N/A | 否 |

- M-RoPE 的优势在于统一性：一套编码方案处理所有模态
- 对纯文本场景无性能损失（退化为标准 RoPE）
- 对视觉场景保留了空间结构信息

## 4. 实验表现
- Qwen2-VL 在多个视觉语言基准上达到领先水平
- 在 DocVQA、ChartQA 等需要空间理解的任务上表现尤为突出（得益于 M-RoPE 保留的空间位置信息）
- 支持任意分辨率图像输入，无需 resize 导致的信息损失
- 视频理解任务上，temporal_id 帮助模型理解帧间时序关系
- 在 Qwen2.5-VL 中进一步验证和改进了 M-RoPE 的设计

## 5. 总结
a) M-RoPE 将 RoPE 的频率维度分为三组分别编码时间、高度、宽度位置，为文本/图像/视频提供统一的多模态位置编码，对纯文本退化为标准 RoPE，对视觉输入保留空间/时空结构。

b) 速记 pipeline: Token → 分配 (temporal_id, height_id, width_id) → RoPE 频率维度三等分 → 各组用对应 ID 计算旋转 → 拼接三组旋转 → 多模态位置编码
