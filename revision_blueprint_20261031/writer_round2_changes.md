# 第二轮返修记录

来源：独立reviewer_round1.md。round1不变；以下是本轮实际新增的文字和处理，候选复审仍待进行。全部F01–F16已逐项回应，没有实质性拒绝审查意见。F03保留一个证据区别：SMC已有hybrid comparison不能证明weight sweep，但未见sweep材料也不能据此断言作者从未做过。

本轮不是倒填历史。working中的162条准确称为短稿／组件草图及取舍，不认证162次完整独立改写。单独GPT-6.1仅审5个摘录，其建议作为局部编辑输入；全段拼接按源文核验。

## F01 至 F16 对应

| Finding | ID | 处理 | 核验原上下文 | round2实际解决方式 |
| --- | --- | --- | --- | --- |
| F01 | R1-15 | 采用 | Chapter_3/chap3.tex:13；原首句后紧接known notes/timing重复 | A/B/C均改成完整首段；每稿missing/flattened/uninformative只出现一次，后段应用语境保留。A为最小首句替换效果。 |
| F02 | R1-21 | 采用 | chap3.tex:375–380 Stimuli 与451 Discussion | 三个正文候选只写训练来源与composition接口；完整拼接在原Discussion首段后。作者量化说明、reference处理和程序细节留中文工作状态，不造另一种确定协议。 |
| F03 | R1-25 | 采用 | chap4.tex:133 loss公式与解释；SMC §3.3 preliminary comparison | 完整保留公式、denominator、变量定义；B保留preliminary证据，删普遍最优性收尾，区别equal coefficient与numerical magnitude。不据未见记录断言从未有sweep。 |
| F04 | R1-13 | 采用 | Background.tex:594 dataset总述与Table2.7 | B改velocity annotations并说明row provenance；C补triangle通用图例；推荐A，不伪造Audio单元格。 |
| F05 | R1-14 | 采用 | Background.tex:879/886 evaluation | A加given class/event type；C改成解释结果时必须注明规则，不保证现有冲突已解决；B保留。 |
| F06 | R1-27；R1-37 | 采用 | chap5.tex:36 targets；Conclusion future_amt | B的metrical grid限于score-facing；C区分note onsets与beat grid，第5章选A，第7章C只放一次。 |
| F07 | R1-28 | 采用 | chap5.tex:38完整target段 | 完整拼接保留定义；B只补explicit boundary supervision。C明确相邻labels可导出boundary，不说独立head逻辑必需。 |
| F08 | R1-29 | 采用归因修正，正文保留 | beat_postproc.py:139–147；final_evaluation.py default与normal分支 | normal/default调用已核验并明确写入外部证据；实际table/run映射仍待查，不把function存在或default当全部run。 |
| F09 | R1-30 | 采用 | chap5.tex:187、328、330 | 完整目的段去rebuttal/停止迁移措辞；共用protocol替换330段，187缩成cross-reference，target-label selection明确披露，V-05继续开放。 |
| F10 | R1-17；R1-18 | 采用 | main/Intro/Ch3/Conclusion全部12个实际出现点 | 逐处列准确原文和保留/替换；只替§3.2 image-based段，保留正式title与已成立类比，不把概括指令当精确替换表。 |
| F11 | R1-33 | 采用 | chap6.tex:111、36、431、457等局部上下文 | C不再预设mismatch造成退化；三处同步给完整段落效果，crop-length实测数值留在原段，只弱化机制解释。 |
| F12 | R1-34 | 采用 | chap6.tex:126 β与PHE/OSF定义段 | 完整拼接中β和1:1只保留一次，A/B/C都明确未做dedicated MAE comparison，不暗示做过而未证实。 |
| F13 | R1-36；另含R1-38C逐稿意见 | 采用 | chap6.tex:517 renderer selection；Conclusion/Ch5 gradual marks | C归因改为selected renderer而非自动化本身；R1-38C改not explicitly represented，避免implicit暗示已有hairpin恢复。 |
| F14 | R2-02 | 采用并撤回过强理由 | Intro.tex:177 organisation及161贡献列表 | B末句写实际synthesis内容，不说exclusive/exhaustive addition；理由撤回已核实全部新增归属，保留概念综合价值与最终paper diff待查。 |
| F15 | R2-04；R1-16 | 采用 | chap3.tex:Results、Discussion；main abstract；Intro；Conclusion | 完整Results保留mean similarity排序，集中一次11人/8段/单PianoTeq与分组限制；R1-16只谈style control；全书同步不重复small/泛化否定，Intro保留结果而非只写研究意图。 |
| F16 | R1-32 | 采用 | chap6.tex:91/93；PHE/OSF §6.5.1对FFT回指 | 完整两段保留100fps、22050Hz、FFT2048、hop221、Hann和Chapter4引用；只改固定架构和符号含义解释，未更改配置。 |

## 全部97条路线的处置

以下保留逐稿审查覆盖：P仅指第一轮审查对当时文字的判断，不能转换成作者YES。本轮修改过的文字一律待复审。

