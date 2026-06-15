#!/bin/bash
# ============================================================
# 一键编译 LLM Architecture Survey
# 用法: cd paper && bash build.sh
#       或: chmod +x build.sh && ./build.sh
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================="
echo "  LLM Architecture Survey — 一键编译"
echo "=========================================="

# ---------- 检测编译器 ----------
if command -v tectonic &>/dev/null; then
    COMPILER="tectonic"
elif command -v pdflatex &>/dev/null; then
    COMPILER="pdflatex"
elif command -v xelatex &>/dev/null; then
    COMPILER="xelatex"
else
    echo "❌ 未找到 LaTeX 编译器 (tectonic / pdflatex / xelatex)"
    echo "   推荐安装: brew install tectonic"
    exit 1
fi

echo "📦 使用编译器: $COMPILER"
echo ""

# ---------- 编译 ----------
if [ "$COMPILER" = "tectonic" ]; then
    # tectonic 自动处理多次编译和 bibtex
    echo "🔨 编译 main.tex ..."
    tectonic main.tex 2>&1 | grep -E "^(error|note: Writing)" || true

else
    # pdflatex / xelatex 需要手动多次编译
    echo "🔨 第 1 次编译 ..."
    $COMPILER -interaction=nonstopmode main.tex > /dev/null 2>&1

    echo "📚 运行 BibTeX ..."
    bibtex main > /dev/null 2>&1 || true

    echo "🔨 第 2 次编译 ..."
    $COMPILER -interaction=nonstopmode main.tex > /dev/null 2>&1

    echo "🔨 第 3 次编译 ..."
    $COMPILER -interaction=nonstopmode main.tex > /dev/null 2>&1
fi

# ---------- 检查结果 ----------
if [ -f main.pdf ]; then
    SIZE=$(du -h main.pdf | cut -f1)
    echo ""
    echo "✅ 编译成功！"
    echo "   📄 main.pdf ($SIZE)"
    echo "   📂 $(pwd)/main.pdf"

    # macOS 自动打开
    if [ "$(uname)" = "Darwin" ]; then
        echo ""
        read -p "🔍 是否打开 PDF? [Y/n] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Nn]$ ]]; then
            open main.pdf
        fi
    fi
else
    echo ""
    echo "❌ 编译失败，未生成 main.pdf"
    echo "   请检查上方错误信息"
    exit 1
fi
