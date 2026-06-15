# ResiDual: Transformer with Dual Residual Connections
**作者**: Shufang Xie, Huishuai Zhang, Junliang Guo, Xu Tan, Jiang Bian, Hany Hassan Awadalla, Arul Menezes, Tao Qin, Rui Yan | **年份**: 2023 | **arxiv**: 2304.14802

## 0. 摘要翻译
ResiDual 提出了一种融合 Pre-LN 和 Post-LN 优势的"双残差连接"架构。在每个 Transformer 块中同时维护两条并行的残差路径：Pre-LN 路径提供稳定的梯度"高速公路"，Post-LN 路径保持表示的多样性。这种设计解决了 Pre-LN 的表示坍塌问题和 Post-LN 的梯度消失问题。

## 1. 方法动机
- **Pre-LN 的问题**：表示坍塌（representation collapse）——高层的表示越来越相似，限制了模型容量
- **Post-LN 的问题**：梯度消失——深层网络训练不稳定
- 两种方案各有致命缺陷，需要一种"两全其美"的设计
- 理论上分析两种路径的互补性

## 2. 方法设计（重点：模块排列顺序及其理论分析）

### 双残差连接设计 (Pre-Post-LN / PPLN)
在每个 Transformer 块中同时运行两条残差流：

#### 流1：Pre-LN 路径（梯度高速公路）
```
x_{l+1} = x_l + SubLayer(LN(x_l))
```
- 提供直接的梯度传播路径
- 防止梯度消失
- 类似于 "skip connection highway"

#### 流2：Post-LN 路径（表示保持）
```
h_{l+1} = LN(h_l + SubLayer(h_l))
```
- 在每层后对表示进行归一化
- 保持各层表示的多样性
- 防止表示坍塌

#### 融合
- 两条路径的输出在下一层输入时进行融合（加权求和）
- 最终输出结合了两条路径的信息

### 理论保证
- **梯度下界**：Pre-LN 路径保证了梯度幅度的下界，防止梯度消失
- **表示多样性**：Post-LN 路径通过逐层归一化保持表示的多样性
- 两条路径互不干扰，各司其职

### 模块结构对比
```
Pre-LN:    x + Attn(LN(x))
Post-LN:   LN(x + Attn(x))
ResiDual:  同时维护两条路径，Pre-LN 保梯度，Post-LN 保表示
```

## 3. 与其他方法对比
| 方法 | 梯度流 | 表示多样性 | 训练稳定性 | 性能 |
|------|-------|-----------|-----------|------|
| Pre-LN | 好 | 差（坍塌） | 高 | 中 |
| Post-LN | 差（消失） | 好 | 低 | 高（若成功） |
| Admin | 自适应 | 中 | 高 | 高 |
| ResiDual | 好（Pre-LN 路径） | 好（Post-LN 路径） | 高 | 高 |

- ResiDual 与 Admin 的思路不同：Admin 是时间维度的自适应（早期→后期），ResiDual 是空间维度的并行（两条路径同时存在）
- 计算开销增加有限，因为两条路径共享子层计算

## 4. 实验表现
- **机器翻译**：在多个 WMT 基准上一致超越 Pre-LN 和 Post-LN 基线
- **不同深度**：在增加网络深度时，Post-LN 训练失败，ResiDual 保持稳定
- **不同数据量**：在小数据和大数据场景下均有优势
- **BLEU 分数**：持续超越两种基线方案
- 理论分析与实验结果一致

## 5. 总结
a) **一句话概括**：ResiDual 通过在每个 Transformer 块中并行维护 Pre-LN（保梯度）和 Post-LN（保表示）两条残差路径，同时解决了梯度消失和表示坍塌两个对立问题。

b) **速记 pipeline**：`Dual streams: [Pre-LN path: x + SubLayer(LN(x))] || [Post-LN path: LN(x + SubLayer(x))] -> Fuse`
