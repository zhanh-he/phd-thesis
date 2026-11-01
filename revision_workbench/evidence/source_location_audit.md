# 来源与位置审核

完成全部43项位置映射。

- 顺序：Benetos的38项在前，第二份报告的5项在后，逐项原顺序。
- 50个annotation objects去重为25条回复，覆盖24项；R1-29有两条。
- 只预填9项明确修改意向；没有足够依据预填任何整项“不改”，34项待定。
- R1-21的keep current是保留项目开发现状，不自动代表拒绝论文澄清。
- 第二位教授的奥克兰归属来自用户说明，未把PDF元数据姓名当作已核实身份。
- 原报告意见43/43在对应PDF页唯一匹配；literal_pdf_text保留实际抽取文本。
- 原报告无R1-/R2-打印编号，这些是工作流ID；PDF章标题、bullet顺序另存。
- 具体候选稿、作者意向、事实核验、实施状态各自独立；旧YES不转移。

机器数据：`author_decision_evidence.json`。前屏只使用reviewer_question_zh与recommended_action_zh；证据、版本和检查记录放折叠详情。

当前定位：194处逐字源码位置、3个图像资产；全部44个最终v5操作均有对应条目。引用体例另保留285处调用清单。

## 给构建者的字段约定

- 每项：`id/reviewer_id/sequence_in_report`保持原报告顺序。
- 前屏：`reviewer_question_zh/recommended_action_zh/author_reply_summary_zh`，无Markdown引用嵌套。
- 预填：`author_decision_seed`仅为原回复修改意向；`author_prefill_evidence`给出精确批注与范围。具体候选仍未批准。
- 位置：统一使用`file/lineStart/lineEnd/anchorExact/plain_label/operation/operation_label_zh/proposedEnglish/proposalEvidence`；图片没有伪造行号，改用`texReference`。
- 路线：`recommended_route`每项只有一条；`locations`是推荐路线与必要上下文，`alternative_locations_evidence`只供查证，默认不显示为待实施动作。`priorConditionalDraftEvidence`不是可直接使用的稿子。
- 待核事实：`proposedEnglish=null`表示该具体文本尚待实验记录，不得拿历史条件稿填入。R1-13默认图注只取安全定义，不新增Audio列、不断言43%分母；R1-26/29保留安全结构解释，R1-30选择/平均的两处同步须先查记录。
- 共用：`sharedEditId`连接顶层`shared_edit_registry`；`ownerCommentId`指定只改一次的主项，其他条目只是同一操作的引用。KEEP只保留其明确范围，不否定同段他项修改。
- 独立小修：`independentlyOptional/choiceGroupId`保持每处单独选择，尤其N05b与N05c；对某条意见勾选“要改”不自动批准所有新英文。
- 持久化：手填决定、留言和改稿优先于全部seed；升级seed不得清空用户内容。
- 颜色：绿色只表示双方同意需要改，红色表示双方明确不改；助手不改、作者待定为灰色，其余为黄色。任何颜色都不证明事实已核实或正文已实施。

## 逐项索引

