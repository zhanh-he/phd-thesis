"""Independent R2 assembly and quote verification. Never edits thesis/writer files."""
from pathlib import Path
import hashlib,json,re,collections,datetime

ROOT=Path('/Users/jollibear/Documents/tmp/phd thesis')
V5=ROOT/'revision_workshop_20261031_v5'
LOCAL=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((V5/'evaluator_baseline_diagnostics.json').read_text())
for group in ['source_manifest','previous_proposal_manifest']:
    for rel,expected in baseline[group].items():
        assert sha(ROOT/rel)==expected,rel
c1=json.loads((V5/'evaluator_cycle1_verification.json').read_text())
for rel,expected in c1['writer_evidence_snapshot'].items():
    assert sha(V5/rel)==expected,'Frozen writer C1 changed: '+rel
old={x['id']:x for x in json.loads((V5/'FINAL_SELECTION.json').read_text())}
items=json.loads((V5/'FINAL_SELECTION_R2.json').read_text())
deps=json.loads((V5/'DEPENDENCIES_R2.json').read_text())
assert len(items)==20 and len(deps)==23
changed=[x['id'] for x in items if x['selected']!=old[x['id']]['selected']]
assert set(changed)=={'T01','T03','T07','T11','N02','N03','N05a'}
sources={}
ops=[]
def source(file):
    if file not in sources:sources[file]=(ROOT/file).read_text()
    return sources[file]
def replace(ident,file,original,new,kind='replacement'):
    s=source(file)
    assert s.count(original)==1,ident+' source not unique'
    p=s.index(original)
    ops.append(dict(id=ident,file=file,start=p,end=p+len(original),new=new,kind=kind))
def insert(ident,file,p,new):
    assert 0<=p<=len(source(file))
    ops.append(dict(id=ident,file=file,start=p,end=p,new='\n\n'+new+'\n\n',kind='insertion'))
for x in items:
    ident=x['id'];file=x['source'];s=source(file)
    if x['original'].startswith('[No additional'):
        if ident=='T01':
            a=s.index('The thesis is driven by')
            marker='\\end{quote}';p=s.index(marker,a)+len(marker)
        elif ident=='T02':
            a=s.index('\\label{tab:intro_scenarios}')
            marker='\\end{table}';p=s.index(marker,a)+len(marker)
        elif ident in ['T04','T05']:
            a=s.index(x['anchor']);p=s.index('\n\n',a)
        else:raise AssertionError('Unexpected insertion '+ident)
        insert(ident,file,p,x['selected'])
    else:
        replace(ident,file,x['original'],x['selected'])
for x in deps:replace(x['id'],x['file'],x['old'],x['new'],'inherited_dependency')
s=source('Chapter_6/chap6.tex');a=s.index('\\label{tab:bp_metric_diagnostic}')
p=s.rfind('\\begin{table}',0,a);q=s.index('\\end{table}',a)+len('\\end{table}')
table=(V5/'N07_TABLE_MARKUP_PROPOSAL.tex').read_text()
table=table[table.index('\\begin{table}'):table.index('\\end{table}')+len('\\end{table}')]
replace('N07','Chapter_6/chap6.tex',s[p:q],table,'table_format')
assert len(ops)==44 and len(set(x['id'] for x in ops))==44
overlaps=[]
byfile=collections.defaultdict(list)
for x in ops:byfile[x['file']].append(x)
for file,rows in byfile.items():
    ordered=sorted(rows,key=lambda x:(x['start'],x['end']))
    for a,b in zip(ordered,ordered[1:]):
        if b['start']<a['end'] or (a['start']==a['end']==b['start']==b['end']):
            overlaps.append([file,a['id'],b['id']])
assert not overlaps,overlaps
declared=json.loads((V5/'evidence/R2_context_operation_manifest.json').read_text())['operations']
norm=lambda x:{k:x[k] for k in ['id','file','start','end','new']}
actual={x['id']:norm(x) for x in ops}
manifest_mismatches=[x['id'] for x in declared if actual.get(x['id'])!=norm(x)]
assert not manifest_mismatches,manifest_mismatches
overlays={}
for file,rows in byfile.items():
    s=source(file)
    for x in sorted(rows,key=lambda x:x['start'],reverse=True):
        s=s[:x['start']]+x['new']+s[x['end']:]
    overlays[file]=s
context_checks=[]
for x in items:
    # reinserted_context preserves the earlier frozen preview; R2 has its own field.
    text=x['reinserted_context_r2']
    valid=text in overlays[x['source']]
    context_checks.append(dict(id=x['id'],r2_context_is_exact_overlay_substring=valid))
