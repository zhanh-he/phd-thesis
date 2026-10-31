import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import assert from 'node:assert/strict';
const dir=path.dirname(fileURLToPath(import.meta.url));
const port=process.env.READER_CDP_PORT||fs.readFileSync(path.join(dir,'evidence/browser-profile/DevToolsActivePort'),'utf8').split('\n')[0];
const tabs=await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const page=tabs.find(t=>t.type==='page'&&t.url.startsWith('file:'))||tabs.find(t=>t.type==='page');
class CDP{
 constructor(url){this.ws=new WebSocket(url);this.next=1;this.pending=new Map();this.events=[];this.ready=new Promise(r=>this.ws.addEventListener('open',r,{once:true}));this.ws.addEventListener('message',e=>{const x=JSON.parse(e.data);if(x.id){const p=this.pending.get(x.id);this.pending.delete(x.id);x.error?p.reject(Error(JSON.stringify(x.error))):p.resolve(x.result);}else this.events.push(x);});}
 async send(method,params={}){await this.ready;const id=this.next++;return new Promise((resolve,reject)=>{this.pending.set(id,{resolve,reject});this.ws.send(JSON.stringify({id,method,params}));});}
 async eval(expression){const r=await this.send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;}
 async loaded(url){const since=this.events.length;await this.send('Page.navigate',{url});for(let n=0;n<100;n++){if(this.events.slice(since).some(x=>x.method==='Page.loadEventFired'))return;await new Promise(r=>setTimeout(r,30));}throw Error('Load timeout');}
 async shot(name){const r=await this.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});fs.writeFileSync(path.join(dir,'evidence',name),Buffer.from(r.data,'base64'));}
 close(){this.ws.close();}
}

