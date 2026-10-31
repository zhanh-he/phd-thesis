# Ch.5 已保存输出与核对附件

输出于 2026-10-22 提取，说明于 2026-10-31 精简。这里保留已有 notebook 输出及其算术汇总，供新版 blueprint 查证；不是论文实验复现，也不是新的正式结果。

## 来源和范围

原仓库 `zhanh-he/piano-dynamic-estimation`，固定 commit `b80be9b355dd28c2a710a3839f63dbbf6d4a9471`。主要输入为 [CrossEval.ipynb](input_snapshot/eval_and_benchmarks/CrossEval.ipynb) 的已保存 stdout，原文件 SHA256 为 `295aa1288f1ffae987c10d64c3928f9bbe00cc338858916e6540bec2e1efe61c`。各输入的固定链接、大小与 hash 见 [manifest](input_snapshot/manifest.json)。

脚本读取 100 个已保存 metric dictionaries，提取 200 个值，形成 40 个完整五折组；没有执行 notebook、加载模型或从逐录音预测重新计算 F1。保存指标已舍入，五折均值不是 pooled F1，五折标准差也不是总体置信区间。

## 值得核对的差异

- 旧版 Table 5.4 的 32 个相关显示值全部匹配保存输出的各任务最大值；按正文所写的多任务共同 dynamic-best fold 规则，仅 22 项匹配。比如 Vienna / MultiTaskCNN / BSSL 的 dynamic-best fold 输出为 `0.3196 / 0.2125 / 0.7373 / 0.2696`，旧表为 `32.0 / 29.8 / 73.8 / 29.3`。尚需确定实际表格来源及汇总规则。
- 保存的 [evaluator.py](input_snapshot/pytorch/evaluator.py) 使用 weighted F1，旧正文公式定义 macro-F1。不能由这些聚合分数重建 macro-F1，也不能自动把公开版本认作论文最终运行。
- [beat_postproc.py](input_snapshot/pytorch/post_processor/beat_postproc.py) 有条件地将 downbeat 吸附到预测 beat；训练 loss 无显式一致性项与 decoding 有连接可以同时成立。评估网格、CPt 阈值和类别处理也需按实际评估版本解释。

上述差异是查证线索，不是新增实验要求。旧论文定位：§5.6.1、§5.6.3、§5.7.3 / Table 5.4；版本身份见[关键核查与证据](../关键核查与证据.md)。

## 附件

- [extract_and_summarise.py](extract_and_summarise.py)：仅依赖标准库的提取与汇总脚本，按自身路径寻找输入。
- [saved_checkpoint_records.csv](saved_checkpoint_records.csv)：100 条保存记录及 checkpoint、fold、cell 来源。
- [saved_per_fold_metrics.csv](saved_per_fold_metrics.csv)：200 条指标。
- [all_fold_summary.csv](all_fold_summary.csv)：40 组描述性统计，含样本标准差 `ddof=1`。
- [v0_table5_4_comparison.csv](v0_table5_4_comparison.csv)：32 项旧表值与两种汇总规则的对照；旧表值是转录输入。
- [validation.json](validation.json)：既有完整性和匹配计数。

需复核时，从仓库根目录运行：

```bash
python3 "02_Ultra_细节/Ch5_现有输出汇总/extract_and_summarise.py"
```

输入快照、脚本、CSV 和验证记录本次均按原样保留。
