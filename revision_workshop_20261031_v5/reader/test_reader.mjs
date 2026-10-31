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
const client=new CDP(page.webSocketDebuggerUrl);const report={tool:'Installed Chrome headless CDP + Node built-ins; Python difflib source build',tests:[],screenshots:[],consoleErrors:[],networkRequests:[]};
const test=(name,result)=>{assert(result,name);report.tests.push({name,passed:true});};
await client.send('Page.enable');await client.send('Runtime.enable');await client.send('Network.enable');
const url=pathToFileURL(path.join(dir,'index.html')).href;
await client.send('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
await client.loaded(url);
test('Five selected cards, explicit legacy edition, default R1-15 A',await client.eval(`document.querySelectorAll('[data-card]').length===5&&document.getElementById('version').textContent.includes('旧轮')&&document.getElementById('variant').value==='A'`));
test('Desktop no horizontal overflow',await client.eval(`document.documentElement.scrollWidth<=innerWidth`));
await client.eval(`document.getElementById('search').blur()`);await client.shot('desktop-first.png');report.screenshots.push('desktop-first.png');
const ids=await client.eval('packet.cards.map(c=>c.id)');
for(const id of ids){
 await client.eval(`navigate(${JSON.stringify(id)},false)`);
 const opts=await client.eval(`packet.cards.find(c=>c.id===${JSON.stringify(id)}).options.map(o=>o.id)`);
 for(let round=0;round<3;round++)for(const opt of opts){
  const ok=await client.eval(`(()=>{const s=document.getElementById('variant');s.value=${JSON.stringify(opt)};s.dispatchEvent(new Event('change'));const c=packet.cards.find(c=>c.id===${JSON.stringify(id)}),o=c.options.find(o=>o.id===${JSON.stringify(opt)});return document.getElementById('old-text').textContent===(o.originalFocus??c.originalFocus)&&document.getElementById('new-text').textContent===(o.kind==='keep'?c.originalFocus:o.focusText)&&document.getElementById('variant').value===o.id&&document.activeElement.id==='variant'})()`);
  test(`${id} / ${opt} exact text after toggle ${round+1}`,ok);
 }
 if(id==='R1-15'){await client.eval(`document.getElementById('variant').value='B';document.getElementById('variant').dispatchEvent(new Event('change'))`);test('R1-15 B shows whole paragraph and precise scope',await client.eval(`document.getElementById('old-text').textContent===packet.cards[0].originalFull&&document.getElementById('new-text').textContent===packet.cards[0].options.find(o=>o.id==='B').fullText&&document.querySelector('.scope').textContent.includes('整体替换')`));}
 test(id+' source/reviewer/ledger links are local',await client.eval(`[...document.querySelectorAll('#card a')].every(a=>a.protocol==='file:')`));
}
await client.eval(`navigate('R1-21',false);choices.delete('R1-21');renderCard();document.getElementById('full-context').open=true`);
test('R1-21 insertion keeps original paragraph then exact candidate',await client.eval(`document.querySelector('.full-pair>div:last-child pre').textContent===packet.cards.find(c=>c.id==='R1-21').originalFull+'\\n\\n'+packet.cards.find(c=>c.id==='R1-21').options[0].fullText`));
await client.shot('desktop-insertion.png');report.screenshots.push('desktop-insertion.png');
await client.eval(`navigate('R1-35',false);choices.delete('R1-35');renderCard()`);
test('R1-35 current v4 recommendation is KEEP',await client.eval(`document.getElementById('variant').value==='KEEP'&&document.getElementById('new-text').textContent===document.getElementById('old-text').textContent`));
await client.shot('desktop-keep.png');report.screenshots.push('desktop-keep.png');
await client.eval(`document.getElementById('filter').value='pending';document.getElementById('filter').dispatchEvent(new Event('change'))`);
test('Fact-pending filter finds three cards',await client.eval(`document.querySelectorAll('[data-card]').length===3`));
await client.eval(`document.getElementById('search').value='not-a-thesis-match';document.getElementById('search').dispatchEvent(new Event('input'))`);
test('Empty filter gives recovery route',await client.eval(`document.querySelector('.empty')?.textContent.includes('重置查看')`));
await client.eval(`document.getElementById('reset').click()`);
test('Reset restores filters, choices, mode, diff, first card',await client.eval(`document.getElementById('search').value===''&&document.getElementById('filter').value==='all'&&document.querySelectorAll('[data-card]').length===5&&document.getElementById('variant').value==='A'&&document.getElementById('mode').value==='compare'&&document.getElementById('mark-diff').checked&&document.activeElement.id==='search'`));
// Keyboard follows normal focus order and activates native buttons/details.
const key=async(k,code,extra={})=>{await client.send('Input.dispatchKeyEvent',{type:'keyDown',key:k,code,windowsVirtualKeyCode:k==='Enter'?13:9,nativeVirtualKeyCode:k==='Enter'?36:48,...(k==='Enter'?{text:'\r',unmodifiedText:'\r'}:{}),...extra});await client.send('Input.dispatchKeyEvent',{type:'keyUp',key:k,code,windowsVirtualKeyCode:k==='Enter'?13:9,nativeVirtualKeyCode:k==='Enter'?36:48,...extra});};
await key('Tab','Tab');test('Keyboard Tab reaches filter',await client.eval(`document.activeElement.id==='filter'`));
await key('Tab','Tab');test('Keyboard Tab reaches card button',await client.eval(`document.activeElement.hasAttribute('data-card')`));
await key('Enter','Enter');test('Keyboard Enter navigates and focuses card title',await client.eval(`document.activeElement.id==='card-title'`));
await client.eval(`document.getElementById('view-keep').focus()`);await key('Enter','Enter');test('Keyboard KEEP comparison works without approval',await client.eval(`document.getElementById('variant').value==='KEEP'&&document.activeElement.id==='view-keep'`));
await client.eval(`document.querySelector('#evidence summary').focus()`);await key('Enter','Enter');test('Evidence details keyboard toggle',await client.eval(`document.getElementById('evidence').open`));
await client.eval(`document.getElementById('reset').click();navigate('R1-25',false)`);
for(const mode of ['proposed','original','compare']){
 await client.eval(`document.getElementById('mode').value='${mode}';document.getElementById('mode').dispatchEvent(new Event('change'))`);
 test('View mode '+mode,await client.eval(`document.getElementById('comparison').dataset.mode==='${mode}'`));
}
await client.eval(`document.activeElement.blur();window.scrollTo(0,0)`);await client.shot('desktop-loss.png');report.screenshots.push('desktop-loss.png');
await client.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:false});
await client.eval(`document.getElementById('reset').click();window.scrollTo(0,0)`);
for(const id of ids){
 await client.eval(`navigate(${JSON.stringify(id)},false)`);
 test(id+' narrow 390px no horizontal overflow',await client.eval(`document.documentElement.scrollWidth<=innerWidth`));
 test(id+' narrow comparison is one column',await client.eval(`getComputedStyle(document.getElementById('comparison')).gridTemplateColumns.split(' ').length===1`));
}
await client.eval(`navigate('R1-15',false);document.activeElement.blur();window.scrollTo(0,0)`);await client.shot('narrow-top.png');report.screenshots.push('narrow-top.png');
await client.eval(`document.querySelector('.comparison').scrollIntoView({block:'start'})`);await client.shot('narrow-text.png');report.screenshots.push('narrow-text.png');
await client.eval(`document.getElementById('full-context').open=true;window.scrollTo(0,document.documentElement.scrollHeight);document.getElementById('next').click()`);test('Bottom Next brings new heading into viewport',await client.eval(`document.getElementById('card-title').getBoundingClientRect().top>=-2&&document.getElementById('card-title').getBoundingClientRect().top<innerHeight&&document.activeElement.id==='card-title'`));
// A newly opened local tab has fresh view defaults; no shared author-choice state.
const fresh=await (await fetch(`http://127.0.0.1:${port}/json/new?${encodeURIComponent(url)}`,{method:'PUT'})).json();
const second=new CDP(fresh.webSocketDebuggerUrl);await second.send('Runtime.enable');await second.send('Page.enable');await second.loaded(url);
test('Second tab starts with original recommended view',await second.eval(`document.getElementById('variant').value==='A'&&document.getElementById('filter').value==='all'`));
await second.send('Page.close');second.close();
await client.loaded(url);test('Reload discards temporary view choices',await client.eval(`document.getElementById('variant').value==='A'&&document.getElementById('search').value===''`));
// Test the actual ledger destination in a fresh test tab. Chrome renders .md as plain text.
const ledgerHref=await client.eval(`document.querySelector('.decision-link').href`);
const ledgerTab=await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`,{method:'PUT'})).json();
const ledger=new CDP(ledgerTab.webSocketDebuggerUrl);await ledger.send('Page.enable');await ledger.send('Runtime.enable');await ledger.loaded(ledgerHref);
report.ledgerNavigation=await ledger.eval(`({url:location.href,contentType:document.contentType,hasOriginalText:document.body.textContent.includes('唯一的人类决定清单'),fragmentResolves:!!document.getElementById('decision-r1-15')})`);
test('Actual ledger link opens original Markdown',report.ledgerNavigation.hasOriginalText);test('Ledger link discloses ID search instead of assuming Markdown anchors',await client.eval(`document.querySelector('.decision-link').textContent.includes('搜索 R1-15')`));await ledger.send('Page.close');ledger.close();
report.consoleErrors=client.events.filter(x=>x.method==='Runtime.exceptionThrown').map(x=>x.params.exceptionDetails);
report.networkRequests=client.events.filter(x=>x.method==='Network.requestWillBeSent').map(x=>x.params.request.url);
test('No runtime exceptions',report.consoleErrors.length===0);
test('No HTTP(S), websocket or external network requests',report.networkRequests.every(u=>u.startsWith('file:')||u==='about:blank'));
const html=fs.readFileSync(path.join(dir,'index.html'),'utf8');
test('No persistence, external content fetch, form or approval controls',!/(?:localStorage|sessionStorage|indexedDB|fetch\(|XMLHttpRequest|<form\b)/.test(html));
fs.writeFileSync(path.join(dir,'evidence/browser_validation.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed:report.tests.length,failed:0,screenshots:report.screenshots,externalRequests:report.networkRequests.filter(u=>!u.startsWith('file:')),runtimeErrors:report.consoleErrors.length}));
client.close();
