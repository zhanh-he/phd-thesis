from pathlib import Path
import json, hashlib, re, subprocess
from urllib.parse import unquote

ROOT = Path('/Users/jollibear/Documents/PhD_Thesis_Source_20261022')
DETAIL = ROOT / '02_Ultra_细节'
AUDIT = DETAIL / '审计记录'
initial = json.loads((AUDIT / '本轮初始文件清单.json').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
allowed_changed = {'02_Ultra_细节/给导读的更新建议.md'}
checks = []
original_changes = []
for item in initial:
    p = ROOT / item['file']
    same = p.is_file() and sha(p) == item['sha256']
    if not same:
        original_changes.append(item['file'])
    checks.append({'file': item['file'], 'unchanged': same, 'permitted_update': item['file'] in allowed_changed})
unexpected = sorted(set(original_changes) - allowed_changed)
backup = AUDIT / '给导读的更新建议_原模板_20261022.md'
old = next(x['sha256'] for x in initial if x['file'] == '02_Ultra_细节/给导读的更新建议.md')
backup_ok = backup.is_file() and sha(backup) == old
tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
tracked = [x for x in tracked if x]
tracked_diff = subprocess.check_output(['git', 'diff', 'HEAD', '--name-only'], cwd=ROOT).decode().splitlines()
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip()
required = ['本轮结果_README.md','答辩详细准备.md','全部评审意见与回应.md','论文修改方案与英文替换稿.md','关键核查与证据.md','给导读的更新建议.md']
missing = [x for x in required if not (DETAIL / x).is_file()]
body = (DETAIL / '全部评审意见与回应.md').read_text()
ids = re.findall(r'^### (R[12]-\d{2})\b', body, re.M)
expected = [f'R1-{i:02}' for i in range(1,39)] + [f'R2-{i:02}' for i in range(1,6)]
ids_ok = len(ids) == 43 and len(set(ids)) == 43 and set(ids) == set(expected)
fields = ['原意见定位与性质','真实关切','现有证据','建议英文 response','修改位置与行动','优先级／状态']
blocks = re.split(r'^### R[12]-\d{2}[^\n]*\n', body, flags=re.M)[1:]
field_missing = {ids[i]: [f for f in fields if f not in b] for i,b in enumerate(blocks) if any(f not in b for f in fields)}
bad_links = []
for name in required:
    p = DETAIL / name
    if not p.exists(): continue
    text = p.read_text()
    for target in re.findall(r'\]\(([^)]+)\)', text):
        raw = target.strip().strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', raw) and not raw.startswith('/'):
            continue
        raw = unquote(raw.split('#')[0])
        raw = re.sub(r':\d+$', '', raw)
        if not raw: continue
        q = Path(raw) if raw.startswith('/') else p.parent / raw
        if not q.exists(): bad_links.append({'file': name, 'target': target})
files = [{'file': str(p.relative_to(DETAIL)), 'bytes': p.stat().st_size, 'sha256': sha(p)} for p in DETAIL.rglob('*') if p.is_file() and 'blueprint_snapshot' not in p.parts and p.name not in ['本轮验收.json','本轮验收.md']]
result = {'head': head, 'baseline_matches': head == '7e319875a8b1e9fc8f6a0afa4dc4417b03212226', 'tracked_count': len(tracked), 'tracked_diff_vs_head': tracked_diff, 'original_file_changes': original_changes, 'unexpected_original_changes': unexpected, 'suggestion_template_preserved': backup_ok, 'required_missing': missing, 'review_ids_43_unique_complete': ids_ok, 'review_field_missing': field_missing, 'broken_local_links': bad_links, 'original_hash_checks': checks, 'current_deliverables': files}
result['passed'] = all([result['baseline_matches'], not tracked_diff, not unexpected, backup_ok, not missing, ids_ok, not field_missing, not bad_links])
(AUDIT / '本轮验收.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps({k: result[k] for k in ['passed','tracked_count','tracked_diff_vs_head','unexpected_original_changes','suggestion_template_preserved','required_missing','review_ids_43_unique_complete','review_field_missing','broken_local_links']}, ensure_ascii=False, indent=2))
if not result['passed']: raise SystemExit(1)
