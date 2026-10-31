from pathlib import Path
import re,json
stage=Path(__file__).resolve().parent
root=Path('/Users/jollibear/Documents/tmp/phd thesis');s=(root/'Chapter_6/chap6.tex').read_text();label=s.index('\\label{tab:bp_metric_diagnostic}')
start=s.rfind('\\begin{table}',0,label);end=s.index('\\end{table}',label)+len('\\end{table}');old=s[start:end]
new=old.replace(' Best score is highlighted in bold, and the second-best is underlined.','')
new=re.sub(r'\\(?:textbf|underline)\{([+\-]?\d+(?:\.\d+)?)\}',r'\1',new)
assert re.findall(r'(?<!\w)[+\-]?\d+(?:\.\d+)?',old)==re.findall(r'(?<!\w)[+\-]?\d+(?:\.\d+)?',new)
(stage/'N07_TABLE_MARKUP_PROPOSAL.tex').write_text('% Proposal only. Source Chapter_6/chap6.tex, tab:bp_metric_diagnostic.\n% Removes cross-metric best/second-best numeric emphasis; keeps every value.\n'+new+'\n')
(stage/'evidence/N07_table_markup_check.json').write_text(json.dumps({'table_anchor':'tab:bp_metric_diagnostic','numeric_tokens_unchanged':True,'numeric_emphasis_removed':len(re.findall(r'\\(?:textbf|underline)\{([+\-]?\d+(?:\.\d+)?)\}',old)),'old':old,'proposed':new},indent=2))
p=(stage/'CANDIDATE_PACKET_C2_REINSERTED.md');t=p.read_text();t=t.replace('These are selected-and-revised passages','Bracketed no-addition markers denote omission alternatives, not quotations from manuscript; actual surrounding prose is displayed below each.\n\nThese are selected-and-revised passages')
t=t.split('\n## N07')[0]
t+='\n## N07 — Necessary metric-table typography synchronisation\n\nC1 flagged best/second-best numeric emphasis across r/cosine/MAE in metric-diagnostic summary rows. Those different scales do not supply a commensurate best ranking. Proposed table in `N07_TABLE_MARKUP_PROPOSAL.tex` removes numeric bold/underline and that caption sentence; source row labels remain. A regex check confirms every numeric token is unchanged. Assess this as a minimal formatting repair required by N01–N03, not a new experiment or re-ranked metric.\n\n```latex\n'+new+'\n```\n'
p.write_text(t)
print('Removed numeric emphasis wrappers',len(re.findall(r'\\(?:textbf|underline)\{([+\-]?\d+(?:\.\d+)?)\}',old)),'; all numeric tokens unchanged')
