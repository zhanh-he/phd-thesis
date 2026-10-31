# 第三轮定点小修记录

依据：reviewer_round2.md。只处理F11a/F11b及三处说明整理，没有重新打开已通过候选。

## 文字差异

| 位置 | round2问题 | round3操作 |
| --- | --- | --- |
| R1-33，共同拼接，源chap6.tex:431 | consistent-with后仍接“This mirrors a long-standing observation...”普遍稳定性断言 | 删除该整句；0.083、0.01、2s/5s和bounded consistent-with句逐字保留 |
| R1-33，共同拼接，源chap6.tex:457 | 原末句将unobserved-controls吸收风险写成既定事实 | 改为“The recovered velocity may therefore absorb effects that, in the real performance, came from other parallel controls.” |
| R1-31C中文评价 | 仍批评已经删除的否定句 | 更新成supervision availability与接口要求的当前取舍；不改ABC |
| R1-38C中文评价 | 仍批评已经删除的implicit | 更新成A最短、B区分CP与span、C偏未来接口；不改ABC |
| R2-05待核验说明 | 把两处10s当成一处 | 明确R1-20处理chap3.tex:71，R2-05处理:358，各一次 |

仅另更新标题/当前状态元数据。全部43项、97条局部候选variants与round2逐字一致；局部ABC评价在上述整理后对应现稿。共同同步从三段／三句操作扩为三段／五句操作，以同时记录删除与may修正。没有源文实施。

## 当前边界

承接round2独立判断：38项ready-for-author-choice，R1-13/21/26/30为evidence-blocked；R1-33两处已修，待最终独立定点核验。此状态不表示作者YES，不表示任何实施。V-01至V-07、最终baseline、run/表源、图来源和未产出的图副本继续保留。GRS与DECISIONS未由写作窗修改。

## 精确新段落

### 源Chapter_6/chap6.tex:431的拟替换段

```latex
Third, the asymmetry between the two adaptation interfaces widens with crop length. On FL dataset, Diff-Synth's $r_{\mathrm{BSSL}}$ falls by $0.083$ when moving from $2$\,s to $5$\,s, while Diff-SFProxy's $r_{\mathrm{BSSL}}$ varies within $0.01$. The crop-length pattern is consistent with greater exposure of the waveform objective to acoustic mismatch, but the present comparison does not isolate that mechanism.
```

### 源Chapter_6/chap6.tex:457的拟替换段

```latex
Velocity is not the only MIDI control that shapes rendered dynamics: continuous controllers can also encode within-note loudness variation~\cite{ryu2024midfild}. Pedal settings and room response also affect the synthesised piano waveform and are explicitly modelled by DDSP-Piano~\cite{renault2023ddsp_piano}. Consequently, when adaptation updates only velocity, the velocity gradient can become entangled with residuals caused by fixed or unobserved controls. Diff-SFProxy restricts the adapted control to velocity, but this does not remove effects of unobserved controls from the target audio. The recovered velocity may therefore absorb effects that, in the real performance, came from other parallel controls.
```

## 校验与hash

- 128份来源文件全部未变，变化列表为空。
- rounds1/2、working、共同来源/编号/交接文件全部未变，具体hash见evidence/writer_round3_validation.json。
- 97/97条局部候选variants逐字保留；只有R1-33共同拼接文字和指定说明/状态变化。
- round2 Markdown SHA256：`2e0430427a9ed337cb7a8734374b38dcdc999d4d884bdac318cced097ad6e627`。
- round3 Markdown SHA256：`1a658584d35ee50580dd2dfd6eb9d0afdac1b573404edbacf3e475a79250c75e`。
- round3候选JSON SHA256：`de9b73e37393623e8b2d1b2361185f8049fcdf4ce735ec62fba55c0d775a2b79`。
- 最小unified diff：evidence/writer_round3_vs_round2.diff，SHA256 `d5cb8eae540fd898f9156631b5559551c402191c729c86083ca5d4dd703eee82`。
- 未编译、未实验、未改图、未commit/push/提交；最终独立定点验证尚未发生。
