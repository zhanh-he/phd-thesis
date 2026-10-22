# Chapter 5：公开 notebook 已保存输出的轻量汇总

2026-10-22。本目录完成了**已保存指标的提取与算术汇总**：没有执行项目 notebook、没有加载 checkpoint、没有训练或新推理，也没有从逐录音预测重新计算 F1。该结果取代本轮较早的“尚未找到可用各 fold 输出”状态，但不构成 v0 实验复现。

## 输入与可复核范围

公开原作者仓库：[piano-dynamic-estimation](https://github.com/zhanh-he/piano-dynamic-estimation)，固定 commit `b80be9b355dd28c2a710a3839f63dbbf6d4a9471`。读取 GitHub 完整 tree 后，只取小文本文件，没有 clone、下载数据集或权重。保存了 [输入 manifest](input_snapshot/manifest.json)，每个原文件包含 SHA256、bytes 和固定 commit 链接。

主要输入是 [CrossEval.ipynb 固定版本](https://github.com/zhanh-he/piano-dynamic-estimation/blob/b80be9b355dd28c2a710a3839f63dbbf6d4a9471/eval_and_benchmarks/CrossEval.ipynb)：SHA256 `295aa1288f1ffae987c10d64c3928f9bbe00cc338858916e6540bec2e1efe61c`。程序只提取 code cells 4、5、7、8、10、11、13、14 中已保存的 stdout，**不以 notebook 开头手写表格作为计算输入**。cell index 从 0 开始。

共找到 100 个带 checkpoint 文件名的已保存 metric dictionaries：多任务 20 个；单任务 80 个（每一目标独立模型）。覆盖 2 数据集 × 2 feature × 2 method × 5 folds 的四个主要任务，以及附带 coarse dynamics。总计 200 个已保存 metric values，形成 40 个完整五折组，其中主要指标为 160 个值／32 组。每个输出前的 Exported 行包含 fold、checkpoint 和 88 个 Vienna／36 个 Batik 文件计数。它支持追踪已保存运行输出，但**不等于已取得这 124 个文件的原始预测**。

## 最重要的新结论

**已由代码/数据确认（公开保存输出）：** v0 Table 5.4 中自有四种 method/feature 在两个外部数据集的 32 个主要指标，全部与这些保存输出的“各任务分别取 max fold”相同（按百分数一位小数显示）。如果按 v0 §5.6.1／§5.7.3 所写“多任务按 dynamic F1 选一个 fold，其他任务取同一 checkpoint”，只有 22/32 个显示值相符；其余 10 个均为多任务辅助指标。

一个最清楚的例子：MultiTaskCNN + BSSL 在 Vienna 的 dynamic-best 是 fold 1，保存输出为 Dyn 0.3196、CPt 0.2125、Beat 0.7373、Dbt 0.2696；而 v0 表写 32.0、29.8、73.8、29.3。后三项来自各自的最大 fold（分别为 0、3、4），不是同一个 fold 1。主论文定位：`Zhanhong_He_PhD_Thesis_v0.pdf`，§5.6.1 印刷 p.75／PDF p.102，§5.7.3／Table 5.4 印刷 p.80／PDF p.107。

因此要分别说：**原文所声明的协议已确认；该表是否遵守协议，现有对照显示不一致，仍需正式 run-to-table mapping 解决。** 不得将公开保存输出自动认定为 v0 最终运行。两者数字全部对应是强烈的核查线索，而非训练版本身份的证明。无论选择哪种规则，target-label selection 的乐观性都存在。

**已由代码/数据确认（公开代码）：** `pytorch/evaluator.py:59–70` 的 fine dynamic F1 使用 `average="weighted"`；`pytorch/final_evaluation.py:181–184` 实际调用它产生 `dynamic_f1`。v0 Eq.5.12 印刷 p.77／PDF p.104 则定义五类 macro-F1。该函数也没有 `labels=[...]` 或显式去除 blank；reference-beat mask 不自动等于去除 blank，因此类别集合和 blank handling 要一并确认，不能据此猜实际有多少 blank。当前保存指标应保留字段名 `dynamic_f1` 并称“公开 notebook 保存指标”；在 v0 run 版本未核定前不能把它们改称已验证 macro-F1，也不能从这些汇总指标推算 macro-F1。[公开 evaluator 固定行](https://github.com/zhanh-he/piano-dynamic-estimation/blob/b80be9b355dd28c2a710a3839f63dbbf6d4a9471/pytorch/evaluator.py#L59-L70)、[final evaluation 调用](https://github.com/zhanh-he/piano-dynamic-estimation/blob/b80be9b355dd28c2a710a3839f63dbbf6d4a9471/pytorch/final_evaluation.py#L181-L184)。

**已由代码/数据确认（公开代码）：** loss 是各任务项相加，没有 beat/downbeat 一致性 loss；但 minimal post-processing 在存在 predicted beats 时，把 predicted downbeats 移到最近 predicted beat 并去重。`final_evaluation.py:72` 固定选 `minimal`，`:114–120` 把预测的 beat/downbeat logits 一起传入，`post_processor/beat_postproc.py:139–147` 执行 snapping。单任务 downbeat 缺少 beat head 时传零 logits，或没有 beat peaks 时会跳过 snapping。故“训练共享且无显式一致性 loss”成立；“整个实现无显式输出一致性处理”不成立。v0 是否实际使用该代码仍待运行记录对应。[loss 聚合](https://github.com/zhanh-he/piano-dynamic-estimation/blob/b80be9b355dd28c2a710a3839f63dbbf6d4a9471/pytorch/losses.py#L164-L203)、[minimal 选择和调用](https://github.com/zhanh-he/piano-dynamic-estimation/blob/b80be9b355dd28c2a710a3839f63dbbf6d4a9471/pytorch/final_evaluation.py#L68-L120)、[snapping 分支](https://github.com/zhanh-he/piano-dynamic-estimation/blob/b80be9b355dd28c2a710a3839f63dbbf6d4a9471/pytorch/post_processor/beat_postproc.py#L125-L148)。

补充协议核查：公开 `inference.py:161–173` 的 practical derived CPt 使用 logit threshold 1.0（注释称约 0.75 概率），但 `final_evaluation.py:198–205` 对 raw CPt logits 用 threshold 0.0；`dynamic_postproc.py:54–70` 直接按该阈值比较，意味着主 metric 与 practical 输出可能使用不同 CPt 阈值。v0 §5.5.2 印刷 p.73／PDF p.100 写 75%；须将最终运行使用的 metric/post-processing 版本一并核对，不能直接用 practical 分支替主评估背书。[practical 分支](https://github.com/zhanh-he/piano-dynamic-estimation/blob/b80be9b355dd28c2a710a3839f63dbbf6d4a9471/pytorch/inference.py#L161-L173)、[主 metric 分支](https://github.com/zhanh-he/piano-dynamic-estimation/blob/b80be9b355dd28c2a710a3839f63dbbf6d4a9471/pytorch/final_evaluation.py#L198-L205)。

## 五折汇总读法

下列只展示 dynamic_f1 的 compact view。单位为百分数；± 为五折**样本标准差 ddof=1**，不是 confidence interval。完整四任务和 coarse 指标在 CSV。保存输出原本已四舍五入到 4 位小数，以下派生统计继承其精度。

| 数据集 | 公开保存方法 | mean ± sample SD (%) |
|---|---|---:|
| Vienna4x22 | MultiTaskCNN / BSSL | 24.33 ± 7.82 |
| Vienna4x22 | MultiTaskCNN / LogMel | 32.78 ± 3.32 |
| Vienna4x22 | SingleCNN / BSSL | 30.37 ± 1.97 |
| Vienna4x22 | SingleCNN / LogMel | 28.37 ± 3.04 |
| Batik-plays-Mozart | MultiTaskCNN / BSSL | 50.06 ± 2.54 |
| Batik-plays-Mozart | MultiTaskCNN / LogMel | 48.46 ± 2.20 |
| Batik-plays-Mozart | SingleCNN / BSSL | 49.98 ± 2.64 |
| Batik-plays-Mozart | SingleCNN / LogMel | 49.63 ± 2.78 |

这些只是同一外部集上的五个训练 fold 模型的描述性汇总；训练数据彼此重叠，不能当五次独立数据集实验或总体不确定性估计。平均五个 F1 也不等于 pooled predictions 上重新计算的 F1。

## 文件与复算

- [extract_and_summarise.py](extract_and_summarise.py)：标准库脚本，读取 snapshot；校验 notebook hash、100 个 dictionaries、每组完整 folds 0–4；不 import 项目代码。
- [saved_checkpoint_records.csv](saved_checkpoint_records.csv)：100 个保存 dictionaries，含 dataset/method/feature/task/fold/checkpoint/cell。
- [saved_per_fold_metrics.csv](saved_per_fold_metrics.csv)：200 条长格式指标，保留 coarse 值及来源 cell。
- [all_fold_summary.csv](all_fold_summary.csv)：40 组 mean、ddof=1 和 ddof=0 SD、min/max 与最大 fold。正文使用 ddof=1。
- [v0_table5_4_comparison.csv](v0_table5_4_comparison.csv)：32 个 v0 表格数值与 per-task max／stated-rule 对照。v0 数值在脚本中逐项明示，来自表格转录，不是重算结果。
- [validation.json](validation.json)：完成性与匹配计数。
- [input_snapshot](input_snapshot/manifest.json)：11 个小输入原文件及来源 hash。

复算命令只做本目录的文本提取和统计：

```bash
python3 "/Users/jollibear/Documents/PhD_Thesis_Source_20261022/02_Ultra_细节/Ch5_现有输出汇总/extract_and_summarise.py"
```

最小后续资料：确认 Table 5.4 的 run commit／评估脚本版本与表格生成记录，说明 fine F1 实际是 macro 还是 weighted、类别集合与 blank handling，以及多任务辅助指标究竟从共同 fold 还是各自 max 汇入。需要真正重算指标时才索取逐录音预测／reference labels；当前不得自动重训。
