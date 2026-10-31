from pathlib import Path
import json,hashlib,runpy,contextlib,io,re
out=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):state=runpy.run_path(str(out/'check_final_reviewed.py'))
root=state['root'];v5=state['v5'];load=state['load'];byid=state['byid'];ops=state['ops'];table=state['table'];fd=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
actual=load(v5/'evidence/FINAL_OPERATION_MANIFEST_v5.json');delivery=load(v5/'FINAL_DELIVERY_MANIFEST_v5.json');reader=load(v5/'READER_PACKET_REVIEWED_v5.json');packet=(v5/'CANDIDATE_PACKET_FINAL_v5.md').read_text()
files=[{'path':name,'hash_bound_to_actual_bytes':(v5/name).exists() and fd(v5/name)==h} for name,h in delivery['files'].items()]
expectedreader='9496ad5ece7f51e5de642c59fe0d547503e6eb7c77eb2376e34b8bad2f3c4c17'
r={'actual_final_operations_exact_independent_reconstruction':actual['operations']==ops,'delivery_file_bindings':files,'reader_hash_matches_manifest_and_writer_message':fd(v5/'READER_PACKET_REVIEWED_v5.json')==delivery['readerPacketSha256']==expectedreader,'reader_card_ids':[c['id'] for c in reader['cards']],'reader_uses_final_selection_and_context_field':reader.get('contextField')=='reinserted_context_final' and 'FINAL_SELECTION_REVIEWED_v5.json' in reader.get('finalSelectionFile',''),'context_packet_contains_all_20_exact_final_contexts':all(x['reinserted_context_final'] in packet for x in byid.values()),'reader_bindings':[]}
for c in reader['cards']:
 id=c['id'];selected=next(o for o in c['options'] if o['id']==c['recommended'])
 if id in byid:
  expected='\n\n'.join(byid[k]['selected'] for k in ['N01','N02','N03']) if id=='N01' else byid[id]['selected']
  ok=selected['fullText']==expected and selected['focusText'] in selected['fullText'] and c['contextPreview']==byid[id]['reinserted_context_final']
 else:
  ok=id=='KEEP-FIG62' and c['recommended']=='KEEP' and selected['fullText'] in (root/c['sourceFile']).read_text()
 exact=c.get('sourceExact',c['originalFull']);sourceok=exact in (root/c['sourceFile']).read_text()
 followok=all(f['old'] in (root/f['file']).read_text() for f in c.get('followthrough',[]))
 r['reader_bindings'].append({'id':id,'recommended_text_and_context_exact':ok,'original_in_real_source':sourceok,'followthrough_originals_in_source':followok})
n=next(c for c in reader['cards'] if c['id']=='N01');f=n.get('followthrough',[])
r['metric_group_exact_five_ranges']=n['options'][0]['fullText']=='\n\n'.join(byid[k]['selected'] for k in ['N01','N02','N03']) and len(f)==2 and any(x['new']==table for x in f) and any(x['new']==byid['N04']['selected'] for x in f)
a=next(c for c in reader['cards'] if c['id']=='N05a');r['n05bc_independent_not_automatic']=not a.get('followthrough') and {x['id'] for x in a.get('independentOptionalPassages',[])}=={'N05b','N05c'}
r['approval_and_implementation_stay_false']=delivery.get('authorApproved') is False and delivery.get('implemented') is False and reader['reviewAgreement'].get('authorApproval') is False and reader['reviewAgreement'].get('sourceImplementation') is False
r['all_binding_checks_passed']=r['actual_final_operations_exact_independent_reconstruction'] and all(x['hash_bound_to_actual_bytes'] for x in files) and r['reader_hash_matches_manifest_and_writer_message'] and r['reader_uses_final_selection_and_context_field'] and r['context_packet_contains_all_20_exact_final_contexts'] and all(all(v for k,v in x.items() if k!='id') for x in r['reader_bindings']) and r['metric_group_exact_five_ranges'] and r['n05bc_independent_not_automatic'] and r['approval_and_implementation_stay_false'] and len(r['reader_card_ids'])==6
(out/'final_binding_results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in r.items() if k not in ['delivery_file_bindings','reader_bindings']},indent=2))
