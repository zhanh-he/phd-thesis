# 第二轮独立复审

日期：2026-10-31。对象是固定的 `writer_round2.md`、`writer_round2_changes.md`、round2候选JSON，以及当前 `GRS_REVISION_REPORT_DRAFT.md`；对照原 thesis、两份examiner报告、作者原回复及第一轮独立意见。第一轮审查保留不变。本文件没有改作者决定、writer/GRS文件或任何论文源。

**结论：首轮16项中，15项的文字问题已解决；F11仅部分解决。** R1-33的局部A/B/C都可用，但完整同步段落仍有旧的确定性机制解释，应定点小修。其余候选不需要再整体重写。43项均已复审，27组A/B/C共81稿，另16个单稿/合并/保留路线，共97条；下表逐项区分文字、证据和作者决定。

本轮项目级建议：**38项 ready-for-author-choice、4项 evidence-blocked、1项 needs-text-revision。** evidence-blocked为R1-13、R1-21、R1-26、R1-30；各项内已经通过的局部文字仍可选择。R2-02的组织性综合段可选，但不能据此关闭最终paper逐结果归属的V-07。

这些状态不表示YES，不表示实施，也不表示事实不确定性已关闭。正式baseline仍未确认；所有候选以当前源码为工作坐标。任何最终revision report还须对真实提交基线和最后实施差异核验。

## 固定输入与实际检查

| 输入 | SHA256 |
| --- | --- |
| writer_round2.md | 2e0430427a9ed337cb7a8734374b38dcdc999d4d884bdac318cced097ad6e627 |
| writer_round2_changes.md | ace8a70970a0cc30386cab08c8d3764b5e2ea3937294797883d75d800fa137fa |
| GRS_REVISION_REPORT_DRAFT.md 初读固定版 | d24cae35574fafcb5a8d2415915942e88d54ec6f2325ee0875331043812321a6 |
| GRS_REVISION_REPORT_DRAFT.md 结束时更新后复读版 | b5e536e8b6b1b4bd4e70c5ec760bc43159fd553a457930edff9bf27a11000d6a |

- 97/97条候选正文都与round2 Markdown相符，未发现JSON和送审正文分叉。
- 81/81处原文与源码逐字相符，行号也相符；13处followthrough、2处共同replacement、12处terminology audit、3处assembled followthrough的原文与行号全部相符。
- `evidence/source_sha256.json`跟踪的128个源文件本轮复核为128个字节不变，无缺失、无变化。主文件、两份thesis PDF、报告和现有图等来源没有被本复审修改。
- 实际重读了候选拼接涉及的首尾段、保留公式及配置、跨章同步和GRS的43项拟答复。未编译、未跑实验；未产生新图，因此不能声称图示路线已经视觉通过。
- 本环境未提供可验证的模型/effort配置回执；不声称已核实Ultra或跨模型独立性。可观察循环是writer round1 → reviewer round1 → writer round2 → 本复审。working短稿/组件的历史界限维持第一轮判断，没有新增虚构轮次。

## F01–F16 实际解决情况

“resolved”指本轮所审文字，不包含待查的run、刺激或最终发表稿。

