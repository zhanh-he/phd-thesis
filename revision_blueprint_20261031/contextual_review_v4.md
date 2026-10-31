# v4语境补充独立审查与阅读层最终QA

2026-10-31。审查对象为`contextual_audit_v4.md`中的三组新增文字、R1-35 KEEP选择，以及编辑的START_HERE、CHANGE_CARDS_v2和DECISIONS。对照了完整Introduction、Background的动态/velocity定义、Chapter5目标与解码、Chapter6任务/renderer定义/离线proxy训练、Conclusion相应论述和原评审/作者批注；另直接查看了未改的Fig6.2图像。

**结论：三组新增文字均可供作者选择；R1-35优先KEEP原caption。它们是独立补充选项，不覆盖冻结第三轮，也不继承任何旧YES。** 原39项文字可选／4项证据待核判断仍有效，新增补充不改变examiner意见数量或关闭V-01–V-07。

**阅读层的U01–U08结构性问题已解决。** 新入口的重点、局部YES、组合/镜像选择、原话与新稿关系均可成立；建议把入口两处措辞再定点收准，精确替换见后文。没有必要增加HTML或启动下一轮整篇润色。

## 1. velocity定义及mf：ACCEPT，作为一个一致性补充包

这是必要的局部修正，不是仅为了“更好看”。Intro:62把velocity说成所有乐器的universal loudness variable；:89把它说成physical intensity/initial strike force测量；:92又把mf说成human perceptual loudness的neutral middle ground。它们与已存在的Background:265、276、280、285以及Conclusion:88–90直接不一致。

Background明确区分key/hammer motion的离散proxy、renderer-dependent control、context-dependent marking；Chapter6:56–65/459也明确guitar的velocity是给定renderer下的控制坐标，不是演奏手势的普适物理真值。因此应让引言使用同一套定义，保留piano传感器数据的有效含义，不把全部velocity变成“无客观性”。作者在R1-09只留下简短“Yes a true”，不能被解释为已经批准本组新增文字；R2-03未有既有作者回复。本组仍是编辑提案。

**可供作者选择的Intro:89整段，按writer原候选接受：**

```latex
Here, MIDI velocity refers to the velocity value in a Note On message. It is a machine-readable control parameter. In sensor-equipped piano data, the recorded value acts as a discretised proxy for key or hammer motion. Each note carries an integer value that can be edited independently, although its acoustic effect depends on the instrument and renderer. When expressive values are missing, a MIDI sequence may instead use a constant such as 64.
```

它保留note-level、independent editing、sensor provenance和64例子，删去“force/intensity的严格测量”“所有乐器通用响度”与笼统的必要默认值规则。无需再补一段MIDI规范细节，也不改变第2章已审的Note On限定。

**Intro:62的实际组装效果：**

```latex
Unlike complex continuous controls (e.g., guitar overdrive or piano pedalling), dynamics offers an exceptionally tractable and editable symbolic representation. MIDI velocity is an editable note-level control in digital audio workstations (DAWs), while score dynamics provide a standardised notational vocabulary for composition, pedagogy, and performance analysis \cite{kosta2014dynpiano,cancinoChacon2018computational}. This dual status makes dynamics a robust bridge between low-level MIR outputs and higher-level musical practice.
```

同组其余准确替换均可接受，建议一起呈现，避免引言仍自相矛盾：

| Intro位置 | 原短语／句 | 选择采用的准确新文字或操作 |
| --- | --- | --- |
| :43 | a deep semantic gap exists between physical machine measurements (MIDI velocity) and subjective human cognition (score dynamics) | a gap remains between machine-readable control values (MIDI velocity) and context-dependent musical notation (score dynamics) |
| :53 | bridging physical machine measurements (e.g., MIDI velocity) with semantic cognitive notations (e.g., score dynamic markings) | using note-level controls (e.g., MIDI velocity) and contextual notation (e.g., score dynamic markings) |
| :82 Nature单元格 | `\makecell[l]{Physical\\measurement}` | `\makecell[l]{Note-level\\control}` |
| :100 | a machine-centric, physical parameter | a machine-readable control parameter |
| :100末句动词短语 | bridge the fundamental gap between objective physical measurement and subjective human cognition | bridge acoustic observations, performance controls, and musical notation |
| :92末句 | In symbolic environments, the default assumption is often that missing score dynamics should be filled with \textit{mf} (mezzo-forte), which is the neutral middle ground of human perceptual loudness. | **删除这一整句；不添加替代默认值。** |