| ID | 第一轮逐稿判断 | 第二轮处理／推荐 |
| --- | --- | --- |
| R1-01 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R1-02 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R1-03 | A/B/C P | 保留原已通过文字；推荐 A |
| R1-04 | 单稿/合并/保留 P | 局部编辑/合并调整；推荐 A |
| R1-05 | A/B/C P；可重叠小建议 | 局部编辑/合并调整；推荐 B |
| R1-06 | A/B/C P | 保留原已通过文字；推荐 B |
| R1-07 | A/B/C P | 保留原已通过文字；推荐 B |
| R1-08 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R1-09 | A/B/C P | 保留原已通过文字；推荐 B |
| R1-10 | 条件通过，图副本需匹配 | 保留原已通过文字；推荐 A |
| R1-11 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R1-12 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R1-13 | A P；B/C V | 已按F04修订；推荐 A |
| R1-14 | A/C V；B P | 已按F05修订；推荐 B |
| R1-15 | A/B/C V | 已按F01修订；推荐 A |
| R1-16 | A/B/C P | 已按F15修订；推荐 B |
| R1-17 | A/B/C P；全文计划V | 已按F10修订；推荐 B |
| R1-18 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R1-19 | A/B/C P | 保留原已通过文字；推荐 B |
| R1-20 | A/B/C P | 保留原已通过文字；推荐 B |
| R1-21 | A/C V；B R | 已按F02修订；推荐 A |
| R1-22 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R1-23 | A/B/C P；偏好A | 局部编辑/合并调整；推荐 A |
| R1-24 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R1-25 | A/C P；B V | 已按F03修订；推荐 B |
| R1-26 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R1-27 | A/C P；B V | 已按F06修订；推荐 A（Ch.5）；C（Ch.7，与R1-37合并） |
| R1-28 | A P；B V；C R | 已按F07修订；推荐 B |
| R1-29 | A/B/C P；归因说明 | 已按F08修订；推荐 B |
| R1-30 | A P；B/C V | 已按F09修订；推荐 B |
| R1-31 | A/B/C P | 局部编辑/合并调整；推荐 B |
| R1-32 | 返修操作范围 | 已按F16修订；推荐 A |
| R1-33 | A/B P；C V | 已按F11修订；推荐 B |
| R1-34 | A/C P；B V | 已按F12修订；推荐 A |
| R1-35 | 条件通过，图副本需匹配 | 保留原已通过文字；推荐 A |
| R1-36 | A/B P；C V | 已按F13修订；推荐 A |
| R1-37 | 单稿/合并/保留 P | 局部编辑/合并调整；推荐 A |
| R1-38 | A/B P；C V | 已按F13修订；推荐 B |
| R2-01 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |
| R2-02 | A/C P；B V | 已按F14修订；推荐 B |
| R2-03 | A/B/C P | 局部编辑/合并调整；推荐 B |
| R2-04 | A P；B/C V | 已按F15修订；推荐 A |
| R2-05 | 单稿/合并/保留 P | 保留原已通过文字；推荐 A |

## 关键完整拼接位置

- R1-15：原§3.1首段整体 → 三个完整首段；后续应用段保留，避免“只替首句”造成第二句重复。
- R1-21：原Discussion首段保留 → 新增干净的应用段 → 后接表示讨论。Stimuli协议不作确定替换。
- R1-25：原loss引言/公式/变量定义 → 所选解释；每个候选都完整展示这一组合。
- R1-28：原四target/beat解码段 → 所选独立head理由 → 原thesis-positioning段。
- R1-30：完整purpose段A/B/C；共同替换原selection段；前文协议段只留cross-reference。
- R1-32：完整§6.4.1两段，原配置和后文FFT回指保留。
- R2-02：完整organisation首段 → 原Chapter2组织段。
- R2-04：完整听测Results段 → 原Discussion；MOS/CI表及方法细节保留，且全书四处作精确同步。

## 给第三编辑的路由意见

本写作窗没有编辑GRS文件或DECISIONS。reviewer对GRS R1-21的新Q/P分支判断应交其维护者：Q只在输入量化已确认后使用，不能默认reference同样处理；P当前不能覆盖作者已记录的量化说明。P中“because it supplied captured velocity targets”不能解释timing是否量化，velocity来源与timing处理分开写；未执行时把“The discussion now separates...”改成“I propose to clarify...”。内部核验规则不放入正式作者response语气。

## 仍开放与实施状态

正式baseline、实际run provenance、听测timing preparation、Ch5 F1/fold与表源、Fig6.3 guitar GT、最终ICASSP稿仍pending。source-local候选可以继续审，不因这些未定停止全部工作；没有以新实验填缺口。

本轮仅新增writer_round2.md、writer_round2_changes.md及round2证据JSON。论文源、作者回复、四篇论文PDF、bibliography、图像原资产和round1均未改。作者批准仍待唯一清单，候选复审待独立审查者完成。
