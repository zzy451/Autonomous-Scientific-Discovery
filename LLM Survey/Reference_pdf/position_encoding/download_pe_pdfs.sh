#!/bin/bash
# 下载 Position Encoding 论文 PDF
# 用法: chmod +x download_pe_pdfs.sh && ./download_pe_pdfs.sh

OUT_DIR="/Users/mjm/LLM Survey/Reference_pdf/position_encoding"
mkdir -p "$OUT_DIR"

echo "=== 下载 Position Encoding 论文 PDF ==="

# 已有笔记但需要 PDF 的论文
curl -sL -o "$OUT_DIR/Vaswani2017_Attention.pdf" "https://arxiv.org/pdf/1706.03762" && echo "OK: Vaswani2017" || echo "FAIL: Vaswani2017"
curl -sL -o "$OUT_DIR/Shaw2018_RelativePE.pdf" "https://arxiv.org/pdf/1803.02155" && echo "OK: Shaw2018" || echo "FAIL: Shaw2018"
curl -sL -o "$OUT_DIR/Dai2019_TransformerXL.pdf" "https://arxiv.org/pdf/1901.02860" && echo "OK: Dai2019" || echo "FAIL: Dai2019"
curl -sL -o "$OUT_DIR/Raffel2020_T5.pdf" "https://arxiv.org/pdf/1910.10683" && echo "OK: Raffel2020" || echo "FAIL: Raffel2020"
curl -sL -o "$OUT_DIR/He2021_DeBERTa.pdf" "https://arxiv.org/pdf/2006.03654" && echo "OK: He2021" || echo "FAIL: He2021"
curl -sL -o "$OUT_DIR/Likhomanenko2021_CAPE.pdf" "https://arxiv.org/pdf/2106.03143" && echo "OK: Likhomanenko2021" || echo "FAIL: Likhomanenko2021"
curl -sL -o "$OUT_DIR/Chi2022_Kerple.pdf" "https://arxiv.org/pdf/2205.09921" && echo "OK: Chi2022" || echo "FAIL: Chi2022"
curl -sL -o "$OUT_DIR/Sun2023_XPOS.pdf" "https://arxiv.org/pdf/2212.10554" && echo "OK: Sun2023" || echo "FAIL: Sun2023"
curl -sL -o "$OUT_DIR/Ruoss2023_RandomizedPE.pdf" "https://arxiv.org/pdf/2305.16843" && echo "OK: Ruoss2023" || echo "FAIL: Ruoss2023"
curl -sL -o "$OUT_DIR/Chen2023_PositionInterpolation.pdf" "https://arxiv.org/pdf/2306.15595" && echo "OK: Chen2023" || echo "FAIL: Chen2023"
curl -sL -o "$OUT_DIR/Peng2023_YaRN.pdf" "https://arxiv.org/pdf/2309.00071" && echo "OK: Peng2023" || echo "FAIL: Peng2023"
curl -sL -o "$OUT_DIR/Li2023_FIRE.pdf" "https://arxiv.org/pdf/2310.04418" && echo "OK: Li2023" || echo "FAIL: Li2023"
curl -sL -o "$OUT_DIR/Ding2024_LongRoPE.pdf" "https://arxiv.org/pdf/2402.13753" && echo "OK: Ding2024" || echo "FAIL: Ding2024"

echo "=== 完成 ==="
echo "PDF 保存在: $OUT_DIR"
ls -la "$OUT_DIR"
