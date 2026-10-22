# Ultra后续任务提示：当前不要自动执行

你协助Zhanhong He（UWA）的论文《Recovering Musical Dynamics for Expressive Automatic Music Transcription》。不要混同候选人与Hanyu Meng。本文件是用户以后主动启动Ultra时的交接提示，不代表Ultra已启动，也不授权训练、改写原件、提交或发布。

## 先确定范围与版本

项目：`/Users/jollibear/Documents/PhD_Thesis_Source_20261022`。

原始commit：`7e319875a8b1e9fc8f6a0afa4dc4417b03212226`。主证据为154页的`Zhanhong_He_PhD_Thesis_v0.pdf`，SHA256 `3479394740921480c1325c70cc343eaea9e5d09df174be449415a9c8dacb4798`。

另有`Z_He_PhD_Thesis.pdf`与`main.pdf`，hash和内容不同。不要静默改用另一版本；先明确拟修订基线及LaTeX与PDF的对应关系。源码存在，但本轮没有编译重建验证。先看当前status与工作区说明，保护所有用户并发改动；不reset、覆盖、删除或合并脏工作。

用户答辩日期为2026-10-22，时区UTC+08:00，确切时间未知。先根据当前时间/用户最新说明判断答辩是否仍待进行。优先顺序可以更新，证据不能沿用过期假设。

## 重新审计源文件，而非只相信blueprint

完整读两份preliminary reports，各4页，包括表格、图像、签名、批注和recommendation。完整读主论文，包括front matter和references，必要时视觉核对图、公式与抽取文字。

报告1有正文和签名确认Dr Emmanouil Benetos。报告2正文无可见署名；Waleed Abdulla仅为PDF Author元数据，未确认。不要凭记忆补身份。Excellent/minor revisions是预评审建议，不是最终viva结果；好评不能代替技术回应。

以快照中的完整清单为起点，逐项核对R1-01至R1-38、R2-01至R2-05全部43项，包括复合问题。区分批评、问题、可选建议和赞扬。若发现遗漏，追加ID，不重排既有ID。

每项写明：报告页、论文section、印刷/PDF页、可定位原文、已有证据、回应、精确拟修改、工作类型和状态。可用confirmed/pending/proposed/completed，但completed必须有实际产物或可复核结果。

## 三项优先核查

1. **Fig6.3来源pending。** p.101/PDF128称guitar excerpt且reference带GT velocities；§6.6.1 p.95/PDF122、§6.8 p.98/PDF125说GAPS、FL的真实录音没有对应的逐音符velocity标签，并区别synthetic MIDI controls。追查`Chapter_6/figures/p3.jpg`、生成脚本、片段、标签字段和原记录。不得假定synthetic/pseudo-label/真实测量；未解决前不据此主张真实吉他velocity准确性。修订可能需要收窄/移除依赖主张，不承诺仅改caption。
2. **Ch4更新范围pending。** §2.5.4 p.28/PDF55称frozen front-end；§4.6.2 p.58/PDF85称retrain velocity branch与jointly trained counterpart。若实际代码/日志可得，核对optimizer参数组、requires_grad、模型边界、阶段、checkpoint及更新记录；否则保留pending，不补造实现。unchanged architecture不等于frozen weights。
3. **Ch5选择协议confirmed。** §5.6.1 p.75/PDF102与§5.7.3 p.80/PDF107明确：target dynamic F1挑multitask best fold，其他任务用同一checkpoint；single-task各任务独立挑best fold。无fine-tuning不等于source-only selection。表应解释为偏乐观transfer diagnostic。若可取得保留的per-fold outputs，可提出all-fold/source-selected汇总；不假称已经重分析，重跑需另获授权。

其余问题也要查实际资料：publication状态、Table2.7的43%和模态、Fig2.3颜色、数据统计口径、loss归一化/descriptor尺度等。不要为未知分母或图例编故事。代码/日志/数据仅在可访问、授权范围内读取；不要为了读PDF执行仓库脚本。

## 产出放在本细节层

建议创建：

- `01_逐项回应.md`：全部43项的证据映射与response。
- `02_拟修改英文.md`：自然、精确的英文替换段落或proposed edits；标明原文位置、拟文、理由、关联ID与证据。未获改原件授权时只提patch。
- `03_核查记录.md`：每个未决问题查到什么、仍缺什么，原资料路径/版本与结论强度。
- `04_改动摘要.md`：短change summary；分清proposed与实际完成，不称规划为已修订。
- `给导读的更新建议.md`：给中文层编辑的简短建议，按“原位置→建议怎样解释→新证据→确认/待确认”记录。

**不要覆盖`01_中文导读`。** 可读性编辑负责中文层的叙述、取舍和最终整合。也不要修改`blueprint_snapshot`；那是上一轮不可变的历史快照。未来Ultra产物与snapshot必须明显分开，不能让读者误以为快照已finalise。

## 主张与执行边界

中文说明使用MIDI力度值或音符级MIDI控制值（velocity），不译作速度；它不是物理演奏力度。beat为节拍，downbeat为小节首拍。描述renderer-conditioned目标时，写“优化目标是让指定合成链的响度表现更接近录音”，不要暗示对每段录音必然成功。

条件velocity completion不等于唯一恢复原演奏；已知notes/alignment的velocity refinement不等于完整AMT；设计理由、训练loss、测试metric、听测感知效益必须分开。Ch6须区分proxy fidelity、优化是否有用、重合成音频匹配和物理控制可识别性。loudness correlation不证明唯一true velocity或演奏力度。

先用准确说明、既有证据和合理收窄完成小修。第二份报告明确不要求新实验、新数据或major rewriting，但不能因此保留无支持的主张。只有重要主张无法支持也无法合理收窄时，才提出决定性实验，并先与用户/导师商定范围和资源；不自动训练。

不得捏造结果、数字、引用、显著性、实现动机或实验已完成。需要外部事实时核对primary sources，不把proposal写成既成事实。没有usable sources时只给位置明确的拟文，不把PDF-only编辑当作源文件修订。

最终交付应短而可审阅：完成/待确认清单、精确英文拟改、完整映射、change summary和给中文层的更新建议。不得覆盖原论文、push、发布、改变可见性、提交或联系他人，除非用户以后另行明确授权。
