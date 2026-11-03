"""Usage: python -X utf8 read_packets.py A 0 15 (zero-based slice)."""
import json
import sys
from pathlib import Path
out=Path(__file__).resolve().parent
batch,start,count=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
rows=[json.loads(s) for s in (out/'inputs'/f'batch_{batch}.jsonl').read_text(encoding='utf-8').splitlines()]
for r in rows[start:start+count]:
    print(f"\n{r['paper_id']} | {r['title']} | {r['year']}")
    print('Old:',r['legacy_agent_type'],'| Note:',r['note_path'])
    for e in r['evidence_lines']:print(f"L{e['line']}: {e['text']}")
