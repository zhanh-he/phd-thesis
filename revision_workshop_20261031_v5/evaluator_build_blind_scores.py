"""Freeze evaluator cycle-1 decisions before revealing candidate provenance."""
from pathlib import Path
import datetime,hashlib,json,re

ROOT=Path('/Users/jollibear/Documents/tmp/phd thesis')
SHARED=ROOT/'revision_workshop_20261031_v5'
LOCAL=Path(__file__).resolve().parent
packet=SHARED/'CANDIDATE_PACKET_BLIND_C1.md'
sha=lambda data:hashlib.sha256(data).hexdigest()

# R,V,C,N,Q,L = reviewer response, voice, cohesion, necessity, readability, length.
# Numbers are ordinal judgements, not measurable effect sizes or summed scores.
S={
'T01':[
 ('K','P',[3,4,4,4,4,4],'Clear data/learning distinction; unavailable reliable labels also covers unreliable labels, but overlap is left implicit.'),
 ('L','P',[4,4,4,4,4,4],'Constant/coarsely quantised velocities are concrete; renderer example and overlapping conditions answer the actual definitional need.'),
 ('M','P',[4,3,3,2,3,2],'Defines extra incomplete term and adds quality-of-performance disclaimer; useful content but 79 words over-expands the two requested definitions.'),
 ('N','P',[1,4,2,2,3,4],'No addition preserves brevity but leaves weakly expressive/weakly supervised undefined at the central question.')],
'T02':[
 ('K','P',[4,4,4,4,4,4],'Directly maps Chapter 6 to S2, preserves aligned notes, and distinguishes future audio-only velocity from score-dynamics S3.'),
 ('L','P',[3,4,4,4,4,4],'Specific and concise; relies on existing table for S3 target and does not explicitly name S2 extension under weaker supervision.'),
 ('M','P',[4,3,3,3,3,3],'Correctly distinguishes target from input, but repeats score-dynamics/table facts in a 63-word insertion.'),
 ('N','P',[1,4,2,2,3,4],'Existing table lacks the Chapter 6 relationship raised by the examiner.')],
'T03':[
 ('K','P',[4,3,3,3,3,2],'Explains scalar versus RGB and regular grid, but convolution/skip-connection explanation duplicates nearby architecture and stretches the paragraph.'),
 ('L','P',[1,3,3,2,3,2],'Keeps image-based/colourisation analogy without resolving single-channel versus colour prediction or the representation choice.'),
 ('M','P',[4,4,4,4,4,4],'Clear model-interface rationale and input/output distinction; no claim that event representations were outperformed.'),
 ('N','P',[4,4,4,4,4,4],'Regular grid, binary structure, scalar output and window attention are explained in order; strongest direct explanation of the analogy.')],
'T04':[
 ('K','P',[4,4,3,3,4,4],'Addresses joint modelling and states no note-detection benefit was tested, but trusted-note premise repeats preceding text.'),
 ('L','P',[2,4,4,3,4,4],'No addition avoids repeated scope; existing use cases remain useful, but the joint-modelling question remains only implicit.'),
 ('M','P',[4,2,2,2,3,2],'Two defensive negations repeat scope already stated; correct but excessively explanatory for this position.'),
 ('N','P',[3,4,3,3,4,4],'Readable application boundary, but does not explicitly say the reported evaluation cannot assess note-detection gains.')],
'T05':[
 ('K','P',[3,4,4,4,4,4],'Explicit transition supervision is a valid design reason; does not make comparison to deriving transitions from level output explicit.'),
 ('L','P',[4,4,3,3,4,3],'Answers the alternative directly, but final modelling-new-region clause repeats the target definition.'),
 ('M','P',[4,4,4,4,4,4],'Acknowledges level-transition alternative then distinguishes explicit boundary/state targets without an untested improvement claim.'),
 ('N','P',[2,4,4,3,4,4],'Existing definitions say what a change point is but not why a separate head is used.')],
'T06':[
 ('K','P',[3,3,3,3,3,2],'More direct is not a cost claim, but target-adaptation wording and reduces-dependence language are less exact than no target labels.'),
 ('L','P',[4,4,4,4,4,4],'Piano-pretraining, real target audio, absent velocity labels and renderer limitation are clear without efficiency superiority.'),
 ('M','P',[4,4,4,4,4,4],'Equally safe short method account; does not restate piano pretraining, which preceding chapter context already supplies.'),
 ('N','F',[1,2,2,1,3,2],'Simpler route is unmeasured; avoids synthesis-to-performance domain gap conflicts with the continuing renderer-mismatch limitation.')],
'T07':[
 ('K','P',[2,3,3,3,3,3],'Conditional can become dominated is a plausible risk, but does not state the actual response: fidelity and gradient accuracy not separately measured.'),
 ('L','P',[4,3,4,3,4,3],'Faithfulness is properly separated from velocity response and cause is not isolated; 64 words include an unnecessary exact-reproductions contrast.'),
 ('M','P',[4,4,4,4,4,4],'Keeps observed degradation, possible mismatch and the two unmeasured properties in 41 concrete words.'),
 ('N','F',[2,3,2,2,3,3],'Which part of that mismatch caused the degradation presupposes a mismatch cause that the experiment did not isolate.')],
'T08':[
 ('K','P',[4,3,3,3,3,2],'Accurate four-paper map verified against declaration, but duplicates a readily available declaration and following roadmap.'),
 ('L','P',[4,4,4,4,4,4],'Based on four co-authored studies plus specific cross-chapter synthesis answers the distinction without claiming exhaustive novelty.'),
 ('M','P',[3,4,4,4,4,4],'Compact and concrete synthesis description; presented and co-authorship details make adaptation less explicit than based on studies.'),
 ('N','P',[2,3,3,3,3,4],'Original only names Chapters 3–5 and does not specify what the thesis synthesis contributes.')],
'T09':[
 ('K','P',[3,4,3,3,4,4],'Tested piano/guitar scope and untested sustained instruments are clear, but captured labels versus dynamics agreement could be more exact.'),
 ('L','P',[4,4,3,4,4,4],'Most economical account of direct piano labels, renderer-conditioned guitar evaluation and untested sustained controls; restore Second for enumeration.'),
 ('M','P',[2,2,3,2,3,2],'Original defensive belief-that-piano-is-universal clause adds no scope information and still does not name untested instruments.'),
 ('N','P',[4,3,3,3,4,3],'Accurate and complete but target-coordinates wording and label discussion are longer than necessary; restore Second.')],
'T10':[
 ('K','P',[4,3,4,3,4,3],'Correct supporting evidence and descriptive composer grouping, but repeats lowest-rating result at the end and generic earlier findings is vague.'),
 ('L','P',[4,4,4,4,4,3],'Careful higher mean ratings and selected SMD/PianoTeq scope; 61 words retain all needed limits without statistical significance claim.'),
 ('M','F',[1,2,2,1,3,2],'Relatively narrow group confidence intervals do not establish participant consistency; clearly outperforms broadens beyond reported mean similarities.'),
 ('N','P',[4,4,4,4,4,4],'Short, factual means comparison and clear finite listening setting; composer groups do not isolate style, with no significance assertion.')],
'N01':[
 ('K','P',[4,3,4,3,3,2],'Correct numbers and no universal insensitivity claim; reads like a table transcription plus audit caveat.'),
 ('L','P',[4,4,4,4,4,4],'Preserves both metrics discriminating GT/flat and confines numerical-gap observation to this diagnostic.'),
 ('M','F',[1,2,2,1,3,3],'A numerical margin across different metrics does not prove cosine similarity insensitive to fine dynamics differences.'),
 ('N','F',[1,2,2,1,3,3],'Identical unsupported proving-insensitive inference; no score difference from M.')],
'N02':[
 ('K','F',[1,2,2,1,3,2],'SoundFont swap is not a gain-only intervention; raw MAE/r changes have different units and cannot prove over-sensitivity.'),
 ('L','F',[1,2,2,1,3,2],'Identical gain-only causal and noncommensurate-magnitude inference; no score difference from K.'),
 ('M','P',[4,4,4,4,4,3],'States table changes, labels the whole renderer intervention, and gives a positive contour-agreement reason for r.'),
 ('N','P',[3,4,4,4,4,4],'Concise and does not identify gain as sole cause, but supports-using-r can still sound like an uncalibrated cross-metric magnitude ranking.')],
'T11':[
 ('K','P',[3,4,4,4,4,4],'Mathematical reason is clear; awkward rather-than-establishing wording is less direct than the actual author statement.'),
 ('L','P',[4,4,4,4,4,4],'Matches actual response: smooth gradients near zero, L1-like large errors, and no established comparative advantage.'),
 ('M','P',[2,3,3,3,3,3],'Robust-loss rationale is plausible but does not explain Huber versus MAE smoothing; second half discusses parameter space instead of loss form.'),
 ('N','U',[3,4,3,3,4,4],'We did not conduct a dedicated comparison goes beyond have not established advantage through a dedicated comparison; experiment history not independently known.')],
'N03':[
 ('K','F',[1,2,2,1,3,3],'Cosine similarity and MAE fail turns a limited diagnostic into an unsupported general metric verdict.'),
 ('L','P',[4,4,4,4,4,4],'Names rendered loudness-contour agreement, positive within-piano diagnostic and complementary metrics; no physical-velocity truth claim.'),
 ('M','P',[4,4,4,4,4,4],'Clear present-task choice and complementary metrics; does not explicitly flag transfer from piano diagnostic to guitar evaluation.'),
 ('N','F',[1,2,2,1,3,3],'Identical fail-on-sensitivity/robustness claim; no score difference from K.')],
'N04':[
 ('K','F',[1,3,2,1,4,4],'Unqualified is dominated upgrades a possible mechanism into universal gradient dominance.'),
 ('L','F',[1,3,2,1,4,4],'Identical unconditional gradient-dominance claim; no score difference from K.'),
 ('M','P',[3,4,4,4,4,4],'Can be influenced is safe but weak and generic; loses why the renderer condition matters.'),
 ('N','P',[4,4,4,4,4,4],'Conditional renderer mismatch and velocity-relevant differences preserve the mechanism as a risk, not a measured causal result.')],
}
RANKS={
'T01':[['L'],['K'],['M'],['N']], 'T02':[['K'],['L'],['M'],['N']],
'T03':[['N'],['M'],['K'],['L']], 'T04':[['K'],['N'],['L'],['M']],
'T05':[['M'],['L'],['K'],['N']], 'T06':[['L'],['M'],['K'],['N']],
'T07':[['M'],['L'],['K'],['N']], 'T08':[['L'],['M'],['K'],['N']],
'T09':[['L'],['N'],['K'],['M']], 'T10':[['N'],['L'],['K'],['M']],
'N01':[['L'],['K'],['M','N']], 'N02':[['M'],['N'],['K','L']],
'T11':[['L'],['K'],['M'],['N']], 'N03':[['L'],['M'],['K','N']],
'N04':[['N'],['M'],['K','L']],
}

