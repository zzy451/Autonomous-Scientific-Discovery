#!/bin/bash
# Normalization 论文 PDF 下载脚本
# 使用方法: cd "/Users/mjm/LLM Survey/Reference_pdf/normalization" && bash download_pdfs.sh

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "=== 开始下载 Normalization 论文 PDF ==="

# N-01: Batch Normalization (Ioffe, Szegedy, 2015)
curl -sL -o "N01_Ioffe_2015_BatchNorm.pdf" "https://arxiv.org/pdf/1502.03167" && echo "[OK] N-01 BatchNorm" || echo "[FAIL] N-01 BatchNorm"

# N-02: Layer Normalization (Ba, Kiros, Hinton, 2016)
curl -sL -o "N02_Ba_2016_LayerNorm.pdf" "https://arxiv.org/pdf/1607.06450" && echo "[OK] N-02 LayerNorm" || echo "[FAIL] N-02 LayerNorm"

# N-03: Instance Normalization (Ulyanov et al., 2016)
curl -sL -o "N03_Ulyanov_2016_InstanceNorm.pdf" "https://arxiv.org/pdf/1607.08022" && echo "[OK] N-03 InstanceNorm" || echo "[FAIL] N-03 InstanceNorm"

# N-04: Group Normalization (Wu, He, 2018)
curl -sL -o "N04_Wu_2018_GroupNorm.pdf" "https://arxiv.org/pdf/1803.08494" && echo "[OK] N-04 GroupNorm" || echo "[FAIL] N-04 GroupNorm"

# N-05: On Layer Normalization in the Transformer Architecture (Xiong et al., 2020)
curl -sL -o "N05_Xiong_2020_PreLN_PostLN.pdf" "https://arxiv.org/pdf/2002.04745" && echo "[OK] N-05 PreLN_PostLN" || echo "[FAIL] N-05 PreLN_PostLN"

# N-06: Understanding and Improving Layer Normalization / AdaNorm (Xu et al., 2019)
curl -sL -o "N06_Xu_2019_AdaNorm.pdf" "https://arxiv.org/pdf/1911.07013" && echo "[OK] N-06 AdaNorm" || echo "[FAIL] N-06 AdaNorm"

# N-07: CogView (Ding et al., 2021) - Sandwich LayerNorm
curl -sL -o "N07_Ding_2021_CogView.pdf" "https://arxiv.org/pdf/2105.13290" && echo "[OK] N-07 CogView" || echo "[FAIL] N-07 CogView"

# N-08: DeepNet / DeepNorm (Wang et al., 2022)
curl -sL -o "N08_Wang_2022_DeepNet.pdf" "https://arxiv.org/pdf/2203.00555" && echo "[OK] N-08 DeepNet" || echo "[FAIL] N-08 DeepNet"

# N-09: Root Mean Square Layer Normalization / RMSNorm (Zhang, Sennrich, 2019)
curl -sL -o "N09_Zhang_2019_RMSNorm.pdf" "https://arxiv.org/pdf/1910.07467" && echo "[OK] N-09 RMSNorm" || echo "[FAIL] N-09 RMSNorm"

# N-11: Scalable Diffusion Models with Transformers / DiT, adaLN-Zero (Peebles, Xie, 2023)
curl -sL -o "N11_Peebles_2023_DiT.pdf" "https://arxiv.org/pdf/2212.09748" && echo "[OK] N-11 DiT" || echo "[FAIL] N-11 DiT"

# N-12: Evolving Normalization-Activation Layers / EvoNorm (Liu et al., 2020)
curl -sL -o "N12_Liu_2020_EvoNorm.pdf" "https://arxiv.org/pdf/2004.02967" && echo "[OK] N-12 EvoNorm" || echo "[FAIL] N-12 EvoNorm"

# N-13: Fixup Initialization (Zhang et al., 2019)
curl -sL -o "N13_Zhang_2019_Fixup.pdf" "https://arxiv.org/pdf/1901.09321" && echo "[OK] N-13 Fixup" || echo "[FAIL] N-13 Fixup"

# N-14: T-Fixup (Huang et al., 2020)
curl -sL -o "N14_Huang_2020_TFixup.pdf" "https://arxiv.org/pdf/2004.08249" && echo "[OK] N-14 T-Fixup" || echo "[FAIL] N-14 T-Fixup"

# N-15: High-Performance Large-Scale Image Recognition Without Normalization / NF-Net (Brock et al., 2021)
curl -sL -o "N15_Brock_2021_NFNet.pdf" "https://arxiv.org/pdf/2102.06171" && echo "[OK] N-15 NF-Net" || echo "[FAIL] N-15 NF-Net"

# N-16: Transformers without Normalization / DyT (Zhu et al., 2025)
curl -sL -o "N16_Zhu_2025_DyT.pdf" "https://arxiv.org/pdf/2503.10622" && echo "[OK] N-16 DyT" || echo "[FAIL] N-16 DyT"

# N-17: Derf - Dynamic Erf (Chen et al., 2025)
curl -sL -o "N17_Chen_2025_Derf.pdf" "https://arxiv.org/pdf/2503.18184" && echo "[OK] N-17 Derf" || echo "[FAIL] N-17 Derf"

echo ""
echo "=== 下载完成 ==="
echo "共 16 篇论文 (N-10 QK-Norm 为实践总结无独立论文, N-18/N-19 为前沿/开放问题)。"
echo "请检查上方输出确认各文件是否下载成功。"
