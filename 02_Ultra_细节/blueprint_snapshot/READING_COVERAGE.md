# 本次实际阅读覆盖 / Coverage ledger

## 原始版本与页码

主版本 Zhanhong_He_PhD_Thesis_v0.pdf，154 PDF页。正文印刷p1–112 = PDF28–139，偏移+27。front matter标签有重复（如abstract i），不能一律加偏移。另两版均154页，但hash不同；逐页text差异见appendix/PDF_VERSION_DIFFERENCES.json。没有宣称三个PDF视觉等价或源码重建等价。

## 已完成

- 两份评审报告：各PDF1–4，完整文本、表格、页眉页脚、末页及全部页面渲染逐页检查。R1有手写签名、未见手写额外批评；R2无可见署名/签名。两报告均无PDF annotations，未见confidentiality限制。
- v0：封面PDF1；abstract PDF4；authorship PDF8；contents PDF10–14。
- v0正文：Ch1 pp1–8/PDF28–35；Ch2 pp9–38/PDF36–65；Ch3 pp39–50/PDF66–77；Ch4 pp51–66/PDF78–93；Ch5 pp67–84/PDF94–111；Ch6 pp85–104/PDF112–131；Ch7 pp105–112/PDF132–139。以上正文文本已逐段读取；p66/p84仅running heading/page number。
- v0额外视觉检查23页：PDF29,37,52,62,69,75,76,81,83,84,86,99,100,105,107,116,117,118,120,124,126,127,128。对应关键Figs1.1/2.1/2.3/3.2/4.2/4.4/5.2/6.1/6.2/6.3、loss equations、major tables。未把仅渲染但未查看的页面计为视觉检查。
- 所有5份PDF均完成page-labelled文本提取、metadata、PDF page count与annotation inventory；仅v0为深读基线。其他版本做逐页文本比较及main的局部问题比对，不宣称全篇深读另两版。
- LaTeX来源存在性/main include路径、相关Ch4/6段落与Fig6.3引用核对；仓库76个tracked文件均记录大小、SHA256和git blob；无LFS pointer。没有运行仓库脚本。

## 未做/仍有限

- 未逐页视觉检查完整154页；正文以文本深读加关键视觉检查，非全面版式proofread。
- 前置declaration/signatures/acknowledgements/acronym全页未逐页深读；PDF3/9 stamp对象已在manifest记录，但没有将其当作评审意见。
- References PDF140–154未逐项核验；没有外部论文/数据集/协议事实的独立检索。方法回答主要解释论文，不新增文献或SOTA断言。ISMIR状态目前只知报告声称accepted。
- 未取得或执行训练/评估代码，未检查原始ratings/folds/logs，未验证数值可复现，未运行新实验。
- 未编译LaTeX，未修改、提交、推送、发布或联系他人；没有自动启动Ultra。

## 本地提取物（未放入可分享规划zip）

/Users/jollibear/Documents/Codex/2026-10-22/task/reading/text/ 下有五份PDF的page-labelled .txt与逐页.json；报告文本文件为 Preliminary_Report_PhD_thesis_Zhanhong_He 1.txt / 2.txt。reading/report_pages/与reading/thesis_pages/仅为本地视觉核验缓存，不上传Library。最终规划包不包含原始PDF、原报告全文或浏览器截图。

## 技能/工具可用性

开始检查了可用document/PDF技能；本机没有专门PDF技能。随后parent提供的e0/builtins/pdf包在本runtime返回“skill package is not available”；这不是读取阻塞。使用task-local PyMuPDF提取、render与annotations检查，图像通过view_image逐页查看。research-to-obsidian与Library技能用于证据/交付规则；遵守明确指定Documents导出，不改Obsidian。