blocks=re.split(r'(?m)^## (?=[TN]\d\d\s*$)',packet.read_text())[1:]
rows=[]
for block in blocks:
    ident=block.splitlines()[0].strip()
    texts=dict(re.findall(r'### ([TN]\d\d-[KLMN])\s*\n+```latex\n(.*?)\n```',block,re.S))
    assert len(texts)==4
    for letter,gate,scores,reason in S[ident]:
        cid=f'{ident}-{letter}'
        rows.append(dict(id=cid,passage=ident,semantic_gate='PASS',
            factual_gate={'P':'PASS','F':'FAIL','U':'UNRESOLVED'}[gate],
            eligible=gate=='P',scores=scores,reason=reason,
            candidate_sha256=sha(texts[cid].encode()),word_count_diagnostic=len(texts[cid].split())))
assert len(rows)==60 and len(set(r['id'] for r in rows))==60
out=dict(stage='Frozen before provenance reveal',
    frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    blind_limit='Provenance labels concealed; evaluator already knows some original source wording and may recognise it. This is not double-blind.',
    packet_sha256=sha(packet.read_bytes()),
    dimensions=['reviewer_response','author_voice','local_full_cohesion','minor_revision_necessity','readability','length_information_density'],
    scale='Ordinal 1–4 frozen source-only rubric; no sums, means or quality percentages. Scores for non-PASS candidates are diagnostic only and never override exclusion.',
    candidates=rows,
    rankings={k:[[f'{k}-{i}' for i in tier] for tier in tiers] for k,tiers in RANKS.items()},
    blockers=['Formal source baseline unresolved','run/GT provenance unresolved','R1-13/21/26/30 remain evidence-pending'],
    outside_subset_keep=['Current Fig.6.2 SoundFont-rendered target caption','Current local V^(0)/Vhat explanation','Detailed O/F/V input-target-mask roles; do not compress into vague prose'],
)
(LOCAL/'evaluator_cycle1_blind_rankings.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
lines=['# Cycle 1: provisional anonymous ranking frozen before reveal','','Scores follow the evaluator’s previously frozen six-axis 1–4 rubric, not the packet’s 0–3 rubric. No composite totals. R/V/C/N/Q/L = response / voice / cohesion / necessity / readability / length. A hard gate excludes even stylistically strong text.','',out['blind_limit'],'']
for ident in S:
    lines+=['## '+ident,'','Preference tiers: '+' > '.join(' = '.join(t) for t in out['rankings'][ident]),'', '| Candidate | Factual gate | R/V/C/N/Q/L | Text-specific reason |','| --- | --- | --- | --- |']
    for row in [r for r in rows if r['passage']==ident]:
        lines.append(f"| {row['id']} | {row['factual_gate']} | {'/'.join(map(str,row['scores']))} | {row['reason']} |")
    lines.append('')
lines+=['## KEEP and limitations','','No unchanged disputed paragraph wins this selected subset as supplied. That is a result of these specific ambiguities, not a presumption that new text is superior. Fig.6.2, local V^(0)/Vhat notation and concrete O/F/V definitions should remain unchanged. Several compact alternatives are tied on ordinal scores; the tier order reflects text-specific preference, not measurable quality differences.','','T04 winner still needs reinsertion editing to avoid repeating trusted-note scope. T09 needs Second restored for the First/Third sequence. T11-N is unresolved rather than known false: lack of established advantage does not establish the full history of attempted comparisons. The baseline evaluator’s own earlier suggested did-not-conduct phrasing was also too categorical and should be superseded by the actual response.','','Frozen UTC: '+out['frozen_utc'],'Packet SHA-256: '+out['packet_sha256']]
(LOCAL/'evaluator_cycle1_provisional.md').write_text('\n'.join(lines)+'\n')
print('Saved 60 candidate scores and 15 pairwise rankings before reveal.')
print('Hard gates:',{s:sum(r['factual_gate']==s for r in rows) for s in ['PASS','FAIL','UNRESOLVED']})
