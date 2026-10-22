#!/usr/bin/env python3
"""Extract saved CrossEval notebook stdout; never import or run project code.

Stdlib only. Run from any directory: python3 /absolute/path/extract_and_summarise.py
All values are already rounded, saved metrics. This is arithmetic aggregation,
not inference, retraining, recalculation of F1, or reconstruction from predictions.
"""
from pathlib import Path
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
import ast
import csv
import hashlib
import json
import re
import statistics

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT / 'input_snapshot/eval_and_benchmarks/CrossEval.ipynb'
MANIFEST = json.loads((ROOT / 'input_snapshot/manifest.json').read_text())
COMMIT = MANIFEST['commit']
METRICS = ('dynamic_f1', 'change_point_f1', 'beat_f1', 'downbeat_f1')

def write_csv(name, records):
    if not records:
        raise ValueError(name + ' has no records')
    with (ROOT / name).open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(records[0]))
        w.writeheader()
        w.writerows(records)

def rounded_percent(value):
    return Decimal(str(value)).scaleb(2).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

def main():
    expected_hash = next(x['sha256'] for x in MANIFEST['files']
                         if x['path'] == 'eval_and_benchmarks/CrossEval.ipynb')
    assert hashlib.sha256(NOTEBOOK.read_bytes()).hexdigest() == expected_hash
    nb = json.loads(NOTEBOOK.read_text())
    checkpoint_rows, metric_rows = [], []
    for cell_index, cell in enumerate(nb['cells']):
        if cell['cell_type'] != 'code':
            continue
        source = ''.join(cell.get('source', []))
        if not source.startswith('# ====='):
            continue
        dataset = 'Vienna4x22' if 'Vienna4x22' in source.splitlines()[0] else 'Batik-plays-Mozart'
        method = 'MultiTaskCNN' if 'MultiTaskCNN' in source.splitlines()[0] else 'SingleCNN'
        feature = 'BSSL' if 'BSSL' in source.splitlines()[0] else 'LogMel'
        # Use stream outputs only, not the manually written markdown tables.
        stdout = ''.join(''.join(o.get('text', [])) for o in cell.get('outputs', [])
                         if o.get('output_type') == 'stream')
        current_fold = None
        current_task = None
        current_checkpoint = None
        for line in stdout.splitlines():
            task_match = re.search(r'>>> .*?\[([a-z_]+)\]', line)
            if task_match:
                current_task = task_match.group(1)
            export_match = re.search(r'^\[(epoch_[^\]]+\.pth)\] Exported (\d+) file\(s\) under (.+)-fold(\d+)/', line)
            if export_match:
                current_checkpoint = export_match.group(1)
                current_fold = int(export_match.group(4))
                expected_files = 88 if dataset == 'Vienna4x22' else 36
                assert int(export_match.group(2)) == expected_files
            result_match = re.match(r'^(epoch_\S+\.pth) -> (\{.*\})$', line)
            if not result_match:
                continue
            assert current_fold is not None
            assert result_match.group(1) == current_checkpoint
            metrics = ast.literal_eval(result_match.group(2))
            if method == 'SingleCNN':
                assert current_task is not None
                assert current_task + '_f1' in metrics
            else:
                assert all(m in metrics for m in METRICS)
            checkpoint_rows.append(dict(dataset=dataset, method=method, feature=feature,
                                        task=current_task or 'multitask', fold=current_fold,
                                        checkpoint=current_checkpoint, notebook_cell_index=cell_index,
                                        notebook_execution_count=cell.get('execution_count'),
                                        saved_metrics=json.dumps(metrics, sort_keys=True)))
            for metric, value in metrics.items():
                assert 0 <= value <= 1
                metric_rows.append(dict(dataset=dataset, method=method, feature=feature,
                                        fold=current_fold, metric=metric, saved_value=value,
                                        checkpoint=current_checkpoint, notebook_cell_index=cell_index))

    assert len(checkpoint_rows) == 100, len(checkpoint_rows)
    assert len(metric_rows) == 200, len(metric_rows)  # Includes 40 coarse-dynamic values.
    groups = defaultdict(list)
    for row in metric_rows:
        groups[(row['dataset'], row['method'], row['feature'], row['metric'])].append(row)
    for key, rows in groups.items():
        assert sorted(r['fold'] for r in rows) == [0, 1, 2, 3, 4], key
    assert len(groups) == 40

    summaries = []
    for key, rows in sorted(groups.items()):
        values = [r['saved_value'] for r in rows]
        best = max(rows, key=lambda x: x['saved_value'])
        dataset, method, feature, metric = key
        summaries.append(dict(dataset=dataset, method=method, feature=feature, metric=metric,
                              n_folds=5, mean=statistics.mean(values),
                              sample_std_ddof1=statistics.stdev(values),
                              population_std_ddof0=statistics.pstdev(values),
                              minimum=min(values), maximum=max(values), max_fold=best['fold'],
                              mean_percent=100*statistics.mean(values),
                              sample_std_percent=100*statistics.stdev(values)))

    # Manual transcription from v0 Table 5.4 p.80 / PDF107, in %.
    # This block is input evidence, not scores recalculated from the notebook.
    thesis = {
        ('Vienna4x22', 'SingleCNN', 'BSSL'): [32.6,26.6,74.2,33.2],
        ('Vienna4x22', 'SingleCNN', 'LogMel'): [31.5,34.7,74.0,21.5],
        ('Vienna4x22', 'MultiTaskCNN', 'BSSL'): [32.0,29.8,73.8,29.3],
        ('Vienna4x22', 'MultiTaskCNN', 'LogMel'): [38.2,36.7,74.5,27.3],
        ('Batik-plays-Mozart', 'SingleCNN', 'BSSL'): [53.9,20.2,40.0,16.7],
        ('Batik-plays-Mozart', 'SingleCNN', 'LogMel'): [54.3,14.1,38.6,13.3],
        ('Batik-plays-Mozart', 'MultiTaskCNN', 'BSSL'): [53.0,14.3,39.2,15.1],
        ('Batik-plays-Mozart', 'MultiTaskCNN', 'LogMel'): [50.2,14.3,37.8,13.9],
    }
    comparisons = []
    for group, thesis_values in sorted(thesis.items()):
        dataset, method, feature = group
        dynamic_rows = groups[(dataset, method, feature, 'dynamic_f1')]
        dynamic_best_fold = max(dynamic_rows, key=lambda x: x['saved_value'])['fold']
        for metric, thesis_percent in zip(METRICS, thesis_values):
            rows = groups[(dataset, method, feature, metric)]
            best = max(rows, key=lambda x: x['saved_value'])
            common = next(x for x in rows if x['fold'] == dynamic_best_fold)
            rule_value = common if method == 'MultiTaskCNN' else best
            comparisons.append(dict(dataset=dataset,method=method,feature=feature,metric=metric,
                                    thesis_percent=thesis_percent,
                                    per_metric_max_percent=float(rounded_percent(best['saved_value'])),
                                    per_metric_max_fold=best['fold'],dynamic_best_fold=dynamic_best_fold,
                                    common_dynamic_fold_percent=float(rounded_percent(common['saved_value'])),
                                    stated_rule_percent=float(rounded_percent(rule_value['saved_value'])),
                                    matches_per_metric_max=Decimal(str(thesis_percent)) == rounded_percent(best['saved_value']),
                                    matches_stated_rule=Decimal(str(thesis_percent)) == rounded_percent(rule_value['saved_value'])))

    write_csv('saved_checkpoint_records.csv', checkpoint_rows)
    write_csv('saved_per_fold_metrics.csv', metric_rows)
    write_csv('all_fold_summary.csv', summaries)
    write_csv('v0_table5_4_comparison.csv', comparisons)
    result = dict(commit=COMMIT, notebook_sha256=expected_hash,
                  saved_stdout_metric_dicts=len(checkpoint_rows),
                  saved_per_fold_metric_values=len(metric_rows),
                  groups_including_coarse=len(groups),
                  complete_five_fold_groups=True,
                  table_primary_entries=len(comparisons),
                  table_entries_matching_per_metric_max=sum(x['matches_per_metric_max'] for x in comparisons),
                  table_entries_matching_stated_rule=sum(x['matches_stated_rule'] for x in comparisons),
                  missing_raw_predictions=True,
                  interpretation='Arithmetic aggregation of saved rounded notebook stdout; not F1 recomputation or inference; v0 run identity unconfirmed.')
    (ROOT / 'validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