| Finding | 状态 | 本轮实际判断 |
| --- | --- | --- |
| F01 R1-15 | resolved | A/B/C都是完整首段；known notes/timing与missing velocity各出现一次，后续应用段保留。A最接近原文，推荐A合理，不再把B强塞给作者。四处most controlled/constrained同步也有准确原句。 |
| F02 R1-21 | resolved；V-02仍开放 | 三个thesis候选只写composition接口与训练目标；不含“The author reports”或编辑指令，不预先肯定timing处理。GRS的Q/P也已分开，见下文。 |
| F03 R1-25 | resolved；实际run仍待对应 | 完整loss引言、公式、两项denominator、标签和变量定义保留。B直接说明相对等权与SMC preliminary comparison，删去every-backbone/dataset万能最优性否定；没有把作者验证说成从未做过。 |
| F04 R1-13 | resolved；表事实仍开放 | B改为velocity annotations并要求说明provenance；C补triangle图例。三个候选不再把全表来源统称captured velocity。但43%分母和新增Audio单元格仍不能认证。 |
| F05 R1-14 | resolved；V-05仍开放 | A加class/event-type；B正确区分macro与support-weighted；C改成解释结果应交代的条件，未保证现有数值已与定义一致。 |
| F06 R1-27/37 | resolved | B将metrical grid限于score-facing dynamics；C区分onset接口与beat坐标。第5章A、第7章C合并37只放一次，未声称实现完整AMT。 |
| F07 R1-28 | resolved | 完整target段保留；B只补explicit boundary supervision；C承认可由相邻level变化导出边界。没有将独立head写成逻辑必需或虚报独立消融。 |
| F08 R1-29 | resolved；最终run仍开放 | 正文保留when beats available；外部记录现在准确写normal/default evaluator路径与advanced分支。默认实现支持说明，但不证明所有最终表、各baseline均使用同一分支。 |
| F09 R1-30 | resolved文字；V-05未解决 | A/B/C完整目的段去掉rebuttal口吻和“stops transferring”；selection段整段替换，前文缩成cross-reference。target标签用于selection写明。条件说明明确保留，不能将它当表值来源已认证。 |
| F10 R1-17/18 | resolved | 12个真实出现点逐处列原句与保留/替换；只改§3.2相关段，保留题名、正式术语和成立的single-channel类比。没有机械全文替词。 |
| F11 R1-33 | **partly resolved；须小修** | C不再预设mismatch是退化原因，三处同步保留实测数值。但是431行拼接段的旧结尾重新作普遍稳定性/纯目标监督断言；457行最后一句也应保持风险语气。具体见下一节。 |
| F12 R1-34 | resolved | A/B/C都明确did not conduct a dedicated comparison with MAE；完整段只出现一次β=1.0，valid notes和PHE/OSF 1:1未丢失。 |
| F13 R1-36/38C | resolved文字 | 36C将操作目标的变化归于选中renderer，未把自动化本身夸大；38C已用not explicitly represented。38的旧中文理由尚未同步，属整理问题。 |
| F14 R2-02 | resolved文字；V-07仍开放 | B列四篇/四章mapping，并描述当前thesis实际的formulation、scenario map、shared background、synthesis。没有声称穷尽或独占新增。旧过强归属理由已撤回；最终ICASSP差分仍不能用提供稿认证。 |
| F15 R2-04/16 | resolved文字；V-02仍开放 | 完整Results保留higher mean similarity、Flat/ConvAE和已有citation；11人/8段/单PianoTeq范围集中一次。不加population naturalness等非本实验目标，不用CI宽窄推广泛validity。摘要/引言/Discussion/Conclusion准确同步，16不重复堆限制。 |
| F16 R1-32 | resolved | 完整两段保留100fps、22050Hz、FFT2048、hop221、Hann、checkpoint来源与Chapter4架构引用。V^(0)与Vhat说明和architecture/parameters区别清楚；后文FFT回指继续成立。 |

## 唯一须返修的正文：R1-33完整同步段

定位均对上述hash的 `writer_round2.md`。此问题不否定局部A/B/C，不要求增加测量，也不要求改表值。

### F11a 1598行：删去重新引入确定机制的末句

当前段先说“does not isolate that mechanism”，随后仍保留：

> This mirrors a long-standing observation in inverse-problem design: a supervision signal that only depends on the latent variable of interest is more stable than a high-dimensional signal that mixes that variable with many nuisance factors.

这里的“only depends”和“is more stable”超过本比较能够推出的结论；还与本轮457行承认target audio仍受unobserved controls影响不一致。它没有提供可核验的独立依据，不应靠一句通用理论重新认证机制。

**最小修复：删除这个末句。** 保留原定量观察和前一句consistent with即可。完整修后段：

```latex
Third, the asymmetry between the two adaptation interfaces widens with crop length. On FL dataset, Diff-Synth's $r_{\mathrm{BSSL}}$ falls by $0.083$ when moving from $2$\,s to $5$\,s, while Diff-SFProxy's $r_{\mathrm{BSSL}}$ varies within $0.01$. The crop-length pattern is consistent with greater exposure of the waveform objective to acoustic mismatch, but the present comparison does not isolate that mechanism.
```

这是删去过度解释，不是删去有效结果；0.083、0.01、2s/5s均保留。

### F11b 1602行：末句与前面的can保持一致

已修的“does not remove effects of unobserved controls”正确，但下一旧句是：

> The recovered velocity absorbs effects that, in the real performance, came from other parallel controls.

本段讨论一种混杂风险，未单独测出这些controls实际贡献；直接用“absorbs … came from”又将风险写成已确认事实。**小修为：**

> The recovered velocity may therefore absorb effects that, in the real performance, came from other parallel controls.

