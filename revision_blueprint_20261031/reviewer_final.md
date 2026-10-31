# 第三轮定点最终核验

日期：2026-10-31。独立复审者对固定的第三轮文件作定点检查，承接且不修改[第二轮完整审查](reviewer_round2.md)。本轮检查实际diff、候选JSON、完整拼接及源文件完整性；没有重复声称进行一轮新的全书审查。

**结论：定点核验通过。F11a/F11b和三处说明均已准确修复，无新的文字返修项。39项可供作者选择、4项证据待核的分类成立。** 这个结论只适用于下列hash的候选提案；不表示作者YES、不表示实施、不关闭既有事实缺口。

## 已核验的固定版本

| 文件 | SHA256 |
| --- | --- |
| writer_round3.md | 1a658584d35ee50580dd2dfd6eb9d0afdac1b573404edbacf3e475a79250c75e |
| writer_round3_changes.md | 135e3e0b894a0bcb3124a395d9242eed0f7de082c7b937d2730847317eedf093 |
| evidence/writer_candidates_round3.json | de9b73e37393623e8b2d1b2361185f8049fcdf4ce735ec62fba55c0d775a2b79 |
| 冻结writer_round2.md | 2e0430427a9ed337cb7a8734374b38dcdc999d4d884bdac318cced097ad6e627 |
| 保留的reviewer_round2.md | 2877440df279b6f1470e6568a287b0371512fce140f4c82ef75ceb24103e48b8 |

第三轮文件已经完整存在，不是对未完成文件作预审。交付前再次计算的round3三个hash均与本表一致。

## 五项定点检查

| 检查 | 实际结果 |
| --- | --- |
| F11a，R1-33对应源chap6.tex:431 | 共同拼接段删除了“This mirrors a long-standing observation...”完整末句。0.083、0.01、2s/5s、BSSL及bounded consistent-with句逐字保留。删除只收窄机制解释，未删定量观察。 |
| F11b，R1-33对应源chap6.tex:457 | 最后一句从确定的absorbs改成may therefore absorb。前面的can become entangled、unobserved-controls限制及后续renderer-conditioned定义衔接一致，不再把风险写成已测因果。 |
| R1-31C评价 | 不再批评已经删除的否定句；现在比较supervision availability、接口要求和段落长度。A/B/C英文均未改，推荐B仍成立。 |
| R1-38C评价 | 不再以旧implicit为理由否定现稿；现在明确C已写not explicitly represented，B更具体区分change point与gradual span。A/B/C英文均未改。 |
| 两处10s说明 | 源chap3.tex:71是segmentation段的“roughly four measures at 120 BPM”；:358是ablation段的“roughly encompasses four measures...”。是两处不同原句，第三轮明确分别由R1-20与R2-05各改一次。候选文字未被重复或合并误删。 |

第三轮R1-33的实际431行拟段落：

```latex
Third, the asymmetry between the two adaptation interfaces widens with crop length. On FL dataset, Diff-Synth's $r_{\mathrm{BSSL}}$ falls by $0.083$ when moving from $2$\,s to $5$\,s, while Diff-SFProxy's $r_{\mathrm{BSSL}}$ varies within $0.01$. The crop-length pattern is consistent with greater exposure of the waveform objective to acoustic mismatch, but the present comparison does not isolate that mechanism.
```

457行拟段落的实际新末句：

> The recovered velocity may therefore absorb effects that, in the real performance, came from other parallel controls.

两处均与第二轮复审提出的最小修复一致。R1-33原先的三处followthrough加上本轮两个操作，共五个逐句操作，作用于三个完整段落。将这些操作实际应用到各自引用的原段落后，三个结果都与JSON的assembled text逐字一致（仅忽略删除末句留下的段尾空白）；Markdown也与此一致。

## 与冻结第二轮的范围比较

