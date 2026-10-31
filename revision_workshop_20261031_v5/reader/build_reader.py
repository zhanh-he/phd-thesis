#!/usr/bin/env python3
"""Validate and embed a comparison packet in one offline, read-only HTML file."""
import argparse, difflib, hashlib, html, json, re
from html.parser import HTMLParser
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def safe_path(s):
    p=(ROOT/s.split('#',1)[0]).resolve()
    if not p.is_relative_to(ROOT) or not p.is_file():raise ValueError('Missing/outside source: '+s)
    return p

def sentence_parts(s):
    # Whitespace remains attached, so removing markup restores the exact input.
    return re.findall(r'.+?(?:[.!?](?=\s|$)(?:\s+|$)|$)',s,re.S)
def diff(a,b):
    aa,bb=sentence_parts(a),sentence_parts(b)
    left=[];right=[]
    for op,i,j,k,l in difflib.SequenceMatcher(None,[x.rstrip()for x in aa],[x.rstrip()for x in bb],autojunk=False).get_opcodes():
        old=''.join(aa[i:j]);new=''.join(bb[k:l])
        if op=='equal':left.append(html.escape(old));right.append(html.escape(new))
        else:
            if old:left.append('<del>'+html.escape(old)+'</del>')
            if new:right.append('<ins>'+html.escape(new)+'</ins>')
    return ''.join(left),''.join(right)

class ContextChecker(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.parts=[];self.depth=0
    def handle_starttag(self,tag,attrs):
        if tag!='mark' or any(k not in ['class','title']for k,v in attrs) or dict(attrs).get('class') not in ['context-v4','context-v5']:raise ValueError('Unsafe context markup')
        self.depth+=1
    def handle_endtag(self,tag):
        if tag!='mark' or self.depth<1:raise ValueError('Unsafe context end tag')
        self.depth-=1
    def handle_data(self,data):self.parts.append(data)
    def handle_comment(self,data):raise ValueError('Unexpected context comment')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--packet',type=Path,default=HERE/'initial_packet.json');ap.add_argument('--output',type=Path,default=HERE/'index.html');ap.add_argument('--allow-provisional',action='store_true');args=ap.parse_args()
    out=args.output.resolve()
    if out.parent!=HERE:raise ValueError('Output must remain in reader/')
    packet=json.loads(args.packet.read_text())
    if packet.get('schemaVersion')!=1:raise ValueError('Unsupported packet schema')
    if packet.get('packetStatus')=='writer-provisional':
        if not args.allow_provisional or out.name=='index.html':raise ValueError('Provisional requires --allow-provisional and separate output; never replace index.html')
        if not packet.get('reviewAgreement',{}).get('parentEvaluatorPending'):raise ValueError('Provisional must preserve pending external review')
    elif packet.get('packetStatus') not in ['reviewed-legacy','jointly-reviewed-v5']:raise ValueError('Do not present unreviewed writing as ready')
    if packet['packetStatus']=='jointly-reviewed-v5' and (not packet.get('reviewAgreement') or packet['reviewAgreement'].get('parentEvaluatorPending')):
        raise ValueError('v5 needs writer/evaluator agreement and exact review references')
    checks=[];ids=set()
    for c in packet['cards']:
        if not re.fullmatch(r'[A-Za-z0-9._-]+',c['id']):raise ValueError('Unsafe card ID')
        if c['id'] in ids:raise ValueError('Duplicate card ID')
        if not isinstance(c['sourceLine'],int) or c['sourceLine']<1:raise ValueError('Source line must be positive integer')
        ids.add(c['id']);source=safe_path(c['sourceFile']);actual=source.read_text()
        exact=c.get('sourceExact',c['originalFull'])
        if exact not in actual:raise ValueError('Quote no longer matches source: '+c['id'])
        if c['originalFocus'] not in c['originalFull']:raise ValueError('Focus is not exact original text')
        if c.get('optionNotes') and not isinstance(c['optionNotes'],dict):raise ValueError('optionNotes must be a per-option dict; use provisional adapter')
        if not any(o['id']=='KEEP' and o['kind']=='keep' for o in c['options']):raise ValueError('KEEP must remain visible')
        if not any(o['id']==c['recommended'] for o in c['options']):raise ValueError('Missing recommended option')
        for field in ['decisionPath','reviewFile','candidateFile','commentFile','originalImage','recommendationSource']:
            if c.get(field):safe_path(c[field])
        for f in c.get('followthrough',[]):
            fp=safe_path(f['file'])
            if f['old'] not in fp.read_text():raise ValueError('Followthrough quote differs: '+c['id'])
        if c.get('contextHtml'):
            checker=ContextChecker();checker.feed(c['contextHtml']);checker.close()
            if checker.depth or ''.join(checker.parts)!=c['contextPreview']:raise ValueError('Context markup changes exact text')
            for dep in c.get('contextDependencyDetails',[]):
                if dep['old'] not in safe_path(dep['file']).read_text():raise ValueError('Context dependency source changed')
                safe_path(dep['legacyReference'])
        c['sourceSha256']=digest(source)
        for o in c['options']:
            if not re.fullmatch(r'[A-Za-z0-9._-]+',o['id']) or o['kind'] not in ['replacement','insertion','keep']:raise ValueError('Invalid option')
            orig=o.get('originalFocus',c['originalFocus'])
            if orig not in c['originalFull']:raise ValueError('Variant original focus must be exact')
            if ''.join(sentence_parts(orig))!=orig or ''.join(sentence_parts(o['focusText']))!=o['focusText']:raise ValueError('Sentence segmentation loses text')
            if o['focusText'] not in o['fullText']:raise ValueError('Focus is not exact candidate text')
            if o['kind']=='keep':o['oldHtml']=html.escape(orig);o['newHtml']=html.escape(orig)
            elif o['kind']=='insertion':o['oldHtml']=html.escape(orig);o['newHtml']='<ins>'+html.escape(o['focusText'])+'</ins>'
            else:o['oldHtml'],o['newHtml']=diff(orig,o['focusText'])
        checks.append({'id':c['id'],'source':c['sourceFile'],'sourceSha256':c['sourceSha256'],'quoteExact':True,'optionCount':len(c['options'])})
    for p in packet.get('provenance',[]):
        if digest(safe_path(p['path']))!=p['sha256']:raise ValueError('Reviewed input changed: '+p['path'])
    # Escape HTML/script delimiters even though rendering uses textContent.
    data=json.dumps(packet,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
    template=(HERE/'reader_template.html').read_text()
    if template.count('/*__PACKET__*/')!=1:raise ValueError('Template data marker missing')
    out.write_text(template.replace('/*__PACKET__*/',data))
    evidence={'packet':str(args.packet.resolve().relative_to(HERE)) if args.packet.resolve().is_relative_to(HERE) else args.packet.name,'packetSha256':digest(args.packet),'htmlSha256':digest(out),'cards':checks,'sourceWrites':False,'choicesSaved':False}
    (HERE/('evidence/build_validation.json' if out.name=='index.html' else f'evidence/{out.stem}_build_validation.json')).write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    print(f'Built {out.name}: {len(checks)} exact-source cards, {out.stat().st_size} bytes; no source/ledger writes')
if __name__=='__main__':main()