无需再插免责声明。这样与本段前面的“can become entangled”和下一段renderer-conditioned定义一致。若writer采用等价的can写法也可；不需要新增一轮全章改写。

请在下一轮新候选文件及其证据JSON中同步这两处完整拼接；保留本次固定的round2及round1历史。复审仅需看这两处实际小修和下列整理，不需重跑全部97稿。

## 43项逐项建议

- **ready-for-author-choice**：列出的候选文字/操作路线已可交作者选；图的制作和渲染、作者YES、事实核验、实施仍各自待完成。
- **evidence-blocked**：关键字段不能用现有证据定稿，局部说明已通过也不等于完整问题关闭。
- **needs-text-revision**：有可定位文字缺陷，先按最小修复返修。
- 表中“ABC可用”只针对当前局部候选正文。R1-33的共同同步段不包含在这个局部判断里。

| ID | 路线文字判断 | 项目建议 | 推荐与准确边界 |
| --- | --- | --- | --- |
| R1-01 | 单A保留方案可用 | ready-for-author-choice | A；numeric/author–year仍由作者选。保留原体例是有效选项；转换需另核排版。 |
| R1-02 | 单A可用 | ready-for-author-choice | A；报告支持accepted，只改状态，不补未经核实出版细节。 |
| R1-03 | ABC可用 | ready-for-author-choice | A最小；补instrument/expressive factors的图副本尚未制作，不能称图已改或视觉通过。 |
| R1-04 | 单A及同步可用 | ready-for-author-choice | A；结论改collecting new data from scratch也自然，只做局部文字。 |
| R1-05 | ABC可用 | ready-for-author-choice | B；数据表达状态与监督条件已区分，并说明可重叠。 |
| R1-06 | ABC可用 | ready-for-author-choice | B；保留Ch6为S2标签稀缺延伸，不新增audio-only velocity结果。 |
| R1-07 | ABC可用 | ready-for-author-choice | B；直达score-dynamics路径清楚，一处caption/正文解释即可；图路线实施后须核对。 |
| R1-08 | 单A可用 | ready-for-author-choice | A；Bark三组三列分隔准确，实施后渲染表格。 |
| R1-09 | ABC可用 | ready-for-author-choice | B；限定Note On velocity，不推广成全部MIDI动态控制。 |
| R1-10 | 单A条件文字可用 | ready-for-author-choice | A只有统一色图副本真正匹配时可用；保留原色则先核实编码。原PDF标题没有抽取工具所示黑区缺陷。 |
| R1-11 | 单A可用 | ready-for-author-choice | A；定义一般humanisation再限定本文velocity，够短。 |
| R1-12 | 单A可用 | ready-for-author-choice | A；保留已有crescendo定义，只补cross-reference和本文输出范围。 |
| R1-13 | ABC表达修复；事实待核 | **evidence-blocked** | 偏A；43%对应哪一版本/分母仍待确认。B新增Audio单元格和各行provenance须有原资料，不能由caption替代。 |
| R1-14 | ABC可用 | ready-for-author-choice | B；class-wise与macro/weighted定义可选。只完成背景定义，V-05实际数值averaging仍开放。 |
| R1-15 | ABC完整首段可用 | ready-for-author-choice | A最小；B可供希望解释歧义时选。不同源码出现点各按准确同步处理。 |
| R1-16 | ABC可用 | ready-for-author-choice | B；保留不做style conditioning的真实范围，composer组不是因果控制。样本/renderer限制集中给R2-04。 |
| R1-17 | ABC及12处audit可用 | ready-for-author-choice | B；single-channel类比准确，不机械改title。V-03实际input-mask/channel分支未由此核实。 |
| R1-18 | 单A合并可用 | ready-for-author-choice | 并R1-17，避免重复；不把操作说明贴成英文正文。 |
| R1-19 | ABC可用 | ready-for-author-choice | B；completion/estimation/recovery角色清楚，未说未知symbolic输入有唯一真实performance。 |
| R1-20 | ABC及同步可用 | ready-for-author-choice | B；物理时间为接口兼容选择，未说beat-relative必然损失表达。其71行10s说明与R2-05的358行是两处。 |
| R1-21 | ABC应用段可用；协议待定 | **evidence-blocked** | 偏A应用段；作者quantised MOS原立场保留。input/reference timing、duration、系统共用处理不能由SMD来源或captured velocity推断。GRS Q/P均未选。 |
| R1-22 | 单A可用 | ready-for-author-choice | A；Flat、pretrained Seq2Seq、本地ConvAE区分正确，不声称全部相同input分支。V-03独立核验。 |
| R1-23 | ABC可用 | ready-for-author-choice | A；modularity解释够用，不将architecture unchanged扩为parameters frozen。Ch4原frozen/joint冲突仍须按V-04统一。 |
| R1-24 | 单A可用 | ready-for-author-choice | A；Ch4矩阵接口与onset token相容，不借Ch5动机证明表示普遍更优。 |
| R1-25 | ABC完整loss块可用 | ready-for-author-choice | B；相对等权、active-position平均、SMC初步比较表述准确。只通过书面objective/证据范围；实际theta、整体尺度和run映射仍在V-04。 |
| R1-26 | A的O/F/Fex定义可用 | **evidence-blocked** | 偏A；onset-only实际输入形状及parameter-count覆盖范围未核实，A的完整system-count归属不能仅靠此文字认证。补既有配置/计数依据，不猜维度或改表数字。 |
| R1-27 | ABC可用 | ready-for-author-choice | Ch5 A；Ch7 C并37。一处解释score-facing beat grid，另一处区分onset，不强统一时间坐标。 |
| R1-28 | ABC完整段可用 | ready-for-author-choice | B；明确boundary supervision，C也不再声称levels逻辑上无法导出边界。 |
| R1-29 | ABC可用 | ready-for-author-choice | B；encoder共享/heads与loss分离/解码snap区分正确。代码normal路径支持归因，实际最终run与各baseline映射仍待查。 |
| R1-30 | ABC目的段可用；共用protocol有条件 | **evidence-blocked** | 偏B；target-informed selection披露必要且口吻自然，但不能以当前书面规则认证表值、共同fold或F1类型。待真实表源定稿。 |
| R1-31 | ABC可用 | ready-for-author-choice | B；more direct具体落在监督可用性/real-audio adaptation，不声称未经测量的算力或一般效率优势。旧中文C理由待清理。 |
| R1-32 | 单A完整两段可用 | ready-for-author-choice | A；配置、架构引用和后文回指均保留。符号/架构/可训练参数清楚，没有重新调参。 |
| R1-33 | ABC局部可用；共同同步段返修 | **needs-text-revision** | B；按F11a删一句、F11b加may即可。不改结果或模型设计。 |
| R1-34 | ABC完整段可用 | ready-for-author-choice | A最小；β与1:1保留，未做MAE比较写清，不暗示已比较而未显著。 |
| R1-35 | 单A条件文字可用 | ready-for-author-choice | A；离线teacher/rendering与real-audio adaptation区分正确。当前图已有rendering文字；新增箭头须图副本匹配，不能宣称已完成。 |
| R1-36 | ABC可用 | ready-for-author-choice | A；保留SoundFont自动选择为具体future工作，选中renderer定义目标而非自动化本身。 |
| R1-37 | 单A合并可用 | ready-for-author-choice | 并27C；不虚报note accuracy提升或听感收益。 |
| R1-38 | ABC可用 | ready-for-author-choice | B；静态levels/CP不等于hairpin spans，C已准确说未显式表示。中文旧理由须跟上。 |
| R2-01 | 单A保留方案可用 | ready-for-author-choice | A；既有首尾定位已覆盖中心问题，允许no-change胜出，不新增四套重复positioning。 |
| R2-02 | ABC组织综合段可用 | ready-for-author-choice | B；四章四paper映射和thesis综合内容可供选择。V-07最终ICASSP/逐结果published-versus-new归属仍阻塞完整核验；不将此ready当该归属已证实。 |
| R2-03 | ABC可用 | ready-for-author-choice | B；guitar证据写loudness agreement，不写已验证captured velocity accuracy。voice/bowed/wind仍属待研究；Fig6.3 GT来源V-06开放。 |
| R2-04 | ABC完整Results及同步可用 | ready-for-author-choice | A；11/8/单renderer只集中一次，所测是reference similarity，对手Flat/ConvAE正确。V-02 timing未解决，不添加任一确定处理。 |
| R2-05 | 单A四项微调可用 | ready-for-author-choice | A；只改实有措辞。10s两处各改一次；未把抽取断行或其他科学疑点当proofreading。旧待核验说明须更正。 |

