# 实际做过什么，哪些判断改变了文字

本轮是独立新审查；未修改thesis、旧稿、作者DECISIONS、数据、图片或bibliography。没有实验、编译、提交、上传、外部grammar/LLM API、Git commit/push。

1. **先读真实来源。** 当前论文相关全文语境、Report1真实作者批注、已发表CMMR/ISMIR样本先于旧候选。PDFKit直接读取原PDF批注，确认Huber的实际措辞；非正式批注只用于意图，不仿写拼写/语法错误。共同署名论文提供既有学术语域，不能证明每句由作者独立写作或识别了个人语言指纹。
2. **完整重新筛选。** 机器抽取43组/97条旧路线；独立源头审查者逐组回看必要性、原稿优势、最低有效改动、事实依赖。其一度误以为R2-05 quote不匹配；主审指出:71和:358是两处，重核后撤回该误判。最终记录保留正确事实，不把误判当新发现。
3. **竞争而非盖通过章。** 15组关键段落共60个候选槽：原文/不增补、v4、两个实质新稿；N01–04的v4和原文相同，允许平局，不冒充不同稿。标签顺序随机，provenance key单独保存。来源可能被认出，只称label-hidden独立比较，不称双盲。
4. **第一轮独立比较C1。** 事实与语义先过硬门槛，再对回应/声音/必要性/拼接/清晰度分别作0–3序位判断，无总分、权重或小数。新T07备选因“which part ... caused”暗含未证实因果被淘汰；旧T11“did not conduct”超过真实批注，被退回。T10旧v4稿继续胜出。T04删重复应用句、T09恢复Second、N01–03要求整组同步，N07格式问题由此发现。
5. **返修和第二轮完整拼接C2。** 换一位独立读者，对15处选稿、5处小删改和N07共21项逐一反向释义，核对实际原段与相邻文字。20项接受，N01一处最小措辞修正：不同响应量尺的gap不能直接判定sensitivity；最终已修。C2不再假装盲评。两轮后停止增加改写，不做第三轮人为循环。
6. **最终来源完整性。** 所有非插入原文唯一匹配；插入项用明确源锚点和周围原文，不把“无新增段落”标记伪装成原句。12个源文件/PDF/真实回复快照的SHA-256全部未变。N07独立验证全部数字token顺序不变，只去12处数值强调和相关caption句。

## 工具与收益

- **Swift/macOS PDFKit：** 本地提取真实PDF和annotations；解决Huber原话与实验史措辞问题，不把PDF折行当语言错误。
- **开源Python标准库：** regex、hashlib、difflib、json；可重跑原文匹配、术语/重复检索、diff、来源哈希及table数值比较。脚本与JSON在`evidence/`及本目录。
- **prose length/term lint：** 标记回读处，不用于质量判决。八处长句提醒中，Ch5技术定义和分号列表仍可读，保留。
- **环境实际情况：** 系统无Vale、LanguageTool、textstat、Poppler等；workspace dependency tool返回本线程不可用。没有为凑工具使用而安装或运行未知来源代码。系统PDFKit与Python已足够完成实际检查。

## 可复核证据

- [全43组/97路线重新筛选](evidence/ALL_43_REAUDIT_INDEPENDENT.md)
- [匿名候选包C1](CANDIDATE_PACKET_BLIND_C1.md)；provenance仅供评分后核对：`evidence/provenance_key.json`
- [C1独立逐候选序位判断](evidence/BLIND_CRITIQUE_C1.md)
- [C2完整拼接包](CANDIDATE_PACKET_C2_REINSERTED.md)与[实际C2结果](evidence/CRITIQUE_C2.md)
- `evidence/real_pdf_author_annotations.txt`、`evidence/selected_quote_diff_checks.json`、`evidence/N07_table_markup_check.json`
- [最终哈希／引用／表值检查](evidence/FINAL_INTEGRITY_CHECK.json)
- [GRS原稿独立状态审查](evidence/tool_checks/grs_audit.md)

父级另有独立evaluator，以事先冻结的1–4六维rubric工作；那一轮不与本内部0–3判断混为同一个量尺。本文只报告实际运行的人工/程序检查，没有假称使用额外模型、grammar服务或客观quality评分。
