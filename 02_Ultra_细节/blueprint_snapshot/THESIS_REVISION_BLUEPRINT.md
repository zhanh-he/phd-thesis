# Thesis revision blueprint / 有边界的修订计划

这是first-pass规划，未修改论文。以两份报告为依据；不把提问自动升级为强制实验。R2明确要求minor revisions且不要求新实验，但新发现的证据缺口仍应核实、纠正或收窄，不能以好评覆盖。

## 修订顺序与可验收结果

| 顺序 | 任务 | 具体落点 | 验收标准 | 工作 |
|---|---|---|---|---|
| 0 | 锁定版本与证据 | source manifest；v0 vs Z/main | 指定最终修订基线；差异不静默覆盖 | 来源核查 |
| 1 | 核查高风险事实 | Fig6.3 p101；Ch4 frozen/joint wording | 追到图数据/脚本及训练记录；无法验证则收窄/移除依赖主张并标明缺口 | 已有证据核查 |
| 2 | 主线与来源 | §1.5–8；各章overview/summary；§7.1 | 四条件一表，paper/adapted/thesis synthesis可追溯 | 改写 |
| 3 | 任务与术语 | §1.5；§3.1/3.3/3.10；Fig1.1/2.1 | controlled限定结构；completion不承诺唯一还原；直接perceptual→score路径 | 澄清/图示 |
| 4 | Ch3有效性范围 | §§3.4/3.6/3.9/3.10 | roll与event权衡；physical-time事实；performance→quantised限制；听测支持性措辞 | 澄清/改写 |
| 5 | Ch4协议 | §§4.3–6；Table4.1 | inputs、loss归一化、训练更新范围、validation选择、known-note metric一览 | 解释现有实验 |
| 6 | Ch5结构与评估 | §§5.3/5.5/5.6/5.7 | state/transition、shared/explicit约束、GT-vs-estimated beat、best-fold选择、hairpin限制均明示 | 改写/可选再分析 |
| 7 | Ch6两阶段与claim | §§6.2–5/6.9；Figs6.1–3 | proxy训练/适配图分开；V0/Vhat清楚；真实/合成标签、metric与physical control不混 | 澄清/纠正 |
| 8 | 全书泛化与校对 | §7.3–4；Table2.7；其余图表 | 乐器边界、43%/三角来源、audio/MIDI模态、颜色图例、引用格式逐项核对 | 小修/排版 |

每一项完成后更新combined matrix状态与change log，而不是只给通用润色。允许多条报告意见由同一个修订解决，但每个R1/R2 ID仍保留独立回应。

## 贡献来源表的拟定内容（先核对、后写入）

| 层次 | 当前可确认的内容 | 仍需核查 |
|---|---|---|
| published/adapted methods | Authorship Declaration把Ch3–6关联到四篇论文；§1.8说Ch3–5保留文章技术贡献并统一叙事 | 录用状态、版本、每个新增段/表/实验对应论文哪一版 |
| thesis-level synthesis | §1.5统一问题、Table1.2场景图、§2.9六要求、Table7.1与§7.2跨章归纳 | 与文章重叠程度；不能凭本规划认定每一段首次出现 |
| author's role | 声明四篇均student contribution80% | 具体工作分工若需展开，应由作者/共作者记录核实 |

## 跨乐器主张边界

| 对象 | 当前证据 | 可保留主张 | 不能外推 |
|---|---|---|---|
| 钢琴 | Ch3/4 directly labelled velocity；Ch5 score labels；Ch6监督基线/间接适配对照 | 指定数据/协议下的velocity或score-dynamics结果 | 所有曲目、量化场景、所有performers |
| 吉他 | GAPS训练适配、FL外部；loudness correlations；synthetic proxy inversion | 指定renderer下attack-driven dynamics控制的探索证据 | 原演奏物理力度、real guitar velocity MAE、真实gesture唯一可识别 |
| voice | 未实验 | 可能需持续控制/新的声学描述，列研究方向 | 直接换bank即可推广 |
| bowed strings | 未实验；§6.9.4承认attack特征不足 | onset+sustain/continuous controls需重新定义 | PHE/OSF已足够 |
| wind | 未实验 | breath/sustain/articulation控制需另建目标 | piano-style scalar velocity等于物理表达 |

## 现有输出再分析与新增实验分开

**优先用解释、现有证据和主张收窄完成小修。**

- 可选已有输出再分析：若保存的Ch5各fold预测在手，报告all-fold分布、source-validation-selected fold，替代目标集best-fold作为主泛化估计；保留原diagnostic以便追溯。无预测/日志时不能假称只是排版。
- 可选已有资料核查：听测participant/stimulus聚合与CI计算；Ch4参数更新/损失尺度、checkpoint规则；Ch6Fig6.3原图/数据、descriptor标准化；Table2.7的43%和MAESTRO时长口径。
- 真正新增实验：Ch3 beat-vs-time、quantised transfer；Ch4 loss weights/joint-AMT与noteF1；Ch5 CPt-vs-level-difference、显式beat/downbeat一致性或predicted-beat系统评估；Ch6 MAE-vs-Huber、自动bank选择、独立renderer fidelity或新的乐器。**本次均未进行**。

只有在核心保留主张无法由现有证据支撑、也不能合理收窄时，才定义决定性实验，并先取得用户/导师对资源、时间和范围的同意。不能为每个viva问题增加一个实验。

## 论文当前可编辑状态

仓库有 main.tex、reference.bib、Chapter_1/Intro.tex、Chapter_2/Background.tex、Chapter_3/chap3.tex、Chapter_4/chap4.tex、Chapter_5/chap5.tex、Chapter_6/chap6.tex、Chapter_7/Conclusion.tex 和图像。因此并非PDF-only；本轮未编译、未改任何源文件，也未证明当前source恰好重建v0。Ultra应先在独立工作副本核对source/PDF对应，再输出reviewable patches。若最终提供的编辑基线缺源文件，则只提供拟替换段落和位置，不把PDF编辑当成等价替代。

## 小修收尾清单

38项R1和5项R2全部见独立清单/矩阵。正文中“all/always/simpler/universal/entirely/verified”等绝对措辞需按真实证据校准；不要机械全局替换。可选author–year先核对格式要求。ISMIR accepted先查录用记录。图颜色和Table2.7未知项必须有来源，不能补造图例/分母。区分抽取文本断词与真实渲染错误。