## 代表性通过段落与全书衔接

### R1-25：既回答相对权重，也保留作者已有验证

B在完整公式后写：

> The frame-wise BCE and onset-wise L1 terms are averaged over their respective active positions and combined with equal relative coefficients. We retain the hybrid objective of Kim et al. (2024), supported by the preliminary comparison with frame-only and onset-only supervision reported in our associated SMC paper. Equal coefficients do not imply equal numerical loss or gradient magnitudes.

这比首轮“every backbone or dataset”更贴问题。SMC提供稿§3.3确有hybrid对single-objective的初步比较；不能由此推出best-ratio sweep，但也不能抹去作者已经验证过的立场。theta=.5与正文sum相对都是1:1，只是整体loss尺度不同；实际run映射仍待核验。公式未因改文字而丢失。

### R1-32：符号修复没有删掉可复现设置

完整两段保留原配置之后说：

> Here, $V^{(0)}$ denotes the intermediate acoustic estimate, while $\hat{V}$ denotes the corrected onset values passed to the rendering interface; the superscript does not identify a pre-adaptation checkpoint.

并以：

> The architecture is retained during adaptation, while VeloEst parameters are updated and the synthesis or proxy back-end remains frozen.

收束。它解决了architecture unchanged与parameters frozen混淆，并保留后面PHE/OSF仍需的FFT设定；没有借修符号删除方法细节。Ch4独立的训练分支冲突仍按V-04核，不把Ch6澄清当成所有章节都已解决。