删除mf句的理由是“软件名义映射≠人类听觉中性基准”；不是否定mf作为有效dynamic marking。该段前面关于score dynamics的定义和metrical structure保留，Background已有名义播放映射也保留。Intro:18的sensor-captured数据介绍不必因此重写；本组不据任何文字推定Fig6.3 guitar GT来源。

## 2. S3结构与beyond-piano scope：ACCEPT，无需加长

### Intro:118新增S3句

**可供选择的准确新增句：**

```latex
Finally, \textbf{Scenario S3} uses an \textit{audio-only} input to jointly estimate dynamic markings and the metrical coordinates needed for a \textit{score-facing} output.
```

此句替换原“removes structural support entirely ... fully open ...”句。Chapter5:11、27–40、95–97实际预测dynamic levels、change points、beats/downbeats，再在beat坐标上形成标注；audio-only指输入没有外给score，而不是输出不需要结构。本句没有新增note transcription模块、hairpin输出或未知实验。

完整候选段已对读：S1/S2说明与表1.2吻合；后接的末句

> These settings form the core empirical arc of the thesis by varying both the available evidence and the target representation.

是冻结第三轮R1-15已存在的同步文字，**本v4选择不自动批准它，也不重复实施。** 推荐作者同时采用原R1-15时，使用writer给出的完整组装段；若R1-15未选，则v4仅替S3这一句，不能整段覆盖作者另选的结尾。中心问题、R1-05定义插入点和R1-06在table后的解释都不受本次操作挤掉。

### Intro:153整条scope bullet

**可供选择的准确文字：**

```latex
\item \textbf{Exploration beyond the piano.} Chapter~\ref{ch:beyondpiano} explores note-level velocity estimation for guitar using indirect supervision. Large-scale non-piano score-dynamics transcription with human labels remains outside the scope of this thesis.
```

必要性是消除原“non-piano score-dynamics ... will only be investigated as an exploratory extension”的语法指向误会。新句与Chapter6:8–16、51–65及Conclusion:113一致：目标是guitar note-level MIDI velocity，输入含performance audio与aligned note events，监督是间接的renderer/proxy比较。它没有说guitar有captured velocity labels，也没有声称恢复了物理pluck force。输入条件在相邻场景说明和第6章已有充分解释，此bullet无需重复一串技术限定。

Scope边界是非钢琴score dynamics未在本thesis做大规模标注转写；不是把第6章变成S3，也不是新宣布guitar结果通过所有GT核验。V-06保持待核。

## 3. data-curation末句：ACCEPT，仅替一句

原Intro:45的“entirely bypass acquisition bottlenecks and annotation ambiguities”与同章:103、Chapter5关于annotation convention的解释、Conclusion:115的context-dependent target相冲突。估计标签可以减少采集需求，不能消灭既有标注歧义。用reduce/can修正承诺即可，不需要在motivation堆新的局限。

**新增可供选择的准确末句：**

```latex
By estimating missing dynamics on existing corpora, we can reduce the need for new data collection and make those corpora more useful for music research.
```

前两句和现有引用保留。writer展示的完整段开头collecting是原R1-04词汇修正，本组新选择**只覆盖末句，不把collecting的新旧决定一并吞掉**。作者原批注同意的是recollecting→collecting，收窄承诺属于本次新增编辑建议，不应写成作者早已同意。

## 4. R1-35 Fig6.2：推荐KEEP，原长A仍是可选解释

**推荐保留的原caption：**

```latex
\caption{An encoder-only Transformer maps padded note sequences to per-note PHE/OSF targets extracted from SoundFont-rendered audio.}
```

它已经回答teacher targets来自rendered audio。独立查看p2.jpg可见左支路“MIDI Sequence → SoundFont / Render MIDI to Audio → Target Params → Masked Params Loss”，右边是Transformer；不能照抄评审right的方位而画错支路。Chapter6:161已说明offline proxy，:215说明procedural MIDI sampler，:233–236明确SoundFont rendering/extractor teacher过程。图注所在段落不是real-recording adaptation。

冻结第三轮A四句描述科学上可接受，但重复上文和随后teacher小节，收益不足以要求重写当前一行caption。**KEEP原caption／原图应是明确有效的作者选项，独立偏好KEEP。** 如作者仍希望视觉更直接，可另选在teacher支路标SoundFont-rendered audio；图本身已有Render MIDI to Audio，因此也不强制新增这个label。任何图副本仍需视觉核验。

若最终选择KEEP，GRS可用的事实说明是：

> Figure 6.2 shows offline proxy training. Its caption identifies the teacher targets as PHE/OSF extracted from SoundFont-rendered audio.

