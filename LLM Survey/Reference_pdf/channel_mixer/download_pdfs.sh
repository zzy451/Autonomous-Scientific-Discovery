#!/bin/bash
# Channel Mixer 论文 PDF 下载脚本
# 使用方法: cd "/Users/mjm/LLM Survey/Reference_pdf/channel_mixer" && bash download_pdfs.sh

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "=== 开始下载 Channel Mixer 论文 PDF ==="

# 1. Jacobs 1991 - Adaptive Mixtures of Local Experts (原始 MoE)
curl -sL -o "Jacobs_1991_AdaptiveMoE.pdf" "https://www.cs.toronto.edu/~hinton/absps/jjnh91.pdf" && echo "[OK] Jacobs_1991" || echo "[FAIL] Jacobs_1991"

# 2. Dauphin 2017 - Language Modeling with Gated Convolutional Networks (GLU)
curl -sL -o "Dauphin_2017_GLU.pdf" "https://arxiv.org/pdf/1612.08083" && echo "[OK] Dauphin_2017" || echo "[FAIL] Dauphin_2017"

# 3. Shazeer 2017 - Outrageously Large Neural Networks: Sparsely-Gated MoE
curl -sL -o "Shazeer_2017_SparseMoE.pdf" "https://arxiv.org/pdf/1701.06538" && echo "[OK] Shazeer_2017" || echo "[FAIL] Shazeer_2017"

# 4. Ramachandran 2017 - Searching for Activation Functions (Swish)
curl -sL -o "Ramachandran_2017_Swish.pdf" "https://arxiv.org/pdf/1710.05941" && echo "[OK] Ramachandran_2017" || echo "[FAIL] Ramachandran_2017"

# 5. Lepikhin 2021 - GShard
curl -sL -o "Lepikhin_2021_GShard.pdf" "https://arxiv.org/pdf/2006.16668" && echo "[OK] Lepikhin_2021" || echo "[FAIL] Lepikhin_2021"

# 6. Fedus 2022 - Switch Transformers
curl -sL -o "Fedus_2022_SwitchTransformer.pdf" "https://arxiv.org/pdf/2101.03961" && echo "[OK] Fedus_2022" || echo "[FAIL] Fedus_2022"

# 7. Zoph 2022 - ST-MoE
curl -sL -o "Zoph_2022_STMoE.pdf" "https://arxiv.org/pdf/2202.08906" && echo "[OK] Zoph_2022" || echo "[FAIL] Zoph_2022"

# 8. Zhou 2022 - Expert Choice Routing
curl -sL -o "Zhou_2022_ExpertChoice.pdf" "https://arxiv.org/pdf/2202.09368" && echo "[OK] Zhou_2022" || echo "[FAIL] Zhou_2022"

# 9. Jiang 2024 - Mixtral of Experts
curl -sL -o "Jiang_2024_Mixtral.pdf" "https://arxiv.org/pdf/2401.04088" && echo "[OK] Jiang_2024" || echo "[FAIL] Jiang_2024"

# 10. Dai 2024 - DeepSeekMoE
curl -sL -o "Dai_2024_DeepSeekMoE.pdf" "https://arxiv.org/pdf/2401.06066" && echo "[OK] Dai_2024" || echo "[FAIL] Dai_2024"

# 11. DeepSeek-AI 2024 - DeepSeek-V2
curl -sL -o "DeepSeekAI_2024_DeepSeekV2.pdf" "https://arxiv.org/pdf/2405.04434" && echo "[OK] DeepSeekAI_2024_V2" || echo "[FAIL] DeepSeekAI_2024_V2"

# 12. Wang 2024 - Auxiliary-Loss-Free Load Balancing
curl -sL -o "Wang_2024_AuxLossFree.pdf" "https://arxiv.org/pdf/2408.15664" && echo "[OK] Wang_2024" || echo "[FAIL] Wang_2024"

# 13. Wei 2024 - Skywork-MoE
curl -sL -o "Wei_2024_SkyworkMoE.pdf" "https://arxiv.org/pdf/2406.06563" && echo "[OK] Wei_2024" || echo "[FAIL] Wei_2024"

# 14. Muennighoff 2024 - OLMoE
curl -sL -o "Muennighoff_2024_OLMoE.pdf" "https://arxiv.org/pdf/2409.02060" && echo "[OK] Muennighoff_2024" || echo "[FAIL] Muennighoff_2024"

# 15. Databricks 2024 - DBRX
curl -sL -o "Databricks_2024_DBRX.pdf" "https://arxiv.org/pdf/2404.14219" && echo "[OK] Databricks_2024" || echo "[FAIL] Databricks_2024"

# 16. Lieber 2024 - Jamba (Hybrid Transformer-Mamba-MoE)
curl -sL -o "Lieber_2024_Jamba.pdf" "https://arxiv.org/pdf/2403.19887" && echo "[OK] Lieber_2024" || echo "[FAIL] Lieber_2024"

# 17. Raposo 2024 - Mixture-of-Depths
curl -sL -o "Raposo_2024_MoD.pdf" "https://arxiv.org/pdf/2404.02258" && echo "[OK] Raposo_2024" || echo "[FAIL] Raposo_2024"

# 18. Qwen Team 2024 - Qwen2 MoE (如有独立 tech report)
curl -sL -o "Qwen_2024_Qwen2MoE.pdf" "https://arxiv.org/pdf/2407.10671" && echo "[OK] Qwen_2024" || echo "[FAIL] Qwen_2024"

echo ""
echo "=== 下载完成 ==="
echo "共 18 篇论文。请检查上方输出确认各文件是否下载成功。"