### R2-04：保留结果，不将小听测反复写成无效

A的完整Results：

> U-Net received higher mean similarity ratings than Flat and ConvAE on the selected excerpts, while Flat received the lowest ratings, consistent with earlier findings on default velocity \cite{kuo2021velocity}. The listening study provides supplementary perceptual evidence from 11 expert listeners, eight selected SMD excerpts, and one PianoTeq rendering configuration. The composer-group scores are descriptive rather than a controlled comparison of stylistic effects.

方法段已交代reference similarity，故这里不必再堆一遍定义。没有把Seq2Seq误加进听测，没有未经报告的significance结论，MOS/CI不变。摘要validated→assessed，Discussion改为greater perceived similarity，Conclusion写selected excerpts/Flat/ConvAE；R1-16不再重复11/8/renderer。范围语句在必要处明确一次即可，不需要继续添加small、population-wide或全模型validity否定。

## GRS blueprint 复审

43项英文拟答复均已读。当前仍以“待决定；说明稿，未执行”和“I propose”处理，未冒称论文已经改好。R1-21此前的内部编辑警告已移到条件/工作说明；没有把“I will not present ... unless”当正式作者答复。

### R1-21 Q/P：文字问题已解决，刺激事实未解决

当前Q只在实际记录确认input timing quantisation时可用，未推定reference同样处理；P只在记录明确确认performance timing保留时可用，当前不默认采用，也不覆盖作者原量化说明。

Q的关键两句：

> The listening-test inputs were timing-quantised versions of the selected SMD excerpts, with velocity values removed before estimation. I propose to clarify this preparation in the listening-test protocol and distinguish this evaluation from a controlled comparison of timing representations.

P对应写：

> The listening-test inputs were derived from the selected SMD performances and retained their performance timing, with velocity values removed before estimation.

两条作为**互斥条件草案**可以保留。前两句composition/训练来源可以先审；不能拿captured velocity targets解释timing，也不能据“来自SMD并删velocity”推导具体量化或未量化。V-02继续需要input、reference各自处理、grid/分辨率、duration是否改变、各系统是否共用刺激。无需新实验。正式答复只使用已证实的那条，不并列Q/P交给examiner。

### 其他关键条目

| GRS项 | 复审结论 | 仍需保留的边界 |
| --- | --- | --- |
| R1-25，531行起 | “In the stated objective”归属准确；相对等权与SMC preliminary comparison可保留。 | 不改写成所有run的最优比例已经核实；V-04继续开放。 |
| R1-29，611行起 | “In the normal evaluation path of the retained code”是正确证据层级，不再只说存在函数。 | 最终表、advanced/default分支与baseline逐项映射未核实。 |
| R1-30，635行起 | 明确“current protocol description”；无fine-tuning不等于未用target labels。拟答复语气可用。 | 中文V-05明确没有认证table provenance，必须保留至实际对齐。 |
| R1-32，679行起 | architecture不变/参数适配说明正确。 | 最终报告还要依实际实施差异，而不是把候选当已完成。 |
| R1-33，699行起 | consistent-with与未分测fidelity/gradient表述可用，没有新增因果保证。 | thesis共同段落F11仍要按上文小修后才可给完整文字通过。 |
| R1-34，719行起 | 未做专门MAE比较写清，Huber理由不伪装成比较结果。 | 保留β和实际方法设置。 |
| R2-02，841行起 | organizing synthesis说明可用，不再宣称穷尽thesis-only novelty。 | 该GRS项自己的最终mapping条件仍应保留，ICASSP提供稿有占位，不能作clean final baseline。 |
| R2-03，861行起 | guitar写resynthesised loudness agreement，voice/bowed/wind不冒称验证。 | Fig6.3所谓GT的身份不能由图像或guitar数据无标签事实反推。 |
| R2-04，881行起 | similarity、reference、11/8/one configuration及Flat/ConvAE正确。 | 不由人类演奏MIDI来源推定reference保留的timing；V-02未关闭。 |