这没有声称新增了内容，也不以保留caption推断Fig6.3所谓GT的来源。若选择A或图内label，则正式report按真正实施差异写。

## 5. 明确的采用／选择映射

以下是交给编辑维护者的映射建议，本复审没有修改ledger或替作者选择。

| 新补充／选择 | 记录在既有ID下 | 批准边界 |
| --- | --- | --- |
| v4组1：Intro velocity定义同步 | R1-09的“Intro定义同步v4”补充；R2-03只交叉引用 | :89整段＋:62短语＋:43/53/82/100一致性替换＋:92删末句。作为明确的一组新文字供选，不从原R1-09 B自动继承YES。 |
| v4组2：S3与guitar scope | R1-06的“Intro范围补充v4”；关联R1-15、R2-03但不重复填 | :118只替S3句、:153替bullet。原R1-15尾句仍依它自己的选择；R1-06原B位于table后，保留其原操作位置。 |
| v4组3：data-curation承诺 | R1-04的“动机末句补充v4”；R2-05只交叉引用 | 仅:45最后一句；不扩充原单一方案包批准范围，不自动批准/拒绝collecting词汇修正。 |
| R1-35 KEEP | R1-35给KEEP原caption／原图与原A两个明确选项 | KEEP是有理由的无改动方案，不把NO原A自动等同已选KEEP，也不把旧A覆盖删除。 |

不新增examiner意见ID，不改变39／4计数的含义。新增补充是已通过文字审查、待作者选择的addenda；所有实施仍未发生。编辑合入时可只更新对应卡和选择范围，无需重开其余第三轮候选。

## 6. 阅读层U01–U08复核

已在编辑完成早期四项修复后的版本重新核对。英文保持冻结第三轮；新v4尚未混入原推荐，处理正确。

| 原诊断 | 当前独立结论与实际证据 |
| --- | --- |
| U01 版本冲突 | **解决。** DECISIONS:105明确原第二轮绑定只是历史，当前新填写绑定第三轮；:31/101分清10s的71、358两处。 |
| U02 组合／共用选择 | **解决。** :85直接提供Ch5 A＋Ch7 C／自定组合；:76/95是镜像而非重复YES输入。:33明确没选Ch7 C时37未解决。两处实际英文在CHANGE_CARDS:165–175均与冻结稿一致。 |
| U03 局部YES | **解决。** :71/79/84/88分别绑定13A前五句、21A两句、26A前三句、30B目的段；明确排除43%/audio facts、Q/P、参数计数/shape、selection protocol。四个局部块与冻结JSON都是准确前缀，不是另造候选。 |
| U04 主句露出实际答案 | **解决。** START_HERE:25–29先给各自平均后相对1:1；:35–41先保留U-Net/Flat/ConvAE排序再限定样本。原/拟节选都准确。另见下一节对more direct节选的精确建议。 |
| U05 上下文／原立场／差异 | **主要障碍解决。** 首屏给五组实际原/拟节选和中文理由，卡表区分原立场与推荐；R1-32在:458–475提供两段old对两段new。并非43项都成了一张完整逐词diff，但其余通过按需全文链接展开，符合先读concise的目标。不能把“未找到回复”写成同意。 |
| U06 合并包隐藏方法内容 | **解决。** 单一方案包:181及DECISIONS:27明确22/32是baseline整理/方法澄清；八项准确内容可展开，唯一稿不要求重复选字母。合并包仍允许排除和逐项覆盖。 |
| U07 重复待核／责任 | **结构解决，入口一句需收准。** 四项局部YES集中，完整V01–07只在ledger作为事实目录；不要求一晚回答全部。START_HERE:63的未来式查记录承诺应改为现有项目材料尚未确认的状态，见下一节。 |
| U08 流程历史抢注意 | **解决。** README首行导入中文START_HERE，主入口不要求读轮次/hash；四组是阅读导航，不是四次笼统批准。43个ID各有且仅有一组导航，镜像与no-change保留。 |

### 独立准确性／完整性检查

- 作者阅读三文件共检查289个本地文件/锚点链接，均能解析到现存文件或锚点；没有仅照抄handoff的链接计数。
- CHANGE_CARDS的29个英文code blocks：15个准确对应原文，14个准确对应冻结候选/其局部；无未知改写。START_HERE十段实际英文引文全部匹配原文或冻结候选；听测省略号明确标出节选。
- 43个ID导航无重复、无缺失。ledger43行原备注逐字保留；全局baseline字段与6个事实确认字段仍是原待填内容，未代填YES/NO或事实答案。新inline anchors和两个镜像不会创造额外决定源。
- 8个details的开闭配对、58个code-fence边界完整。这是Markdown结构和内容检查，未声称已做另一种HTML/PDF的视觉验收。没有比较HTML待交付，Markdown已能承担这一轮入口。

