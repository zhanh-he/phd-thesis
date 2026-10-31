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
const report={edition:'jointly-reviewed-v5, author choice pending',tests:[],screenshots:[]};
const test=(name,ok)=>{assert(ok,name);report.tests.push({name,passed:true});};
const url=pathToFileURL(path.join(dir,'index.html')).href;
await client.send('Page.enable');await client.send('Runtime.enable');await client.send('Network.enable');
await client.send('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
await client.loaded(url);
test('Final page is exact jointly-reviewed proposal, not author-approved',await client.eval(`packet.packetStatus==='jointly-reviewed-v5'&&!packet.reviewAgreement.parentEvaluatorPending&&!packet.reviewAgreement.externalCycle2Pending&&document.title.includes('v5 最新提案')`));
test('Six priority cards and folded fifteen-item source index',await client.eval(`document.querySelectorAll('[data-card]').length===6&&document.querySelectorAll('#overview a').length===15&&!document.querySelector('#overview details').open`));
test('First screen omits internal acceptance/pending jargon',await client.eval(`!/(接受可选精简|接受实质合并|待.?cycle2|cycle2.?待|待第二次外部|返修推荐|接受返修)/i.test(document.body.innerText)`));
test('Main entry distinguishes latest v5, v4 references and unedited thesis',await client.eval(`document.getElementById('version').textContent.includes('v5')&&document.getElementById('version').textContent.includes('v4')&&document.getElementById('version').textContent.includes('正文未改')`));
test('Huber exact approved sentence',await client.eval(`document.getElementById('new-text').textContent.endsWith('We have not established an advantage over MAE.')&&!document.getElementById('new-text').textContent.includes('through a dedicated comparison')`));
test('Stable v5-T11 reply identity visible; ledger is historical only',await client.eval(`document.querySelector('.meta').textContent.includes('v5-T11')&&document.querySelector('.read-only').textContent.includes('v5-T11')&&document.querySelector('.decision-link').textContent.includes('历史参考')`));
await client.shot('final-desktop.png');report.screenshots.push('final-desktop.png');
const ids=await client.eval('packet.cards.map(c=>c.id)');
for(const id of ids){
 await client.eval(`navigate(${JSON.stringify(id)},false)`);
 const opts=await client.eval(`packet.cards.find(c=>c.id===${JSON.stringify(id)}).options.map(o=>o.id)`);
 for(let round=0;round<3;round++)for(const opt of opts){
  test(`${id}/${opt} exact passage after toggle ${round+1}`,await client.eval(`(()=>{const s=document.getElementById('variant');s.value=${JSON.stringify(opt)};s.dispatchEvent(new Event('change'));const c=packet.cards.find(c=>c.id===${JSON.stringify(id)}),o=c.options.find(o=>o.id===${JSON.stringify(opt)});return document.getElementById('old-text').textContent===(o.originalFocus??c.originalFocus)&&document.getElementById('new-text').textContent===(o.kind==='keep'?(o.originalFocus??c.originalFocus):o.focusText)&&document.activeElement.id==='variant'})()`));
 }
 test(id+' file-only references',await client.eval(`[...document.querySelectorAll('#card a')].every(a=>a.protocol==='file:')`));
}
for(const id of ['T11','N01','T03','T01','N05a']){
 await client.eval(`navigate(${JSON.stringify(id)},false);choices.delete(${JSON.stringify(id)});renderCard();document.getElementById('assembled-context').open=true`);
 test(id+' exact final context',await client.eval(`document.querySelector('.context-view').textContent===packet.cards.find(c=>c.id===${JSON.stringify(id)}).contextPreview`));
 test(id+' context does not imply other proposals approved',await client.eval(`document.getElementById('assembled-context').textContent.includes('均未实施，本卡 KEEP 不改变其他提案')`));
}
await client.eval(`navigate('T03',false);choices.delete('T03');renderCard()`);await client.shot('final-piano-roll.png');report.screenshots.push('final-piano-roll.png');
await client.eval(`navigate('T01',false);choices.delete('T01');renderCard();document.getElementById('full-context').open=true`);
test('Insertion retains original question and inserts exact candidate',await client.eval(String.raw`(()=>{const c=packet.cards.find(c=>c.id==='T01'),o=c.options.find(o=>o.id===c.recommended);return c.operation==='insertion'&&document.querySelector('.full-pair>div:last-child pre').textContent===c.originalFull+'\n\n'+o.fullText})()`));
await client.eval(`document.getElementById('assembled-context').open=true;document.querySelector('.context-v4').scrollIntoView({block:'center'})`);
await client.shot('final-context.png');report.screenshots.push('final-context.png');
test('Inherited v4 is visibly separate',await client.eval(`document.querySelectorAll('#assembled-context .context-v4').length===2&&document.getElementById('assembled-context').textContent.includes('原样沿用')`));
await client.eval(`navigate('N01',false);choices.delete('N01');renderCard();window.scrollTo(0,0)`);
await client.shot('final-metrics.png');report.screenshots.push('final-metrics.png');
await client.eval(`document.getElementById('full-context').open=true`);
test('N01 five-range scope and corrected table row',await client.eval(String.raw`document.querySelectorAll('.follow').length===2&&document.querySelector('.scope').textContent.includes('五')&&(()=>{const c=packet.cards.find(c=>c.id==='N01'),f=c.followthrough.find(f=>f.proposalId==='N07');return f.new.includes('\\textbf{$\\Delta$ (GT $-$ Flat)}')&&!f.new.includes('\\textbf{$\\Delta$ (GT $-$ Flat) $\\uparrow$}')})()`));
await client.eval(`document.getElementById('view-keep').click()`);
test('N01 KEEP retains entire five-range group',await client.eval(`document.querySelector('.scope').textContent.includes('N07')&&document.querySelector('.scope').textContent.includes('Ch2 N04')&&document.querySelector('.scope').textContent.includes('现有三段')`));
await client.eval(`navigate('N05a',false);choices.delete('N05a');renderCard();window.scrollTo(0,0)`);
test('N05a visually retains original boundaries sentence',await client.eval(`document.getElementById('new-text').textContent==='The thesis has several boundaries.'&&![...document.querySelectorAll('#old-text del')].some(n=>n.textContent.includes('The thesis has several boundaries.'))`));
await client.shot('final-defensive-prose.png');report.screenshots.push('final-defensive-prose.png');
await client.eval(`document.getElementById('view-keep').click();document.getElementById('full-context').open=true`);
test('N05b/c stay independently identified while a is KEEP',await client.eval(`document.querySelectorAll('#optional-passages .follow').length===2&&document.getElementById('optional-passages').textContent.includes('v5-N05b')&&document.getElementById('optional-passages').textContent.includes('v5-N05c')&&document.getElementById('optional-passages').textContent.includes('不随本卡自动采用')`));
test('KEEP does not falsely recompute fixed final context',await client.eval(`!document.getElementById('assembled-context')&&document.querySelector('.focus-note').textContent.includes('固定')`));
await client.eval(`document.getElementById('synchronization').querySelector('details').open=true`);
test('Corrected roadmap has fresh v5 identity, no old-approval inheritance',await client.eval(`(()=>{const d=packet.synchronization.find(d=>d.displayId==='v5-ROADMAP');return d&&d.old.startsWith('Supported by listening tests, it demonstrates')&&d.new.startsWith('It shows that')&&d.responseInstruction.includes('旧 YES 不适用')&&!d.legacyReference})()`));
test('Exactly22 dependencies are unchanged-v4, corrected one is new-v5',await client.eval(`packet.retainedV4DependencyCount===22&&packet.correctedDependencyIds.length===1&&packet.correctedDependencyIds[0]==='V4-R2-04-sync-3'`));
await client.eval(`document.getElementById('reset').click();document.getElementById('search').value='v5-T11';document.getElementById('search').dispatchEvent(new Event('input'))`);
test('Stable visible ID search works',await client.eval(`document.querySelectorAll('[data-card]').length===1&&activeId==='T11'`));
await client.eval(`document.getElementById('search').value='v5-N05b';document.getElementById('search').dispatchEvent(new Event('input'))`);
test('Independent subrange search works',await client.eval(`activeId==='N05a'&&document.querySelectorAll('[data-card]').length===1`));
await client.eval(`document.getElementById('search').value='v5-ROADMAP';document.getElementById('search').dispatchEvent(new Event('input'))`);
test('Corrected roadmap ID search reveals exact new scope',await client.eval(`document.getElementById('card').textContent.includes('v5-ROADMAP')&&document.getElementById('card').textContent.includes('Supported by listening tests, it demonstrates')&&document.getElementById('card').textContent.includes('旧 YES 不适用')&&!document.querySelector('.empty')`));
await client.eval(`document.getElementById('search').value='no-such-thesis-text';document.getElementById('search').dispatchEvent(new Event('input'))`);
test('Empty search has recovery instruction',await client.eval(`document.querySelector('.empty').textContent.includes('重置查看')`));
await client.eval(`document.getElementById('reset').click()`);
const key=async(k,code)=>{const v=k==='Enter'?13:9,n=k==='Enter'?36:48;await client.send('Input.dispatchKeyEvent',{type:'keyDown',key:k,code,windowsVirtualKeyCode:v,nativeVirtualKeyCode:n,...(k==='Enter'?{text:'\r',unmodifiedText:'\r'}:{})});await client.send('Input.dispatchKeyEvent',{type:'keyUp',key:k,code,windowsVirtualKeyCode:v,nativeVirtualKeyCode:n});};
await key('Tab','Tab');test('Keyboard Tab reaches filter',await client.eval(`document.activeElement.id==='filter'`));
await key('Tab','Tab');await key('Enter','Enter');test('Keyboard card navigation focuses visible title',await client.eval(`document.activeElement.id==='card-title'&&document.getElementById('card-title').getBoundingClientRect().top>=-2`));
await client.eval(`document.getElementById('view-keep').focus()`);await key('Enter','Enter');test('Keyboard KEEP is view-only',await client.eval(`document.getElementById('variant').value==='KEEP'&&document.activeElement.id==='view-keep'`));
await client.eval(`document.querySelector('#evidence summary').focus()`);await key('Enter','Enter');test('Evidence keyboard disclosure',await client.eval(`document.getElementById('evidence').open`));
await client.eval(`document.getElementById('reset').click()`);
for(const mode of ['proposed','original','compare']){await client.eval(`document.getElementById('mode').value='${mode}';document.getElementById('mode').dispatchEvent(new Event('change'))`);test('View mode '+mode,await client.eval(`document.getElementById('comparison').dataset.mode==='${mode}'`));}
await client.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:false});
for(const id of ids){await client.eval(`navigate(${JSON.stringify(id)},false)`);test(id+'390px no horizontal overflow',await client.eval(`document.documentElement.scrollWidth<=innerWidth`));}
await client.eval(`document.getElementById('reset').click();document.activeElement.blur();window.scrollTo(0,0)`);test('Reset closes global disclosures',await client.eval(`![...document.querySelectorAll('#synchronization details,#overview details,#remaining-materials details')].some(d=>d.open)`));test('Narrow uses compact passage picker',await client.eval(`getComputedStyle(document.querySelector('.mobile-picker')).display==='block'&&getComputedStyle(document.getElementById('card-list')).display==='none'`));await client.shot('final-narrow-top.png');report.screenshots.push('final-narrow-top.png');
await client.eval(`document.querySelector('.comparison').scrollIntoView({block:'start'})`);await client.shot('final-narrow-text.png');report.screenshots.push('final-narrow-text.png');
await client.eval(`document.getElementById('view-keep').click()`);
const fresh=await(await fetch(`http://127.0.0.1:${port}/json/new?about:blank`,{method:'PUT'})).json();const second=new CDP(fresh.webSocketDebuggerUrl);await second.send('Page.enable');await second.send('Runtime.enable');await second.loaded(url);
test('Second tab has independent default, no shared author state',await second.eval(`document.getElementById('variant').value===packet.cards[0].recommended&&document.getElementById('search').value===''`));await second.send('Page.close');second.close();
await client.loaded(url);test('Reload restores view defaults',await client.eval(`document.getElementById('variant').value===packet.cards[0].recommended&&document.getElementById('search').value===''`));
const crypto=await import('node:crypto');const hash=name=>crypto.createHash('sha256').update(fs.readFileSync(path.join(dir,name))).digest('hex');
for(const [file,record] of [['legacy_v3_v4.html','legacy_build_validation.json'],['provisional.html','provisional_build_validation.json'],['provisional_r2.html','provisional_r2_build_validation.json']])test(file+' archived unchanged',hash(file)===JSON.parse(fs.readFileSync(path.join(dir,'evidence',record),'utf8')).htmlSha256);
report.runtimeErrors=client.events.filter(e=>e.method==='Runtime.exceptionThrown');report.externalRequests=client.events.filter(e=>e.method==='Network.requestWillBeSent'&&!e.params.request.url.startsWith('file:')).map(e=>e.params.request.url);
test('No runtime errors',report.runtimeErrors.length===0);test('No external content calls',report.externalRequests.length===0);
test('No persistent choice state, fetch or forms',!/(?:localStorage|sessionStorage|indexedDB|fetch\(|XMLHttpRequest|<form\b)/.test(fs.readFileSync(path.join(dir,'index.html'),'utf8')));
fs.writeFileSync(path.join(dir,'evidence/final_browser_validation.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:report.tests.length,errors:report.runtimeErrors.length,external:report.externalRequests.length,screenshots:report.screenshots}));client.close();