| ID | 问题 | 助手 | 作者原意 | 位置数 |
| --- | --- | --- | --- | --- |
| R1-01 | 是否改用作者—年份引用？ | no_modify | pending | 3 |
| R1-02 | ISMIR论文是否仍写成待审？ | modify | pending | 3 |
| R1-03 | 图1.1为何称通用AMT，却只画力度？ | modify | modify | 4 |
| R1-04 | recollecting是否应为collecting？ | modify | modify | 3 |
| R1-05 | weakly expressive和weakly supervised是什么意思？ | modify | modify | 2 |
| R1-06 | 第6章是否也是纯音频到MIDI力度的场景？ | modify | pending | 7 |
| R1-07 | 感知强度到乐谱力度必须经过MIDI吗？ | modify | pending | 4 |
| R1-08 | 表2.3的三组列是否需要分隔？ | modify | pending | 2 |
| R1-09 | MIDI力度总是只属于音符起点吗？ | modify | pending | 10 |
| R1-10 | 图2.3(e)(f)的颜色表示什么？ | modify | pending | 4 |
| R1-11 | humanisation的含义是什么？ | modify | pending | 3 |
| R1-12 | 背景是否应讨论渐强、渐弱？ | no_modify | pending | 1 |
| R1-13 | 表2.7的模态、符号和43%各指什么？ | modify | pending | 6 |
| R1-14 | 是否应先定义常用力度评价指标？ | modify | pending | 4 |
| R1-15 | 无音频的任务为何叫最受约束？ | modify | modify | 5 |
| R1-16 | 力度补全是否应由风格或作曲家控制？ | modify | pending | 6 |
| R1-17 | image-based和colourisation是否误导读者？ | modify | modify | 14 |
| R1-18 | 为何用钢琴卷帘而不是音符列表？ | modify | pending | 3 |
| R1-19 | 这是力度恢复还是力度估计？ | modify | pending | 2 |
| R1-20 | 为何用物理时间，而不用节拍时间？ | modify | pending | 4 |
| R1-21 | 用演奏MIDI评估是否符合创作用途？ | modify | pending | 4 |
| R1-22 | 基线模型能否集中介绍？ | modify | pending | 3 |
| R1-23 | 单独修力度是否贴近真实应用？ | modify | pending | 1 |
| R1-24 | 第4章为何仍使用钢琴卷帘？ | modify | pending | 2 |
| R1-25 | 两项损失是否平衡，需要加权吗？ | modify | modify | 1 |
| R1-26 | 表4.1的各实验组合是什么？ | modify | pending | 3 |
| R1-27 | 是否已将力度输出接入完整AMT系统？ | modify | pending | 2 |
| R1-28 | 已有逐拍力度，为什么还预测变化点？ | modify | pending | 2 |
| R1-29 | 节拍与小节拍分支如何连接？ | modify | pending | 4 |
| R1-30 | 受作曲家和演奏者影响，为何做跨数据集评估？ | modify | pending | 4 |
| R1-31 | 可微合成为何称为更简单的方法？ | modify | modify | 1 |
| R1-32 | V^(0)和V-hat有什么区别？ | no_modify | pending | 1 |
| R1-33 | DDSP合成器有多忠实于目标录音？ | modify | pending | 9 |
| R1-34 | 为何采用Huber而不是MAE？ | modify | modify | 2 |
| R1-35 | 图6.2的目标是否来自合成音频？ | no_modify | pending | 2 |
| R1-36 | SoundFont能否自动选择？ | modify | pending | 1 |
| R1-37 | 接入完整AMT后会改善音符转录吗？ | modify | pending | 2 |
| R1-38 | 未来工作是否应包括渐强等其他记号？ | modify | modify | 2 |
| R2-01 | 各技术章与总研究问题的关系够明确吗？ | no_modify | pending | 11 |
| R2-02 | 论文贡献与博士论文综合分别是什么？ | modify | pending | 6 |
| R2-03 | 哪些结论能推广到其他乐器？ | modify | pending | 13 |
| R2-04 | 11位听者的评估能支持多强的结论？ | modify | pending | 10 |
| R2-05 | 哪些语言和格式问题需要精简？ | modify | pending | 16 |

## 交付核验

- 186项自动核验全部通过；原报告43段、原回复25条、194个逐字源码位置及3个图像资产引用均已检查。
- 5处未选方案只放在证据区；推荐路线的替换/删除范围没有重叠，44个最终v5操作逐字一致、各有一个主归属。
- 285处引用调用全部定位正确；源文件19个、旧提案文件80个指纹不变。
- 严格作者种子：9改、0不改、34待定；初始颜色9绿、29黄、5灰、0红。
- R1-04只明确同意词语修正，额外动机句改写及score-dynamics默认值删除独立放在R2-05小修下；不扩大作者原意。
- 正式提交PDF版本、R1-13表格数据、R1-21听测处理、R1-26输入维度、R1-29最终解码与R1-30选择/平均规则仍未核实；该清单不是实施报告。
- 当前交付只覆盖数据与来源；未执行网页交互/持久化验收，也没有更改正文或推送Git。

JSON SHA-256：`2377297c61df5baca654d13a3fe79b42871ebecc6c3e53a66e4ac983ad508250`。详细诊断保存在本任务目录`workbench_seed_validation.json`，不放入默认阅读界面。
