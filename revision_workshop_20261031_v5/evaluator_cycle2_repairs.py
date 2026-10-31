"""Prepare two evaluator-owned corrective proposals; never edit writer or thesis."""
from pathlib import Path
import copy,difflib,hashlib,json

ROOT=Path('/Users/jollibear/Documents/tmp/phd thesis')
V5=ROOT/'revision_workshop_20261031_v5'
LOCAL=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
verification=json.loads((LOCAL/'evaluator_cycle2_verification.json').read_text())
for rel,h in verification['reviewed_input_snapshot'].items():assert sha(V5/rel)==h
deps=json.loads((V5/'DEPENDENCIES_R2.json').read_text())
dep=next(x for x in deps if x['id']=='V4-R2-04-sync-3')
before=copy.deepcopy(dep)
dep['old']='Supported by listening tests, '+dep['old']
dep['new']='I'+dep['new'][1:]
dep['line']=(ROOT/dep['file']).read_text().split(dep['old'])[0].count('\n')+1
dep['origin']+='; evaluator external C2 repairs composed Supported repetition'
dep['status']='evaluator-corrected author-unapproved proposal; writer acknowledgement pending'
raw=(ROOT/dep['file']).read_text()
assert raw.count(dep['old'])==1
depsfile=LOCAL/'evaluator_cycle2_dependencies_corrected_proposal.json'
depsfile.write_text(json.dumps(deps,ensure_ascii=False,indent=2)+'\n')
table=(V5/'N07_TABLE_MARKUP_PROPOSAL.tex').read_text()
oldrow='\\textbf{$\\Delta$ (GT $-$ Flat) $\\uparrow$}'
newrow='\\textbf{$\\Delta$ (GT $-$ Flat)}'
assert table.count(oldrow)==1
table=table.replace(oldrow,newrow)
tablefile=LOCAL/'evaluator_cycle2_N07_corrected_proposal.tex'
tablefile.write_text(table)
ops=json.loads((V5/'evidence/R2_context_operation_manifest.json').read_text())['operations']
repaired=copy.deepcopy(ops)
for x in repaired:
    if x['id']==dep['id']:
        x['start']=raw.index(dep['old']);x['end']=x['start']+len(dep['old']);x['new']=dep['new']
    elif x['id']=='N07':
        x['new']=table[table.index('\\begin{table}'):table.index('\\end{table}')+len('\\end{table}')]
def assemble(rows):
    files={x['file'] for x in rows};out={}
    for file in files:
        edits=sorted([x for x in rows if x['file']==file],key=lambda x:(x['start'],x['end']))
        for a,b in zip(edits,edits[1:]):assert a['end']<=b['start']
        text=(ROOT/file).read_text()
        for x in reversed(edits):text=text[:x['start']]+x['new']+text[x['end']:]
        out[file]=text
    return out
old=assemble(ops);new=assemble(repaired)
assert len(repaired)==44
changes=[k for k in old if old[k]!=new[k]]
assert set(changes)=={'Chapter_1/Intro.tex','Chapter_6/chap6.tex'}
assert 'Supported by listening tests, it shows' not in new['Chapter_1/Intro.tex']
assert newrow in new['Chapter_6/chap6.tex']
numeric=lambda s:__import__('re').findall(r'[-+]?\d+(?:\.\d+)?',s)
assert numeric(old['Chapter_6/chap6.tex'])==numeric(new['Chapter_6/chap6.tex'])
patch=''.join(''.join(difflib.unified_diff(old[f].splitlines(True),new[f].splitlines(True),fromfile='R2-virtual-preview/'+f,tofile='evaluator-corrected-virtual-preview/'+f)) for f in sorted(changes))
(LOCAL/'evaluator_cycle2_two_repairs.diff').write_text(patch)
evidence={'corrected_operation_count':44,'overlaps':False,'only_changed_operation_ids':['V4-R2-04-sync-3','N07'],
 'corrected_dependency':dep,'previous_dependency':before,'old_table_row':oldrow,'new_table_row':newrow,
 'all_table_numbers_unchanged':True,'source_writes':False,'writer_writes':False,
 'corrected_proposal_files':{depsfile.name:sha(depsfile),tablefile.name:sha(tablefile)},
 'corrected_virtual_overlay_sha256':{f:hashlib.sha256(t.encode()).hexdigest() for f,t in new.items()},
 'status':'Exact corrective proposals reviewed by evaluator; writer agreement and final reader integration pending.'}
(LOCAL/'evaluator_cycle2_repair_verification.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
print('Prepared exact two-repair proposals; 44 non-overlapping virtual operations; all table numbers unchanged.')