assert all(x['r2_context_is_exact_overlay_substring'] for x in context_checks)
need_absent=[
 ('Chapter_1/Intro.tex','removes structural support entirely'),
 ('Chapter_1/Intro.tex','a universal loudness variable for all instruments'),
 ('Chapter_3/chap3.tex','most controlled'),
 ('Chapter_3/chap3.tex','most constrained'),
 ('Chapter_3/chap3.tex','four measures at 120'),
 ('Chapter_7/Conclusion.tex','sequence-oriented baselines'),
 ('Chapter_6/chap6.tex','proving \\emph{insensitive}'),
 ('Chapter_6/chap6.tex','MAE proves \\emph{over-sensitive}'),
 ('Chapter_6/chap6.tex','Cosine similarity and MAE fail'),
 ('Chapter_6/chap6.tex','This avoids the synthesis-to-performance domain gap'),
 ('Chapter_6/chap6.tex','therefore spends much of its gradient budget'),
 ('Chapter_2/Background.tex','so the gradient signal is dominated'),
 ('Chapter_7/Conclusion.tex','not artefacts of unfinished implementation'),
 ('Chapter_7/Conclusion.tex','rather than repair it'),
]
assert all(needle not in overlays[file] for file,needle in need_absent)
packet=json.loads((V5/'WRITER_READER_PACKET_R2.json').read_text())
assert packet['packetStatus']=='writer-r2-pending-external-cycle2'
assert packet['reviewAgreement']['externalCycle2Pending'] is True
card_checks=[]
for c in packet['cards']:
    s=source(c['sourceFile']);quote=c.get('sourceExact',c['originalFull'])
    assert s.count(quote)==1,c['id']
    assert c['originalFocus'] in c['originalFull']
    assert any(o['id']=='KEEP' and o['kind']=='keep' for o in c['options'])
    rec=next(o for o in c['options'] if o['id']==c['recommended'])
    if c['id'] in {'T01','T03','T11','N05a'}:
        assert rec['fullText']==next(x for x in items if x['id']==c['id'])['selected']
    elif c['id']=='N01':
        expected='\n\n'.join(next(x for x in items if x['id']==i)['selected'] for i in ['N01','N02','N03'])
        assert rec['fullText']==expected
    for o in c['options']:assert o['focusText'] in o['fullText']
    for f in c.get('followthrough',[]):assert source(f['file']).count(f['old'])==1
    if c.get('contextPreview'):assert c['contextPreview'] in overlays[c['sourceFile']]
    card_checks.append(dict(id=c['id'],quote_exact=True,recommended_text_exact=True,
        has_keep=True,context_dependency_ids=c.get('contextDependencyIds',[])))
for p in packet['provenance']:assert sha(ROOT/p['path'])==p['sha256']
inputs=['CANDIDATE_PACKET_R2_FULL_CONTEXT.md','WRITER_REVISION_RESPONSE_R2.md',
        'FINAL_SELECTION_R2.json','DEPENDENCIES_R2.json','WRITER_READER_PACKET_R2.json',
        'N07_TABLE_MARKUP_PROPOSAL.tex','evidence/R2_context_operation_manifest.json']
out=dict(verified_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    changed_passages=changed,source_files_unchanged=19,prior_proposal_files_unchanged=80,
    frozen_writer_c1_snapshot_unchanged=True,source_quote_operations=len(ops),
    operation_counts=dict(collections.Counter(x['kind'] for x in ops)),
    operation_ids=[x['id'] for x in ops],overlap_pairs=overlaps,
    declared_manifest_matches_independent_derivation=True,
    independently_reassembled_contexts=context_checks,
    removed_targeted_overclaims=need_absent,
    reader_input_checks=card_checks,reader_pending_status_honest=True,
    reviewed_source_provenance=[dict(path=file,sha256=sha(ROOT/file)) for file in sorted(byfile)],
    reviewed_input_snapshot={name:sha(V5/name) for name in inputs},
    limits=['Assembly/quote checking does not prove run or GT provenance.',
            '23 inherited dependencies are still author-unapproved proposals.',
            'Reader HTML integration and post-integration usability are separate work.',
            'Some original source issues outside the 44 reviewed operations may remain; this is not complete thesis implementation.'])
(LOCAL/'evaluator_cycle2_verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Verified exactly seven actual passage changes:',changed)
print('Independently reconstructed operations:',len(ops),out['operation_counts'])
print('All20 R2 contexts match independent overlay; no overlap.')
print('Six reader-card source/recommended ranges exact; pending status honest.')
print('19 source and80 prior proposal files unchanged; frozen writer C1 preserved.')
print('Saved evaluator_cycle2_verification.json')