结束校验时GRS发生并行更新，随后固定新快照并复读43项英文拟答复及关键条件，结论不变。新版本的43个候选链接已全部指向writer_round2，均仍标复审待完成，没有把它们升级为作者批准或实施。部分“待返修F07”等审查状态仍待本次结果同步；交第三编辑制作concise表前，只更新实际通过的文字状态，F11和事实缺口保留。不要用本次文字复审把所有“待核验”清零。GRS结论适用于上表两份hash，后续修改需按差异核验。

## 少量说明整理，不要求新的实质改写

1. `writer_round2.md:1493`仍说R1-31C“否定句偏多”，但本轮C已删那句。建议改成“C把对比落在supervision availability与接口要求，解释较长；B更紧凑”。当前B推荐可保留。
2. `writer_round2.md:1807`仍以38C的“implicit可能被误读”否定它，而C已改为not explicitly represented。建议改成“A最短，B更具体说明CP与span输出的区别，C更偏未来接口叙述；推荐B”。
3. `writer_round2.md:2119`的“与R1-20同一10s解释只改一次”不准确：R1-20对应 `chap3.tex:71`，R2-05对应 `chap3.tex:358`，是两处不同原句。改为“10s说明有两处：R1-20处理71行，R2-05处理358行；各改一次，不重复实施”。实际candidate replacement未冲突，是说明要跟上。
4. 候选链接已更新到round2；继续同步F01–F16审查状态时，F11留待这次小修复核；V-01至V-07、表格43%、未产出的图副本和作者决定分别保留。

这些整理不能回写为作者已同意，也不应改掉历史round1。没有必要继续循环全部候选以追求整齐的“全绿”。

## 开放证据与交付范围

| 边界 | 本轮可以确认 | 仍不能确认 |
| --- | --- | --- |
| V-01 正式baseline | 当前源码工作坐标、两PDF的准确身份与内容差异已保存。 | 报告154/127与Z相容、Git/日期都不能单独证明正式送审附件；需要提交记录或作者确认。 |
| V-02 听测 | 作者原批注明确称quantised MOS；正文写SMD来源/去velocity；两者可以同时成立。 | 实际timing、duration、reference、各系统刺激制作细节。不能默认P，也不能替Q补reference量化。 |
| V-03 Ch3 run | 表示类比和baseline来源说明可以先选。 | actual mask/channels/loss/window配置；默认快照不是最终run证据。 |
| V-04 Ch4 run | 书面相对等权与SMC preliminary evidence、O/F/Fex定义明确。 | 具体训练mode、onset-only shape、参数计数覆盖、theta/整体尺度及SMD开发用途；Background frozen与joint表述需按实际run统一。 |
| V-05 Ch5 | normal代码有条件snap/dedup；现书面protocol使用target labels选择；有macro/weighted与表源冲突。 | 最终表各项真正run/evaluator/fold；不能由汇总值逆推macro。既有对照32/32显示数值与per-task maxima相合，只有22/32与书面共同dynamic-best fold规则相合，故不能仅靠disclosure关闭。 |
| V-06 Fig6.3 | 当前caption/asset声称guitar GT velocity；真实GAPS/FL无直接velocity标签。 | 该图究竟是真实标注、合成控制、pseudo-label或其他来源。不得先猜、先删或据图声称accuracy已证实。 |
| V-07 ICASSP | 四章/四paper映射和thesis综合结构可读；提供稿p4/p5含未完成占位。 | clean final publication与逐结果published/adapted/thesis-new归属。 |

以上是既有证据边界，不是新加examiner要求，也不要求新实验。原source不变、文字候选与正式实施分开。下一步最小动作是writer修F11a/F11b和三处说明，再由reviewer定点复核；第三编辑随后呈现精简选择表和仍开放的人类决策，不替作者批准。
