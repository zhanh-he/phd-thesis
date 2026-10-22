# 补充核查缺口（不是评审原报告的新要求）

## V-01 — Ch5 target-selected fold：已从文字与表格确认协议

位置：§5.6.1 p75/PDF102、§5.7.3/Table5.4 p80/PDF107。multitask按目标dynamic F1挑五折最好一折，single-task每任务独立挑最好fold；论文明确说test-only/no-finetuning，但选择用了target metric。

推论：是乐观的迁移诊断，不能等同source-only selection的无偏外部估计。无需先断言结论无效；缩小主张、说明协议，可选用保留预测做all-fold/source-selected再分析。此处未拿到fold输出，也未重跑。

## V-02 — Fig6.3的reference label来源：未解决

位置：p101/PDF128。原图左侧写GT MIDI Notes+Velo，caption和正文写guitar excerpt、ground-truth velocities；§6.6.1 p95/PDF122和§6.8.1 p98/PDF125说真实吉他GAPS/FL没有direct velocity labels。

已检查：v0、main.pdf同页文字；原图视觉；Chapter_6/chap6.tex第442–447行；图像为Chapter_6/figures/p3.jpg；git历史显示该资产由commit2f035ed（to final）引入。当前树内没有对应作图代码/数据说明。源caption重复相同说法，不能独立佐证真值。

状态：**证据来源待核查**，没有推断其为synthetic controls、reference estimator/pseudo-label或genuine acoustic measurements。需要作者的生成脚本、原始输入/数据记录和标签语义。未找到前不以该图证明真实吉他velocity恢复；依据核查结果纠正图文或收窄/移除依赖主张，不能承诺仅改caption即可。

## V-03 — Ch4 training scope：未解决

§2.5.4 p28/PDF55写frozen AMT front-end；§4.6.2 p58/PDF85写retrain velocity branch、jointly trained counterpart。§4.5“unchanged backbone”可能指架构，不足以判断weights。需查实验实现/optimizer参数与checkpoint记录。本次仓库为thesis源码，未查得训练实现/日志，不做实现级结论。

## V-04 — 数据统计/局部措辞：待来源核验

- MAESTRO时长：Table2.7 p35/PDF62写172h；§3.6.1 p43/PDF70及§4.6.1 p57/PDF84写>200h；§6.6.1 p95/PDF122写198.7h。可能涉及版本/过滤/口径，当前没有证据指定原因，不替作者猜。
- Table2.7中ATEPP的43%、三角符号、MIDI模态需定义并核对来源，报告R1-13已提。
- Fig2.3(e,f)颜色没有解释，原图已看；不能补造色图语义。
- Ch4 §4.9 p65/PDF92提SMD/MAPS，但本章展示表格的外部比较为SMD。需要找到MAPS结果或删掉未展示的范围；不能从结论一句补造MAPS实验。

这些补充项先做资料核对和主张校准，均不自动意味着必须开展新实验。