const client=new CDP(page.webSocketDebuggerUrl);
const report={edition:'writer-provisional; external evaluator pending',tests:[],screenshots:[]};
const test=(name,ok)=>{assert(ok,name);report.tests.push({name,passed:true});};
await client.send('Page.enable');await client.send('Runtime.enable');await client.send('Network.enable');
await client.send('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
await client.loaded(pathToFileURL(path.join(dir,'provisional_r2.html')).href);
test('Provisional status visible, not accepted review',await client.eval(`document.title.includes('待独立评审')&&document.getElementById('version').textContent.includes('第二轮复核尚未确认')&&packet.reviewAgreement.parentEvaluatorPending`));
test('Six priority cards; 15-item optional index collapsed',await client.eval(`document.querySelectorAll('[data-card]').length===6&&document.querySelectorAll('#overview a').length===15&&!document.querySelector('#overview details').open`));
test('No duplicated short/why lead',await client.eval(`!document.querySelector('.lead')`));
test('Historical author-choice link does not claim T11 approval row',await client.eval(`document.querySelector('.decision-link').textContent.includes('R1-34')&&document.querySelector('.decision-link').textContent.includes('历史参考')&&document.querySelector('.read-only').textContent.includes('v5-T11（R2／KEEP）')`));
await client.shot('r2-desktop.png');report.screenshots.push('r2-desktop.png');
const ids=await client.eval('packet.cards.map(c=>c.id)');
for(const id of ids){
 await client.eval(`navigate(${JSON.stringify(id)},false)`);
 const opts=await client.eval(`packet.cards.find(c=>c.id===${JSON.stringify(id)}).options.map(o=>o.id)`);
 for(let round=0;round<2;round++)for(const opt of opts){
  test(`${id}/${opt} exact original/candidate, toggle ${round+1}`,await client.eval(`(()=>{const s=document.getElementById('variant');s.value=${JSON.stringify(opt)};s.dispatchEvent(new Event('change'));const c=packet.cards.find(c=>c.id===${JSON.stringify(id)}),o=c.options.find(o=>o.id===${JSON.stringify(opt)});return document.getElementById('old-text').textContent===(o.originalFocus??c.originalFocus)&&document.getElementById('new-text').textContent===(o.kind==='keep'?c.originalFocus:o.focusText)})()`));
 }
 test(id+' historical approval warning stays visible',await client.eval(`document.querySelector('.variant-note')?.textContent.includes('尚未绑定')&&(document.querySelector('.read-only').textContent.includes('旧 YES 不转移')||packet.cards.find(c=>c.id===activeId).id==='KEEP-FIG62')`));
}
await client.eval(`navigate('N01',false);choices.delete('N01');renderCard();document.getElementById('full-context').open=true`);
test('N01 whole group exact sync ranges and five-range notice',await client.eval(`document.querySelectorAll('.follow').length===2&&document.querySelector('.scope').textContent.includes('五个范围')`));
await client.shot('r2-metric-group.png');report.screenshots.push('r2-metric-group.png');
await client.eval(`document.getElementById('view-keep').click()`);
test('N01 KEEP scope retains whole group',await client.eval(`document.querySelector('.scope').textContent.includes('N07')&&document.querySelector('.scope').textContent.includes('Ch2 N04')&&document.querySelector('.scope').textContent.includes('现有三段')`));
await client.eval(`navigate('N05a',false);document.getElementById('full-context').open=true`);
test('Optional b/c remain visible independent when a kept',await client.eval(`document.getElementById('variant').value==='KEEP'&&document.querySelectorAll('.follow').length===2&&document.getElementById('full-context').textContent.includes('每处独立审阅')`));
await client.eval(`navigate('T03',false);document.getElementById('variant').value='GRID';document.getElementById('variant').dispatchEvent(new Event('change'))`);
test('GRID has actual alternative source instead of selected-only file',await client.eval(`[...document.querySelectorAll('.source-links a')].some(a=>a.href.includes('CANDIDATE_PACKET_BLIND_C1.md')&&a.textContent.includes('GRID'))`));
await client.eval(`navigate('T01',false);document.getElementById('evidence').open=true`);
test('T01 shows actual examiner and authored reply',await client.eval(`document.getElementById('evidence').textContent.includes('Section 1.5: how do you define')&&document.getElementById('evidence').textContent.includes('Oops, Thanks')`));
await client.eval(`navigate('N01',false)`);
test('New editorial issue not labeled examiner quote',await client.eval(`document.querySelector('#evidence summary').textContent.includes('编辑发现')&&document.getElementById('evidence').textContent.includes('编辑发现摘要')`));
await client.eval(`document.getElementById('filter').value='pending';document.getElementById('filter').dispatchEvent(new Event('change'))`);
test('Workflow pending does not masquerade as scientific fact blocks',await client.eval(`document.querySelectorAll('[data-card]').length===0&&!!document.querySelector('.empty')`));
await client.eval(`document.getElementById('reset').click()`);
test('Reset restores six defaults',await client.eval(`document.querySelectorAll('[data-card]').length===6&&document.getElementById('variant').value==='R2'`));

await client.eval(`document.getElementById('reset').click()`);
test('Huber exact corrected sentence, no dedicated-comparison phrase in candidate',await client.eval(`document.getElementById('new-text').textContent.endsWith('We have not established an advantage over MAE.')&&!document.getElementById('new-text').textContent.includes('through a dedicated comparison')`));
test('Stable v5 identifier displayed',await client.eval(`document.querySelector('.meta').textContent.includes('v5-T11')`));
for(const id of ['T11','N01','T03','T01','N05a']){
 await client.eval(`navigate(${JSON.stringify(id)},false);choices.delete(${JSON.stringify(id)});renderCard();document.getElementById('assembled-context').open=true`);
 test(id+' exact reconstructed R2 context',await client.eval(`document.querySelector('.context-view').textContent===packet.cards.find(c=>c.id===${JSON.stringify(id)}).contextPreview`));
 test(id+' other unapproved proposal IDs explicitly listed',await client.eval(`document.getElementById('assembled-context').textContent.includes('均未实施，本卡 KEEP 不改变其他提案')`));
 if(id==='T01'||id==='T03')test(id+' retained v4 dependencies separately colored and labeled',await client.eval(`document.querySelectorAll('.context-v4').length>0&&document.getElementById('assembled-context').textContent.includes('不要求重复选择')`));
}
await client.eval(`navigate('T01',false);document.getElementById('assembled-context').open=true;document.querySelector('.context-v4').scrollIntoView({block:'center'})`);
await client.shot('r2-v4-context.png');report.screenshots.push('r2-v4-context.png');
await client.eval(`navigate('N05a',false);document.getElementById('full-context').open=true`);
test('N05a first sentence preserved as boundaries',await client.eval(`document.getElementById('new-text').textContent==='The thesis has several boundaries.'`));
test('N05 optional subranges have stable separate IDs',await client.eval(`document.getElementById('full-context').textContent.includes('v5-N05b')&&document.getElementById('full-context').textContent.includes('v5-N05c')`));
await client.eval(`document.getElementById('view-keep').click()`);
test('KEEP cannot masquerade as R2 assembled context',await client.eval(`!document.getElementById('assembled-context')&&document.querySelectorAll('.focus-note').length>0`));
const prev=JSON.parse(fs.readFileSync(path.join(dir,'evidence/provisional_build_validation.json'),'utf8'));
const crypto2=await import('node:crypto');
test('Previous provisional.html preserved',crypto2.createHash('sha256').update(fs.readFileSync(path.join(dir,'provisional.html'))).digest('hex')===prev.htmlSha256);


await client.eval(`document.getElementById('search').value='v5-T11';document.getElementById('search').dispatchEvent(new Event('input'))`);
test('Visible stable v5-T11 ID is searchable',await client.eval(`document.querySelectorAll('[data-card]').length===1&&document.querySelector('.meta').textContent.includes('v5-T11')`));
await client.eval(`document.getElementById('search').value='v5-N05b';document.getElementById('search').dispatchEvent(new Event('input'))`);
test('Independent v5-N05b ID finds its parent reading card',await client.eval(`document.querySelectorAll('[data-card]').length===1&&activeId==='N05a'`));
await client.eval(`document.getElementById('reset').click()`);
test('Writer response is not labeled independent review',await client.eval(`[...document.querySelectorAll('.source-links a')].some(a=>a.href.includes('WRITER_REVISION_RESPONSE_R2')&&a.textContent.includes('非评审结论'))`));
test('Real quote link uses correct legacy R1-34 identity',await client.eval(`[...document.querySelectorAll('.source-links a')].some(a=>a.href.includes('COMMENT_MAP.md#r1-34')&&a.textContent.includes('R1-34'))`));

await client.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:false});
for(const id of ids){await client.eval(`navigate(${JSON.stringify(id)},false)`);test(id+' at 390px no horizontal overflow',await client.eval(`document.documentElement.scrollWidth<=innerWidth`));}
await client.eval(`navigate('T11',false);document.querySelector('.comparison').scrollIntoView({block:'start'});document.activeElement.blur()`);
await client.shot('r2-narrow.png');report.screenshots.push('r2-narrow.png');
report.runtimeErrors=client.events.filter(x=>x.method==='Runtime.exceptionThrown');
report.externalRequests=client.events.filter(x=>x.method==='Network.requestWillBeSent'&&!x.params.request.url.startsWith('file:')).map(x=>x.params.request.url);
test('No runtime errors',report.runtimeErrors.length===0);test('No external requests',report.externalRequests.length===0);
const old=JSON.parse(fs.readFileSync(path.join(dir,'evidence/build_validation.json'),'utf8'));
const crypto=await import('node:crypto');
test('Legacy index.html not overwritten',crypto.createHash('sha256').update(fs.readFileSync(path.join(dir,'index.html'))).digest('hex')===old.htmlSha256);
fs.writeFileSync(path.join(dir,'evidence/r2_browser_validation.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:report.tests.length,screenshots:report.screenshots,externalRequests:report.externalRequests.length,runtimeErrors:report.runtimeErrors.length,externalReview:'pending'}));client.close();
