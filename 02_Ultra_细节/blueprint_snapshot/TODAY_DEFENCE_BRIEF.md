# 今天答辩先读 / 22 October 2026, UTC+08:00

答辩确切时间未知；按仍需今天口头应答准备。本文件约5分钟，之后只练被问到的答辩卡。两份报告总体积极，但preliminary recommendation不等于最终viva结果；不要以好评替代技术回应。

## 先记住的主线

统一问题是：在可信的结构/监督条件下，补回可解释、可编辑的dynamics层。Ch3 symbolic completion；Ch4 audio+aligned-score velocity correction；Ch5 audio→score dynamics+metre；Ch6 audio+aligned notes、无目标velocity标签的renderer-conditioned adaptation。四章是scenario map，不是一个完整end-to-end AMT系统。

今天最该收窄的四个说法：

1. “controlled”只指note structure固定，不表示无音频的velocity唯一可识别。Ch3应说conditional completion。
2. Ch4的known-note velocity改善，不等于note detection F1提升；Ch5的工作流图不等于完整AMT系统量化验证。
3. Ch6吉他指标是渲染后loudness correlation，不是物理力度/真实velocity准确率；钢琴directly supervised baseline仍然最好。
4. 11位专家、8段短片的听测是支持证据；不是严格MUSHRA或普遍知觉定论。

## 练习顺序（依问题跳卡）

| 顺序 | 卡 | 重点 | 建议 |
|---|---|---|---|
| 1 | A01 | 四章主线、published/adapted/synthesis | 先准备开场定位 |
| 2 | A02 | recovery、controlled、weak supervision | 优先练30秒版本 |
| 3 | A05 | 模块化与完整AMT | 不承诺note F1提升 |
| 4 | A09 | renderer-conditioned、保真度、泛化 | 分清真实/合成标签 |
| 5 | A06 | Ch4 loss、实验设置 | 系数相等≠梯度平衡 |
| 6 | A07 | change points与beat/downbeat | 共享≠显式一致性约束 |
| 7 | A08 | 跨数据集 | 主动坦白best-fold目标选择 |
| 8 | A04 | 风格依赖、听测 | 不把CI当显著性检验 |
| 9 | A03 | roll/event、beat time、量化使用场景 | Ch4已onset-token |
| 10 | A10 | V0/Vhat、两阶段proxy | 说清更新谁、target哪里来 |
| 11 | A11 | Huber vs MAE | 理由≠已证明更优 |
| 12 | A12 | simpler、自动选SoundFont | 自动选择未实施 |

完整口语草案见 [ORAL_ANSWER_CARDS.md](ORAL_ANSWER_CARDS.md)。每卡均按“问题→有范围的贡献→已有证据→限制→具体修订”。先答问题、再引用页码、最后给修改，不在答辩现场背整段。

## 随手可查的证据（主v0）

| 对象 | 位置 | 可以说 | 不可扩大为 |
|---|---|---|---|
| Ch3 MAE | Tables3.2–3.3 p46/PDF73 | MAESTRO11.5、SMD11.2 | 量化输入/作曲家无关已验证 |
| Ch3听测 | §3.9 pp48–49/PDF75–76 | 11专家、8×10s；U-Net overall3.01±0.34 | 全人群知觉定论 |
| Ch4 SMD | Table4.2 p63/PDF90 | HPT10.0→Score-HPT8.0 velocity MAE | pitch/onset F1提升 |
| Ch5主结果 | Table5.2 p78/PDF105 | BSSL multitask DynF1 54.4±8.9；0.5M | 普遍instrument泛化 |
| Ch5外部结果 | Table5.4 p80/PDF107 | best-fold transfer diagnostic | 完全target-independent选择 |
| Ch6吉他 | Table6.3 p100/PDF127 | FL rBSSL 0.740→0.777 | 真实velocity MAE改善 |
| Ch6钢琴 | Table6.2 p99/PDF126 | baseline MAE3.9，proxy10.5 | proxy优于直接监督 |

## 今天必须避免误说的核查缺口

- **Fig6.3来源**：p101/PDF128称guitar ground-truth velocity；同章真实GAPS/FL无velocity标签。尚未找到生成脚本/源数据，不能猜是合成、pseudo-label或真实测量。若被问，承认需要追溯证据，暂不以该图支持真实吉他真值恢复。修订取决于核查结果，可能需移除/收窄依赖该图的主张。
- **Ch4训练状态**：§2.5.4 p28/PDF55写frozen，§4.6.2 p58/PDF85写jointly trained counterpart；实际trainable scope须查实验代码/记录。今天可准确描述接口与已报告协议，不臆造冻结细节。
- **没有完成的实验**：beat-aligned/quantised、loss weight、Huber-vs-MAE、explicit beat consistency、自动bank selection、joint AMT均不能说已做。

## 评审原意

R1 Emmanouil Benetos：p3批准进入viva，excellent/top25%；主要是小问题与讨论。R2正文无署名，metadata Waleed Abdulla不能确认身份：p4建议Pass with minor revisions/2 Excellent；p1/4明确不要求新数据、新实验或大改。

先承认可成立的批评，再划清证据范围，最后承诺可执行的小修。若涉及新增实验，先决定主张能否通过准确解释/收窄解决；确实无法保留核心结论时再与用户/导师商定实验。
