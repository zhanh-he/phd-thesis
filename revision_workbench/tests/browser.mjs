// Real-browser integration checks. Uses installed Chrome and Node built-ins only.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawn, spawnSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {fileURLToPath, pathToFileURL} from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, '../..');
const evidence = path.resolve(here, '../evidence');
fs.mkdirSync(evidence, {recursive: true});
const entry = pathToFileURL(path.join(repo, 'START_HERE.html')).href;
const report = {entry: 'START_HERE.html', startedAt: new Date().toISOString(), tests: [], screenshots: [], runtimeErrors: [], externalRequests: []};
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
let chrome, profile, port = process.env.WORKBENCH_CDP_PORT;
const tempDirs=[];

class CDP {
  constructor(url) {
    this.events = []; this.pending = new Map(); this.next = 1;
    this.ws = new WebSocket(url);
    this.ready = new Promise((resolve, reject) => {
      this.ws.addEventListener('open', resolve, {once: true});
      this.ws.addEventListener('error', reject, {once: true});
    });
    this.ws.addEventListener('message', e => {
      const msg = JSON.parse(e.data);
      if (!msg.id) {this.events.push(msg); return;}
      const task = this.pending.get(msg.id); this.pending.delete(msg.id);if(!task)return;clearTimeout(task.timer);
      if (msg.error) task.reject(new Error(JSON.stringify(msg.error))); else task.resolve(msg.result);
    });
    for(const event of ['error','close'])this.ws.addEventListener(event,()=>{for(const task of this.pending.values()){clearTimeout(task.timer);task.reject(new Error('CDP transport '+event));}this.pending.clear();});
  }
  async send(method, params = {}) {
    await this.ready; const id = this.next++;
    return new Promise((resolve, reject) => {
      const timer=setTimeout(()=>{this.pending.delete(id);reject(new Error('CDP command timeout: '+method));},25000);
      this.pending.set(id, {resolve, reject,timer});
      this.ws.send(JSON.stringify({id, method, params}));
    });
  }
  async eval(expression) {
    const result = await this.send('Runtime.evaluate', {expression, returnByValue: true, awaitPromise: true});
    if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
    return result.result.value;
  }
  async readString(expression){
    // Node's built-in WebSocket can stall on very large CDP string frames.
    // Transfer actual backups in bounded pieces; this is test transport only.
    const key='qaTransfer'+Math.random().toString(36).slice(2);
    const length=await this.eval(`window.${key}=(${expression});window.${key}.length`);let out='';
    for(let at=0;at<length;at+=128000)out+=await this.eval(`window.${key}.slice(${at},${at+128000})`);
    await this.eval(`delete window.${key}`);return out;
  }
  async putString(text,key='qaIncomingString'){
    await this.eval(`window.${key}=''`);
    for(let at=0;at<text.length;at+=128000)await this.eval(`window.${key}+=${JSON.stringify(text.slice(at,at+128000))}`);
    return key;
  }
  async load(url = entry) {
    await this.send('Page.navigate', {url});
    for (let tries = 0; tries < 160; tries++) {
      if (await this.eval('!!window.workbench').catch(() => false)) return;
      await sleep(30);
    }
    throw new Error('Workbench did not initialize');
  }
  async shot(name, full = false) {
    const size=full?(await this.send('Page.getLayoutMetrics')).cssContentSize:null;
    const result = await this.send('Page.captureScreenshot', {format: 'png', captureBeyondViewport: full,...(size?{clip:{x:0,y:0,width:size.width,height:size.height,scale:1}}:{})});
    fs.writeFileSync(path.join(evidence, name), Buffer.from(result.data, 'base64'));
    report.screenshots.push(name);
  }
  async key(key, code = key) {
    const virtual = {Tab: 9, Enter: 13, ArrowRight: 39, ArrowLeft: 37, Space: 32}[key];
    await this.send('Input.dispatchKeyEvent', {type: 'keyDown', key, code, ...(virtual ? {windowsVirtualKeyCode: virtual} : {}), ...(key === 'Enter' ? {text: '\r'} : {})});
    await this.send('Input.dispatchKeyEvent', {type: 'keyUp', key, code, ...(virtual ? {windowsVirtualKeyCode: virtual} : {})});
  }
  close() {this.ws.close();}
}

const clients = [];
async function newTab(script, url = entry) {
  const target = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, {method: 'PUT'})).json();
  const client = new CDP(target.webSocketDebuggerUrl); clients.push(client);
  await client.send('Page.enable'); await client.send('Runtime.enable'); await client.send('Network.enable');
  if (script) await client.send('Page.addScriptToEvaluateOnNewDocument', {source: script});
  await client.load(url); return client;
}
async function check(name, work) {
  try {
    const result = typeof work === 'function' ? await work() : await work;
    if (!result) throw new Error('Assertion returned false');
    report.tests.push({name, passed: true});
  } catch (error) {
    report.tests.push({name, passed: false, error: String(error.message || error)});
  }
}
async function edit(client, selector, value, focus = true) {
  await client.eval(`(()=>{const el=document.querySelector(${JSON.stringify(selector)});${focus ? 'el.focus();' : ''}el.value=${JSON.stringify(value)};el.dispatchEvent(new Event('input',{bubbles:true}));return true;})()`);
}
async function importLedgerFile(client,file){
  const doc=await client.send('DOM.getDocument');
  const input=await client.send('DOM.querySelector',{nodeId:doc.root.nodeId,selector:'#import-ledger'});
  await client.send('DOM.setFileInputFiles',{nodeId:input.nodeId,files:[file]});
  for(let tries=0;tries<200;tries++){if(await client.eval(`document.getElementById('import-ledger').value===''`))return;await sleep(20);}
  throw Error('File import did not settle');
}