- 全部43个canonical ID及顺序不变；97/97条局部variants逐字不变，含27组A/B/C共81稿及16项单稿/合并/保留路线。97/97均在第三轮Markdown中对应存在。
- 按43个正文section比较，只改变R1-31、R1-33、R1-38、R2-05四个section；其他39个section逐字不变。这里的39个不变section是diff计数，与下文39项文字可选的分类计数不是同一集合。
- 这四个section的差异只包括指定的R1-33共同段落及精确操作、31/38的中文评价、R2-05的两处10s说明；其余变化位于文件标题、历史说明、当前状态索引和收尾边界记录。未发现重新打开其他已通过正文。
- JSON差异也仅为所有条目的round3状态元数据、31/38的rationale、33的rationale/定点说明/五个操作与完整拼接、R2-05的pending说明。没有改变原文引用、局部候选、推荐路线、其他证据条件。
- 81处originals、15处followthrough、2处common replacements、12处terminology audit、3处assembled followthrough的引用原文和行号全部与未改源码相符。
- round1、round2、round2变化记录、working、COMMENT_MAP、ID_CROSSWALK、SOURCES、WRITER_HANDOFF的hash与已记录的冻结版本一致。第二轮独立审查文件也保留不变。

因此没有无关重写、方法配置丢失、结果数值变化或来源归属升级。R1-32完整配置、R1-25公式与证据边界、R2-04听测metric/comparator等第二轮已通过内容保持原文。

## 最终分类的准确含义

**ready-for-author-choice共39项**：继承第二轮的38项，再将已修复并核验的R1-33由needs-text-revision改为ready-for-author-choice。完整集合是R1-01至R1-38中除下列四项之外的34项，加R2-01至R2-05五项。

**evidence-blocked共4项，未关闭：**

| ID | 已可使用的局部文字 | 尚不能定稿的事实 |
| --- | --- | --- |
| R1-13 | 字段/triangle释义与不同velocity provenance说明 | ATEPP 43%对应版本与分母、各行Audio/velocity来源；不能用通顺caption代替逐行核验。 |
| R1-21 | composition接口与captured training targets说明 | 作者quantised MOS原陈述保留；input/reference timing、grid、duration、共用刺激处理仍待原始记录。GRS Q/P均不能默认选定。 |
| R1-26 | O/F/Fex、BiLSTM/Transformer条件解释 | onset-only实际形状与parameter-count覆盖范围，须按已有run/计数记录核验，不猜尺寸、不改结果。 |
| R1-30 | combined corpus transfer目的说明与书面target-selection披露 | 最终evaluator averaging、共同fold/per-task maxima与表源仍未对齐。披露target labels参与不等于实际表源已确认。 |

这四项是证据待核，不是仍需再润色英文。当前没有新的needs-text-revision项。第三轮header/index还保留写稿时“38项可选、33待最终核验”的状态，这是核验前的正确历史记录；本文件提供核验后的39/4结果，第三编辑可在concise表引用，不必为了改状态而重写冻结round3。

39项“文字可选”也不表示其中关联证据全部查明。例如R1-25实际run的theta/整体尺度仍在V-04；R1-29最终table/baseline与normal/advanced分支对应仍在V-05；R2-02的组织性综合段通过，但最终ICASSP逐结果published-versus-thesis-new归属仍在V-07。它们的当前候选已经限制到有证据的层级，不能把此ready标签用于更宽的事实认证。

## 源文件完整性与剩余边界

本轮独立重新计算 `evidence/source_sha256.json` 跟踪的128个源文件：**128/128不变，无缺失，无变化**。没有修改thesis、作者回复、论文PDF、图源、bibliography、数据或决定清单，没有实验、编译、commit、push或提交。本复审只新建本文件。

仍须保留第二轮记录的全部边界：

- V-01正式送审baseline尚未绑定到提交记录；当前源码是提案坐标，最终页码须在实际实施/编译后核对。
- V-02听测timing preparation、V-03 Ch3实际run/input/loss/window、V-04 Ch4训练/形状/权重范围、V-05 Ch5 metric/fold/table、V-06 Fig6.3 guitar GT身份、V-07最终ICASSP稿均未因本次文字修复而解决。
- 图示路线仍是提案。R1-03/07/10/35等需要对应图副本与视觉核验，R1-08需要实际表格排版核验；没有新图或编译结果就不能写“已匹配、已完成”。
- GRS说明稿最终须依据作者选项、实际改动和真实提交基线写完成式；本轮没有重新编辑或认证之后并行更新的GRS版本。
- 作者YES/NO与A/B/C仍由统一决定清单接收。39/4是独立编辑判断，不是作者批准，更不是执行授权。

没有操作被拒绝；定点复审和报告保存已完成。下一步可由第三编辑制作concise选择表，保留上述四项待核及跨项事实条件，供作者人工抉择。
