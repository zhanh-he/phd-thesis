'use strict';
// Runs the real application's import registration and preflight helper in a
// small VM facade. All manuscript data/storage is synthetic; no browser opens.
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const crypto=require('node:crypto');
const Ledger=require('../ledger.js');
const root=path.join(__dirname,'..');
const app=fs.readFileSync(path.join(root,'app.js'),'utf8');
const sha=value=>crypto.createHash('sha256').update(value).digest('hex');
const evidence={startedAt:new Date().toISOString(),scope:'Actual app file-input handler + actual prepareDraftImport in Node VM; synthetic DOM, source data and memory storage only; no browser navigation.',runtime:process.version,sourceHashes:{app:sha(app),ledger:sha(fs.readFileSync(path.join(root,'ledger.js')))},cases:[]};
class MemoryStorage {
  constructor(){this.data=new Map();this.writes=0;}
  get length(){return this.data.size;}
  key(index){return [...this.data.keys()][index]??null;}
  getItem(key){return this.data.has(key)?this.data.get(key):null;}
  setItem(key,value){this.data.set(key,String(value));this.writes++;}
}
const docId='qa-app-import-preflight';
const data={schemaVersion:1,documentId:docId,edition:'Synthetic import QA',sourceBaseline:{label:'Synthetic source'},sources:{},comments:['QA-01','QA-02'].map((id,index)=>({id,reviewer:'QA',reportOrder:index+1,reportLabel:'QA '+(index+1),original:'Synthetic reviewer text',authorReply:{text:'Synthetic reply',decision:'pending'},candidateVersion:'qa-v1',sourceBindingVersion:'qa-source-v1',locations:[],recommendation:'Synthetic recommendation',assistant:{decision:'pending',reason:'Synthetic reason'},proposals:[]}))};
function extractFunction(name){
  const marker='function '+name+'(',start=app.indexOf(marker);
  assert.ok(start>=0,'Actual app must define '+name+' before import commits');
  // App declarations are intentionally one top-level declaration per line.
  // Include continuation lines until the next top-level declaration/handler.
  const next=app.slice(start+marker.length).search(/\n(?=(?:function |const |let |\$\(|if\(|window\.))/);
  return next<0?app.slice(start):app.slice(start,start+marker.length+next);
}
function fixture(){
  const storage=new MemoryStorage(),ledger=new Ledger({storage,docId,knownIds:['QA-01','QA-02']});
  ledger.set('QA-01','plan','existing exact plan\n\\cite{Original}');
  ledger.set('QA-02','actualText','existing actual text');
  const initial=JSON.parse(ledger.exportJSON());initial.knownContext={source:'existing metadata'};ledger.importJSON(JSON.stringify(initial));
  const drafts=new Map([['QA-01.plan',{documentId:docId,recordId:'QA-01',field:'plan',value:'existing unsaved draft\n  exact spaces',error:'prior failure',updatedAt:'2026-11-01T00:00:00.000Z',priorExtension:{keep:true}}]]);
  const extras=[{documentId:docId,recordId:'old-unknown',field:'futureField',value:'existing extra draft',future:'preserve'}];
  const toasts=[],handlers=new Map(),elements=new Map();let refreshes=0,importCalls=0;
  const originalImport=ledger.importJSON.bind(ledger);
  ledger.importJSON=text=>{importCalls++;return originalImport(text);};
  const $=id=>{if(!elements.has(id))elements.set(id,{hidden:false,value:'synthetic-file-input',addEventListener(type,handler){handlers.set(id+':'+type,handler);}});return elements.get(id);};
  const context=vm.createContext({ledger,data,uncommittedDrafts:drafts,extraDrafts:extras,refreshView(){refreshes++;},toast:message=>toasts.push(String(message)),$});
  const start=app.indexOf("$('import-ledger').addEventListener('change',async e=>{"),end=app.indexOf("$('download-import-source').onclick",start);
  assert.ok(start>=0&&end>start,'Could not find actual app import registration');
  const registration=app.slice(start,end);
  vm.runInContext('let rejectedImport=null;\n'+['prepareDraftImport','decisionVersion','portableDataset','backupJSON'].map(extractFunction).join('\n')+'\n'+registration+'\n;globalThis.readRejectedImport=()=>rejectedImport;globalThis.actualBackupJSON=backupJSON;',context,{filename:'actual-app-import-fragment.js'});
  function snapshot(){return JSON.stringify({storage:[...storage.data].sort(([a],[b])=>a.localeCompare(b)),writes:storage.writes,operations:ledger.history(),metadata:[...ledger.importMetadata],current:ledger.snapshot(),drafts:[...drafts],extras});}
  async function importFile(input){const text=typeof input==='string'?input:JSON.stringify(input);await handlers.get('import-ledger:change')({target:{files:[{text:async()=>text}]}});return text;}
  return {storage,ledger,drafts,extras,toasts,elements,context,snapshot,importFile,exportBackup:()=>context.actualBackupJSON(),get importCalls(){return importCalls;},get refreshes(){return refreshes;},readRejected:()=>context.readRejectedImport()};
}
function incoming(drafts){
  const ledger=new Ledger({storage:new MemoryStorage(),docId,knownIds:['QA-01','QA-02']});
  ledger.set('QA-01','plan','SHOULD NOT APPEAR AFTER REJECT');
  const input=JSON.parse(ledger.exportJSON());input.incomingUnknownExtension={nested:{exact:['future',false,3]}};
  if(drafts!==undefined)input.uncommittedDrafts=drafts;
  return input;
}
function check(name,fn){
  test(name,async()=>{try{const result=await fn();evidence.cases.push({name,pass:true,...result});}catch(error){evidence.cases.push({name,pass:false,error:String(error.stack||error)});throw error;}});
}
const goodDraft=(overrides={})=>({documentId:docId,recordId:'QA-02',field:'actualText',value:'incoming unsaved text\n\\textbf{Exact}\n',error:'value validation failed',updatedAt:'2026-11-01T01:02:03.000Z',...overrides});
async function rejectsAtomically(value){
  const f=fixture(),before=f.snapshot(),input=incoming(value),text=await f.importFile(input);
  assert.equal(f.importCalls,0,'Malformed app drafts must reject before invoking ledger.importJSON');
  assert.equal(f.snapshot(),before,'Storage bytes, operation/metadata ledger, fields and both draft stores must remain exact');
  assert.equal(f.refreshes,0);assert.ok(f.toasts.some(message=>message.includes('导入未合并')));
  assert.ok(!f.toasts.some(message=>message.startsWith('已合并导入')));
  assert.equal(f.readRejected(),text);assert.equal(f.elements.get('download-import-source').hidden,false);
  return {importCalls:0,persistentAndDraftStateExact:true,truthfulNotMerged:true};
}

check('NEW01 object draft container rejects before ledger import or any writes',()=>rejectsAtomically({}));
check('NEW01 null draft row rejects before ledger import or any writes',()=>rejectsAtomically([null]));
check('NEW01 later invalid row cannot partially mutate prepared draft maps',()=>rejectsAtomically([goodDraft(),null]));

const malformed=[
  ['null container',null],['string container','drafts'],['boolean row',[false]],['array row',[[]]],
  ['missing document ID',[goodDraft({documentId:undefined})]],['foreign document ID',[goodDraft({documentId:'other-manuscript'})]],
  ['numeric document ID',[goodDraft({documentId:7})]],['empty record ID',[goodDraft({recordId:''})]],
  ['numeric record ID',[goodDraft({recordId:7})]],['overlong record ID',[goodDraft({recordId:'a'.repeat(301)})]],
  ['control in record ID',[goodDraft({recordId:'QA\n01'})]],['missing field',[goodDraft({field:undefined})]],
  ['numeric field',[goodDraft({field:7})]],['empty field',[goodDraft({field:''})]],
  ['overlong field',[goodDraft({field:'f'.repeat(301)})]],['control in field',[goodDraft({field:'plan\u0000'})]],
  ['numeric value',[goodDraft({value:7})]],['null value',[goodDraft({value:null})]],
  ['object value',[goodDraft({value:{text:'invalid'}})]],['missing value',[goodDraft({value:undefined})]],
  ['numeric error',[goodDraft({error:7})]],['null error',[goodDraft({error:null})]],
  ['numeric updatedAt',[goodDraft({updatedAt:7})]],['invalid updatedAt',[goodDraft({updatedAt:'not an ISO timestamp'})]],
  ['non-ISO human date',[goodDraft({updatedAt:'January 1, 2026'})]]
];
for(const [label,value]of malformed)check('Malformed known draft structure: '+label,()=>rejectsAtomically(value));

check('Valid drafts preserve multiline text, optional omissions, unknown records/fields and future extensions',async()=>{
  const f=fixture();
  const unknown=JSON.parse('{"documentId":"'+docId+'","recordId":"future-reviewer.17","field":"future.field-name","value":"future exact text\\n\\\\LaTeX{}","__proto__":{"keep":"inert"},"constructor":{"keep":true},"futureNested":{"exact":[false,7,{"key":"value"}]}}');
  const rows=[goodDraft(),unknown,{documentId:docId,recordId:'QA-01',field:'futureKnownRecordField',value:''},{documentId:docId,recordId:'r'.repeat(300),field:'f'.repeat(300),value:'boundary-length unknown ID/field',error:'',updatedAt:'2026-11-01T01:02:03+08:00'}];
  const input=incoming(rows);await f.importFile(input);
  assert.equal(f.importCalls,1);assert.ok(f.toasts.some(message=>message.startsWith('已合并导入')));
  assert.ok(!f.toasts.some(message=>message.includes('导入未合并')));assert.equal(f.readRejected(),null);
  const all=[...f.drafts.values(),...f.extras];
  for(const row of rows)assert.ok(all.some(saved=>JSON.stringify(saved)===JSON.stringify(row)),'Draft and all unknown extensions must remain exact');
  assert.equal(f.drafts.get('QA-01.plan').value,'existing unsaved draft\n  exact spaces');
  assert.ok(f.extras.some(row=>row.recordId==='old-unknown'));
  const exported=JSON.parse(f.ledger.exportJSON());
  assert.ok(exported.recovery.importedMetadata.some(meta=>JSON.stringify(meta.metadata.incomingUnknownExtension)===JSON.stringify(input.incomingUnknownExtension)));
  assert.ok(exported.recovery.importedMetadata.some(meta=>JSON.stringify(meta.metadata.uncommittedDrafts)===JSON.stringify(rows)));
  const actualBackup=f.exportBackup();
  for(const row of rows)assert.ok(JSON.parse(actualBackup).uncommittedDrafts.some(saved=>JSON.stringify(saved)===JSON.stringify(row)));
  const restored=fixture();await restored.importFile(actualBackup);
  assert.equal(restored.importCalls,1);const restoredRows=[...restored.drafts.values(),...restored.extras];
  for(const row of rows)assert.ok(restoredRows.some(saved=>JSON.stringify(saved)===JSON.stringify(row)));
  return {validDraftsExact:true,unknownIdsFieldsAndKeysPreserved:true,roundtripExact:true};
});

check('Valid conflicting draft stays as an extra without replacing the existing unsaved text',async()=>{
  const f=fixture(),row=goodDraft({recordId:'QA-01',field:'plan',value:'conflicting new draft\nretain both',futureExtension:{notDiscarded:true}});
  await f.importFile(incoming([row]));
  assert.equal(f.importCalls,1);assert.equal(f.drafts.get('QA-01.plan').value,'existing unsaved draft\n  exact spaces');
  assert.ok(f.extras.some(saved=>JSON.stringify(saved)===JSON.stringify(row)));
  return {bothDraftVersionsRetained:true};
});

check('Ledger-level rejection after valid draft preparation does not commit prepared draft maps',async()=>{
  const f=fixture(),before=f.snapshot(),input=incoming([goodDraft()]);input.schemaVersion=2;input.minReaderVersion=2;
  await f.importFile(input);
  assert.equal(f.importCalls,1);assert.equal(f.snapshot(),before);
  assert.ok(f.toasts.some(message=>message.includes('导入未合并')));
  return {preparedDraftsNotCommittedAfterLedgerRejection:true};
});

test.after(()=>{
  evidence.completedAt=new Date().toISOString();evidence.summary={passed:evidence.cases.filter(row=>row.pass).length,failed:evidence.cases.filter(row=>!row.pass).length,browserNavigation:false,realAuthorDataOrStorageTouched:false};
  fs.writeFileSync(path.join(root,'evidence/import_preflight.json'),JSON.stringify(evidence,null,2)+'\n');
});