try {
  if (!port) {
    profile = fs.mkdtempSync(path.join(os.tmpdir(), 'thesis-workbench-browser-'));
    chrome = spawn(process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`, '--no-first-run', '--no-default-browser-check', '--disable-background-networking', '--disable-component-update', 'about:blank'], {stdio: ['ignore', 'ignore', 'pipe']});
    let chromeLog = ''; chrome.stderr.on('data', chunk => {chromeLog += chunk;});
    const portFile = path.join(profile, 'DevToolsActivePort');
    for (let tries = 0; tries < 200 && !fs.existsSync(portFile); tries++) await sleep(30);
    if (!fs.existsSync(portFile)) throw new Error(`Chrome startup failed: ${chromeLog.slice(-2000)}`);
    port = fs.readFileSync(portFile, 'utf8').split('\n')[0];
  }
  const first = await newTab();
  report.dataset = await first.eval(`({documentId:workbench.data.documentId,edition:workbench.data.edition,commentCount:workbench.data.comments.length})`);
  report.entrySha256 = createHash('sha256').update(fs.readFileSync(path.join(repo, 'START_HERE.html'))).digest('hex');
  report.backupMetrics=await first.eval(`(()=>{const text=workbench.exportBackup(),b=JSON.parse(text);return {utf8Bytes:new TextEncoder().encode(text).length,operations:b.operations.length,contextRecords:b.workbenchContext.records.length,reviewerCount:b.workbenchContext.dataset.reviewers.length}})()`);
  const freshBackup=await first.readString('workbench.exportBackup()');await first.putString(freshBackup);
  await check('Actual portable backup imports on fresh state without losing configured source/reply context',first.eval(`(()=>{workbench.ledger.importJSON(qaIncomingString);const b=JSON.parse(workbench.exportBackup());return b.workbenchContext.records.length===workbench.data.comments.length&&b.workbenchContext.records.every((r,i)=>r.documentedReply.text===workbench.data.comments[i].authorReply.text&&r.sourceReferences.length===workbench.data.comments[i].locations.length)})()`));
  await first.send('Emulation.setDeviceMetricsOverride', {width: 1440, height: 1000, deviceScaleFactor: 1, mobile: false});
  await check('Fresh load has unique comment IDs and config-derived count', first.eval(`(()=>{const ids=workbench.data.comments.map(c=>c.id);return ids.length>0&&new Set(ids).size===ids.length&&document.getElementById('list-count').textContent.includes(String(ids.length))})()`));
  await check('Primary thesis retains all43 IDs in exact report order', first.eval(`workbench.data.comments.map(c=>c.id).join(',')===[...Array.from({length:38},(_,i)=>'R1-'+String(i+1).padStart(2,'0')),...Array.from({length:5},(_,i)=>'R2-'+String(i+1).padStart(2,'0'))].join(',')`));
  await check('Navigation preserves config comment order and reviewer metadata', first.eval(`(()=>{const ids=[...document.querySelectorAll('#comment-list [data-comment-id]')].map(el=>el.dataset.commentId),reviewers=workbench.data.reviewers||[{id:'R1',displayName:'Benetos'},{id:'R2',displayName:'奥克兰大学教授'}];return ids.join(',')===workbench.data.comments.map(c=>c.id).join(',')&&reviewers.every(r=>[...document.getElementById('reviewer-filter').options].some(o=>o.value===r.id&&o.textContent.includes(r.shortName||r.displayName)))})()`));
  await check('Desktop has no horizontal overflow', first.eval('document.documentElement.scrollWidth<=innerWidth'));
  await first.shot('browser-desktop.png');
  for(const id of ['R1-05','R1-13','R1-21','R1-30','R1-34','R1-35']){
    await first.eval(`workbench.select('${id}');document.activeElement.blur();window.scrollTo(0,0)`);await first.shot('browser-'+id.toLowerCase()+'.png');
    if(['R1-05','R1-21','R1-30','R1-35'].includes(id)){
      await first.eval(`document.querySelector('.evidence-box').open=true`);
      const rendered=await first.readString(`document.getElementById('workspace').innerText+'\\n\\n=== Exact editor values / placeholders (fresh source-seeded state) ===\\n'+[...document.querySelectorAll('#workspace textarea')].map(el=>el.id+'\\nVALUE: '+JSON.stringify(el.value)+'\\nPLACEHOLDER: '+el.placeholder).join('\\n\\n')+'\\n\\n=== Checked decisions ===\\n'+[...document.querySelectorAll('#workspace input:checked')].map(el=>(el.name||el.dataset.authorScope||'checkbox')+': '+el.value).join('\\n')`);
      fs.writeFileSync(path.join(evidence,'browser-'+id.toLowerCase()+'.txt'),rendered+'\n');
      await first.shot('browser-'+id.toLowerCase()+'-full.png',true);
    }
  }
  await first.eval(`workbench.select('R1-01');window.scrollTo(0,0)`);
  await first.send('Emulation.setDeviceMetricsOverride', {width:390,height:844,deviceScaleFactor:1,mobile:false});
  await first.eval(`document.activeElement.blur();window.scrollTo(0,0)`);await first.shot('browser-narrow-top.png');
  await first.eval(`document.getElementById('plan').scrollIntoView({block:'center'})`);await first.shot('browser-narrow-notes.png');
  await first.send('Emulation.setDeviceMetricsOverride', {width:1440,height:1000,deviceScaleFactor:1,mobile:false});
  await first.eval('window.scrollTo(0,0)');
  const comments = JSON.parse(await first.readString('JSON.stringify(workbench.data.comments)'));
  for (const comment of comments) {
    await first.eval(`workbench.select(${JSON.stringify(comment.id)})`);
    await check(`${comment.id} navigates to an identified subsection`, first.eval(`document.querySelector('#workspace article').id===${JSON.stringify(comment.id)}&&document.querySelector('.card-kicker').textContent.includes(${JSON.stringify(comment.id)})`));
    await check(`${comment.id} has two exclusive three-state decisions`, first.eval(`['authorDecision','assistantDecision'].every(name=>{const rs=[...document.querySelectorAll('input[name="'+name+'"]')];return rs.length===3&&rs.filter(r=>r.checked).length===1&&rs.map(r=>r.value).sort().join(',')==='keep,modify,pending'})`));
    const replyDisplay=comment.authorReply.displayText||comment.authorReply.text||'未找到针对这一条的明确回复。';
    await check(`${comment.id} shows exact reviewer original and faithful separate author reply`, first.eval(`document.querySelector('.original-text').textContent===${JSON.stringify(comment.original)}&&document.querySelector('.reply-text').textContent===${JSON.stringify(replyDisplay)}`));
    await check(`${comment.id} author seed follows source decision without inferred choice`, first.eval(`(()=>{const c=workbench.data.comments.find(c=>c.id===${JSON.stringify(comment.id)}),s=workbench.state(c.id);return s.authorDecision===c.authorReply.decision&&(!c.authorReply.prefill?c.authorReply.decision==='pending':c.authorReply.sources.length>0)})()`));
    await check(`${comment.id} all edit quotes and related retained references are accessible`, first.eval(`(()=>{const c=workbench.data.comments.find(c=>c.id===${JSON.stringify(comment.id)}),changes=c.locations.filter(l=>l.operation?.toLowerCase()!=='keep'),keeps=c.locations.filter(l=>l.operation?.toLowerCase()==='keep'),primary=c.assistant.decision==='keep'&&keeps.length?keeps:changes.length?changes:c.locations,q=[...document.querySelectorAll('.source-quote')],e=document.querySelector('.evidence-box').textContent;return q.length===primary.length&&q.every((el,i)=>el.textContent===primary[i].quote)&&c.locations.every(l=>workbench.data.sources[l.file]?.text.includes(l.quote))&&c.locations.filter(l=>!primary.includes(l)).every(l=>e.includes(l.quote))})()`));
    await check(`${comment.id} visible edit location numbering is sequential despite hidden references`,first.eval(`(()=>{const headings=[...document.querySelectorAll('.location>h4')];return headings.length<2||headings.every((h,i)=>h.textContent.startsWith((i+1)+'. '))})()`));
    if(comment.assistant.decision==='keep')await check(`${comment.id} keep recommendation does not present another item's edits as its own proposal`,first.eval(`!document.querySelector('#workspace .proposal')`));
    if (comment.locations.length) {
      await first.eval(`document.querySelector('[data-context]').click()`);
      await check(`${comment.id} contextual preview exposes highlighted source lines`, first.eval(`(()=>{const i=document.querySelector('[data-context]').dataset.context;return !document.getElementById('context-'+i).hidden&&document.querySelectorAll('#context-'+i+' .source-line.target').length>0})()`));
    }
  }
  for(const id of ['R1-20','R1-21','R1-24','R1-29','R1-36']){
    await first.eval(`workbench.select('${id}')`);
    await check(`${id} qualified author stance remains visible without blanket decision`,first.eval(`(()=>{const c=workbench.data.comments.find(c=>c.id==='${id}');return typeof c.authorReply.stance==='string'&&c.authorReply.stance.length>0&&document.getElementById('workspace').textContent.includes(c.authorReply.stance)&&workbench.state(c.id).authorDecision==='pending'})()`));
  }
  await first.eval(`workbench.select('R1-21')`);
  await check('R1-21 scoped no-expansion stance is checked while main decision remains yellow/pending',first.eval(`document.querySelector('[data-author-scope]').checked&&document.getElementById('workspace').textContent.includes('不扩展当前项目')&&workbench.state('R1-21').authorDecision==='pending'&&workbench.state('R1-21').color==='yellow'`));
  await first.eval(`document.querySelector('[data-author-scope]').click()`);await first.load();await first.eval(`workbench.select('R1-21')`);
  await check('Scoped override survives reload without modifying plan or main author decision',first.eval(`!document.querySelector('[data-author-scope]').checked&&workbench.state('R1-21').authorDecision==='pending'&&workbench.state('R1-21').color==='yellow'&&workbench.ledger.history('R1-21','plan').length===0&&workbench.ledger.history('R1-21','authorDecision').length===0`));
  await first.eval(`document.querySelector('[data-author-scope]').click()`);await first.load();await first.eval(`workbench.select('R1-21')`);
  await check('Restored scoped no-expansion choice remains separate from execution',first.eval(`document.querySelector('[data-author-scope]').checked&&workbench.state('R1-21').executionStatus==='not_started'&&workbench.state('R1-21').authorDecision==='pending'`));
  await check('Portable export preserves every raw documented author reply',first.eval(`(()=>{const b=JSON.parse(workbench.exportBackup());return workbench.data.comments.every((c,i)=>b.workbenchContext.dataset.comments[i].authorReply.text===c.authorReply.text)})()`));
  for(const c of comments){
    for(const [i,l] of c.locations.entries()){
      if(l.asset){
        await first.eval(`workbench.select(${JSON.stringify(c.id)})`);
        const relative=l.asset.split('/').map(encodeURIComponent).join('/');
        await check(`${c.id} image asset has a working portable reference and separate LaTeX locator`,fs.existsSync(path.join(repo,l.asset))&&await first.eval(`(()=>{const b=document.querySelector('[data-location="${i}"]');return !!b.querySelector('a[href="${relative}"]')&&b.textContent.includes('无行号')&&b.textContent.includes('LaTeX')})()`));
      }
      if(l.operation==='verify'&&l.audit?.proposedEnglish===null){
        await first.eval(`workbench.select(${JSON.stringify(c.id)})`);
        await check(`${c.id}/${l.key} unresolved source evidence does not fabricate replacement/deletion text`,first.eval(`(()=>{const b=document.querySelector('[data-location="${i}"]');return b?!b.querySelector('.proposal')&&!b.querySelector('[data-copy-proposal]')&&!b.textContent.includes('删除，不添加新文字'):document.querySelector('.evidence-box').textContent.includes(${JSON.stringify(l.quote)})})()`));
      }
    }
  }
  const shared=comments.find(c=>c.assistant.decision!=='keep'&&c.locations.some(l=>l.operationOwner&&l.operationOwner!==c.id));
  if(shared){
    const owner=shared.locations.find(l=>l.operationOwner&&l.operationOwner!==shared.id).operationOwner;
    await first.eval(`workbench.select(${JSON.stringify(shared.id)});document.querySelector('[data-owner]').click()`);
    await check('Shared source operation navigates to its canonical reviewer owner',first.eval(`document.querySelector('#workspace article').id===${JSON.stringify(owner)}`));
  }
  const optional=comments.find(c=>c.assistant.decision!=='keep'&&c.locations.some(l=>l.independentlyOptional&&l.operation!=='keep'));
  if(optional){
    const location=optional.locations.find(l=>l.independentlyOptional&&l.operation!=='keep'),owner=location.operationOwner||optional.id,field='editChoice:'+(location.audit?.sharedEditId||location.key);
    await first.eval(`workbench.select(${JSON.stringify(optional.id)});document.querySelector('[data-optional]').click()`);
    await check('Optional source edit uses canonical persistent field and does not claim execution',first.eval(`workbench.ledger.get(${JSON.stringify(owner)},${JSON.stringify(field)}).value==='modify'&&workbench.state(${JSON.stringify(optional.id)}).executionStatus==='not_started'`));
    await first.load();await first.eval(`workbench.select(${JSON.stringify(optional.id)})`);
    await check('Optional source edit choice survives reload',first.eval(`document.querySelector('[data-optional]').checked`));
  }
  await first.eval(`workbench.select('R1-01')`);
  await check('All nine agreement combinations have requested colors', first.eval(`(()=>{const f=(a,b)=>{const v=workbench.agreement(a,b);return typeof v==='string'?v:v.color||v.tone||v.status};return f('modify','modify')==='green'&&f('keep','keep')==='red'&&['gray','grey'].includes(f('keep','pending'))&&['modify,pending','modify,keep','pending,pending','pending,modify','pending,keep','keep,modify'].every(p=>f(...p.split(','))==='yellow')})()`));
  await check('Source links are portable relative local references', first.eval(`[...document.querySelectorAll('#workspace a[href]')].every(a=>a.protocol==='file:'&&!a.getAttribute('href').startsWith('/')&&!a.getAttribute('href').includes('/Users/'))`));
  await first.eval(`window.qaClipboard=[];Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async text=>qaClipboard.push(text)}});window.qaCopiedLocation=Number(document.querySelector('[data-copy-path]').dataset.copyPath);document.querySelector('[data-copy-path]').click();document.querySelector('[data-copy-quote="'+qaCopiedLocation+'"]').click()`);
  await check('Copy location and exact quote expose portable source anchors', first.eval(`(()=>{const l=workbench.data.comments[0].locations[qaCopiedLocation],line=l.binding&&l.binding.status!=='needs_relocation'?l.binding.lineStart:l.lineStart;return qaClipboard[0]===l.file+':'+line&&qaClipboard[1]===l.quote})()`));
  await check('Export backup and report actions are available', first.eval(`['export-ledger','export-report'].every(id=>!!document.getElementById(id)&&!document.getElementById(id).disabled)&&document.getElementById('import-ledger').type==='file'`));
  await check('Timestamped export workflow has no connected-file overwrite controls',first.eval(`!document.getElementById('link-file')&&!document.getElementById('save-file')&&!document.body.innerText.includes('连接备份文件')&&!document.body.innerText.includes('保存到已连接文件')`));
  await first.eval(`document.getElementById('search').focus()`); await first.key('Tab');
  await check('Keyboard Tab moves to an interactive filter', first.eval(`['status-filter','reviewer-filter'].includes(document.activeElement.id)`));
  await first.eval(`document.querySelector('[name=authorDecision][value=pending]').focus()`); await first.key('ArrowRight');
  await check('Native keyboard decision control stays mutually exclusive', first.eval(`document.querySelectorAll('[name=authorDecision]:checked').length===1`));
  const exact = 'QA only — multiline plan\n\\textbf{A & B} $x_1$\n  preserve indentation\n';
  await edit(first, '#plan', exact);
  await check('Input saves synchronously before blur/navigation', first.eval(`workbench.ledger.get('R1-01','plan').value===${JSON.stringify(exact)}`));
  await first.load(); await first.eval(`workbench.select('R1-01')`);
  await check('Refresh preserves exact English/LaTeX/multiline text', first.eval(`document.getElementById('plan').value===${JSON.stringify(exact)}`));
  const second = await newTab(); await second.eval(`workbench.select('R1-01')`);
  await check('Reopen restores existing edits', second.eval(`document.getElementById('plan').value===${JSON.stringify(exact)}`));
  await first.eval(`document.getElementById('plan').focus()`);
  await second.eval(`document.getElementById('actualText').focus()`);
  await edit(first, '#plan', 'QA parallel plan', false);
  const actual = 'QA parallel actual\n\\cite{example}';
  await edit(second, '#actualText', actual, false);
  await sleep(80); // Observe the real cross-tab storage event, without forcing refresh.
  await check('Old and new tabs merge independent fields without replacement', first.eval(`workbench.ledger.get('R1-01','plan').value==='QA parallel plan'&&workbench.ledger.get('R1-01','actualText').value===${JSON.stringify(actual)}`));
  const trace = `window.qaTrace=[];const rawSet=workbench.ledger.set.bind(workbench.ledger);workbench.ledger.set=(...args)=>{qaTrace.push({type:'set',args:JSON.parse(JSON.stringify(args))});return rawSet(...args)};workbench.select('R1-02');document.getElementById('plan').addEventListener('focus',()=>qaTrace.push({type:'focus',heads:workbench.ledger.get('R1-02','plan').heads}));document.getElementById('plan').focus()`;
  await first.eval(trace);
  await second.eval(trace);
  report.sameFieldBefore = [await first.eval(`({state:workbench.ledger.get('R1-02','plan'),active:document.activeElement.id})`), await second.eval(`({state:workbench.ledger.get('R1-02','plan'),active:document.activeElement.id})`)];
  await edit(first, '#plan', 'QA simultaneous A', false);
  await edit(second, '#plan', 'QA simultaneous B', false);
  await sleep(80); // The open peer tab must surface conflicts automatically.
  report.sameFieldAfter = [await first.eval(`workbench.ledger.history('R1-02','plan')`), await second.eval(`workbench.ledger.history('R1-02','plan')`)];
  report.sameFieldTrace = [await first.eval('qaTrace'), await second.eval('qaTrace')];
  await check('Same-field concurrent values are retained as a conflict', first.eval(`(()=>{const s=workbench.ledger.get('R1-02','plan');return s.conflicts?.length>=2&&JSON.stringify(s.conflicts).includes('QA simultaneous A')&&JSON.stringify(s.conflicts).includes('QA simultaneous B')})()`));
  await check('Conflict is visible in UI with both texts', first.eval(`document.getElementById('workspace').textContent.includes('QA simultaneous A')&&document.getElementById('workspace').textContent.includes('QA simultaneous B')`));
  const exported = await first.readString('workbench.exportBackup()');await first.putString(exported);
  await first.eval(`workbench.ledger.importJSON(qaIncomingString)`);
  await check('Export/import roundtrip is idempotent and retains conflict', first.eval(`(()=>{const s=workbench.ledger.get('R1-02','plan');return s.conflicts?.length>=2&&workbench.ledger.get('R1-01','actualText').value===${JSON.stringify(actual)}})()`));
  await check('Report export preserves raw note text and pending markers', first.eval(`(()=>{const r=workbench.exportReport();const s=typeof r==='string'?r:JSON.stringify(r);return s.includes('QA parallel plan')&&s.includes('QA parallel actual')&&/pending|待定|未实施|未执行/.test(s)})()`));
  await first.eval(`workbench.select('R1-03');workbench.ledger.set('R1-03','authorDecision','modify',{candidateVersion:'QA-outdated-candidate'});workbench.refresh()`);
  await check('Choice on changed candidate is preserved but current agreement becomes pending', first.eval(`workbench.ledger.get('R1-03','authorDecision').value==='modify'&&workbench.state('R1-03').authorDecision==='pending'&&workbench.state('R1-03').color==='yellow'&&document.getElementById('workspace').innerText.includes('旧版本')`));
  await first.eval(`document.querySelector('[name=authorDecision][value=modify]').click()`);
  await check('Explicit current-version reconfirmation clears stale decision marker', first.eval(`workbench.state('R1-03').authorDecision==='modify'&&!workbench.state('R1-03').fields.authorDecision.raw.stale`));
  await first.eval(`(()=>{const json=JSON.parse(workbench.ledger.exportJSON());json.schemaVersion=2;json.minReaderVersion=1;json.qaFutureMetadata={retain:'exact future metadata'};json.operations.push({id:'QA-import-unknown-op',documentId:json.documentId,recordId:'QA-UNKNOWN-ID',field:'future-field',value:'QA unknown data\\n\\\\command{unchanged}',parents:[],actor:'QA-import',timestamp:new Date().toISOString(),candidateVersion:null});workbench.ledger.importJSON(JSON.stringify(json));workbench.refresh()})()`);
  await check('Compatible schema evolution retains unknown IDs separately and visibly', first.eval(`!!workbench.ledger.snapshot().unknownRecords['QA-UNKNOWN-ID']&&document.getElementById('warnings').textContent.includes('QA-UNKNOWN-ID')&&workbench.ledger.exportJSON().includes('exact future metadata')`));
  await check('Invalid known decision import is rejected atomically', first.eval(`(()=>{const count=workbench.ledger.history().length,json=JSON.parse(workbench.ledger.exportJSON());json.operations.push({id:'QA-invalid-decision',documentId:json.documentId,recordId:'R1-03',field:'authorDecision',value:'QA-bogus-choice',parents:[],actor:'QA-import',timestamp:new Date().toISOString(),candidateVersion:null});let rejected=false;try{workbench.ledger.importJSON(JSON.stringify(json))}catch(e){rejected=true}return rejected&&workbench.ledger.history().length===count})()`));
  const importFile = path.join(profile || os.tmpdir(), 'qa-ledger-roundtrip.json');
  fs.writeFileSync(importFile, await first.readString('workbench.exportBackup()'));
  const doc = await first.send('DOM.getDocument');
  const fileInput = await first.send('DOM.querySelector', {nodeId:doc.root.nodeId, selector:'#import-ledger'});
  await first.send('DOM.setFileInputFiles', {nodeId:fileInput.nodeId, files:[importFile]});
  for (let tries=0;tries<100;tries++) {if (await first.eval(`document.getElementById('import-ledger').value===''`)) break; await sleep(20);}
  await check('File input imports portable ledger by merge and retains earlier note history', first.eval(`document.getElementById('import-ledger').value===''&&workbench.ledger.get('R1-01','actualText').value===${JSON.stringify(actual)}&&workbench.ledger.get('R1-02','plan').conflicts.length>=2`));
  await first.eval(`workbench.select('R1-01');document.querySelector('[data-history=plan]').click()`);
  await check('History/recovery dialog offers prior exact values', first.eval(`document.getElementById('history-dialog').open&&document.getElementById('history-content').textContent.includes('QA parallel plan')&&document.getElementById('history-content').textContent.includes('preserve indentation')`));
  await first.eval(`document.getElementById('close-history').click();document.querySelector('[data-undo=plan]').click()`);
  await check('Undo creates recoverable history and restores exact previous text', first.eval(`workbench.ledger.get('R1-01','plan').value===${JSON.stringify(exact)}&&workbench.ledger.history('R1-01','plan').some(op=>op.value==='QA parallel plan')`));
  await first.eval(`document.getElementById('plan').focus()`); await edit(first,'#plan','QA parallel plan',false);
  await first.eval(`localStorage.setItem(workbench.ledger.prefix+'qa-corrupt','{QA invalid JSON')`);
  const recovery = await newTab();
  await check('Corrupt storage produces a visible recovery warning without losing valid edits', recovery.eval(`workbench.ledger.status().quarantinedCount===1&&document.body.innerText.includes('损坏')&&workbench.ledger.get('R1-01','plan').value==='QA parallel plan'`));
  await check('Corrupt original bytes remain in portable recovery export', recovery.eval(`workbench.ledger.exportJSON().includes('{QA invalid JSON')&&localStorage.getItem(workbench.ledger.prefix+'qa-corrupt')==='{QA invalid JSON'`));
  await first.eval(`workbench.select('R1-01');document.activeElement.blur();window.scrollTo(0,0)`);
  await first.send('Emulation.setDeviceMetricsOverride', {width: 390, height: 844, deviceScaleFactor: 1, mobile: false});
  await check('390px layout has no horizontal overflow', first.eval('document.documentElement.scrollWidth<=innerWidth'));
  for(const c of comments){await first.eval(`workbench.select(${JSON.stringify(c.id)})`);await check(`${c.id} narrow source/decision layout has no overflow`,first.eval('document.documentElement.scrollWidth<=innerWidth'));}
  await first.eval(`workbench.select('R1-01');document.activeElement.blur();window.scrollTo(0,0)`);
  await first.eval(`document.getElementById('plan').scrollIntoView({block:'center'})`);
  const blocked = await newTab(`Object.defineProperty(window,'localStorage',{get(){throw new DOMException('QA disabled storage','SecurityError')}});`);
  await check('Disabled storage warns clearly and keeps export available', blocked.eval(`/不可|无法|未保存|临时|unavailable|volatile|禁用/i.test(document.body.innerText)&&!document.getElementById('export-ledger').disabled`));
  await edit(blocked, '#plan', 'QA volatile notes');
  await check('Disabled storage retains editable notes in portable export', blocked.eval(`workbench.ledger.exportJSON().includes('QA volatile notes')`));
  // A second manuscript uses the same app and browser profile with a different
  // document ID, arbitrary reviewer IDs/order and a deliberately reused record ID.
  const manuscriptDir=fs.mkdtempSync(path.join(profile||os.tmpdir(),'manuscript-two-'));
  tempDirs.push(manuscriptDir);
  const secondData={
    schemaVersion:1,documentId:'qa-independent-manuscript-two',edition:'QA second manuscript fixture',
    manuscript:{title:'QA Second Manuscript',shortTitle:'QA Manuscript 2',author:'QA Author',subtitle:'Reusable workbench verification'},
    reviewers:[{id:'Reviewer-C',displayName:'Reviewer C',shortName:'C'},{id:'Reviewer-A',displayName:'Reviewer A',shortName:'A'},{id:'Reviewer-B',displayName:'Reviewer B',shortName:'B'}],
    sourceBaseline:{label:'QA synthetic second-manuscript snapshot'},
    sources:{'paper.tex':{text:'First original line.\nSecond original line.\n',sha256:'QA-source'}},
    comments:[['R1-01','Reviewer-C','C.1'],['SECOND-02','Reviewer-A','A.9']].map(([id,reviewer,reportLabel],i)=>({
      id,reviewer,reportOrder:i+1,reportLabel,title:'Second manuscript '+reviewer,original:'QA original '+reviewer,meaning:'QA 配置驱动的第二篇文章',
      authorReply:{text:'',decision:'pending',prefill:false,reason:'No prior author decision',sources:[]},assistant:{decision:'modify',reason:'QA recommendation'},recommendation:'QA independent manuscript recommendation',
      candidateVersion:'qa-manuscript-two-v1',locations:[{file:'paper.tex',lineStart:i+1,lineEnd:i+1,quote:i?'Second original line.':'First original line.',operation:i?'deletion':'verify',section:'QA section'}],proposals:[{locationIndex:0,operation:i?'deletion':'verify',text:''}]
    }))
  };
  const secondDataPath=path.join(manuscriptDir,'data.json'),secondHTML=path.join(manuscriptDir,'START_HERE.html');
  secondData.sources['paper.tex'].sha256=createHash('sha256').update(secondData.sources['paper.tex'].text).digest('hex');
  fs.writeFileSync(secondDataPath,JSON.stringify(secondData,null,2));fs.writeFileSync(path.join(manuscriptDir,'paper.tex'),secondData.sources['paper.tex'].text);
  const build=spawnSync(process.env.PYTHON||'python3',[path.join(repo,'revision_workbench/build.py'),'--data',secondDataPath,'--output',secondHTML,'--source-root',manuscriptDir],{encoding:'utf8'});
  await check('Same builder produces independent second manuscript without new dependencies',build.status===0&&fs.existsSync(secondHTML));
  if(build.status!==0||!fs.existsSync(secondHTML))throw new Error('Second manuscript build failed: '+build.stdout+' '+build.stderr);
  const manuscript=await newTab(undefined,pathToFileURL(secondHTML).href);
  report.secondManuscript={documentId:secondData.documentId,reviewers:secondData.reviewers,commentIds:secondData.comments.map(c=>c.id)};
  await check('Second manuscript shows generic metadata and exactly two comments in configured order',manuscript.eval(`document.title.includes('QA Second Manuscript')&&workbench.data.comments.length===2&&[...document.querySelectorAll('#comment-list [data-comment-id]')].map(el=>el.dataset.commentId).join(',')==='R1-01,SECOND-02'&&document.getElementById('list-count').textContent.includes('2 / 2')&&!document.getElementById('toggle-directory').textContent.includes('43')`));
  await check('Arbitrary three-reviewer metadata drives filter order and report labels',manuscript.eval(`(()=>{const options=[...document.getElementById('reviewer-filter').options].filter(o=>o.value!=='all');return options.map(o=>o.value).join(',')==='Reviewer-C,Reviewer-A,Reviewer-B'&&workbench.exportReport().includes('Reviewer C')&&workbench.exportReport().includes('Reviewer A')&&!document.querySelector('#workspace .card-kicker').textContent.includes('奥克兰')})()`));
  await manuscript.eval(`document.getElementById('reviewer-filter').value='Reviewer-A';document.getElementById('reviewer-filter').dispatchEvent(new Event('change'))`);
  await check('Generic reviewer filter selects the configured author without reordering',manuscript.eval(`[...document.querySelectorAll('#comment-list [data-comment-id]')].map(el=>el.dataset.commentId).join(',')==='SECOND-02'`));
  await manuscript.eval(`document.getElementById('reviewer-filter').value='all';document.getElementById('reviewer-filter').dispatchEvent(new Event('change'))`);
  await check('Generic portable backup contains complete second-manuscript metadata',manuscript.eval(`(()=>{const b=JSON.parse(workbench.exportBackup());return b.workbenchContext.dataset.documentId==='qa-independent-manuscript-two'&&b.workbenchContext.dataset.reviewers.length===3&&b.workbenchContext.records.length===2})()`));
  await check('Empty verification proposal is explicitly pending and never displayed as a deletion',manuscript.eval(`!document.querySelector('.proposal')&&!document.querySelector('[data-copy-proposal]')&&document.querySelector('.location .pending-note').textContent.includes('暂不改动')`));
  await manuscript.eval(`workbench.select('SECOND-02')`);
  await check('Explicit empty deletion alone is presented as deletion',manuscript.eval(`document.querySelector('.proposal pre').textContent==='（删除，不添加新文字）'&&document.querySelector('.operation').textContent==='删除'`));
  await manuscript.eval(`workbench.select('R1-01')`);
  const originalStorage=await first.eval('Object.entries(localStorage).filter(([key])=>key.startsWith(workbench.ledger.prefix))');
  await manuscript.eval(`for(const [k,v] of ${JSON.stringify(originalStorage)})localStorage.setItem(k,v);workbench.ledger.refresh()`);
  await check('Distinct document prefix ignores first manuscript operations even with reused record ID',manuscript.eval(`workbench.ledger.docId==='qa-independent-manuscript-two'&&workbench.ledger.get('R1-01','plan').value===undefined&&document.getElementById('plan').value===''`));
  await edit(manuscript,'#plan','QA manuscript2 notes only');
  const secondStorage=await manuscript.eval('Object.entries(localStorage).filter(([key])=>key.startsWith(workbench.ledger.prefix))');
  await first.eval(`for(const [k,v] of ${JSON.stringify(secondStorage)})localStorage.setItem(k,v);workbench.ledger.refresh()`);
  await check('Second-manuscript edits do not alter original project records',first.eval(`workbench.ledger.get('R1-01','plan').value==='QA parallel plan'&&!workbench.ledger.exportJSON().includes('QA manuscript2 notes only')`));
  const firstBackup=await first.readString('workbench.ledger.exportJSON()'),secondBackup=await manuscript.readString('workbench.ledger.exportJSON()');
  await manuscript.putString(firstBackup);await first.putString(secondBackup);
  await check('Second manuscript rejects foreign backup without changing its notes',manuscript.eval(`(()=>{const count=workbench.ledger.history().length;let rejected=false;try{workbench.ledger.importJSON(qaIncomingString)}catch(e){rejected=true}return rejected&&workbench.ledger.history().length===count&&workbench.ledger.get('R1-01','plan').value==='QA manuscript2 notes only'})()`));
  await check('Original manuscript rejects second-project backup without changing its notes',first.eval(`(()=>{const count=workbench.ledger.history().length;let rejected=false;try{workbench.ledger.importJSON(qaIncomingString)}catch(e){rejected=true}return rejected&&workbench.ledger.history().length===count&&workbench.ledger.get('R1-01','plan').value==='QA parallel plan'})()`));
  // Targeted regressions from the independent adversarial audit.
  await edit(manuscript,'#plan','keep');await manuscript.eval(`document.querySelector('[data-history=plan]').click()`);
  await check('Plan history preserves literal keep without decision-label substitution',manuscript.eval(`document.querySelector('#history-content .history-item pre').textContent==='keep'`));
  await manuscript.eval(`document.getElementById('close-history').click()`);
  await edit(manuscript,'#actualText','constructor');await manuscript.eval(`document.querySelector('[data-history=actualText]').click()`);
  await check('Actual-text history preserves literal constructor without inherited property lookup',manuscript.eval(`document.querySelector('#history-content .history-item pre').textContent==='constructor'`));
  await manuscript.eval(`document.getElementById('close-history').click()`);
  await edit(manuscript,'#actualText','QA verified revision A');
  await manuscript.eval(`document.getElementById('executionStatus').value='verified';document.getElementById('executionStatus').dispatchEvent(new Event('change'))`);
  await edit(manuscript,'#verificationNotes','QA verified notes A');
  await edit(manuscript,'#actualText','QA changed revision B');
  await check('Changing actual text invalidates prior verification without deleting its evidence',manuscript.eval(`workbench.state('R1-01').executionStatus==='not_started'&&workbench.state('R1-01').fields.executionStatus.raw.stale&&workbench.ledger.get('R1-01','executionStatus').value==='verified'&&workbench.state('R1-01').fields.verificationNotes.raw.stale&&workbench.ledger.get('R1-01','verificationNotes').value==='QA verified notes A'&&document.getElementById('workspace').textContent.includes('旧建议或旧文字')`));
  await manuscript.eval(`document.getElementById('executionStatus').value='verified';document.getElementById('executionStatus').dispatchEvent(new Event('change'));workbench.data.comments[0].candidateVersion+='-changed';workbench.refresh()`);
  await check('Changing candidate version also invalidates execution/verification claims',manuscript.eval(`workbench.state('R1-01').executionStatus==='not_started'&&workbench.state('R1-01').fields.executionStatus.raw.stale&&workbench.exportReport().includes('不作为当前核验')`));
  await edit(manuscript,'#plan','QA stable saved value before storage loss');
  await manuscript.eval(`window.qaLostHead=workbench.ledger.get('R1-01','plan').heads[0];localStorage.removeItem(workbench.ledger.prefix+qaLostHead);workbench.ledger.refresh()`);
  await check('Deleted real storage key becomes visibly unsaved while in-memory value survives',manuscript.eval(`workbench.ledger.status().unsavedOperations>0&&workbench.ledger.get('R1-01','plan').value==='QA stable saved value before storage loss'&&!document.getElementById('retry-save').hidden&&document.getElementById('save-status').textContent.includes('内存')`));
  await manuscript.eval(`document.getElementById('retry-save').click()`);
  await check('Explicit retry restores lost operation without replacing its history',manuscript.eval(`localStorage.getItem(workbench.ledger.prefix+qaLostHead)!==null&&workbench.ledger.status().unsavedOperations===0&&workbench.ledger.get('R1-01','plan').value==='QA stable saved value before storage loss'`));
  await manuscript.eval(`localStorage.setItem(workbench.ledger.prefix+qaLostHead,'{QA corrupt actual saved key');workbench.ledger.refresh();document.getElementById('retry-save').click()`);
  await check('Retry repairs known corrupted key while retaining exact corrupt bytes for recovery',manuscript.eval(`workbench.ledger.status().unsavedOperations===0&&workbench.ledger.exportJSON().includes('{QA corrupt actual saved key')&&workbench.ledger.get('R1-01','plan').value==='QA stable saved value before storage loss'`));
  await manuscript.eval(`window.qaOversized='QA over-limit exact draft\\n'+'x'.repeat(9*1024*1024)+'\\nEND QA';const el=document.getElementById('plan');el.focus();el.value=qaOversized;el.dispatchEvent(new Event('input',{bubbles:true}))`);
  await check('Rejected over-limit input remains exact in memory with rescue warning and no false saved claim',manuscript.eval(`workbench.state('R1-01').plan===qaOversized&&document.getElementById('plan').value===qaOversized&&workbench.ledger.get('R1-01','plan').value==='QA stable saved value before storage loss'&&!document.getElementById('rescue-drafts').hidden&&document.getElementById('warnings').textContent.includes('救出未保存文字')&&document.getElementById('save-status').textContent.includes('内存')`));
  await manuscript.eval(`workbench.select('SECOND-02');workbench.select('R1-01')`);
  await check('Navigating between comments retains the exact rejected draft',manuscript.eval(`document.getElementById('plan').value===qaOversized`));
  await check('Portable backup includes exact rejected draft independently of committed operations',manuscript.eval(`(()=>{const b=JSON.parse(workbench.exportBackup()),d=b.uncommittedDrafts.find(d=>d.recordId==='R1-01'&&d.field==='plan');return d.value===qaOversized&&b.operations.some(o=>o.field==='plan'&&o.value==='QA stable saved value before storage loss')})()`));
  const rejectedDraftPath=path.join(manuscriptDir,'qa-rejected-draft.json');fs.writeFileSync(rejectedDraftPath,await manuscript.readString('workbench.exportBackup()'));
  const restoredDraft=await newTab(undefined,pathToFileURL(secondHTML).href);await importLedgerFile(restoredDraft,rejectedDraftPath);
  await check('Import restores rejected draft without overwriting last valid committed notes',restoredDraft.eval(`document.getElementById('plan').value.length===9*1024*1024+'QA over-limit exact draft\\n'.length+'\\nEND QA'.length&&document.getElementById('plan').value.startsWith('QA over-limit exact draft\\n')&&document.getElementById('plan').value.endsWith('\\nEND QA')&&workbench.ledger.get('R1-01','plan').value==='QA stable saved value before storage loss'&&!document.getElementById('rescue-drafts').hidden`));
  await edit(manuscript,'#plan','QA recovered valid notes');
  await check('A subsequent valid edit clears its failed draft while preserving normal persistence',manuscript.eval(`!workbench.state('R1-01').fields.plan.uncommitted&&workbench.ledger.get('R1-01','plan').value==='QA recovered valid notes'&&!(JSON.parse(workbench.exportBackup()).uncommittedDrafts||[]).some(d=>d.recordId==='R1-01'&&d.field==='plan')`));
  for (const client of clients) {
    report.runtimeErrors.push(...client.events.filter(e=>e.method==='Runtime.exceptionThrown').map(e=>e.params.exceptionDetails));
    report.externalRequests.push(...client.events.filter(e=>e.method==='Network.requestWillBeSent'&&!/^(file:|about:|data:)/.test(e.params.request.url)).map(e=>e.params.request.url));
  }
  await check('No uncaught runtime exceptions', report.runtimeErrors.length===0);
  await check('No external requests from the local app', report.externalRequests.length===0);
} catch (error) {
  report.fatal = String(error.stack || error);
} finally {
  for (const client of clients) {try {await client.send('Page.close');} catch {} client.close();}
  if (chrome) {chrome.kill('SIGTERM'); await sleep(100);}
  for (const dir of tempDirs) {try {fs.rmSync(dir,{recursive:true,force:true});}catch{}}
  if (profile) {try {fs.rmSync(profile, {recursive: true, force: true});} catch {}}
  report.completedAt = new Date().toISOString();
  report.passed = report.tests.filter(test=>test.passed).length;
  report.failed = report.tests.filter(test=>!test.passed).length + (report.fatal ? 1 : 0);
  fs.writeFileSync(path.join(evidence, 'browser_validation.json'), JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({passed:report.passed,failed:report.failed,fatal:report.fatal,screenshots:report.screenshots}));
  if (report.failed) process.exitCode=1;
}
