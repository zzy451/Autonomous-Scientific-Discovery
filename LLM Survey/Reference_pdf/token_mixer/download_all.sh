#!/bin/bash
# Token Mixer 论文 PDF 下载脚本
# 使用方法: cd "/Users/mjm/LLM Survey/Reference_pdf/token_mixer/" && bash download_all.sh

DIR="/Users/mjm/LLM Survey/Reference_pdf/token_mixer"
cd "$DIR"

echo "=== 下载 Token Mixer 论文 PDF ==="

# --- 已引用论文 ---
echo "[1/25] Vaswani 2017 - Attention Is All You Need"
curl -sL -o "vaswani_2017_attention.pdf" "https://arxiv.org/pdf/1706.03762"

echo "[2/25] Kitaev 2020 - Reformer"
curl -sL -o "kitaev_2020_reformer.pdf" "https://arxiv.org/pdf/2001.04451"

echo "[3/25] Wang 2020 - Linformer"
curl -sL -o "wang_2020_linformer.pdf" "https://arxiv.org/pdf/2006.04768"

echo "[4/25] Choromanski 2021 - Performer"
curl -sL -o "choromanski_2021_performer.pdf" "https://arxiv.org/pdf/2009.14794"

echo "[5/25] Beltagy 2020 - Longformer"
curl -sL -o "beltagy_2020_longformer.pdf" "https://arxiv.org/pdf/2004.05150"

echo "[6/25] Yuan 2025 - NSA (Native Sparse Attention)"
curl -sL -o "yuan_2025_nsa.pdf" "https://arxiv.org/pdf/2502.11089"

echo "[7/25] Lu 2025 - MOBA"
curl -sL -o "lu_2025_moba.pdf" "https://arxiv.org/pdf/2502.13189"

echo "[8/25] Ye 2024 - Differential Transformer"
curl -sL -o "ye_2024_difftransformer.pdf" "https://arxiv.org/pdf/2410.05258"

echo "[9/25] Lv 2024 - CogAttention"
curl -sL -o "lv_2024_cogattention.pdf" "https://arxiv.org/pdf/2410.07105"

echo "[10/25] Ramapuram 2024 - Sigmoid Self-Attention"
curl -sL -o "ramapuram_2024_sigmoid.pdf" "https://arxiv.org/pdf/2409.04431"

echo "[11/25] Gu & Dao 2024 - Mamba"
curl -sL -o "gu_2024_mamba.pdf" "https://arxiv.org/pdf/2312.00752"

echo "[12/25] Peng 2023 - RWKV"
curl -sL -o "peng_2023_rwkv.pdf" "https://arxiv.org/pdf/2305.13048"

echo "[13/25] Yang 2024 - Gated Delta Networks"
curl -sL -o "yang_2024_gatedDelta.pdf" "https://arxiv.org/pdf/2412.06464"

echo "[14/25] Qiu 2025 - Gated Self Attention"
curl -sL -o "qiu_2025_gatedSelfAttn.pdf" "https://arxiv.org/pdf/2504.00622"

# --- 补充论文 ---
echo "[15/25] Shazeer 2019 - Multi-Query Attention (MQA)"
curl -sL -o "shazeer_2019_mqa.pdf" "https://arxiv.org/pdf/1911.02150"

echo "[16/25] Ainslie 2023 - Grouped Query Attention (GQA)"
curl -sL -o "ainslie_2023_gqa.pdf" "https://arxiv.org/pdf/2305.13245"

echo "[17/25] DeepSeek-AI 2024 - DeepSeek-V2 (MLA)"
curl -sL -o "deepseek_2024_mla.pdf" "https://arxiv.org/pdf/2405.04434"

echo "[18/25] Dao 2022 - FlashAttention"
curl -sL -o "dao_2022_flashattention.pdf" "https://arxiv.org/pdf/2205.14135"

echo "[19/25] Kwon 2023 - PagedAttention (vLLM)"
curl -sL -o "kwon_2023_pagedattention.pdf" "https://arxiv.org/pdf/2309.06180"

echo "[20/25] Dao & Gu 2024 - Mamba-2 (SSD)"
curl -sL -o "dao_2024_mamba2.pdf" "https://arxiv.org/pdf/2405.21060"

echo "[21/25] Peng 2024 - RWKV v5/v6 (Eagle & Finch)"
curl -sL -o "peng_2024_rwkv56.pdf" "https://arxiv.org/pdf/2404.05892"

echo "[22/25] Peng 2025 - RWKV-7 (Goose)"
curl -sL -o "peng_2025_rwkv7.pdf" "https://arxiv.org/pdf/2503.14456"

echo "[23/25] Sun 2023 - RetNet"
curl -sL -o "sun_2023_retnet.pdf" "https://arxiv.org/pdf/2307.08621"

echo "[24/25] Lieber 2024 - Jamba"
curl -sL -o "lieber_2024_jamba.pdf" "https://arxiv.org/pdf/2403.19887"

echo "[25/25] Yang 2024 - GLA (Gated Linear Attention)"
curl -sL -o "yang_2024_gla.pdf" "https://arxiv.org/pdf/2312.06635"

# --- 额外补充 ---
echo "[Extra 1] Qin 2024 - HGRN2"
curl -sL -o "qin_2024_hgrn2.pdf" "https://arxiv.org/pdf/2404.07904"

echo "[Extra 2] Arora 2024 - Based"
curl -sL -o "arora_2024_based.pdf" "https://arxiv.org/pdf/2402.18668"

echo "[Extra 3] Qin 2024 - Lightning Attention-2"
curl -sL -o "qin_2024_lightning2.pdf" "https://arxiv.org/pdf/2401.04658"

echo "[Extra 4] Yang 2024 - DeltaNet"
curl -sL -o "yang_2024_deltanet.pdf" "https://arxiv.org/pdf/2406.06484"

echo "[Extra 5] Jiang 2023 - Mistral 7B (Sliding Window Attention)"
curl -sL -o "jiang_2023_mistral.pdf" "https://arxiv.org/pdf/2310.06825"

echo "[Extra 6] Dao 2023 - FlashAttention-2"
curl -sL -o "dao_2023_flashattention2.pdf" "https://arxiv.org/pdf/2307.08691"

echo ""
echo "=== 下载完成！共 31 篇 ==="
ls -la *.pdf | wc -l
