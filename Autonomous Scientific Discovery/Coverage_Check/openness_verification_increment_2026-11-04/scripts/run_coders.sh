#!/usr/bin/env bash
# Resumable O/V/A coding run on H20: every batch coded independently by Claude Code (claude-sonnet-5-5,
# primary; prompt via stdin, which this gateway requires) and Codex (gpt-6.1-sol, second coder). A batch whose output already has one line per id
# is skipped, so the script can be re-run after an interruption.
#   bash run_coders.sh [parallel_jobs] [only_batch]      (run inside tmux; only_batch e.g. b01 for a smoke test)
set -u
W="$(cd "$(dirname "$0")" && pwd)"
P="${1:-8}"
ONLY="${2:-}"
mkdir -p "$W/full/codex" "$W/full/sonnet" "$W/logs"

prompt() {  # $1 batch, $2 coder folder
cat <<EOF
You are an independent coder for a literature-survey dataset. Work only inside $W/.

1. Read $W/CODER_BRIEF.md and $W/classification_protocol.md in full. They are the rules; the protocol's boundary lists are binding.
2. Code every paper id listed in $W/batches/$1.txt. For each id, read $W/packets/<paper_id>.txt.
3. Write one JSON object per paper, exactly as the brief specifies, to $W/full/$2/$1.jsonl. The file must end with exactly one line per id in the batch file.

Do not read any other coder's output (nothing under $W/full/ except your own file). Do not modify any other file. Every quote must be copied verbatim from the cited packet line, without the "L<n>: " prefix.
When done, print one line: "$1 $2: coded N, low confidence M".
EOF
}

job() {  # $1 batch, $2 coder
  local b="$1" c="$2" out="$W/full/$2/$1.jsonl" want rc=0
  want=$(grep -c . "$W/batches/$b.txt")
  if [ -f "$out" ] && [ "$(grep -c . "$out")" -eq "$want" ]; then echo "skip $b $c"; return 0; fi
  rm -f "$out"
  if [ "$c" = codex ]; then
    timeout 3600 codex exec --skip-git-repo-check -C "$W" --sandbox danger-full-access \
      -c model_reasoning_effort='"high"' "$(prompt "$b" codex)" > "$W/logs/codex_$b.log" 2>&1
    rc=$?
  else
    ( cd "$W" && prompt "$b" sonnet | timeout 3600 claude -p --model claude-sonnet-5-5 \
      --permission-mode acceptEdits --allowedTools "Read" "Write" "Edit" "Glob" "Grep" ) > "$W/logs/sonnet_$b.log" 2>&1
    rc=$?
  fi
  local got=0; [ -f "$out" ] && got=$(grep -c . "$out")
  echo "$(date +%H:%M:%S) done $b $c: $got/$want lines (exit $rc)"
}
export -f job prompt
export W

for b in $(ls "$W/batches" | sed 's/\.txt$//'); do
  [ -n "$ONLY" ] && [ "$b" != "$ONLY" ] && continue
  echo "$b codex"; echo "$b sonnet"
done \
  | xargs -P "$P" -L 1 bash -c 'job "$0" "$1"' | tee -a "$W/logs/run.log"
echo "ALL JOBS FINISHED $(date +%H:%M:%S)" | tee -a "$W/logs/run.log"