## 7. 两处入口文字的精确收准

这两处都不需要改冻结第三轮正文或新增A/B/C。

### START_HERE:49：用原B的具体适配句作节选

“more direct route”在完整B的下一句有具体含义：用real recordings与differentiable rendering interface形成目标域适配信号，而不是仅靠synthetically labelled audio上的迁移。它**没有证据支持更短的总inference链、更少训练阶段或更低算力**；proxy仍有offline training，VeloEst仍用piano-pretrained checkpoint。因此不能为了回应这次检查又加“shorter/faster”优越性。

最小修法是保留推荐B和原文对照，只把49行的拟稿首句节选替换为同一个已通过B的第二句，并把标签写“拟段节选”：

> Rather than relying only on transfer from synthetically labelled audio, the estimator is adapted using real performance recordings and a differentiable rendering interface.

45行原作者more efficient立场与编辑未有成本比较的判断已分开，可保留；51行继续保留renderer要求。这样作者第一眼看到实际监督连接，而不必先接受另一个比较形容词。无需把原B重新判为未通过，也不把词direct解读成已测量的运行性能。

### START_HERE:63：把未来查找承诺改成准确待核状态

当前“先由我们继续查已有记录，缺材料时再请你指出位置”容易让人以为还有一个后台查找步骤在持续运行，或会搜索项目外来源。本轮授权只限当前`phd thesis`项目，没有上传或外部检索授权。建议整段改为以下同样简短的文字，链接沿用：

> 量化MOS的原说明保留。现有phd thesis材料尚未确认的刺激处理、最终run／表源、吉他图GT和最终ICASSP版本，继续待核；如项目内另有记录，请注明位置。四项可先选的文字与未定事实见[这里](CHANGE_CARDS_v2.md#pending-scope)，完整目录仍在[决定清单](DECISIONS.md#事实确认)。

这说明已知状态和材料入口，不承诺新的项目外搜索、无人值守工作或上传。卡页的“先对齐run”等属于定稿条件，可保留，但总体范围应服从这条项目内边界。

另有一处可选中文精确化，不构成新的科学缺陷：START_HERE:9把most controlled问题解释成“没有音频，不代表信息最充分”，略过了评审真正区分的结构固定与力度估计不确定性。可改为：

> 评审指出：音符与时间虽然固定，缺少音频中的力度线索仍会增加估计的不确定性。你原本想说输入信号更少，也已同意换词。推荐只修正描述条件的首句，保留后面的研究提问。

它直接依据COMMENT_MAP:273/277，不把控制条件、信息量与难度排序混成同一件事。若只做最少必要入口修正，先处理前面两处即可，不再开启润色循环。

## 8. 固定版本与未改动范围

| 本复审输入 | SHA256 |
| --- | --- |
| contextual_audit_v4.md | 8b72c2121b5f998630678d8bbcf6319a104d7de668317b223d749bd6e1c37f82 |
| START_HERE.md（早期QA小修后） | 119bfc9aab2f15c76d6c3f6d5a0f3eabd2580d686a244c967c19ceaacaf027ee |
| CHANGE_CARDS_v2.md（早期QA小修后） | 9fa9687ed001933dded80a50d64691dc52a841a04c5e525b8267edd95d343460 |
| DECISIONS.md（早期QA小修后） | 5f777d675875c8956a62fe7c68ed28d8991dcc1842113e74e70950912b7aebfd |
| READABILITY_HANDOFF_v2.md（含早期修复记录） | 5e4d51dfc4e2674efab4776727a9a47394b5452b999b2768ed870a2feca3d1c7 |
| 冻结writer_round3.md | 1a658584d35ee50580dd2dfd6eb9d0afdac1b573404edbacf3e475a79250c75e |

编辑在本次阅读期间完成了已知的四项早期QA修复；本复审重新核对了实际diff和上述新版本，并未因文件仍在最初生成就推定其通过。之后的入口收准和v4合入如有发生，需以真实新diff作定点核对，不把这些建议预写成已经实施。

独立复核源清单128/128字节未变；冻结第三轮hash保持一致，先前审查均保留。本复审只新建本文件，没有改源码、原回复、PDF/图片、作者选择、ledger或编辑入口，没有实验、Git操作、上传或对外通信。V-01–V-07和四项evidence-blocked保持原状态。
